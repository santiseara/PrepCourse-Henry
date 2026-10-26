# -*- coding: utf-8 -*-
"""TK · Racks y bandejas para camioneta."""
from engine import *
from comun import *

P = []

# ------------------------------------------------------------------ rack overland
def rack_caja(cod, L, A, H):
    pz = []
    for (x, y) in [(40, 40), (L-40, 40), (40, A-40), (L-40, A-40)]:
        pz.append(vz('columna', 'columna', 'TC40', 0, H, x, y))
        pz.append(chapa_h('placa', 'placa de amure a la caja', 'CH6', x-70, x+70, y-70, y+70, 0))
    pz += marco_xy('marco', 'marco de la parrilla', 'TC40', 0, L, 0, A, H-20)
    for x in interiores(0, L, 4):
        pz.append(vy('trav', 'travesaño de la parrilla', 'TR4020', 40, A-40, x, H-20))
    pz += [Pz('escuadra', 'escuadra de la columna', 'PL38', (40, 40, H-220), (40, A-250, H-20), corte='en ángulo'),
           Pz('escuadra', 'escuadra de la columna', 'PL38', (L-40, 40, H-220), (L-40, A-250, H-20), corte='en ángulo')]
    pz += [vx('baranda', 'baranda lateral', 'TR4020', 0, L, 40, H+120),
           vx('baranda', 'baranda lateral', 'TR4020', 0, L, A-40, H+120)]
    for x in reparto(200, L-200, 4):
        pz += [vz('parantito', 'parante de la baranda', 'TC25', H-20, H+120, x, 40),
               vz('parantito', 'parante de la baranda', 'TC25', H-20, H+120, x, A-40)]
    pasos = [
      ('Medí la caja de la camioneta con la cinta apoyada en el borde, no en el plástico: ahí es donde se equivocan todos.', ['placa']),
      ('Cortá las cuatro columnas iguales y soldales la placa de amure abajo.', ['columna','placa']),
      ('Armá el marco de la parrilla a 45 grados y escuadralo.', ['marco','marcob']),
      ('Puntéa las cuatro columnas al marco, controlando plomo con el marco apoyado en caballetes.', ['columna']),
      ('Soldá los travesaños de la parrilla repartidos y las dos escuadras de planchuela.', ['trav','escuadra']),
      ('Soldá los parantes y las barandas laterales.', ['parantito','baranda']),
      ('Pintá, apoyá el rack en la caja y amuralo con bulones de 10 y arandelas grandes, con goma entre la placa y la chapa.', ['placa']),
    ]
    return Plano('TK', 'Rack overland para caja de %s' % metros(L), pz, pasos, (8, 12), 'Intermedio',
      'Rack de caño 40 para la caja de la camioneta, con parrilla de travesaños y baranda perimetral. Aguanta carpa de '
      'techo, tablones o la escalera de laburo.',
      'Camionetas de trabajo y de salida: constructores, pescadores, overlanders. Es un trabajo que se cotiza alto '
      'porque el cliente ya vio el precio de los importados.',
      HERR_BASE + ['agujereadora', 'bulones de 10'],
      ['Entre la placa de hierro y la chapa de la caja va una goma. Hierro contra chapa pintada, en tres meses tenés '
       'óxido en la camioneta del cliente.',
       'Medí la caja con la camioneta cargada y descargada: la caja de algunas camionetas se abre 10 mm con peso.'],
      variante='%d x %d x %d mm · parrilla y baranda' % (L, A, H))
P.append(('TK-024', rack_caja('TK-024', 2440, 1500, 700)))
P.append(('TK-031', rack_caja('TK-031', 1800, 1400, 650)))

