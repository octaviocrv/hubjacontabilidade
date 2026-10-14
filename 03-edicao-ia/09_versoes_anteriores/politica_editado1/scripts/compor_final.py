"""Composicao final do Reel Politica (ffmpeg, trecho a trecho como no compose.py do Reel Pintor).
A camera mantem os pixels originais; so e escalada/recortada nos trechos B.
  base  = work/gfx60.mp4 (fundo + graficos, 240->60 fps com motion blur)
  A     = camera em tela cheia (work/cam.mp4)
  B     = camera no cartao superior (mascara cantos inferiores r=200, mesma geometria do .camcard do HTML),
          escala/deslocamento do rastreio facial (work/enquadramento.json), interpolados por quadro
  C     = so graficos
  topo  = work/ovl.mov (legendas, selo, etiquetas da emenda, CTA, capa; com alfa)
  audio = work/master.wav (-14 LUFS)
Uso: python compor_final.py <pasta_projeto> <saida.mp4>
"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image

P, OUT = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
W, H, CARD_H, FPS = 1080, 1920, 960, 60
tl = json.load(open(os.path.join(P, "assets", "timeline.json"), encoding="utf-8"))
enq = json.load(open(os.path.join(P, "work", "enquadramento.json"), encoding="utf-8"))
SEG = os.path.join(P, "work", "segv"); os.makedirs(SEG, exist_ok=True)
ENC = ["-c:v", "libx264", "-profile:v", "high", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p",
       "-r", str(FPS), "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709"]

# mascara do cartao: retangulo x -65..1145, base y=960, cantos inferiores circulares r=200 (4x supersample)
S = 4
yy, xx = np.mgrid[0:CARD_H * S, 0:W * S] / S + 0.5 / S
m = np.ones_like(xx, dtype=bool)
for cx, side in ((-65 + 200, -1), (1145 - 200, 1)):
    corner = (yy > CARD_H - 200) & ((xx - cx) * side > 0)
    m &= ~corner | ((xx - cx) ** 2 + (yy - (CARD_H - 200)) ** 2 <= 200 ** 2)
alpha = m.reshape(CARD_H, S, W, S).mean((1, 3))
mask = os.path.join(P, "work", "card_mask.png")
Image.fromarray((alpha * 255).round().astype(np.uint8), "L").save(mask)

def piecewise(kf, col, a, lim):
    """deslocamento linear por partes em t (tempo local do trecho), negado e limitado ao quadro escalado"""
    expr = f"{-kf[-1][col]:.1f}"
    for i in range(len(kf) - 2, -1, -1):
        t0, t1 = kf[i][0] - a, kf[i + 1][0] - a
        v0, v1 = -kf[i][col], -kf[i + 1][col]
        if t1 - t0 < 1e-4: continue
        expr = f"if(lt(t,{t1:.4f}),{v0:.1f}+({v1 - v0:.1f})*(t-{t0:.4f})/{t1 - t0:.4f},{expr})"
    return f"max(0,min({lim},{expr}))"

def ff(args): subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)

lista = []
for t in tl["trechos"]:
    tid, a, b, lay = t["id"], t["start"], t["end"], t["layout"]
    n = round(b * FPS) - round(a * FPS)
    out = os.path.join(SEG, f"{tid}.mp4"); lista.append(out)
    ins = ["-ss", f"{a:.4f}", "-i", os.path.join(P, "work", "gfx60.mp4"),
           "-ss", f"{a:.4f}", "-i", os.path.join(P, "work", "cam.mp4"),
           "-ss", f"{a:.4f}", "-i", os.path.join(P, "work", "ovl.mov")]
    if lay == "A":
        fc = "[1:v]setpts=PTS-STARTPTS[c];[2:v]setpts=PTS-STARTPTS[o];[c][o]overlay=0:0:format=auto,format=yuv420p[v]"
    elif lay == "C":
        fc = "[0:v]setpts=PTS-STARTPTS[g];[2:v]setpts=PTS-STARTPTS[o];[g][o]overlay=0:0:format=auto,format=yuv420p[v]"
    else:
        e = enq[tid]; s = e["s"]; SW, SH = round(W * s / 2) * 2, round(H * s / 2) * 2
        x = piecewise(e["kf"], 1, a, SW - W); y = piecewise(e["kf"], 2, a, SH - CARD_H)
        ins += ["-loop", "1", "-framerate", str(FPS), "-i", mask]
        fc = (f"[0:v]setpts=PTS-STARTPTS[g];[2:v]setpts=PTS-STARTPTS[o];"
              f"[1:v]setpts=PTS-STARTPTS,scale={SW}:{SH}:flags=lanczos,crop={W}:{CARD_H}:x='{x}':y='{y}',format=yuva420p[k];"
              f"[3:v]format=gray[mk];[k][mk]alphamerge[card];"
              f"[g][card]overlay=0:0[gc];[gc][o]overlay=0:0:format=auto,format=yuv420p[v]")
    ff([*ins, "-filter_complex", fc, "-map", "[v]", "-frames:v", str(n), *ENC, "-an", out])
    nf = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", out],
                        capture_output=True, text=True).stdout.strip()
    print(f"{tid} {lay} quadros {nf} (esperado {n})", flush=True)

lst = os.path.join(SEG, "lista.txt")
open(lst, "w").write("".join(f"file '{p.replace(os.sep, '/')}'\n" for p in lista))
ff(["-f", "concat", "-safe", "0", "-i", lst, "-i", os.path.join(P, "work", "master.wav"),
    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-ac", "2",
    "-shortest", "-movflags", "+faststart", OUT])
print("ok", OUT)
