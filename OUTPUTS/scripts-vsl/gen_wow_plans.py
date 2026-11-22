# -*- coding: utf-8 -*-
"""Planes de los 4 ads de Laboratorio Wow (mercado argentino, 2026-11-21),
clonando la edicion de "Happy Kids Corner" / Laboratorium Wow.

De ellos se copia: caja de hook blanca de dos renglones (el segundo en rojo), subtitulos en
MAYUSCULA con cada palabra en su caja (negro sobre blanco, la que suena al reves), b-roll real
de experimentos y los insertos del producto anclados a la palabra que los nombra.

Uso: python3 gen_wow_plans.py <carpeta_work>   -> V1.json .. V4.json
"""
import os, re, sys, json

WK = sys.argv[1]
sys.path.insert(0, WK)
from vent_wow import VENT, FAM

SEG = 2.6
TOPE = 8


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src='pool/clips/%s.mp4' % vid, fam=FAM.get(vid, vid), **ex)
        tramos, t = [], a
        while t < b - 1.6:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


def occ(script, frase, palabra):
    txt = script.lower()
    i = txt.find(frase.lower())
    if i < 0:
        raise SystemExit('no esta la frase: ' + frase)
    pre = re.findall(r"[\w'áéíóúñ-]+", txt[:i])
    n = lambda w: re.sub(r"[^\wáéíóúñ]", '', w.lower())
    return sum(1 for w in pre if n(w) == n(palabra))


HOOKS = {
 1: dict(l1='Bicarbonato, vinagre, leche:', l2='300 experimentos'),
 2: dict(l1='Algo más interesante', l2='que la tablet'),
 3: dict(l1='No tenés que saber química:', l2='300 experimentos'),
 4: dict(l1='Para la próxima que vengan:', l2='300 experimentos'),
}
# (frase que ubica, palabra ancla, inserto)
ANCLAS = {
 1: [('viene en su ficha', 'ficha', 'ficha'), ('el color de seguridad', 'color', 'colores')],
 2: [('con su ficha de tres pasos', 'ficha', 'ficha'), ('el plan de treinta tardes', 'plan', 'plan')],
 3: [('escrita en la ficha', 'ficha', 'ficha'), ('verde: lo hace solo', 'verde', 'colores')],
 4: [('está en la ficha', 'ficha', 'ficha'), ('ordenados por edad', 'edad', 'colores')],
}

for n in (1, 2, 3, 4):
    pool, clips = pool_y_clips()
    script = open(os.path.join(WK, 'guiones', 'V%d.txt' % n)).read()
    anchors = []
    for frase, pal, gfx in ANCLAS[n]:
        clips[gfx] = dict(src='work/gfx/%s.jpg' % gfx, fam='gfx', still=True)
        pool.append([gfx, 0.0, 6.0])
        anchors.append([pal, occ(script, frase, pal), gfx, 0.0])
    plan = dict(
        vo='work/voces/V%d.wav' % n, script='work/guiones/V%d.txt' % n, lang='es',
        speed=1.20, silence=[0.26, 0.12], cut=[1.7, 2.2, 2.7],
        nosfx=True, music_db=-13,
        words=3, font='Montserrat ExtraBold', fsize=66, capy=1240,
        basec='&H00000000&', baseout='&H00FFFFFF&',
        hi='&H00FFFFFF&', hibox='&H00000000&', hibord=13,
        outline=13, shadow=0, spacing=3, margin=60,
        hook2=dict(l1=HOOKS[n]['l1'], l2=HOOKS[n]['l2'], y=400, s1=58, s2=84),
        seed=n * 811, usage='pool/usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool,
        anchors=anchors, overlays=[])
    json.dump(plan, open(os.path.join(WK, '..', 'V%d.json' % n), 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - %d tramos, %d anclas' % (n, len(pool), len(anchors)))
