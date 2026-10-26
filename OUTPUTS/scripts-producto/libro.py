# -*- coding: utf-8 -*-
"""Arma el PDF completo de la biblioteca."""
import sys, os
from engine import *
import paginas
from paginas import ML, MR, ANCHO, seccion, encabezado, pie
import cat_tr, cat_bq, cat_gy, cat_fm, cat_sh, cat_tk, cat_fn, cat_st

MODULOS = {'TR': cat_tr, 'BQ': cat_bq, 'GY': cat_gy, 'FM': cat_fm,
           'SH': cat_sh, 'TK': cat_tk, 'FN': cat_fn, 'ST': cat_st}

def recolectar():
    todos = []
    for cat, nom, sub in CATS:
        items = sorted(MODULOS[cat].P, key=lambda cp: cp[0])
        for cod, pl in items:
            pl.codigo = cod
            todos.append(pl)
    return todos

# ============================================================= piezas de hoja
def pie_simple(c, n, texto=''):
    linea(c, ML, 58, A4W-MR, GRIS_CL, 0.5)
    c.setFont('BCM', 7); c.setFillColor(GRIS)
    c.drawString(ML, 47, 'Herrero de Finde · Biblioteca de planos')
    c.drawCentredString(A4W/2, 47, texto)
    c.drawRightString(A4W-MR, 47, 'pág. %d' % n)

def cabecera_simple(c, titulo, bajada=''):
    c.setFillColor(TINTA); c.rect(0, A4H-52, A4W, 52, stroke=0, fill=1)
    c.setFillColor(NARANJA); c.rect(0, A4H-55, A4W, 3, stroke=0, fill=1)
    c.setFont('BC', 9); c.setFillColor(NARANJA)
    c.drawString(ML, A4H-24, 'HERRERO DE FINDE')
    c.setFont('BCM', 7.4); c.setFillColor(HexColor('#9AA2AB'))
    c.drawString(ML, A4H-36, 'BIBLIOTECA DE PLANOS · VOLUMEN 1')
    c.setFont('BC', 15); c.setFillColor(PAPEL)
    c.drawRightString(A4W-MR, A4H-28, titulo.upper())
    if bajada:
        c.setFont('BCM', 7.4); c.setFillColor(HexColor('#9AA2AB'))
        c.drawRightString(A4W-MR, A4H-40, bajada.upper())

