# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off de la Guia de Autocuracion Energetica (LATAM, 2026-10-28).
Uso: python3 gen_energia_plans.py   -> escribe V1.json .. V6.json en ~/Desktop/energia-vital/anuncios/work/"""
import os, json

WK = os.path.expanduser('~/Desktop/energia-vital/anuncios/work')

# clip -> (inicio util, fin util, extras)  ventanas revisadas en la hoja de contactos
# F (conos backflow) y K (puestos de cristales) se descartaron: traen una marca de @usuario
# que se mueve de lugar y el zoom no la recorta, y K ademas muestra la cara del creador.
VENT = {
    'A': (0, 20, {}),            # geoda abierta a martillazos
    'B': (0, 27, {}),            # cuenco de barro con hierbas y humo
    'C': (0, 22, {}),            # amatistas en la tierra
    'D': (0, 61, {}),            # manos con piedras en frascos
    'E': (0, 16, {}),            # sahumerio humeando en mesa de madera
    'G': (0, 7,  {}),            # geoda de amatista
    'H': (0, 20, {}),            # minerales grandes
    'I': (0, 7,  {}),            # sahumerio encendido
    'J': (0, 59, {}),            # cuarzos, amatistas, geodas en mano
    'L': (4, 18, {}),            # manos atando un manojo de romero
    'M': (6, 17, {}),            # sahumerio con humo a contraluz
    'N': (0, 60, {}),            # sesion de limpieza con cristales sobre la cara
    'O': (0, 20, {}),            # camilla de terapia con chakras de colores
    'P': (0, 13, {}),            # opalo en la mano
    'Q': (7, 59, {}),            # manos haciendo pases energeticos
    'R': (3, 9,  {}),            # humo de sahumerio sobre fondo negro
    'S': (7, 57, {}),            # manos limpiando energia
    'T': (0, 51, {}),            # sahumerio encendiendose con luz natural
    'U': (0, 15, {}),            # cuarzo con arcoiris en la mano
}
SEG = 6.5

def pool_y_clips():
    pool, clips = [], {}
    for k, (a, b, ex) in VENT.items():
        clips[k] = dict(src=f'tiktoks/{k}.mp4', **ex)
        t = a
        while t < b - 2.0:
            pool.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
    return pool, clips

FIN = dict(type='end', head=['GUÍA DE AUTOCURACIÓN', 'ENERGÉTICA'],
           sub='80 FICHAS · 8 BONOS DE REGALO',
           sub2='DESCARGA INMEDIATA · GARANTÍA DE 30 DÍAS',
           cta='Toca Más información 👇')

VIDEOS = [
    dict(n=1, slug='energia-pesada-en-la-espalda',
         hook='SI TE MANDARON ENERGÍA PESADA, PRESTA ATENCIÓN', hook_until='espalda',
         first=['N', 0], seed=11,
         anchors=[['cristal', 0, 'J', 0], ['hierba', 0, 'L', 4], ['chakra', 0, 'O', 0]],
         overlays=[dict(type='chip', text='80 FICHAS, UNA POR DOLENCIA', icon='✓', word='fichas', dur=2.4),
                   dict(type='chip', text='CRISTAL · HIERBA · AFIRMACIÓN', icon='✓', word='cristal', dur=2.4),
                   dict(FIN=1, word='Toca')]),
    dict(n=2, slug='atencion-terapeutas',
         hook='ATENCIÓN TERAPEUTAS DE REIKI', hook_until='sesión',
         first=['O', 0], seed=22,
         anchors=[['camilla', 0, 'N', 0], ['cristales', 0, 'J', 13]],
         overlays=[dict(type='chip', text='+100 PRÁCTICAS EN UN SOLO LUGAR', icon='✓', word='prácticas', dur=2.4),
                   dict(type='chip', text='GUÍA DE CONSULTA, NO UN MANUAL', icon='✓', word='consulta', dur=2.4),
                   dict(FIN=1, word='acceso')]),
    dict(n=3, slug='no-es-el-tipico-libro',
         hook='ESTE NO ES EL TÍPICO LIBRO ESPIRITUAL', hook_until='espiritual',
         first=['R', 3], seed=33,
         anchors=[['hierba', 0, 'L', 4], ['cristal', 0, 'U', 0]],
         overlays=[dict(type='chip', text='80 FICHAS, UNA POR DOLENCIA', icon='✓', word='fichas', dur=2.4),
                   dict(type='chip', text='LA HIERBA · EL CRISTAL · LA FRASE', icon='✓', word='hierba', dur=2.4),
                   dict(FIN=1, word='Toca')]),
    dict(n=4, slug='mapa-cuerpo-emocion',
         hook='DÓNDE GUARDA TU CUERPO CADA EMOCIÓN', hook_until='distinto',
         first=['Q', 7], seed=44,
         anchors=[['cristal', 0, 'J', 0], ['hierba', 0, 'B', 0]],
         overlays=[dict(type='chip', text='EL MAPA COMPLETO EN 80 FICHAS', icon='✓', word='mapa', dur=2.4),
                   dict(FIN=1, word='enlace')]),
    dict(n=5, slug='lo-que-sabia-tu-abuela',
         hook='LO QUE TU ABUELA SABÍA Y NADIE ANOTÓ', hook_until='anotó',
         first=['T', 0], seed=55,
         anchors=[['romero', 0, 'L', 4], ['ruda', 0, 'B', 0], ['hierba', 0, 'E', 0]],
         overlays=[dict(type='chip', text='RECETAS DE 3.000 AÑOS', icon='✓', word='recetas', dur=2.4),
                   dict(type='chip', text='+ CALENDARIO LUNAR Y PROTECCIÓN', icon='✓', word='calendario', dur=2.4),
                   dict(FIN=1, word='Toca')]),
    dict(n=6, slug='alivias-y-vuelve',
         hook='TE ALIVIAS Y A LOS TRES DÍAS VUELVE', hook_until='mismo',
         first=['S', 7], seed=66,
         anchors=[['cristal', 0, 'J', 0], ['hierba', 0, 'E', 0]],
         overlays=[dict(type='chip', text='VA A LA RAÍZ, NO AL SÍNTOMA', icon='✓', word='raíz', dur=2.4),
                   dict(type='chip', text='30 DÍAS PARA PROBARLA ENTERA', icon='✓', word='instante', dur=2.4),
                   dict(FIN=1, word='cansada')]),
]

pool, clips = pool_y_clips()
for v in VIDEOS:
    ovs = []
    for o in v['overlays']:
        if o.get('FIN'):
            e = dict(FIN); e['word'] = o['word']; ovs.append(e)
        else:
            ovs.append(o)
    P = dict(vo=f"vo/EV-V{v['n']}.wav", script=f"vo/EV-V{v['n']}.txt", lang='es',
             speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], flash=4, words=2,
             seed=v['seed'], usage='usage.json', hook=v['hook'], hook_until=v['hook_until'],
             first=v['first'], anchors=v['anchors'], clips=clips, pool=pool, overlays=ovs)
    json.dump(P, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}  {v['slug']}  {len(pool)} segmentos")
