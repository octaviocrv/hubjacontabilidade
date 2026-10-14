"""Rev 5 sound pass: keeps every existing SFX of stems/sfx.wav, replaces only the generic impact under the
"EXCLUSÃO" stamp (3.430 s) with a real stamp slam, and adds SFX on every animation that had none.
Voice, riser and music stems are copied untouched. Output: stems5/*.wav, work/master5.wav, work/sfx5_log.json."""
import json, os, shutil, subprocess, re, numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve

SR = 48000
os.makedirs("stems5", exist_ok=True)
voice, sr = sf.read("stems/voice.wav", dtype="float64"); assert sr == SR
sfx, _ = sf.read("stems/sfx.wav", dtype="float64")
N = len(voice)
VPK = 20 * np.log10(np.abs(voice).max())
rng = np.random.default_rng(11)

def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], "bandpass", fs=SR, output="sos"), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, "lowpass", fs=SR, output="sos"), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, "highpass", fs=SR, output="sos"), x)
def env(n, tau): return np.exp(-np.arange(n) / (tau * SR))
def at_peak(x, db): return x / np.abs(x).max() * 10 ** ((VPK + db) / 20)
def sweep_noise(n, lo0, hi0, lo1, hi1, curve=None):
    noise = rng.standard_normal(n); out = np.zeros(n); hop = 512
    for s in range(0, n, hop):
        p = s / n; w = curve(p) if curve else p
        lo = lo0 + (lo1 - lo0) * w; hi = hi0 + (hi1 - hi0) * w
        blk = bp(noise[max(0, s - 2048):s + hop], lo, hi)[-min(hop, n - s):]
        out[s:s + len(blk)] = blk
    return out
def room(x, t=0.35, mix=0.18):
    n = int(t * 3 * SR); ir = rng.standard_normal(n) * env(n, t / 2.5); ir = lp(hp(ir, 300), 7000)
    y = fftconvolve(x, ir)[:len(x) + n]; y = y / np.abs(y).max() * np.abs(x).max()
    out = np.zeros(len(y)); out[:len(x)] = x
    return out * (1 - mix) + y * mix

# ------------------------------------------------------------------ sound designs
def swish(L=0.42, peak=0.5, lo=(400, 1500), hi=(1800, 6500), width=0.22):
    """airy pass-by; returns (signal, index of the energy peak)"""
    n = int(L * SR); t = np.arange(n) / SR
    a = np.exp(-((t - peak * L) / (width * L)) ** 2)
    x = sweep_noise(n, lo[0], lo[1], hi[0], hi[1], curve=lambda p: np.sin(np.pi * min(p / peak, 1) / 2) if p < peak else 1 - 0.4 * (p - peak)) * a
    return x, int(peak * n)
def swish_up():   # rising pass for the news card entrance
    n = int(0.5 * SR); t = np.arange(n) / SR
    a = np.minimum(1, t / 0.18) ** 2 * np.exp(-np.maximum(0, t - 0.24) / 0.07)
    return sweep_noise(n, 250, 900, 1800, 7000, curve=lambda p: p ** 1.5) * a
def land():       # soft card landing
    n = int(0.25 * SR); t = np.arange(n) / SR
    f = 70 + 60 * np.exp(-t / 0.03)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.06) * np.minimum(1, t / 0.002)
    tap = bp(rng.standard_normal(n), 800, 3500) * env(n, 0.008)
    return lp(body + 0.25 * tap / np.abs(tap).max(), 2500)
def line_tick(i):
    n = int(0.03 * SR); t = np.arange(n) / SR
    return bp(rng.standard_normal(n), 3000, 9000) * env(n, 0.004) + 0.3 * np.sin(2 * np.pi * (2400 + 180 * i) * t) * env(n, 0.006)