# ------------------------------------------------------------------ protector de cabina
def protector_cabina(cod, L, H, con_luces):
    pz = marco_xz('marco', 'marco del protector', 'TC50', 0, L, 0, H, 0)
    for x in interiores(0, L, 3):
        pz.append(vz('parante', 'parante vertical', 'TC40', 25, H-25, x, 0))
    pz.append(vx('medio', 'travesaño del medio', 'TC40', 25, L-25, 0, H*0.55))
    pz.append(chapa_v('malla', 'malla del protector', 'CHEX', 25, L-25, 0, H*0.55, H-25))
    pz += [chapa_h('pie', 'pie de amure', 'CH6', x-70, x+70, -80, 80, 0) for x in (60, L-60)]
    pz += [Pz('escuadra', 'escuadra del pie', 'PL50', (x, 0, 300), (x, -140, 10), corte='en ángulo') for x in (60, L-60)]
    if con_luces:
        pz.append(vx('luces', 'barral de luces', 'TC40', L*0.25, L*0.75, 0, H+60))
        pz += [vz('luces', 'parante del barral', 'TC40', H-25, H+60, x, 0) for x in (L*0.25+20, L*0.75-20)]
    pasos = [
      ('Armá el marco a 45 grados, escuadrado sobre la mesa.', ['marco','marcob']),
      ('Soldá el travesaño del medio y los tres parantes verticales.', ['medio','parante']),
      ('Cortá la chapa expandida 10 mm más grande, apoyala por detrás y puntéala cada 120 mm.', ['malla']),
      ('Soldá los dos pies de amure abajo, a escuadra con el marco.', ['pie']),
      ('Soldá las escuadras de los pies: son las que aguantan el frenazo con carga.', ['escuadra']),
    ] + ([('Soldá el barral de luces arriba, con los dos parantitos.', ['luces'])] if con_luces else []) + [
      ('Pintá en negro mate y amurá con cuatro bulones de 10 a la caja, con goma entre el hierro y la chapa.', ['pie']),
    ]
    return Plano('TK', 'Protector de cabina%s' % (' con barral de luces' if con_luces else ''), pz, pasos,
      (5, 7), 'Principiante',
      'El arco que va detrás de la cabina: marco de caño 50, malla de chapa expandida y pies de amure a la caja. '
      'Frena la carga antes de que te entre por la luneta.',
      'Camionetas de trabajo, corralones, forestales y servicios. Es un trabajo chico, rápido y con precio alto: '
      'el cliente lo compara contra un accesorio importado de tres veces el precio.',
      HERR_CHAPA + ['agujereadora', 'bulones de 10'],
      ['Los pies van atornillados, nunca soldados a la camioneta. Soldar sobre el vehículo quema la pintura por dentro '
       'y te deja un reclamo seguro.',
       'La malla va puntéada por detrás, no por delante: así no se ven los puntos desde atrás del auto.'],
      variante='%d x %d mm%s' % (L, H, ' · con barral de luces' if con_luces else ''))
P.append(('TK-038', rack_caja('TK-038', 2000, 1450, 680)))
P.append(('TK-082', protector_cabina('TK-082', 1700, 950, False)))
P.append(('TK-076', protector_cabina('TK-076', 1500, 900, False)))
P.append(('TK-089', protector_cabina('TK-089', 1700, 950, True)))

# ------------------------------------------------------------------ bandeja plana
def bandeja_plana():
    L, A = 2740, 2030
    pz = []
    for y in (60, A-60):
        pz.append(vx('larguero', 'larguero principal', 'TR10050', 0, L, y, 50))
    pz.append(vx('larguero', 'larguero principal', 'TR10050', 0, L, A/2.0, 50))
    for x in reparto(60, L-60, 8):
        pz.append(vy('trav', 'travesaño', 'TR6040', 0, A, x, 50))
    pz.append(chapa_h('piso', 'piso de la bandeja', 'CHA3', 0, L, 0, A, 100, extra={'sin_vista': ('planta',)}))
    for y in (0, A):
        pz.append(vx('baranda', 'baranda', 'TC50', 0, L, y+(25 if y == 0 else -25), 230))
    for x in reparto(200, L-200, 5):
        pz += [vz('parante', 'parante de la baranda', 'TC50', 100, 230, x, 25),
               vz('parante', 'parante de la baranda', 'TC50', 100, 230, x, A-25)]
    pz.append(vy('frente', 'baranda del frente', 'TC50', 0, A, 25, 230))
    pasos = [
      ('Cortá los tres largueros y presentalos sobre el chasis de la camioneta para confirmar las medidas reales.', ['larguero']),
      ('Armá la parrilla en el piso: tres largueros y ocho travesaños, todo escuadrado.', ['larguero','trav']),
      ('Medí las diagonales de la parrilla entera. En una bandeja de 2,74 m, 10 mm de diferencia se ven.', ['trav']),
      ('Soldá el piso de chapa antideslizante con puntos cada 250 mm, alternando de punta a punta.', ['piso']),
      ('Soldá los parantes y después las barandas laterales y la del frente.', ['parante','baranda','frente']),
      ('Pintá con antióxido por abajo antes de montarla: después no llegás nunca más.', ['piso']),
      ('Montala sobre el chasis con los soportes originales y bulones de 12.', ['frente']),
    ]
    return Plano('TK', 'Bandeja plana 2,74 x 2,03', pz, pasos, (20, 28), 'Avanzado',
      'Bandeja de carga completa: tres largueros de caño 100 x 50, ocho travesaños, piso antideslizante y baranda '
      'perimetral. Reemplaza la caja original y te deja la camioneta lista para trabajar.',
      'Corralones, agro, forestales y servicios. Es uno de los trabajos más caros de toda la biblioteca y el que más '
      'te posiciona: una bandeja bien hecha trabaja de publicidad todos los días.',
      HERR_CHAPA + ['nivel de burbuja', 'agujereadora'],
      ['Pintá toda la parte de abajo antes de montarla. Una vez arriba del chasis, esa cara no la pintás nunca más y '
       'es la que se pudre.',
       'No sueldes nada al chasis de la camioneta. La bandeja se monta con los soportes de goma y bulones originales.'],
      variante='2.740 x 2.030 mm · piso antideslizante')
