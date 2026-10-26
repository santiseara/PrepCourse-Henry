# -*- coding: utf-8 -*-
"""Bonus que son planos: packs extra, los que dejan plata y el catálogo para clientes."""
import math
from engine import *
import paginas
from paginas import ML, MR, ANCHO, seccion
from doc import Doc

def _canvas(ruta, titulo):
    c = rl_canvas.Canvas(ruta, pagesize=(A4W, A4H))
    c.setTitle('Herrero de Finde · ' + titulo); c.setAuthor('Herrero de Finde')
    return c

# ----------------------------------------------------------------- packs de planos
def portada_pack(c, bonus, titulo, planos, bajada, items):
    c.setFillColor(TINTA); c.rect(0, 0, A4W, A4H, stroke=0, fill=1)
    c.setFillColor(NARANJA); c.rect(0, A4H-14, A4W, 14, stroke=0, fill=1)
    c.setFont('BC', 13); c.setFillColor(NARANJA)
    c.drawString(ML, A4H-62, 'HERRERO DE FINDE · BIBLIOTECA DE PLANOS')
    c.setFont('BCM', 9.5); c.setFillColor(HexColor('#9AA2AB'))
    c.drawString(ML, A4H-78, bonus.upper())
    c.setFont('MB', 30); c.setFillColor(PAPEL)
    y = A4H - 140
    for l in envolver(c, titulo.upper(), 'MB', 30, ANCHO):
        c.drawString(ML, y, l); y -= 36
    c.setFillColor(NARANJA); c.rect(ML, y+8, 120, 5, stroke=0, fill=1)
    c.setFont('BCM', 14); c.setFillColor(HexColor('#D7DBDF'))
    c.drawString(ML, y-18, '%d planos extra · %s' % (len(planos), bajada))
    muestra = max(planos[:40], key=lambda p: len(p.piezas))
    dibujar_iso(c, muestra.piezas, (ML-10, 230, ANCHO+20, 250), pad=10,
                base=HexColor('#B6BDC4'), contorno=False)
    c.setFont('BCM', 9); c.setFillColor(HexColor('#9AA2AB'))
    c.drawCentredString(A4W/2, 206, muestra.codigo + ' · ' + muestra.nombre)
    alto = 30 + len(items)*14
    c.setFillColor(HexColor('#22262B')); c.roundRect(ML, 96, ANCHO, alto, 4, stroke=0, fill=1)
    c.setFont('BC', 10); c.setFillColor(NARANJA)
    c.drawString(ML+16, 96+alto-22, 'QUÉ TRAE ESTE PACK')
    yy = 96 + alto - 40
    for t in items:
        c.setFillColor(NARANJA); c.circle(ML+22, yy+2.6, 2, stroke=0, fill=1)
        c.setFont('B', 8.4); c.setFillColor(PAPEL); c.drawString(ML+30, yy, t); yy -= 14
    c.setFillColor(NARANJA); c.rect(0, 0, A4W, 14, stroke=0, fill=1)