def stamp():
    """rubber stamp slammed on paper: 160 ms down-swoosh, sharp contact crack, wooden thock, paper slap, sub weight"""
    pre = int(0.16 * SR); n = int(0.9 * SR); x = np.zeros(pre + n)
    t = np.arange(pre) / SR
    x[:pre] += 0.22 * sweep_noise(pre, 1500, 5000, 300, 1400) * (t / t[-1]) ** 2.5
    t = np.arange(n) / SR
    crack = hp(rng.standard_normal(n), 1800, 4) * env(n, 0.0025)
    thock = bp(rng.standard_normal(n), 160, 700, 3) * env(n, 0.035)
    wood = (np.sin(2 * np.pi * 185 * t) + 0.5 * np.sin(2 * np.pi * 410 * t)) * env(n, 0.05) * np.minimum(1, t / 0.0008)
    slap = bp(rng.standard_normal(n), 2000, 8000) * env(n, 0.018)
    f = 42 + 50 * np.exp(-t / 0.04)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.22) * np.minimum(1, t / 0.002)
    hit = (0.55 * crack / np.abs(crack).max() + 0.9 * thock / np.abs(thock).max() + 0.6 * wood / np.abs(wood).max()
           + 0.35 * slap / np.abs(slap).max() + 0.8 * sub)
    x[pre:] += room(hit, 0.3, 0.14)[:n]
    return x, pre
def denied():     # short descending two-tone "negative" cue for the "Termo de Exclusão" tag
    n = int(0.5 * SR); out = np.zeros(n)
    for k, (f, off) in enumerate([(587.3, 0.0), (440.0, 0.11)]):
        o = int(off * SR); m = n - o; t = np.arange(m) / SR
        a = np.minimum(1, t / 0.004) * env(m, 0.09)
        tone = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t) + 0.12 * np.sin(2 * np.pi * 3 * f * t)
        out[o:] += lp(tone * a, 3500) * (0.9 if k == 0 else 1.0)
    return out
def roller(L=0.3):  # paint roller stroke: sticky, rolling texture
    n = int(L * SR); t = np.arange(n) / SR
    a = np.sin(np.pi * t / L) ** 1.2
    tex = bp(rng.standard_normal(n), 250, 1600) * (0.65 + 0.35 * np.sin(2 * np.pi * 34 * t + rng.uniform(0, 6)))
    crackle = bp(rng.standard_normal(n) * (rng.random(n) < 0.02), 2000, 6000)
    return tex * a + 0.4 * crackle * a
def paper():      # paper slip flicked away
    n = int(0.18 * SR); t = np.arange(n) / SR
    a = np.minimum(1, t / 0.006) * env(n, 0.045)
    return sweep_noise(n, 1200, 6000, 2500, 9000) * a
def pop(f0=950):
    n = int(0.09 * SR); t = np.arange(n) / SR
    f = f0 * (0.55 + 0.45 * np.exp(-t / 0.018))
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.03) * np.minimum(1, t / 0.0015)
    return body + 0.25 * bp(rng.standard_normal(n), 2500, 8000) * env(n, 0.004)
def marker(L):    # felt-tip highlighter swipe
    n = int(L * SR); t = np.arange(n) / SR
    a = np.minimum(1, t / 0.03) * np.minimum(1, (L - t) / 0.06)
    grain = 0.7 + 0.3 * lp(rng.standard_normal(n), 60) / 0.05
    return bp(rng.standard_normal(n), 1800, 6000) * a * np.clip(grain, 0.2, 1.6)
