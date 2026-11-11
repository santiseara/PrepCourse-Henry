# -*- coding: utf-8 -*-
"""Planes de los 6 ads de la oferta de displays de papel (LATAM, 2026-11-11).

Competidor: Decorarina / Fabrica de Displays (decorarina.com), ~110 ads activos, el mas viejo
del 19 de septiembre. Corre en portugues, espanol LATAM e ingles a la vez.

Santiago: *"vamos a competir en el mismo mercado... tenemos que hacer cosas nuevas y mejores"*.
Asi que de ellos se toman los ANGULOS ganadores y nada mas:
  - no se copia una sola frase de sus guiones
  - no se copia su estetica (ellos: UGC real con sus displays, pastel de fiesta infantil,
    subtitulo chico con la palabra activa en AMARILLO sin caja, placa de marca a mitad del video)
  - nuestro visual es b-roll de TikTok del oficio + insertos dibujados por codigo, con
    papel crema / tinta azul noche / naranja quemado, y subtitulo de 3 palabras con la palabra
    activa en una CAJA tinta sobre texto crema.

Sin cifras en moneda: sale a varios paises de LATAM a la vez (regla del 2026-11-08).

Uso: python3 gen_displays_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/displays-de-papel/anuncios/work')
SEG = 2.9
TOPE = 8

VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_displays.py')).read())

GFX = {'1': 'tamanos.png', '2': 'costos.png', '3': 'biblioteca.png', '4': 'celular.png'}
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


CREMA = '&H00E6F1F7&'       # texto de la palabra activa: papel crema #F7F1E6 en BGR
TINTA = '&H003A2A1B&'       # caja detras de la palabra activa: azul noche #1B2A3A en BGR

CIERRE = dict(type='end', occ=0,
              head=['TOCA ABAJO'],
              sub='y arma tu primer display esta semana',
              cta='Ver el paso a paso completo',
              sub2='Curso en video · ~2.000 imágenes · 13 formas de vender · Soporte · Acceso de por vida',
              img='gfx/celular_solo.png')

VIDEOS = [
    dict(n=1, first=['a', 0.0], last='q', cta='clic', gfx='143',
         anchors=[('uniones', 0, '1', 0), ('video', 0, '4', 0), ('imágenes', 0, '3', 0)],
         tags=[('plotter', 0, 'SIN PLOTTER · SIN SUBLIMACIÓN')],
         chips=[('comedor', 0, 'La mesa del comedor')],
         plan=None),
    dict(n=2, first=['c', 0.0], last='y', cta='clic', gfx='21',
         anchors=[('siete', 0, '2', 0), ('paquete', 0, '1', 0)],
         tags=[('espera', 0, 'EL MISMO DÍA · SIN MÍNIMO DE PEDIDO')],
         chips=[('aparte', 0, 'Base y soporte, aparte')],
         plan=None),
    dict(n=3, first=['s', 10.0], last='h', cta='clic', gfx='134',
         anchors=[('Cincuenta', 0, '1', 0), ('banco', 0, '3', 0), ('video', 0, '4', 0)],
         tags=[('cajón', 0, 'UN PAQUETE DE HOJAS · TODO TU INVENTARIO')],
         chips=[],
         plan=('metro', 0, 'LA MISMA RESMA', 'Lo único que cambia es cuántas hojas',
               ['7 hojas · medio metro', '20 hojas · un metro', '50 hojas · dos metros'])),
    dict(n=4, first=['u', 0.0], last='w', cta='clic', gfx='13',
         anchors=[('técnica', 0, '1', 0), ('escenarios', 0, '3', 0)],
         tags=[('fecha', 0, 'IGLESIAS · VIDRIERAS · ESCUELAS')],
         chips=[('noviembre', 0, 'Diciembre se arma en noviembre')],
         plan=None),
    dict(n=5, first=['q', 0.0], last='z', cta='clic', gfx='43',
         anchors=[('curso', 0, '4', 0), ('banco', 0, '3', 0)],
         tags=[('diseñar', 0, 'NO HACE FALTA SABER DISEÑAR')],
         chips=[('celular', 0, 'Desde el celular')],
         plan=('tarde', 0, 'LO QUE SÍ HAY QUE SABER', 'Tres cosas, y se aprenden en una tarde',
               ['Elegir la imagen', 'Configurar la impresora una vez', 'Saber dónde cortar'])),
    dict(n=6, first=['m', 3.0], last='p', cta='clic', gfx='12',
         anchors=[('fábrica', 0, '1', 0), ('hojas', 0, '2', 0)],
         tags=[('doble', 0, 'EL TEMA QUE NADIE TIENE SE PAGA MÁS')],
         chips=[('mismo', 0, 'Cualquier tema, el mismo día')],
         plan=None),
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
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-9,
        hi=CREMA, hibox=TINTA, hibord=20, capy=1340,
        first=v.get('first'), last=v.get('last'), seed=v['n'] * 397, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=overlays)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - %d tramos' % (v['n'], len(pool)))
