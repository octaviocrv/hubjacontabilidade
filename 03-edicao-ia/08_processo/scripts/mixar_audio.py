"""Som do Reel Politica: 4 stems (voice, sfx, riser, music) + master -14 LUFS.
Desenhos de som herdados do Reel Pintor (05_assets/scripts/audio_rev5.py), mais: tecla de urna,
ticks de apuracao, ponteiro do medidor. Volumes relativos ao pico da voz (ESTILO.md).
Rev2: S01 sem SFX (camera original); bipes da urna no S02; suspense no S03 (musica perde o ar,
cama grave + riser ate o corte) e virada no S04 (whoosh + impacto + musica reancorada no corte,
com palmas leves = outra energia). Eventos da rev1 depois da pausa andam AJ.shift.seg via T().
Uso: python mixar_audio.py <pasta_projeto>
"""
import json, os, re, shutil, subprocess, sys
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve

P = sys.argv[1]
SR = 48000
os.makedirs(os.path.join(P, "work", "stems"), exist_ok=True)
voice, sr = sf.read(os.path.join(P, "work", "voice.wav"), dtype="float64"); assert sr == SR
if voice.ndim == 1: voice = np.stack([voice, voice], 1)
END = json.load(open(os.path.join(P, "assets", "timeline.json")))["END"]
N = int(round(END * SR)); voice = voice[:N] if len(voice) >= N else np.pad(voice, ((0, N - len(voice)), (0, 0)))
VPK = 20 * np.log10(np.abs(voice).max())
rng = np.random.default_rng(11)
AJ = json.load(open(os.path.join(P, "src", "ajustes.json"), encoding="utf-8"))
TRS = {t["id"]: t for t in json.load(open(os.path.join(P, "assets", "timeline.json")))["trechos"]}
SH, SPLIT = AJ["shift"]["seg"], AJ["shift"]["apos"]
def T(t): return t + SH if t >= SPLIT - 0.06 else t  # relogio da rev1 -> relogio novo

def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], "bandpass", fs=SR, output="sos"), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, "lowpass", fs=SR, output="sos"), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, "highpass", fs=SR, output="sos"), x)
def env(n, tau): return np.exp(-np.arange(n) / (tau * SR))
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

# ---------------- desenhos (Reel Pintor) ----------------
def swish(L=0.42, peak=0.5, lo=(400, 1500), hi=(1800, 6500), width=0.22):
    n = int(L * SR); t = np.arange(n) / SR
    a = np.exp(-((t - peak * L) / (width * L)) ** 2)
    x = sweep_noise(n, lo[0], lo[1], hi[0], hi[1], curve=lambda p: np.sin(np.pi * min(p / peak, 1) / 2) if p < peak else 1 - 0.4 * (p - peak)) * a
    return x, int(peak * n)
def swish_up():
    n = int(0.5 * SR); t = np.arange(n) / SR
    a = np.minimum(1, t / 0.18) ** 2 * np.exp(-np.maximum(0, t - 0.24) / 0.07)
    return sweep_noise(n, 250, 900, 1800, 7000, curve=lambda p: p ** 1.5) * a
def land():
    n = int(0.25 * SR); t = np.arange(n) / SR
    f = 70 + 60 * np.exp(-t / 0.03)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.06) * np.minimum(1, t / 0.002)
    tap = bp(rng.standard_normal(n), 800, 3500) * env(n, 0.008)
    return lp(body + 0.25 * tap / np.abs(tap).max(), 2500)
def line_tick(i):
    n = int(0.03 * SR); t = np.arange(n) / SR
    return bp(rng.standard_normal(n), 3000, 9000) * env(n, 0.004) + 0.3 * np.sin(2 * np.pi * (2400 + 180 * i) * t) * env(n, 0.006)
def stamp():
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
def denied():
    n = int(0.5 * SR); out = np.zeros(n)
    for k, (f, off) in enumerate([(587.3, 0.0), (440.0, 0.11)]):
        o = int(off * SR); m = n - o; t = np.arange(m) / SR
        a = np.minimum(1, t / 0.004) * env(m, 0.09)
        tone = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t) + 0.12 * np.sin(2 * np.pi * 3 * f * t)
        out[o:] += lp(tone * a, 3500) * (0.9 if k == 0 else 1.0)
    return out
