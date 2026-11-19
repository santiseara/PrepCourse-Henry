# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Capillas de la Virgen (LATAM, 2026-11-18), clonando a
Mariana Williams Creations (ourladychapels.impultienda.ar).

Lo que se copia de ellos, medido sobre sus 6 creativos de mas impresiones (31/10 al 16/11):
  - 9:16, 24 a 31 s, voz de mujer calida y cama musical por debajo.
  - CAJA DE HOOK blanca arriba, texto azul marino en mayuscula, se va con la primera frase.
  - FICHAS DE PASO azules arriba, una por paso, ancladas a la palabra que las nombra.
  - SUBTITULOS de 3 palabras abajo, blancos con la palabra que suena en DORADO.
  - PLACA DE CIERRE: la misma cajita blanca con el CTA, sobre el b-roll, hasta el final.
  - Sin SFX, sin placa oscura, sin boton.

Uso: python3 gen_capillas_plans.py   -> V1.json .. V6.json en anuncios/work/
"""
import os, re, sys, json

WK = os.path.expanduser('~/Desktop/capillas-papel/anuncios/work')
sys.path.insert(0, WK)
from vent_capillas import VENT

SEG = 2.8          # largo de cada tramo candidato (sus cortes van de 1,8 a 2,8 s)
TOPE = 6           # maximo de recortes por clip

DORADO = '&H0000C8FF&'   # BGR del dorado #FFC800 de sus subtitulos
NEGRO = '&H00000000&'

# familia = autor de TikTok (el comentario de cada linea de vent_capillas.py): las claves van
# corridas (c00, c01...), asi que la regla de "no repetir fuente" no puede salir de la inicial.
_vs = open(os.path.join(WK, 'vent_capillas.py')).read()
AUTOR = dict(re.findall(r"'(c\d+)':\s*\('\d+'.*?#\s*@?([^\s]+)", _vs))


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src=f'clips/{vid}.mp4', fam=AUTOR.get(k, vid), **ex)
        tramos, t = [], a
        while t < b - 1.6:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


CIERRE_CLIC = 'HAZ CLIC EN "MÁS INFORMACIÓN" Y DESCÁRGALO HOY'
CIERRE_TOCA = 'TOCA "MÁS INFORMACIÓN" Y DESCÁRGALO HOY'

VIDEOS = [
    dict(n=1, hook='3 PASOS PARA UNA CAPILLITA DE LA VIRGEN', until='pasos', first='c53',
         pasos=[('uno', 0, '1. IMPRIME'), ('dos', 0, '2. RECORTA Y DOBLA'), ('tres', 1, '3. REZA O REGALA')],
         cierre=('Haz', 0, CIERRE_CLIC)),
    dict(n=2, hook='DE UNA HOJA DE PAPEL A UNA CAPILLA', until='Virgen', first='c05',
         pasos=[('imprimes', 0, '1. IMPRIME'), ('recortas', 0, '2. RECORTA Y DOBLA'), ('pegas', 0, '3. PEGA LA BASE')],
         cierre=('Haz', 0, CIERRE_CLIC)),
    dict(n=3, hook='POV: EL RINCÓN DE ORACIÓN DE LA ABUELA ESTRENA CAPILLA', until='juntas', first='c01',
         pasos=[], cierre=('Haz', 0, CIERRE_CLIC)),
    dict(n=4, hook='SI DAS CATEQUESIS, MIRA ESTO', until='esto', first='c33',
         pasos=[('uno', 0, '1. IMPRIMIR'), ('dos', 0, '2. RECORTAR'), ('tres', 0, '3. DOBLAR')],
         cierre=('Toca', 0, CIERRE_TOCA)),
    dict(n=5, hook='UN RECUERDO DE COMUNIÓN QUE SE GUARDA', until='algo', first='c43',
         pasos=[('uno', 0, '1. IMPRIME'), ('dos', 0, '2. RECORTA'), ('tres', 0, '3. DOBLA')],
         cierre=('Toca', 0, CIERRE_TOCA)),
    dict(n=6, hook='UNA HOJA DE PAPEL. DIEZ MINUTOS.', until='después', first='c15',
         pasos=[], cierre=('Toca', 0, CIERRE_TOCA)),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    overlays = [dict(type='step', word=w, occ=o, text=t, y=250, dur=2.6) for w, o, t in v['pasos']]
    cw, co, ct = v['cierre']
    overlays.append(dict(type='box', word=cw, occ=co, text=ct, y=250, size=56, hasta_el_final=True))
    plan = dict(
        vo=f"voz/V{v['n']}.wav", script=f"voz/V{v['n']}.txt", lang='es',
        speed=1.20, silence=[0.26, 0.12], cut=[1.8, 2.3, 2.8], words=3,
        music='music/bed.wav', music_db=-10,
        hook=v['hook'], hook_until=v['until'], hook_y=250, hook_size=62,
        hi=DORADO, hibox=NEGRO, hibord=0, capy=1460, pop=False,
        font='Montserrat ExtraBold', fsize=58, spacing=6, outline=4, shadow=3,
        first=[v['first'], next(t[1] for t in pool if t[0] == v['first'])] if v.get('first') else None,
        seed=v['n'] * 419, usage='usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool, anchors=[], overlays=overlays)
    if plan.get('first') is None: plan.pop('first')
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print("V%d listo · %d tramos · %d overlays · hook: %s" % (v['n'], len(pool), len(overlays), v['hook']))
