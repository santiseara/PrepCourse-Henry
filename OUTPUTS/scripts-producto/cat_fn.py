# -*- coding: utf-8 -*-
"""FN · Muebles industriales."""
from engine import *
from comun import *

P = []

# ------------------------------------------------------------------ mesa de comedor patas en X
def mesa_x(cod, L, A, H, mat='TC60', tapa='MAD25'):
    w = M[mat]['w']
    pz = []
    for y in (w/2.0, A-w/2.0):
        pass
    for xc in (A*0.35, L-A*0.35):
        pz += [Pz('patax', 'pata en X', mat, (xc-A*0.30, w/2.0, 0), (xc+A*0.30, w/2.0, H-120), corte='en ángulo'),
               Pz('patax', 'pata en X', mat, (xc+A*0.30, w/2.0, 0), (xc-A*0.30, w/2.0, H-120), corte='en ángulo'),
               Pz('patax', 'pata en X', mat, (xc-A*0.30, A-w/2.0, 0), (xc+A*0.30, A-w/2.0, H-120), corte='en ángulo'),
               Pz('patax', 'pata en X', mat, (xc+A*0.30, A-w/2.0, 0), (xc-A*0.30, A-w/2.0, H-120), corte='en ángulo'),
               vy('piso', 'patín del piso', mat, 0, A, xc, w/2.0),
               vy('alto', 'travesaño de arriba', mat, 0, A, xc, H-120+w/2.0)]
    pz.append(vx('union', 'tirante de unión', 'TR6040', A*0.35, L-A*0.35, A/2.0, H-220))
    pz.append(chapa_h('tapa', 'tapa de madera', tapa, 0, L, 0, A, H-25, extra={'sin_vista': ('planta',)}))
    pasos = [
      ('Cortá las ocho piezas de las X con el mismo ángulo. Cortá la primera, controlala y usala de plantilla.', ['patax']),
      ('Armá la primera X apoyada en el piso, con el patín abajo y el travesaño arriba. Medí la altura antes de soldar.', ['patax','piso','alto']),
      ('Armá la segunda X usando la primera como molde: apoyá una sobre la otra para que salgan gemelas.', ['patax','piso','alto']),
      ('Parálas, puntéa el tirante de unión entre las dos y medí las diagonales desde arriba.', ['union']),
      ('Controlá que la mesa no cojee sobre un piso plano y recién ahí soldá todos los cordones.', ['union']),
      ('Pintá o laqueá la estructura y amurá la tapa de madera desde abajo, con tornillos y arandela.', ['tapa']),
    ]
    return Plano('FN', 'Mesa de comedor con patas en X %s' % med2(L, A), pz, pasos, (8, 11), 'Intermedio',
      'La mesa industrial que se vende sola: dos X de caño %s, tirante de unión y tapa de madera maciza de 25 mm. '
      'La estructura la hacés vos, la tapa la comprás cortada y lijada.' % M[mat]['corto'],
      'Parejas jóvenes, cervecerías, cafés y casas de campo. Es el mueble de hierro con más margen de toda la biblioteca: '
      'la gente paga el estilo, no los kilos de hierro.',
      HERR_BASE + ['agujereadora', 'nivel de burbuja'],
      ['El ángulo de las ocho piezas tiene que ser el mismo. Si cortás una por una "a ojo", la mesa queda torcida y no hay forma de arreglarla.',
       'La tapa de madera trabaja con la humedad: amurala con agujeros ovalados o con tornillo y arandela floja, nunca rígida en los cuatro puntos.'],
      variante='%d x %d x %d mm · tapa de madera maciza' % (L, A, H))
P.append(('FN-022', mesa_x('FN-022', 2440, 1020, 760)))
P.append(('FN-031', mesa_x('FN-031', 1800, 900, 760)))

