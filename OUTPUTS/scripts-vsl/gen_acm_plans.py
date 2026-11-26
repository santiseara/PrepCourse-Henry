# -*- coding: utf-8 -*-
"""Planes de los 6 ads de la Guia Puertas de ACM Rentables (LATAM, 2026-11-26),
clonando el formato B de orbitadigital2026.com (AcademiaPractica.com).

Medido sobre sus 20 creativos de video (19 transcriptos) y 5 hojas de contactos:
  - 9:16, 22 a 39 s, voz en off de MUJER y cama musical suave por debajo.
  - 100 % b-roll del oficio. Hay operarios trabajando; nadie habla a camara.
  - SUBTITULOS abajo, 2 palabras, mayuscula, la que suena en CIAN #38E8DB, sin caja.
  - PASTILLA VERDE LIMA #CFF80E con el nombre del producto, al medio, cuando la voz lo nombra.
  - Sin titular, sin chips, sin placa de cierre.
  - El ritmo del ganador es de 185-196 palabras por minuto: el speed de cada video sale de
    dividir ese objetivo por el ritmo crudo del wav (regla del 25/11).

Uso: python3 gen_acm_plans.py <workdir>
"""
import os, sys, json, subprocess, wave

WK = sys.argv[1]
sys.path.insert(0, WK)
from vent_acm import VENT

SEG = 2.2          # sus cortes van de 1,8 a 2,6 s
TOPE = 8
PPM_OBJ = 188.0    # el ritmo de su locutora, medido sobre sus transcripciones

CIAN = '&H00DBE838&'   # #38E8DB en BGR: el color de la palabra que suena en sus subtitulos
NEGRO = '&H00000000&'

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


def velocidad(n):
    """El speed sale del ritmo real del wav, no de un numero fijo (regla del 25/11)."""
    wav = os.path.join(WK, f'voces/V{n}.wav')
    txt = os.path.join(WK, f'guiones/V{n}.txt')
    with wave.open(wav) as w:
        d = w.getnframes() / w.getframerate()
    pal = len(open(txt).read().split())
    crudo = pal / d * 60
    return round(min(max(PPM_OBJ / crudo, 0.95), 1.22), 3), round(d, 1), round(crudo)


VIDEOS = [
    # el hook de 1 y 2 es el DUPLICADO del ganador: no se toca
    dict(n=1, sfx=[]),
    dict(n=2, sfx=[]),
    dict(n=3, sfx=[]),
    dict(n=4, sfx=[]),
    dict(n=5, sfx=[]),
    dict(n=6, sfx=[]),
]

PRIMEROS = json.load(open(os.path.join(WK, 'primeros.json'))) if os.path.exists(os.path.join(WK, 'primeros.json')) else {}

for v in VIDEOS:
    n = v['n']
    pool, clips = pool_y_clips()
    sp, dcrudo, ppm = velocidad(n)
    plan = dict(
        vo=f'voces/V{n}.wav', script=f'guiones/V{n}.txt', lang='es',
        speed=sp, silence=[0.26, 0.12], cut=[1.8, 2.2, 2.6], words=2,
        music='cama.wav', music_db=-6, duck=6,
        hi=CIAN, hibox=NEGRO, hibord=0, capy=1480, pop=True, italic=False, margin=70,
        font='Montserrat ExtraBold', fsize=72, spacing=2, outline=6, shadow=3,
        seed=n * 977, usage='usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool,
        sfx=v['sfx'],
        overlays=[dict(type='pastilla', text='Guía Puertas de ACM Rentables',
                       word='Guía', occ=0, y=0.47, dur=3.2)])
    fk = PRIMEROS.get(str(n))
    if fk:
        plan['first'] = [fk, next(s[1] for s in pool if s[0] == fk)]
    json.dump(plan, open(os.path.join(WK, f'V{n}.json'), 'w'), ensure_ascii=False, indent=1)
    print(f'V{n} listo - {len(pool)} tramos, {len(clips)} clips - '
          f'voz {dcrudo}s a {ppm} ppm, speed {sp} -> {dcrudo / sp:.1f}s')
