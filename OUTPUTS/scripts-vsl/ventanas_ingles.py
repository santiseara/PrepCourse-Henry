# -*- coding: utf-8 -*-
"""Ventana util de cada clip elegido a ojo: el tramo mas largo SIN subtitulo quemado ni cara.

En este nicho el OCR encuentra texto en casi todos los cuadros, porque el tema ES papel escrito.
Lo que descalifica no es el texto de la hoja (chiquito) sino el SUBTITULO QUEMADO del creador:
grande (alto > 3,2 % del cuadro) o ancho y centrado. Se mide cuadro por cuadro y se devuelve el
tramo limpio mas largo.

Uso: python3 ventanas_ingles.py <workdir> <lista.txt> [parte] [de]
"""
import os, sys, re, glob, json, subprocess
W, LISTA = sys.argv[1], sys.argv[2]
PARTE = int(sys.argv[3]) if len(sys.argv) > 3 else 0
DE = int(sys.argv[4]) if len(sys.argv) > 4 else 1
S = os.path.dirname(os.path.abspath(__file__))
FF = os.path.expanduser('~/bin/ffmpeg')
SCAN = S + '/scanbin2'
tmp = W + '/_vent%d' % PARTE; os.makedirs(tmp, exist_ok=True)
ALTO_CAP = 0.075          # un renglon mas alto que esto ya no es texto de hoja: es cartel
MIN = 2.2                 # ventana minima util

def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0

ids = [l.split('#')[0].strip() for l in open(LISTA)]
ids = [i for i in ids if i][PARTE::DE]
out = {}
for vid in ids:
    p = '%s/clips/%s.mp4' % (W, vid)
    D = dur(p)
    for f in glob.glob(tmp + '/*.jpg'): os.remove(f)
    subprocess.run([FF, '-v', 'error', '-y', '-i', p, '-vf', 'fps=2,scale=640:-2',
                    tmp + '/f_%04d.jpg'], check=False)
    frames = sorted(glob.glob(tmp + '/f_*.jpg'))
    if not frames:
        out[vid] = dict(dur=D, a=0.5, b=min(D - 0.3, 6), nota='sin cuadros'); continue
    o = subprocess.run([SCAN], input='\n'.join(frames) + '\n', capture_output=True,
                       text=True, timeout=900).stdout
    sucio = {}
    for ln in o.strip().split('\n'):
        pr = ln.split('\t')
        if len(pr) < 3 or pr[1] == 'ERR': continue
        k = int(re.search(r'f_(\d+)\.jpg', pr[0]).group(1)) - 1
        malo = pr[1].startswith('FACES=') and int(pr[1][6:]) > 0
        for t in pr[2].split('||'):
            if not t.strip(): continue
            c = t.split(';')
            if len(c) < 4: continue
            h, an, mx = float(c[0]), float(c[1]), float(c[2])
            # cartel quemado = renglon ANCHO y CENTRADO, o un renglon enorme.
            # El texto impreso en la hoja es angosto o esta fuera del centro.
            if h > ALTO_CAP or (an > 0.45 and 0.28 < mx < 0.72):
                malo = True
        sucio[k] = malo
    n = len(frames)
    mejor, largo, ini = (0, 0), 0, None
    for k in range(n + 1):
        if k < n and not sucio.get(k, False):
            if ini is None: ini = k
        else:
            if ini is not None:
                if k - ini > largo: largo, mejor = k - ini, (ini, k)
                ini = None
    a, b = mejor[0] / 2.0, mejor[1] / 2.0
    limpio = largo / 2.0
    if limpio < MIN:
        out[vid] = dict(dur=D, a=None, b=None, limpio=limpio, nota='sin ventana limpia')
    else:
        out[vid] = dict(dur=D, a=round(a + 0.15, 2), b=round(min(b - 0.15, D - 0.15), 2), limpio=limpio)
    print(vid, out[vid], flush=True)
json.dump(out, open(W + '/ventanas%d.json' % PARTE, 'w'), indent=1)
