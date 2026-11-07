# -*- coding: utf-8 -*-
"""Planes de los 6 ads de la guía de meliponicultura (LATAM, 2026-11-07).

Clonado de Meliponicultura Essencial (BR): b-roll real de meliponario + las páginas del
cuadernillo ancladas a la palabra que las nombra, subtítulos derechos en mayúscula de 3
palabras con la palabra activa en verde lima o amarillo (sin caja) y botón rojo de CTA al
final, que es su placa manuscrita.

Pool: 24 clips de TikTok de #meliponicultura revisados con hoja de contactos a 1,5 s; las
ventanas evitan los tramos con texto quemado en portugués.

Uso: python3 gen_meliponi_plans.py  -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/meliponicultura/anuncios/work')
SEG = 4.0
TOPE = 5

# id de TikTok -> (desde, hasta, extras).  Ventanas revisadas una por una.
VENT = {
    'a': ('6982238828509613318', 0.5, 28.0, {}),      # abrir un tronco con el nido adentro
    'b': ('7009275958913993989', 9.0, 24.0, {}),      # cuadro lleno de potes (el cartel va de 5 a 7,5)
    'c': ('7019049880421240070', 0.5, 23.0, {}),      # fila de piqueras de barro
    'd': ('7042465415934610693', 15.0, 20.0, {}),     # piqueras en la pared (texto hasta el 14)
    'e': ('7077730307612495110', 1.0, 20.0, {'zoom': 1.35, 'ybias': 1.0}),  # polen (cartel arriba)
    'f': ('7150402909832793350', 0.5, 7.5, {}),       # jarabe sobre los potes
    'g': ('7458776330067365126', 0.5, 28.0, {}),      # cajas y piquera con movimiento
    # 'h' (7501325906858773765, enjambre volando) se cayó en la revisión del render: entra una nena en cuadro
    'i': ('7513752148711083270', 0.5, 25.0, {}),      # macro de piquera con abejas entrando
    'j': ('7527110824545078533', 0.5, 22.0, {}),      # caja trampa casera con botella
    'k': ('7587193042814143762', 12.0, 20.0, {}),     # macro de potes de miel
    'l': ('7592788919222078738', 0.5, 11.0, {}),      # meliponario en postes
    'm': ('7600765864450821397', 0.5, 26.0, {}),      # alimentador con frasco de jarabe
    'n': ('7609704726862548245', 0.5, 28.0, {}),      # transferencia de nido a caja
    'o': ('7609764906862202130', 0.5, 28.0, {}),      # cajas trampa colgadas en los árboles
    'p': ('7650291043715304725', 0.5, 18.0, {}),      # caja abierta llena de potes
    'q': ('7654387428119022856', 14.0, 28.0, {}),     # flores con abeja y potes (título hasta el 13)
    'r': ('7682152144220196117', 0.5, 28.0, {}),      # succión de la miel de los potes
    's': ('7688096013785042197', 0.5, 22.0, {}),      # caja llena de potes en la mano
    't': ('7693690099791367444', 0.5, 28.0, {}),      # meliponario tipo casita en el patio
    'u': ('7702888350356737281', 0.5, 28.0, {}),      # armado de la caja en el banco
    'v': ('7704727741714779400', 0.5, 28.0, {}),      # caja trampa atada a un tronco
    'w': ('7704845457213771029', 0.5, 28.0, {}),      # alimentación con frasco y manos
    'x': ('7704857377161481473', 0.5, 28.0, {}),      # cajas trampa en la pared del campo
}

GFX = {'T': 'tapa.png', 'K': 'calendario.png', 'F': 'floraciones.png',
       'E': 'especies.png', 'R': 'trampa.png', 'G': 'agua.png', 'V': 'venta.png'}


def pool_y_clips():
    pool, clips = [], {}
    for k, (vid, a, b, ex) in VENT.items():
        clips[k] = dict(src=f'tiktoks/{vid}.mp4', fam=vid, **ex)
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    for k, fn in GFX.items():
        clips[k] = dict(src=f'gfx/{fn}', fam=k, still=True)
        pool.append([k, 0, 3.4])
    return pool, clips


LIMA = '&H0000FC7C&'      # verde lima (BGR)
AMAR = '&H0000E8FF&'      # amarillo
NEGRO = '&H00000000&'     # "caja" negra = no se ve caja, solo el borde de siempre

VIDEOS = [
    dict(n=1, hi=LIMA, first=['w', 0.5],
         anchors=[('silenciosos', 0, 'G', 0), ('Esta', 0, 'T', 0),
                  ('especie', 0, 'E', 0), ('venderla', 0, 'V', 0)],
         overlays=[dict(type='button', word='Toca', text='TOCA EN MÁS INFORMACIÓN', size=56, y=1560)],
         last='T'),
    dict(n=2, hi=AMAR, first=['t', 0.5],
         anchors=[('calendario', 0, 'K', 0), ('verano', 0, 'K', 0),
                  ('especie', 0, 'E', 0)],
         overlays=[dict(type='button', word='Toca', occ=1, text='TOCA EN MÁS INFORMACIÓN', size=56, y=1560)],
         last='K'),
    dict(n=3, hi=LIMA, first=['j', 0.5],
         anchors=[('trampa', 0, 'R', 0), ('página', 0, 'T', 0),
                  ('especie', 0, 'E', 0), ('vender', 0, 'V', 0)],
         overlays=[dict(type='tag', word='rincón', text='LUGAR EQUIVOCADO', dur=2.0, y=230),
                   dict(type='button', word='enlace', occ=0, text='TOCA EN MÁS INFORMACIÓN', size=56, y=1560)],
         last='T'),
    dict(n=4, hi=AMAR, first=['i', 0.5],
         anchors=[('angelita', 0, 'E', 0), ('guía', 0, 'T', 0),
                  ('calendario', 0, 'K', 0)],
         overlays=[dict(type='button', word='Toca', text='TOCA EN MÁS INFORMACIÓN', size=56, y=1560)],
         last='E'),
    dict(n=5, hi=LIMA, first=['q', 14.0],
         anchors=[('floraciones', 0, 'F', 0), ('mapa', 0, 'F', 0),
                  ('especie', 0, 'E', 0), ('venta', 0, 'V', 0)],
         overlays=[dict(type='button', word='Toca', text='TOCA EN MÁS INFORMACIÓN', size=56, y=1560)],
         last='F'),
    dict(n=6, hi=AMAR, first=['r', 0.5],
         anchors=[('Esta', 0, 'T', 0), ('especie', 0, 'E', 0),
                  ('cosechar', 0, 'V', 0), ('calendario', 0, 'K', 0)],
         overlays=[dict(type='button', word='Toca', text='TOCA EN MÁS INFORMACIÓN', size=56, y=1560)],
         last='T'),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-9,
        hi=v['hi'], hibox=NEGRO, hibord=8, capy=1340,
        first=v['first'], last=v['last'], seed=v['n'] * 211, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=v['overlays'])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo · %d tramos' % (v['n'], len(pool)))
