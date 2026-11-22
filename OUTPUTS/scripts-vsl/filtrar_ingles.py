# -*- coding: utf-8 -*-
"""Filtro denso del pool de b-roll de la oferta de ingles: tira TEXTO QUEMADO, CARAS
y BANDAS NEGRAS internas. Un cuadro por segundo desde la primera pasada (regla del 22/11).
Uso: python3 filtrar_ingles.py <workdir> [parte] [de]
"""
import os, sys, json, subprocess, glob, collections
W = sys.argv[1]
PARTE = int(sys.argv[2]) if len(sys.argv) > 2 else 0
DE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
S = os.path.dirname(os.path.abspath(__file__))
FF = os.path.expanduser('~/bin/ffmpeg')
SCAN = S + '/scanbin'
PASO = 1.0
tmp = W + '/_filtro%d' % PARTE; os.makedirs(tmp, exist_ok=True)

def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    for ln in r.split('\n'):
        if 'Duration:' in ln:
            h, m, s = ln.split('Duration:')[1].split(',')[0].strip().split(':')
            return int(h) * 3600 + int(m) * 60 + float(s)
    return 0.0

def bandas(p, D):
    """% del alto que ocupan las filas negras de arriba y abajo (cropdetect en 3 momentos)."""
    peor = 0.0
    for t in (D * 0.25, D * 0.5, D * 0.75):
        r = subprocess.run([FF, '-v', 'info', '-ss', str(t), '-i', p, '-t', '0.6',
                            '-vf', 'cropdetect=24:2:0', '-f', 'null', '-'],
                           capture_output=True, text=True).stderr
        linea = [l for l in r.split('\n') if 'crop=' in l]
        if not linea: continue
        c = linea[-1].split('crop=')[1].strip().split(':')
        try:
            w, h, x, y = (int(v) for v in c[:4])
        except ValueError:
            continue
        alto = None
        for l in r.split('\n'):
            if 'Video:' in l and 'x' in l:
                for tok in l.replace(',', ' ').split():
                    if 'x' in tok and tok.replace('x', '').isdigit():
                        try: alto = int(tok.split('x')[1])
                        except Exception: pass
                        break
                if alto: break
        if not alto: continue
        peor = max(peor, (alto - h) / alto)
    return peor

clips = sorted(glob.glob(W + '/clips/*.mp4'))[PARTE::DE]
log = open(W + '/filtrar%d.log' % PARTE, 'w')
res = {}
for i, p in enumerate(clips, 1):
    vid = os.path.basename(p)[:-4]
    D = dur(p)
    if D < 4 or D > 180:
        res[vid] = dict(ok=False, why='dura %.1f s' % D, dur=round(D, 1))
        print('%3d/%d %s FUERA %s' % (i, len(clips), vid, res[vid]['why']), file=log, flush=True); continue
    for fr in glob.glob(tmp + '/*.jpg'): os.remove(fr)
    paso = max(PASO, D / 22.0)
    subprocess.run([FF, '-v', 'error', '-y', '-i', p, '-vf', 'fps=1/%.3f,scale=640:-2' % paso,
                    tmp + '/f_%03d.jpg'], check=False)
    frames = sorted(glob.glob(tmp + '/f_*.jpg'))[:24]
    if not frames:
        res[vid] = dict(ok=False, why='no se pudo leer', dur=round(D, 1))
        print('%3d/%d %s FUERA no se pudo leer' % (i, len(clips), vid), file=log, flush=True); continue
    try:
        o = subprocess.run([SCAN], input='\n'.join(frames) + '\n', capture_output=True,
                           text=True, timeout=600).stdout
    except Exception:
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
    bn = 0.0
    ok, why = True, ''
    if leidos == 0:
        ok, why = False, 'el escaner no pudo leer ningun cuadro'
    elif pt > 0.22:
        ok, why = False, 'texto quemado %d/%d: %s' % (con_texto, n, ' | '.join(t for t, _ in textos.most_common(3)))
    elif pc > 0.25:
        ok, why = False, 'caras %d/%d cuadros' % (con_cara, n)
    elif (lambda: False)():
        pass
    elif (bn := bandas(p, D)) > 0.10:
        ok, why = False, 'bandas negras %.0f%% del alto' % (bn * 100)
    res[vid] = dict(ok=ok, why=why, dur=round(D, 1), n=n, texto=con_texto, cara=con_cara,
                    bandas=round(bn, 3), textos=[t for t, _ in textos.most_common(4)])
    print('%3d/%d %s %s %s' % (i, len(clips), vid, 'OK  ' if ok else 'FUERA', why), file=log, flush=True)
json.dump(res, open(W + '/veredicto%d.json' % PARTE, 'w'), ensure_ascii=False, indent=1)
g = sum(1 for v in res.values() if v['ok'])
print('FIN %d clips, pasan %d, se caen %d' % (len(res), g, len(res) - g), file=log, flush=True)
print('FIN %d clips, pasan %d, se caen %d' % (len(res), g, len(res) - g))
