# -*- coding: utf-8 -*-
"""Planes de los 6 ads de +500 Actividades ABA Naturalistas (LATAM, 2026-11-27),
clonando el formato A de ABA Tools (en.abatools.pro/500-nap/).

Medido sobre 10 de sus creativos (10 transcriptos) y sus hojas de contactos:
  - 9:16, 45 a 55 s en total, voz en off de MUJER y cama musical por debajo.
  - 100 % b-roll de sesiones y materiales. Nadie habla a camara.
  - PASTILLA AZUL #0074FC fija ARRIBA (dos cajas, una por renglon) todo el video,
    con el nombre del producto. Arranca en y 0,098 del alto.
  - SUBTITULO de UNA sola palabra, blanco, ITALICA, mayuscula, con borde negro, en y 0,78.
  - PLACA NEGRA FINAL de ~5 s: "Toca en / Mas informacion" y la flecha violeta.
  - Sus cortes van de 2,4 a 3,4 s.
  - Su locutora lee a ~170 ppm: el speed de cada video sale de dividir ese objetivo
    por el ritmo crudo del wav (regla del 25/11).

Uso: python3 gen_aba_plans.py <workdir>
"""
import os, sys, json, wave

WK = sys.argv[1]
sys.path.insert(0, WK)
from vent_aba import VENT

SEG = 2.9          # sus cortes van de 2,4 a 3,4 s
TOPE = 6           # tope de recortes por clip (regla del 30/10: el pool se come la tanda)
PPM_OBJ = 170.0    # el ritmo de su locutora, medido sobre sus transcripciones
TAIL = 5.0         # los segundos de placa negra despues de que termina la voz

BLANCO = '&H00FFFFFF&'   # su subtitulo no resalta: es todo blanco

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
    wav = os.path.join(WK, f'voces/V{n}.wav')
    txt = os.path.join(WK, f'guiones/V{n}.txt')
    with wave.open(wav) as w:
        d = w.getnframes() / w.getframerate()
    pal = len(open(txt).read().split())
    crudo = pal / d * 60
    return round(min(max(PPM_OBJ / crudo, 0.95), 1.22), 3), round(d, 1), round(crudo)


for n in range(1, 7):
    pool, clips = pool_y_clips()
    sp, dcrudo, ppm = velocidad(n)
    plan = dict(
        vo=f'voces/V{n}.wav', script=f'guiones/V{n}.txt', lang='es',
        speed=sp, silence=[0.26, 0.12], cut=[2.4, 2.9, 3.4], words=1,
        tail=TAIL,
        music='cama.wav', music_db=-6, duck=6,
        hi=BLANCO, hibox=BLANCO, hibord=0, capy=1500, pop=True, italic=True, margin=70,
        font='Montserrat ExtraBold', fsize=84, spacing=1, outline=7, shadow=4,
        seed=n * 613, usage='usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool, sfx=[],
        overlays=[
            dict(type='badge', text=['+500 ACTIVIDADES ABA', 'NATURALISTAS'], y=0.098, size=86),
            dict(type='end', from_end=TAIL + 0.5, head=['Toca en', 'Más información']),
        ])
    json.dump(plan, open(os.path.join(WK, f'V{n}.json'), 'w'), ensure_ascii=False, indent=1)
    print(f'V{n} listo - {len(pool)} tramos, {len(clips)} clips - '
          f'voz {dcrudo}s a {ppm} ppm, speed {sp} -> {dcrudo / sp + TAIL:.1f}s de video')
