"""Monta o A-roll (apresentadores) a partir do EDL: corta cada frase do proxy,
aplica micro-fade de audio nas emendas, concatena e normaliza loudness (-14 LUFS).

Saidas:
  <projeto>/assets/aroll.mp4         video 1080x1920 30fps + audio
  <projeto>/assets/timeline.json     inicio/fim de cada segmento no tempo editado
  <projeto>/assets/palavras.json     palavras da transcricao remapeadas p/ tempo editado

Uso: python montar_aroll.py <edl.json> <pasta_projeto>
"""
import json, subprocess, sys, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FPS = 30
FADE = 0.015

edl = json.load(open(sys.argv[1], encoding="utf-8"))
proj = sys.argv[2]
os.makedirs(os.path.join(proj, "assets"), exist_ok=True)

def snap(t):
    return round(t * FPS) / FPS

def palavras(src):
    out = []
    for ln in open(os.path.join(ROOT, "03_transcricoes", f"{src}_palavras.txt"), encoding="utf-8"):
        m = re.match(r"\s*([\d.]+)\s*->\s*([\d.]+)\s+(.*)", ln)
        if m:
            out.append((float(m[1]), float(m[2]), m[3].strip()))
    return out

inputs, filt, tl, words = [], [], [], []
t = 0.0
for i, s in enumerate(edl["segmentos"]):
    a, b = snap(s["in"]), snap(s["out"])
    d = b - a
    inputs += ["-i", os.path.join(ROOT, "05_assets", "proxies", s["src"] + ".mp4")]
    filt.append(f"[{i}:v]trim=start={a}:end={b},setpts=PTS-STARTPTS,fps={FPS}[v{i}]")
    filt.append(
        f"[{i}:a]atrim=start={a}:end={b},asetpts=PTS-STARTPTS,"
        f"afade=t=in:d={FADE},afade=t=out:st={d - FADE:.3f}:d={FADE}[a{i}]"
    )
    tl.append({"id": s["id"], "src": s["src"], "start": round(t, 4), "end": round(t + d, 4),
               "srcIn": a, "fala": s["fala"]})
    for (ws, we, w) in palavras(s["src"]):
        if ws >= a - 0.05 and we <= b + 0.15:
            words.append({"seg": s["id"], "w": w,
                          "s": round(max(t, t + ws - a), 3), "e": round(min(t + d, t + we - a), 3)})
    t += d

n = len(edl["segmentos"])
filt.append("".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[vc][ac]")
filt.append("[ac]highpass=f=80,loudnorm=I=-14:TP=-1.5:LRA=9[ao]")

out = os.path.join(proj, "assets", "aroll.mp4")
cmd = ["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(filt),
       "-map", "[vc]", "-map", "[ao]", "-c:v", "libx264", "-preset", "medium", "-crf", "15",
       "-g", "15", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", out]
subprocess.run(cmd, check=True)

json.dump({"duracao": round(t, 4), "segmentos": tl}, open(os.path.join(proj, "assets", "timeline.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(words, open(os.path.join(proj, "assets", "palavras.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"A-roll: {t:.2f}s, {len(words)} palavras -> {out}")
for s in tl:
    print(f"  {s['id']:3s} {s['start']:6.2f} -> {s['end']:6.2f}  {s['fala'][:60]}")
