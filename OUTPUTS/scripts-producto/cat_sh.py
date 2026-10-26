# -*- coding: utf-8 -*-
"""SH · Herramientas, plantillas y mesas de taller."""
from engine import *
from comun import *

P = []

# ------------------------------------------------------------------ mesa de soldar
def mesa_soldar(cod, L, A, H, tapa, horas, nivel='Principiante'):
    w = 50
    pz = mesa('TC50', L, A, H, tapa=tapa, est_z=200, mat_est='TC40',
              n_trav=2 if L > 1300 else 1, mat_trav='TC40', rol_tapa='tapa de la mesa')
    pasos = [
      ('Cortá todo, escribí la letra en cada pieza y juntá las cuatro del marco de arriba.', ['marco','marcob']),
      ('Presentá el marco sobre una superficie plana, escuadralo y puntéa las cuatro esquinas. '
       'Medí las dos diagonales: tienen que dar lo mismo.', ['marco','marcob']),
      ('Sumá los travesaños del medio, al ras de arriba, repartidos parejos.', ['trav']),
      ('Dalo vuelta y puntéa las patas por dentro del marco, a escuadra con la cinta apoyada en el piso.', ['pata']),
      ('Puntéa el marco del estante a 200 mm del piso, por dentro de las patas.', ['est','estb']),
      ('Controlá escuadra y nivel, soldá todos los cordones y recién ahí apoyá la tapa.', ['tapa']),
      ('Puntéa la tapa de a 20 mm cada 200 mm, alternando de lado, y rellená los cuatro cantos.', ['tapa']),
    ]
    return Plano('SH', 'Mesa de soldar %s' % med2(L, A), pz, pasos, horas, nivel,
      'La mesa que te falta para que todo lo demás te salga derecho. Estructura de caño 50 x 50 y tapa de chapa de %s, '
      'que aguanta el golpe, el amure del sargento y la masa sin pandearse. El estante de abajo te saca del piso '
      'los recortes y las morsas.' % M[tapa]['corto'],
      'Es el primer trabajo que te conviene hacer para vos. Y el que más te piden los talleres del barrio apenas la ven: '
      'el que arregla autos, el tornero y el que hace changas de herrería la necesitan y nunca la compran hecha.',
      HERR_BASE + ['nivel de burbuja'],
      ['Si puntéas la tapa de punta a punta, la chapa se arquea con el calor. Puntos cortos, alternando de lado, '
       'y dejala enfriar antes de seguir.',
       'Las patas van por dentro del marco, nunca abajo: apoyadas abajo, la mesa se bambolea apenas la cargues.'],
      dims=[dict(vista='frente', tipo='v', a=0, b=200, ref=L*0.5, off=-14, lado=-1, txt='200 mm'),
            dict(vista='lateral', tipo='v', a=0, b=H, ref=-A*0.5, off=14, lado=-1)],
      variante='%d x %d x %d mm · tapa de %s' % (L, A, H, M[tapa]['corto']))

P.append(('SH-004', mesa_soldar('SH-004', 1220, 760, 900, 'CH6', (5, 7))))
P.append(('SH-012', mesa_soldar('SH-012', 1500, 750, 900, 'CH6', (6, 8))))
P.append(('SH-019', mesa_soldar('SH-019', 900, 600, 850, 'CH47', (4, 6))))
P.append(('SH-026', mesa_soldar('SH-026', 1800, 900, 900, 'CH6', (7, 10), 'Intermedio')))

