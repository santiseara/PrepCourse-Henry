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

V3_SHEETS = ['g3_ing', 'g3_fij', 'g3_sus', 'g3_var', 'g3_deu', 'g3_lib', 'g3_dist', 'g3_plan']
V3_ANCHORS = [('ingresos', 0, 'a', 0), ('fijos', 0, 'b', 0), ('suscripciones', 0, 'c', 0),
              ('variables', 0, 'd', 0), ('deudas', 0, 'e', 0), ('ahorro', 0, 'f', 0),
              ('reparte', 0, 'g', 0), ('plan', 0, 'h', 0)]

V5_SHEETS = ['g5_pat', 'g5_cat', 'g5_met', 'g5_res']
V5_ANCHORS = [('número', 0, 'a', 0), ('categorías', 0, 'b', 0), ('metas', 0, 'c', 0),
              ('adivinar', 0, 'd', 0)]

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
        clips=clips, pool=pool, anchors=v['anchors'], overlays=overlays)


if __name__ == '__main__':
    import sys
    cuales = [int(x) for x in sys.argv[1:]] or [1, 3, 5]
    for n in cuales:
        if n in PANTALLA:
            json.dump(plan_pantalla(n), open(f'{WK}/V{n}.json', 'w'), ensure_ascii=False, indent=1)
            print(f'V{n} listo (pantalla)')
