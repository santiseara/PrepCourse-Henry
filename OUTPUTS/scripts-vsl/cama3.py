# -*- coding: utf-8 -*-
"""Cama musical SIN BUCLE, sacada del instrumental de un ad largo del competidor.
Por que existe: cama2.py repetia una pista de 10 s para llenar 30 s y el empalme se oia
(24/11/2026, Santiago: "se repite la misma parte todo el video, dejá correr esa canción").
Aca la pista tiene que ser mas larga que el video: si no alcanza, el script CORTA y avisa,
nunca repite. El instrumental sale de demucs sobre un ad con voz en off (ver stems.py).
Uso: python3 cama3.py instrumental.wav salida.wav <segundos> [offset_seg]"""
import sys, numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt

ent, sal, total = sys.argv[1], sys.argv[2], float(sys.argv[3])
OFF = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
x, sr = sf.read(ent, dtype='float32')
if x.ndim == 1: x = np.stack([x, x], 1)

def hp(y, f): return sosfilt(butter(2, f, 'high', fs=sr, output='sos'), y, axis=0)
def bp(y, a, b): return sosfilt(butter(2, [a, b], 'band', fs=sr, output='sos'), y, axis=0)
x = x + 0.75 * hp(x, 4500) - 0.25 * bp(x, 200, 500)   # la Biblioteca sirve el audio a 48 kbps: + aire, - barro
x = np.clip(x, -1, 1)

need = int(total * sr); o = int(OFF * sr)
if len(x) - o < need:
    raise SystemExit(f'ERROR: {ent} tiene {len(x)/sr:.1f} s y desde el segundo {OFF:.1f} '
                     f'hacen falta {total:.1f} s. Buscá un ad mas largo; repetir no es opcion.')
out = x[o:o + need].copy()
fi = int(0.15 * sr); out[:fi] *= np.linspace(0, 1, fi)[:, None]
fo = int(min(1.2, total * 0.12) * sr); out[-fo:] *= np.linspace(1, 0, fo)[:, None]
out = out / (np.abs(out).max() + 1e-9) * 0.95
sf.write(sal, out, sr)
print(f'{sal} {len(out)/sr:.1f} s · corrida continua del segundo {OFF:.1f} al {OFF+total:.1f} de {ent}')
