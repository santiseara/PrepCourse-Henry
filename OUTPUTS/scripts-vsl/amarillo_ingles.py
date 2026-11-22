# -*- coding: utf-8 -*-
"""Saca de las ventanas los tramos donde ELLOS tienen su subtitulo quemado.

Su subtitulo es blanco con UNA PALABRA EN AMARILLO fuerte, en la banda y 0,60-0,80 del cuadro.
Las hojas son pastel: un amarillo saturado ahi abajo solo aparece cuando esta su subtitulo.
Medido: 1.967 pixeles amarillos con subtitulo, 0 sin el.

Uso: python3 amarillo_ingles.py <workdir> [parte] [de]
"""
import os, sys, json, glob, subprocess
import numpy as np
from PIL import Image

W = sys.argv[1]
PARTE = int(sys.argv[2]) if len(sys.argv) > 2 else 0
DE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
FF = os.path.expanduser('~/bin/ffmpeg')
FPS = 2
UMBRAL = 250          # pixeles amarillos en la banda
MIN = 2.5             # tramo minimo util
tmp = W + '/_am%d' % PARTE; os.makedirs(tmp, exist_ok=True)

vent = {}
for p in sorted(glob.glob(W + '/vent_orig*.json')):
    vent.update(json.load(open(p)))

res = {}
vids = sorted(vent)[PARTE::DE]
for vid in vids:
    v = vent[vid]
    if not v.get('ventanas'): continue
    for f in glob.glob(tmp + '/*.png'): os.remove(f)
    subprocess.run([FF, '-v', 'error', '-y', '-i', '%s/orig/%s.mp4' % (W, vid),
                    '-vf', 'crop=560:256:80:768,fps=%d,scale=280:-2' % FPS,
                    tmp + '/a_%05d.png'], check=False)
    frames = sorted(glob.glob(tmp + '/a_*.png'))
    sucio = []
    for p in frames:
        a = np.asarray(Image.open(p).convert('RGB')).astype(int)
        r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
        n = int(((r > 215) & (g > 170) & (b < 120) & (r - b > 110)).sum())
        sucio.append(n > UMBRAL / 4)       # la banda va a la mitad de ancho: umbral /4
    limpias = []
    for w in v['ventanas']:
        a0, b0 = w[0], w[1]
        i, ini = int(a0 * FPS), None
        fin = min(int(b0 * FPS), len(sucio))
        for k in range(i, fin + 1):
            malo = sucio[k] if k < len(sucio) else True
            if k < fin and not malo:
                if ini is None: ini = k
            else:
                if ini is not None:
                    a, b = ini / FPS, k / FPS
                    if b - a >= MIN:
                        limpias.append([round(a + 0.15, 2), round(b - 0.15, 2), w[2] if len(w) > 2 else []])
                    ini = None
    res[vid] = dict(dur=v['dur'], ventanas=limpias,
                    limpio=round(sum(x[1] - x[0] for x in limpias), 1),
                    antes=v.get('limpio', 0))
    print(vid, v.get('limpio', 0), '->', res[vid]['limpio'], 's', flush=True)
json.dump(res, open(W + '/vent_final%d.json' % PARTE, 'w'), ensure_ascii=False, indent=1)
