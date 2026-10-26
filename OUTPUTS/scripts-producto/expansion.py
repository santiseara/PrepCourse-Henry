# -*- coding: utf-8 -*-
"""Genera la biblioteca completa: las cantidades por categoría que promete la landing."""
import os, re, itertools
import cat_tr, cat_bq, cat_gy, cat_fm, cat_sh, cat_tk, cat_fn, cat_st

MODS = {'TR': cat_tr, 'BQ': cat_bq, 'GY': cat_gy, 'FM': cat_fm,
        'SH': cat_sh, 'TK': cat_tk, 'FN': cat_fn, 'ST': cat_st}

OBJETIVO = {'TR': 180, 'BQ': 145, 'GY': 120, 'FM': 210,
            'SH': 165, 'TK': 95, 'FN': 180, 'ST': 110}

HERE = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------- planos pinchados
def _curados():
    """Las combinaciones que ya tenían código asignado (los que salieron en los ads)."""
    ruta = os.path.join(HERE, 'curados.txt')
    pin = {}
    orden = {}
    if not os.path.exists(ruta): return pin, orden
    for linea in open(ruta, encoding='utf-8'):
        if not linea.strip(): continue
        cod, func, args = [x.strip() for x in linea.split('|')]
        tupla = eval('(%s,)' % args) if args else ()
        pin[(func, tupla)] = cod
        orden.setdefault(func, []).append(tupla)
    return pin, orden

PIN, CURADOS = _curados()

def _mezclar(func, grilla):
    """Primero los curados de esa familia, después el resto de la grilla sin repetir."""
    vistos = []
    for t in CURADOS.get(func, []):
        if t not in vistos: vistos.append(t)
    for t in grilla:
        if t not in vistos: vistos.append(t)
    return vistos

def niv(h):
    return 'Principiante' if h[0] <= 6 else ('Intermedio' if h[0] <= 14 else 'Avanzado')

# ================================================================= grillas
def gr_trailer_util():
    out = []
    for L in range(1500, 3001, 100):
        for A in (1100, 1250, 1400, 1500, 1600):
            if A > L*0.72: continue
            for b in (350, 450, 600):
                out.append((L, A, b))
    return out

def gr_trailer_rampa():
    return [(L, A, 300) for L in (3600, 4000, 4400, 4880, 5200, 5600, 6000)
            for A in (1800, 2080, 2300)]

def gr_carro_quinta():
    return [(L, A, 500) for L in (1500, 1800, 2000, 2200, 2400, 2800)
            for A in (1000, 1200, 1400)]

def gr_zorra():
    return [(L, A, H) for L in (800, 1000, 1200, 1400, 1600)
            for A in (500, 600, 700, 800) for H in (400, 500)]

def gr_porta_autos():
    return [(L, A, 400) for L in (5500, 6100, 6700, 7300) for A in (2200, 2440)]

def gr_lancha():
    return [(L, A, 420) for L in (4000, 4500, 5000, 5500, 6000, 6500)
            for A in (1600, 1800, 2000)]

def gr_fogonero_hex():
    out = []
    for across in (800, 900, 1000, 1100, 1220, 1350, 1500):
        for alto in (300, 350, 400, 450):
            mat = 'CH3' if across <= 1000 else 'CH47'
            h = (4, 6) if across <= 900 else ((6, 9) if across <= 1250 else (8, 11))
            out.append((across, alto, mat, h))
    return out

def gr_fogonero_cuad():
    return [(L, alto) for L in (500, 600, 700, 800, 900, 1000) for alto in (300, 350, 400)]

def gr_parrilla_carro():
    out = []
    for L in (1000, 1200, 1400, 1500, 1600, 1830, 2000, 2200):
        for A in (600, 700, 760):
            h = (9, 12) if L <= 1300 else ((10, 14) if L <= 1600 else (12, 16))
            out.append((L, A, 850, h, niv(h)))
    return out

def gr_santa_maria():
    return [(L, A, 900) for L in (1200, 1520, 1800, 2000) for A in (700, 800)]

def gr_ahumador_offset():
    return [(D, L) for D in (460, 560, 600) for L in (1200, 1520, 1800)]

def gr_ahumador_vertical():
    return [(L, A, H) for L in (500, 600, 700) for A in (500, 600) for H in (1200, 1500, 1800)]

def gr_parrilla_portatil():
    return [(L, A, H) for L in (500, 600, 700, 800) for A in (300, 400, 500) for H in (250, 300)]