# ------------------------------------------------------------------ mesa de fabricación pesada
def mesa_pesada():
    L, A, H = 3000, 1200, 900
    pz = marco_xy('marco', 'marco de arriba', 'TC80', 0, L, 0, A, H-40)
    pz += patas('TC80', L, A, H-80, rol='pata')
    for x in interiores(0, L, 4):
        pz.append(vy('trav', 'travesaño de la tapa', 'TC60', 80, A-80, x, H-30))
    for x in (0, L):
        pass
    pz += [vx('cad', 'cadena de abajo', 'TC50', 40, L-40, 40+25, 250),
           vx('cad', 'cadena de abajo', 'TC50', 40, L-40, A-40-25, 250),
           vy('cadb', 'cadena de abajo', 'TC50', 80, A-80, 40+25, 250),
           vy('cadb', 'cadena de abajo', 'TC50', 80, A-80, L-40-25, 250)]
    pz.append(chapa_h('tapa', 'tapa de la mesa', 'CH6', 0, L, 0, A, H, extra={'sin_vista': ('planta',)}))
    pasos = [
      ('Cortá todo. Esta mesa es pesada: armala en el lugar donde va a quedar.', ['marco','marcob']),
      ('Armá el marco de arriba en el piso, escuadrado, y soldá las cuatro esquinas de los dos lados del caño.', ['marco','marcob']),
      ('Repartí los cuatro travesaños cada 600 mm y soldalos al ras de arriba.', ['trav']),
      ('Dalo vuelta, puntéa las seis patas por dentro del marco y controlá con el nivel en los dos sentidos.', ['pata']),
      ('Sumá la cadena de abajo a 250 mm del piso: es la que le saca el movimiento.', ['cad','cadb']),
      ('Soldá todo, dalo vuelta de nuevo y apoyá la chapa.', ['tapa']),
      ('Fijá la chapa con puntos de 25 mm cada 250 mm, siempre en cruz y nunca seguido.', ['tapa']),
    ]
    return Plano('SH', 'Mesa de fabricación 3 x 1,20', pz, pasos, (10, 14), 'Intermedio',
      'La mesa grande del taller: 3 metros de chapa de 6 mm sobre caño de 80 x 80. Es la que te permite armar un portón '
      'entero arriba de la mesa, en vez de en el piso con dos caballetes y la espalda rota.',
      'El taller que ya trabaja y está cansado de armar en el suelo. También se vende muy bien a herrerías que están '
      'montando un galpón nuevo: es una compra de una sola vez y se cotiza entera.',
      HERR_BASE + ['nivel de burbuja', 'escuadra grande'],
      ['No la armes sobre un piso que no esté nivelado: la mesa toma la forma del piso y después no hay forma de enderezarla.',
       'La chapa de 6 mm de 3 metros pesa más de 140 kg. Conseguite una mano antes de apoyarla, no la levantes solo.'],
      dims=[dict(vista='frente', tipo='v', a=0, b=250, ref=L*0.5, off=-14, lado=-1, txt='250 mm')],
      variante='3.000 x 1.200 x 900 mm · tapa de 6 mm')
P.append(('SH-128', mesa_pesada()))

# ------------------------------------------------------------------ banco de trabajo
def banco_trabajo(cod, L, A, H):
    pz = mesa('TC40', L, A, H, tapa='FEN18', est_z=250, mat_est='TC30', n_trav=1, mat_trav='TC30',
              rol_tapa='tapa de fenólico')
    pz.append(chapa_h('estch', 'piso del estante', 'FEN18', 40, L-40, 40, A-40, 265))
    pz += [Pz('diag', 'diagonal de la pata', 'PL38', (20, 20, H-250), (L-20, 20, H-40), corte='en ángulo')]
    pasos = [
      ('Armá el marco de arriba con el caño de 40 y escuadralo con la diagonal.', ['marco','marcob']),
      ('Sumá el travesaño del medio: es el que evita que la tapa de fenólico se hamaque.', ['trav']),
      ('Puntéa las cuatro patas por dentro del marco.', ['pata']),
      ('Soldá el marco del estante a 250 mm del piso.', ['est','estb']),
      ('Poné la diagonal de planchuela en el lado que va contra la pared: le saca todo el juego.', ['diag']),
      ('Soldá todo, pintá y recién ahí amurá las dos tapas de fenólico con tornillos desde abajo.', ['tapa','estch']),
    ]
    return Plano('SH', 'Banco de trabajo %s' % med2(L, A), pz, pasos, (4, 6), 'Principiante',
      'Banco de taller con tapa de fenólico de 18 mm y estante abajo. No es para soldar arriba: es para armar, '
      'atornillar, pintar y tener la morsa. Sale barato porque la estructura es de caño de 40 y la tapa es madera.',
      'El que está armando el taller y todavía trabaja arriba de un tablón apoyado en dos caballetes. Es el trabajo '
      'más fácil de vender por el barrio: todo el mundo quiere uno en el garaje.',
      HERR_BASE + ['agujereadora', 'mechas de 6'],
      ['El fenólico se amura desde abajo, con tornillos de 1/4 y arandela, nunca soldado ni clavado por arriba.',
       'Si vas a poner la morsa, reforzá esa esquina con un pedazo de planchuela abajo de la tapa: sin eso, el fenólico se hunde.'],
      variante='%d x %d x %d mm · tapa de fenólico' % (L, A, H))