def chime():  # sinal de duas notas (confirmacao)
    n = int(0.7 * SR); out = np.zeros(n)
    for k, (f, off) in enumerate([(880.0, 0.0), (1318.5, 0.1)]):
        o = int(off * SR); m = n - o; t = np.arange(m) / SR
        a = np.minimum(1, t / 0.003) * env(m, 0.16)
        out[o:] += (np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 2 * f * t)) * a
    return room(out, 0.4, 0.2)[:n]
def pop(f0=950):
    n = int(0.09 * SR); t = np.arange(n) / SR
    f = f0 * (0.55 + 0.45 * np.exp(-t / 0.018))
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.03) * np.minimum(1, t / 0.0015)
    return body + 0.25 * bp(rng.standard_normal(n), 2500, 8000) * env(n, 0.004)
def marker(L):
    n = int(L * SR); t = np.arange(n) / SR
    a = np.minimum(1, t / 0.03) * np.minimum(1, (L - t) / 0.06)
    grain = 0.7 + 0.3 * lp(rng.standard_normal(n), 60) / 0.05
    return bp(rng.standard_normal(n), 1800, 6000) * a * np.clip(grain, 0.2, 1.6)
def coin(f, tau=0.09):
    n = int(tau * 4 * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for k, (r, g) in enumerate([(1, 1), (2.76, 0.6), (5.40, 0.35), (8.93, 0.18)]):
        x += g * np.sin(2 * np.pi * f * r * t + rng.uniform(0, 6)) * env(n, tau / (1 + 0.6 * k))
    return x * np.minimum(1, t / 0.0006)
def money_counter(L, f0=1500, f1=2900, n_ticks=None, rise=True):
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
def shimmer(L=0.84):
    n = int(L * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for f in [2093, 2637, 3136, 3951, 4699]:
        x += np.sin(2 * np.pi * f * (1 + 0.06 * t / L) * t + rng.uniform(0, 6)) * (0.6 + 0.4 * np.sin(2 * np.pi * rng.uniform(9, 14) * t))
    a = (t / L) ** 1.6
    air = sweep_noise(n, 800, 3000, 3000, 9000, curve=lambda p: p ** 2)
    return (0.35 * x / np.abs(x).max() + 0.65 * air / np.abs(air).max()) * a
def bloom():
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
def key(i):
    n = int(0.035 * SR); t = np.arange(n) / SR
    f = 2600 + 380 * ((i * 7) % 5)
    return bp(rng.standard_normal(n), 2000, 6500) * env(n, 0.003) + 0.35 * np.sin(2 * np.pi * f * t) * env(n, 0.004)
def click():
    n = int(0.05 * SR); t = np.arange(n) / SR
    body = np.sin(2 * np.pi * 1850 * t) * env(n, 0.006)
    tick = bp(rng.standard_normal(n), 2500, 7000) * env(n, 0.0025)
    return lp(body * 0.7 + tick * 0.6, 9000)
# ---------------- novos (Politica) ----------------
def urna_key(i):  # tecla de borracha da urna: abafada, curta
    n = int(0.06 * SR); t = np.arange(n) / SR
    body = np.sin(2 * np.pi * (380 + 25 * (i % 3)) * t) * env(n, 0.012)
    clack = bp(rng.standard_normal(n), 1200, 4500) * env(n, 0.004)
    return lp(0.8 * body + 0.5 * clack / np.abs(clack).max(), 6000)
def needle():  # ponteiro balancando ate assentar
    n = int(0.75 * SR); t = np.arange(n) / SR
    f = 900 * 2 ** (-1.2 * t / 0.75)
    return lp(np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.22) * np.minimum(1, t / 0.01), 2500) + 0.3 * line_tick(1).sum() * 0
def urna_bip(f=1950, L=0.085):  # bipe eletronico da urna: quase quadrada, curta, filtrada
    n = int(L * SR); t = np.arange(n) / SR
    sq = sum(np.sin(2 * np.pi * f * k * t) / k for k in (1, 3, 5))
    a = np.minimum(1, t / 0.003) * np.minimum(1, (L - t) / 0.012)
    return room(lp(sq * a, 5500), 0.18, 0.08)
def blip(i):  # letra surgindo no visor
    n = int(0.022 * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * (2350 + 60 * (i % 4)) * t) * env(n, 0.006) * np.minimum(1, t / 0.001)
def tensao(L):  # cama de suspense: quinta grave (A1+E2) com batimento lento (~0,6 Hz) e brilho subindo
    n = int(L * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * 55 * t) + 0.6 * np.sin(2 * np.pi * 82.41 * t) + 0.25 * np.sin(2 * np.pi * 110.6 * t)
    air = sweep_noise(n, 300, 900, 1200, 3500, curve=lambda p: p ** 2)
    a = (t / L) ** 1.4 * np.minimum(1, (L - t) / 0.02)
    return lp(x + 0.4 * air / np.abs(air).max(), 2500) * a
def virada():  # impacto da virada: sub com queda de pitch + corpo abafado (sem estalo agressivo)
    n = int(1.2 * SR); t = np.arange(n) / SR
    f = 40 + 55 * np.exp(-t / 0.06)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.35) * np.minimum(1, t / 0.004)
    body = bp(rng.standard_normal(n), 120, 900, 2) * env(n, 0.05)
    air = hp(rng.standard_normal(n), 4000) * env(n, 0.12)
    return room(lp(sub + 0.35 * body / np.abs(body).max(), 4000) + 0.06 * air / np.abs(air).max(), 0.6, 0.2)[:n]
