"""Gera as 3 saidas da composicao a partir de src/ (fonte unica):
  index.html -> previa completa p/ Studio (graficos + camera + voz)
  gfx.html   -> fundo + cenas (render 240 fps -> 60 fps com motion blur)
  ovl.html   -> legendas, selo, etiquetas da emenda, CTA, capa (render com alfa)
Uso: python build.py
"""
import json, os, re

D = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: open(os.path.join(D, p), encoding="utf-8").read()
tl = json.load(open(os.path.join(D, "assets", "timeline.json"), encoding="utf-8"))
enq = json.load(open(os.path.join(D, "work", "enquadramento.json"), encoding="utf-8"))
leg = json.load(open(os.path.join(D, "src", "legendas.json"), encoding="utf-8"))
aj = json.load(open(os.path.join(D, "src", "ajustes.json"), encoding="utf-8"))  # rev2
END = tl["END"]
TR = {t["id"]: dict(start=t["start"], end=t["end"], dur=t["dur"], layout=t["layout"]) for t in tl["trechos"]}

def preview():
    out = []
    for t in tl["trechos"]:
        tid, a, d = t["id"], t["start"], t["dur"]
        if t["layout"] == "A":
            out.append(f'<video id="cam{tid}" class="clip prev" src="work/cam.mp4" data-start="{a}" data-duration="{d}" '
                       f'data-media-start="{a}" data-track-index="2" muted playsinline style="width:1080px;height:1920px;"></video>')
        elif t["layout"] == "B":
            e = enq[tid]; s = e["s"]; _, ox, oy = e["kf"][len(e["kf"]) // 2]
            out.append(f'<div id="pv{tid}" class="camcard prev" style="opacity:0;z-index:2;">'
                       f'<video id="cam{tid}" src="work/cam.mp4" data-start="{a}" data-duration="{d}" data-media-start="{a}" '
                       f'data-track-index="2" muted playsinline style="transform:translate({ox + 65:.1f}px,{oy + 400:.1f}px) scale({s});"></video></div>')
    out.append(f'<audio id="vozprev" class="prev" src="work/{"master.wav" if os.path.exists(os.path.join(D, "work", "master.wav")) else "voice.wav"}" '
               f'data-start="0" data-duration="{END}" data-track-index="20" data-volume="1"></audio>')
    return "\n".join(out)

def page(layer):
    body = rd("src/body.html").replace("{{END}}", str(END))
    body = body.replace("{{PREVIEW}}", preview() if layer == "prev" else "")
    body = re.sub(r'data-trecho="(S\d+)"', lambda m: f'data-start="{TR[m[1]]["start"]}" data-duration="{TR[m[1]]["dur"]}"', body)
    js = rd("src/main.js")
    if layer == "prev":  # mostra o cartao da camera de cada trecho B
        js = js.replace("root.set({}, {}, END);", "".join(
            f'root.set("#pv{k}", {{ opacity: 1 }}, {v["start"]}); root.set("#pv{k}", {{ opacity: 0 }}, {v["end"] - 0.005});\n'
            for k, v in TR.items() if v["layout"] == "B") + "root.set({}, {}, END);")
    cls = {"prev": "L-prev", "gfx": "L-gfx", "ovl": "L-ovl"}[layer]
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<title>JA · Eleições e impostos ({layer})</title>
<script src="assets/lib/gsap.min.js"></script>
<style>
{rd("src/style.css")}
</style>
</head>
<body>
<div id="root" class="{cls}" data-composition-id="main" data-start="0" data-duration="{END}" data-width="1080" data-height="1920">
{body}
</div>
<script>
const TR = {json.dumps(TR)};
const LEG = {json.dumps(leg, ensure_ascii=False)};
const AJ = {json.dumps(aj, ensure_ascii=False)};
const END = {END};
const LAYER = "{layer}";
{js}
</script>
</body>
</html>
"""

import shutil
open(os.path.join(D, "index.html"), "w", encoding="utf-8").write(page("prev"))
for layer in ("gfx", "ovl"):  # cada camada de render e um projeto proprio (uma raiz por pasta)
    L = os.path.join(D, "layers", layer)
    os.makedirs(L, exist_ok=True)
    for sub in ("fontes", "lib"):
        shutil.copytree(os.path.join(D, "assets", sub), os.path.join(L, "assets", sub), dirs_exist_ok=True)
    for f in ("logo_badge.png", "logo_dourado.jpg"):
        shutil.copy(os.path.join(D, "assets", f), os.path.join(L, "assets", f))
    shutil.copy(os.path.join(D, "hyperframes.json"), L)
    open(os.path.join(L, "index.html"), "w", encoding="utf-8").write(page(layer))
print("ok", END, list(TR))