# ------------------------------------------------------------------ mesa de patas rectas
def mesa_recta(cod, L, A, H, tapa='MAD25', mat='TC50'):
    pz = mesa(mat, L, A, H-25, tapa=None, n_trav=1 if L > 1400 else 0, mat_trav='TC40')
    pz.append(chapa_h('tapa', 'tapa de madera', tapa, -40, L+40, -40, A+40, H-25, extra={'sin_vista': ('planta',)}))
    pz += [Pz('escuadra', 'escuadra de la pata', 'PL38', (25, 100, H-100), (120, 25, H-100), corte='en ángulo')
           for _ in (0,)]
    pasos = [
      ('Armá el marco de arriba a 45 grados y escuadralo midiendo las dos diagonales.', ['marco','marcob']),
      ('Sumá el travesaño del medio si la mesa pasa 1,40 m: sin él la tapa se hamaca.', ['trav']),
      ('Dalo vuelta y puntéa las cuatro patas por dentro de las esquinas del marco.', ['pata']),
      ('Controlá con el nivel en los dos sentidos antes de soldar a fondo.', ['pata']),
      ('Rematá todos los cordones, desbastá y pintá la estructura.', ['escuadra']),
      ('Apoyá la tapa centrada, con 40 mm de vuelo por lado, y amurala desde abajo.', ['tapa']),
    ]
    return Plano('FN', 'Mesa de patas rectas %s' % med2(L, A), pz, pasos, (5, 7), 'Principiante',
      'La mesa más fácil de toda la categoría y la que más rápido se vende: marco de caño 50 x 50, cuatro patas y una '
      'tapa de madera con vuelo de 40 mm. Sin cortes en ángulo salvo las esquinas a 45.',
      'Comedores, escritorios, mesas de bar y mesas de local. Si recién arrancás a vender muebles, empezá por esta: '
      'es la que podés cotizar sin miedo porque sabés cuántas horas te lleva.',
      HERR_BASE + ['agujereadora'],
      ['Las patas van por dentro del marco. Si las soldás por fuera, se ven los cordones desde afuera y el mueble pierde la mitad del valor.',
       'Antes de pintar, pasá disco de láminas por todos los cordones que quedan a la vista. En un mueble, la terminación es el producto.'],
      variante='%d x %d x %d mm · tapa con 40 mm de vuelo' % (L, A, H))
P.append(('FN-038', mesa_x('FN-038', 2000, 1000, 760)))
P.append(('FN-045', mesa_recta('FN-045', 1600, 800, 760)))
P.append(('FN-049', mesa_recta('FN-049', 1800, 900, 760)))
P.append(('FN-052', mesa_recta('FN-052', 1400, 700, 750)))

# ------------------------------------------------------------------ banqueta alta
def banqueta(cod, L, A, H):
    pz = marco_xy('marco', 'marco del asiento', 'TC30', 0, L, 0, A, H-15)
    pz += patas('TC30', L, A, H-30, rol='pata')
    pz += [vx('apoyo', 'apoyapiés', 'TC25', 15, L-15, 15, 250),
           vx('apoyo', 'apoyapiés', 'TC25', 15, L-15, A-15, 250),
           vy('apoyob', 'apoyapiés', 'TC25', 30, A-30, 15, 250),
           vy('apoyob', 'apoyapiés', 'TC25', 30, A-30, L-15, 250)]
    pz.append(chapa_h('asiento', 'asiento de madera', 'MAD25', 0, L, 0, A, H-25, extra={'sin_vista': ('planta',)}))
    pasos = [
      ('Armá el marco del asiento, escuadrado y plano.', ['marco','marcob']),
      ('Puntéa las cuatro patas por dentro del marco, bien a 90 grados.', ['pata']),
      ('Marcá los 250 mm en las cuatro patas de una sola vez, con la banqueta parada.', ['pata']),
      ('Soldá el aro del apoyapiés: va igual en los cuatro lados, porque se usa de todos lados.', ['apoyo','apoyob']),
      ('Soldá todo, desbastá y pintá.', ['apoyo','apoyob']),
      ('Amurá la tabla del asiento desde abajo con cuatro tornillos.', ['asiento']),
    ]
    return Plano('FN', 'Banqueta alta de %d mm' % H, pz, pasos, (2, 3), 'Principiante',
      'Banqueta de caño 30 x 30 con asiento de madera y apoyapiés en los cuatro lados. Es el trabajo chico ideal para '
      'hacer en serie: una sola plantilla y salen de a seis en una tarde.',
      'Bares, cervecerías, islas de cocina y casas con desayunador. Se venden siempre de a dos o de a cuatro, '
      'así que una venta son cuatro banquetas.',
      HERR_BASE,
      ['Hacé una plantilla con dos pedazos de ángulo antes de la primera: si vas a hacer seis, la plantilla te ahorra una hora por banqueta.',
       'El apoyapiés a 250 mm no es capricho: más abajo no se usa y más arriba te tapa el asiento.'],
      variante='%d x %d x %d mm · asiento de madera' % (L, A, H))
