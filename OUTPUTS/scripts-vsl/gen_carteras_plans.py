# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Carteras Maison / el Metodo Riviera (Argentina, 2026-11-10).

Clonado de Maison Luxe Bags (maisonluxebags.impultienda.ar): 100 % b-roll de carteras de
canamazo reales, subtitulos de 2 palabras en mayuscula con la palabra activa en MAGENTA sin
caja, placa de texto arriba y los insertos del producto (gfx_carteras.py) anclados a la palabra
que los nombra.

Uso: python3 gen_carteras_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/carteras-maison/anuncios/work')
SEG = 3.0
TOPE = 8

VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_carteras.py')).read())

GFX = {'1': 'tapa.png', '2': 'moldes.png', '3': 'materiales.png', '4': 'bonos.png', '5': 'celular.png'}
TODOS = ''.join(VENT.keys())


def pool_y_clips(gfx_keys, claves):
    pool, clips = [], {}
    for k in claves:
        fn, a, b, ex = VENT[k]
        d = dict(src=f'clips/{fn}.mp4'); d.update(ex)
        clips[k] = d
        tramos, t = [], a
        while t < b - 1.6:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    for k in gfx_keys:
        clips[k] = dict(src=f'gfx/{GFX[k]}', fam='gfx' + k, still=True)
        pool.append([k, 0, 3.2])
    return pool, clips


MAGENTA = '&H006F35D4&'     # #D4356F en BGR: el resalte de Maison Luxe Bags
NEGRO = '&H00000000&'       # sin caja: el borde sigue siendo negro

CIERRE = dict(type='end', occ=0,
              head=['TOCÁ ABAJO'],
              sub='y empezá tu primera cartera esta noche',
              cta='Ver todo lo que hay adentro',
              sub2='250+ moldes · 25 clases en video · 5 bonos de regalo',
              img='gfx/celular_solo.png')

VIDEOS = [
    dict(n=1, cta='Tocá', gfx='124', first=['b', 0.0], last='s',
         anchors=[('Maison', 0, '1', 0), ('moldes', 0, '2', 0), ('bonos', 0, '4', 0)],
         tags=[('fácil', 0, 'SIN MÁQUINA DE COSER'),
               ('amigas', 0, 'PRIMERO LAS AMIGAS')],
         money=('cincuenta', 0, 'CADA CARTERA', '50.000 PESOS', ''),
         plan=None),
    dict(n=2, cta='Tocá', gfx='12', first=['e', 0.0], last='t',
         anchors=[('Maison', 0, '1', 0), ('moldes', 0, '2', 0)],
         tags=[('detalles', 0, 'EL SECRETO SON LOS DETALLES'),
               ('herrajes', 0, 'FORRO ADENTRO · HERRAJES AFUERA')],
         money=None,
         plan=None),
    dict(n=3, cta='Tocá', gfx='312', first=['g', 3.0], last='q',
         anchors=[('plancha', 0, '3', 0), ('Maison', 0, '1', 0), ('moldes', 0, '2', 0)],
         tags=[('todo', 1, 'SIN MÁQUINA · SIN CUERO'),
               ('mercería', 0, 'SE CONSIGUE ACÁ')],
         money=None,
         plan=None),
    dict(n=4, cta='Tocá', gfx='123', first=['d', 18.0], last='e',
         anchors=[('Maison', 0, '1', 0), ('moldes', 0, '2', 0), ('materiales', 0, '3', 0)],
         tags=[('despertador', 0, 'SIN DESPERTADOR'),
               ('cocina', 0, 'LA MESA DE LA COCINA')],
         money=None,
         plan=None),
    dict(n=5, cta='Tocá', gfx='124', first=['u', 3.0], last='t',
         anchors=[('Maison', 0, '1', 0), ('moldes', 0, '2', 0), ('bonos', 0, '4', 0)],
         tags=[('perderte', 0, 'QUÉ AGUJERO · QUÉ COLOR')],
         money=None,
         plan=('oficial', 0, 'TRES DÍAS, UNA CARTERA', 'La apuesta',
               ['Día 1: contás y cortás', 'Día 2: fila por fila', 'Día 3: forro, cierre, cadena'])),
    dict(n=6, cta='Tocá', gfx='12', first=['s', 0.0], last='e',
         anchors=[('Maison', 0, '1', 0), ('moldes', 0, '2', 0)],
         tags=[('molde', 0, 'MISMO MATERIAL · OTRO MOLDE'),
               ('experiencia', 0, 'SIN EXPERIENCIA')],
         money=None,
         plan=None),
]

for v in VIDEOS:
    pool, clips = pool_y_clips(v['gfx'], TODOS)
    overlays = [dict(type='tag', word=w, occ=o, text=t, dur=2.4) for w, o, t in v['tags']]
    if v.get('money'):
        w, o, lab, a_, b_ = v['money']
        overlays.append(dict(type='money', word=w, occ=o, label=lab, left=a_, right=b_, y=1430))
    if v.get('plan'):
        w, o, lab, tit, rows = v['plan']
        overlays.append(dict(type='plan', word=w, occ=o, label=lab, title=tit, rows=rows))
    fin = dict(CIERRE); fin['word'] = v['cta']
    overlays.append(fin)
    plan = dict(
        vo=f"voz/V{v['n']}.wav", script=f"txt/V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=2,
        music='music/bed_activo.wav', music_db=-9,
        hi=MAGENTA, hibox=NEGRO, hibord=8, capy=1300,
        first=v['first'], last=v['last'], seed=v['n'] * 173, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=overlays)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - %d tramos' % (v['n'], len(pool)))