P.append(('SH-030', mesa_soldar('SH-030', 1200, 600, 900, 'CH47', (4, 6))))
P.append(('SH-033', banco_trabajo('SH-033', 1500, 600, 900)))
P.append(('SH-037', banco_trabajo('SH-037', 1200, 600, 900)))
P.append(('SH-041', banco_trabajo('SH-041', 1800, 700, 900)))

# ------------------------------------------------------------------ caballete
def caballete():
    L, A, H = 900, 600, 750
    pz = [vx('viga', 'viga de arriba', 'TC50', 0, L, A/2.0, H-25)]
    for y, s in ((0, 1), (A, -1)):
        for x in (60, L-60):
            pz.append(Pz('pata', 'pata', 'TC40', (x, A/2.0, H-50), (x, 20 if s > 0 else A-20, 20), corte='en ángulo'))
    pz += [Pz('trav', 'travesaño de la pata', 'TC30', (60, 150, 260), (60, A-150, 260), corte='recto'),
           Pz('trav', 'travesaño de la pata', 'TC30', (L-60, 150, 260), (L-60, A-150, 260), corte='recto')]
    pasos = [
      ('Cortá la viga de arriba y las cuatro patas. Las patas llevan corte en ángulo arriba y abajo: usá la pieza ya cortada como plantilla para las otras tres.', ['viga']),
      ('Marcá sobre la viga dónde van las patas, a 60 mm de cada punta.', ['viga']),
      ('Puntéa las dos patas de un lado, controlando que abran parejo.', ['pata']),
      ('Puntéa las dos del otro lado y apoyá el caballete en el piso: si no cojea, soldá.', ['pata']),
      ('Sumá los dos travesaños que atan las patas: sin eso, se abre con el peso.', ['trav']),
      ('Repetí todo para el segundo caballete. Un caballete solo no sirve para nada.', ['trav']),
    ]
    return Plano('SH', 'Caballete de taller (el par)', pz, pasos, (3, 4), 'Principiante',
      'El caballete que aguanta un portón arriba sin moverse. Viga de caño 50 x 50 y patas abiertas de caño 40, '
      'con travesaño para que no se cierren. El plano es para uno: cortá todo por dos y hacé el par de una.',
      'Se vende siempre de a dos y es la venta más fácil que vas a tener: cualquier herrero, carpintero o albañil '
      'te compra un par. Es el trabajo ideal para estrenar la soldadora.',
      HERR_BASE,
      ['Las cuatro patas tienen que abrir igual. Cortá la primera, controlala apoyada y recién ahí cortá las otras tres con esa de plantilla.',
       'Si lo soldás sobre un piso desparejo, el caballete queda rengo para siempre. Armalo sobre la mesa o sobre una chapa plana.'],
      variante='900 x 600 x 750 mm · se hacen de a dos')
P.append(('SH-052', caballete()))

