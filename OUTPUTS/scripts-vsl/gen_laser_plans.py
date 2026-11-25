# -*- coding: utf-8 -*-
"""Planes de los 6 ads de The Laser Profit Vault (mercado ingles, 2026-11-25),
clonando el formato B de Taller Laser Rentable (mikitlaser.auracreativadigital.com).

Medido sobre 13 de sus ~37 ads activos (bajados y transcriptos el 25/11) y 4 hojas de contactos:
  - 9:16, 23 a 49 s, voz en off de hombre y cama musical por debajo.
  - 100 % b-roll del nicho (laser cortando, lamparas, relojes, manos armando). Cero caras.
  - TITULAR de 2 renglones arriba los primeros segundos: renglon 1 blanco, renglon 2 AMARILLO,
    sin caja, con borde negro.
  - CHIPS NEGROS redondeados ARRIBA con emoji, anclados a la palabra que los nombra.
  - SUBTITULOS abajo, 4 palabras, mayuscula, la que suena en AMARILLO (sin caja).
  - PLACA AMARILLA de cierre con el CTA.
  - Efectos: solo los que dispara el editor (pop del chip, chaching del numero, ding del cierre).

Uso: python3 gen_laser_plans.py <workdir>
"""
import os, sys, json

WK = sys.argv[1]
sys.path.insert(0, WK)
from vent_laser import VENT

SEG = 2.3
TOPE = 8

AMARILLO = '&H0000C7FF&'     # #FFC700, el amarillo de sus titulares y subtitulos
NEGRO    = '&H00000000&'

AUTOR = json.load(open(os.path.join(WK, 'autores.json'))) if os.path.exists(os.path.join(WK, 'autores.json')) else {}


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src=f'clips/{vid}.mp4', fam=AUTOR.get(vid, vid), **ex)
        tramos, t = [], a
        while t < b - 1.2:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


END = dict(type='cta', l1='INSTANT ACCESS', l2='Tap the button 👇', y=1120,
           word='button', occ=0)

VIDEOS = [
    dict(n=1, hook='SAME LASER.|DIFFERENT RESULTS.', hasta=('wattage', 0), overlays=[
        dict(type='chip', text='20 categories, ready to cut', icon='📁', word='categories', occ=0, dur=2.6),
        dict(type='money', left='1 SHEET', right='$40', label='AT A WEEKEND MARKET', word='forty', occ=0, dur=2.6),
    ]),
    dict(n=2, hook='YOUR LASER EARNS NOTHING|SITTING THERE SWITCHED OFF', hasta=('off', 0), overlays=[
        dict(type='chip', text='profit calculator', icon='💲', word='calculator', occ=0, dur=2.4),
        dict(type='chip', text='7-day plan to your first sale', icon='📅', word='plan', occ=0, dur=2.6),
        dict(type='money', left='ONE SATURDAY', right='MACHINE PAID OFF', word='paid', occ=0, dur=2.6),
    ]),
    dict(n=3, hook="YOU DON'T NEED|TO LEARN DESIGN", hasta=('thing', 0), overlays=[
        dict(type='chip', text='SVG · DXF · CDR · PDF', icon='📁', word='clean', occ=0, dur=2.6),
        dict(type='money', left='1 ORNAMENT', right='$18', word='eighteen', occ=0, dur=2.6),
    ]),
    dict(n=4, hook='STOP RUINING|GOOD SHEETS', hasta=('fault', 0), overlays=[
        dict(type='chip', text='calibration + LightBurn settings', icon='⚙️', word='calibration', occ=0, dur=2.6),
        dict(type='money', left='PLYWOOD', right='$4 A SHEET', word='four', occ=0, dur=2.6),
    ]),
    dict(n=5, hook='WHAT YOU CUT IN NOVEMBER|YOU SELL IN DECEMBER', hasta=('sales', 0), overlays=[
        dict(type='money', left='1 SHEET', right='11 SALES', word='eleven', occ=0, dur=2.6),
        dict(type='chip', text='Christmas market playbook', icon='🎄', word='playbook', occ=0, dur=2.6),
    ]),
    dict(n=6, hook='SAME THREE KEYCHAINS|SINCE FEBRUARY', hasta=('February', 0), overlays=[
        dict(type='chip', text='4 bonus collections', icon='🎁', word='bonus', occ=0, dur=2.6),
        dict(type='money', left='1 CLOCK', right='$60', word='sixty', occ=0, dur=2.6),
    ]),
]

PRIMEROS = json.load(open(os.path.join(WK, 'primeros.json'))) if os.path.exists(os.path.join(WK, 'primeros.json')) else {}

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"voces/V{v['n']}.wav", script=f"guiones/V{v['n']}.txt", lang='en',
        speed=1.20, silence=[0.26, 0.12], cut=[1.9, 2.2, 2.6], words=4,
        music='music/bed.wav', music_db=-11,
        hi=AMARILLO, hibox=NEGRO, hibord=0, capy=1430, pop=True, italic=False, margin=60,
        font='Montserrat ExtraBold', fsize=66, spacing=2, outline=5, shadow=3,
        hook=v['hook'], hook_size=96, hook_y=200,
        hook_until=v['hasta'][0], hook_until_occ=v['hasta'][1],
        chip_y=236,
        seed=v['n'] * 977, usage='usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool,
        overlays=v['overlays'] + [dict(END)])
    fk = PRIMEROS.get(str(v['n']))
    if fk:
        plan['first'] = [fk, next(s[1] for s in pool if s[0] == fk)]
    json.dump(plan, open(os.path.join(WK, f"V{v['n']}.json"), 'w'), ensure_ascii=False, indent=1)
    print("V%d listo - %d tramos, %d clips" % (v['n'], len(pool), len(clips)))
