"""Wrap each gfx/src/SXX.html (style / body / script parts) into a standalone HyperFrames project gfx/SXX/."""
import json, shutil, sys, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
segs = {s["id"]: s for s in json.load(open(f"{ROOT}/work/segments.json", encoding="utf-8"))["segments"]}

def norm(w):
    return re.sub(r"[^\wÀ-ÿ%$]", "", w.lower())

def build(sid):
    s = segs[sid]
    src = open(f"{ROOT}/gfx/src/{sid}.html", encoding="utf-8").read()
    part = lambda tag: (re.search(rf"<{tag}>(.*?)</{tag}>", src, re.S) or [None, ""])[1]
    style, body, hud, script = part("style"), part("body"), part("hud"), part("script")
    dur = s["dur"]
    words = [dict(w=norm(w["w"]), t=round(w["ts"] - s["start"], 3), e=round(w["te"] - s["start"], 3)) for w in s["words"]]
    layout = {"B": "split", "C": "full", "A": "cam"}[s["layout"]]
    out = f"{ROOT}/gfx/{sid}"
    os.makedirs(out, exist_ok=True)
    if os.path.exists(f"{out}/shared"): shutil.rmtree(f"{out}/shared")
    shutil.copytree(f"{ROOT}/gfx/shared", f"{out}/shared")
    if os.path.exists(f"{ROOT}/gfx/assets"):
        if os.path.exists(f"{out}/assets"): shutil.rmtree(f"{out}/assets")
        shutil.copytree(f"{ROOT}/gfx/assets", f"{out}/assets")
    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<link rel="stylesheet" href="shared/base.css" />
<script src="shared/gsap.min.js"></script>
<script src="shared/cam.js"></script>
<style>{style}</style>
</head>
<body>
<div id="root" class="{layout}" data-composition-id="main" data-start="0" data-duration="{dur:.4f}" data-width="1080" data-height="1920" data-fps="240">
  <div id="stage" class="clip" data-start="0" data-duration="{dur:.4f}" data-track-index="0">
    <div id="world">{body}</div>
  </div>
  <div id="hud" class="clip" data-start="0" data-duration="{dur:.4f}" data-track-index="1" style="position:absolute;inset:0;">{hud}</div>
</div>
<script>
const D = {dur:.4f};
const WORDS = {json.dumps(words, ensure_ascii=False)};
// time of the n-th (0-based) occurrence of a word (normalized, prefix match)
function T(w, n) {{ n = n || 0; const m = WORDS.filter(x => x.w.startsWith(w)); if (!m[n]) throw new Error("word " + w); return m[n].t; }}
function TE(w, n) {{ n = n || 0; const m = WORDS.filter(x => x.w.startsWith(w)); return m[n].e; }}
const tl = gsap.timeline({{ paused: true }});
const world = document.getElementById("world");
{script}
tl.set({{}}, {{}}, D);
window.__timelines = window.__timelines || {{}};
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body>
</html>
"""
    open(f"{out}/index.html", "w", encoding="utf-8").write(html)
    json.dump({"id": sid, "name": sid}, open(f"{out}/meta.json", "w"))
    shutil.copy(f"{ROOT}/work/hftest/hyperframes.json", f"{out}/hyperframes.json")
    print("built", sid, f"{dur:.3f}s", layout)

for sid in (sys.argv[1:] or sorted(segs)):
    if os.path.exists(f"{ROOT}/gfx/src/{sid}.html"):
        build(sid)
