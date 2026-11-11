# -*- coding: utf-8 -*-
"""Planes de las 3 renovaciones de The Party Box Vault (mercado ingles, 2026-11-11).

Clonado de Moldes Prontos / caixinha cenario (page 1288335281030909, 51 ads activos).
La edicion del ganador, sacada de la hoja de contactos de 10 de sus videos:
  - b-roll de manos armando y llenando cajitas, el producto en pantalla todo el tiempo
  - subtitulos de UNA palabra, texto negro dentro de una caja AMARILLA, abajo al centro
  - sin caja de hook ni placa de apertura
  - insertos del producto (la carpeta de moldes, el indice) con un chip grande encima
  - voz en off de mujer, cierre con "Clique em Saiba Mais"

Lectura de la cuenta del 11/11 (captura de Santiago, 6 conjuntos, $63,22 de gasto, 3 compras):
  CJTO 3 - "There is no month of the year..."   2 compras   $7,12   <- GANADOR
  CJTO 5 - "Your saved folder is full..."       1 compra    $14,10
  CJTO 1 / 2 / 4 / 6                            0 compras
Lo que vendio es la DEMANDA (el calendario, "esa parte no la hace nadie") y la comparacion
social con catalogo. Lo que murio son los angulos de mecanismo (la impresora, no hace falta
disenar) y los emocionales (la caja contra el regalo, el storytime). Frecuencia 1,39: no hay
fatiga de publico todavia, asi que se renueva el HOOK, no el alcance.

Las 3 renovaciones llevan el **cuerpo del CJTO 3 copiado textual** y cambian el formato del hook:
  R1 - el trabajo que nadie tomo (tres cobran, uno queda vacio)
  R2 - la escena de la puerta cuando termina la fiesta
  R3 - la misma mama compra cuatro veces este anio

Y cambia la estetica, que es la otra mitad de una renovacion: la caja del subtitulo deja de ser
amarilla en los tres y pasa a **un color por creativo** (coral, verde, violeta), otro ritmo de
corte y planos nuevos con offset de +1,4 s sobre las mismas ventanas ya revisadas.

Uso: python3 gen_boxes_plans_11.py   -> escribe R1.json .. R3.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/party-box-vault/anuncios/work')
SEG = 2.8
OFF = 1.4            # desplazamiento sobre la tanda del 10/11 -> tramos nuevos
TOPE = 10

VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_boxes.py')).read())

GFX = {'1': 'libreria.png', '2': 'celular.png', '3': 'armado.png', '4': 'calendario.png'}
TODOS = ''.join(VENT.keys())


def pool_y_clips(gfx_keys, claves):
    pool, clips = [], {}
    for k in claves:
        fn, a, b, ex = VENT[k]
        d = dict(src=f'clips/{fn}.mp4'); d.update(ex)
        clips[k] = d
        tramos, t = [], a + (OFF if b - a > OFF + SEG + 1.6 else 0)
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


NEGRO = '&H00000000&'       # texto de la palabra activa: negro
BLANCO_T = '&H00FFFFFF&'    # texto blanco para las cajas oscuras
CORAL = '&H005668F0&'       # caja coral #F06856 en BGR
VERDE = '&H00569B2E&'       # caja verde #2E9B56 en BGR
VIOLETA = '&H00B0509B&'     # caja violeta #9B50B0 en BGR
# el amarillo del ganador (#FFE800) queda para la tanda del 10/11: una renovacion cambia la estetica

CIERRE = dict(type='end', occ=0,
              head=['TAP BELOW'],
              sub='and print your first box tonight',
              cta='See every theme inside',
              sub2='300+ templates · assembly video · First Sale Kit · 100 ready messages',
              img='gfx/celular_solo.png')

VIDEOS = [
    dict(n=1, cta='Tap', gfx='14', first='i', last='s',
         hi=NEGRO, hibox=CORAL,
         anchors=[('templates', 0, '1', 0), ('phone', 0, '4', 0)],
         tags=[('backdrop', 0, 'THE CAKE · THE BALLOONS · THE BACKDROP')],
         chips=[('supermarket', 0, 'Thrown together the night before')],
         plan=None),
    dict(n=2, cta='Tap', gfx='13', first='t', last='q',
         hi=BLANCO_T, hibox=VERDE,
         anchors=[('templates', 0, '1', 0), ('season', 0, '3', 0)],
         tags=[('making', 0, 'NOBODY IS MAKING THIS PART')],
         chips=[('fold', 0, 'Print, cut, fold')],
         plan=None),
    dict(n=3, cta='Tap', gfx='14', first='c', last='l',
         hi=BLANCO_T, hibox=VIOLETA,
         anchors=[('templates', 0, '1', 0), ('calendar', 0, '4', 0)],
         tags=[('Christmas', 0, 'BIRTHDAY · BABY SHOWER · SCHOOL · CHRISTMAS')],
         chips=[('season', 0, 'A product with no season')],
         plan=None),
]

def _first(pool, k):
    if not k: return None
    seg = next((x for x in pool if x[0] == k), None)
    if seg is None: raise SystemExit('first %r no esta en el pool' % k)
    return [seg[0], seg[1]]


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
        vo=f"vo/R{v['n']}.wav", script=f"R{v['n']}.txt", lang='en',
        speed=1.30, silence=[0.26, 0.12], cut=[1.6, 2.1, 2.6], words=1,
        music='music/bed_activo.wav', music_db=-9,
        hi=v['hi'], hibox=v['hibox'], hibord=20, capy=1340,
        first=_first(pool, v.get('first')), last=v.get('last'), seed=v['n'] * 211, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=overlays)
    json.dump(plan, open(f"{WK}/R{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('R%d listo - %d tramos' % (v['n'], len(pool)))
