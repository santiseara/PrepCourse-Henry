# -*- coding: utf-8 -*-
"""Hoja de contactos de las VENTANAS del pool (ya recortadas arriba del watermark).
Dos cuadros por ventana, numeradas igual que el indice que imprime el script.
Uso: python3 hoja_ventanas.py <workdir> <salida_base> [cols] [filas]
"""
import os, sys, glob, json, subprocess
from PIL import Image, ImageDraw, ImageFont
W, BASE = sys.argv[1], sys.argv[2]
COLS = int(sys.argv[3]) if len(sys.argv) > 3 else 8
FILAS = int(sys.argv[4]) if len(sys.argv) > 4 else 3
FF = os.path.expanduser('~/bin/ffmpeg')
CROP = 'crop=576:1024:72:0'
CW, CH = 186, 330
FONT = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
tmp = W + '/_hv'; os.makedirs(tmp, exist_ok=True)

vent = {}
for p in sorted(glob.glob(W + '/vent_orig*.json')):
    vent.update(json.load(open(p)))

filas = []
for vid, v in sorted(vent.items()):
    for w in (v.get('ventanas') or []):
        filas.append((vid, w[0], w[1]))
json.dump([[a, b, c] for a, b, c in filas], open(W + '/indice_ventanas.json', 'w'), indent=0)

celdas = []
for i, (vid, a, b) in enumerate(filas, 1):
    p = '%s/orig/%s.mp4' % (W, vid)
    col = Image.new('RGB', (CW, CH * 2), (18, 18, 22))
    for j, k in enumerate((0.25, 0.75)):
        t = a + (b - a) * k
        f = '%s/h.jpg' % tmp
        subprocess.run([FF, '-v', 'error', '-y', '-ss', '%.2f' % t, '-i', p, '-vframes', '1',
                        '-vf', '%s,scale=%d:%d' % (CROP, CW, CH), f], check=False)
        if os.path.exists(f):
            col.paste(Image.open(f), (0, j * CH)); os.remove(f)
    d = ImageDraw.Draw(col)
    d.rectangle((0, 0, 70, 34), fill=(255, 215, 0))
    d.text((5, 2), str(i), font=ImageFont.truetype(FONT, 26), fill=(0, 0, 0))
    celdas.append(col)

por = COLS * FILAS
for h in range((len(celdas) + por - 1) // por):
    hoja = Image.new('RGB', (CW * COLS, CH * 2 * FILAS), (10, 10, 12))
    for n, c in enumerate(celdas[h * por:(h + 1) * por]):
        hoja.paste(c, ((n % COLS) * CW, (n // COLS) * CH * 2))
    out = '%s_%d.jpg' % (BASE, h + 1)
    hoja.save(out, quality=80); print(out, hoja.size)
print('ventanas:', len(filas))
