import sys, json
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[1], device="cpu", compute_type="int8")
for p in sys.argv[2:]:
    import soundfile as sf; a,_=sf.read(p,dtype="float32")
    segs, info = m.transcribe(a, language="pt", word_timestamps=True, vad_filter=False, beam_size=5, condition_on_previous_text=False)
    words=[]
    for s in segs:
        for w in s.words: words.append(dict(w=w.word.strip(), s=round(w.start,3), e=round(w.end,3), p=round(w.probability,3)))
    json.dump(words, open(p.replace(".wav","."+sys.argv[1]+".json"),'w'), ensure_ascii=False, indent=0)
    print("==", p); print(" ".join(f"[{x['s']:.2f}]{x['w']}" for x in words))
