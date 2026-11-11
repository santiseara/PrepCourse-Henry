# -*- coding: utf-8 -*-
"""Planes de los 6 ads de la oferta de tapizado de sillones (Argentina, 2026-11-11).

Modelada de **Caprichos de Mar** / `aprendeatapizarsillones.impultienda.ar`: 19 ads activos en
Argentina, el mas viejo del 30 de octubre, curso de AR$39.990 en ImpulTienda con 3 bonos, grupo
de WhatsApp y garantia de 7 dias.

Su edicion, sacada de la hoja de contactos de 14 de sus videos:
  - b-roll de sillones ANTES/DESPUES, panoramicas lentas del sillon terminado
  - **banda blanca con texto negro arriba** durante el hook
  - subtitulos chicos BLANCOS, sin caja, abajo al centro, de 3 a 5 palabras
  - sin placa de cierre: cierran con el subtitulo sobre el ultimo plano
Eso se clona. Lo que agregamos son los insertos de producto dibujados por codigo
(`gfx_tapizar.py`), que ellos no tienen, y una placa final liviana con el CTA.

Argentina = **voseo** y, si entra una cifra, **una sola en pesos y como precio de mercado**
(regla del 2026-11-07). En esta tanda no entra ninguna: el guion 4 lo dice como multiplo.

Uso: python3 gen_tapizar_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/tapizar-sillones/anuncios/work')
SEG = 3.0
TOPE = 8

VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_tapizar.py')).read())

GFX = {'1': 'sistema.png', '2': 'herramientas.png', '3': 'todo.png', '4': 'celular.png'}
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


BLANCO = '&H00FFFFFF&'      # palabra activa en blanco: ellos NO resaltan en color
NEGRO = '&H00000000&'       # sin caja, solo el borde negro

CIERRE = dict(type='end', occ=0,
              head=['TOCÁ ABAJO'],
              sub='y empezá por el sillón que tenés en casa',
              cta='Ver las clases en video',
              sub2='Curso completo · Almohadones · La tela justa · Grupo de WhatsApp · Garantía de 7 días',
              img='gfx/celular_solo.png')

VIDEOS = [
    dict(n=1, first=['a', 0.0], last='f', cta='Tocá', gfx='24',
         hook='El sillón que iba a la basura', hook_until='nuevo.',
         anchors=[('taller', 0, '2', 0), ('video', 0, '4', 0)],
         tags=[('tapicero', 0, 'LA TELA LA PAGA EL CLIENTE')],
         chips=[('garage', 0, 'Un rincón alcanza')],
         plan=None),
    dict(n=2, first=['n', 0.0], last='b', cta='Tocá', gfx='21',
         hook='Tapizar no se cose: se clava', hook_until='clava.',
         anchors=[('martillo', 0, '2', 0), ('orden', 0, '1', 0)],
         tags=[('coser', 0, 'NI MÁQUINA NI MANOS DE MODISTA')],
         chips=[('paciencia', 0, 'Paciencia, no fuerza')],
         plan=None),
    dict(n=3, first=['e', 0.0], last='c', cta='Tocá', gfx='13',
         hook='El gato te arruinó la tela, no el sillón', hook_until='intacto.',
         anchors=[('video', 0, '1', 0), ('almohadones', 0, '3', 0)],
         tags=[('fracción', 0, 'LA ESTRUCTURA ESTÁ SANA')],
         chips=[('semana', 0, 'Un fin de semana')],
         plan=None),
    dict(n=4, first=['u', 0.0], last='i', cta='Tocá', gfx='13',
         hook='Un oficio que todos los barrios necesitan', hook_until='necesitan.',
         anchors=[('sistema', 0, '1', 0), ('presupuestar', 0, '3', 0)],
         tags=[('sano', 0, 'EN CADA CASA HAY UNO')],
         chips=[('WhatsApp', 0, 'Soporte por WhatsApp')],
         plan=None),
    dict(n=5, first=['o', 0.0], last='j', cta='Tocá', gfx='14',
         hook='El miedo no es que quede feo', hook_until='meses.',
         anchors=[('desarmar', 0, '1', 0), ('esquinas', 0, '4', 0)],
         tags=[('molde', 0, 'LA TELA VIEJA ES EL MOLDE')],
         chips=[('sábado', 0, 'Lo retomás el sábado')],
         plan=None),
    dict(n=6, first=['w', 0.0], last='x', cta='Tocá', gfx='23',
         hook='El sillón de tu abuela no se tira', hook_until='tapizar.',
         anchors=[('maciza', 0, '2', 0), ('clases', 0, '3', 0)],
         tags=[('coser', 0, 'SIN COSER · SIN MÁQUINAS · SIN TALLER')],
         chips=[('tijera', 0, 'Martillo, engrampadora y tijera')],
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
        speed=1.30, silence=[0.26, 0.12], cut=[2.0, 2.5, 3.0], words=4,
        music='music/bed_activo.wav', music_db=-9,
        hi=BLANCO, hibox=NEGRO, hibord=8, capy=1500,
        hook=v['hook'], hook_until=v['hook_until'],
        first=v.get('first'), last=v.get('last'), seed=v['n'] * 521, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=overlays)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - %d tramos' % (v['n'], len(pool)))
