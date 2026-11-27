# -*- coding: utf-8 -*-
"""Filtro denso del pool de Navidad 3D (Argentina): ventana limpia de cada clip.

Nicho de oficio donde el creador SE FILMA (tutoriales de impresion 3D), asi que ademas de la ventana
se cuenta la cara sobre el CLIP ENTERO (regla del 23/11): 8+ cuadros con cara y se cae el clip.
El ad es en INGLES, asi que un cartel en otro alfabeto tambien lo tira (regla del 30/10).

--- cabecera original ---
Filtro denso del pool de Alivio en Cada Plato: busca la VENTANA LIMPIA mas larga de cada clip.

Corre a 1 cuadro por segundo desde la primera pasada (regla del 22/11: el filtro barato cuesta
cuatro re-renders) y busca las tres cosas juntas:
  - TEXTO quemado (OCR de Vision, scanbin)
  - CARAS (Vision) -> el ganador no muestra una sola cara
  - BANDAS NEGRAS internas (clip apaisado dentro de un lienzo 9:16): mas del 10 % del alto
Ademas tira el clip entero si el OCR nombra al ENEMIGO del pitch (azucar, harina, gluten)
o una marca de agua (@usuario, "link in bio", "follow").

Salida: <workdir>/vent_n3d.py con VENT = {'cNN': ('<id>', ini, fin), ...} y el log.
Uso: python3 ventanas_alivio.py <workdir>
"""
import os, sys, json, glob, subprocess, collections
from PIL import Image

W = sys.argv[1]
WK_I = int(sys.argv[2]) if len(sys.argv) > 2 else 0
WK_N = int(sys.argv[3]) if len(sys.argv) > 3 else 1
S = os.path.dirname(os.path.abspath(__file__))
FF = os.path.expanduser('~/bin/ffmpeg')
SCAN = os.path.join(S, 'scanbin')
MIN_VENT = 4.5          # una ventana util no baja de esto
tmp = os.path.join(W, '_vent%s%d' % (os.environ.get('SUF',''), WK_I)); os.makedirs(tmp, exist_ok=True)

# El enemigo del pitch: lo que vendemos es SIN harina y SIN azucar, asi que un plano que
# muestre harina o azucar en pantalla es el argumento contrario (regla del 19/11). Ojo: la
# negacion lo da vuelta -> "sugar free" y "sin azucar" son NUESTRO argumento, no el contrario.
ENEMIGO = ()      # en este nicho no hay un objeto que contradiga el pitch
NEGACION = ()
MARCA = ('link in bio', 'follow me', 'follow for', 'subscribe', '@', '.com', 'etsy', 'shop now',
         'tiktok shop', 'discount code', 'use code', 'makerworld', 'printables', 'thingiverse',
         'patreon', 'cults3d', 'my store', 'order now', 'sale', 'link en bio', 'seguime',
         'mi tienda', 'envios', 'env\u00edos', 'descuento', 'pedidos por')
TOPE_CARAS = 8    # cuadros con cara en el CLIP ENTERO antes de tirarlo (regla del 23/11)
UMBRAL_ENTERO = 0.22   # un cartel que vive en menos de esto se recorta con la ventana, no tira el clip


def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    for ln in r.split('\n'):
        if 'Duration:' in ln:
            h, m, s = ln.split('Duration:')[1].split(',')[0].strip().split(':')
            return int(h) * 3600 + int(m) * 60 + float(s)
    return 0.0


def bandas(path):
    """% del alto ocupado por filas casi negras pegadas al borde de arriba y de abajo."""
    im = Image.open(path).convert('L').resize((80, 320))
    px = im.load()
    def fila_negra(y):
        return sum(px[x, y] for x in range(80)) / 80 < 18
    arriba = 0
    while arriba < 160 and fila_negra(arriba): arriba += 1
    abajo = 0
    while abajo < 160 and fila_negra(319 - abajo): abajo += 1
    # letterbox real = bandas en los DOS bordes
    return (min(arriba, abajo) * 2) / 320.0


LISTA = os.environ.get('LISTA')     # opcional: solo estos ids (un id por linea)
if LISTA:
    ids = [l.strip() for l in open(LISTA) if l.strip()]
    clips = [os.path.join(W, 'clips', i + '.mp4') for i in ids]
    clips = [c for c in clips if os.path.exists(c)]
else:
    clips = sorted(glob.glob(os.path.join(W, 'clips', '*.mp4')))
