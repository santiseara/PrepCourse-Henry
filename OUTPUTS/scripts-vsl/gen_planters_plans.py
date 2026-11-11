# -*- coding: utf-8 -*-
"""Planes de los 6 ads de From Concrete to Cash (mercado ingles, 2026-11-11).

Clonado de "De Cemento a Dinero" (AR, page 1312841241922512, 35 ads activos del 5 al 9/11).
La edicion de ellos, sacada de la hoja de contactos de sus videos:
  - 100 % b-roll de macetas de cemento, el producto en pantalla todo el tiempo
  - subtitulos de 3 palabras, blancos en mayuscula, la palabra activa en AMARILLO, sin caja
  - sin placa de apertura, sin insertos de producto, sin placa de cierre: cierran con el subtitulo
  - voz en off de mujer, cierre con "Toca el boton de mas informacion"

Uso: python3 gen_planters_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/concrete-planters/anuncios/work')
SEG = 2.8
TOPE = 8

VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_planters.py')).read())
TODOS = ''.join(VENT.keys())

AMARILLO = '&H0000E8FF&'   # #FFE800 en BGR: la palabra activa del ganador
NEGRO = '&H00000000&'      # el borde negro de siempre (sin caja de color)


def pool_y_clips(claves, off=0.0):
    pool, clips = [], {}
    for k in claves:
        fn, a, b, ex = VENT[k]
        d = dict(src='clips/%s.mp4' % fn); d.update(ex)
        clips[k] = d
        tramos, t = [], a + (off if b - a > off + SEG + 1.6 else 0)
        while t < b - 1.2:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


VIDEOS = [
    dict(n=1, seed=411, first=None, last=None, off=0.0,
         anchors=[('mold', 0, None, 0)]),
    dict(n=2, seed=422, first=None, last=None, off=1.4, anchors=[]),
    dict(n=3, seed=433, first=None, last=None, off=0.7, anchors=[]),
    dict(n=4, seed=444, first=None, last=None, off=2.1, anchors=[]),
    dict(n=5, seed=455, first=None, last=None, off=1.0, anchors=[]),
    dict(n=6, seed=466, first=None, last=None, off=1.7, anchors=[]),
]


def _first(pool, k):
    if not k: return None
    seg = next((x for x in pool if x[0] == k), None)
    if seg is None: raise SystemExit('first %r no esta en el pool' % k)
    return [seg[0], seg[1]]


for v in VIDEOS:
    pool, clips = pool_y_clips(TODOS, v['off'])
    plan = dict(
        vo='vo/V%d.wav' % v['n'], script='V%d.txt' % v['n'], lang='en',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-9,
        hi=AMARILLO, hibox=NEGRO, hibord=8, capy=1340,
        seed=v['seed'], usage='usage.json',
        clips=clips, pool=pool,
        anchors=[a for a in v['anchors'] if a[2]],
        overlays=[],
    )
    if v['first']: plan['first'] = _first(pool, v['first'])
    if v['last']: plan['last'] = v['last']
    json.dump(plan, open(os.path.join(WK, 'V%d.json' % v['n']), 'w'), indent=1)
    print('V%d  %d tramos  %d clips' % (v['n'], len(pool), len(clips)))