def gr_mesa_parrilla():
    return [(L, A, 900) for L in (900, 1100, 1300, 1500) for A in (500, 600, 700)]

def gr_jaula():
    out = []
    for L in (1100, 1200, 1320, 1450):
        for A in (1100, 1200, 1520, 1650):
            for H in (2100, 2150, 2300, 2440):
                out.append((L, A, H, 'TC80' if H >= 2300 else 'TC60'))
    return out

def gr_rig():
    return [(L, A, H) for L in (2440, 3000, 3600) for A in (1200, 1500) for H in (2740, 3000)]

def gr_banco_plano():
    return [(r, L, A, H) for r in (False, True) for L in (1000, 1100, 1200)
            for A in (280, 300, 320) for H in (420, 450)]

def gr_rack_discos():
    return [(L, A, H) for L in (700, 900, 1100) for A in (400, 500) for H in (800, 900, 1000)]

def gr_squat():
    return [(L, A, H) for L in (1000, 1200, 1400) for A in (600, 700, 800)
            for H in (1600, 1800, 2000)]

def gr_dominadas():
    return [(L, A, H) for L in (900, 1100, 1200, 1400) for A in (500, 600, 700) for H in (500, 600)]

def gr_torre():
    return [(L, A, H) for L in (800, 1000, 1200) for A in (400, 450, 500) for H in (700, 800, 900)]

def gr_porton_campo():
    out = []
    for L in range(1800, 5201, 200):
        for H in (1000, 1100, 1150, 1200, 1300):
            for n in (4, 5, 6):
                out.append((L, H, n))
    return out

def gr_porton_corredizo():
    return [(L, H) for L in range(2500, 6001, 250) for H in (1600, 1800, 2000, 2200)]

def gr_tranquera():
    return [(L, H) for L in (2000, 2500, 3000, 3500, 4000, 4500) for H in (1000, 1100, 1200, 1300)]

def gr_comedero():
    return [(L, A, H) for L in (1500, 2000, 2500, 3000, 3500, 4000) for A in (500, 600, 700)
            for H in (450, 500, 550)]

def gr_panel_corral():
    return [(L, H) for L in (1500, 2000, 2500, 3000, 3500, 4000, 4500) for H in (1000, 1200, 1400, 1600, 1800)]

def gr_puerta_peatonal():
    return [(L, H) for L in (700, 800, 900, 1000, 1100, 1200, 1300) for H in (1700, 1800, 1900, 2000, 2100, 2200)]

def gr_porton_dos_hojas():
    return [(L, H) for L in range(2600, 5401, 200) for H in (1600, 1800, 1900, 2100, 2300)]

def gr_mesa_soldar():
    out = []
    for L in (900, 1000, 1100, 1220, 1400, 1500, 1600, 1800, 2000):
        for A in (600, 700, 760, 800, 900):
            if A > L*0.72: continue
            for tapa in ('CH47', 'CH6'):
                h = (4, 6) if L <= 1100 else ((5, 7) if L <= 1500 else (7, 10))
                out.append((L, A, 900, tapa, h, niv(h)))
    return out

def gr_mesa_pesada():
    return [(L, A, 900) for L in (2400, 3000, 3600) for A in (1000, 1200, 1500)]

def gr_banco_trabajo():
    return [(L, A, H) for L in (1200, 1500, 1800, 2000) for A in (600, 700, 800) for H in (900, 950)]

def gr_caballete():
    return [(L, A, H) for L in (700, 900, 1100) for A in (500, 600, 700) for H in (600, 750, 900)]

def gr_carro_herr():
    return [(L, A, H) for L in (600, 760, 900) for A in (400, 460, 520) for H in (750, 850, 950)]

def gr_estanteria():
    return [(L, A, H, n) for L in (900, 1200, 1500, 1800, 2000) for A in (400, 450, 500, 600)
            for H in (1500, 1800, 2000) for n in (4, 5)]

def gr_rack_barras():
    return [(L, H, A) for L in (2000, 3000, 4000) for H in (1600, 2000, 2400) for A in (400, 500, 600)]

def gr_mesa_moto():
    return [(L, A, H) for L in (1800, 2130, 2400) for A in (700, 760, 900) for H in (500, 600, 700)]

def gr_escuadra():
    return [(L,) for L in (300, 400, 500, 600, 800)]

def gr_banco_morsa():
    return [(L, A, H) for L in (600, 700, 800, 900) for A in (450, 550, 650) for H in (900, 950)]

