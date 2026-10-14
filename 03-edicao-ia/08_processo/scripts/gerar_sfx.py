"""Sintetiza a biblioteca de efeitos sonoros da JA (sem licencas de terceiros).
Saida: 05_assets/sons/*.wav (48kHz mono, pico -3 dBFS; o volume final e ajustado na mixagem)."""
import numpy as np, wave, os

SR = 48000
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "05_assets", "sons")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(7)

def t(d): return np.arange(int(SR * d)) / SR

def save(name, x):
    x = x / (np.max(np.abs(x)) + 1e-9) * 0.707
    fade = int(SR * 0.004)
    x[:fade] *= np.linspace(0, 1, fade); x[-fade:] *= np.linspace(1, 0, fade)
    with wave.open(os.path.join(OUT, name), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())

def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR); y = np.zeros_like(x); acc = 0.0
    for i, v in enumerate(x):
        acc = (1 - a) * v + a * acc; y[i] = acc
    return y

def bandsweep(d, f0, f1, q=0.15):
    """ruido filtrado com centro varrendo f0->f1 (filtro de estado variavel)"""
    n = rng.standard_normal(int(SR * d)); y = np.zeros_like(n)
    fc = np.geomspace(f0, f1, len(n)); low = band = 0.0
    for i, v in enumerate(n):
        f = 2 * np.sin(np.pi * fc[i] / SR)
        low += f * band; high = v - low - q * band; band += f * high; y[i] = band
    return y

# whoosh: transicao entre blocos
d = 0.5; tt = t(d)
env = np.sin(np.pi * np.clip(tt / d, 0, 1)) ** 2
save("whoosh.wav", bandsweep(d, 300, 4000, 0.4) * env)

# whoosh reverso curto (saida / swipe)
d = 0.32; tt = t(d)
save("swipe.wav", bandsweep(d, 2500, 500, 0.5) * np.sin(np.pi * tt / d) ** 1.5)

# pop: entrada de card
d = 0.14; tt = t(d)
f = 520 + 900 * (1 - np.exp(-tt * 40))
save("pop.wav", np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 28))

# tecla da urna: clique curto e seco
d = 0.06; tt = t(d)
save("tecla.wav", (np.sin(2 * np.pi * 1850 * tt) * 0.6 + rng.standard_normal(len(tt)) * 0.4) * np.exp(-tt * 120))

# bipe de confirmacao (sequencia rapida estilo urna)
seq = []
for k in range(5):
    tt = t(0.07 if k < 4 else 0.32)
    seq.append(np.sign(np.sin(2 * np.pi * 1000 * tt)) * 0.5 * np.exp(-tt * (6 if k == 4 else 2)))
    seq.append(np.zeros(int(SR * 0.035)))
save("confirma.wav", lowpass(np.concatenate(seq), 5000))

# impacto grave: dado/afirmacao forte
d = 0.7; tt = t(d)
f = 38 + 70 * np.exp(-tt * 9)
body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 5)
hit = lowpass(rng.standard_normal(len(tt)), 1800) * np.exp(-tt * 40) * 2
save("impacto.wav", body + hit)

# glitch digital: interferencia
d = 0.34; tt = t(d)
sq = np.sign(np.sin(2 * np.pi * (180 + 900 * (np.floor(tt * 40) % 5)) * tt))
gate = (np.floor(tt * 55) % 3 != 0).astype(float)
crush = np.round(rng.standard_normal(len(tt)) * 3) / 3
save("glitch.wav", (sq * 0.5 + crush * 0.5) * gate * np.exp(-tt * 4))

# erro: dois tons descendentes
seq = []
for fq in (440, 330):
    tt = t(0.13)
    seq.append(lowpass(np.sign(np.sin(2 * np.pi * fq * tt)), 2500) * np.exp(-tt * 9))
    seq.append(np.zeros(int(SR * 0.02)))
save("erro.wav", np.concatenate(seq))

# ding positivo: conquista / check
d = 0.9; tt = t(d)
x = sum(a * np.sin(2 * np.pi * fq * tt) * np.exp(-tt * k) for fq, a, k in ((1318.5, 1, 4.5), (1975.5, .5, 6), (2637, .25, 8)))
x[int(SR * 0.09):] += 0.8 * sum(a * np.sin(2 * np.pi * fq * tt[:len(tt) - int(SR * 0.09)]) * np.exp(-tt[:len(tt) - int(SR * 0.09)] * k) for fq, a, k in ((1760, 1, 4.5), (2637, .4, 7)))
save("ding.wav", x)

# tique: contadores / barras de apuracao
d = 0.035; tt = t(d)
save("tique.wav", np.sin(2 * np.pi * 3200 * tt) * np.exp(-tt * 200))

# subida (riser) curta para a abertura da tela dividida
d = 0.6; tt = t(d)
save("riser.wav", bandsweep(d, 200, 6000, 0.3) * (tt / d) ** 2 + np.sin(2 * np.pi * np.cumsum(120 + 300 * tt / d) / SR) * 0.3 * (tt / d))

print(sorted(os.listdir(OUT)))
