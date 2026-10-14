"""Builds each segment's final 1080x1920@60 picture: A = camera, B = split (graphic + card + cut-out head), C = graphic."""
import json, os, subprocess, sys
CAM, SEGV = os.environ.get("CAM_DIR", "work/cam"), os.environ.get("SEGV_DIR", "work/segv")
GFXR = os.environ.get("GFXR_DIR", "work/gfxr")
S = {s["id"]: s for s in json.load(open("work/segments.json"))["segments"]}
SC, VW, VH, VX, VY = 1.2, 1296, 2304, -108, 100   # camera geometry for the split layout
ENC = ["-c:v", "libx264", "-crf", "8", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", "60"]
def run(args): subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)
for sid in (sys.argv[1:] or sorted(S)):
    s = S[sid]; n = s["f1"] - s["f0"]; out = f"{SEGV}/{sid}.mp4"
    if s["layout"] == "A":
        run(["-i", f"{CAM}/{sid}.mp4", "-frames:v", str(n), *ENC, out])
    elif s["layout"] == "C":
        run(["-i", f"{GFXR}/{sid}.mp4", "-frames:v", str(n), *ENC, out])
    else:
        fc = (
            f"[1:v]scale={VW}:{VH}:flags=lanczos,split[v1][v2];"
            # card: crop the card window from the scaled frame, clip with the superellipse mask
            f"[v1]crop=1210:864:{-65 - VX}:{1200 - VY},format=rgba[cv];[3:v]format=gray[cm];[cv][cm]alphamerge[card];"
            # cut-out head: SAME scaled frame + its matte, placed identically, feathered 40 px at the card top
            f"[2:v]format=rgba,alphaextract,scale={VW}:{VH}:flags=bicubic[ma];"
            f"[v2]crop=1080:{1920 - VY}:{-VX}:0,pad=1080:1920:0:{VY}:color=black,format=rgba[hv];"
            f"[ma]crop=1080:{1920 - VY}:{-VX}:0,pad=1080:1920:0:{VY}:color=black,format=gray[ha];"
            f"[5:v]format=gray[fe];[ha][fe]blend=all_mode=multiply,format=gray[hm];"
            f"[hv][hm]alphamerge[head];"
            f"[0:v]format=rgba[bg];[bg][4:v]overlay=0:0[b1];[b1][card]overlay=-65:1200[b2];[b2][head]overlay=0:0,format=yuv420p[o]"
        )
        run(["-i", f"{GFXR}/{sid}.mp4", "-i", f"{CAM}/{sid}.mp4", "-c:v", "libvpx-vp9", "-i", f"work/matte/{sid}.webm",
             "-loop", "1", "-i", "work/masks/card_mask.png", "-loop", "1", "-i", "work/masks/card_shadow.png",
             "-loop", "1", "-i", "work/masks/head_feather.png",
             "-filter_complex", fc, "-map", "[o]", "-frames:v", str(n), *ENC, out])
    nf = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", out], capture_output=True, text=True).stdout.strip()
    print(sid, s["layout"], "frames", nf, "expected", n)
