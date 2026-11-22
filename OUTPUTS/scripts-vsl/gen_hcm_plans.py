# -*- coding: utf-8 -*-
"""Planes de los 6 ads de The Home Catering Method (mercado ingles, 2026-11-21).

Formato copiado medido de Premium Finger Foods (aperitivospremium.online):
  - 9:16, b-roll de comida PURO, ni una sola cara, ni una foto fija.
  - UN CORTE POR SEGUNDO (ellos: 29 a 47 cortes por video).
  - SIN caja de hook arriba. Subtitulos quemados ABAJO, 2 a 4 palabras, mayuscula,
    blancos con borde y sombra, y la palabra que suena en AMARILLO.
  - Voz femenina calida en off. speed 1.15 (pedido de Santiago el 21/11).
  - Sin placas, sin chips, sin SFX: cierra sobre el b-roll con el ultimo subtitulo.

Uso: python3 -I gen_planes.py <workdir>
"""
import os, sys, json, glob, subprocess

W = sys.argv[1]
FF = os.path.expanduser('~/bin/ffmpeg')
SEG = 1.4          # largo del tramo candidato (los cortes del editor son de ~1 s)
TOPE = 8           # maximo de recortes por clip (regla del pool)
BORDE = 0.5        # se descartan los primeros/ultimos 0,5 s de cada clip

AMARILLO = '&H0000D7FF&'   # BGR del #FFD700
NEGRO = '&H00000000&'

ver = json.load(open(W + '/veredicto.json'))
autores = {}
for ln in open(W + '/autores.txt'):
    ln = ln.strip()
    if '/' in ln:
        a, i = ln.rsplit('/', 1); autores[i] = a or i

def pool_y_clips():
    pool, clips, k = [], {}, 0
    for vid, v in sorted(ver.items()):
        if not v.get('ok'):
            continue
        D = v['dur']
        a, b = BORDE, D - BORDE
        if b - a < SEG:
            continue
        key = 'c%03d' % k; k += 1
        clips[key] = dict(src='clips/%s.mp4' % vid, fam=autores.get(vid, vid))
        tramos, t = [], a
        while t < b - SEG * 0.8:
            tramos.append([key, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips

VIDEOS = [1, 2, 3, 4, 5, 6]
pool, clips = pool_y_clips()
for n in VIDEOS:
    plan = dict(
        vo='voz/V%d.wav' % n, script='voz/V%d.txt' % n, lang='en',
        speed=1.15, silence=[0.40, 0.20],      # recorte suave: el doc pide ritmo natural, no video sin aire
        cut=[0.9, 1.0, 1.1], words=3,          # un corte por segundo, subtitulo de 3 palabras
        music='music/bed.wav', music_db=-10,
        hook='', hook_until='',                # SIN caja de hook (lo que cambia contra Slime)
        hi=AMARILLO, hibox=NEGRO, hibord=0, capy=1500, pop=False,
        font='Montserrat ExtraBold', fsize=60, spacing=7, outline=4, shadow=3,
        seed=n * 541, usage='usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool, anchors=[], overlays=[])
    json.dump(plan, open('%s/V%d.json' % (W, n), 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - %d tramos de %d clips' % (n, len(pool), len(clips)))