# ------------------------------------------------------------------ carro de herramientas
def carro_herramientas():
    L, A, H = 760, 460, 850
    pz = []
    for z in (120, 420, H-25):
        pz += marco_xy('band%d' % z, 'marco de bandeja', 'TC30', 0, L, 0, A, z)
    pz += patas('TC30', L, A, H-30, rol='pata')
    for z in (120, 420, H-25):
        pz.append(chapa_h('piso%d' % z, 'piso de bandeja', 'CH16', 15, L-15, 15, A-15, z+15))
    pz += [vz('manija', 'manija', 'CR25', H, H+180, 30, A/2.0),
           vz('manija', 'manija', 'CR25', H, H+180, L-30, A/2.0),
           vx('manija2', 'caño de la manija', 'CR25', 30, L-30, A/2.0, H+180)]
    pz += [chapa_h('rueda', 'placa de amure de la rueda', 'CH3', x-45, x+45, y-45, y+45, 0)
           for x in (70, L-70) for y in (70, A-70)]
    pasos = [
      ('Armá los tres marcos de bandeja iguales, uno arriba del otro, y controlá que midan lo mismo.', ['band120','band420','band825']),
      ('Marcá las patas a 120, 420 y 825 mm: ahí van los marcos.', ['pata']),
      ('Apoyá una pata contra la pared, puntéa los tres marcos de un lado y controlá escuadra.', ['pata']),
      ('Sumá las otras dos patas y cerrá la caja. Medí las diagonales de arriba.', ['pata']),
      ('Soldá las placas de las ruedas abajo de cada pata y amurá las ruedas: dos fijas y dos giratorias con freno.', ['rueda']),
      ('Doblá o armá la manija y soldala a las dos patas del frente.', ['manija','manija2']),
      ('Apoyá las tres chapas de los pisos y puntealas cada 150 mm.', ['piso120','piso420','piso825']),
    ]
    return Plano('SH', 'Carro de herramientas de 3 bandejas', pz, pasos, (5, 7), 'Principiante',
      'Carro rodante de tres bandejas con chapa de 1,6 mm y manija de caño. Entra abajo del banco, se lleva las '
      'herramientas al trabajo y no se vuelca cuando lo cargás de un lado.',
      'Lo compran talleres mecánicos, gomerías y herreros. Es un trabajo chico, barato de material y de venta rápida: '
      'el margen sale de la mano de obra, no del hierro.',
      HERR_CHAPA, 
      ['Las ruedas giratorias van adelante, las fijas atrás. Al revés, el carro se te va solo en cualquier pendiente.',
       'La chapa de 1,6 mm se deforma si le das cordón corrido. Puntos de 15 mm cada 150 y listo.'],
      variante='760 x 460 x 850 mm · 4 ruedas de 100')
P.append(('SH-061', carro_herramientas()))

