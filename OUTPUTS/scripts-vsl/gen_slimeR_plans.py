# -*- coding: utf-8 -*-
"""Planes de las 3 RENOVACIONES del ad ganador del Slime Shop Kit (2026-11-20).

El ganador es el 01 ("Did you know slime and sensory dough can turn into your next little
business?", 18,5 s). Segun [[renovacion-de-creativos]]: el cuerpo y el CTA se copian TEXTUALES
y solo cambia el hook, con un FORMATO distinto por renovacion (no el mismo hook con otra
palabra):
  R1 - reaccion de un tercero  (otra mama pregunta donde lo compro)
  R2 - cuentas rapidas         (diez minutos, dos dolares, un frasco)
  R3 - declaracion contraintuitiva (el slime ya no es un juguete)

El checklist del 27/10 pide que una renovacion tambien se VEA distinta. Sin bajar un clip nuevo:
  - la ventana de muestreo va CORRIDA media ventana (OFF) y con TOPE 8 en vez de 6, asi las
    claves cXX@t no coinciden con las del usage.json de la tanda 1 (regla del 9/11, DanceGo);
  - se reusa el usage.json de la tanda 1, que penaliza x10 lo ya visto, asi el editor elige
    planos frescos solo;
  - el ritmo de corte pasa de [1.5, 2.0, 2.5] a [1.7, 2.2, 2.7], dentro de la firma de ellos.

Uso: python3 gen_slimeR_plans.py <dir_de_trabajo>   -> R1.json R2.json R3.json
"""
import os, re, sys, json

WK = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
sys.path.insert(0, WK)
from vent_slime import VENT

SEG = 2.6          # largo de cada tramo candidato
OFF = 1.3          # ventana corrida media ventana: tramos nuevos sobre material ya revisado
TOPE = 8           # recortes por clip (la tanda 1 uso 6)

AMARILLO = '&H0000D7FF&'   # BGR del amarillo de sus subtitulos (#FFD700)
NEGRO = '&H00000000&'

_vs = open(os.path.join(WK, 'vent_slime.py')).read()
AUTOR = dict(re.findall(r"'(c\d+)':\s*\('\d+'.*?#\s*@?([^\s]+)", _vs))


# Vetos de la revision del render (20/11). Van como dict y no recortando la ventana, asi el
# resto del clip se sigue usando y el veto queda documentado (regla del 12/11, displays de papel).
#   c04, c08, c17, c30: el TRIPODE DE FILMACION asoma arriba en cuadro. No es texto, asi que ni el
#        OCR ni el pase de carteles lo marcan, y en la tanda 1 ninguno de los cuatro habia salido
#        sorteado: aparecio recien en la hoja de contactos del render. Los cuatro son del MISMO
#        creador (@mushslime), que graba con el tripode dentro del encuadre: el defecto es del
#        autor, no del clip, asi que se cayeron los cuatro.
#   c28: la etiqueta "SLIME BUTTER / EXTRA WHIPPED BUTTERCREAM" de otra tienda es grande y nitida
#        los primeros 13 s (salio en el PRIMER plano de R3, abajo de la caja de hook). Desde los
#        14 s es slime amarillo suelto y sirve.
#   c25: el frasco "MARKET COOLER" de otra tienda entra entre los 2,5 y los 5,5 s.
VETO = {
    'c04': [(0.0, 99.0)], 'c08': [(0.0, 99.0)], 'c17': [(0.0, 99.0)], 'c30': [(0.0, 99.0)],
    'c28': [(0.0, 14.0)],
    'c25': [(2.5, 5.5)],
}


def vetado(k, t0, t1):
    return any(t0 < f and t1 > i for i, f in VETO.get(k, []))


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src=f'clips/{vid}.mp4', fam=AUTOR.get(k, vid), **ex)
        tramos, t = [], a + OFF
        while t < b - 1.5:
            if not vetado(k, t, min(t + SEG, b)):
                tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


# hook nuevo + la palabra de la primera frase donde se va la cajita blanca
VIDEOS = [
    dict(n=1, hook='ANOTHER MOM ASKED ME WHERE I BOUGHT IT', until='morning'),
    dict(n=2, hook='TEN MINUTES. TWO DOLLARS. ONE JAR.', until='for'),
    dict(n=3, hook="SLIME ISN'T JUST A TOY ANYMORE", until='home'),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"voz/R{v['n']}.wav", script=f"voz/R{v['n']}.txt", lang='en',
        speed=1.20, silence=[0.26, 0.12], cut=[1.7, 2.2, 2.7], words=3,
        music='music/bed.wav', music_db=-10,
        hook=v['hook'], hook_until=v['until'], hook_until_occ=0,
        hook_y=250, hook_size=66,
        hi=AMARILLO, hibox=NEGRO, hibord=0, capy=1500, pop=False,
        font='Montserrat ExtraBold', fsize=60, spacing=7, outline=4, shadow=3,
        seed=v['n'] * 911, usage='usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool, anchors=[], overlays=[])
    json.dump(plan, open(f"{WK}/R{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print("R%d listo · %d tramos · hook: %s" % (v['n'], len(pool), v['hook']))
