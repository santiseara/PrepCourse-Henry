# -*- coding: utf-8 -*-
"""Arma el producto completo: la biblioteca, los packs extra y los 12 bonus."""
import os, sys, shutil, time
import engine
from engine import registrar_fuentes
import expansion, libro, bonus_texto, bonus_planos, planilla

ARCHIVOS_BONUS = {
 '02': 'BONUS 02 - Cobralo Bien.pdf',
 '03': 'BONUS 03 - El Checklist Cero Errores.pdf',
 '04': 'BONUS 04 - Terminacion de Taller.pdf',
 '05': 'BONUS 05 - El Taller de 500 mil.pdf',
 '06': 'BONUS 06 - Los que Dejan Plata.pdf',
 '07': 'BONUS 07 - Vende lo que Fabricas.pdf',
 '08': 'BONUS 08 - Solda como un Pro.pdf',
}

def main(destino):
    registrar_fuentes()
    t0 = time.time()
    if not os.path.isdir(destino): os.makedirs(destino)
    salidas = []

    planos = expansion.generar()
    info = libro.paginar_categoria(planos)
    for cat, nom, sub in engine.CATS:
        ruta = os.path.join(destino, libro.NOMBRES_ARCHIVO[cat] + ' (%d planos).pdf' % len(info[cat][2]))
        total = libro.construir_categoria(cat, info, ruta)
        salidas.append((ruta, total))
    guia = os.path.join(destino, '00 - Guia de la biblioteca (empeza por aca).pdf')
    salidas.insert(0, (guia, libro.construir_guia(planos, guia)))
    print('biblioteca lista · %.0f s' % (time.time()-t0))

    # --- bonus 1: la planilla
    ruta = os.path.join(destino, 'BONUS 01 - La Planilla de Cortes.xlsx')
    planilla.construir(ruta); salidas.append((ruta, 0))

    # --- bonus escritos
    for clave, func in (('02', bonus_texto.cobralo_bien), ('03', bonus_texto.checklist),
                        ('04', bonus_texto.terminacion), ('05', bonus_texto.taller),
                        ('07', bonus_texto.vende), ('08', bonus_texto.soldar)):
        ruta = os.path.join(destino, ARCHIVOS_BONUS[clave])
        func(ruta, planos); salidas.append((ruta, 0))
    ruta = os.path.join(destino, ARCHIVOS_BONUS['06'])
    bonus_planos.los_que_dejan(ruta, planos); salidas.append((ruta, 0))
    print('bonus escritos listos · %.0f s' % (time.time()-t0))

    # --- bonus 9, 10, 11: packs de planos extra
    usados = set((p.familia, p.args) for p in planos)
    packs = [
      ('EB', 'Bonus 09', 'BONUS 09 - Escaleras, Barandas y Pasamanos (120 planos).pdf',
       'escaleras rectas, barandas y escaleras de gato',
       ['120 planos que no están en la biblioteca principal',
        'Escaleras rectas con alzada y pedada calculadas',
        'Barandas con barrotes cada 110 mm, como piden las normas',
        'Escaleras de gato para techos y tanques']),
      ('PC', 'Bonus 10', 'BONUS 10 - Portones, Cercos y Pergolas (150 planos).pdf',
       'portones, puertas peatonales, paneles de cerco y pérgolas',
       ['150 planos que no están en la biblioteca principal',
        'Portones de una y dos hojas, corredizos y de campo',
        'Puertas peatonales con chapa abajo y barrotes arriba',
        'Paneles de cerco y pérgolas de patio']),
      ('PT', 'Bonus 11', 'BONUS 11 - El Pack de Estructuras para el Patio (10 estructuras).pdf',
       'cocheras, invernaderos, aleros y pérgolas grandes',
       ['Diez estructuras completas para el patio y el fondo',
        'Cada una con su pedido de hierro y su precio sugerido',
        'Las mismas cuatro hojas que el resto de la biblioteca']),
    ]
    todos_extra = []
    for pref, bonus, arch, bajada, items in packs:
        nom, lote = expansion.generar_pack(pref, usados)
        ruta = os.path.join(destino, arch)
        total = bonus_planos.pack(ruta, bonus, nom, bajada, lote, items)
        salidas.append((ruta, total)); todos_extra.extend(lote)
        print('%s listo · %.0f s' % (pref, time.time()-t0))

    # --- bonus 12: catalogo
    ruta = os.path.join(destino, 'BONUS 12 - El Catalogo para Clientes.pdf')
    total = bonus_planos.catalogo(ruta, planos)
    salidas.append((ruta, total))
    print('catalogo listo · %.0f s' % (time.time()-t0))
    return planos, todos_extra, salidas

if __name__ == '__main__':
    destino = sys.argv[1] if len(sys.argv) > 1 else '.'
    planos, extra, salidas = main(destino)
    print()
    tot = 0; mb = 0
    for ruta, pags in sorted(salidas):
        t = os.path.getsize(ruta)/1048576.0
        mb += t; tot += pags
        print('%-70s %5s  %6.1f MB' % (os.path.basename(ruta), (str(pags)+' pág') if pags else '', t))
    print()
    print('%d planos en la biblioteca + %d en los packs extra = %d planos' % (len(planos), len(extra), len(planos)+len(extra)))
    print('%d páginas · %.0f MB en total' % (tot, mb))
