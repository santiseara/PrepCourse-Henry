# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Navidad en Macrame (LATAM, 2026-11-14).

Modelada de **emprender con manualidades** / `navidadenmacrame.impultienda.ar`: 26 creativos
distintos y 58 ads activos, el mas viejo del 15/10. Se bajaron y transcribieron 10 de sus
videos y se armo la hoja de contactos de los 3 mas duplicados (13, 10 y 10 copias).

Su edicion, que es la que se clona:
  - 100 % b-roll de macrame navideno, manos trabajando, sin una sola foto de relleno.
  - **Sin banda de hook** arriba: arrancan directo con el subtitulo.
  - Subtitulos de **3 palabras** en mayuscula, blancos con borde negro, y la palabra que suena
    **dentro de una caja magenta** redondeada, a la altura del 75 %.
  - El producto aparece dos veces por video (la tapa y las paginas internas del PDF), anclado
    a la palabra que lo nombra. Nosotros lo dibujamos por codigo (`gfx_macrame.py`).
  - **Sin placa de cierre**: terminan con el subtitulo del CTA sobre el ultimo plano. Nosotros
    agregamos solo la pastilla del CTA encima del b-roll, sin tapar la imagen.

Santiago, el 14/11: *"es para LATAM, asi que usa acento neutro"*. Los guiones van en **espanol
neutro sin voseo** y **sin cifra en moneda** (regla del 2026-11-08 de Quesos LATAM). El acento
de la voz se verifico con Gemini: "latinoamericano neutro, tutea, sin argentinismos".

Uso: python3 gen_macrame_plans.py   -> escribe N1.json .. N6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/navidad-macrame/anuncios/work')
# El Escritorio esta sincronizado con iCloud y durante esta tanda vacio diez clips del pool
# (tamano en el `ls`, cero bytes en el disco, "Error reading"), lo que mata el render con el
# AttributeError del Duration. Por eso los clips se leen de una carpeta LOCAL: se pasa en
# CLIPS_DIR. Sin la variable, se usa la de siempre.
CLIPS = os.environ.get('CLIPS_DIR', 'clips')
SEG = 3.0
TOPE = 8

VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_macrame.py')).read())

GFX = {'1': 'tapa.png', '2': 'proyecto.png', '3': 'categorias.png', '4': 'nudos.png', '5': 'bonos.png'}
TODOS = ''.join(VENT.keys())

BLANCO = '&H00FFFFFF&'      # texto de la palabra activa: blanco, como ellos
MAGENTA = '&H00E84BD1&'     # caja de la palabra activa (BGR de #D14BE8), el unico color de sus ads


def pool_y_clips(gfx_keys, claves):
    pool, clips = [], {}
    for k in claves:
        fn, a, b, ex = VENT[k]
        d = dict(src=f'{CLIPS}/{fn}.mp4'); d.update(ex)
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


VIDEOS = [
    dict(n=1, first=['w', 0.0], last='1', gfx='134',
         anchors=[('cien', 0, '3', 0), ('nudos', 0, '4', 0)],
         cta='QUIERO MI NAVIDAD 🎄'),
    dict(n=2, first=['p', 0.0], last='1', gfx='135',
         anchors=[('cien', 0, '3', 0), ('bonos', 0, '5', 0)],
         cta='QUIERO MI MESA ASÍ 🎄'),
    dict(n=3, first=['q', 0.0], last='1', gfx='135',
         anchors=[('cien', 0, '3', 0), ('bonos', 0, '5', 0)],
         cta='QUIERO EMPEZAR HOY 🎄'),
    dict(n=4, first=['b', 0.0], last='1', gfx='125',
         anchors=[('lugar', 0, '2', 0), ('bonos', 0, '5', 0)],
         cta='VER TODO LO QUE INCLUYE 🎄'),
    dict(n=5, first=['e', 0.0], last='1', gfx='134',
         anchors=[('cien', 0, '3', 0), ('nudos', 0, '4', 0)],
         cta='QUIERO HACER LOS REGALOS 🎄'),
    dict(n=6, first=['c', 0.0], last='1', gfx='124',
         anchors=[('nudos', 1, '4', 0), ('proyecto', 0, '2', 0)],
         cta='QUIERO EMPEZAR HOY 🎄'),
]

for v in VIDEOS:
    pool, clips = pool_y_clips(v['gfx'], TODOS)
    overlays = [dict(type='button', word='clic', occ=0, text=v['cta'], y=1600, size=56)]
    plan = dict(
        vo=f"vo/N{v['n']}.wav", script=f"N{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-9, whoosh=[],
        hi=BLANCO, hibox=MAGENTA, hibord=18, capy=1450,
        first=v.get('first'), last=v.get('last'), seed=7400 + v['n'] * 457, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=overlays)
    json.dump(plan, open(f"{WK}/N{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('N%d listo - %d tramos' % (v['n'], len(pool)))
