# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Metodo Ganadero (LATAM, 2026-11-13).

Clonado de Correa Suelta / metodoganadero.com (AR): voz en off de campo en primera persona,
b-roll 100 % de hacienda real, subtitulos de 3 palabras con la palabra activa en amarillo o
verde lima (sin caja) y caja de hook ambar arriba en los primeros segundos.

Ellos NO muestran el producto: no hay mockups ni paginas del PDF. Lo que no se ve se cuenta
con placas de texto encima del b-roll.

Uso: python3 gen_ganadero_plans.py  -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/metodo-ganadero/anuncios/work')
SEG = 4.0
TOPE = 5

exec(open(os.path.join(WK, 'vent.py')).read())   # define VENT = {clave: (id, desde, hasta, extras)}


def pool_y_clips():
    pool, clips = [], {}
    for k, (vid, a, b, ex) in VENT.items():
        clips[k] = dict(src=f'tiktoks/tk_{vid}.mp4', fam=vid, **ex)
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


LIMA = '&H0000FC7C&'      # verde lima (BGR)
AMAR = '&H0000E8FF&'      # amarillo
NEGRO = '&H00000000&'     # "caja" negra = no se ve caja, solo el borde de siempre
CTA = 'TOCA EN MÁS INFORMACIÓN'

VIDEOS = [
    dict(n=1, hi=LIMA,
         hook='NO SÉ EXPLICARLE A MI HIJO CÓMO ELEGIR', hook_until='explicación',
         anchors=[],
         overlays=[dict(type='tag', word='costillar', text='COSTILLAR HONDO, PATAS CORTAS', dur=2.4, y=250),
                   dict(type='tag', word='pierna', text='MÁS ANCHA ABAJO QUE EN LA CADERA', dur=2.4, y=250),
                   dict(type='button', word='enlace', text=CTA, size=56, y=1560)]),
    dict(n=2, hi=AMAR,
         hook='ME TRAJE EL LOTE MÁS LINDO DE LA FERIA', hook_until='todos',
         anchors=[],
         overlays=[dict(type='tag', word='estado', text='LO QUE ESTÁ, NO LO QUE ES', dur=2.4, y=250),
                   dict(type='tag', word='estructura', text='LA ESTRUCTURA NO SE VA NUNCA', dur=2.4, y=250),
                   dict(type='button', word='Toca', text=CTA, size=56, y=1560)]),
    dict(n=3, hi=LIMA,
         hook='TENÍA EL TÍTULO Y NO LA RESPUESTA', hook_until='respuesta',
         anchors=[],
         overlays=[dict(type='tag', word='precocidad', text='PRIMERO LA PRECOCIDAD', dur=2.4, y=250),
                   dict(type='tag', word='disfraza', text='MÁS GORDO DISFRAZA', dur=2.2, y=250),
                   dict(type='button', word='enlace', text=CTA, size=56, y=1560)]),
    dict(n=4, hi=AMAR,
         hook='SE COME EL PASTO DE LA QUE SÍ RINDE', hook_until='rinde',
         anchors=[],
         overlays=[dict(type='tag', word='boca', text='DIENTES GASTADOS', dur=2.2, y=250),
                   dict(type='tag', word='caminar', text='SI PISA CORTO DE ATRÁS', dur=2.2, y=250),
                   dict(type='button', word='Toca', text=CTA, size=56, y=1560)]),
    dict(n=5, hi=LIMA,
         hook='PAREJO EN LA BALANZA NO ES PAREJO', hook_until='verdad',
         anchors=[],
         overlays=[dict(type='tag', word='cabecera', text='CABECERA Y FONDO', dur=2.4, y=250),
                   dict(type='tag', word='mitad', text='TE DURA LA MITAD', dur=2.2, y=250),
                   dict(type='button', word='enlace', text=CTA, size=56, y=1560)]),
    dict(n=6, hi=AMAR,
         hook='NO ES MEJOR OJO, ES OTRO ORDEN', hook_until='orden',
         anchors=[],
         overlays=[dict(type='tag', word='aplomos', text='UN JARRETE MAL ANGULADO', dur=2.4, y=250),
                   dict(type='tag', word='ombligo', text='EL OMBLIGO QUE NADIE MIRA', dur=2.4, y=250),
                   dict(type='button', word='Toca', text=CTA, size=56, y=1560)]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-9,
        hi=v['hi'], hibox=NEGRO, hibord=8, capy=1340,
        hook=v['hook'], hook_until=v['hook_until'],
        seed=v['n'] * 211, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=v['overlays'])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo · %d tramos' % (v['n'], len(pool)))
