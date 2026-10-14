import sys, wave, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel("medium", compute_type="int8")
for p in sys.argv[1:]:
    w = wave.open(p)
    a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    segs, info = m.transcribe(a, language="pt", word_timestamps=True, beam_size=5,
        initial_prompt="Contabilidade, política, impostos, eleições, Simples Nacional, CNPJ, MEI.")
    out = p.replace("02_audio", "03_transcricoes").replace(".wav", "_palavras.txt")
    with open(out, "w", encoding="utf-8") as f:
        for s in segs:
            for x in s.words:
                f.write(f"{x.start:6.2f} -> {x.end:6.2f}  {x.word.strip()}\n")
    print("ok", out, flush=True)
