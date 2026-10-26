# -*- coding: utf-8 -*-
"""Piezas que se repiten en muchos planos."""
from engine import *

def patas(mat, L, A, H, z0=0.0, tag='pata', rol='pata', inset=0.0):
    w = M[mat]['w']
    d = w/2.0 + inset
    return [vz(tag, rol, mat, z0, H, x, y)
            for x in (d, L-d) for y in (d, A-d)]

def mesa(mat, L, A, H, tapa=None, est_z=None, mat_est=None, n_trav=0,
         mat_trav=None, rol_tapa='tapa', corte_patas=None):
    """Marco superior a 45 + 4 patas por dentro + travesaños + estante + tapa."""
    w = M[mat]['w']
    mat_trav = mat_trav or mat
    mat_est = mat_est or mat
    pz = marco_xy('marco', 'marco de arriba', mat, 0, L, 0, A, H - w/2.0)
    pz += patas(mat, L, A, H - w, rol='pata')
    for x in interiores(0, L, n_trav):
        pz.append(vy('trav', 'travesaño del medio', mat_trav, w, A-w, x, H - w/2.0))
    if est_z is not None:
        we = M[mat_est]['w']
        pz += [vx('est', 'marco del estante', mat_est, w/2.0, L-w/2.0, w + we/2.0, est_z),
               vx('est', 'marco del estante', mat_est, w/2.0, L-w/2.0, A-w-we/2.0, est_z),
               vy('estb', 'marco del estante', mat_est, w, A-w, w + we/2.0, est_z),
               vy('estb', 'marco del estante', mat_est, w, A-w, L-w-we/2.0, est_z)]
    if tapa:
        pz.append(chapa_h('tapa', rol_tapa, tapa, 0, L, 0, A, H, extra={'sin_vista': ('planta',)}))
    return pz

def ruedas(mat_sop, L, A, z=0.0, diam=100, tag='rueda'):
    """Cuatro placas de amure para ruedas (la rueda se compra hecha)."""
    t = 'PL100'
    return [chapa_h(tag, 'placa de amure de rueda', 'CH6', x-50, x+50, y-50, y+50, z)
            for x in (90, L-90) for y in (90, A-90)]

def diagonal(tag, rol, mat, p1, p2, **kw):
    return Pz(tag, rol, mat, p1, p2, corte='en ángulo', **kw)

def panel_barrotes(tag, rol, mat, x0, x1, y, z0, z1, n, vertical=True):
    """Barrotes repartidos entre dos puntos."""
    out = []
    for x in interiores(x0, x1, n):
        out.append(vz(tag, rol, mat, z0, z1, x, y))
    return out

HERR_BASE = ['soldadora', 'amoladora', 'escuadra', 'sargentos', 'cinta de medir', 'disco de corte']
HERR_CHAPA = HERR_BASE + ['disco de láminas']
HERR_PLUS = HERR_BASE + ['mechas', 'agujereadora']

CIERRE_PINTURA = ('Desbastá la escoria, pasá disco de láminas por cada cordón y matá los cantos vivos. '
                  'Desengrasá, una mano de fondo antióxido y dos de esmalte sintético.')