# ------------------------------------------------------------------ estantería de taller
def estanteria(cod, L, A, H, n):
    pz = patas('TC40', L, A, H, rol='parante')
    alturas = reparto(150, H-60, n)
    for i, z in enumerate(alturas):
        pz += [vx('est', 'larguero del estante', 'TC40', 0, L, 20, z),
               vx('est', 'larguero del estante', 'TC40', 0, L, A-20, z),
               vy('estb', 'travesaño del estante', 'TC30', 40, A-40, 20, z),
               vy('estb', 'travesaño del estante', 'TC30', 40, A-40, L-20, z)]
        if A > 400:
            for x in interiores(0, L, 1):
                pz.append(vy('estb', 'travesaño del estante', 'TC30', 40, A-40, x, z))
        pz.append(chapa_h('tabla', 'piso del estante', 'FEN18', 0, L, 0, A, z+20))
    pz += [Pz('cruz', 'cruz de San Andrés', 'PL38', (20, A-20, 150), (L-20, A-20, H-60), corte='en ángulo'),
           Pz('cruz', 'cruz de San Andrés', 'PL38', (L-20, A-20, 150), (20, A-20, H-60), corte='en ángulo')]
    pasos = [
      ('Armá los dos laterales en el piso: dos parantes y los travesaños de cada estante.', ['parante','estb']),
      ('Controlá que los dos laterales sean gemelos apoyando uno sobre el otro antes de soldar.', ['parante','estb']),
      ('Parala contra la pared, puntéa los largueros de un estante del medio y controlá nivel.', ['est']),
      ('Sumá el resto de los largueros de abajo hacia arriba, siempre con el nivel.', ['est']),
      ('Soldá la cruz de San Andrés en el fondo: es lo que le saca el bamboleo.', ['cruz']),
      ('Soldá todo, pintá y recién ahí apoyá los fenólicos de cada estante.', ['tabla']),
    ]
    return Plano('SH', 'Estantería de taller %s' % med2(L, A), pz, pasos, (5, 8), 'Principiante',
      'Estantería de %d estantes de caño de 40, con pisos de fenólico que apoyás y sacás. Aguanta baldes de pintura, '
      'cajas de electrodos y motores chicos sin pandearse.' % n,
      'Se vende por metro a talleres, depósitos, viveros y despensas. Es el trabajo que te conviene ofrecer cuando el '
      'cliente te dice "después vemos": una estantería se cotiza rápido y se entrega en una semana.',
      HERR_BASE + ['nivel de burbuja'],
      ['Los estantes largos se pandean en el medio. Arriba de 1,5 m de largo, el travesaño del medio no es opcional.',
       'Si la vas a amurar a la pared, dejá la cruz del fondo igual: la pared te sostiene, pero no te escuadra.'],
      dims=[dict(vista='frente', tipo='v', a=150, b=alturas[1], ref=L*0.5, off=-16, lado=-1)],
      variante='%d x %d x %d mm · %d estantes' % (L, A, H, n))
P.append(('SH-073', estanteria('SH-073', 1800, 600, 1800, 4)))
P.append(('SH-079', estanteria('SH-079', 1200, 450, 1800, 5)))
P.append(('SH-082', estanteria('SH-082', 1500, 500, 2000, 5)))
P.append(('SH-090', estanteria('SH-090', 900, 400, 1500, 4)))

# ------------------------------------------------------------------ rack de barras
def rack_barras():
    L, H, A = 3000, 2000, 500
    pz = []
    for x in (100, L/2.0, L-100):
        pz.append(vz('parante', 'parante', 'TC80', 0, H, x, 60))
        pz.append(chapa_h('base', 'base de amure', 'CH6', x-100, x+100, 0, 200, 0))
    for z in (400, 800, 1200, 1600, 1950):
        for x in (100, L/2.0, L-100):
            pz.append(vy('brazo', 'brazo', 'TC50', 60, A, x, z))
            pz.append(Pz('escuadra', 'escuadra del brazo', 'PL38', (x, A-120, z-25), (x, 75, z-220), corte='en ángulo'))
    pasos = [
      ('Cortá los tres parantes iguales. Marcá las alturas de los brazos en los tres al mismo tiempo, apoyados juntos.', ['parante']),
      ('Soldá la base de amure abajo de cada parante, bien a escuadra.', ['base']),
      ('Apoyá un parante en la mesa y puntéa sus cinco brazos, controlando que salgan a 90 grados.', ['brazo']),
      ('Sumá la escuadra de planchuela abajo de cada brazo: es la que aguanta el peso.', ['escuadra']),
      ('Repetí con los otros dos parantes y soldá todo a fondo.', ['brazo','escuadra']),
      ('Amurá los tres parantes a la pared con brocas de 10, usando el nivel. Nunca lo dejes parado solo.', ['base']),
    ]
    return Plano('SH', 'Rack de barras de pared', pz, pasos, (6, 8), 'Intermedio',
      'Tres parantes de caño 80 x 80 con cinco brazos cada uno para guardar las barras de 6 m apoyadas, separadas por '
      'perfil. Se termina el "todo el hierro tirado en un rincón" y dejás de cortar en el lugar equivocado por no ver qué tenés.',
      'Lo compran herrerías, casas de hierros chicas y talleres que venden perfiles. También carpinterías, para tablas y varillas.',
      HERR_BASE + ['agujereadora', 'brocas de 10', 'nivel de burbuja'],
      ['Va amurado a una pared de material, nunca a durlock ni a chapa. Cada parante aguanta más de 200 kg colgados.',
       'Las escuadras de abajo del brazo no son adorno: sin ellas el brazo se dobla hacia abajo con la primera barra de 6 m llena.'],
      variante='3.000 x 2.000 mm · 5 niveles · se amura a la pared')