P.append(('FN-060', banqueta('FN-060', 380, 380, 750)))
P.append(('FN-064', banqueta('FN-064', 400, 400, 650)))
P.append(('FN-067', banqueta('FN-067', 400, 400, 450)))
P.append(('FN-055', mesa_recta('FN-055', 1200, 600, 750)))

# ------------------------------------------------------------------ estantería industrial
def estanteria_ind():
    L, A, H, n = 900, 350, 1800, 5
    pz = patas('TC40', L, A, H, rol='parante')
    alturas = reparto(250, H-100, n)
    for z in alturas:
        pz += [vx('est', 'travesaño del estante', 'TC30', 0, L, 15, z),
               vx('est', 'travesaño del estante', 'TC30', 0, L, A-15, z)]
        pz.append(chapa_h('tabla', 'tabla del estante', 'MAD25', -15, L+15, -10, A+10, z+15))
    pz += [Pz('cruz', 'diagonal del fondo', 'PL25', (20, A-20, 250), (L-20, A-20, H-100), corte='en ángulo')]
    pasos = [
      ('Cortá los cuatro parantes iguales y marcá las cinco alturas en los cuatro juntos, apoyados y parejos.', ['parante']),
      ('Armá el primer lateral: dos parantes y los travesaños de los cinco estantes.', ['parante','est']),
      ('Armá el segundo lateral encima del primero para que salgan gemelos.', ['est']),
      ('Parálos, puntéa el travesaño de arriba y el de abajo y medí las diagonales.', ['est']),
      ('Soldá la diagonal del fondo y rematá todo.', ['cruz']),
      ('Pintá y apoyá las cinco tablas: van sueltas, con 15 mm de vuelo por lado.', ['tabla']),
    ]
    return Plano('FN', 'Estantería industrial de 5 estantes', pz, pasos, (6, 8), 'Principiante',
      'Estantería de caño y madera, 1,80 m de alto y 5 estantes. Es el mueble "industrial" que más se publica y el que '
      'más rápido se vende, porque entra en cualquier pared de 90 cm.',
      'Casas, locales de ropa, cafeterías y depósitos. Si la hacés en serie con dos o tres medidas fijas, podés tener '
      'siempre una armada para mostrar.',
      HERR_BASE + ['agujereadora'],
      ['La diagonal del fondo es lo único que impide que se vaya de costado. No la saques "porque se ve": va contra la pared.',
       'Las tablas van apoyadas, no soldadas ni atornilladas: así el cliente las lija o las cambia de color cuando quiere.'],
      variante='900 x 350 x 1.800 mm · 5 tablas de madera')
P.append(('FN-071', estanteria_ind()))