def riser(L):
    n = int(L * SR); t = np.arange(n) / SR
    air = sweep_noise(n, 300, 1200, 2500, 9000, curve=lambda p: p ** 1.8)
    tone = np.sin(2 * np.pi * np.cumsum(110 * 2 ** (1.5 * t / L)) / SR)
    a = (t / L) ** 2.2
    x = (0.7 * air / np.abs(air).max() + 0.3 * lp(tone, 1500)) * a
    x[-int(0.01 * SR):] *= np.linspace(1, 0, int(0.01 * SR))  # termina seco no corte
    return x

# ---------------- colocacao ----------------
sfx = np.zeros((N, 2)); log = []
def at_peak(x, db): return x / np.abs(x).max() * 10 ** ((VPK + db) / 20)
def place(x, t, db, pan=0.0, what="", buf=None, velho=True):
    buf = sfx if buf is None else buf
    t = T(t) if velho else t
    x = at_peak(np.asarray(x, float), db); i = int(round(t * SR)); x = x[: max(0, N - i)]
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4); m = max(l, r)
    buf[i:i + len(x), 0] += x * l / m; buf[i:i + len(x), 1] += x * r / m
    if what: log.append(dict(t=round(t, 3), sfx=what, db=db))
def place_peak(xi, t_peak, db, pan=0.0, what="", velho=True):
    x, ci = xi; place(x, (T(t_peak) if velho else t_peak) - ci / SR, db, pan, what, velho=False)

# S01: camera original, sem efeitos (rev2)
# S02 urna (rev2): entra inteira, assenta; o visor liga com o bipe; "PRESIDENTE" surge letra a letra
t02 = TRS["S02"]["start"]
place(swish_up(), t02 + 0.01, -18, what="S02 urna entra")
place(land(), t02 + 0.36, -21, what="S02 urna assenta")
place(urna_bip(), 3.36, -17, pan=-0.1, what="S02 visor liga (bipe da urna)")
for i in range(10): place(blip(i), 4.2 + i * 0.045, -24, pan=-0.1, what="S02 'PRESIDENTE' no visor" if i == 0 else "")
# S04 apuracao
# (rev2: o whoosh da virada cobre a subida do painel)
place(land(), 7.92 + 0.42, -16, what="S04 painel assenta")
place(pop(760), 8.5, -20, pan=-0.2, what="S04 linha A"); place(pop(860), 8.62, -20, pan=0.2, what="S04 linha B")
for k, t in enumerate(np.arange(8.7, 11.7, 0.11)):
    place(line_tick(k % 5), t, -27 - 4 * (k / 27), pan=0.3 * np.sin(k), what="S04 apuracao contando" if k == 0 else "")
