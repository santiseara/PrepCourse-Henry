#!/usr/bin/env python3
"""Mide la silueta recortada y escribe escala+posicion en el plan del video.

Uso: python3 avatar_ubicar.py <carpeta_de_trabajo> <V>   (despues de avatar_recortar.sh)

Mide la silueta en las mascaras y la ubica igual que el ganador:
en su video de 720x1280 la persona va de x 408 a 719 (pegada al borde derecho)
y de y 840 a 1279 (pegada al piso). En 1080x1920 eso es alto 660 y tope en y=1260.
"""
import glob, json, sys
import numpy as np
from PIL import Image

base, V = sys.argv[1], sys.argv[2]
ms = sorted(glob.glob(f'{base}/key/{V}/m/*.png'))[::10]
tops, rights, lefts = [], [], []
for p in ms:
    a = np.array(Image.open(p).convert('L')) > 128
    cols, rows = a.sum(0), a.sum(1)
    nz, nzr = np.where(cols > 5)[0], np.where(rows > 5)[0]
    if not len(nz): continue
    lefts.append(nz.min()); rights.append(nz.max()); tops.append(nzr.min())
top, right, left = np.median(tops), np.median(rights), np.median(lefts)
print(f'{V}: tope {top:.0f}  izq {left:.0f}  der {right:.0f}  (de {len(tops)} cuadros)')

ALTO_DEST, TOPE_DEST = 660.0, 1260.0          # medidos en el video del ganador
s = ALTO_DEST / (1280 - top)
x = 1080 - right * s
y = 1920 - 1280 * s
print(f'  escala {s:.4f}  ->  x {x:.1f}  y {y:.1f}  ancho silueta {(right-left)*s:.0f}')


j = f'{base}/{V}.json'  # el plan que usa el editor es el de la raiz
P = json.load(open(j))
P['avatar'] = {'src': f'avatar/{V}_key.mov', 'key': True, 's': round(s, 5), 'x': round(x), 'y': round(y)}
json.dump(P, open(j, 'w'), ensure_ascii=False, indent=1)
print('  plan actualizado:', P['avatar'])