# ------------------------------------------------------------------ mesa ratona
def mesa_ratona():
    L, A, H = 1100, 600, 450
    pz = mesa('TC40', L, A, H-25, tapa=None, n_trav=0)
    pz += [vx('bajo', 'travesaño bajo', 'TC30', 20, L-20, 20, 120),
           vx('bajo', 'travesaño bajo', 'TC30', 20, L-20, A-20, 120)]
    pz.append(chapa_h('tapa', 'tapa de madera', 'MAD25', -30, L+30, -30, A+30, H-25, extra={'sin_vista': ('planta',)}))
    pz.append(chapa_h('est', 'estante de madera', 'MAD25', 20, L-20, 20, A-20, 135))
    pasos = [
      ('Armá el marco de arriba y escuadralo.', ['marco','marcob']),
      ('Puntéa las cuatro patas cortas por dentro del marco.', ['pata']),
      ('Soldá los dos travesaños bajos a 120 mm del piso: ahí apoya el estante.', ['bajo']),
      ('Controlá que no cojee y soldá todo.', ['bajo']),
      ('Pintá en negro mate: en una mesa ratona la terminación es la mitad del precio.', ['marco']),
      ('Apoyá la tapa con vuelo y el estante de abajo.', ['tapa','est']),
    ]
    return Plano('FN', 'Mesa ratona con estante', pz, pasos, (3, 5), 'Principiante',
      'Mesa baja de living con tapa de madera y estante abajo para revistas. Poco hierro, pocas horas y un precio de '
      'venta que no tiene nada que ver con lo que te costó.',
      'Se vende por Marketplace todo el año y es el mueble que la gente compra por impulso. Hacela en negro mate y con '
      'madera clara: esa combinación es la que más se publica y la que más se vende.',
      HERR_BASE,
      ['Las patas cortas marcan cualquier diferencia de medida. Cortá las cuatro juntas, con tope en la sierra.',
       'Pintá antes de poner la madera. Si pintás después, salpicás la tapa y perdés el trabajo.'],
      variante='1.100 x 600 x 450 mm · tapa y estante de madera')
P.append(('FN-078', mesa_ratona()))

# ------------------------------------------------------------------ isla de cocina
def isla_cocina():
    L, A, H = 2130, 910, 900
    pz = mesa('TC50', L, A, H-30, tapa=None, est_z=200, mat_est='TC40', n_trav=2, mat_trav='TC40')
    pz.append(chapa_h('tapa', 'tapa de madera maciza', 'MAD25', -40, L+40, -40, A+40, H-30, extra={'sin_vista': ('planta',)}))
    pz.append(chapa_h('estante', 'estante de madera', 'MAD25', 50, L-50, 50, A-50, 215))
    pz += [vz('toalla', 'barral de toalla', 'CR25', 300, 700, L+30, A/2.0)]
    pasos = [
      ('Armá el marco de arriba con los dos travesaños: la tapa de una isla pesa y no se puede hamacar.', ['marco','marcob','trav']),
      ('Puntéa las cuatro patas por dentro y controlá nivel en los dos sentidos.', ['pata']),
      ('Soldá el marco del estante a 200 mm del piso.', ['est','estb']),
      ('Sumá el barral lateral: es un detalle que no cuesta nada y sube el precio.', ['toalla']),
      ('Rematá todos los cordones a la vista y pintá.', ['toalla']),
      ('Apoyá la tapa con 40 mm de vuelo y el estante de abajo. Amurá desde abajo.', ['tapa','estante']),
    ]
    return Plano('FN', 'Estructura de isla de cocina 2,13 x 0,91', pz, pasos, (10, 13), 'Intermedio',
      'La estructura de hierro de una isla de cocina, lista para que el cliente le ponga la tapa de madera, de mármol '
      'o de granito. Estante abajo, barral lateral y altura de mesada estándar.',
      'Es el trabajo que te cae cuando alguien está reformando la cocina, y el que mejor se paga de los muebles: '
      'hay presupuesto de obra atrás. Cotizá la estructura sola y que la tapa la compren ellos.',
      HERR_BASE + ['nivel de burbuja'],
      ['Preguntá qué tapa van a poner antes de cortar. El granito necesita apoyo continuo, la madera no: cambia el marco.',
       'La altura final la da la tapa. Si la tapa es de 40 mm, la estructura va 40 mm más baja que la mesada que quieren.'],
      variante='2.130 x 910 x 900 mm · altura de mesada')
P.append(('FN-107', isla_cocina()))

