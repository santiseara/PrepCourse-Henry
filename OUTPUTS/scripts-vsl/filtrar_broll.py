# -*- coding: utf-8 -*-
"""Filtro del pool de b-roll de comida: tira los clips con TEXTO QUEMADO o CARAS.
El doc de la oferta es tajante: b-roll de comida puro, ni una sola cara.
Un cuadro cada 1,5 s, OCR + deteccion de caras con Vision (scanbin).
Uso: python3 filtrar.py <workdir>
"""
import os, sys, json, subprocess, glob, collections
W = sys.argv[1]
S = os.path.dirname(os.path.abspath(__file__))
FF = os.path.expanduser('~/bin/ffmpeg')
SCAN = S + '/scanbin'
PASO = 1.5
tmp = W + '/_filtro'; os.makedirs(tmp, exist_ok=True)

def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    for ln in r.split('\n'):
        if 'Duration:' in ln:
            h, m, s = ln.split('Duration:')[1].split(',')[0].strip().split(':')
            return int(h) * 3600 + int(m) * 60 + float(s)
    return 0.0

clips = sorted(glob.glob(W + '/clips/*.mp4'))
log = open(W + '/filtrar.log', 'w')
res = {}
for i, p in enumerate(clips, 1):
    vid = os.path.basename(p)[:-4]
    D = dur(p)
    if D < 4:
        res[vid] = dict(ok=False, why='clip de menos de 4 s', dur=round(D, 1))
        print('%3d/%d %s FUERA %s' % (i, len(clips), vid, res[vid]['why']), file=log, flush=True); continue
    for f in glob.glob(tmp + '/*.jpg'): os.remove(f)
    subprocess.run([FF, '-v', 'error', '-y', '-i', p, '-vf', f'fps=1/{PASO},scale=720:-2',
                    tmp + '/f_%03d.jpg'], check=False)
    frames = sorted(glob.glob(tmp + '/f_*.jpg'))
    if not frames:
        res[vid] = dict(ok=False, why='no se pudo leer', dur=round(D, 1))
        print('%3d/%d %s FUERA no se pudo leer' % (i, len(clips), vid), file=log, flush=True); continue
    try:
        o = subprocess.run([SCAN], input='\n'.join(frames) + '\n', capture_output=True,
                           text=True, timeout=240).stdout
    except Exception as e:
        o = ''
    textos, con_texto, con_cara, leidos = collections.Counter(), 0, 0, 0
    for ln in o.strip().split('\n'):
        if not ln.strip(): continue
        parts = ln.split('\t')
        if len(parts) < 3 or parts[1] == 'ERR': continue
        leidos += 1
        if parts[1].startswith('FACES=') and int(parts[1][6:]) > 0: con_cara += 1
        ts = [t.strip() for t in parts[2].split('||') if len(t.strip()) >= 3]
        if ts:
            con_texto += 1
            for t in ts: textos[t[:46]] += 1
    n = max(leidos, 1)
    pt, pc = con_texto / n, con_cara / n
    ok, why = True, ''
    if leidos == 0:
        ok, why = False, 'el escaner no pudo leer ningun cuadro'
    elif pt > 0.25:
        ok, why = False, 'texto quemado %d/%d: %s' % (con_texto, n, ' | '.join(t for t, _ in textos.most_common(3)))
    elif pc > 0.30:
        ok, why = False, 'caras %d/%d cuadros' % (con_cara, n)
    res[vid] = dict(ok=ok, why=why, dur=round(D, 1), n=n, texto=con_texto, cara=con_cara,
                    textos=[t for t, _ in textos.most_common(4)])
    print('%3d/%d %s %s %s' % (i, len(clips), vid, 'OK  ' if ok else 'FUERA', why), file=log, flush=True)
json.dump(res, open(W + '/veredicto.json', 'w'), ensure_ascii=False, indent=1)
g = sum(1 for v in res.values() if v['ok'])
print('FIN %d clips, pasan %d, se caen %d' % (len(res), g, len(res) - g), file=log, flush=True)
print('FIN %d clips, pasan %d, se caen %d' % (len(res), g, len(res) - g))
