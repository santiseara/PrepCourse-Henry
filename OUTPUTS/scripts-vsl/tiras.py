# -*- coding: utf-8 -*-
"""Tira de N cuadros repartidos en todo el clip, una columna por clip.
Para decidir a ojo si tiene cartel quemado en algun momento.
Uso: python3 tiras.py <workdir> <lista.txt> <salida_base> [clips_por_hoja] [cuadros]
"""
import os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
W, LISTA, BASE = sys.argv[1], sys.argv[2], sys.argv[3]
POR = int(sys.argv[4]) if len(sys.argv) > 4 else 8
N = int(sys.argv[5]) if len(sys.argv) > 5 else 6
FF = os.path.expanduser('~/bin/ffmpeg')
CW, CH = 180, 320
tmp = W + '/_tira'; os.makedirs(tmp, exist_ok=True)
FONT = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0
ids = [l.split('#')[0].strip() for l in open(LISTA) if l.split('#')[0].strip()]
cols = []
for i, vid in enumerate(ids, 1):
    p = '%s/clips/%s.mp4' % (W, vid)
    if not os.path.exists(p): continue
    D = dur(p)
    col = Image.new('RGB', (CW, CH * N), (18, 18, 22))
    for j in range(N):
        t = D * (j + 0.5) / N
        f = '%s/t.jpg' % tmp
        subprocess.run([FF, '-v', 'error', '-y', '-ss', '%.2f' % t, '-i', p, '-vframes', '1', '-vf',
                        'scale=%d:%d:force_original_aspect_ratio=decrease,pad=%d:%d:(ow-iw)/2:(oh-ih)/2'
                        % (CW, CH, CW, CH), f], check=False)
        if os.path.exists(f):
            col.paste(Image.open(f), (0, j * CH)); os.remove(f)
    d = ImageDraw.Draw(col)
    d.rectangle((0, 0, 66, 36), fill=(255, 215, 0))
    d.text((6, 2), str(i), font=ImageFont.truetype(FONT, 28), fill=(0, 0, 0))
    cols.append(col)
for h in range((len(cols) + POR - 1) // POR):
    hoja = Image.new('RGB', (CW * POR, CH * N), (10, 10, 12))
    for n, c in enumerate(cols[h * POR:(h + 1) * POR]):
        hoja.paste(c, (n * CW, 0))
    out = '%s_%d.jpg' % (BASE, h + 1)
    hoja.save(out, quality=80); print(out, hoja.size)
