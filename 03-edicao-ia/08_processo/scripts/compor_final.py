"""Composicao final do Reel Politica (ffmpeg, trecho a trecho como no compose.py do Reel Pintor).
A camera chega do montar_edl60.py ja convertida HLG -> SDR BT.709; aqui so e escalada/recortada.
  base  = work/gfx60.mp4 (fundo + graficos, 240->60 fps com motion blur)
  A     = camera em tela cheia (work/cam.mp4)
  B     = camera no cartao superior (mascara cantos inferiores r=200, mesma geometria do .camcard do HTML),
          escala/deslocamento do rastreio facial (work/enquadramento.json), interpolados por quadro
  C     = so graficos
  topo  = work/ovl.mov (legendas, selo, etiquetas da emenda, CTA; com alfa)
  audio = work/master.wav (-14 LUFS)
Rev2 (src/ajustes.json):
  suspense (S03) = zoom progressivo ancorado no rosto durante a duvida; nos ultimos `whip` s acelera
                   (zoom-through) com motion blur de obturador 180 graus (subamostras). Legenda/selo nao zoomam.
  virada   (S04) = o quadro (graficos + cartao, sem o ovl) chega ampliado e assenta em 1,0 (power3.out),
                   com o mesmo motion blur: continuidade do zoom-through.
  O arquivo final leva as tags BT.709 (antes ficavam 'unknown').
Uso: python compor_final.py <pasta_projeto> <saida.mp4>
"""
import json, math, os, subprocess, sys
import numpy as np
import cv2
from PIL import Image

P, OUT = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
W, H, CARD_H, FPS = 1080, 1920, 960, 60
tl = json.load(open(os.path.join(P, "assets", "timeline.json"), encoding="utf-8"))
enq = json.load(open(os.path.join(P, "work", "enquadramento.json"), encoding="utf-8"))
AJ = json.load(open(os.path.join(P, "src", "ajustes.json"), encoding="utf-8"))
TRS = {t["id"]: t for t in tl["trechos"]}
SEG = os.path.join(P, "work", "segv"); os.makedirs(SEG, exist_ok=True)
ENC = ["-c:v", "libx264", "-profile:v", "high", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p",
       "-r", str(FPS), "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709"]
TO_RGB = "zscale=matrixin=709:rangein=limited:range=full,format=rgb24"
TO_YUV = "zscale=matrix=709:rangein=full:range=limited:dither=error_diffusion,format=yuv420p"

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

# ---------------- movimentos de camera da rev2 ----------------
def cam_suspense(t):
    """(escala, foco na fonte, posicao na saida) do S03"""
    su = AJ["suspense"]; a = TRS["S03"]["start"]; e = TRS["S03"]["end"]; wb = e - su["whip"]
    F = np.array(su["foco"], float); O1 = np.array(su["destino"], float); z1 = su["zoom"]
    if t <= wb:  # aproximacao que cresce com a duvida (ease-in suave)
        p = np.clip((t - a) / (wb - a), 0, 1) ** 1.6
        return 1 + (z1 - 1) * p, F, F + (O1 - F) * p
    u = np.clip((t - wb) / su["whip"], 0, 1)  # aceleracao final, emendada em C1 na velocidade da aproximacao
    v0 = 1.6 * (z1 - 1) / (wb - a) * su["whip"]
    return z1 + v0 * u + (su["whip_zoom"] - z1 - v0) * u ** 3, F, O1

def cam_virada(t):
    vi = AJ["virada"]; a = TRS["S04"]["start"]
    u = np.clip((t - a) / vi["dur"], 0, 1)
    F = np.array(vi["foco"], float)
    return 1 + (vi["zoom"] - 1) * (1 - u) ** 3, F, F

def warp(img, s, F, O, interp):
    M = np.array([[s, 0, O[0] - s * F[0]], [0, s, O[1] - s * F[1]]], np.float32)
    return cv2.warpAffine(img, M, (W, H), flags=interp, borderMode=cv2.BORDER_REPLICATE)

def com_movimento(frame, t, cam):
    """aplica a camera virtual com motion blur de obturador 180 graus (subamostras proporcionais a velocidade)"""
    s, F, O = cam(t)
    s1, _, _ = cam(t + 1 / (4 * FPS)); s0, _, _ = cam(t - 1 / (4 * FPS))
    desloc = abs(s1 - s0) * 1100  # px percorridos na borda do quadro durante o obturador
    k = int(np.clip(math.ceil(desloc / 1.5), 1, 24))
    if k == 1:
        return warp(frame, s, F, O, cv2.INTER_LANCZOS4) if abs(s - 1) > 1e-4 else frame
    acc = np.zeros(frame.shape, np.float32)
    for j in range(k):
        tj = t + (j + 0.5) / k / (2 * FPS) - 1 / (4 * FPS)
        sj, Fj, Oj = cam(tj)
        acc += warp(frame, sj, Fj, Oj, cv2.INTER_LINEAR)
    return np.clip(acc / k + 0.5, 0, 255).astype(np.uint8)