def indice_simple(c, planos, n, titulo, bonus, primera, total_pags):
    c.setFillColor(TINTA); c.rect(0, A4H-52, A4W, 52, stroke=0, fill=1)
    c.setFillColor(NARANJA); c.rect(0, A4H-55, A4W, 3, stroke=0, fill=1)
    c.setFont('BC', 9); c.setFillColor(NARANJA); c.drawString(ML, A4H-24, 'HERRERO DE FINDE')
    c.setFont('BCM', 7.4); c.setFillColor(HexColor('#9AA2AB')); c.drawString(ML, A4H-36, bonus.upper())
    c.setFont('BC', 15); c.setFillColor(PAPEL); c.drawRightString(A4W-MR, A4H-28, 'ÍNDICE')
    y = A4H - 84
    if primera:
        c.setFont('BC', 20); c.setFillColor(TINTA)
        c.drawString(ML, y, titulo.upper()); y -= 24
    c.setFont('BCM', 6.4); c.setFillColor(GRIS)
    c.drawString(ML+2, y, 'CÓDIGO'); c.drawString(ML+54, y, 'TRABAJO')
    c.drawString(ML+238, y, 'MEDIDA'); c.drawString(ML+322, y, 'HORAS')
    c.drawString(ML+356, y, 'NIVEL')
    c.drawRightString(ML+452, y, 'HIERRO'); c.drawRightString(ML+494, y, 'VENTA')
    c.drawRightString(A4W-MR, y, 'PÁG.')
    y -= 4; linea(c, ML, y, A4W-MR, GRIS_CL, 0.5); y -= 12
    for p in planos:
        c.setFont('BC', 8.2); c.setFillColor(NARANJA); c.drawString(ML+2, y, p.codigo)
        c.setFont('B', 8.2); c.setFillColor(TINTA)
        nom = p.nombre
        while c.stringWidth(nom, 'B', 8.2) > 178: nom = nom[:-2]
        c.drawString(ML+54, y, nom)
        W, D, H = p.medidas()
        c.setFont('B', 7.2); c.setFillColor(TINTA2)
        c.drawString(ML+238, y, '%d x %d x %d' % (W, D, H))
        c.drawString(ML+322, y, '%d-%d h' % p.horas)
        c.drawString(ML+356, y, p.nivel)
        c.setFont('BM', 7.4); c.setFillColor(TINTA2); c.drawRightString(ML+452, y, pesos(p.costo_material()))
        c.setFillColor(VERDE); c.drawRightString(ML+494, y, pesos(p.precio_venta()[0]))
        c.setFont('BM', 8); c.setFillColor(TINTA); c.drawRightString(A4W-MR, y, '%d' % p.pagina)
        linea(c, ML, y-3.4, A4W-MR, HexColor('#EDEFF1'), 0.4)
        y -= 13.2
    linea(c, ML, 58, A4W-MR, GRIS_CL, 0.5)
    c.setFont('BCM', 7); c.setFillColor(GRIS)
    c.drawString(ML, 47, 'Herrero de Finde · ' + bonus)
    c.drawCentredString(A4W/2, 47, titulo)
    c.drawRightString(A4W-MR, 47, 'pág. %d' % n)

def pack(ruta, bonus, titulo, bajada, planos, items):
    POR_PAG = 40
    pags_indice = int(math.ceil(len(planos)/float(POR_PAG)))
    pag = 1 + pags_indice + 1
    for p in planos:
        p.pagina = pag; pag += 4
    c = _canvas(ruta, titulo)
    portada_pack(c, bonus, titulo, planos, bajada, items); c.showPage()
    n = 2
    for i in range(pags_indice):
        indice_simple(c, planos[i*POR_PAG:(i+1)*POR_PAG], n, titulo, bonus, i == 0, pags_indice)
        c.showPage(); n += 1
    for p in planos:
        paginas.hojas(c, p); n += 4
    c.save()
    return n - 1