place(pop(1040), 11.62, -17, what="S04 'quem vence?'")
# S05 mesma carga
place(swish_up(), 12.22, -17, what="S05 'sua empresa' entra")
place(marker(0.5), 13.0, -23, what="S05 ligacoes desenhadas")
place(land(), 13.18 + 0.4, -17, pan=-0.3, what="S05 coluna A"); place(land(), 13.26 + 0.4, -17, pan=0.3, what="S05 coluna B")
place(money_counter(0.7, 1500, 3000), 13.56, -16, what="S05 impostos contam (identicos)")
place_peak(stamp(), 14.6, -8, what="S05 sinal de igual bate")
place(marker(0.45), 14.95, -21, what="S05 sublinhado 'mesma carga'")
# S07 sem planejamento
place(denied(), 17.4, -15, pan=-0.4, what="S07 etiqueta 'sem planejamento'")
place(swish_up(), 18.5, -17, pan=-0.3, what="S07 NF-e sobe"); place(land(), 18.92, -16, pan=-0.3, what="S07 NF-e assenta")
for i in range(3): place(marker(0.16), 19.18 + i * 0.07, -21, pan=-0.3, what="S07 campos riscados" if i == 0 else "")
place_peak(stamp(), 19.42, -6, what="S07 carimbo 'ERRADA'")
place(swish_up(), 19.86, -17, pan=0.3, what="S07 card de dividas sobe"); place(land(), 20.28, -16, pan=0.3, what="S07 dividas assenta")
for k, t in enumerate(np.arange(19.95, 21.2, 0.05)):
    if k % 2 == 0: place(key(k), t, -27, pan=0.3, what="S07 valores embaralhando" if k == 0 else "")
place_peak(swish(0.5, 0.5, (500, 2000), (1500, 5000)), 20.47, -19, pan=0.3, what="S07 lupa varre")
place(pop(700), 20.62, -18, pan=0.3, what="S07 'nao identificadas'")
# S08 esperar x caixa
place(land(), 21.31 + 0.3, -16, what="S08 card 'esperar' assenta")
place(marker(0.6), 22.18, -24, what="S08 congresso desenhado")
place_peak(stamp(), 22.8, -6, what="S08 carimbo 'NAO ADIANTA'")
place(swish_up(), 23.2, -17, what="S08 'seu caixa' sobe"); place(land(), 23.62, -16, what="S08 caixa assenta")
place(money_counter(1.2, 2600, 1100, n_ticks=16, rise=False), 23.4, -15, what="S08 saldo despenca")
place(denied(), 24.42, -15, what="S08 alerta -75%")
# S09 com planejamento
place(chime(), 24.95, -15, pan=-0.4, what="S09 etiqueta 'com planejamento'")
place(swish_up(), 24.9, -18, what="S09 checklist sobe")
for i, t in enumerate([24.98, 25.3, 25.62]): place(pop(900 + 140 * i), t, -15, pan=-0.2 + 0.2 * i, what="S09 item conferido")
place(land(), 25.78 + 0.3, -18, what="S09 'vencedor' assenta")
for k, t in enumerate(np.arange(25.9, 26.8, 0.15)): place(click(), t, -22, pan=-0.3, what="S09 vencedor alterna A/B" if k == 0 else "")
place(chime(), 26.78, -10, what="S09 'empresa preparada'")
# S10 marca
place(shimmer(0.5), 27.19, -16, what="S10 anel dourado desenha")
place(bloom(), 27.48, -11, what="S10 logo floresce")
place(sparkle(), 27.7, -19, what="S10 brilho no logo")
place_peak(swish(0.55, 0.5), 28.95, -17, what="S10 marca recua (unico whoosh do trecho)")
place(needle(), 29.74, -19, what="S10 ponteiro vai de 'alta' a 'planejada'")
# S11 CTA
place(swish_up(), 30.6, -18, what="S11 cartao do perfil sobe"); place(pop(780), 30.98, -18, what="S11 cartao assenta")
place(click(), 31.12, -11, what="S11 toque em 'Link na bio'")