# ------------------------------------------------------------------ botellero
def botellero():
    L, A, H = 900, 400, 1800
    pz = patas('TC30', L, A, H, rol='parante')
    for z in reparto(300, H-120, 5):
        pz += [vx('est', 'travesaño del estante', 'TC25', 0, L, 15, z),
               vx('est', 'travesaño del estante', 'TC25', 0, L, A-15, z)]
        pz.append(chapa_h('tabla', 'tabla del estante', 'MAD25', 0, L, 0, A, z+12))
        for x in interiores(0, L, 5):
            pz.append(vy('divi', 'separador de botella', 'RD10', 40, A-40, x, z+40))
    pz += [Pz('cruz', 'diagonal del fondo', 'PL25', (15, A-15, 300), (L-15, A-15, H-120), corte='en ángulo')]
    pasos = [
      ('Armá los dos laterales con los parantes y los travesaños de los cinco niveles.', ['parante','est']),
      ('Unilos con los travesaños del frente y del fondo, midiendo diagonales.', ['est']),
      ('Soldá la diagonal del fondo.', ['cruz']),
      ('Soldá los separadores de redondo de 10 en cada nivel, repartidos parejos.', ['divi']),
      ('Desbastá bien: este mueble se toca con la mano, no puede tener filos.', ['divi']),
      ('Pintá y apoyá las tablas de cada nivel.', ['tabla']),
    ]
    return Plano('FN', 'Botellero de 5 niveles', pz, pasos, (6, 8), 'Intermedio',
      'Botellero alto de caño 30 con separadores de redondo y tablas de madera. Entra en 90 cm de pared y guarda '
      '30 botellas acostadas.',
      'Vinotecas, cervecerías, parrillas y casas con quincho. Es un mueble de catálogo: lo mostrás y te lo piden en '
      'dos medidas distintas.',
      HERR_BASE,
      ['Los separadores se sueldan por abajo de la tabla, no por arriba: si quedan a la vista, se ve el punto y queda sucio.',
       'Respetá los 100 mm entre separadores. Más junto no entra la botella de espumante, que es la más gorda.'],
      variante='900 x 400 x 1.800 mm · 30 botellas')
P.append(('FN-139', botellero()))

# ------------------------------------------------------------------ cama
def cama(cod, L, A, nombre):
    H = 350
    pz = marco_xy('marco', 'marco de la cama', 'TR6040', 0, L, 0, A, H-30)
    pz += patas('TC50', L, A, H-60, rol='pata')
    pz.append(vz('pata', 'pata del medio', 'TC50', 0, H-60, L/2.0, 30))
    pz.append(vz('pata', 'pata del medio', 'TC50', 0, H-60, L/2.0, A-30))
    for y in interiores(0, A, 11):
        pz.append(vx('listón', 'listón del somier', 'TR4020', 30, L-30, y, H-50))
    pz.append(vx('larguero', 'larguero del medio', 'TC40', 20, L-20, A/2.0, H-80))
    for z in (H, H+300, H+600):
        pass
    pz += marco_xz('respaldo', 'marco del respaldo', 'TC40', 0, L, H-30, H+650, 30)
    for x in interiores(0, L, 7):
        pz.append(vz('barrote', 'barrote del respaldo', 'TC25', H, H+620, x, 30))
    pasos = [
      ('Armá el marco de la cama a 45 grados, en el piso, y medí las dos diagonales: una cama fuera de escuadra no recibe el colchón.', ['marco','marcob']),
      ('Soldá el larguero del medio a lo largo: es lo que evita que el somier se hunda.', ['larguero']),
      ('Puntéa las cuatro patas de las esquinas y las dos del medio.', ['pata']),
      ('Repartí los listones cada %d mm y puntéalos a los largueros.' % int(A/12), ['listón']),
      ('Armá el marco del respaldo aparte y recién después soldalo a la cabecera.', ['respaldo','respaldob']),
      ('Sumá los barrotes del respaldo, repartidos, y rematá todo antes de pintar.', ['barrote']),
    ]
    return Plano('FN', nombre, pz, pasos, (8, 11), 'Intermedio',
      'Estructura de cama con somier de listones de caño, pata central y respaldo de barrotes. No lleva madera: todo '
      'hierro, así no cruje ni se arquea con el tiempo.',
      'Es el mueble que más se pide en departamentos chicos y en casas de alquiler temporario. Hacé una de dos plazas '
      'y sacale fotos con el colchón puesto: así se vende.',
      HERR_BASE + ['nivel de burbuja'],
      ['Medí el colchón real antes de cortar. Las medidas "de una plaza" cambian entre marcas hasta 40 mm.',
       'La pata del medio no es opcional en dos plazas: sin ella el larguero se arquea en seis meses.'],
      variante='colchón de %d x %d mm · respaldo de 650 mm' % (L, A))
