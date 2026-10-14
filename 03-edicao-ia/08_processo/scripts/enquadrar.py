"""Enquadramento da camera no cartao do Layout B (apresentador em cima, graficos embaixo).

Rastreia o rosto (YuNet) em work/cam.mp4 nos trechos B e gera, por trecho, a escala e um
deslocamento suave (operador virtual: gaussiana forte, sem atravessar cortes) que mantem o
rosto em (540, ALVO_Y) dentro do cartao de 1080 x CARD_H. Tambem mede, nos trechos A, a
luminancia sob a legenda para escolher branco ou grafite e (rev2) o rosto em tela cheia:
centro/altura medianos e o topo do rosto mais alto, usados no zoom de suspense (S03) e na
legenda acima da cabeca.

Saida: work/enquadramento.json
Uso: python enquadrar.py <pasta_projeto>
"""
import cv2, json, os, sys
import numpy as np

proj = sys.argv[1]
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CARD_H, ALVO_Y, ALVO_FH = 960, 545, 300
S_MIN, S_MAX = 1.08, 1.30
tl = json.load(open(os.path.join(proj, "assets", "timeline.json"), encoding="utf-8"))
det = cv2.FaceDetectorYN.create(os.path.join(ROOT, "05_assets", "modelos", "face_yunet.onnx"), "", (540, 960), 0.6, 0.3, 5000)
cap = cv2.VideoCapture(os.path.join(proj, "work", "cam.mp4"))
fps = cap.get(cv2.CAP_PROP_FPS)

frames = {}
i = 0
while True:
    ok, f = cap.read()
    if not ok: break
    t = i / fps; i += 1
    if i % 3: continue  # 20 amostras/s
    tr = next(x for x in tl["trechos"] if x["start"] <= t < x["end"] + 1e-6)
    if tr["layout"] == "B":
        _, faces = det.detect(cv2.resize(f, (540, 960)))
        if faces is not None and len(faces):
            fc = max(faces, key=lambda r: r[2] * r[3])
            x, y, w, h = fc[:4] * 2
            frames.setdefault(tr["id"], []).append((t, x + w / 2, y + h / 2, h))
    elif tr["layout"] == "A":
        y0 = 1401 - 40
        lum = cv2.cvtColor(f[y0:y0 + 80, 240:840], cv2.COLOR_BGR2GRAY).mean() / 255
        frames.setdefault(tr["id"], []).append((t, lum))
        _, faces = det.detect(cv2.resize(f, (540, 960)))
        if faces is not None and len(faces):
            fc = max(faces, key=lambda r: r[2] * r[3])
            x, y, w, h = fc[:4] * 2
            frames.setdefault(tr["id"] + "_rosto", []).append((t, x + w / 2, y + h / 2, h, y))

def gauss(a, sigma):
    r = int(sigma * 3); k = np.exp(-0.5 * (np.arange(-r, r + 1) / sigma) ** 2); k /= k.sum()
    return np.convolve(np.pad(a, r, mode="edge"), k, mode="valid")

out = {}
for tr in tl["trechos"]:
    d = np.array(frames.get(tr["id"], []))
    if tr["layout"] == "A":
        out[tr["id"]] = dict(layout="A", lum=round(float(d[:, 1].mean()), 3), lum_max=round(float(d[:, 1].max()), 3))
        r = np.array(frames.get(tr["id"] + "_rosto", []))
        if len(r):
            out[tr["id"]]["rosto"] = dict(cx=round(float(np.median(r[:, 1])), 1), cy=round(float(np.median(r[:, 2])), 1),
                                          h=round(float(np.median(r[:, 3])), 1), topo_min=round(float(r[:, 4].min()), 1))
        continue
    if tr["layout"] != "B": continue
    t, cx, cy, fh = d.T
    s = float(np.clip(ALVO_FH / np.median(fh), S_MIN, S_MAX))
    cx, cy = gauss(cx, 14), gauss(cy, 10)  # ~0,7 s / 0,5 s
    ox = np.clip(540 - cx * s, 1080 - 1080 * s, 0)
    oy = np.clip(ALVO_Y - cy * s, CARD_H - 1920 * s, 0)
    kf = [[round(float(a), 3), round(float(b), 1), round(float(c), 1)] for a, b, c in zip(t, ox, oy)][::5]  # a cada 0,25 s
    kf[0][0] = tr["start"]; kf.append([tr["end"], kf[-1][1], kf[-1][2]])
    out[tr["id"]] = dict(layout="B", s=round(s, 3), kf=kf,
                         face_y=[round(float(cy.min() * s + oy.min())), round(float(cy.max() * s + oy.max()))])
    print(tr["id"], "B escala %.3f" % s, "rosto cy %d-%d" % (cy.min(), cy.max()), "kf", len(kf))
for k, v in out.items():
    if v["layout"] == "A": print(k, "A lum legenda %.2f (max %.2f)" % (v["lum"], v["lum_max"]), v.get("rosto"))
json.dump(out, open(os.path.join(proj, "work", "enquadramento.json"), "w"), indent=1)
