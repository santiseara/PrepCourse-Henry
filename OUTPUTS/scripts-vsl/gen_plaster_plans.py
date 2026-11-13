# -*- coding: utf-8 -*-
"""Planes de los 6 ads de The Plaster & Concrete Guide (mercado ingles, 2026-11-13).

La edicion del ganador "Manualidades y Arte" (page 118274498039808), sacada de sus hojas de contactos:
  - 100 % b-roll real de manos trabajando el yeso y el cemento
  - subtitulo de UNA palabra, blanca, en pastilla FUCSIA opaca, centrada abajo
  - cartel de hook AMARILLO arriba en los primeros segundos
  - chip fucsia de cierre ("TAP BUY NOW" + "50% OFF") y SIN placa final de marca
  - voz en off de mujer

Uso: python3 gen_plaster_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/plaster-concrete/anuncios/work')
SEG = 2.6
TOPE = 7

VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_plaster.py')).read())
TODOS = list(VENT.keys())


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
    dict(n=1, seed=131, off=0.0, first='704007',
         hook='AN $80 TRAY FOR A DOLLAR OF PLASTER',
         anchors=[('terrazzo', 0, '704007', 0), ('chips', 0, '581957', 0),
                  ('cures', 0, '734917', 0), ('seal', 0, '708807', 0)],
         chip=('50% OFF + 7 BONUSES', 'below')),
    dict(n=2, seed=232, off=1.3, first='892229',
         hook='NO MONEY FOR GIFTS LAST DECEMBER',
         anchors=[('trays', 0, '892229', 0), ('wrapped', 0, '848658', 0),
                  ('packaging', 0, '684365', 0), ('mold', 0, '711506', 0)],
         chip=('50% OFF + 7 BONUSES', 'below')),
    dict(n=3, seed=333, off=0.6, first='922497',
         hook='3 MISTAKES CRACKING YOUR PIECES',
         anchors=[('water', 0, '922497', 0), ('colour', 0, '677703', 0),
                  ('curing', 0, '734917', 0), ('seal', 1, '708807', 0)],
         chip=('50% OFF + 7 BONUSES', 'below')),
    dict(n=4, seed=434, off=2.0, first='734917',
         hook='SAME MOLD. $14 OR $38.',
         anchors=[('finish', 0, '734917', 0), ('smooth', 0, '708807', 0),
                  ('packaging', 0, '848658', 0), ('pigmenting', 0, '677703', 0)],
         chip=('50% OFF + 7 BONUSES', 'below')),
    dict(n=5, seed=535, off=1.0, first='848658',
         hook='30 FAVORS DUE TOMORROW MORNING',
         anchors=[('favors', 0, '848658', 0), ('candle', 0, '934674', 0),
                  ('batch', 0, '934542', 0), ('pigment', 0, '677703', 0)],
         chip=('50% OFF + 7 BONUSES', 'below')),
    dict(n=6, seed=636, off=1.6, first='922497',
         hook="IT'S NOT TALENT. IT'S THE RATIOS.",
         anchors=[('mixes', 0, '922497', 0), ('terrazzo', 0, '677703', 0),
                  ('candles', 0, '483488', 0), ('difficulty', 0, '934542', 0)],
         chip=('50% OFF + 7 BONUSES', 'below')),
]


def _first(pool, k):
    seg = next((x for x in pool if x[0] == k), None)
    if seg is None: raise SystemExit('first %r no esta en el pool' % k)
    return [seg[0], seg[1]]


for v in VIDEOS:
    pool, clips = pool_y_clips(TODOS, v['off'])
    plan = dict(
        vo='vo/V%d.wav' % v['n'], script='V%d.txt' % v['n'], lang='en',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=1,
        music='music/bed.wav', music_db=-10,
        capy=1330, seed=v['seed'], usage='usage.json',
        clips=clips, pool=pool,
        hook=v['hook'],
        anchors=[a for a in v['anchors'] if a[2]],
        overlays=[dict(type='chip', text=v['chip'][0], word=v['chip'][1], occ=0, dur=3.2)],
        first=_first(pool, v['first']),
    )
    json.dump(plan, open(os.path.join(WK, 'V%d.json' % v['n']), 'w'), indent=1)
    print('V%d  %d tramos  %d clips' % (v['n'], len(pool), len(clips)))