def gr_rack_caja():
    return [(L, A, H) for L in (1600, 1800, 2000, 2200, 2440, 2600) for A in (1300, 1400, 1450, 1500, 1600)
            for H in (600, 650, 700, 800)]

def gr_protector():
    return [(L, H, luz) for L in (1400, 1500, 1600, 1700, 1800) for H in (800, 900, 950, 1050)
            for luz in (False, True)]

def gr_bandeja():
    return [(L, A) for L in (2000, 2300, 2500, 2740, 3000) for A in (1800, 1900, 2030, 2200)]

def gr_barras_techo():
    return [(L, A) for L in (1100, 1200, 1300, 1400, 1500) for A in (1000, 1100, 1200, 1400)]

def gr_portabicis():
    return [(L, A, H) for L in (1000, 1200, 1400) for A in (500, 600, 700) for H in (450, 500, 600)]

def gr_jaula_caja():
    return [(L, A, H) for L in (1800, 2000, 2200, 2400) for A in (1300, 1400, 1500, 1600)
            for H in (500, 600, 700)]

def gr_mesa_x():
    return [(L, A, 760, mat) for L in (1600, 1800, 2000, 2200, 2440, 2600, 3000)
            for A in (800, 900, 1000, 1020, 1100) for mat in ('TC50', 'TC60') if A <= L*0.52]

def gr_mesa_recta():
    return [(L, A, H) for L in (1000, 1200, 1400, 1600, 1800, 2000, 2200)
            for A in (600, 700, 800, 900) for H in (750, 760) if A <= L*0.62]

def gr_banqueta():
    return [(L, L, H) for L in (350, 380, 400, 450) for H in (450, 550, 650, 750, 800)]

def gr_estanteria_ind():
    return [(L, A, H, n) for L in (700, 900, 1100, 1300) for A in (300, 350, 400)
            for H in (1400, 1800, 2100) for n in (4, 5, 6)]

def gr_mesa_ratona():
    return [(L, A, H) for L in (900, 1100, 1300) for A in (500, 600, 700) for H in (400, 450, 500)]

def gr_isla():
    return [(L, A, H) for L in (1600, 1800, 2130, 2400) for A in (800, 910, 1000) for H in (900, 950)]

def gr_botellero():
    return [(L, A, H) for L in (700, 900, 1100) for A in (350, 400, 450) for H in (1400, 1800, 2000)]

def gr_cama():
    out = []
    for L, A, nom in ((1900, 800, 'Cama de una plaza con respaldo'),
                      (1900, 900, 'Cama de una plaza con respaldo'),
                      (1900, 1000, 'Cama de plaza y media con respaldo'),
                      (1900, 1400, 'Cama de dos plazas con respaldo'),
                      (2000, 1400, 'Cama de dos plazas con respaldo'),
                      (1900, 1600, 'Cama queen con respaldo'),
                      (2000, 1600, 'Cama queen con respaldo'),
                      (2000, 1800, 'Cama king con respaldo'),
                      (1900, 1800, 'Cama king con respaldo')):
        out.append((L, A, nom))
    return out

def gr_perchero():
    return [(L, A, H) for L in (900, 1200, 1500) for A in (400, 500, 600) for H in (1600, 1700, 1800)]

def gr_escritorio():
    return [(L, A, H) for L in (1100, 1200, 1400, 1600, 1800) for A in (600, 700, 800) for H in (740, 750, 760)]

def gr_banco_jardin():
    return [(L, A, H) for L in (1200, 1500, 1800, 2000) for A in (550, 600, 650) for H in (850, 900)]

def gr_pergola():
    return [(L, A, H) for L in (2500, 3000, 3500, 4000, 4500, 5000, 6000)
            for A in (2500, 3000, 3500, 4000) for H in (2300, 2400, 2500) if A <= L]

def gr_cochera():
    return [(L, A, zb, za) for L in (3000, 3500, 5500, 6000) for A in (5000, 5500, 6000)
            for (zb, za) in ((2300, 2750), (2400, 3000))]

def gr_escalera():
    out = []
    for H in range(1600, 3701, 100):
        for n in range(max(8, int(H/230)-1), int(H/160)+1):
            paso = 250 if H/n > 180 else 280
            out.append((H, int(paso*n), n))
    return out

def gr_baranda():
    return [(L, H) for L in range(1000, 5001, 250) for H in (900, 1000, 1050, 1100, 1200)]

