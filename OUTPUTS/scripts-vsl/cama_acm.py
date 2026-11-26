# -*- coding: utf-8 -*-
"""Cama musical para la tanda de Puertas de ACM a partir de una pista que mando Santiago.
Reglas del 25/11 ([[guiones-y-anuncios]]):
  - la ventana arranca donde la pista YA esta en pleno, nunca en la intro ni en el fade
  - pasa-altos a 70 Hz y hueco de -0,35 en 250-700 Hz para que la voz se despegue
  - se balancea para parlante de telefono: la energia no puede vivir abajo de 90 Hz
Uso: python3 cama_acm.py entrada.mp3 salida.wav <segundos> [offset]
"""
import subprocess, sys, numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt

ent, sal, total = sys.argv[1], sys.argv[2], float(sys.argv[3])
off = float(sys.argv[4]) if len(sys.argv) > 4 else None
sr = 48000
raw = subprocess.run(['ffmpeg','-v','0','-i',ent,'-ac','2','-ar',str(sr),'-f','f32le','-'],
                     capture_output=True).stdout
x = np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).copy()

# 1) nivel segundo a segundo -> donde esta en pleno
niv = np.array([np.sqrt((x[i*sr:(i+1)*sr]**2).mean()) for i in range(len(x)//sr)])
pleno = niv.max()
if off is None:
    buenos = np.where(niv > 0.75*pleno)[0]
    off = float(buenos[0]) if len(buenos) else 0.0
a = int(off*sr); b = a + int(total*sr)
if b > len(x):
    reps = int(np.ceil((b-a)/ (len(x)-a))) + 1
    x = np.concatenate([x[a:]]*reps); a = 0; b = int(total*sr)
y = x[a:b].copy()

def sos(f, t, o=4): return butter(o, f, t, fs=sr, output='sos')
y = sosfilt(sos(70, 'high'), y, axis=0)                 # fuera el subgrave que el telefono no da
# hueco donde vive la voz: banda 250-700 Hz a -0,35
banda = sosfilt(sos([250, 700], 'bandpass', 2), y, axis=0)
y = y - 0.35*banda
# 2) balance para parlante de telefono (regla del 25/11): objetivo 14/26/33/21/6 %
#    en <90 / 90-200 / 200-1k / 1-4k / 4-8k. Se arma una curva suave de ganancia y se
#    aplica en frecuencia, iterando hasta caer dentro del objetivo.
CORTES = [0, 90, 200, 1000, 4000, 8000, sr/2]
OBJ = np.array([14, 26, 33, 21, 6, 0.3], float); OBJ /= OBJ.sum()
def pct(z):
    Z = np.abs(np.fft.rfft(z.mean(1)))**2
    fr = np.fft.rfftfreq(len(z), 1/sr); t = Z.sum()
    return np.array([Z[(fr>=CORTES[i])&(fr<CORTES[i+1])].sum()/t for i in range(6)]), fr
for _ in range(6):
    p_, fr = pct(y)
    g = np.sqrt(OBJ/np.maximum(p_, 1e-9))
    g = np.clip(g, 0.15, 8.0)
    centros = np.array([45, 145, 600, 2500, 6000, 14000.0])
    curva = np.exp(np.interp(np.log(np.maximum(fr, 20)), np.log(centros), np.log(g)))
    Y = np.fft.rfft(y, axis=0) * curva[:, None]
    y = np.fft.irfft(Y, n=len(y), axis=0)
    if np.abs(pct(y)[0]*100 - OBJ*100).max() < 2.5: break
y = y / (np.abs(y).max() + 1e-9) * 0.9
f = int(0.8*sr)
y[:f] *= np.linspace(0, 1, f)[:, None]
y[-f:] *= np.linspace(1, 0, f)[:, None]
sf.write(sal, y, sr)

def banda_pct(z):
    Z = np.abs(np.fft.rfft(z.mean(1)))**2
    fr = np.fft.rfftfreq(len(z), 1/sr); t = Z.sum()
    cortes = [0, 90, 200, 1000, 4000, 8000, sr/2]
    return [round(100*Z[(fr >= cortes[i]) & (fr < cortes[i+1])].sum()/t, 1) for i in range(6)]
print(sal, f'offset {off:.0f}s  {total:.1f}s  bandas <90/90-200/200-1k/1-4k/4-8k/>8k = {banda_pct(y)}')