P.append(('FN-085', cama('FN-085', 1900, 1400, 'Cama de dos plazas con respaldo')))
P.append(('FN-091', cama('FN-091', 1900, 900, 'Cama de una plaza con respaldo')))
P.append(('FN-088', cama('FN-088', 1900, 1600, 'Cama king con respaldo')))

# ------------------------------------------------------------------ perchero
def perchero():
    L, A, H = 1200, 500, 1700
    pz = []
    for y in (30, A-30):
        pz += [vz('parante', 'parante', 'TC30', 0, H, 30, y),
               vz('parante', 'parante', 'TC30', 0, H, L-30, y),
               vx('piso', 'patín del piso', 'TC30', 0, L, y, 15)]
    pz += [vx('barral', 'barral de colgar', 'CR25', 30, L-30, A/2.0, H-120),
           vx('arriba', 'travesaño de arriba', 'TC30', 0, L, 30, H-15),
           vx('arriba', 'travesaño de arriba', 'TC30', 0, L, A-30, H-15),
           vy('cost', 'travesaño del costado', 'TC30', 0, A, 30, H-15),
           vy('cost', 'travesaño del costado', 'TC30', 0, A, L-30, H-15)]
    pz.append(chapa_h('estante', 'estante de madera', 'MAD25', 20, L-20, 20, A-20, H-14))
    pz += [Pz('diag', 'diagonal', 'PL25', (30, 30, H-500), (30, A-30, H-15), corte='en ángulo'),
           Pz('diag', 'diagonal', 'PL25', (L-30, 30, H-500), (L-30, A-30, H-15), corte='en ángulo')]
    pasos = [
      ('Armá los dos laterales: dos parantes, el patín del piso y el travesaño de arriba.', ['parante','piso','cost']),
      ('Unilos con los dos travesaños de arriba y medí las diagonales desde el piso.', ['arriba']),
      ('Soldá las dos diagonales de planchuela: son las que impiden que se cierre como un acordeón.', ['diag']),
      ('Soldá el barral de colgar a 120 mm abajo del estante, centrado.', ['barral']),
      ('Rematá, desbastá y pintá.', ['barral']),
      ('Apoyá el estante de madera arriba.', ['estante']),
    ]
    return Plano('FN', 'Perchero de pie con estante', pz, pasos, (4, 6), 'Principiante',
      'Perchero industrial de pie, con barral de caño y estante de madera arriba. Se arma en una tarde y es de los '
      'muebles de hierro con mejor relación precio de venta contra material.',
      'Locales de ropa, dormitorios sin placard y alquileres temporarios. Si lo vendés a un local, te piden tres o cuatro '
      'iguales: cotizá con descuento por cantidad y ganás igual.',
      HERR_BASE,
      ['Sin las diagonales el perchero se bambolea apenas le colgás cuatro camperas. No las saques.',
       'El barral va de caño redondo, no de caño cuadrado: la percha tiene que poder correrse.'],
      variante='1.200 x 500 x 1.700 mm · barral y estante')
P.append(('FN-096', perchero()))

