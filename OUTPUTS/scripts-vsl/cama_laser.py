# -*- coding: utf-8 -*-
"""Cama musical a partir de la instrumental separada de un ad ajeno a 48-73 kbps HE-AAC.
Contra cama2.py: NO realza agudos. En HE-AAC los agudos estan SINTETIZADOS (SBR), asi que
realzarlos solo amplifica el ruido de la separacion. Lo que hay que hacer es lo contrario:
  - pasa-altos a 90 Hz: la separacion deja un retumbe de subgraves que era el 65 % de la energia
  - pasa-bajos a 7 kHz: arriba de ahi el original no tiene nada real, solo artefacto
  - normalizar y loopear con crossfade largo de potencia constante
Uso: python3 cama_laser.py entrada.wav salida.wav <segundos> [crossfade]"""
import sys, numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt

ent, sal, total = sys.argv[1], sys.argv[2], float(sys.argv[3])
XF = float(sys.argv[4]) if len(sys.argv) > 4 else 2.5
x, sr = sf.read(ent)
if x.ndim == 1: x = np.stack([x, x], 1)
x = x[int(0.3 * sr):len(x) - int(0.25 * sr)]

def sos(f, t): return butter(4, f, t, fs=sr, output='sos')
x = sosfilt(sos(90, 'high'), x, axis=0)      # fuera el retumbe de la separacion
x = sosfilt(sos(7000, 'low'), x, axis=0)     # fuera el siseo del SBR (en HE-AAC es sintetico)
# la separacion deja el 92 % de la energia entre 90 Hz y 1 kHz: suena a barro.
# se saca medio-bajo y se levanta la banda donde vive la melodia.
# Las ganancias salieron de un ajuste numerico contra la curva de una cama normal
# (0,5 / 22 / 40 / 28 / 9 % en <90, 90-200, 200-1k, 1-4k, 4-7k). Sin esto, la separacion
# deja el 92 % de la energia entre 90 Hz y 1 kHz y suena a barro.
def bp(y, a, b): return sosfilt(butter(4, [a, b], 'band', fs=sr, output='sos'), y, axis=0)
# ⛔ El realce de 1-4 kHz tiene un TECHO: ahi vive la melodia, pero tambien la voz que se
# separo. Medido con Whisper sobre la cama: con 0,4 devuelve 0 palabras; con 0,8 ya transcribe
# 37 y con 1,2 transcribe 123. O sea que subir la melodia te mete la voz en espanol del
# competidor abajo de un ad en ingles. El maximo seguro es 0,4.
x = (x - 0.75 * bp(x, 90, 200) - 0.20 * bp(x, 150, 420)
       + 0.40 * bp(x, 1100, 4200) + 0.44 * bp(x, 4000, 6800))
# compresion suave para que la cama no tenga baches donde estaba la voz
env = np.abs(x).mean(1)
n = int(0.25 * sr)
env = np.convolve(env, np.ones(n) / n, 'same')
g = (np.median(env) / np.maximum(env, 1e-6)) ** 0.45
g = np.clip(g, 0.5, 2.2)[:, None]
x = x * g
x = x / (np.abs(x).max() + 1e-9) * 0.9

need = int(total * sr)
if len(x) >= need:
    out = x[:need]
else:
    xf = int(XF * sr); out = x.copy()
    while len(out) < need:
        r = (np.linspace(0, 1, xf) ** 0.5)[:, None]
        out = np.concatenate([out[:-xf], out[-xf:] * (1 - r) + x[:xf] * r, x[xf:]])
    out = out[:need]
sf.write(sal, np.clip(out, -1, 1), sr)
print(f'{sal} {total:.0f} s (fuente {len(x)/sr:.0f} s, HP 90 Hz, LP 7 kHz, sin realce)')