def coin(f, tau=0.09):  # small metallic coin "tink" (inharmonic partials)
    n = int(tau * 4 * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for k, (r, g) in enumerate([(1, 1), (2.76, 0.6), (5.40, 0.35), (8.93, 0.18)]):
        x += g * np.sin(2 * np.pi * f * r * t + rng.uniform(0, 6)) * env(n, tau / (1 + 0.6 * k))
    return x * np.minimum(1, t / 0.0006)
def money_counter(L, f0=1500, f1=2900, n_ticks=None, rise=True):
    """financial growth: coin ticks that speed up and rise in pitch + a soft rising tone underneath"""
    n = int((L + 0.4) * SR); out = np.zeros(n)
    k = n_ticks or max(6, int(L / 0.045))
    for i in range(k):
        p = i / (k - 1); tt = L * (1 - (1 - p) ** 1.35) if rise else L * p
        f = f0 + (f1 - f0) * (p if rise else 1 - p)
        c = coin(f * rng.uniform(0.98, 1.02), 0.05) * (0.55 + 0.45 * p if rise else 1 - 0.5 * p)
        i0 = int(tt * SR); out[i0:i0 + len(c)] += c[: n - i0]
    t = np.arange(n) / SR
    fr = (330 * 2 ** (np.minimum(t, L) / L)) if rise else (520 * 2 ** (-np.minimum(t, L) / L))
    tone = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.minimum(1, t / 0.05) * np.where(t < L, 1, np.exp(-(t - L) / 0.08))
    return out / np.abs(out).max() + 0.22 * lp(tone, 1200)
def coin_jingle(k=7, spread=0.22):
    n = int((spread + 0.4) * SR); out = np.zeros(n)
    for i in range(k):
        c = coin(rng.uniform(2200, 4200), rng.uniform(0.05, 0.11)) * rng.uniform(0.5, 1)
        i0 = int(rng.uniform(0, spread) * SR * (i / k) ** 0.7); out[i0:i0 + len(c)] += c[: n - i0]
    return out
def fill_tone(L):  # soft rising tone while a bar fills
    n = int(L * SR); t = np.arange(n) / SR
    f = 220 * 2 ** (t / L)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.3 * np.sin(2 * np.pi * np.cumsum(2 * f) / SR)
    return lp(x * np.minimum(1, t / 0.15) * np.minimum(1, (L - t) / 0.12), 1500)
def slicer(L=0.7, k=26):  # bar splitting into installments: rapid ticks spreading outward
    n = int((L + 0.1) * SR); out = np.zeros(n)
    for i in range(k):
        p = i / (k - 1); c = line_tick(i % 5) * (1 - 0.5 * p)
        i0 = int(p * L * SR); out[i0:i0 + len(c)] += c[: n - i0]
    return out
def shimmer(L=0.84):  # gold spark + rings drawing: rising shimmer
    n = int(L * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for f in [2093, 2637, 3136, 3951, 4699]:
        x += np.sin(2 * np.pi * f * (1 + 0.06 * t / L) * t + rng.uniform(0, 6)) * (0.6 + 0.4 * np.sin(2 * np.pi * rng.uniform(9, 14) * t))
    a = (t / L) ** 1.6
    air = sweep_noise(n, 800, 3000, 3000, 9000, curve=lambda p: p ** 2)
    return (0.35 * x / np.abs(x).max() + 0.65 * air / np.abs(air).max()) * a
def bloom():      # logo lands: warm soft impact with a short major-chord halo
    n = int(1.1 * SR); t = np.arange(n) / SR
    f = 55 + 45 * np.exp(-t / 0.05)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.16) * np.minimum(1, t / 0.003)
    ch = sum(np.sin(2 * np.pi * fr * t) for fr in (261.6, 329.6, 392.0, 523.3)) * env(n, 0.35) * np.minimum(1, t / 0.01)
    return room(lp(sub + 0.18 * ch, 3000), 0.5, 0.25)[:n]
def sparkle():
    n = int(0.8 * SR); out = np.zeros(n)
    for i, f in enumerate([3520, 4186, 4699, 5274]):
        c = coin(f, 0.12) * (1 - 0.15 * i); i0 = int(i * 0.07 * SR); out[i0:i0 + len(c)] += c[: n - i0]
    return out
def deflate(L=0.45):  # value drops by half: falling ticks + falling tone
    return money_counter(L, 2600, 1300, n_ticks=9, rise=False)
def key(i):
    n = int(0.035 * SR); t = np.arange(n) / SR
    f = 2600 + 380 * ((i * 7) % 5)
    return bp(rng.standard_normal(n), 2000, 6500) * env(n, 0.003) + 0.35 * np.sin(2 * np.pi * f * t) * env(n, 0.004)
def click():
    n = int(0.05 * SR); t = np.arange(n) / SR
    body = np.sin(2 * np.pi * 1850 * t) * env(n, 0.006)
    tick = bp(rng.standard_normal(n), 2500, 7000) * env(n, 0.0025)
    return lp(body * 0.7 + tick * 0.6, 9000)

# ------------------------------------------------------------------ placement
new = np.zeros_like(sfx)
log = []
def place(x, t, db, pan=0.0, what=""):
    x = at_peak(x, db); i = int(round(t * SR)); x = x[: max(0, N - i)]
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4); m = max(l, r)
    new[i:i + len(x), 0] += x * l / m; new[i:i + len(x), 1] += x * r / m
    log.append(dict(t=round(t, 3), sfx=what, db=db))
