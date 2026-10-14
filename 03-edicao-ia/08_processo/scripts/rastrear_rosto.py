"""Rastreia o rosto no A-roll (YuNet) e gera keyframes suavizados de enquadramento
para a metade superior da tela dividida.

Saida: <projeto>/assets/rosto.json  ->  {"fps":10, "segmentos":[{"id","start","end","kf":[[t,cx,cy,fh],...]}]}
  cx, cy = centro do rosto em px do quadro 1080x1920; fh = altura do rosto em px.
A suavizacao e feita por segmento (nunca atravessa um corte), simulando um
operador de camera: filtro gaussiano + zona morta.

Uso: python rastrear_rosto.py <pasta_projeto>
"""
import cv2, json, os, sys
import numpy as np

proj = sys.argv[1]
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
model = os.path.join(ROOT, "05_assets", "modelos", "face_yunet.onnx")
tl = json.load(open(os.path.join(proj, "assets", "timeline.json"), encoding="utf-8"))

STEP = 1 / 10
W, H = 540, 960  # deteccao em meia resolucao
det = cv2.FaceDetectorYN.create(model, "", (W, H), 0.6, 0.3, 5000)
cap = cv2.VideoCapture(os.path.join(proj, "assets", "aroll.mp4"))
fps = cap.get(cv2.CAP_PROP_FPS)

raw = []  # (t, cx, cy, fh) ou None
i = 0
next_t = 0.0
while True:
    ok, frame = cap.read()
    if not ok:
        break
    t = i / fps
    i += 1
    if t + 1e-6 < next_t:
        continue
    next_t += STEP
    small = cv2.resize(frame, (W, H))
    _, faces = det.detect(small)
    if faces is None or len(faces) == 0:
        raw.append((t, None))
        continue
    # maior rosto (mais proximo da camera)
    f = max(faces, key=lambda r: r[2] * r[3])
    x, y, w, h = f[:4] * 2
    raw.append((t, (x + w / 2, y + h / 2, h)))

def gauss(arr, sigma):
    if len(arr) < 3:
        return arr
    r = int(sigma * 3)
    k = np.exp(-0.5 * (np.arange(-r, r + 1) / sigma) ** 2); k /= k.sum()
    pad = np.pad(arr, r, mode="edge")
    return np.convolve(pad, k, mode="valid")

out = []
for s in tl["segmentos"]:
    pts = [(t, v) for (t, v) in raw if s["start"] - 1e-6 <= t < s["end"]]
    ts = np.array([p[0] for p in pts])
    vals = np.array([p[1] if p[1] is not None else (np.nan,) * 3 for p in pts], dtype=float)
    for c in range(3):  # interpola falhas de deteccao
        col = vals[:, c]; good = ~np.isnan(col)
        if good.sum() == 0:
            col[:] = [540, 700, 200][c]
        else:
            col[~good] = np.interp(ts[~good], ts[good], col[good])
        vals[:, c] = col
    # operador virtual: suavizacao forte na posicao, mais forte ainda no tamanho
    cx = gauss(vals[:, 0], 6); cy = gauss(vals[:, 1], 6); fh = gauss(vals[:, 2], 10)
    kf = [[round(float(t), 2), round(float(a)), round(float(b)), round(float(c))]
          for t, a, b, c in zip(ts, cx, cy, fh)]
    out.append({"id": s["id"], "start": s["start"], "end": s["end"], "kf": kf,
                "detectado": f"{int((~np.isnan(np.array([p[1][0] if p[1] else np.nan for p in pts]))).sum())}/{len(pts)}"})
    print(s["id"], out[-1]["detectado"], "cx %d-%d cy %d-%d fh %d-%d" % (cx.min(), cx.max(), cy.min(), cy.max(), fh.min(), fh.max()))

json.dump({"fps": 10, "segmentos": out}, open(os.path.join(proj, "assets", "rosto.json"), "w"), indent=0)