# S03 suspense -> S04 virada (relogio novo)
cut04 = TRS["S04"]["start"]
rs = np.zeros((N, 2))
place(tensao(cut04 - 5.3), 5.3, -24, what="S03 cama de suspense (quinta grave)", buf=rs, velho=False)
place(riser(cut04 - 6.9), 6.9, -18, what="S03 riser ate o corte (termina seco)", buf=rs, velho=False)
place_peak(swish(0.5, 0.7, (500, 2000), (1800, 7000)), cut04, -15, what="S03>S04 whoosh do zoom-through", velho=False)
place(virada(), cut04, -11, what="S04 impacto da virada", velho=False)

# musica: 110 BPM. Parte 1 (S01-S03) ancorada no quadro 1, Am-F-C-G, perde o ar durante a duvida.
# Parte 2 reancorada no corte do S04 (primeiro tempo forte = impacto da virada), com palmas leves.
CH = {"Am": [57, 60, 64], "F": [53, 57, 60], "C": [48, 55, 64], "G": [55, 59, 62], "Dm": [50, 57, 62], "E": [52, 56, 59]}
def mtof(m): return 440 * 2 ** ((m - 69) / 12)
def music(t_anchor, t_to, secao, palmas=False, ataque0=0.25):
    beat = 60 / 110; bar = 4 * beat
    out = np.zeros((N, 2)); cont = {}
    for b in range(int(np.ceil((t_to - t_anchor) / bar))):
        tb = t_anchor + b * bar
        nome, prog = secao(tb); k_sec = cont.get(nome, 0); cont[nome] = k_sec + 1
        ch = CH[prog[k_sec % len(prog)]]
        # pad
        L = bar; n = int(L * SR); t = np.arange(n) / SR
        a = np.minimum(1, t / (ataque0 if b == 0 else 0.25)) * np.minimum(1, (L - t) / 0.3)
        pad = sum(np.sin(2 * np.pi * mtof(m + 12) * t) + 0.3 * np.sin(2 * np.pi * mtof(m + 12) * 2.001 * t) for m in ch) * a
        i0 = int(tb * SR); seg = lp(pad, 2200) * 0.18
        k = min(n, N - i0)
        if k > 0: out[i0:i0 + k, 0] += seg[:k]; out[i0:i0 + k, 1] += seg[:k]
        for q in range(8):  # arpejo em colcheias
            tq = tb + q * beat / 2; i0 = int(tq * SR)
            if i0 >= N: break
            m = ch[[0, 1, 2, 1, 0, 2, 1, 2][q]] + 24
            n = int(0.35 * SR); t = np.arange(n) / SR
            pl = (np.sin(2 * np.pi * mtof(m) * t) + 0.4 * np.sin(2 * np.pi * mtof(m) * 3 * t) * env(n, 0.02)) * env(n, 0.09) * np.minimum(1, t / 0.002)
            k = min(n, N - i0); pan = 0.35 * np.sin(q)
            out[i0:i0 + k, 0] += pl[:k] * 0.22 * (1 - pan); out[i0:i0 + k, 1] += pl[:k] * 0.22 * (1 + pan)
        for q in range(4):  # kick suave + baixo (+ palmas nos tempos 2 e 4 na parte 2)
            tq = tb + q * beat; i0 = int(tq * SR)
            if i0 >= N: break
            n = int(0.4 * SR); t = np.arange(n) / SR
            kick = np.sin(2 * np.pi * np.cumsum(48 + 70 * np.exp(-t / 0.03)) / SR) * env(n, 0.12) * (1.0 if q % 2 == 0 else 0.55)
            bass = np.sin(2 * np.pi * mtof(ch[0] - 12) * t) * env(n, 0.25) * 0.5
            k = min(n, N - i0); s_ = (kick + bass)[:k]
            out[i0:i0 + k] += np.stack([s_, s_], 1) * 0.5
            if palmas and q % 2:
                m_ = int(0.14 * SR); tt = np.arange(m_) / SR
                cl = bp(rng.standard_normal(m_), 900, 5200) * (env(m_, 0.03) + 0.6 * (tt > 0.009) * env(m_, 0.02))
                k = min(m_, N - i0); out[i0:i0 + k] += np.stack([cl[:k] * 0.9, cl[:k]], 1) * 0.16
        for q in range(8):  # chimbal
            tq = tb + q * beat / 2; i0 = int(tq * SR)
            if i0 >= N: break
            n = int(0.05 * SR); h = hp(rng.standard_normal(n), 7000) * env(n, 0.012) * (0.5 if q % 2 else 0.25)
            k = min(n, N - i0); out[i0:i0 + k] += np.stack([h[:k] * 0.8, h[:k]], 1) * 0.3
    out[int(round(t_to * SR)):] = 0
    return np.stack([room(out[:, 0], 0.6, 0.15)[:N], room(out[:, 1], 0.6, 0.15)[:N]], 1)

