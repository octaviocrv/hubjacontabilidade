"""EDL definitivo a 60 fps (regras do Reel Pintor, revisao 3):
- inicio/fim real de cada frase por RMS (janelas de 10 ms, >= -35 dBFS)
- pre-roll 40 ms; pausa entre frases = 120 ms; pausas internas > 250 ms reduzidas a 120 ms
- J-cut de 50 ms: o audio da nova frase entra 50 ms antes da imagem
- "hold" (opcional, por segmento): segundos de imagem/som real mantidos depois da ultima fala
  (rev2: pausa de suspense da Malu antes da virada)
- camera (rev2): iPhone HLG BT.2100 -> SDR BT.709 pelo libplacebo com curva FIXA (spline, sem deteccao
  de pico por quadro, sem metadados Dolby Vision), mesma conversao em todos os takes; 60 fps exatos.
  A rev1 mantinha os pixels HLG e so trocava a matriz -> imagem lavada, sem contraste, pele palida.
- voz: passa-alta 80 Hz, compressao 2,2:1, -14 LUFS, limitador -2,2 dBFS

Entrada : 04_planos_de_cena/Politica_edl.json
Saidas  : <proj>/work/cam.mp4 (camera continua, sem audio), <proj>/work/voice.wav,
          <proj>/assets/timeline.json (trechos + pecas) e <proj>/assets/palavras.json
Uso: python montar_edl60.py <edl.json> <pasta_projeto>
"""
import json, os, re, subprocess, sys, wave
import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FPS, SR = 60, 48000
PRE, GAP, JCUT, THR = 0.04, 0.12, 0.05, -35.0
edl = json.load(open(sys.argv[1], encoding="utf-8"))
proj = sys.argv[2]
for d in ("work", "assets"):
    os.makedirs(os.path.join(proj, d), exist_ok=True)

def mov(src): return os.path.join(ROOT, "01_originais", "Video Politica", src + ".MOV")

_cache = {}
def audio(src):
    if src not in _cache:
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", mov(src), "-vn", "-ac", "1", "-ar", str(SR),
                              "-f", "s16le", "-"], capture_output=True, check=True).stdout
        _cache[src] = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    return _cache[src]

def rms_db(src, a, b):
    x = audio(src); w = int(SR * 0.01); i0, i1 = int(a * SR), int(b * SR)
    n = (i1 - i0) // w
    blk = x[i0:i0 + n * w].reshape(n, w)
    return a + np.arange(n) * 0.01, 20 * np.log10(np.sqrt((blk ** 2).mean(1)) + 1e-9)

def palavras(src):
    out = []
    for ln in open(os.path.join(ROOT, "03_transcricoes", f"{src}_palavras.txt"), encoding="utf-8"):
        m = re.match(r"\s*([\d.]+)\s*->\s*([\d.]+)\s+(.*)", ln)
        if m: out.append((float(m[1]), float(m[2]), m[3].strip()))
    return out

# 1) pecas de fala (on/off reais), quebrando pausas internas > 250 ms
pecas = []
for s in edl["segmentos"]:
    t, db = rms_db(s["src"], s["in"], s["out"])
    loud = db >= THR
    idx = np.where(loud)[0]
    on, off = t[idx[0]], t[idx[-1]] + 0.01
    # pausas internas
    runs, start = [], None
    for k in range(idx[0], idx[-1] + 1):
        if not loud[k] and start is None: start = k
        if loud[k] and start is not None:
            if (k - start) * 0.01 > 0.25: runs.append((t[start], t[k]))
            start = None
    cur = on
    for (p0, p1) in runs:
        pecas.append(dict(seg=s["id"], src=s["src"], on=cur, off=p0)); cur = p1
    pecas.append(dict(seg=s["id"], src=s["src"], on=cur, off=off))
    if s.get("hold"): pecas[-1]["hold"] = float(s["hold"])
    if s.get("quebra"):  # quebra de trecho dentro do segmento (mudanca de layout numa pausa curta)
        q = s["quebra"]
        for i, p in enumerate(pecas):
            if p["seg"] == s["id"] and p["on"] < q < p["off"]:
                tq, dq = rms_db(s["src"], q - 0.2, q + 0.2)
                sil = tq[dq < THR]
                a, b = sil.min(), sil.max() + 0.01
                pecas[i:i + 1] = [dict(p, off=a), dict(p, on=b, novo_trecho=True)]
                break

# 2) timeline de audio: cada peca = [on-PRE, off+(GAP-PRE)]
t = 0.0
for p in pecas:
    p["a_src"] = p["on"] - PRE
    p["a_len"] = (p["off"] - p["on"]) + GAP + p.get("hold", 0.0)
    p["a_t0"] = t; t += p["a_len"]
END = round(t * FPS) / FPS
pecas[-1]["a_len"] += END - t  # ultimo ajustado ao grid de quadros
# a ultima peca ganha cauda de imagem para o CTA respirar
TAIL = edl.get("cauda_final", 0.0)
pecas[-1]["a_len"] += TAIL; END += TAIL

# 3) timeline de imagem com J-cut (corte de imagem 50 ms depois do inicio do audio da peca)
for k, p in enumerate(pecas):
    p["v_t0"] = 0.0 if k == 0 else round((p["a_t0"] + JCUT) * FPS) / FPS
for k, p in enumerate(pecas):
    p["v_t1"] = pecas[k + 1]["v_t0"] if k + 1 < len(pecas) else END
    p["v_src"] = p["a_src"] + (p["v_t0"] - p["a_t0"])

