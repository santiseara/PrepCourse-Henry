# -*- coding: utf-8 -*-
"""Planes de los 6 ads de The 3D Method (mercado ingles, 2026-11-26), clonando el formato de
Metodo 3D - Juan Avalos (metodo3d.shop, fanpage "Metodo 3D - Juan Avalos").

Medido sobre sus 99 ads activos, 112 creativos de video bajados y 24 transcriptos (26/11):
  - 25 a 45 s, 9:16, voz en off de HOMBRE (F0 110-124 Hz) y cama musical por debajo.
  - 100 % b-roll del nicho. Cero caras hablando a camara.
  - BANNER FIJO de dos pastillas arriba (roja + amarilla), pegado todo el video.
  - TITULAR de arranque: renglon blanco + renglon en PASTILLA ROJA.
  - PASTILLA ROJA numerada para las listas, PASTILLA VERDE para el numero de plata.
  - SUBTITULOS de 3 palabras, la que suena en AMARILLO #FDD400 (sin caja).
  - BARRA DE PROGRESO amarilla abajo. Cierre con pastilla roja "INSTANT ACCESS".

El ritmo final apunta a 188 ppm (tope de la banda que valido Santiago el 24/11); el ganador
lee a 205-213 ppm, asi que el speed de cada video sale de dividir, no es fijo.

Uso: python3 gen_m3d_plans.py <workdir>
"""
import os, sys, json, wave

WK = sys.argv[1]
sys.path.insert(0, WK)
from vent_m3d import VENT

SEG = 2.3
TOPE = 8
PPM = 188.0

AMARILLO = '&H0000D4FD&'     # #FDD400 en BGR: el amarillo de su banner y de su palabra resaltada
NEGRO    = '&H00000000&'

AUTOR = json.load(open(os.path.join(WK, 'autores.json'))) if os.path.exists(os.path.join(WK, 'autores.json')) else {}


def velocidad(n):
    """Speed por video para que el montaje final caiga en PPM (regla del 25/11:
    el 1.20 no es fijo, es un objetivo de ritmo). A speed 1.00 el final sale a 0.988 del crudo."""
    w = wave.open(os.path.join(WK, 'voces', 'V%d.wav' % n))
    crudo = len(open(os.path.join(WK, 'guiones', 'V%d.txt' % n)).read().split()) / (w.getnframes() / w.getframerate()) * 60
    return round(min(1.30, max(0.84, PPM / (crudo * 0.988))), 2)


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src='clips/%s.mp4' % vid, fam=AUTOR.get(vid, vid), **ex)
        tramos, t = [], a
        while t < b - 1.2:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


# Su banner fijo de arriba: renglon rojo con la oferta, renglon amarillo con las condiciones.
BANNER = dict(l1='+90,000 STL FILES + FULL COURSE', l2='ONE-TIME PAYMENT - INSTANT ACCESS', y=96, size=46)
BANNER_XMAS = dict(l1='CHRISTMAS ORNAMENTS + 90,000 DESIGNS', l2='ONE-TIME PAYMENT - INSTANT ACCESS', y=96, size=46)

# Su cierre vive los ultimos ~4 s y se mide DESDE EL FINAL (regla del 25/11), no por palabra.
END = dict(type='cta', l1='INSTANT ACCESS', l2='Tap Learn more', y=1150, from_end=4.2)

VIDEOS = [
    # 1 - su ad n.º 1 por impresiones (30/10) sobre su CUERPO VALIDADO (el mismo en 10 de sus 20 mas vistos)
    dict(n=1, banner=BANNER,
         hook='WANT TO PRINT SOMETHING|EVERYONE ASKS YOU FOR?', hasta=('zip', 0),
         overlays=[
             dict(type='chip', text='sorted by category', icon='\U0001F4C1', word='category', occ=0, dur=2.6),
             dict(type='chip', text='new designs every month', icon='\U0001F504', word='month', occ=0, dur=2.6),
         ]),
    # 2 - su ad n.º 2 por impresiones (16/11): la cuenta del adorno navideno
    dict(n=2, banner=BANNER_XMAS,
         hook='THE MATH BEHIND ONE|3D PRINTED ORNAMENT', hasta=('ornaments', 0),
         overlays=[
             dict(type='money', left='UNDER $1 OF FILAMENT', word='dollar', occ=0, dur=2.6, y=980),
             dict(type='money', left='SELLS FOR $15', word='fifteen', occ=0, dur=2.6, y=980),
         ]),
    # 3 - su formato de lista numerada, el que corre en dos mercados a la vez (3 y 17)
    dict(n=3, banner=BANNER,
         hook='3 MISTAKES|EVERY BEGINNER MAKES', hasta=('printing', 0),
         overlays=[
             dict(type='step', text='MISTAKE #1', word='one', occ=0, dur=2.4, y=300),
             dict(type='step', text='MISTAKE #2', word='two', occ=0, dur=2.4, y=300),
             dict(type='step', text='MISTAKE #3', word='three', occ=1, dur=2.4, y=300),
         ]),
    # 4 - los flexis: su angulo de producto mas reconocible (ad 6)
    dict(n=4, banner=BANNER,
         hook='ONE PIECE.|NOTHING TO GLUE.', hasta=('touch', 0),
         overlays=[
             dict(type='chip', text='flexi & articulated category', icon='\U0001F409', word='category', occ=0, dur=2.6),
         ]),
    # 5 - la cuenta del valor (ad 19): lo que costarian sueltos
    dict(n=5, banner=BANNER,
         hook='WHAT WOULD YOU PAY|FOR 90,000 DESIGNS?', hasta=('3D', 0),
         overlays=[
             dict(type='money', left='ONE BY ONE', right='$200,000', word='models', occ=0, dur=2.8, y=980),
             dict(type='money', left='THE 3D METHOD', right='DIRT CHEAP', word='serious', occ=0, dur=2.8, y=980),
         ]),
    # 6 - lo de todos los dias tambien se vende (ad 7b)
    dict(n=6, banner=BANNER,
         hook="YOU DON'T HAVE TO PRINT|THE HARDEST THING", hasta=('too', 0),
         overlays=[
             dict(type='chip', text='stands - organizers - planters', icon='\U0001F3E0', word='planters', occ=0, dur=2.6),
         ]),
]

PRIMEROS = json.load(open(os.path.join(WK, 'primeros.json'))) if os.path.exists(os.path.join(WK, 'primeros.json')) else {}

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo='voces/V%d.wav' % v['n'], script='guiones/V%d.txt' % v['n'], lang='en',
        speed=velocidad(v['n']), silence=[0.26, 0.12], cut=[1.8, 2.1, 2.5], words=3,
        music='music/bed.wav', music_db=-6, duck=6.0,
        hi=AMARILLO, hibox=NEGRO, hibord=0, capy=1480, pop=True, italic=False, margin=60,
        font='Montserrat ExtraBold', fsize=70, spacing=2, outline=5, shadow=3,
        banner=v['banner'],
        hook=v['hook'], hook_size=104, hook_y=290,
        hook_until=v['hasta'][0], hook_until_occ=v['hasta'][1],
        chip_y=1300, step_size=118, progress=True,
        seed=v['n'] * 1301, usage='usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool,
        overlays=v['overlays'] + [dict(END)])
    fk = PRIMEROS.get(str(v['n']))
    if fk:
        plan['first'] = [fk, next(s[1] for s in pool if s[0] == fk)]
    json.dump(plan, open(os.path.join(WK, 'V%d.json' % v['n']), 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - speed %.2f, %d tramos, %d clips' % (v['n'], plan['speed'], len(pool), len(clips)))