def gr_alero():
    return [(L, A, H) for L in (1500, 2000, 2500, 3000) for A in (900, 1200, 1500) for H in (2300, 2400, 2600)]

def gr_invernadero():
    return [(L, A, H, Hc) for L in (4000, 6000, 8000, 10000) for A in (3000, 4000, 5000)
            for (H, Hc) in ((2000, 2600), (2200, 2900))]

def gr_escalera_gato():
    return [(H, A) for H in range(2000, 6001, 250) for A in (400, 450, 500, 600)]

# ================================================================= familias por categoría
FAMILIAS = {
 'TR': [('trailer_util', gr_trailer_util, 8), ('trailer_rampa', gr_trailer_rampa, 1),
        ('carro_quinta', gr_carro_quinta, 1), ('zorra', gr_zorra, 1),
        ('porta_autos', gr_porta_autos, 1), ('trailer_lancha', gr_lancha, 1)],
 'BQ': [('fogonero_hex', gr_fogonero_hex, 3), ('fogonero_cuad', gr_fogonero_cuad, 2),
        ('parrilla_carro', gr_parrilla_carro, 3), ('santa_maria', gr_santa_maria, 1),
        ('ahumador_offset', gr_ahumador_offset, 1), ('ahumador_vertical', gr_ahumador_vertical, 1),
        ('parrilla_portatil', gr_parrilla_portatil, 2), ('mesa_parrilla', gr_mesa_parrilla, 1),
        ('disco_arado', lambda: [()], 1)],
 'GY': [('jaula', gr_jaula, 3), ('rig', gr_rig, 1), ('banco_plano', gr_banco_plano, 2),
        ('rack_discos', gr_rack_discos, 1), ('squat_stand', gr_squat, 2),
        ('dominadas_pared', gr_dominadas, 2), ('torre_mancuernas', gr_torre, 2)],
 'FM': [('porton_campo', gr_porton_campo, 5), ('porton_corredizo', gr_porton_corredizo, 2),
        ('tranquera', gr_tranquera, 2), ('comedero', gr_comedero, 2),
        ('panel_corral', gr_panel_corral, 2), ('puerta_peatonal', gr_puerta_peatonal, 2),
        ('porton_dos_hojas', gr_porton_dos_hojas, 2)],
 'SH': [('mesa_soldar', gr_mesa_soldar, 4), ('mesa_pesada', gr_mesa_pesada, 1),
        ('banco_trabajo', gr_banco_trabajo, 2), ('caballete', gr_caballete, 1),
        ('carro_herramientas', gr_carro_herr, 1), ('estanteria', gr_estanteria, 3),
        ('rack_barras', gr_rack_barras, 1), ('mesa_moto', gr_mesa_moto, 1),
        ('escuadra_armado', gr_escuadra, 1), ('banco_morsa', gr_banco_morsa, 1)],
 'TK': [('rack_caja', gr_rack_caja, 3), ('protector_cabina', gr_protector, 3),
        ('bandeja_plana', gr_bandeja, 1), ('barras_techo', gr_barras_techo, 1),
        ('portabicis', gr_portabicis, 1), ('jaula_caja', gr_jaula_caja, 1)],
 'FN': [('mesa_x', gr_mesa_x, 3), ('mesa_recta', gr_mesa_recta, 3), ('banqueta', gr_banqueta, 2),
        ('estanteria_ind', gr_estanteria_ind, 3), ('mesa_ratona', gr_mesa_ratona, 1),
        ('isla_cocina', gr_isla, 1), ('botellero', gr_botellero, 1), ('cama', gr_cama, 1),
        ('perchero', gr_perchero, 1), ('escritorio', gr_escritorio, 2), ('banco_jardin', gr_banco_jardin, 1)],
 'ST': [('pergola', gr_pergola, 3), ('cochera', gr_cochera, 2), ('escalera', gr_escalera, 3),
        ('baranda_galeria', gr_baranda, 2), ('alero', gr_alero, 2),
        ('invernadero', gr_invernadero, 1), ('escalera_gato', gr_escalera_gato, 1)],
}

def _codigos_libres(cat, usados, cuantos):
    libres = []
    n = 1
    while len(libres) < cuantos:
        cod = '%s-%03d' % (cat, n)
        if cod not in usados: libres.append(cod)
        n += 1
    return libres

