# -*- coding: utf-8 -*-
"""Renovaciones R1-R3 de la oferta de displays de papel (2026-11-12).

Renovacion, no tanda nueva: el CUERPO del guion 1 (la imprenta escondida, el angulo que
Decorarina mas replica en PT y ES) va copiado TEXTUAL y solo cambia el hook, con tres
FORMATOS distintos (demo con el objeto en la mano / declaracion de autoridad / pregunta-acertijo),
como pide el checklist del 27/10 de renovacion-de-creativos.

La estetica tambien cambia, que es la otra mitad del checklist:
  - la caja de la palabra activa pasa de tinta azul noche a NARANJA QUEMADO
  - cortes mas rapidos: 1.6 / 2.0 / 2.5 en vez de 1.9 / 2.4 / 2.9
  - ventana de muestreo corrida +1.45 s con tramos de 2.4 s y tope de 10 por clip, asi
    ninguna clave coincide con las del usage.json de la tanda 1 (regla del 9/11, DanceGo):
    los planos son nuevos sin bajar un solo clip nuevo.

Uso: python3 gen_displays_ren_plans.py   -> escribe V7.json V8.json V9.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/displays-de-papel/anuncios/work')
SEG = 2.4
TOPE = 10
OFF = 1.45

VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_displays.py')).read())

# Vetos que aparecieron en la hoja de contactos del primer render (12/11):
#   s 59-71 s: la bolsa naranja "SUPORTE PARA BALAO - MEDIO" en portugues, grande y legible
#   en el borde de la mesa (sale en el hook de R1), y los primeros planos de dedos donde no
#   se ve lo que vendemos. El OCR de la tanda 1 no la marco porque no es cartel, es un envase.
VETO = {
    's': [(59.0, 71.0)],   # bolsa naranja "SUPORTE PARA BALAO" en portugues + primeros planos de dedos
    'r': [(27.0, 30.0)],   # la silueta de MDF pelada: es exactamente lo que decimos que NO es
    'b': [(133.0, 153.0)], # el carton de "maizena" con la marca impresa, usado de base
}

GFX = {'1': 'tamanos.png', '2': 'costos.png', '3': 'biblioteca.png', '4': 'celular.png'}
TODOS = ''.join(VENT.keys())


def pool_y_clips(gfx_keys, claves):
    pool, clips = [], {}
    for k in claves:
        fn, a, b, ex = VENT[k]
        d = dict(src=f'clips/{fn}.mp4'); d.update(ex)
        clips[k] = d
        tramos, t = [], a + OFF
        while t < b - 1.4:
            fin = min(t + SEG, b)
            if not any(t < v1 and fin > v0 for v0, v1 in VETO.get(k, [])):
                tramos.append([k, round(t, 2), round(fin, 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    for k in gfx_keys:
        clips[k] = dict(src=f'gfx/{GFX[k]}', fam='gfx' + k, still=True)
        pool.append([k, 0, 3.2])
    return pool, clips


CREMA = '&H00E6F1F7&'       # texto de la palabra activa: papel crema #F7F1E6 en BGR
NARANJA = '&H002A62C8&'     # caja detras de la palabra activa: naranja quemado #C8622A en BGR

CIERRE = dict(type='end', occ=0,
              head=['TOCA ABAJO'],
              sub='y arma tu primer display esta semana',
              cta='Ver el paso a paso completo',
              sub2='Curso en video · ~2.000 imágenes · 13 formas de vender · Soporte · Acceso de por vida',
              img='gfx/celular_solo.png')

VIDEOS = [
    # R1 - demo con el objeto en la mano: la hoja contra el dinosaurio de dos metros
    dict(n=7, first=['a', 1.45], last='k', cta='clic', gfx='143',
         anchors=[('uniones', 0, '1', 0), ('video', 0, '4', 0), ('imágenes', 0, '3', 0)],
         tags=[('metros', 0, 'DOS METROS DE ALTO · HOJAS TAMAÑO CARTA')],
         chips=[('tarde', 0, 'Una tarde en el comedor')],
         plan=None),
    # R2 - declaracion de autoridad: cuatro anos de oficio sin pisar una imprenta
    dict(n=8, first=['d', 1.45], last='z', cta='clic', gfx='234',
         anchors=[('imprenta', 0, '2', 0), ('banco', 0, '3', 0), ('video', 0, '4', 0)],
         tags=[('real', 0, 'OSO · LETRAS · PERSONAJES DE TAMAÑO REAL')],
         chips=[('casa', 0, 'Impresora de escritorio')],
         plan=('hojas', 0, 'LO QUE HAY EN LA MESA', 'Nada más que esto',
               ['Un paquete de hojas', 'Cinta', 'Una impresora común'])),
    # R3 - pregunta-acertijo: de que esta hecho el leon de tamano real
    dict(n=9, first=['h', 5.45], last='w', cta='clic', gfx='13',
         anchors=[('técnica', 0, '1', 0), ('imágenes', 0, '3', 0)],
         tags=[('cartón', 0, 'NO ES CARTÓN · NO ES MADERA')],
         chips=[('cortadas', 0, 'Cortado en la mesa de casa')],
         plan=None),
]

for v in VIDEOS:
    pool, clips = pool_y_clips(v['gfx'], TODOS)
    overlays = [dict(type='tag', word=w, occ=o, text=t, dur=2.4) for w, o, t in v['tags']]
    overlays += [dict(type='chip', word=w, occ=o, text=t, dur=2.2) for w, o, t in v['chips']]
    if v.get('plan'):
        w, o, lab, tit, rows = v['plan']
        overlays.append(dict(type='plan', word=w, occ=o, label=lab, title=tit, rows=rows))
    fin = dict(CIERRE); fin['word'] = v['cta']
    overlays.append(fin)
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.6, 2.0, 2.5], words=3,
        music='music/bed_activo.wav', music_db=-9,
        hi=CREMA, hibox=NARANJA, hibord=20, capy=1340,
        first=v.get('first'), last=v.get('last'), seed=v['n'] * 911, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=overlays)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - %d tramos' % (v['n'], len(pool)))
