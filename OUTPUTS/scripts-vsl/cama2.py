# -*- coding: utf-8 -*-
"""Cama musical a partir de la pista de un ad ajeno.
La Biblioteca de Meta sirve el audio en HE-AAC a 48 kbps: suena opaco y metalico, asi que
la pista se levanta en agudos y se le saca algo de barro en los medios-bajos.
Para alargarla NO se busca el periodo del compas (estas pistas no cierran en loop entero y
el empalme da un salto ritmico): se repite la pista completa con un crossfade LARGO, que
sobre musica ritmica se disimula mucho mejor que un corte.
Uso: python3 cama2.py entrada.wav salida.wav <segundos> [crossfade_seg]"""
import sys, numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt

ent, sal, total = sys.argv[1], sys.argv[2], float(sys.argv[3])
XF = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
x, sr = sf.read(ent)
if x.ndim == 1: x = np.stack([x, x], 1)
x = x[int(0.3 * sr):len(x) - int(0.15 * sr)]      # fade de entrada y cola cortada del ad

def hp(y, f): return sosfilt(butter(2, f, 'high', fs=sr, output='sos'), y, axis=0)
def bp(y, a, b): return sosfilt(butter(2, [a, b], 'band', fs=sr, output='sos'), y, axis=0)
x = x + 0.75 * hp(x, 4500) - 0.25 * bp(x, 200, 500)   # + aire, - barro
x = np.clip(x, -1, 1)

need = int(total * sr)
if len(x) >= need:
    out = x[:need]
else:
    xf = int(XF * sr)
    out = x.copy()
    while len(out) < need:
        r = (np.linspace(0, 1, xf) ** 0.5)[:, None]   # curva de potencia constante
        out = np.concatenate([out[:-xf], out[-xf:] * np.sqrt(1 - r**2) + x[:xf] * r, x[xf:]])
    out = out[:need]
fo = int(min(1.2, total * 0.12) * sr)
out[-fo:] *= np.linspace(1, 0, fo)[:, None]
out = out / (np.abs(out).max() + 1e-9) * 0.95
sf.write(sal, out, sr)
print(f'{sal} {len(out)/sr:.1f} s  (fuente {len(x)/sr:.1f} s, crossfade {XF} s)')