# ------------------------------------------------------------------ escritorio
def escritorio():
    L, A, H = 1400, 700, 750
    pz = mesa('TC40', L, A, H-25, tapa=None, n_trav=1, mat_trav='TC30')
    pz.append(chapa_h('tapa', 'tapa de madera', 'MAD25', -25, L+25, -25, A+25, H-25, extra={'sin_vista': ('planta',)}))
    pz += [vx('pasa', 'travesaño pasacables', 'TC30', 40, L-40, A-60, H-150),
           Pz('diag', 'diagonal lateral', 'PL25', (20, 20, H-120), (20, A-20, 200), corte='en ángulo'),
           Pz('diag', 'diagonal lateral', 'PL25', (L-20, 20, H-120), (L-20, A-20, 200), corte='en ángulo')]
    pasos = [
      ('Armá el marco de arriba y el travesaño del medio.', ['marco','marcob','trav']),
      ('Puntéa las cuatro patas por dentro del marco.', ['pata']),
      ('Soldá el travesaño pasacables en el fondo, 150 mm abajo de la tapa.', ['pasa']),
      ('Sumá las diagonales de los laterales: un escritorio sin diagonal se mueve cuando escribís.', ['diag']),
      ('Rematá, desbastá y pintá en negro mate.', ['diag']),
      ('Amurá la tapa desde abajo con tornillos y arandela.', ['tapa']),
    ]
    return Plano('FN', 'Escritorio industrial 1,40 x 0,70', pz, pasos, (4, 6), 'Principiante',
      'Escritorio de caño 40 con tapa de madera y travesaño pasacables en el fondo. Es el mueble que más se vendió '
      'desde que todo el mundo trabaja en casa.',
      'Oficinas chicas, estudios y gente que armó el escritorio en el living. Se vende muy bien de a dos, para parejas '
      'que trabajan en casa.',
      HERR_BASE + ['agujereadora'],
      ['Dejá el travesaño del fondo bien abajo: si lo ponés al ras de la tapa, no entran las rodillas.',
       'La tapa tiene que volar 25 mm por lado. Al ras se ve barato; con vuelo se ve de mueblería.'],
      variante='1.400 x 700 x 750 mm · con pasacables')
P.append(('FN-115', escritorio()))

# ------------------------------------------------------------------ banco de jardín
def banco_jardin():
    L, A, H = 1500, 600, 850
    pz = []
    for x in (60, L-60):
        pz += [vz('pata', 'pata trasera', 'TC40', 0, H, x, A-20),
               vz('pata2', 'pata delantera', 'TC40', 0, 450, x, 20),
               vy('asiento', 'travesaño del asiento', 'TC40', 0, A, x, 430)]
    pz += [vx('larg', 'larguero del asiento', 'TC40', 0, L, 20, 430),
           vx('larg', 'larguero del asiento', 'TC40', 0, L, A-20, 430),
           vx('resp', 'larguero del respaldo', 'TC40', 0, L, A-20, H-20),
           vx('resp', 'larguero del respaldo', 'TC40', 0, L, A-20, H-220)]
    for y in reparto(40, A-40, 4):
        pz.append(vx('tabla', 'tabla del asiento', 'MAD25', 0, L, y, 455))
    for z in (H-60, H-160):
        pz.append(vx('tablar', 'tabla del respaldo', 'MAD25', 0, L, A-45, z))
    pasos = [
      ('Armá los dos laterales: pata trasera larga, pata delantera corta y el travesaño del asiento que las une.', ['pata','pata2','asiento']),
      ('Controlá que los dos laterales sean iguales apoyando uno sobre el otro.', ['asiento']),
      ('Unilos con los dos largueros del asiento y medí las diagonales.', ['larg']),
      ('Soldá los dos largueros del respaldo entre las patas traseras.', ['resp']),
      ('Rematá todo, desbastá y pintá con esmalte para intemperie.', ['resp']),
      ('Amurá las tablas del asiento y del respaldo desde abajo y por atrás, con tornillos de bronce.', ['tabla','tablar']),
    ]
    return Plano('FN', 'Banco de jardín de 1,50 m', pz, pasos, (5, 7), 'Principiante',
      'Banco de plaza con estructura de caño y tablas de madera: asiento a 450 mm y respaldo inclinado hacia atrás. '
      'Aguanta a la intemperie si lo pintás bien.',
      'Municipios, countries, quintas y casas con jardín. Si conseguís un cliente que necesita seis bancos iguales, '
      'tenés el mes resuelto con un solo trabajo.',
      HERR_BASE + ['agujereadora'],
      ['Usá tornillos de bronce o inoxidables. Con tornillos comunes, en un año la madera queda manchada de óxido.',
       'La pata trasera sube hasta el respaldo de una sola pieza: si la empalmás, el respaldo se afloja con el uso.'],
      variante='1.500 x 600 x 850 mm · asiento a 450 mm')
P.append(('FN-124', banco_jardin()))
