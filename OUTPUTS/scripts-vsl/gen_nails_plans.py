# -*- coding: utf-8 -*-
"""Planes de los 6 ads de lanzamiento de Nail Designer (mercado inglés, 2026-11-08).

Modelado sobre Fabiana Rodrigues (162 ads activos, el ganador corre desde el 9/6 = 5 meses):
  - Visual 100 % macro de uña en construcción, igual que ella: ni una cara, ni una foto fija.
  - 43 clips de TikTok de #polygelnails y #nailextensions, revisados con hoja de contactos a
    1,5 s y cuadro grande de la mitad inferior. Los que traían cartel se entran después del cartel.
  - Un color de caja de subtítulo por creativo. Cierre con pastilla de CTA, sin placa oscura.

Uso: python3 gen_nails_plans.py  -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/nail-designer/anuncios/work')
VENT = json.load(open(f'{WK}/ventanas.json'))
SEG = 4.0
TOPE = 8


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src=f'tiktoks/{vid}.mp4', fam=vid, **ex)
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


VIDEOS = [
    # 1 "In one hour"      · caja rosa fuerte, texto blanco
    dict(n=1, hi='&H00FFFFFF&', hibox='&H007E19E6&', cta='TAP LEARN MORE', word='Tap'),
    # 2 "job application"  · caja violeta, texto blanco
    dict(n=2, hi='&H00FFFFFF&', hibox='&H00ED3A7C&', cta='GO NOW', word='go'),
    # 3 "one client"       · caja ambar, texto tinta
    dict(n=3, hi='&H00141414&', hibox='&H0024A5F5&', cta='TAP LEARN MORE', word='Tap'),
    # 4 "point zero"       · caja celeste, texto tinta
    dict(n=4, hi='&H00141414&', hibox='&H00E6C322&', cta='START TONIGHT', word='Tap'),
    # 5 "minimum filing"   · caja roja, texto blanco
    dict(n=5, hi='&H00FFFFFF&', hibox='&H004639E6&', cta='TAP LEARN MORE', word='Tap'),
    # 6 "one bead"         · caja magenta, texto blanco
    dict(n=6, hi='&H00FFFFFF&', hibox='&H00D326C0&', cta='WATCH LESSON ONE', word='Tap'),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='en',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-8,
        hi=v['hi'], hibox=v['hibox'], hibord=20, capy=1300,
        seed=v['n'] * 173, usage='usage.json',
        clips=clips, pool=pool, anchors=[],
        overlays=[dict(type='button', word=v['word'], occ=0, text=v['cta'], y=1560, size=62)])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo · %d tramos · %d clips' % (v['n'], len(pool), len(clips)))