def perde_o_ar(x):  # durante a duvida: passa-baixa descendo, -9 dB, e silencio no fim da fala
    t = np.arange(len(x)) / SR
    t0 = TRS["S03"]["start"]; t2 = AJ["suspense"]["fala_fim"]; t1 = t2 - 0.55
    p = np.clip((t - t0) / (t1 - t0), 0, 1)
    l1 = np.stack([lp(x[:, c], 1800) for c in (0, 1)], 1); l2 = np.stack([lp(x[:, c], 420) for c in (0, 1)], 1)
    w1 = np.clip(p * 2, 0, 1); w2 = np.clip(p * 2 - 1, 0, 1)
    y = x * (1 - w1)[:, None] + l1 * (w1 - w2)[:, None] + l2 * w2[:, None]
    g = 10 ** (-9 * p / 20) * np.clip((t2 - t) / (t2 - t1), 0, 1) ** 2
    return y * g[:, None]

prog_a = ["Am", "F", "C", "G"]; prog_b = ["Dm", "Am", "E", "Am"]; prog_c = ["F", "G", "C", "C"]
parte1 = perde_o_ar(music(1 / 60, cut04, lambda tb: ("a", prog_a)))
sec2 = lambda tb: ("a", prog_a) if tb < TRS["S07"]["start"] - 0.35 else (("b", prog_b) if tb < TRS["S09"]["start"] else ("c", prog_c))
parte2 = music(cut04, END, sec2, palmas=True, ataque0=0.03)
fo = int(0.6 * SR); parte2[-fo:] *= np.linspace(1, 0, fo)[:, None]
mus = parte1 + parte2

def write(name, x): sf.write(os.path.join(P, "work", "stems", name), x.astype(np.float32), SR, subtype="PCM_24")
def meas(path):
    o = subprocess.run(["ffmpeg", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    o = o[o.rindex("Summary:"):]
    return float(re.search(r"I:\s+(-?[\d.]+) LUFS", o).group(1)), float(re.search(r"Peak:\s+(-?[\d.]+|-inf) dBFS", o).group(1))

# musica ~10 LU abaixo da voz (-24 LUFS), nivel unico
write("music.wav", mus); Im, _ = meas(os.path.join(P, "work", "stems", "music.wav"))
mus *= 10 ** ((-24.0 - Im) / 20)
write("voice.wav", voice); write("sfx.wav", sfx); write("riser.wav", rs); write("music.wav", mus)
m = voice + sfx + rs + mus
tmp = os.path.join(P, "work", "master_sum.wav"); sf.write(tmp, m.astype(np.float32), SR, subtype="FLOAT")
I, tp = meas(tmp); g = 10 ** ((-14 - I) / 20)
mst = os.path.join(P, "work", "master.wav"); sf.write(mst, (m * g).astype(np.float32), SR, subtype="FLOAT")
I2, tp2 = meas(mst)
if tp2 > -1.0:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mst, "-af", "alimiter=limit=0.84:attack=5:release=60:level=disabled:asc=1,aresample=48000",
                    "-c:a", "pcm_f32le", mst + ".l.wav"], check=True)
    shutil.move(mst + ".l.wav", mst); I2, tp2 = meas(mst)
json.dump(log, open(os.path.join(P, "work", "sfx_log.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for s in ("voice", "sfx", "riser", "music"): print(s, meas(os.path.join(P, "work", "stems", s + ".wav")))
print("eventos", len(log), "| trim master %.2f dB" % (20 * np.log10(g)), "| master", (I2, tp2))