P.append(('SH-085', rack_barras()))

# ------------------------------------------------------------------ mesa para motos
def mesa_moto():
    L, A, H = 2130, 760, 600
    pz = mesa('TC50', L, A, H, tapa='CH3', est_z=150, mat_est='TC40', n_trav=3, mat_trav='TC40',
              rol_tapa='tapa de la mesa')
    pz += [Pz('rampa', 'larguero de la rampa', 'TC40', (L, 180, H-50), (L+700, 180, 20), corte='en ángulo'),
           Pz('rampa', 'larguero de la rampa', 'TC40', (L, A-180, H-50), (L+700, A-180, 20), corte='en ángulo')]
    for i, t in enumerate(reparto(0.1, 0.9, 5)):
        x = L + 700*t; z = (H-50) + ((20)-(H-50))*t
        pz.append(vy('escrampa', 'travesaño de la rampa', 'TC30', 180, A-180, x, z))
    pz.append(vx('tope', 'tope de la rueda', 'TC50', 150, A-150, 0, 0))
    pasos = [
      ('Armá el marco de arriba y los tres travesaños: esta mesa se carga en el medio, así que los travesaños van sí o sí.', ['marco','marcob','trav']),
      ('Puntéa las cuatro patas por dentro y controlá nivel en los dos sentidos.', ['pata']),
      ('Sumá el marco del estante abajo, a 150 mm del piso.', ['est','estb']),
      ('Apoyá la chapa de 3 mm y puntéala cada 200 mm, alternando de lado.', ['tapa']),
      ('Cortá los dos largueros de la rampa con el ángulo que te da el plano y puntéalos a la mesa.', ['rampa']),
      ('Repartí los travesaños de la rampa cada 170 mm.', ['escrampa']),
      ('Soldá el tope de la rueda delantera al frente de la tapa y rematá todos los cordones.', ['tope']),
    ]
    return Plano('SH', 'Mesa de trabajo para motos 2,13 m', pz, pasos, (10, 14), 'Intermedio',
      'Mesa baja de 600 mm con tapa de chapa de 3 mm, rampa de acceso y tope para la rueda. Subís la moto, trabajás parado '
      'y dejás de arrodillarte en el piso. El estante de abajo se lleva las herramientas y las piezas que vas sacando.',
      'Talleres de motos, gomerías y el que arregla motos en el fondo de la casa. Es un trabajo que se cotiza alto porque '
      'nadie lo tiene y el que lo necesita lo necesita en serio.',
      HERR_BASE + ['nivel de burbuja'],
      ['La rampa tiene que entrar justo al ras de la tapa. Si queda un escalón de 10 mm, la rueda lo engancha al subir.',
       'No la hagas más angosta de 760 mm: con la moto arriba necesitás lugar para apoyar el pie y las herramientas.'],
      variante='2.130 x 760 x 600 mm · con rampa')
P.append(('SH-148', mesa_moto()))