def trecho_com_camera(tid, a, n, base_ins, base_fc, cam, out):
    """base (sem ovl) -> RGB -> camera virtual em Python -> ovl por cima -> segmento"""
    rd = subprocess.Popen(["ffmpeg", "-v", "error", *base_ins, "-filter_complex", f"{base_fc};[base]{TO_RGB}[rgb]",
                           "-map", "[rgb]", "-frames:v", str(n), "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
    wr = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-ss", f"{a:.4f}", "-i", os.path.join(P, "work", "ovl.mov"),
                           "-filter_complex", f"[0:v]{TO_YUV}[c];[1:v]setpts=PTS-STARTPTS[o];[c][o]overlay=0:0:format=auto,format=yuv420p[v]",
                           "-map", "[v]", "-frames:v", str(n), *ENC, "-an", out], stdin=subprocess.PIPE)
    sz = W * H * 3
    for i in range(n):
        buf = rd.stdout.read(sz)
        if len(buf) < sz: raise RuntimeError(f"{tid}: faltou quadro {i}")
        fr = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
        wr.stdin.write(com_movimento(fr, a + i / FPS, cam).tobytes())
    wr.stdin.close(); rd.wait(); wr.wait()
    if rd.returncode or wr.returncode: raise RuntimeError(f"{tid}: ffmpeg falhou")

CAM = {AJ["suspense"]["trecho"]: cam_suspense, AJ["virada"]["trecho"]: cam_virada}
lista = []
for t in tl["trechos"]:
    tid, a, b, lay = t["id"], t["start"], t["end"], t["layout"]
    n = round(b * FPS) - round(a * FPS)
    out = os.path.join(SEG, f"{tid}.mp4"); lista.append(out)
    ins = ["-ss", f"{a:.4f}", "-i", os.path.join(P, "work", "gfx60.mp4"),
           "-ss", f"{a:.4f}", "-i", os.path.join(P, "work", "cam.mp4"),
           "-ss", f"{a:.4f}", "-i", os.path.join(P, "work", "ovl.mov")]
    if lay == "A":
        base = "[1:v]setpts=PTS-STARTPTS[base]"
    elif lay == "C":
        base = "[0:v]setpts=PTS-STARTPTS[base]"
    else:
        e = enq[tid]; s = e["s"]; SW, SH = round(W * s / 2) * 2, round(H * s / 2) * 2
        x = piecewise(e["kf"], 1, a, SW - W); y = piecewise(e["kf"], 2, a, SH - CARD_H)
        ins += ["-loop", "1", "-framerate", str(FPS), "-i", mask]
        base = (f"[0:v]setpts=PTS-STARTPTS[g];"
                f"[1:v]setpts=PTS-STARTPTS,scale={SW}:{SH}:flags=lanczos,crop={W}:{CARD_H}:x='{x}':y='{y}',format=yuva420p[k];"
                f"[3:v]format=gray[mk];[k][mk]alphamerge[card];[g][card]overlay=0:0[base]")
    if tid in CAM:
        trecho_com_camera(tid, a, n, ins, base, CAM[tid], out)
    else:
        fc = f"{base};[2:v]setpts=PTS-STARTPTS[o];[base][o]overlay=0:0:format=auto,format=yuv420p[v]"
        ff([*ins, "-filter_complex", fc, "-map", "[v]", "-frames:v", str(n), *ENC, "-an", out])
    nf = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", out],
                        capture_output=True, text=True).stdout.strip()
    print(f"{tid} {lay} quadros {nf} (esperado {n})" + (" + camera virtual" if tid in CAM else ""), flush=True)

lst = os.path.join(SEG, "lista.txt")
open(lst, "w").write("".join(f"file '{p.replace(os.sep, '/')}'\n" for p in lista))
ff(["-f", "concat", "-safe", "0", "-i", lst, "-i", os.path.join(P, "work", "master.wav"),
    "-map", "0:v", "-map", "1:a", "-c:v", "copy",
    "-bsf:v", "h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1:video_full_range_flag=0",
    "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-ac", "2",
    "-shortest", "-movflags", "+faststart", OUT])
print("ok", OUT)