clips = [p for j, p in enumerate(clips) if j % WK_N == WK_I]
SUF = os.environ.get('SUF', '')
log = open(os.path.join(W, 'ventanas%s%d.log' % (SUF, WK_I)), 'w')
res = {}
for i, p in enumerate(clips, 1):
    vid = os.path.basename(p)[:-4]
    D = dur(p)
    if D < 6:
        res[vid] = dict(ok=False, why='dura %.1f s' % D)
        print('%3d/%d %s FUERA dura %.1f s' % (i, len(clips), vid, D), file=log, flush=True); continue
    for f in glob.glob(tmp + '/*.jpg'): os.remove(f)
    subprocess.run([FF, '-v', 'error', '-y', '-i', p, '-vf', 'fps=1,scale=720:-2,format=yuv420p',
                    '-pix_fmt', 'yuvj420p', tmp + '/f_%03d.jpg'], check=False)
    frames = sorted(glob.glob(tmp + '/f_*.jpg'))
    if not frames:
        res[vid] = dict(ok=False, why='no se pudo leer')
        print('%3d/%d %s FUERA no se pudo leer' % (i, len(clips), vid), file=log, flush=True); continue
    try:
        o = subprocess.run([SCAN], input='\n'.join(frames) + '\n', capture_output=True,
                           text=True, timeout=300).stdout
    except Exception:
        o = ''
    sucio = [True] * len(frames)        # por defecto sucio: si no se leyo, no se usa
    textos = collections.Counter()
    idx = {os.path.abspath(f): k for k, f in enumerate(frames)}
    n_enemigo = n_marca = n_caras = 0
    ej_enemigo = ej_marca = ''
    for ln in o.strip().split('\n'):
        if not ln.strip(): continue
        parts = ln.split('\t')
        if len(parts) < 3 or parts[1] == 'ERR': continue
        k = idx.get(os.path.abspath(parts[0]))
        if k is None: continue
        caras = int(parts[1][6:]) if parts[1].startswith('FACES=') else 0
        ts = [t.strip() for t in parts[2].split('||') if len(t.strip()) >= 3]
        for t in ts:
            textos[t[:46]] += 1
            tl = t.lower()
            if any(e in tl for e in ENEMIGO) and not any(ng in tl for ng in NEGACION):
                n_enemigo += 1; ej_enemigo = ej_enemigo or t[:40]
            if any(mm in tl for mm in MARCA):
                n_marca += 1; ej_marca = ej_marca or t[:40]
        # el ad es en INGLES: un cartel en otro alfabeto tira el cuadro igual que uno en ingles
        sucio[k] = bool(ts) or caras > 0 or bandas(frames[k]) > 0.10
        if caras > 0: n_caras += 1
    nf = max(len(frames), 1)
    fuera_entero = ''
    if n_caras >= TOPE_CARAS:
        fuera_entero = 'cara del creador en %d/%d cuadros del clip entero' % (n_caras, nf)
    if fuera_entero: pass
    elif n_enemigo / nf > UMBRAL_ENTERO:
        fuera_entero = 'enemigo del pitch en %d/%d cuadros: %s' % (n_enemigo, nf, ej_enemigo)
    elif n_marca / nf > UMBRAL_ENTERO:
        fuera_entero = 'marca del creador en %d/%d cuadros: %s' % (n_marca, nf, ej_marca)
    if fuera_entero:
        res[vid] = dict(ok=False, why=fuera_entero)
        print('%3d/%d %s FUERA %s' % (i, len(clips), vid, fuera_entero), file=log, flush=True); continue
    # tramo limpio mas largo
    mejor = (0, 0, 0)   # largo, ini, fin
    j = 0
    while j < len(sucio):
        if sucio[j]: j += 1; continue
        k = j
        while k < len(sucio) and not sucio[k]: k += 1
        if k - j > mejor[0]: mejor = (k - j, j, k)
        j = k
    largo, a, b = mejor
    # el cuadro k cubre [k, k+1): se recorta medio segundo de cada borde por seguridad
    ini, fin = a + 0.4, min(b + 0.6, D - 0.2)
    sucios = sum(sucio)
    if fin - ini < MIN_VENT:
        res[vid] = dict(ok=False, why='ventana limpia de %.1f s (%d/%d cuadros sucios): %s'
                        % (max(fin - ini, 0), sucios, len(sucio), ' | '.join(t for t, _ in textos.most_common(2))))
        print('%3d/%d %s FUERA %s' % (i, len(clips), vid, res[vid]['why']), file=log, flush=True); continue
    res[vid] = dict(ok=True, ini=round(ini, 2), fin=round(fin, 2), dur=round(D, 1),
                    sucios=sucios, n=len(sucio))
    print('%3d/%d %s OK   %.1f-%.1f (%.1f s limpios de %.1f)'
          % (i, len(clips), vid, ini, fin, fin - ini, D), file=log, flush=True)

json.dump(res, open(os.path.join(W, 'ventanas%s%d.json' % (SUF, WK_I)), 'w'), ensure_ascii=False, indent=1)
buenos = [k for k, v in res.items() if v.get('ok')]
print('FIN %d clips, ventana limpia en %d' % (len(res), len(buenos)))
print('FIN %d clips, ventana limpia en %d' % (len(res), len(buenos)), file=log, flush=True)
