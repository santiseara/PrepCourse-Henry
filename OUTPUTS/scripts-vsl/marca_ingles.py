# -*- coding: utf-8 -*-
"""Tramos donde se ve GRANDE la marca del ganador (el logo "fluente com legenda" impreso en la hoja).

El @usuario chiquito impreso al pie de la hoja no molesta (regla del 22/11), pero el logo grande
cruzado sobre la pagina sí: es la marca del competidor adentro de nuestro ad. Se busca con OCR
cualquier texto que contenga "fluen"/"legend" con alto > 3,5 % del cuadro.

Uso: python3 marca_ingles.py <workdir> [parte] [de]
"""
import os, sys, json, glob, subprocess
W = sys.argv[1]
PARTE = int(sys.argv[2]) if len(sys.argv) > 2 else 0
DE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
S = os.path.dirname(os.path.abspath(__file__))
FF = os.path.expanduser('~/bin/ffmpeg')
SCAN = S + '/scanbin2'
CROP = 'crop=576:1024:72:0'
ALTO = 0.035
tmp = W + '/_mk%d' % PARTE; os.makedirs(tmp, exist_ok=True)

vent = {}
for p in sorted(glob.glob(W + '/vent_final*.json')):
    vent.update(json.load(open(p)))

res = {}
for vid in sorted(vent)[PARTE::DE]:
    v = vent[vid]
    if not v.get('ventanas'): continue
    for f in glob.glob(tmp + '/*.jpg'): os.remove(f)
    subprocess.run([FF, '-v', 'error', '-y', '-i', '%s/orig/%s.mp4' % (W, vid),
                    '-vf', '%s,fps=1,scale=576:-2' % CROP, tmp + '/m_%04d.jpg'], check=False)
    frames = sorted(glob.glob(tmp + '/m_*.jpg'))
    if not frames: continue
    o = subprocess.run([SCAN], input='\n'.join(frames) + '\n', capture_output=True,
                       text=True, timeout=900).stdout
    seg = set()
    for ln in o.strip().split('\n'):
        pr = ln.split('\t')
        if len(pr) < 3: continue
        k = int(pr[0].rsplit('m_', 1)[1][:4]) - 1
        for tx in pr[2].split('||'):
            c = tx.lstrip('|').split(';')
            if len(c) < 4: continue
            try: alto = float(c[0])
            except ValueError: continue
            t = ';'.join(c[3:]).lower()
            if alto > ALTO and ('fluen' in t or 'legend' in t):
                seg.add(k)
    res[vid] = sorted(seg)
    print(vid, 'MARCA en s' if seg else 'ok', sorted(seg)[:8], flush=True)
json.dump(res, open(W + '/marca%d.json' % PARTE, 'w'), indent=1)
