# -*- coding: utf-8 -*-
"""Planes de los 6 ads de la Planilla Maestra (LATAM, 2026-11-12).

Competidor clonado: The Sheet Code (~57 ads activos en ingles, corriendo desde el 17/12/2025).
De ellos se copia el MONTAJE, no el guion:
  - V1, V3 y V5: la planilla en pantalla casi todo el video (es su formato "payday routine"),
    dibujada por codigo en gfx_planilla.py, bloque por bloque y en el orden del guion.
  - V2, V4 y V6: b-roll de TikTok con placas blancas redondeadas encima, que es su formato de
    resenas y de objeciones.
Sin cifras en moneda (regla del 8/11) y sin precio en el ad.

Uso: python3 gen_planilla_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/cuentas-claras/anuncios/work')
HI = '&H00FFFFFF&'      # texto de la palabra activa: blanco
HIBOX = '&H00525E2E&'   # caja detras: verde salvia oscuro #2E5E52 en BGR

CIERRE = dict(type='end', occ=0,
              head=['TOCÁ ABAJO'],
              sub='y ordená tus finanzas esta misma semana',
              cta='Ver la planilla completa',
              sub2='21 hojas · Google Sheets y Excel · Guía de 60 páginas · Pago único · 30 días de garantía',
              img='gfx/producto.png')


def stills(nombres, prefijo):
    """clips + pool a partir de las capturas de la planilla, dos entradas por captura."""
    clips, pool = {}, []
    for i, nom in enumerate(nombres):
        k = chr(ord('a') + i)
        clips[k] = dict(src=f'sheet/{nom}.png', still=True)
        pool += [[k, 0, 3.2], [k, 0.3, 3.5]]
    return clips, pool


# ------------------------------------------------------------------ pantalla
V1_SHEETS = ['g1_mes', 'g1_ing0', 'g1_ing1', 'g1_ing2', 'g1_fij0', 'g1_fij1',
             'g1_fij2', 'g1_sus', 'g1_var1', 'g1_var2', 'g1_dist', 'g1_res']
V1_ANCHORS = [('mes', 0, 'a', 0), ('cargo', 0, 'b', 0), ('cobro', 0, 'c', 0), ('dos', 1, 'd', 0),
              ('fijos', 0, 'e', 0), ('luz', 0, 'f', 0), ('fecha', 0, 'g', 0),
              ('suscripciones', 0, 'h', 0), ('variables', 0, 'i', 0), ('ropa', 0, 'j', 0),
              ('separa', 0, 'k', 0), ('pantalla', 0, 'l', 0)]

V3_SHEETS = ['g1_mes', 'g3_ing0', 'g3_ing', 'g3_fij0', 'g3_fij', 'g3_sus', 'g3_var0', 'g3_var',
             'g3_deu0', 'g3_deu', 'g3_lib', 'g3_dist', 'g3_plan']
V3_ANCHORS = [('cuentas', 0, 'a', 0), ('ingresos', 0, 'b', 0), ('extra', 0, 'c', 0),
              ('fijos', 0, 'd', 0), ('celulares', 0, 'e', 0), ('suscripciones', 0, 'f', 0),
              ('variables', 0, 'g', 0), ('ropa', 0, 'h', 0), ('deudas', 0, 'i', 0),
              ('tasa', 0, 'j', 0), ('ahorro', 0, 'k', 0), ('reparte', 0, 'l', 0),
              ('plan', 0, 'm', 0)]

V5_SHEETS = ['g1_mes', 'g1_var1', 'g1_var2', 'g5_pat', 'g5_cat', 'g1_dist', 'g5_met', 'g5_res']
V5_ANCHORS = [('mes', 0, 'a', 0), ('anotar', 1, 'b', 0), ('hiciste', 0, 'c', 0),
              ('número', 0, 'd', 0), ('categorías', 0, 'e', 0), ('mano', 0, 'f', 0),
              ('metas', 0, 'g', 0), ('adivinar', 0, 'h', 0)]

PANTALLA = {
    1: dict(sheets=V1_SHEETS, anchors=V1_ANCHORS, hook='RUTINA DEL DÍA DE PAGO',
            hook_until='clínica',
            overlays=[dict(type='chip', word='tres', occ=0, text='Tres que no usaba', dur=2.4),
                      dict(type='tag', word='necesario', occ=0, text='NECESIDADES · GUSTOS · AHORRO', dur=2.4)]),
    3: dict(sheets=V3_SHEETS, anchors=V3_ANCHORS, hook='DOS SUELDOS, CERO AHORRO',
            hook_until='nada',
            overlays=[dict(type='chip', word='tasa', occ=0, text='Cada deuda con su tasa', dur=2.4),
                      dict(type='tag', word='concreta', occ=0, text='CON FECHA DE SALIDA', dur=2.6)]),
    5: dict(sheets=V5_SHEETS, anchors=V5_ANCHORS, hook='ANOTAR NO ES PRESUPUESTAR',
            hook_until='presupuestar',
            overlays=[dict(type='chip', word='restas', occ=0, text='Sin restas a mano', dur=2.4),
                      dict(type='tag', word='sobre', occ=0, text='UN SOBRE POR META', dur=2.4)]),
}


def plan_pantalla(n):
    v = PANTALLA[n]
    clips, pool = stills(v['sheets'], n)
    overlays = list(v['overlays'])
    fin = dict(CIERRE); fin['word'] = 'link'; fin['occ'] = 0
    overlays.append(fin)
    return dict(
        vo=f'vo/V{n}.wav', script=f'V{n}.txt', lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music_db=-9, hi=HI, hibox=HIBOX, hibord=20, capy=1420, nosfx=True,
        hook=v['hook'], hook_until=v['hook_until'],
        first=['a', 0], last=chr(ord('a') + len(v['sheets']) - 1),
        seed=n * 401, usage='usage.json',
        clips=clips, pool=pool, seq=[chr(ord('a') + i) for i in range(len(v['sheets']))],
        anchors=v['anchors'], overlays=overlays)




# ------------------------------------------------------------------ b-roll + placas
SEG, TOPE = 2.6, 6
VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_planilla.py')).read())

BROLL = {
    2: dict(hook='CASI MIL RESEÑAS DE 5 ESTRELLAS', hook_until='Excel',
            gfx={'1': 'res1', '2': 'res2', '3': 'res3', '4': 'g5_pat', '5': 'g1_res'},
            anchors=[('Carolina', 0, '1', 0), ('Martín', 0, '2', 0), ('Valentina', 0, '3', 0),
                     ('lugar', 0, '4', 0), ('estrellas', 0, '5', 0)],
            chips=[('cuenta', 0, 'Sin acceso a tu banco')],
            tags=[('todo', 1, 'UN SOLO LUGAR CON TODO')]),
    4: dict(hook='PAGAR TODOS LOS MESES, ¿PARA QUÉ?', hook_until='gastaste',
            gfx={'1': 'g1_mes', '2': 'g5_pat', '3': 'g3_deu', '4': 'g6_cal', '5': 'g1_res',
                 '6': 'g1_dist'},
            anchors=[('planilla', 0, '1', 0), ('tienes', 0, '2', 0), ('debes', 0, '3', 0),
                     ('vence', 0, '4', 0), ('libre', 0, '5', 0), ('hojas', 0, '6', 0)],
            chips=[('clave', 0, 'Sin la clave de tu banco')],
            tags=[('tuya', 0, 'PAGO ÚNICO · SIN MENSUALIDAD')]),
    6: dict(hook='LOS RECARGOS NO SON FALTA DE DINERO', hook_until='fecha',
            gfx={'1': 'g6_cal', '2': 'g1_sus', '3': 'g1_res', '4': 'g1_dist', '5': 'g1_mes'},
            anchors=[('calendario', 0, '1', 0), ('suscripciones', 0, '2', 0),
                     ('tablero', 0, '3', 0), ('libre', 0, '4', 0), ('archivo', 0, '5', 0)],
            chips=[('intereses', 0, 'Recargos por olvido')],
            tags=[('pase', 0, 'EL AVISO LLEGA ANTES')]),
}


def plan_broll(n):
    v = BROLL[n]
    clips, pool = {}, []
    for k, (fn, a, b, ex) in VENT.items():
        d = dict(src=f'clips/{fn}.mp4'); d.update(ex)
        clips[k] = d
        tramos, t = [], a
        while t < b - 1.5:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    for k, nom in v['gfx'].items():
        # una sola entrada por captura: con dos, la misma hoja salia cuatro veces en V4
        clips[k] = dict(src=f'sheet/{nom}.png', still=True)
        pool.append([k, 0, 3.2])
    overlays = [dict(type='chip', word=w, occ=o, text=t, dur=2.4) for w, o, t in v['chips']]
    overlays += [dict(type='tag', word=w, occ=o, text=t, dur=2.4) for w, o, t in v['tags']]
    fin = dict(CIERRE); fin['word'] = 'link'; fin['occ'] = 0
    overlays.append(fin)
    return dict(
        vo=f'vo/V{n}.wav', script=f'V{n}.txt', lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music_db=-9, hi=HI, hibox=HIBOX, hibord=20, capy=1420, nosfx=True,
        hook=v['hook'], hook_until=v['hook_until'],
        first=['f', 3.0], seed=n * 613, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=overlays)

if __name__ == '__main__':
    import sys
    cuales = [int(x) for x in sys.argv[1:]] or [1, 2, 3, 4, 5, 6]
    for n in cuales:
        if n in PANTALLA:
            json.dump(plan_pantalla(n), open(f'{WK}/V{n}.json', 'w'), ensure_ascii=False, indent=1)
            print(f'V{n} listo (pantalla)')
        else:
            json.dump(plan_broll(n), open(f'{WK}/V{n}.json', 'w'), ensure_ascii=False, indent=1)
            print(f'V{n} listo (b-roll)')
