# -*- coding: utf-8 -*-
"""Encuentra los creativos que llevan un STICKER DE COMENTARIO o de PREGUNTA pegado encima.

Son cajas (negra con texto blanco, o blanca con avatar) en la mitad de arriba del cuadro, con
texto en portugues: "Qual sua duvida?", "Replying to @...", etc. Nada de eso puede quedar en un
ad argentino. Se escanea la banda de arriba del cuadro ya recortado y se busca la frase.

Uso: python3 stickers_ingles.py <workdir> [parte] [de]
"""
import os, sys, json, glob, subprocess
W = sys.argv[1]
PARTE = int(sys.argv[2]) if len(sys.argv) > 2 else 0
DE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
S = os.path.dirname(os.path.abspath(__file__))
FF = os.path.expanduser('~/bin/ffmpeg')
SCAN = S + '/scanbin2'
BANDA = 'crop=576:420:72:80'        # y 80-500 del original (mitad de arriba del recorte)
FRASES = ('replying', 'respondendo', 'sua duvida', 'sua dúvida', 'qual sua', 'consigo aprender',
          'eu nao sei', 'eu não sei', 'como voce', 'como você', 'tem o jeito', 'pronunciar as')
FPS = 1
tmp = W + '/_st%d' % PARTE; os.makedirs(tmp, exist_ok=True)

clips = sorted(glob.glob(W + '/orig/*.mp4'))[PARTE::DE]
res = {}
for p in clips:
    vid = os.path.basename(p)[:-4]
    for f in glob.glob(tmp + '/*.jpg'): os.remove(f)
    subprocess.run([FF, '-v', 'error', '-y', '-i', p, '-vf', '%s,fps=%d,scale=576:-2' % (BANDA, FPS),
                    tmp + '/s_%04d.jpg'], check=False)
    frames = sorted(glob.glob(tmp + '/s_*.jpg'))
    if not frames:
        res[vid] = dict(sticker=False); continue
    o = subprocess.run([SCAN], input='\n'.join(frames) + '\n', capture_output=True,
                       text=True, timeout=900).stdout
    sucios, muestra = set(), []
    for ln in o.strip().split('\n'):
        pr = ln.split('\t')
        if len(pr) < 3: continue
        k = int(pr[0].rsplit('s_', 1)[1][:4]) - 1
        for tx in pr[2].split('||'):
            c = tx.lstrip('|').split(';')
            if len(c) < 4: continue
            t = ';'.join(c[3:])
            if any(fr in t.lower() for fr in FRASES):
                sucios.add(k)
                if len(muestra) < 3: muestra.append(t[:40])
    res[vid] = dict(sticker=bool(sucios), segundos=sorted(sucios), textos=muestra)
    print(vid, 'STICKER' if sucios else 'ok', len(sucios), ' | '.join(muestra[:2]), flush=True)
json.dump(res, open(W + '/stickers%d.json' % PARTE, 'w'), ensure_ascii=False, indent=1)
