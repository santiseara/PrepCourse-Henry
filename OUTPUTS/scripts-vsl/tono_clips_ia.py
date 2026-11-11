"""F0 mediana por clip (autocorrelacion simple sobre el audio ya recortado en voz/*.wav),
para ver si la voz se mantiene pareja entre clips del mismo personaje. Sustituye a voz.py (que pide librosa)."""
import json, os, sys, numpy as np, soundfile as sf
C = json.load(open("proyecto.json"))
def f0(y, sr=16000):
    out = []
    w = int(0.04 * sr)
    for i in range(0, len(y) - w, w // 2):
        x = y[i:i + w] - y[i:i + w].mean()
        if np.sqrt((x ** 2).mean()) < 0.02: continue
        a = np.correlate(x, x, "full")[w - 1:]
        lo, hi = sr // 400, sr // 70
        if hi >= len(a): continue
        p = np.argmax(a[lo:hi]) + lo
        if a[p] > 0.3 * a[0]: out.append(sr / p)
    return float(np.median(out)) if out else float("nan")
por = {}
for c in C["clips"]:
    p = os.path.join("voz", c["k"] + ".wav")
    if not os.path.exists(p): continue
    y, sr = sf.read(p)
    if y.ndim > 1: y = y.mean(1)
    y = y[::3] if sr == 48000 else y          # 48k -> 16k aprox
    por.setdefault(c["personaje"], []).append((c["k"], f0(y)))
for per, xs in por.items():
    med = np.nanmedian([x[1] for x in xs])
    print(f"{per}: mediana {med:.0f} Hz")
    for k, f in xs:
        print(f"   {k:4} {f:6.1f} Hz ({(f/med-1)*100:+5.1f} %)" + ("   <- se sale" if abs(f/med-1) > 0.08 else ""))
