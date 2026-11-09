# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Deco Magic LATAM (2026-11-09).

Clonado de Magic Deco / decomagic.shop: b-roll real de golosinas personalizadas, cajitas,
envoltorios y mesas de dulces, con la app y Canva anclados a la palabra que los nombra,
pastillas rosas arriba, subtitulos blancos de 3 palabras con la palabra activa adentro de una
caja magenta (#E74FA4) y placa de cierre con su degradado violeta -> magenta.

Uso: python3 gen_deco_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/deco-magic/anuncios/work')
SEG = 3.4
TOPE = 6

VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_deco.py')).read())

GFX = {'1': 'app.png', '2': 'canva.png'}

# 'a' se cayo: tiene una Cricut en pantalla y el ad dice justo que no hace falta maquina de corte
PROD = 'bcdefghijklmnpqrsEFHIJ'    # producto en primer plano
# de las mesas quedan solo las que se ven como fiesta infantil con deco; las de pura
# pasteleria fina (t, u, v, w, A, B, D) no muestran lo que vendemos y se cayeron
MESA = 'xyzCG'


def pool_y_clips(gfx_keys, claves):
    pool, clips = [], {}
    for k in claves:
        fn, a, b, ex = VENT[k]
        d = dict(src=f'clips/{fn}.mp4'); d.update(ex)
        clips[k] = d
        tramos, t = [], a
        while t < b - 1.6:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    for k in gfx_keys:
        clips[k] = dict(src=f'gfx/{GFX[k]}', fam='gfx' + k, still=True)
        pool.append([k, 0, 3.2])
    return pool, clips


BLANCO = '&H00FFFFFF&'      # texto de la palabra activa
MAGENTA = '&H00A44FE7&'     # caja magenta #E74FA4 en BGR

CIERRE = dict(type='end', word='toca', occ=0,
              head=['TODA LA FIESTA', 'EN UNA APP'],
              sub='Cientos de temáticas · Canva gratis · Imprime en casa',
              cta='Mira todo lo que hay adentro')

VIDEOS = [
    dict(n=1, gfx='12',
         first=['H', 11.0],
         anchors=[('app', 0, '1', 0), ('canva', 0, '2', 0)],
         chips=[('impresora', 0, 'IMPRESO EN CASA'), ('máquina', 0, 'SIN MÁQUINA DE CORTE'),
                ('personaje', 0, 'SU PERSONAJE · SU NOMBRE')],
         last='z'),
    dict(n=2, gfx='12',
         first=['p', 0.3],
         anchors=[('app', 0, '1', 0), ('canva', 0, '2', 0)],
         chips=[('diseñar', 0, 'SIN SABER DISEÑAR'), ('impresora', 0, 'IMPRIME EN CASA'),
                ('cientos', 0, 'CIENTOS DE TEMÁTICAS')],
         last='x'),
    dict(n=3, gfx='12',
         first=['x', 0.3],
         anchors=[('app', 0, '1', 0), ('canva', 0, '2', 0)],
         chips=[('combinar', 0, 'TODO COMBINA'), ('tarde', 0, 'EN UNA SOLA TARDE')],
         last='y'),
    dict(n=4, gfx='12',
         first=['z', 0.3],
         anchors=[('buscador', 0, '1', 0), ('canva', 0, '2', 0)],
         chips=[('carpeta', 0, 'NO ES UNA CARPETA'), ('kit', 0, 'EL KIT COMPLETO'),
                ('tarde', 0, 'EN UNA TARDE')],
         last='C'),
    dict(n=5, gfx='12',
         first=['j', 0.3],
         anchors=[('app', 0, '1', 0), ('canva', 0, '2', 0)],
         chips=[('nombre', 0, 'CON EL NOMBRE DE SU HIJO'), ('corte', 0, 'SIN MÁQUINA DE CORTE')],
         last='G'),
    dict(n=6, gfx='12',
         first=['c', 0.3],
         anchors=[('temática', 0, '1', 0), ('canva', 0, '2', 0)],
         chips=[('horas', 0, 'SE TE VAN LAS HORAS'), ('combina', 0, 'TODO COMBINA'),
                ('mes', 0, 'COLECCIONES NUEVAS CADA MES')],
         last='p'),
]

for v in VIDEOS:
    pool, clips = pool_y_clips(v['gfx'], PROD + MESA)
    overlays = [dict(type='tag', word=w, occ=o, text=t, dur=2.4) for w, o, t in v['chips']]
    overlays.append(dict(CIERRE))
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.8, 2.2, 2.7], words=3,
        music='music/bed_activo.wav', music_db=-9,
        hi=BLANCO, hibox=MAGENTA, hibord=18, capy=1240,
        first=v['first'], last=v['last'], seed=v['n'] * 211, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=overlays)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - %d tramos' % (v['n'], len(pool)))