# ----------------------------------------------------------------- bonus 6
def los_que_dejan(ruta, planos):
    c = _canvas(ruta, 'Los que Dejan Plata')
    d = Doc(c, 'Los que Dejan Plata', 'Los 40 trabajos con el mejor margen de toda la biblioteca', 'Bonus 06')
    d.portada('No todos los trabajos se pagan igual. Estos son los que dejan la mayor diferencia entre lo que te '
              'cuesta el hierro y lo que se venden, ordenados.',
              ['Los 40 que más dejan, con el código del plano',
               'Los que más dejan por hora de taller',
               'El mejor de cada categoría',
               'Cómo elegir cuál fabricar este fin de semana'])
    datos = []
    for p in planos:
        bajo = p.precio_venta()[0]
        deja = bajo - p.costo_material()
        datos.append((deja, deja/float(p.horas[0]), p))

    def podar(lista, por_familia=2):
        vistos = {}
        out = []
        for t in lista:
            fam = getattr(t[2], 'familia', t[2].nombre)
            if vistos.get(fam, 0) >= por_familia: continue
            vistos[fam] = vistos.get(fam, 0) + 1
            out.append(t)
        return out

    d.h1('Los 40 que más dejan')
    d.p('Ordenados por la diferencia entre el precio sugerido y lo que te consume de hierro. Está acotado a dos '
        'medidas por tipo de trabajo, para que la lista te sirva: si una medida te deja bien, las otras del mismo '
        'trabajo también. La última columna es lo que te queda por cada hora de taller.')
    por_total = podar(sorted(datos, key=lambda t: -t[0]))[:40]
    d.tabla(['Código', 'Trabajo', 'Hierro', 'Se vende a', 'Te queda', 'Por hora'],
            [[p.codigo, p.nombre, pesos(p.costo_material()), pesos(p.precio_venta()[0]),
              pesos(deja), pesos(redondear(ph, 1000))] for deja, ph, p in por_total],
            [50, 158, 74, 80, 76, 72])
    d.h1('Los 20 que más dejan por hora')
    d.p('Un trabajo grande deja más plata, pero te ocupa el taller dos semanas y te obliga a poner una fortuna en '
        'material antes de cobrar. Estos son los que mejor pagan tu tiempo.')
    por_hora = podar(sorted(datos, key=lambda t: -t[1]))[:20]
    d.tabla(['Código', 'Trabajo', 'Horas', 'Hierro', 'Se vende a', 'Por hora'],
            [[p.codigo, p.nombre, '%d-%d h' % p.horas, pesos(p.costo_material()),
              pesos(p.precio_venta()[0]), pesos(redondear(ph, 1000))] for deja, ph, p in por_hora],
            [50, 158, 50, 76, 86, 90])
    d.h1('El mejor de cada categoría')
    filas = []
    for cat, nom, sub in CATS:
        dec = [t for t in datos if t[2].cat == cat]
        if not dec: continue
        mejor = max(dec, key=lambda t: t[1])
        filas.append([mejor[2].codigo, nom, mejor[2].nombre, pesos(redondear(mejor[1], 1000))])
    d.tabla(['Código', 'Categoría', 'El que mejor paga tu hora', 'Por hora'], filas, [52, 160, 200, 98])
    d.h1('Cómo elegir cuál fabricar')
    d.bullets([
        '**Si recién arrancás:** de la tabla por hora, el que puedas hacer con lo que ya tenés y esté marcado como '
        'Principiante. Terminar uno vale más que empezar tres.',
        '**Si tenés el taller parado:** el que se venda rápido en tu zona, aunque deje menos. La rueda la empieza una venta.',
        '**Si ya tenés clientes:** los de arriba de la primera tabla. Ahí es donde está la plata grande.',
        '**Si tenés poco lugar:** mirá la medida en el índice. Un porta autos necesita 7 metros libres.',
        '**Si vas a hacer varios iguales:** cualquiera de la tabla por hora mejora un 30 % cuando hacés el segundo, '
        'porque ya tenés la plantilla.',
    ])
    d.caja('Lo que no está en esta tabla',
           'El trabajo que te piden. Un portón que te encargaron y que se cobra la semana que viene siempre vale más '
           'que el mejor margen de la lista esperando comprador. Esta tabla es para cuando elegís vos.')
    d.cerrar(); c.save()

