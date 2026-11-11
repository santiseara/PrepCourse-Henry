"""Deja el audio de todos los clips parejo en voz_vc/: mismo nivel (RMS 0.10, igual que montar.py)
y, para los clips que la medicion de tono marca desviados, un ajuste suave de pitch que NO cambia
la duracion (asetrate + atempo), asi el lipsync queda intacto.
Uso: python3 ../empareja.py [clave=factor ...]    ej: python3 ../empareja.py h1=1.05"""
import json, os, subprocess, sys
import numpy as np
FF = os.path.expanduser("~/bin/ffmpeg")
SR = 48000
C = json.load(open("proyecto.json"))
fix = dict(x.split("=") for x in sys.argv[1:])
os.makedirs("voz_vc", exist_ok=True)
for c in C["clips"]:
    k = c["k"]; src = os.path.join("clips", k + ".mp4"); out = os.path.join("voz_vc", k + ".wav")
    f = float(fix.get(k, 1.0))
    af = f"asetrate={SR}*{f},aresample={SR},atempo={1/f:.6f}" if abs(f - 1) > 1e-6 else "anull"
    raw = subprocess.run([FF, "-v", "error", "-i", src, "-af", af, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True).stdout
    y = np.frombuffer(raw, np.float32).copy()
    y *= 0.10 / np.sqrt(np.mean(y[np.abs(y) > 0.01] ** 2) + 1e-9)
    y = np.clip(y, -0.99, 0.99)
    import wave
    with wave.open(out, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((y * 32767).astype("<i2").tobytes())
    print("ok", k, "pitch", f)