P.append(('TK-060', bandeja_plana()))

# ------------------------------------------------------------------ barras de techo
def barras_techo():
    L, A = 1300, 1200
    pz = []
    for y in (0, A):
        pz.append(vx('barra', 'barra', 'TR6040', 0, L, y, 60))
        for x in (90, L-90):
            pz.append(chapa_h('pie', 'pie de amure', 'CH6', x-60, x+60, y-50, y+50, 0))
            pz.append(Pz('escuadra', 'escuadra del pie', 'PL38', (x, y, 50), (x, y+(80 if y == 0 else -80), 5), corte='en ángulo'))
    pz += [vy('cruz', 'travesaño de unión', 'TR4020', 0, A, x, 60) for x in (200, L-200)]
    pasos = [
      ('Medí el techo entre las canaletas con la cinta apoyada, y restá 10 mm por lado.', ['barra']),
      ('Cortá las dos barras iguales y soldales los pies de amure.', ['barra','pie']),
      ('Soldá las escuadras de cada pie.', ['escuadra']),
      ('Uní las dos barras con los dos travesaños, escuadrado.', ['cruz']),
      ('Desbastá todo: este trabajo va arriba del auto y se ve de cerca.', ['cruz']),
      ('Pintá y amurá con bulones de 8, con goma entre el pie y el techo.', ['pie']),
    ]
    return Plano('TK', 'Barras de techo universales', pz, pasos, (3, 4), 'Principiante',
      'Dos barras de caño rectangular con pies de amure y travesaños de unión. Para escalera, caños o tablones arriba '
      'de cualquier utilitario.',
      'Electricistas, plomeros, pintores y albañiles con utilitario. Es un trabajo de media jornada que se cobra bien '
      'porque la alternativa comprada no aguanta un caño de 6 m.',
      HERR_BASE + ['agujereadora'],
      ['Siempre goma entre el pie y la chapa del techo. Sin eso, en un invierno el techo está oxidado.',
       'No excedas 80 kg repartidos. Si el cliente va a cargar más, el refuerzo tiene que ir al parante de la carrocería, no al techo.'],
      variante='1.300 x 1.200 mm · dos barras')
P.append(('TK-045', barras_techo()))