def place_peak(xi, t_peak, db, pan=0.0, what=""):
    x, ci = xi; place(x, t_peak - ci / SR, db, pan, what)

S = {s["id"]: s["start"] for s in json.load(open("work/segments.json"))["segments"]}

# remove the old generic impact under the stamp (only sound in 3.430-3.880 s of the old SFX stem)
i0, i1 = int(round(3.430 * SR)), int(round(3.885 * SR))
assert np.abs(sfx[int(3.0 * SR):i0]).max() < 1e-6 and np.abs(sfx[i1:int(4.5 * SR)]).max() < 1e-6
sfx[i0:i1] = 0

# S01: news card entrance, stamp, painter card, exclusion tag
te = 1 / 60
place(swish_up(), te, -15, what="S01 card rises (entrance)")
place(land(), te + 0.42, -15, what="S01 card lands")
for i in range(4): place(line_tick(i), te + 0.14 + i * 0.075 + 0.06, -24, pan=-0.2 + 0.13 * i, what="S01 line reveal")
place_peak(stamp(), 3.430, -6, what="S01 'EXCLUSÃO' stamp slam (replaces generic impact)")
place_peak(swish(0.45, 0.5), 4.173 + 0.2, -17, pan=0.2, what="S01 painter card slides in")
place(denied(), 5.31, -15, what="S01 'Termo de Exclusão' tag")
# S02: camera pass, paint roller, DAS slips, pull-back
s = S["S02"]
place_peak(swish(0.6, 0.5, (300, 1200), (1500, 6000)), s + 2.13, -14, pan=-0.2, what="S02 camera pass to work card")
for i, t in enumerate([2.33, 2.65, 2.97, 3.29]): place(roller(0.3), s + t, -21, pan=-0.3 + 0.2 * i, what="S02 roller stroke")
for i, t in enumerate([3.25, 3.47, 3.69]): place(paper(), s + t, -18, pan=[-0.4, 0.1, 0.4][i], what="S02 DAS slip flies")
place_peak(swish(1.1, 0.45, (150, 600), (500, 2200), 0.3), s + 3.30 + 0.5, -21, what="S02 camera pull-back")
# S04: job check marks
s = S["S04"]
for i, t in enumerate([0.19, 0.55, 0.91]): place(pop(900 + 120 * i), s + t, -16, pan=-0.2 + 0.2 * i, what="S04 job checked")
# S05: magnifier sweeps + money growth (counter to R$ 72.400, then juros/multa raising the total)
s = S["S05"]
place_peak(swish(0.5, 0.5, (500, 2000), (1500, 5000)), s + 0.59, -19, pan=0.3, what="S05 magnifier sweep 1")
place_peak(swish(0.45, 0.5, (500, 2000), (1500, 5000)), s + 1.065, -19, pan=-0.3, what="S05 magnifier sweep 2")
place(money_counter(0.9, 1500, 3000), s + 2.003, -14, what="S05 debt grows to R$ 72.400 (financial growth)")
place(coin_jingle(8, 0.25), s + 2.003 + 0.86, -17, what="S05 coins settle on R$ 72.400")
place(money_counter(0.35, 2000, 3200, n_ticks=8), s + 3.633, -16, pan=-0.15, what="S05 + juros raises total")
place(coin_jingle(6, 0.18), s + 3.633, -18, pan=-0.15, what="S05 juros coins")
place(money_counter(0.35, 2300, 3600, n_ticks=8), s + 4.153, -15, pan=0.15, what="S05 + multa raises total to R$ 108.000")
place(coin_jingle(8, 0.22), s + 4.153, -17, pan=0.15, what="S05 multa coins")
# S07: logo intro, logo steps back
s = S["S07"]
place(shimmer(0.84), s + 0.02, -16, what="S07 gold spark + rings draw (logo intro)")
place(bloom(), s + 0.86, -11, what="S07 logo blooms in")
place(sparkle(), s + 1.12, -19, what="S07 shine across logo")
place_peak(swish(0.55, 0.5), s + 2.043 + 0.28, -17, what="S07 logo steps back")
# S09: window push-in
s = S["S09"]
place_peak(swish(0.5, 0.5, (250, 900), (900, 3500)), s + 0.4, -19, what="S09 window pushes in")
# S12: separator line, total highlight
s = S["S12"]
place(marker(0.3), s + 1.46, -21, what="S12 separator line")
place(marker(0.35), s + 2.17, -18, what="S12 total highlighted")
# S13: bar fills, value counts to 108 mil, drop to 54 mil
s = S["S13"]
place(fill_tone(1.4), s + 0.21, -22, what="S13 debt bar fills")
place(money_counter(0.5, 1600, 3000, n_ticks=10), s + 43.31 - 41.367, -16, what="S13 value counts to R$ 108 mil")
place(deflate(0.45), s + 3.673, -15, what="S13 value/bar drop to R$ 54 mil")
# S14: bar splits into 145 installments, camera approach, highlight band
s = S["S14"]
place(slicer(0.7, 26), s + 1.13, -18, what="S14 bar splits into 145 installments")
place_peak(swish(1.6, 0.5, (150, 600), (600, 2600), 0.28), s + 1.52 + 0.8, -21, what="S14 camera approach")
place(marker(0.4), s + 1.90, -18, what="S14 'em até 145 meses' highlighted")
# S15: highlight band
s = S["S15"]
place(marker(0.45), s + 1.343, -18, what="S15 '1.102.924' sentence highlighted")
# S16: CTA comment box, typing, click on "Publicar"
s = S["S16"]
place_peak(swish(0.4, 0.45, (300, 1200), (1500, 5000)), s + 0.15, -18, what="S16 comment box rises")
place(pop(780), s + 0.3, -18, what="S16 comment box lands")
t0 = s + 1.45
for i in range(1, 12): place(key(i), t0 + i * 0.075, -17, pan=0.15 * np.sin(i), what="S16 typing 'Consultoria'" if i == 1 else "")
place(click(), t0 + 11 * 0.075 + 0.45, -11, what="S16 click 'Publicar'")

