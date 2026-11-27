# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Navidad 3D (Argentina, 2026-11-27), clonando el formato de
Atelie 3D (Brasil, page id 1358703690661118) medido sobre 12 de sus ~120 creativos.

  - 24 a 36 s en el ganador; aca 40 a 47 s porque Santiago pidio guiones mas largos (27/11).
  - 9:16, voz en off de MUJER (Sulafat) y cama musical por debajo.
  - 100 % b-roll del nicho. Cero caras hablando a camara.
  - BANNER FIJO de dos pastillas arriba, pegado todo el video.
  - TITULAR de arranque de dos renglones.
  - PASTILLA VERDE para el numero de plata, pastilla con icono para el beneficio.
  - SUBTITULOS de 3 palabras, la que suena en AMARILLO. BARRA DE PROGRESO abajo.
  - Cierre: "ACCESO INMEDIATO / Tocá Más información" los ultimos ~4 s.

Ritmo objetivo 200 ppm, que es como leen los dos ganadores del nicho (Atelie 3D y Metodo 3D
estan en 205-213). El speed de cada video sale de dividir.

Uso: python3 gen_n3d_plans.py <workdir>
"""
import os, sys, json, wave

WK = sys.argv[1]
sys.path.insert(0, WK)
from vent_n3d import VENT

SEG = 2.3
TOPE = 8
PPM = 200.0

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
# 27/11: Santiago: "bajalos un poco, hay formatos donde no se ven" + que se vayan a los 10-15 s.
# y=270 lo deja debajo de la UI de Reels/Stories (que se come ~14 % de arriba), y until=12 lo apaga.
BANNER = dict(l1='+400 ARCHIVOS STL DE NAVIDAD', l2='PAGO ÚNICO · ACCESO INMEDIATO', y=270, size=46, until=12)

# Su cierre vive los ultimos ~4 s y se mide DESDE EL FINAL (regla del 25/11), no por palabra.
END = dict(type='cta', l1='ACCESO INMEDIATO', l2='Tocá Más información', y=1150, from_end=4.2)

VIDEOS = [
    # V1 - el aguinaldo lo gasta alguien
    dict(n=1, banner=BANNER,
         hook='EN DICIEMBRE SE GASTA|EL AGUINALDO', hasta=('regalos', 0),
         overlays=[
             dict(type='money', left='SE GASTA', right='DEL 10 AL 24', word='aguinaldo', occ=1, dur=2.6, y=980),
             dict(type='chip', text='+400 archivos de Navidad', icon='📁', word='archivos', occ=0, dur=2.6),
         ]),
    # V2 - treinta piezas de un solo pedido
    dict(n=2, banner=BANNER,
         hook='TREINTA PIEZAS|DE UN SOLO PEDIDO', hasta=('adelantado', 0),
         overlays=[
             dict(type='money', left='UN PEDIDO', right='30 PIEZAS', word='pedido', occ=0, dur=2.6, y=980),
             dict(type='chip', text='la foto de cada modelo', icon='📸', word='foto', occ=1, dur=2.6),
         ]),
    # V3 - cobra antes de imprimir
    dict(n=3, banner=BANNER,
         hook='COBRÁ ANTES|DE IMPRIMIR', hasta=('puede', 0),
         overlays=[
             dict(type='money', left='COBRÁS PRIMERO', right='IMPRIMÍS DESPUÉS', word='revés', occ=0, dur=2.8, y=980),
             dict(type='chip', text='imprimís solo lo vendido', icon='✅', word='foto', occ=1, dur=2.6),
         ]),
    # V4 - el puesto de la feria
    dict(n=4, banner=BANNER,
         hook='EL PUESTO SE PAGA|CON SEIS ADORNOS', hasta=('vendés', 0),
         overlays=[
             dict(type='money', left='EL PUESTO SE PAGA', right='CON 6 ADORNOS', word='adornos', occ=0, dur=2.8, y=980),
             dict(type='chip', text='+400 modelos listos', icon='📁', word='modelos', occ=0, dur=2.6),
         ]),
    # V5 - las publicaciones que ya estan vendiendo
    dict(n=5, banner=BANNER,
         hook='ELLOS YA ESTÁN|VENDIENDO', hasta=('tuya', 0),
         overlays=[
             dict(type='chip', text='publicaciones que ya vendieron', icon='🔥', word='vendieron', occ=0, dur=2.6),
             dict(type='money', left='LAS QUE SUBEN EL 18', right='PÁGINA 4', word='página', occ=0, dur=2.6, y=980),
         ]),
    # V6 - quinientos pesos de plastico
    dict(n=6, banner=BANNER,
         hook='$500 DE PLÁSTICO|SE VENDE A $10.000', hasta=('mismo', 0),
         overlays=[
             dict(type='money', left='UN ROLLO', right='$22.000', word='rollo', occ=0, dur=2.4, y=980),
             dict(type='money', left='TE DA', right='40 ADORNOS', word='adornos', occ=0, dur=2.4, y=980),
             dict(type='money', left='TE DEVUELVE', right='x10 LO QUE PAGASTE', word='mitad', occ=0, dur=2.6, y=980),
         ]),
]

PRIMEROS = json.load(open(os.path.join(WK, 'primeros.json'))) if os.path.exists(os.path.join(WK, 'primeros.json')) else {}

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo='voces/V%d.wav' % v['n'], script='guiones/V%d.txt' % v['n'], lang='es',
        speed=velocidad(v['n']), silence=[0.26, 0.12], cut=[1.8, 2.1, 2.5], words=3,
        music='music/bed.wav', music_db=-6, duck=6.0,
        hi=AMARILLO, hibox=NEGRO, hibord=0, capy=1480, pop=True, italic=False, margin=60,
        font='Montserrat ExtraBold', fsize=70, spacing=2, outline=5, shadow=3,
        banner=v['banner'],
        hook=v['hook'], hook_size=104, hook_y=500,
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