# ------------------------------------------------------------------ portabicis de enganche
def portabicis():
    L, A, H = 1200, 600, 500
    pz = [vy('lanza', 'lanza del enganche', 'TC50', -A, 0, L/2.0, 100)]
    pz += [vx('cruz', 'travesaño', 'TC50', 0, L, 0, 100),
           vx('cruz', 'travesaño', 'TC50', 0, L, 0, H)]
    pz += [vz('parante', 'parante', 'TC50', 100, H, x, 0) for x in (60, L-60)]
    pz += [Pz('escuadra', 'escuadra', 'PL38', (L/2.0-200, 0, 100), (L/2.0, -200, 100), corte='en ángulo'),
           Pz('escuadra', 'escuadra', 'PL38', (L/2.0+200, 0, 100), (L/2.0, -200, 100), corte='en ángulo')]
    for x in reparto(150, L-150, 3):
        pz.append(vy('soporte', 'soporte de rueda', 'TR4020', 0, 260, x, H+30))
    pz.append(chapa_h('placa', 'placa del enganche', 'CH6', L/2.0-60, L/2.0+60, -A-60, -A, 100))
    pasos = [
      ('Cortá la lanza y soldale la placa del enganche: esa unión aguanta todo el peso en voladizo.', ['lanza','placa']),
      ('Soldá el travesaño de abajo a la lanza, a 90 grados exactos.', ['cruz']),
      ('Soldá las dos escuadras entre la lanza y el travesaño.', ['escuadra']),
      ('Puntéa los dos parantes y el travesaño de arriba.', ['parante']),
      ('Soldá los tres soportes de rueda, repartidos.', ['soporte']),
      ('Probalo cargado con tres bicicletas antes de entregarlo, moviendo con la mano.', ['soporte']),
    ]
    return Plano('TK', 'Portabicis de enganche para 3', pz, pasos, (4, 6), 'Intermedio',
      'Portabicis que entra en el enganche de 2" con tres soportes de rueda. Todo el trabajo está en la unión de la '
      'lanza con el travesaño: ahí es donde se rompen los comprados.',
      'Familias, ciclistas y gente que sale de fin de semana. Es un trabajo chico con un precio de venta que sorprende, '
      'porque el equivalente importado sale una fortuna.',
      HERR_BASE + ['agujereadora'],
      ['La unión lanza-travesaño va con escuadras sí o sí. Sin ellas, con el movimiento del camino se fisura en meses.',
       'Dejá previsto el agujero del perno del enganche antes de soldar nada: después no entra la mecha.'],
      variante='1.200 x 600 x 500 mm · enganche de 2"')
P.append(('TK-053', portabicis()))

# ------------------------------------------------------------------ jaula de caja
def jaula_caja():
    L, A, H = 2200, 1400, 600
    pz = []
    for x in reparto(50, L-50, 4):
        pz += [vz('parante', 'parante', 'TC40', 0, H, x, 30),
               vz('parante', 'parante', 'TC40', 0, H, x, A-30)]
    pz += [vx('baranda', 'baranda superior', 'TC40', 0, L, 30, H-20),
           vx('baranda', 'baranda superior', 'TC40', 0, L, A-30, H-20),
           vx('medio', 'baranda del medio', 'TR4020', 0, L, 30, H/2.0),
           vx('medio', 'baranda del medio', 'TR4020', 0, L, A-30, H/2.0)]
    pz += [vy('frente', 'baranda del frente', 'TC40', 0, A, 30, H-20),
           vy('frente', 'baranda del frente', 'TC40', 0, A, 30, H/2.0),
           vz('parante', 'parante', 'TC40', 0, H, 30, A/2.0)]
    pz += [chapa_h('pie', 'pie de amure', 'CH6', x-50, x+50, y-50, y+50, 0)
           for x in (50, L-50) for y in (30, A-30)]
    pz.append(chapa_v('malla', 'malla del frente', 'CHEX', 30, A-30, 30, 30, H-20, extra={'sin_vista': ('frente',)}))
    pasos = [
      ('Medí la caja por dentro y descontá 20 mm por lado.', ['parante']),
      ('Cortá los parantes iguales y soldales los pies de amure a los cuatro de las esquinas.', ['parante','pie']),
      ('Armá los dos laterales en el piso: parantes, baranda del medio y baranda de arriba.', ['baranda','medio']),
      ('Levantá los dos laterales dentro de la caja y unilos con las barandas del frente.', ['frente']),
      ('Puntéa la malla del frente por detrás.', ['malla']),
      ('Pintá y amurá con bulones de 10 y goma entre el hierro y la chapa de la caja.', ['pie']),
    ]
    return Plano('TK', 'Jaula de barandas para caja', pz, pasos, (6, 9), 'Principiante',
      'Barandas altas con malla al frente para llevar carga suelta: escombro, bolsas, leña o animales chicos. '
      'Desmontable, con cuatro pies atornillados.',
      'Fleteros, corralones, criadores y el que usa la camioneta para todo. Se vende por necesidad, no por gusto: '
      'cuando lo piden, lo piden para la semana que viene.',
      HERR_CHAPA + ['agujereadora'],
      ['Hacela desmontable. Una jaula soldada a la caja le baja el valor de reventa a la camioneta y el cliente lo sabe.',
       'La baranda del medio no es decorativa: sin ella, la carga empuja los parantes y se abren hacia afuera.'],
      variante='2.200 x 1.400 x 600 mm · desmontable')
P.append(('TK-070', jaula_caja()))
