# -*- coding: utf-8 -*-
"""Planes de los 6 ads de El Manual del Piso Epoxi (LATAM, 2026-11-10).

Clonado de Hands & Home / The Epoxy Floor Playbook (handshome.impultienda.ar): b-roll real de
pisos epoxi (desbaste, mezcla, vertido, rasqueta, metalizados terminados), chips oscuros arriba,
pastillas blancas con cruz roja para los defectos, el panel "EL SISTEMA" que se va tildando,
los insertos del producto anclados a la palabra que los nombra y placa de cierre cobre.

Uso: python3 gen_epoxi_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/pisos-epoxi/anuncios/work')
SEG = 3.0
TOPE = 8

VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_epoxi.py')).read())

GFX = {'1': 'sistema.png', '2': 'tabla.png', '3': 'precios.png', '4': 'bonos.png', '5': 'celular.png'}
TODOS = ''.join(VENT.keys())


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
COBRE = '&H002C6AC0&'       # cobre #C06A2C en BGR: el resalte del ganador
NEGRO = '&H00000000&'       # sin caja: el borde sigue siendo negro

CIERRE = dict(type='end', occ=0,
              head=['TOCA ABAJO'],
              sub='y vuelca tu primer piso espejo este fin de semana',
              cta='Ver todo lo que hay adentro',
              sub2='60+ proyectos · 6 sistemas de piso · Tabla de Soluciones · 3 bonos gratis',
              img='gfx/celular_solo.png')

VIDEOS = [
    dict(n=1, cta='toca', gfx='125', first=['c', VENT['c'][1]], last='u',
         anchors=[('manual', 0, '1', 0), ('celular', 0, '5', 0), ('tabla', 0, '2', 0)],
         tags=[('preparas', 0, 'PREPARAR · MEZCLAR · VERTER · TERMINAR'),
               ('fracción', 0, 'EL MATERIAL ES LA PARTE BARATA')],
         chips=[('burbujas', 0, 'Burbujas'), ('levantarse', 0, 'Se levanta a los 6 meses')],
         plan=None),
    dict(n=2, cta='abre', gfx='13', first=['a', VENT['a'][1]], last='h',
         anchors=[('manual', 0, '1', 0), ('cobrar', 0, '3', 0)],
         tags=[('espejo', 1, 'EL ORDEN ES TODO')],
         chips=[('placas', 0, 'Se levanta en placas')],
         plan=('orden', 0, 'EL SISTEMA', 'Los cuatro pasos, en orden',
               ['Preparar el concreto', 'Mezclar', 'Verter', 'Sellar'])),
    dict(n=3, cta='toca', gfx='124', first=['C', VENT['C'][1]], last='y',
         anchors=[('manual', 0, '1', 0), ('tabla', 0, '2', 0), ('bonos', 0, '4', 0)],
         tags=[('barata', 0, 'EL MATERIAL ES LA PARTE BARATA')],
         chips=[('pegajosas', 0, 'Manchas pegajosas'), ('zapato', 0, 'Placas que se despegan')],
         plan=('pasos', 0, 'EL SISTEMA PROFESIONAL', 'Cuatro pasos, en este orden',
               ['Preparar', 'Mezclar', 'Verter', 'Terminar'])),
    dict(n=4, cta='toca', gfx='13', first=['i', VENT['i'][1]], last='g',
         anchors=[('manual', 0, '1', 0), ('precios', 0, '3', 0)],
         tags=[('cuadra', 0, 'EL TRABAJO MÁS CARO DE LOS DOS')],
         money=('hora', 0, 'TU TARIFA POR HORA', '3X', ''),
         chips=[],
         plan=('sistema', 0, 'LO QUE TE FALTA', 'No es habilidad, es el sistema',
               ['Qué piso ofrecer', 'Cómo prepararlo', 'Cuánto comprar', 'Cuánto cobrar'])),
    dict(n=5, cta='toca', gfx='13', first=['q', VENT['q'][1]], last='r',
         anchors=[('manual', 0, '1', 0), ('cobrar', 0, '3', 0)],
         tags=[('día', 0, 'LA MÁQUINA SE ALQUILA POR DIA'),
               ('semana', 0, 'UN GARAGE · UN FIN DE SEMANA')],
         chips=[('burbujas', 0, 'Burbujas')],
         plan=None),
    dict(n=6, cta='toca', gfx='124', first=['l', VENT['l'][1]], last='t',
         anchors=[('manual', 0, '1', 0), ('tabla', 0, '2', 0), ('bonos', 0, '4', 0)],
         tags=[('talleres', 0, 'GARAGES · TALLERES · GIMNASIOS'),
               ('oficio', 0, 'NO ES UNA MODA · ES UN OFICIO')],
         chips=[],
         plan=None),
]

for v in VIDEOS:
    pool, clips = pool_y_clips(v['gfx'], TODOS)
    overlays = [dict(type='tag', word=w, occ=o, text=t, dur=2.4) for w, o, t in v['tags']]
    overlays += [dict(type='chip', word=w, occ=o, text=t, dur=2.2) for w, o, t in v['chips']]
    if v.get('money'):
        w, o, lab, a_, b_ = v['money']
        overlays.append(dict(type='money', word=w, occ=o, label=lab, left=a_, right=b_, y=1430))
    if v.get('plan'):
        w, o, lab, tit, rows = v['plan']
        overlays.append(dict(type='plan', word=w, occ=o, label=lab, title=tit, rows=rows))
    fin = dict(CIERRE); fin['word'] = v['cta']
    overlays.append(fin)
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-9,
        hi=COBRE, hibox=NEGRO, hibord=8, capy=1300,
        first=v['first'], last=v['last'], seed=v['n'] * 173, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=overlays)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - %d tramos' % (v['n'], len(pool)))