# ----------------------------------------------------------------- bonus 12
def catalogo(ruta, planos):
    """Una ficha por trabajo distinto (no por cada medida), para pasarle al cliente."""
    COLS, FILAS = 2, 2
    POR_PAG = COLS*FILAS
    vistos = set(); fichas = []
    for p in planos:
        if p.nombre in vistos: continue
        vistos.add(p.nombre); fichas.append(p)
    c = _canvas(ruta, 'El Catálogo para Clientes')
    # ---- portada
    c.setFillColor(TINTA); c.rect(0, 0, A4W, A4H, stroke=0, fill=1)
    c.setFillColor(NARANJA); c.rect(0, A4H-14, A4W, 14, stroke=0, fill=1)
    c.setFont('BC', 13); c.setFillColor(NARANJA); c.drawString(ML, A4H-62, 'HERRERO DE FINDE')
    c.setFont('BCM', 9.5); c.setFillColor(HexColor('#9AA2AB')); c.drawString(ML, A4H-78, 'BONUS 12')
    c.setFont('MB', 34); c.setFillColor(PAPEL)
    c.drawString(ML, A4H-150, 'EL CATÁLOGO')
    c.drawString(ML, A4H-192, 'PARA CLIENTES')
    c.setFillColor(NARANJA); c.rect(ML, A4H-214, 120, 5, stroke=0, fill=1)
    c.setFont('BCM', 14); c.setFillColor(HexColor('#D7DBDF'))
    c.drawString(ML, A4H-244, 'Pasáselo al cliente. Que señale lo que quiere.')
    c.setFont('B', 10); c.setFillColor(HexColor('#AEB6BE'))
    y = A4H - 268
    for l in envolver(c, '%d trabajos distintos de la biblioteca, con su imagen y su medida. Se terminó describir un '
                         'portón con las manos: el cliente mira, señala y vos abrís el plano.' % len(fichas),
                      'B', 10, ANCHO-40):
        c.drawString(ML, y, l); y -= 14
    muestra = [p for p in fichas if p.cat == 'BQ'][:1] or fichas[:1]
    dibujar_iso(c, muestra[0].piezas, (ML-10, 190, ANCHO+20, 230), pad=10,
                base=HexColor('#B6BDC4'), contorno=False)
    c.setFillColor(HexColor('#22262B')); c.roundRect(ML, 96, ANCHO, 76, 4, stroke=0, fill=1)
    c.setFont('BC', 10); c.setFillColor(NARANJA); c.drawString(ML+16, 150, 'CÓMO SE USA')
    for i, t in enumerate(['Abrilo en el celular y pasáselo al cliente mientras tomás el pedido.',
                           'Cuando señale uno, anotá el código: con ese código abrís el plano completo.',
                           'Los precios no están acá a propósito: los ponés vos con la Planilla de Cortes.']):
        c.setFillColor(NARANJA); c.circle(ML+22, 134-i*15+2.6, 2, stroke=0, fill=1)
        c.setFont('B', 8.4); c.setFillColor(PAPEL); c.drawString(ML+30, 134-i*15, t)
    c.setFillColor(NARANJA); c.rect(0, 0, A4W, 14, stroke=0, fill=1)
    c.showPage()

    n = 2
    cw = (ANCHO - 16) / float(COLS)
    ch = (A4H - 150) / float(FILAS)
    for i in range(0, len(fichas), POR_PAG):
        bloque = fichas[i:i+POR_PAG]
        c.setFillColor(TINTA); c.rect(0, A4H-44, A4W, 44, stroke=0, fill=1)
        c.setFillColor(NARANJA); c.rect(0, A4H-47, A4W, 3, stroke=0, fill=1)
        c.setFont('BC', 8.4); c.setFillColor(NARANJA); c.drawString(ML, A4H-22, 'HERRERO DE FINDE')
        c.setFont('BCM', 7); c.setFillColor(HexColor('#9AA2AB')); c.drawString(ML, A4H-33, 'CATÁLOGO PARA CLIENTES')
        c.setFont('BC', 11); c.setFillColor(PAPEL)
        c.drawRightString(A4W-MR, A4H-26, CAT_NOM[bloque[0].cat].upper()[:46])
        for j, p in enumerate(bloque):
            col, fil = j % COLS, j // COLS
            x = ML + col*(cw+16)
            yy = A4H - 66 - fil*ch
            c.setFillColor(CREMA); c.roundRect(x, yy-ch+14, cw, ch-14, 4, stroke=0, fill=1)
            dibujar_iso(c, p.piezas, (x+8, yy-ch+56, cw-16, ch-82), pad=6)
            c.setFont('BC', 10); c.setFillColor(NARANJA)
            c.drawString(x+14, yy-ch+38, p.codigo)
            c.setFont('BM', 11); c.setFillColor(TINTA)
            nom = p.nombre
            while c.stringWidth(nom, 'BM', 11) > cw-28 and len(nom) > 6: nom = nom[:-2]
            c.drawString(x+14, yy-ch+24, nom)
            W, D, H = p.medidas()
            c.setFont('B', 8); c.setFillColor(GRIS)
            c.drawString(x+14, yy-ch+12, '%d x %d x %d mm  ·  %s' % (W, D, H, p.variante.split(' · ')[-1] if ' · ' in p.variante else p.nivel))
        linea(c, ML, 52, A4W-MR, GRIS_CL, 0.5)
        c.setFont('BCM', 7); c.setFillColor(GRIS)
        c.drawString(ML, 42, 'Herrero de Finde · Catálogo para clientes')
        c.drawCentredString(A4W/2, 42, 'Señalá el trabajo y pedilo por su código')
        c.drawRightString(A4W-MR, 42, 'pág. %d' % n)
        c.showPage(); n += 1
    c.save()
    return n - 1