# ------------------------------------------------------------------ escuadra de armado
def escuadra_armado():
    L = 600
    pz = [chapa_h('base', 'chapa base', 'CH6', 0, L, 0, L, 0, extra={'sin_vista': ('planta',)}),
          vx('ala', 'ala fija', 'TC50', 0, L, 25, 31),
          vy('alab', 'ala fija', 'TC50', 50, L, 25, 31),
          Pz('refu', 'refuerzo en ángulo', 'PL50', (60, 60, 6), (260, 260, 6), corte='en ángulo'),
          Pz('refu', 'refuerzo en ángulo', 'PL50', (L-60, 60, 6), (L-260, 260, 6), corte='en ángulo')]
    pasos = [
      ('Cortá la chapa base bien a escuadra: esta pieza es la que le va a dar la escuadra a todo lo que fabriques después.', ['base']),
      ('Controlá la base midiendo las dos diagonales. Si no dan iguales, corregí ahora.', ['base']),
      ('Puntéa el primer ala sobre un borde, al ras.', ['ala']),
      ('Apoyá la segunda ala, controlá los 90 grados con una escuadra de albañil y puntéa.', ['alab']),
      ('Sumá los dos refuerzos en diagonal: son los que mantienen los 90 grados cuando la plantilla se calienta.', ['refu']),
      ('Soldá por abajo y por afuera, nunca por adentro del rincón: ahí es donde apoya la pieza.', ['ala','alab']),
    ]
    return Plano('SH', 'Escuadra de armado de 600 mm', pz, pasos, (2, 3), 'Principiante',
      'La plantilla de 90 grados que reemplaza las tres manos que no tenés. Apoyás las dos piezas contra las alas, '
      'puntéas y sale a escuadra siempre. Es la herramienta que más veces vas a usar de toda la biblioteca.',
      'Esta no se vende: se usa. Igual, el herrero que te ve trabajar con dos de estas te las pide. Hacé cuatro: '
      'con dos escuadras armás un marco solo y sin ayuda.',
      HERR_BASE + ['escuadra de albañil'],
      ['Nunca sueldes la pieza del cliente a la plantilla. Un punto de más y arrancás los 90 grados a la amoladora.',
       'Si la plantilla se calienta mucho, se mueve. Dejala enfriar entre armado y armado y controlala cada tanto.'],
      variante='600 x 600 mm · chapa de 6 mm')
P.append(('SH-101', escuadra_armado()))

# ------------------------------------------------------------------ banco de morsa
def banco_morsa():
    L, A, H = 700, 550, 900
    pz = mesa('TC50', L, A, H, tapa='CH6', est_z=250, mat_est='TC40', n_trav=1, mat_trav='TC40',
              rol_tapa='tapa de la mesa')
    pz += [chapa_h('refu', 'refuerzo abajo de la morsa', 'CH6', 60, 360, 60, 360, H-6),
           Pz('escuadra', 'escuadra de la pata', 'PL50', (25, 25, 250), (25, 25, 600), corte='en ángulo')]
    pasos = [
      ('Armá el marco de arriba y el travesaño del medio: la morsa va justo arriba de una pata, nunca en el vacío.', ['marco','marcob','trav']),
      ('Puntéa las cuatro patas por dentro del marco.', ['pata']),
      ('Sumá el marco del estante a 250 mm.', ['est','estb']),
      ('Soldá el refuerzo de chapa en la esquina donde va la morsa, abajo de la tapa.', ['refu']),
      ('Apoyá la tapa y puntéala en cruz desde el centro hacia afuera.', ['tapa']),
      ('Marcá los cuatro agujeros de la morsa con la morsa apoyada, agujereá y amurala con bulones de 12.', ['tapa','refu']),
    ]
    return Plano('SH', 'Banco de morsa', pz, pasos, (4, 6), 'Principiante',
      'Banco chico y macizo, pensado para que la morsa quede arriba de una pata y no se mueva cuando martillás. '
      'Tapa de 6 mm con refuerzo abajo y estante para las limas y los machos.',
      'El herrero que tiene la morsa amurada al banco de madera y la ve bailar con cada golpe. También carpinterías '
      'metálicas chicas y talleres de mantenimiento.',
      HERR_BASE + ['agujereadora', 'mechas de 12'],
      ['La morsa va sobre una pata. Si la ponés en el medio de la tapa, el banco se hamaca con cada golpe de maza.',
       'Antes de agujerear, apoyá la morsa y marcá los agujeros con la morsa puesta: los planos de la morsa mienten.'],
      variante='700 x 550 x 900 mm · tapa de 6 mm')
P.append(('SH-110', banco_morsa()))
