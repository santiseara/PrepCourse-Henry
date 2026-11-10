# -*- coding: utf-8 -*-
"""Planes de los 6 ads de The Party Box Vault (mercado ingles, 2026-11-10).

Clonado de Moldes Prontos / caixinha cenario (page 1288335281030909, 51 ads activos).
La edicion del ganador, sacada de la hoja de contactos de 10 de sus videos:
  - b-roll de manos armando y llenando cajitas, el producto en pantalla todo el tiempo
  - subtitulos de UNA palabra, texto negro dentro de una caja AMARILLA, abajo al centro
  - sin caja de hook ni placa de apertura
  - insertos del producto (la carpeta de moldes, el indice) con un chip grande encima
  - voz en off de mujer, cierre con "Clique em Saiba Mais"

Uso: python3 gen_boxes_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/party-box-vault/anuncios/work')
SEG = 2.8
TOPE = 8

VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_boxes.py')).read())

GFX = {'1': 'libreria.png', '2': 'celular.png', '3': 'armado.png', '4': 'calendario.png'}
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


NEGRO = '&H00000000&'       # texto de la palabra activa: negro, como el ganador
AMARILLO = '&H0000E8FF&'    # caja amarilla #FFE800 en BGR: el resalte del ganador

CIERRE = dict(type='end', occ=0,
              head=['TAP BELOW'],
              sub='and print your first box tonight',
              cta='See every theme inside',
              sub2='300+ templates · assembly video · First Sale Kit · 100 ready messages',
              img='gfx/celular_solo.png')

VIDEOS = [
    dict(n=1, first=['E', 0.0], last='s', cta='Tap', gfx='132',
         anchors=[('hundred', 0, '1', 0), ('video', 0, '3', 0), ('Kit', 0, '2', 0)],
         tags=[('printer', 0, 'PRINTER · CARD STOCK · SCISSORS'),
               ('measurements', 0, 'THE MEASUREMENTS ARE THE PRODUCT')],
         chips=[('birthday', 0, 'A birthday every week')],
         plan=None),
    dict(n=2, first=['h', 7.0], last='l', cta='link', gfx='13',
         anchors=[('themes', 0, '1', 0), ('drawn', 0, '3', 0)],
         tags=[('crooked', 0, 'CROOKED · WRONG SIZE · WASTED PAPER')],
         chips=[('scissors', 0, 'Scissors and glue')],
         plan=('fixed', 0, 'WHAT ACTUALLY FIXED IT', 'Not practice. A finished file.',
               ['Measurements already done', 'Artwork already drawn', 'No cutting machine', 'Say yes the same day'])),
    dict(n=3, first=['i', 0.0], last='q', cta='Tap', gfx='14',
         anchors=[('templates', 0, '1', 0), ('calendar', 0, '4', 0)],
         tags=[('season', 0, 'A PRODUCT WITH NO SEASON')],
         chips=[('cake', 0, 'Everybody sells the cake')],
         plan=('month', 0, 'EVERY SINGLE MONTH', 'Somebody is handing out favors',
               ['Birthdays', 'Baby showers', 'Graduations', 'Christmas'])),
    dict(n=4, first=['j', 0.0], last='n', cta='Tap', gfx='13',
         anchors=[('measured', 0, '1', 0), ('video', 0, '3', 0)],
         tags=[('triple', 0, 'SAME MUG · TRIPLE THE PRICE')],
         chips=[('folding', 0, 'Four minutes of folding')],
         plan=None),
    dict(n=5, first=['c', 5.0], last='t', cta='Tap', gfx='12',
         anchors=[('templates', 0, '1', 0), ('messages', 0, '2', 0)],
         tags=[('catalog', 0, 'NOT TALENT · A CATALOG')],
         chips=[('tonight', 0, 'Photograph them tonight')],
         plan=None),
    dict(n=6, first=['m', 0.0], last='i', cta='Tap', gfx='132',
         anchors=[('templates', 0, '1', 0), ('phone', 0, '2', 0), ('Fold', 0, '3', 0)],
         tags=[('creative', 0, 'THEY DID NOT QUIT BECAUSE OF TALENT')],
         chips=[('scissors', 0, 'Scissors, not software')],
         plan=('theme', 0, 'THE WHOLE JOB', 'Four steps, that is all of it',
               ['Pick a theme', 'Print it', 'Cut it', 'Fold it'])),
]

for v in VIDEOS:
    pool, clips = pool_y_clips(v['gfx'], TODOS)
    overlays = [dict(type='tag', word=w, occ=o, text=t, dur=2.4) for w, o, t in v['tags']]
    overlays += [dict(type='chip', word=w, occ=o, text=t, dur=2.2) for w, o, t in v['chips']]
    if v.get('plan'):
        w, o, lab, tit, rows = v['plan']
        overlays.append(dict(type='plan', word=w, occ=o, label=lab, title=tit, rows=rows))
    fin = dict(CIERRE); fin['word'] = v['cta']
    overlays.append(fin)
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='en',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=1,
        music='music/bed_activo.wav', music_db=-9,
        hi=NEGRO, hibox=AMARILLO, hibord=20, capy=1340,
        first=v.get('first'), last=v.get('last'), seed=v['n'] * 211, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=overlays)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - %d tramos' % (v['n'], len(pool)))