out = sfx + new
sf.write("stems5/sfx.wav", out.astype(np.float32), SR, subtype="PCM_24")
for n_ in ("voice", "riser", "music"): shutil.copy(f"stems/{n_}.wav", f"stems5/{n_}.wav")
json.dump([e for e in log if e["sfx"]], open("work/sfx5_log.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# master: plain sum, single trim to -14 LUFS (same rule as master.py)
riser, _ = sf.read("stems/riser.wav", dtype="float64"); music, _ = sf.read("stems/music.wav", dtype="float64")
m = voice + out + riser + music
sf.write("work/master5_sum.wav", m.astype(np.float32), SR, subtype="FLOAT")
def meas(p):
    o = subprocess.run(["ffmpeg", "-nostats", "-i", p, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    o = o[o.rindex("Summary:"):]
    return float(re.search(r"I:\s+(-?[\d.]+) LUFS", o).group(1)), float(re.search(r"Peak:\s+(-?[\d.]+|-inf) dBFS", o).group(1))
I, tp = meas("work/master5_sum.wav"); g = 10 ** ((-14 - I) / 20)
sf.write("work/master5.wav", (m * g).astype(np.float32), SR, subtype="FLOAT")
I2, tp2 = meas("work/master5.wav")
if tp2 > -1.0:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "work/master5.wav", "-af", "alimiter=limit=0.84:attack=5:release=60:level=disabled:asc=1,aresample=48000", "-c:a", "pcm_f32le", "work/master5_l.wav"], check=True)
    shutil.move("work/master5_l.wav", "work/master5.wav"); I2, tp2 = meas("work/master5.wav")
print("new events", len([e for e in log if e["sfx"]]), "| sfx stem", meas("stems5/sfx.wav"), "| master trim %.2f dB" % (20 * np.log10(g)), "| master", (I2, tp2))