# 4) camera: trims a 60 fps a partir do MOV original
inputs, filt = [], []
srcs = sorted({p["src"] for p in pecas})
for i, s in enumerate(srcs): inputs += ["-i", mov(s)]
for k, p in enumerate(pecas):
    i = srcs.index(p["src"])
    a, d = p["v_src"], p["v_t1"] - p["v_t0"]
    filt.append(f"[{i}:v]trim=start={a:.4f}:duration={d + 0.1:.4f},setpts=PTS-STARTPTS,fps={FPS},"
                f"trim=end_frame={round(d * FPS)},setpts=PTS-STARTPTS[v{k}]")
filt.append("".join(f"[v{k}]" for k in range(len(pecas))) + f"concat=n={len(pecas)}:v=1:a=0[vc]")
HLG2SDR = ("libplacebo=colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv:tonemapping=spline:"
           "gamut_mode=perceptual:peak_detect=0:contrast_recovery=0:apply_dolbyvision=0:dithering=blue:format=yuv420p")
filt.append(f"[vc]{HLG2SDR}[vo]")
cam = os.path.join(proj, "work", "cam.mp4")
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[vo]",
                "-c:v", "libx264", "-preset", "medium", "-crf", "10", "-g", "30", "-r", str(FPS),
                "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", cam], check=True)

# 5) voz: pecas com micro-fades (entrada 10 ms; saida ate 60 ms sem invadir a proxima)
voice = np.zeros(int(round(END * SR)) + SR, np.float32)
for p in pecas:
    x = audio(p["src"]); i0 = int(round(p["a_src"] * SR)); n = int(round(p["a_len"] * SR))
    seg = x[i0:i0 + n].copy()
    fi, fo = int(0.01 * SR), int(0.06 * SR)
    seg[:fi] *= np.linspace(0, 1, fi); seg[-fo:] *= np.linspace(1, 0, fo)
    o = int(round(p["a_t0"] * SR)); voice[o:o + len(seg)] += seg
voice = voice[:int(round(END * SR))]
raw = os.path.join(proj, "work", "voice_raw.wav")
with wave.open(raw, "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(voice, -1, 1) * 32767).astype(np.int16).tobytes())

def lufs(path):
    o = subprocess.run(["ffmpeg", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    o = o[o.rindex("Summary:"):]
    return float(re.search(r"I:\s+(-?[\d.]+) LUFS", o).group(1)), float(re.search(r"Peak:\s+(-?[\d.]+|-inf) dBFS", o).group(1))

comp = os.path.join(proj, "work", "voice_comp.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-af",
                "highpass=f=80,acompressor=threshold=-26dB:ratio=2.2:attack=8:release=140:makeup=1",
                "-ac", "2", "-c:a", "pcm_f32le", comp], check=True)
I, _ = lufs(comp)
out = os.path.join(proj, "work", "voice.wav")
for _ in range(3):  # ganho + limitador, ajustando ate -14,0 LUFS
    g = -14.0 - I
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", comp, "-af",
                    f"volume={g:.2f}dB,alimiter=limit={10 ** (-2.2 / 20):.4f}:attack=4:release=60:level=disabled",
                    "-ar", str(SR), "-c:a", "pcm_f32le", out], check=True)
    I2, tp = lufs(out)
    if abs(I2 + 14) < 0.15: break
    I -= (I2 + 14)

# 6) trechos (layout) e palavras no tempo editado
lay = edl["trechos"]
trechos, cur = [], None
for k, p in enumerate(pecas):
    if cur is None or p["seg"] != pecas[k - 1]["seg"] or p.get("novo_trecho"):
        key = p["seg"] + ("b" if p.get("novo_trecho") else "")
        if key in lay:
            cur = dict(id=lay[key][0], layout=lay[key][1], start=p["v_t0"], segs=[])
            trechos.append(cur)
    cur["segs"].append(p["seg"])
for i, tr in enumerate(trechos):
    tr["end"] = trechos[i + 1]["start"] if i + 1 < len(trechos) else END
    tr["dur"] = round(tr["end"] - tr["start"], 4)

words = []
for p in pecas:
    for (ws, we, w) in palavras(p["src"]):
        mid = (ws + we) / 2
        if p["on"] - 0.08 <= mid <= p["off"] + 0.08 or (ws < p["on"] < we and we - p["on"] > 0.1):
            s_ = p["a_t0"] + max(ws, p["on"]) - p["a_src"]; e_ = p["a_t0"] + min(we, p["off"]) - p["a_src"]
            words.append(dict(seg=p["seg"], w=w, s=round(s_, 3), e=round(max(e_, s_ + 0.06), 3)))

json.dump(dict(END=END, fps=FPS, trechos=trechos,
               pecas=[{k: (round(v, 4) if isinstance(v, float) else v) for k, v in p.items()} for p in pecas]),
          open(os.path.join(proj, "assets", "timeline.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(words, open(os.path.join(proj, "assets", "palavras.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"END {END:.4f}s ({round(END * FPS)} quadros) | voz {lufs(out)}")
for tr in trechos:
    print(f"  {tr['id']} {tr['layout']} {tr['start']:7.3f} -> {tr['end']:7.3f} ({tr['dur']:.2f}s) {tr['segs']}")
for p in pecas:
    print(f"    {p['seg']:3s} src {p['on']:.2f}-{p['off']:.2f}  audio@{p['a_t0']:.3f} video@{p['v_t0']:.3f}")