# ------------------------------------------------------------------ portada
def portada(c, planos, n):
    c.setFillColor(TINTA); c.rect(0, 0, A4W, A4H, stroke=0, fill=1)
    c.setFillColor(NARANJA); c.rect(0, A4H-14, A4W, 14, stroke=0, fill=1)
    c.setFont('BC', 13); c.setFillColor(NARANJA)
    c.drawString(ML, A4H-62, 'HERRERO DE FINDE')
    c.setFont('BCM', 9.5); c.setFillColor(HexColor('#9AA2AB'))
    c.drawString(ML, A4H-78, 'PARA EL QUE TIENE UNA SOLDADORA Y UN SÁBADO LIBRE')

    c.setFont('MB', 46); c.setFillColor(PAPEL)
    c.drawString(ML, A4H-150, 'BIBLIOTECA')
    c.drawString(ML, A4H-200, 'DE PLANOS')
    c.setFillColor(NARANJA); c.rect(ML, A4H-222, 120, 5, stroke=0, fill=1)

    c.setFont('BCM', 15); c.setFillColor(HexColor('#D7DBDF'))
    c.drawString(ML, A4H-252, 'Volumen 1 · %d planos completos, listos para fabricar' % len(planos))
    c.setFont('BCM', 11); c.setFillColor(HexColor('#9AA2AB'))
    c.drawString(ML, A4H-272, 'Cada uno con sus tres vistas, su lista de cortes, su orden de soldadura')
    c.drawString(ML, A4H-287, 'y un precio de venta sugerido. En milímetros y en pulgadas.')

    piezas = []
    for cod in ('BQ-090', 'TR-018'):
        for pl in planos:
            if pl.codigo == cod: piezas = pl.piezas
        if piezas: break
    dibujar_iso(c, piezas, (ML-10, 250, ANCHO+20, 250), pad=10, base=HexColor('#AEB6BE'), lw=0.25)

    y = 150
    c.setFillColor(HexColor('#22262B')); c.roundRect(ML, y-10, ANCHO, 96, 4, stroke=0, fill=1)
    cuenta = {}
    for pl in planos: cuenta[pl.cat] = cuenta.get(pl.cat, 0) + 1
    xs = [ML+16, ML+16+ANCHO/2.0]
    for i, (cat, nom, sub) in enumerate(CATS):
        x = xs[i % 2]; yy = y + 66 - (i//2)*21
        c.setFont('BC', 9); c.setFillColor(NARANJA)
        c.drawString(x, yy, cat)
        c.setFont('BCM', 9); c.setFillColor(HexColor('#D7DBDF'))
        c.drawString(x+24, yy, nom[:44])
        c.setFont('BC', 9); c.setFillColor(PAPEL)
        c.drawRightString(x + ANCHO/2.0 - 24, yy, '%d' % cuenta.get(cat, 0))
    c.setFont('BCM', 8.6); c.setFillColor(HexColor('#9AA2AB'))
    c.drawCentredString(A4W/2, 96, 'Medidas en milímetros y pulgadas  ·  listas de cortes sumadas en barras de 6 m  ·  precios de referencia de octubre de 2026')
    c.setFillColor(NARANJA); c.rect(0, 0, A4W, 14, stroke=0, fill=1)

# ------------------------------------------------------------------ arranque
def bienvenida(c, planos, n):
    cabecera_simple(c, 'Lo que tenés acá')
    y = A4H - 88
    c.setFont('BC', 24); c.setFillColor(TINTA)
    c.drawString(ML, y, 'NO TE FALTA MANO. TE FALTAN NÚMEROS.')
    y -= 26
    txt = ('Soldar nunca fue lo difícil. Lo difícil era la hoja: qué cortar, cuánto hierro comprar, en qué orden '
           'soldarlo para que no se descuadre y cuánto cobrar cuando alguien te pregunta. Esta biblioteca es eso, '
           '%d veces.' % len(planos))
    y = parrafo(c, txt, ML, y, ANCHO, 'B', 10.5, 14) - 24

    bloques = [
      ('CADA PLANO SON CUATRO HOJAS',
       'La primera te muestra el trabajo terminado, lo que tenés que pedir en la casa de hierros y a cuánto se vende. '
       'La segunda trae las tres vistas con todas las medidas. La tercera, la lista de cortes pieza por pieza y cómo '
       'sale de las barras de 6 m. La cuarta, el orden de soldadura, paso por paso y con dibujo.'),
      ('MILÍMETROS Y PULGADAS, SIEMPRE',
       'Cada medida está en las dos unidades, una al lado de la otra. Los caños van en la medida comercial con la que '
       'los vende la casa de hierros, no en una medida que después no existe.'),
      ('LOS PRECIOS SON DE REFERENCIA',
       'Los valores de hierro son de octubre de 2026 y los de venta salen de una fórmula que está explicada en la '
       'página 7: material, insumos, tus horas y margen. Si en tu zona el hierro está más caro, cambiás el valor de '
       'la barra y todo lo demás se acomoda.'),
      ('ESTO NO ES UNA PROMESA DE INGRESOS',
       'Lo que ganes depende de lo que fabriques y de lo que cobres. Los planos, las listas de cortes y los precios '
       'sugeridos son la parte que te damos nosotros. La soldadora la ponés vos.'),
    ]
    for tit, txt in bloques:
        c.setFillColor(NARANJA); c.rect(ML, y-2, 3, 11, stroke=0, fill=1)
        c.setFont('BC', 10.5); c.setFillColor(TINTA)
        c.drawString(ML+10, y, tit)
        y = parrafo(c, txt, ML+10, y-15, ANCHO-10, 'B', 8.8, 11.8) - 22

    c.setFillColor(CREMA); c.roundRect(ML, 120, ANCHO, 118, 4, stroke=0, fill=1)
    c.setFont('BC', 11); c.setFillColor(TINTA)
    c.drawString(ML+16, 214, 'LO QUE PODÉS HACER CON ESTOS PLANOS')
    perm = [('SÍ', 'Fabricar todo lo que quieras, para vos o para vender.', VERDE),
            ('SÍ', 'Imprimirlos las veces que necesites y llevarlos al taller.', VERDE),
            ('SÍ', 'Cobrar por los trabajos que fabriques con ellos, sin pagarnos nada más.', VERDE),
            ('NO', 'Revender, regalar ni compartir los archivos.', HexColor('#C0392B')),
            ('NO', 'Publicarlos en grupos, nubes o páginas de descarga.', HexColor('#C0392B'))]
    yy = 194
    for et, t, col in perm:
        c.setFillColor(col); c.roundRect(ML+16, yy-2, 20, 11, 2, stroke=0, fill=1)
        c.setFont('BC', 7); c.setFillColor(PAPEL); c.drawCentredString(ML+26, yy+1, et)
        c.setFont('B', 8.6); c.setFillColor(TINTA2); c.drawString(ML+44, yy, t)
        yy -= 15
    pie_simple(c, n, 'Herrero de Finde · Volumen 1')

# ------------------------------------------------------------------ cómo leer un plano
def como_leer(c, n):
    cabecera_simple(c, 'Cómo se lee un plano', 'las cuatro hojas')
    y = A4H - 88
    c.setFont('BC', 22); c.setFillColor(TINTA)
    c.drawString(ML, y, 'LAS CUATRO HOJAS DE CADA PLANO')
    y -= 20
    y = parrafo(c, 'Todos los planos de la biblioteca están armados igual. Si entendés estas cuatro hojas una vez, '
                   'entendiste los %s.' % 'ciento quince', ML, y, ANCHO, 'B', 9.5, 13) - 20

    hojas = [
      ('1', 'EL TRABAJO', ['Vista 3D de cómo termina', 'Tiempo, nivel y hierro que lleva',
                           'Lo que pedís en la casa de hierros, barra por barra',
                           'A cuánto se vende y cómo sale ese precio']),
      ('2', 'EL DIBUJO', ['Frente, lateral y planta, a la misma escala',
                          'Cada medida en mm y en pulgadas',
                          'Un detalle ampliado de la unión clave',
                          'Lo punteado es una pieza que tapa a las de abajo']),
      ('3', 'LA LISTA DE CORTES', ['Cada pieza con su letra, su largo y su corte',
                                   'Cómo sale de las barras de 6 m, con el sobrante',
                                   'Dónde va cada letra, marcado sobre el dibujo',
                                   'El control antes del primer corte']),
      ('4', 'EL ARMADO', ['El orden de soldadura, paso por paso',
                          'En naranja, lo que sumás en cada paso',
                          'Los dos errores que arruinan ese trabajo',
                          'Terminación, pintura y cuánto cobrarlo']),
    ]
    w = (ANCHO - 3*10)/4.0
    top = y
    for i, (num, tit, items) in enumerate(hojas):
        x = ML + i*(w+10)
        c.setFillColor(CREMA); c.roundRect(x, top-250, w, 250, 3, stroke=0, fill=1)
        c.setFillColor(TINTA); c.rect(x, top-28, w, 28, stroke=0, fill=1)
        c.setFont('BC', 15); c.setFillColor(NARANJA); c.drawString(x+8, top-20, num)
        c.setFont('BC', 9.5); c.setFillColor(PAPEL); c.drawString(x+26, top-19, tit)
        # mini maqueta de la hoja
        mx, my, mw, mh = x+14, top-152, w-28, 108
        c.setFillColor(PAPEL); c.setStrokeColor(GRIS_CL); c.setLineWidth(0.6)
        c.rect(mx, my, mw, mh, stroke=1, fill=1)
        c.setFillColor(TINTA); c.rect(mx, my+mh-10, mw, 10, stroke=0, fill=1)
        c.setFillColor(GRIS_CL)
        if num == '1':
            c.rect(mx+6, my+mh-56, mw-12, 40, stroke=0, fill=1)
            for k in range(4): c.rect(mx+6+k*(mw-12)/4.0, my+mh-70, (mw-12)/4.0-3, 10, stroke=0, fill=1)
            for k in range(5): c.rect(mx+6, my+mh-84-k*7, mw-12, 4, stroke=0, fill=1)
        elif num == '2':
            c.rect(mx+6, my+mh-62, (mw-18)*0.6, 46, stroke=0, fill=1)
            c.rect(mx+12+(mw-18)*0.6, my+mh-62, (mw-18)*0.4, 46, stroke=0, fill=1)
            c.rect(mx+6, my+8, (mw-18)*0.6, 44, stroke=0, fill=1)
            c.rect(mx+12+(mw-18)*0.6, my+8, (mw-18)*0.4, 44, stroke=0, fill=1)
        elif num == '3':
            for k in range(7): c.rect(mx+6, my+mh-24-k*7, mw-12, 4, stroke=0, fill=1)
            for k in range(3): c.rect(mx+6, my+10+k*12, mw-12, 8, stroke=0, fill=1)
        else:
            for k in range(6):
                c.rect(mx+6+(k % 3)*(mw-12)/3.0, my+mh-62-(k//3)*44, (mw-12)/3.0-4, 36, stroke=0, fill=1)
        yy = my - 14
        for it in items:
            c.setFillColor(NARANJA); c.circle(x+16, yy+2.6, 1.8, stroke=0, fill=1)
            c.setFont('B', 7.4); c.setFillColor(TINTA2)
            for l in envolver(c, it, 'B', 7.4, w-30):
                c.drawString(x+22, yy, l); yy -= 9.2
            yy -= 3
    y = top - 272
    c.setFillColor(TINTA); c.roundRect(ML, y-96, ANCHO, 92, 4, stroke=0, fill=1)
    c.setFont('BC', 12); c.setFillColor(NARANJA)
    c.drawString(ML+16, y-24, 'TRES COSAS QUE VALEN PARA TODOS LOS PLANOS')
    tips = ['Las medidas mandan sobre el dibujo. Los dibujos están a escala, pero nunca midas con la regla sobre el papel.',
            'La tolerancia de taller es ± 2 mm. Si una pieza te da 3 mm de diferencia, cortala de nuevo: se acumula.',
            'Antes de soldar a fondo, presentá todo en seco y medí las dos diagonales. Es el único control que importa.']
    yy = y - 42
    for t in tips:
        c.setFillColor(NARANJA); c.circle(ML+20, yy+2.6, 2, stroke=0, fill=1)
        c.setFont('B', 8.4); c.setFillColor(PAPEL); c.drawString(ML+28, yy, t)
        yy -= 15
    y -= 118
    y = seccion(c, ML, y, 'Las palabras que vas a leer en las hojas')
    glos = [('Puntear', 'dar un punto corto de soldadura que sujeta sin fijar del todo'),
            ('Presentar', 'apoyar las piezas en posición, sin soldar, para ver cómo cierra'),
            ('Escuadrar', 'dejar a 90 grados; se controla midiendo las dos diagonales'),
            ('Zanca', 'el perfil inclinado de una escalera, donde apoyan los escalones'),
            ('Cabio', 'la viga inclinada de un techo; va de la columna alta a la baja'),
            ('Correa', 'el perfil horizontal que cruza los cabios y sostiene la chapa'),
            ('Contrahuella', 'la parte vertical del escalón; la huella es la que pisás'),
            ('Bocado', 'el corte curvo en la punta de un caño para que abrace a otro caño'),
            ('Descuadrar', 'perder los 90 grados por el calor de la soldadura'),
            ('Alabear', 'torcerse fuera de plano: la pieza deja de apoyar en los cuatro puntos')]
    col = (ANCHO - 18)/2.0
    yy = y
    for i, (t, d) in enumerate(glos):
        x = ML + (i % 2)*(col+18)
        if i % 2 == 0 and i: yy -= 14
        c.setFont('BC', 8.4); c.setFillColor(NARANJA); c.drawString(x, yy, t.upper())
        c.setFont('B', 8.2); c.setFillColor(TINTA2); c.drawString(x+78, yy, d)
    pie_simple(c, n, 'Cómo se lee un plano')

# ------------------------------------------------------------------ la casa de hierros
def casa_hierros(c, n):
    cabecera_simple(c, 'La casa de hierros', 'perfiles, medidas y precios de referencia')
    y = A4H - 88
    c.setFont('BC', 22); c.setFillColor(TINTA)
    c.drawString(ML, y, 'TODO LO QUE PEDÍS, EN UNA TABLA')
    y -= 18
    y = parrafo(c, 'Estos son los perfiles que usan los planos de la biblioteca, con la medida comercial con la que se '
                   'piden, el peso por metro y el precio de referencia de la barra de 6 metros en octubre de 2026. '
                   'Si en tu zona el hierro está más caro, calculá el factor una vez y aplicalo a todos los planos.',
                ML, y, ANCHO, 'B', 8.8, 11.6) - 18

    grupos = [('Caños estructurales cuadrados', 'tubo', lambda k: M[k]['w'] == M[k]['h']),
              ('Caños estructurales rectangulares', 'tubo', lambda k: M[k]['w'] != M[k]['h']),
              ('Ángulos y planchuelas', None, lambda k: M[k]['fam'] in ('angulo', 'planchuela')),
              ('Redondos y caños redondos', None, lambda k: M[k]['fam'] == 'redondo'),
              ('Perfiles', None, lambda k: M[k]['fam'] == 'perfil'),
              ('Chapas y planos (precio por m²)', None, lambda k: M[k]['fam'] == 'chapa')]
    for titulo, fam, filtro in grupos:
        claves = [k for k in M if (fam is None or M[k]['fam'] == fam) and filtro(k)]
        if fam is not None:
            claves = [k for k in claves if M[k]['fam'] == fam]
        claves.sort(key=lambda k: M[k]['precio'])
        if y < 150:
            pie_simple(c, n, 'La casa de hierros'); c.showPage()
            n += 1; cabecera_simple(c, 'La casa de hierros', 'continuación'); y = A4H - 88
        c.setFont('BC', 9.5); c.setFillColor(NARANJA); c.drawString(ML, y, titulo.upper())
        y -= 4; linea(c, ML, y, A4W-MR, GRIS_CL, 0.5); y -= 12
        c.setFont('BCM', 6.6); c.setFillColor(GRIS)
        c.drawString(ML, y, 'PERFIL'); c.drawString(ML+260, y, 'CÓMO SE PIDE')
        c.drawString(ML+370, y, 'PESO'); c.drawRightString(A4W-MR, y, 'BARRA DE 6 M')
        y -= 12
        for k in claves:
            d = M[k]
            c.setFont('B', 8); c.setFillColor(TINTA); c.drawString(ML, y, d['nom'])
            c.setFont('BM', 8); c.setFillColor(TINTA2); c.drawString(ML+260, y, d['corto'])
            if d.get('por') == 'm2':
                c.setFont('B', 8); c.setFillColor(GRIS); c.drawString(ML+370, y, '%s mm de espesor' % ('%.2f' % d['t']).replace('.', ',').rstrip('0').rstrip(','))
                c.setFont('BM', 8); c.setFillColor(TINTA); c.drawRightString(A4W-MR, y, pesos(d['precio']) + ' el m²')
            else:
                c.setFont('B', 8); c.setFillColor(GRIS); c.drawString(ML+370, y, ('%.2f kg/m' % d['kgm']).replace('.', ','))
                c.setFont('BM', 8); c.setFillColor(TINTA); c.drawRightString(A4W-MR, y, pesos(d['precio']))
            y -= 11.5
        y -= 10
    if y > 170:
        c.setFillColor(CREMA); c.roundRect(ML, y-140, ANCHO, 140, 4, stroke=0, fill=1)
        c.setFont('BC', 11); c.setFillColor(TINTA); c.drawString(ML+16, y-24, 'CÓMO PEDIR PARA QUE NO TE SOBRE MEDIA BARRA')
        tips = ['Llevá la hoja 3 impresa. La lista de cortes ya está sumada en barras de 6 m: pedís barras, no metros.',
                'Preguntá si te cortan en la casa de hierros. Muchas cortan gratis hasta cierta cantidad y te ahorrás el flete de 6 m.',
                'Confirmá el espesor. "Caño de 50" puede ser de 1,6 o de 2 mm, y la diferencia de precio y de resistencia es enorme.',
                'La chapa se vende en hojas de 1 x 2 m o 1,22 x 2,44 m. Si tu pieza es más grande, cambiá el plano, no la chapa.',
                'Pedí el recorte. El sobrante de tus barras es tuyo: es material que ya pagaste y que te sirve para el próximo trabajo.',
                'Guardá el remito. Es lo que te permite rehacer el presupuesto cuando el hierro se mueve.']
        yy = y - 44
        for t in tips:
            c.setFillColor(NARANJA); c.circle(ML+20, yy+2.6, 2, stroke=0, fill=1)
            c.setFont('B', 8.2); c.setFillColor(TINTA2)
            c.drawString(ML+28, yy, t); yy -= 15
    pie_simple(c, n, 'La casa de hierros')
    return n

# ------------------------------------------------------------------ cómo cobrar
def como_cobrar(c, n):
    cabecera_simple(c, 'Cuánto cobrar', 'la fórmula que usa cada plano')
    y = A4H - 88
    c.setFont('BC', 22); c.setFillColor(TINTA)
    c.drawString(ML, y, 'DE DÓNDE SALE EL PRECIO SUGERIDO')
    y -= 18
    y = parrafo(c, 'Cada plano trae un precio de venta sugerido. No es un número inventado: sale de esta fórmula, '
                   'con los números de ese plano. Si cambiás el valor de tu hora, cambia todo lo demás.',
                ML, y, ANCHO, 'B', 9.2, 12.4) - 24

    c.setFillColor(CREMA); c.roundRect(ML, y-118, ANCHO, 118, 4, stroke=0, fill=1)
    c.setFillColor(VERDE); c.rect(ML, y-118, 3.5, 118, stroke=0, fill=1)
    filas = [('Hierro que lleva el trabajo', 'los metros que consume, no la barra entera'),
             ('+ Insumos: 12 % del hierro', 'discos, gas o alambre, electrodos, antióxido y pintura'),
             ('+ Tus horas × el valor de tu hora', 'en esta biblioteca, %s por hora' % pesos(VALOR_HORA)),
             ('= PRECIO SUGERIDO (piso)', 'por debajo de esto estás trabajando gratis'),
             ('× 1,30 = techo del rango', 'lo que podés cobrar con terminación prolija y entrega rápida')]
    yy = y - 24
    for i, (a, b) in enumerate(filas):
        c.setFont('BC' if i >= 3 else 'BM', 10.5 if i >= 3 else 9.5)
        c.setFillColor(VERDE if i >= 3 else TINTA)
        c.drawString(ML+16, yy, a)
        c.setFont('B', 8); c.setFillColor(GRIS); c.drawString(ML+280, yy, b)
        yy -= 21
    y -= 136

    y = seccion(c, ML, y, 'Lo que no entra en esa cuenta y tenés que sumar aparte')
    extras = [('El traslado', 'Si lo entregás, cobralo. Un portón de 3,60 m no entra en un auto.'),
              ('La instalación', 'Amurar, nivelar y cargar no es parte del precio de taller. Es otro trabajo.'),
              ('El apuro', 'Si lo quiere para el viernes y tenías el sábado ocupado, eso se cobra.'),
              ('Los viajes a medir', 'Dos visitas son dos horas de tu día más la nafta.'),
              ('El diseño a medida', 'Si te pide algo distinto del plano, el cambio se cotiza aparte.'),
              ('La pintura especial', 'Epoxi, galvanizado en frío o color a elección no es el mismo precio que el negro.')]
    for a, b in extras:
        c.setFillColor(NARANJA); c.circle(ML+3, y+2.6, 2.2, stroke=0, fill=1)
        c.setFont('BC', 8.8); c.setFillColor(TINTA); c.drawString(ML+11, y, a.upper())
        c.setFont('B', 8.4); c.setFillColor(TINTA2); c.drawString(ML+120, y, b)
        y -= 15
    y -= 10

    c.setFillColor(TINTA); c.roundRect(ML, y-120, ANCHO, 118, 4, stroke=0, fill=1)
    c.setFont('BC', 12); c.setFillColor(NARANJA)
    c.drawString(ML+16, y-24, 'TRES REGLAS PARA NO REGALAR TU TRABAJO')
    reglas = ['Cobrá el 50 % de adelanto para comprar el material. Nunca pongas plata tuya en el hierro de otro.',
              'Si te regatean, no bajes el precio: sacá algo. Menos horas, menos terminación, menos trabajo.',
              'Si te sale más rápido de lo que calculaste, ganaste vos. Esa es la razón de cobrar por trabajo y no por hora.',
              'Nunca des un precio en el momento, de memoria. "Te lo paso esta noche por WhatsApp" es una frase que vale plata.']
    yy = y - 44
    for t in reglas:
        c.setFillColor(NARANJA); c.circle(ML+20, yy+2.6, 2, stroke=0, fill=1)
        c.setFont('B', 8.4); c.setFillColor(PAPEL); c.drawString(ML+28, yy, t); yy -= 16
    pie_simple(c, n, 'Cuánto cobrar')

# ------------------------------------------------------------------ antes de cortar
def antes_de_cortar(c, n):
    cabecera_simple(c, 'Antes del primer corte', 'el control que ahorra el sábado')
    y = A4H - 88
    c.setFont('BC', 22); c.setFillColor(TINTA)
    c.drawString(ML, y, 'LO QUE SE HACE ANTES DE PRENDER LA MÁQUINA')
    y -= 24
    col = (ANCHO - 18)/2.0
    izq = [('MEDIR Y MARCAR', [
              'Medí la barra entera: muchas vienen 5,95 m y no 6 m.',
              'Marcá con punta de metal o rayador, nunca con fibra gruesa: la fibra se corre 2 mm.',
              'Marcá siempre desde la misma punta de la pieza. Si vas encadenando medidas, el error se suma.',
              'Escribí la letra de la lista de cortes en cada pieza apenas la cortás.']),
            ('CORTAR', [
              'Cortá de mayor a menor. Lo que sobra de una barra larga todavía sirve; lo que sobra de un recorte, no.',
              'Dejá 3 mm por corte de disco. En una barra con seis cortes son casi 2 cm.',
              'Desbastá la rebaba de cada corte antes de presentar: con rebaba nada apoya derecho.',
              'En los cortes a 45, hacé el primero y usalo de plantilla para todos los demás.'])]
    der = [('PRESENTAR Y PUNTEAR', [
              'Presentá todo en seco y mirá el conjunto antes de dar el primer punto.',
              'Puntos de 15 a 20 mm, nunca cordón corrido en el armado.',
              'Medí las dos diagonales: si no dan iguales, está fuera de escuadra y hay que corregir ahora.',
              'Soldá alternando lados y puntas. Soldar todo seguido de un lado tuerce la pieza con el calor.']),
            ('SEGURIDAD, EN SERIO', [
              'Máscara fotosensible y guantes. El golpe de arco se siente ocho horas después, cuando ya no podés dormir.',
              'Protección ocular también para amolar: el disco salta y el esquirlazo no avisa.',
              'Nunca sueldes sobre tambores, bidones o caños cerrados sin ventilar: explotan.',
              'Ventilación y matafuego a mano. Las chispas vuelan 10 metros y el trapo con nafta está siempre cerca.'])]
    for xo, bloques in ((ML, izq), (ML+col+18, der)):
        yy = y
        for tit, items in bloques:
            c.setFillColor(TINTA); c.rect(xo, yy-2, col, 18, stroke=0, fill=1)
            c.setFont('BC', 9.5); c.setFillColor(NARANJA); c.drawString(xo+8, yy+4, tit)
            yy -= 24
            for it in items:
                c.setStrokeColor(GRIS); c.setLineWidth(0.6)
                c.rect(xo+2, yy-1.5, 7, 7, stroke=1, fill=0)
                c.setFont('B', 8.4); c.setFillColor(TINTA2)
                for l in envolver(c, it, 'B', 8.4, col-18):
                    c.drawString(xo+15, yy, l); yy -= 10.6
                yy -= 5
            yy -= 12
    c.setFillColor(CREMA); c.roundRect(ML, 110, ANCHO, 86, 4, stroke=0, fill=1)
    c.setFont('BC', 11); c.setFillColor(TINTA)
    c.drawString(ML+16, 174, 'LA REGLA QUE MÁS PLATA TE VA A AHORRAR')
    parrafo(c, 'Medí dos veces y cortá una. Suena a cartel de taller, pero el 80 % del hierro que termina en el tacho '
               'de recortes se fue por una medida que alguien dio por sabida. Antes de cada corte, mirá la hoja 3. '
               'La hoja ya hizo la cuenta por vos.',
            ML+16, 156, ANCHO-32, 'B', 9, 12.6)
    pie_simple(c, n, 'Antes del primer corte')

# ------------------------------------------------------------------ índice
def filas_indice(planos):
    filas = []
    for cat, nom, sub in CATS:
        items = [p for p in planos if p.cat == cat]
        filas.append(('cat', cat, nom, len(items)))
        for p in items:
            filas.append(('pl', p))
    return filas

def paginar_indice(filas, alto_cat=30.0, alto_pl=13.2, alto_util=600.0):
    paginas_, actual, h = [], [], 0.0
    for f in filas:
        hh = alto_cat if f[0] == 'cat' else alto_pl
        if h + hh > alto_util and actual:
            paginas_.append(actual); actual = []; h = 0.0
        actual.append(f); h += hh
    if actual: paginas_.append(actual)
    return paginas_

def hoja_indice(c, bloque, n, primera):
    cabecera_simple(c, 'Índice', 'los %d planos' % 115)
    y = A4H - 84
    if primera:
        c.setFont('BC', 22); c.setFillColor(TINTA)
        c.drawString(ML, y, 'TODOS LOS PLANOS, POR CATEGORÍA')
        y -= 22
    for f in bloque:
        if f[0] == 'cat':
            y -= 10
            c.setFillColor(TINTA); c.rect(ML, y-4, ANCHO, 17, stroke=0, fill=1)
            c.setFont('BC', 9.5); c.setFillColor(NARANJA); c.drawString(ML+8, y+1, f[1])
            c.setFont('BC', 9.5); c.setFillColor(PAPEL); c.drawString(ML+30, y+1, f[2].upper())
            c.setFont('BCM', 8); c.setFillColor(HexColor('#9AA2AB'))
            c.drawRightString(A4W-MR-8, y+1, '%d planos' % f[3])
            y -= 17
            c.setFont('BCM', 6.4); c.setFillColor(GRIS)
            c.drawString(ML+2, y, 'CÓDIGO'); c.drawString(ML+54, y, 'TRABAJO')
            c.drawString(ML+238, y, 'MEDIDA'); c.drawString(ML+322, y, 'HORAS')
            c.drawString(ML+356, y, 'NIVEL')
            c.drawRightString(ML+452, y, 'HIERRO'); c.drawRightString(ML+494, y, 'VENTA')
            c.drawRightString(A4W-MR, y, 'PÁG.')
            y -= 11
        else:
            p = f[1]
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
            c.setFont('BM', 7.4); c.setFillColor(TINTA2)
            c.drawRightString(ML+452, y, pesos(p.costo_material()))
            c.setFillColor(VERDE); c.drawRightString(ML+494, y, pesos(p.precio_venta()[0]))
            c.setFont('BM', 8); c.setFillColor(TINTA); c.drawRightString(A4W-MR, y, '%d' % p.pagina)
            linea(c, ML, y-3.4, A4W-MR, HexColor('#EDEFF1'), 0.4)
            y -= 13.2
    pie_simple(c, n, 'Índice')

# ------------------------------------------------------------------ los que dejan plata
def mejores_margenes(c, planos, n):
    cabecera_simple(c, 'Los que dejan plata', 'ordenados por lo que te queda')
    y = A4H - 88
    c.setFont('BC', 22); c.setFillColor(TINTA)
    c.drawString(ML, y, 'LOS 30 TRABAJOS QUE MÁS TE DEJAN')
    y -= 18
    y = parrafo(c, 'Ordenados por la diferencia entre el precio sugerido y lo que te cuesta el hierro. La última '
                   'columna es lo que te queda por hora de trabajo: esa es la que hay que mirar cuando tenés que '
                   'elegir qué fabricar este fin de semana.', ML, y, ANCHO, 'B', 8.8, 11.6) - 16
    datos = []
    for p in planos:
        bajo = p.precio_venta()[0]
        deja = bajo - p.costo_material()
        datos.append((deja, deja/float(p.horas[0]), p))
    datos.sort(key=lambda t: -t[0])
    c.setFont('BCM', 6.6); c.setFillColor(GRIS)
    c.drawString(ML, y, 'CÓDIGO'); c.drawString(ML+54, y, 'TRABAJO')
    c.drawString(ML+270, y, 'HIERRO'); c.drawString(ML+330, y, 'SE VENDE A')
    c.drawString(ML+400, y, 'TE QUEDA'); c.drawRightString(A4W-MR, y, 'POR HORA')
    y -= 4; linea(c, ML, y, A4W-MR, GRIS_CL, 0.5); y -= 12
    for i, (deja, porhora, p) in enumerate(datos[:30]):
        if i % 2 == 0:
            c.setFillColor(HexColor('#F7F8F9')); c.rect(ML-4, y-4, ANCHO+8, 15, stroke=0, fill=1)
        c.setFont('BC', 8.4); c.setFillColor(NARANJA); c.drawString(ML, y, p.codigo)
        c.setFont('B', 8.4); c.setFillColor(TINTA)
        nom = p.nombre
        while c.stringWidth(nom, 'B', 8.4) > 205: nom = nom[:-2]
        c.drawString(ML+54, y, nom)
        c.setFont('BM', 8.2); c.setFillColor(TINTA2); c.drawString(ML+270, y, pesos(p.costo_material()))
        c.drawString(ML+330, y, pesos(p.precio_venta()[0]))
        c.setFillColor(VERDE); c.setFont('BC', 9); c.drawString(ML+400, y, pesos(deja))
        c.setFont('BM', 8.2); c.setFillColor(TINTA); c.drawRightString(A4W-MR, y, pesos(redondear(porhora, 1000)))
        y -= 15
    y -= 8
    c.setFillColor(CREMA); c.roundRect(ML, y-78, ANCHO, 76, 4, stroke=0, fill=1)
    c.setFont('BC', 11); c.setFillColor(TINTA); c.drawString(ML+16, y-24, 'CÓMO SE LEE ESTA TABLA')
    parrafo(c, 'El de arriba de todo no es siempre el mejor negocio: un porta autos deja mucho, pero te ocupa dos '
               'semanas y hay que poner millones en material antes de cobrar. Mirá la última columna. Un trabajo '
               'chico que te deja bien por hora y se vende el mismo mes vale más que uno grande que tenés parado '
               'en el taller esperando que el cliente junte la plata.',
            ML+16, y-40, ANCHO-32, 'B', 8.6, 11.6)
    pie_simple(c, n, 'Los que dejan plata')

# ------------------------------------------------------------------ cierre
def cierre(c, n):
    cabecera_simple(c, 'Cómo seguir')
    y = A4H - 100
    c.setFont('BC', 26); c.setFillColor(TINTA)
    c.drawString(ML, y, 'ELEGÍ UNO Y CORTÁ ESTE SÁBADO.')
    y -= 26
    y = parrafo(c, 'La biblioteca no sirve de nada en la carpeta de descargas. Abrí el índice, buscá un trabajo '
                   'marcado como Principiante que puedas hacer con lo que ya tenés, imprimí la hoja 3 y llevala a la '
                   'casa de hierros. El primer trabajo terminado es el que te cambia la cabeza: después vas a querer '
                   'hacer el siguiente antes de terminar ese.', ML, y, ANCHO, 'B', 10, 13.6) - 26

    pasos = [('1', 'ELEGÍ', 'Filtrá por tiempo y por nivel en el índice. Empezá por algo de 3 a 6 horas.'),
             ('2', 'IMPRIMÍ', 'La hoja 3 es la que va a la casa de hierros. La hoja 4, al banco de trabajo.'),
             ('3', 'COMPRÁ', 'Pedí barras, no metros. La lista ya está sumada y tiene el corte de sierra contemplado.'),
             ('4', 'FABRICÁ', 'Seguí el orden de soldadura. No lo saltees: está pensado para que nada se descuadre.'),
             ('5', 'SACALE FOTO', 'Con el trabajo limpio, de día y apoyado en un fondo liso. Esa foto es la que vende la próxima.'),
             ('6', 'PUBLICALO', 'Con el precio sugerido de la hoja 1. Y cuando te pregunten, respondé el mismo día.')]
    w = (ANCHO - 2*10)/3.0
    for i, (num, tit, txt) in enumerate(pasos):
        x = ML + (i % 3)*(w+10); yy = y - (i//3)*98
        c.setFillColor(CREMA); c.roundRect(x, yy-84, w, 84, 3, stroke=0, fill=1)
        c.setFillColor(NARANJA); c.circle(x+16, yy-18, 9, stroke=0, fill=1)
        c.setFont('BC', 10); c.setFillColor(PAPEL); c.drawCentredString(x+16, yy-21.5, num)
        c.setFont('BC', 10.5); c.setFillColor(TINTA); c.drawString(x+32, yy-22, tit)
        parrafo(c, txt, x+12, yy-44, w-24, 'B', 8, 10.6)
    y -= 216

    c.setFillColor(TINTA); c.roundRect(ML, y-124, ANCHO, 122, 4, stroke=0, fill=1)
    c.setFont('BC', 13); c.setFillColor(NARANJA)
    c.drawString(ML+18, y-28, 'LO QUE VIENE DESPUÉS DE ESTE VOLUMEN')
    items = ['Planos nuevos todos los meses, gratis, con el mismo acceso con el que descargaste este archivo.',
             'Los 12 bonus que vinieron con tu compra: la planilla de cortes, el kit para presupuestar, el checklist '
             'de errores, la terminación de taller y el curso de soldadura en video.',
             'Si un plano no se entiende o encontrás un número que no cierra, escribinos respondiendo el mail con el '
             'que recibiste la descarga. Se corrige y sale corregido para todos.']
    yy = y - 50
    for t in items:
        c.setFillColor(NARANJA); c.circle(ML+22, yy+2.6, 2, stroke=0, fill=1)
        c.setFont('B', 8.6); c.setFillColor(PAPEL)
        for l in envolver(c, t, 'B', 8.6, ANCHO-56):
            c.drawString(ML+30, yy, l); yy -= 11.6
        yy -= 5
    c.setFont('BCM', 7.6); c.setFillColor(GRIS)
    c.drawCentredString(A4W/2, 86, 'Herrero de Finde · Biblioteca de planos · Volumen 1 · edición de octubre de 2026')
    c.drawCentredString(A4W/2, 74, 'Uso personal y comercial de lo que fabriques. Prohibida la reventa o distribución de los archivos.')
    pie_simple(c, n, 'Cómo seguir')

# ============================================================= armado
def construir(salida):
    registrar_fuentes()
    planos = recolectar()
    filas = filas_indice(planos)
    bloques = paginar_indice(filas)
    # paginación: portada, bienvenida, cómo leer, casa de hierros (2), cobrar, cortar, índice, planos..., margen, cierre
    n_casa = 2
    n_front = 1 + 1 + 1 + n_casa + 1 + 1 + len(bloques)
    pag = n_front + 1
    for p in planos:
        p.pagina = pag; pag += 4
    c = rl_canvas.Canvas(salida, pagesize=(A4W, A4H))
    c.setTitle('Herrero de Finde · Biblioteca de planos · Volumen 1')
    c.setAuthor('Herrero de Finde')
    c.setSubject('%d planos de herrería listos para fabricar, con lista de cortes, orden de soldadura y precio de venta sugerido' % len(planos))
    n = 1
    portada(c, planos, n); c.showPage(); n += 1
    bienvenida(c, planos, n); c.showPage(); n += 1
    como_leer(c, n); c.showPage(); n += 1
    n2 = casa_hierros(c, n)
    c.showPage(); n = n2 + 1
    como_cobrar(c, n); c.showPage(); n += 1
    antes_de_cortar(c, n); c.showPage(); n += 1
    for i, b in enumerate(bloques):
        hoja_indice(c, b, n, i == 0); c.showPage(); n += 1
    if n != n_front + 1:
        sys.stderr.write('OJO: paginación del frente %d vs %d\n' % (n, n_front+1))
    for p in planos:
        paginas.hojas(c, p); n += 4
    mejores_margenes(c, planos, n); c.showPage(); n += 1
    cierre(c, n); c.showPage(); n += 1
    c.save()
    return planos, n-1

if __name__ == '__main__':
    salida = sys.argv[1] if len(sys.argv) > 1 else 'biblioteca.pdf'
    planos, total = construir(salida)
    print('%s · %d planos · %d páginas · %.1f MB' % (salida, len(planos), total,
          os.path.getsize(salida)/1048576.0))
