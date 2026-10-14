import sys, wave, numpy as np
p, t0, t1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
w = wave.open(p); sr = w.getframerate()
a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)/32768
win = int(sr*0.04)
out=[]
for i in range(int(t0*sr), min(int(t1*sr), len(a)-win), win):
    r = np.sqrt(np.mean(a[i:i+win]**2)); db = 20*np.log10(r+1e-9)
    out.append(f"{i/sr:5.2f}:{int(db):d}")
print(" ".join(out))
