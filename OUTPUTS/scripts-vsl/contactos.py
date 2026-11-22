# -*- coding: utf-8 -*-
"""Hoja de contactos para mirar un pool de clips (la medicion no decide sola, regla del 22/11).
Un cuadro al 35 %, 55 % y 75 % de cada clip, con el numero de orden quemado.
Uso: python3 contactos.py <workdir> <lista.txt de ids> <salida_base> [cols] [filas]
"""
import os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

W, LISTA, BASE = sys.argv[1], sys.argv[2], sys.argv[3]
COLS = int(sys.argv[4]) if len(sys.argv) > 4 else 6
FILAS = int(sys.argv[5]) if len(sys.argv) > 5 else 4
FF = os.path.expanduser('~/bin/ffmpeg')
CW, CH = 196, 348
MOMENTOS = (0.35, 0.65)
tmp = W + '/_cont'; os.makedirs(tmp, exist_ok=True)
FONT = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'

def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0

ids = [l.strip() for l in open(LISTA) if l.strip() and not l.startswith('#')]
celdas = []
for i, vid in enumerate(ids, 1):
    p = '%s/clips/%s.mp4' % (W, vid)
    if not os.path.exists(p): continue
    D = dur(p)
    tira = Image.new('RGB', (CW, CH * len(MOMENTOS)), (20, 20, 24))
    for j, k in enumerate(MOMENTOS):
        f = '%s/f%d.jpg' % (tmp, j)
        subprocess.run([FF, '-v', 'error', '-y', '-ss', str(max(0.1, D * k)), '-i', p, '-vframes', '1',
                        '-vf', 'scale=%d:%d:force_original_aspect_ratio=decrease,pad=%d:%d:(ow-iw)/2:(oh-ih)/2'
                        % (CW, CH, CW, CH), f], check=False)
        if os.path.exists(f):
            tira.paste(Image.open(f), (0, j * CH))
            os.remove(f)
    d = ImageDraw.Draw(tira)
    d.rectangle((0, 0, 74, 40), fill=(255, 215, 0))
    d.text((8, 4), str(i), font=ImageFont.truetype(FONT, 30), fill=(0, 0, 0))
    celdas.append(tira)

por_hoja = COLS * FILAS
for h in range((len(celdas) + por_hoja - 1) // por_hoja):
    hoja = Image.new('RGB', (CW * COLS, CH * len(MOMENTOS) * FILAS), (10, 10, 12))
    for n, c in enumerate(celdas[h * por_hoja:(h + 1) * por_hoja]):
        hoja.paste(c, ((n % COLS) * CW, (n // COLS) * CH * len(MOMENTOS)))
    out = '%s_%d.jpg' % (BASE, h + 1)
    hoja.save(out, quality=82)
    print(out, hoja.size)