def generar(objetivo=None):
    """Devuelve la lista completa de planos con su código asignado."""
    objetivo = objetivo or OBJETIVO
    todos = []
    for cat, _nom, _sub in __import__('engine').CATS:
        meta = objetivo[cat]
        fams = [(nombre, _mezclar(nombre, grilla()), peso) for nombre, grilla, peso in FAMILIAS[cat]]
        elegidos = []
        idx = [0]*len(fams)
        while len(elegidos) < meta:
            avance = False
            for i, (nombre, combos, peso) in enumerate(fams):
                for _ in range(peso):
                    if idx[i] < len(combos) and len(elegidos) < meta:
                        elegidos.append((nombre, combos[idx[i]])); idx[i] += 1; avance = True
            if not avance:
                raise RuntimeError('faltan combinaciones en %s: %d de %d' % (cat, len(elegidos), meta))
        mod = MODS[cat]
        fijos = {}
        libres_necesarios = 0
        for nombre, args in elegidos:
            cod = PIN.get((nombre, args))
            if cod: fijos[(nombre, args)] = cod
            else: libres_necesarios += 1
        libres = _codigos_libres(cat, set(fijos.values()), libres_necesarios)
        it = iter(libres)
        lote = []
        for nombre, args in elegidos:
            pl = getattr(mod, nombre)(*args)
            pl.codigo = fijos.get((nombre, args)) or next(it)
            pl.familia = nombre
            pl.args = args
            lote.append(pl)
        lote.sort(key=lambda p: p.codigo)
        todos.extend(lote)
    return todos

if __name__ == '__main__':
    import collections, engine
    engine.registrar_fuentes()
    ps = generar()
    c = collections.Counter(p.cat for p in ps)
    for cat, nom, sub in engine.CATS:
        print('%s %-44s %4d' % (cat, nom, c[cat]))
    print('TOTAL', len(ps))
    print('pinchados respetados:', sum(1 for p in ps if p.codigo in PIN.values()), 'de', len(PIN))


# ================================================================= packs extra (bonus 9, 10, 11)
PACKS = {
 'EB': ('Escaleras, Barandas y Pasamanos', 120,
        [('ST', 'escalera', gr_escalera, 2), ('ST', 'baranda_galeria', gr_baranda, 2),
         ('ST', 'escalera_gato', gr_escalera_gato, 2)]),
 'PC': ('Portones, Cercos y Pérgolas', 150,
        [('FM', 'porton_campo', gr_porton_campo, 2), ('FM', 'porton_corredizo', gr_porton_corredizo, 2),
         ('FM', 'porton_dos_hojas', gr_porton_dos_hojas, 2), ('FM', 'puerta_peatonal', gr_puerta_peatonal, 2),
         ('FM', 'panel_corral', gr_panel_corral, 1), ('ST', 'pergola', gr_pergola, 2)]),
 'PT': ('El Pack de Estructuras para el Patio', 10,
        [('ST', 'cochera', gr_cochera, 1), ('ST', 'invernadero', gr_invernadero, 1),
         ('ST', 'pergola', gr_pergola, 1), ('ST', 'alero', gr_alero, 1),
         ('SH', 'mesa_pesada', gr_mesa_pesada, 1)]),
}

def generar_pack(prefijo, usados):
    """usados: set de (familia, args) que ya salieron en la biblioteca o en otro pack."""
    nombre, objetivo, fams = PACKS[prefijo]
    listas = []
    for cat, func, grilla, peso in fams:
        libres = [a for a in grilla() if (func, a) not in usados]
        listas.append((cat, func, libres, peso))
    elegidos = []
    idx = [0]*len(listas)
    while len(elegidos) < objetivo:
        avance = False
        for i, (cat, func, libres, peso) in enumerate(listas):
            for _ in range(peso):
                if idx[i] < len(libres) and len(elegidos) < objetivo:
                    elegidos.append((cat, func, libres[idx[i]])); idx[i] += 1; avance = True
        if not avance:
            raise RuntimeError('faltan combinaciones en el pack %s: %d de %d' % (prefijo, len(elegidos), objetivo))
    planos = []
    for i, (cat, func, args) in enumerate(elegidos, start=1):
        pl = getattr(MODS[cat], func)(*args)
        pl.codigo = '%s-%03d' % (prefijo, i)
        pl.familia = func; pl.args = args
        planos.append(pl)
        usados.add((func, args))
    planos.sort(key=lambda p: (p.familia, p.codigo))
    for i, p in enumerate(planos, start=1):
        p.codigo = '%s-%03d' % (prefijo, i)
    return nombre, planos
