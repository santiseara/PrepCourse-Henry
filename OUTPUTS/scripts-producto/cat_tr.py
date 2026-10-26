# -*- coding: utf-8 -*-
"""TR · Trailers y carros."""
from engine import *
from comun import *

P = []

def chasis_base(L, A, mat_larg='TR10050', mat_trav='TR6040', z=250, ntrav=6, lanza=900):
    """Dos largueros, travesaños, lanza en V y guardabarros."""
    pz = [vx('larguero', 'larguero del chasis', mat_larg, 0, L, 60, z),
          vx('larguero', 'larguero del chasis', mat_larg, 0, L, A-60, z)]
    for x in reparto(50, L-50, ntrav):
        pz.append(vy('trav', 'travesaño del chasis', mat_trav, 0, A, x, z))
    pz += [Pz('lanza', 'lanza', mat_larg, (-lanza, A/2.0, z), (L*0.25, 60, z), corte='en ángulo'),
           Pz('lanza', 'lanza', mat_larg, (-lanza, A/2.0, z), (L*0.25, A-60, z), corte='en ángulo')]
    pz.append(vy('eje', 'eje con elásticos (se compra)', 'RD20', -60, A+60, L*0.55, 80,
                 extra={'no_lista': True}))
    for y in (-30, A+30):
        pz.append(Pz('rueda', 'rueda', 'CH3', (L*0.55, y, 160), (L*0.55, y+(60 if y < 0 else -60), 160),
                     kind='cil', w=560, h=560, extra={'no_lista': True}))
    return pz

# ------------------------------------------------------------------ trailer utilitario
def trailer_util(cod, L, A, alto_baranda=400):
    z = 250
    pz = chasis_base(L, A, z=z)
    pz.append(chapa_h('piso', 'piso de fenólico', 'FEN18', 0, L, 0, A, z+50, extra={'sin_vista': ('planta',)}))
    pz += marco_xz('baranda', 'baranda lateral', 'TC40', 0, L, z+68, z+68+alto_baranda, 20)
    pz += marco_xz('baranda', 'baranda lateral', 'TC40', 0, L, z+68, z+68+alto_baranda, A-20)
    for x in interiores(0, L, 3):
        pz += [vz('parante', 'parante de la baranda', 'TC40', z+68, z+68+alto_baranda, x, 20),
               vz('parante', 'parante de la baranda', 'TC40', z+68, z+68+alto_baranda, x, A-20)]
    pz += marco_yz('frente', 'baranda del frente', 'TC40', 0, A, z+68, z+68+alto_baranda, 20)
    pz += [chapa_v('chapa', 'chapa de la baranda', 'CH16', 20, L-20, 20, z+80, z+68+alto_baranda-20,
                   extra={'sin_vista': ('frente',)})]
    pasos = [
      ('Armá el chasis en el piso: dos largueros y los seis travesaños, todo escuadrado. Medí las dos diagonales.', ['larguero','trav']),
      ('Cortá la lanza en V con el ángulo del plano y soldala a los largueros, con la punta en el eje del trailer.', ['lanza']),
      ('Amurá el eje con elásticos abajo de los largueros, con el centro a %d mm de la punta trasera.' % int(L*0.45), ['eje','rueda']),
      ('Apoyá el chasis sobre las ruedas y controlá que quede nivelado y sin panza.', ['rueda']),
      ('Armá las dos barandas laterales y la del frente, aparte, y soldalas al chasis.', ['baranda','barandab','parante','frente','frenteb']),
      ('Puntéa la chapa de las barandas por dentro, cada 200 mm.', ['chapa']),
      ('Pintá todo con antióxido, sobre todo abajo, y recién ahí amurá el piso de fenólico.', ['piso']),
    ]
    return Plano('TR', 'Trailer utilitario %s' % med2(L, A), pz, pasos, (16, 22), 'Avanzado',
      'Trailer de caja abierta con chasis de caño 100 x 50, lanza en V, piso de fenólico y barandas de %d mm. '
      'Es el trailer que sirve para todo: mudanza, escombro, leña o la moto.' % alto_baranda,
      'Cualquiera que tenga enganche. Es el trabajo más buscado de la categoría y el que mejor se paga por hora, '
      'porque el comprado sale tres veces más.',
      HERR_CHAPA + ['nivel de burbuja', 'agujereadora'],
      ['El eje va atrás del centro de la caja, nunca en el medio exacto: un trailer con el eje centrado culebrea a 80 km/h.',
       'Antes de cortar nada, averiguá qué pide el registro de tu provincia para patentarlo: la lanza, la chapa patente '
       'y las luces tienen medidas obligatorias.'],
      extras=[('Eje con elásticos, bujes y cubo (armado)', '1 juego', 480000),
              ('Dos ruedas con cubierta', '2 unidades', 320000),
              ('Kit de luces, chapa patente y cableado', '1 juego', 95000),
              ('Enganche, cuplín y rueda de apoyo', '1 juego', 140000)],
      variante='%d x %d mm · barandas de %d mm' % (L, A, alto_baranda))
P.append(('TR-018', trailer_util('TR-018', 1800, 1200)))
P.append(('TR-026', trailer_util('TR-026', 2000, 1250, 450)))
P.append(('TR-034', trailer_util('TR-034', 2400, 1500, 500)))

# ------------------------------------------------------------------ trailer con rampa
def trailer_rampa():
    L, A, z = 4880, 2080, 300
    pz = chasis_base(L, A, 'TR12060', 'TR6040', z=z, ntrav=9, lanza=1200)
    pz.append(chapa_h('piso', 'piso de fenólico', 'FEN18', 0, L, 0, A, z+60, extra={'sin_vista': ('planta',)}))
    for y in (30, A-30):
        pz.append(vx('baranda', 'baranda lateral', 'TC50', 0, L, y, z+300))
        for x in reparto(100, L-100, 5):
            pz.append(vz('parante', 'parante', 'TC50', z+30, z+300, x, y))
    pz += [Pz('rampa', 'larguero de la rampa', 'TR6040', (L, 300, z+30), (L+1400, 300, 30), corte='en ángulo'),
           Pz('rampa', 'larguero de la rampa', 'TR6040', (L, A-300, z+30), (L+1400, A-300, 30), corte='en ángulo')]
    for i, t in enumerate(reparto(0.08, 0.95, 6)):
        pz.append(vy('travrampa', 'travesaño de la rampa', 'TC40', 300, A-300, L+1400*t, z+30 + (30-(z+30))*t))
    pasos = [
      ('Armá el chasis: dos largueros de 120 x 60 y nueve travesaños. Este trailer es largo: controlá que no tenga panza con un hilo de punta a punta.', ['larguero','trav']),
      ('Soldá la lanza en V, bien centrada y en el eje del chasis.', ['lanza']),
      ('Amurá el eje con elásticos, con el centro a un 55 % del largo desde la lanza.', ['eje','rueda']),
      ('Soldá los parantes y las barandas laterales.', ['parante','baranda']),
      ('Armá la rampa aparte con sus dos largueros y los travesaños, y probá que apoye bien antes de soldar las bisagras.', ['rampa','travrampa']),
      ('Pintá todo con antióxido, abajo primero.', ['rampa']),
      ('Amurá el piso de fenólico con tornillos autoperforantes y arandela, cada 300 mm.', ['piso']),
    ]
    return Plano('TR', 'Trailer con rampa 2,08 x 4,88', pz, pasos, (28, 34), 'Avanzado',
      'Trailer largo con rampa trasera para subir cuatriciclo, moto o un carrito: chasis de 120 x 60, nueve travesaños, '
      'barandas bajas y rampa abatible. Es el trailer de trabajo pesado.',
      'Talleres, productores, gente de fierros. Es el trabajo más caro de la biblioteca después del porta autos, '
      'y el que más adelanto te permite pedir.',
      HERR_CHAPA + ['nivel de burbuja', 'agujereadora'],
      ['Un chasis de casi 5 m se pandea solo con su peso. Armalo sobre cuatro caballetes nivelados y controlá con un '
       'hilo tenso de punta a punta antes de soldar a fondo.',
       'La rampa tiene que apoyar en el piso con la misma inclinación que el ángulo de ataque del vehículo que va a subir. '
       'Si queda muy empinada, el cuatriciclo pega abajo.'],
      extras=[('Eje con elásticos de 1.500 kg, bujes y cubos', '1 juego', 680000),
              ('Dos ruedas con cubierta', '2 unidades', 380000),
              ('Kit de luces, chapa patente y cableado', '1 juego', 95000),
              ('Enganche, cuplín, rueda de apoyo y bisagras de rampa', '1 juego', 180000)],
      variante='4.880 x 2.080 mm · rampa de 1.400 mm')
P.append(('TR-072', trailer_rampa()))

# ------------------------------------------------------------------ carro de arrastre
def carro_quinta():
    L, A, z = 2000, 1200, 500
    pz = [vx('larguero', 'larguero del chasis', 'TR8040', 0, L, 50, z),
          vx('larguero', 'larguero del chasis', 'TR8040', 0, L, A-50, z)]
    for x in reparto(40, L-40, 5):
        pz.append(vy('trav', 'travesaño', 'TR6040', 0, A, x, z))
    pz.append(chapa_h('piso', 'piso de chapa', 'CH3', 0, L, 0, A, z+40, extra={'sin_vista': ('planta',)}))
    for y in (25, A-25):
        pz.append(vx('baranda', 'baranda', 'TC40', 0, L, y, z+420))
        for x in reparto(80, L-80, 4):
            pz.append(vz('parante', 'parante', 'TC40', z+40, z+420, x, y))
    pz += [chapa_v('chapa', 'chapa de la baranda', 'CH16', 25, L-25, 25, z+50, z+400, extra={'sin_vista': ('frente',)})]
    pz += [Pz('lanza', 'lanza', 'TR8040', (-800, A/2.0, z), (400, 50, z), corte='en ángulo'),
           Pz('lanza', 'lanza', 'TR8040', (-800, A/2.0, z), (400, A-50, z), corte='en ángulo')]
    for y in (-20, A+20):
        pz.append(Pz('rueda', 'rueda', 'CH3', (L*0.6, y, 280), (L*0.6, y+(50 if y < 0 else -50), 280),
                     kind='cil', w=560, h=560, extra={'no_lista': True}))
    pz.append(vy('eje', 'eje (se compra)', 'RD20', -40, A+40, L*0.6, 280, extra={'no_lista': True}))
    pasos = [
      ('Armá el chasis con los dos largueros y los cinco travesaños, escuadrado.', ['larguero','trav']),
      ('Soldá la lanza en V. En un carro de quinta la lanza va más corta: se maneja de a pie o con un tractorcito.', ['lanza']),
      ('Amurá el eje y las ruedas, y controlá que el carro quede nivelado vacío.', ['eje','rueda']),
      ('Soldá los parantes y las barandas.', ['parante','baranda']),
      ('Puntéa la chapa de las barandas por dentro.', ['chapa']),
      ('Pintá y soldá el piso de chapa de 3 mm con puntos alternados.', ['piso']),
    ]
    return Plano('TR', 'Carro de arrastre para quinta', pz, pasos, (12, 16), 'Intermedio',
      'Carro de arrastre sin patente: chasis de 80 x 40, piso de chapa de 3 mm y barandas de 400 mm. Es para adentro '
      'del campo o de la quinta, no para la ruta.',
      'Quintas, viveros, criaderos y campos chicos. Se vende rápido porque es barato de hacer y resuelve un problema '
      'de todos los días.',
      HERR_CHAPA,
      ['Este carro no se patenta ni sale a la ruta. Dejáselo claro al cliente por escrito en el presupuesto.',
       'El piso de chapa soldado de corrido se arquea con el sol. Puntos de 25 mm cada 250, alternando.'],
      extras=[('Eje recto con bujes y dos ruedas de 13"', '1 juego', 290000)],
      variante='2.000 x 1.200 mm · piso de chapa')
P.append(('TR-011', trailer_util('TR-011', 1500, 1100, 350)))
P.append(('TR-029', trailer_util('TR-029', 2600, 1600, 500)))
P.append(('TR-041', carro_quinta()))

# ------------------------------------------------------------------ porta autos
def porta_autos():
    L, A, z = 6100, 2440, 400
    pz = [vx('larguero', 'larguero principal', 'C120', 0, L, 160, z),
          vx('larguero', 'larguero principal', 'C120', 0, L, A-160, z)]
    for x in reparto(60, L-60, 11):
        pz.append(vy('trav', 'travesaño', 'TR8040', 0, A, x, z))
    for y in (500, A-500):
        pz.append(vx('rodera', 'rodera', 'CHA3', 0, L, y, z+45))
    pz += [Pz('lanza', 'lanza', 'C120', (-1500, A/2.0, z), (1200, 160, z), corte='en ángulo'),
           Pz('lanza', 'lanza', 'C120', (-1500, A/2.0, z), (1200, A-160, z), corte='en ángulo')]
    for y in (-40, A+40):
        for x in (L*0.55, L*0.72):
            pz.append(Pz('rueda', 'rueda', 'CH3', (x, y, 290), (x, y+(60 if y < 0 else -60), 290),
                         kind='cil', w=580, h=580, extra={'no_lista': True}))
    pz += [vy('eje', 'eje doble con elásticos (se compra)', 'RD20', -60, A+60, x, 290, extra={'no_lista': True})
           for x in (L*0.55, L*0.72)]
    pz += [Pz('rampa', 'rampa', 'TR6040', (L, 500, z+20), (L+1600, 500, 20), corte='en ángulo'),
           Pz('rampa', 'rampa', 'TR6040', (L, A-500, z+20), (L+1600, A-500, 20), corte='en ángulo')]
    pasos = [
      ('Armá los dos largueros de perfil C sobre caballetes nivelados: a 6 m, cualquier panza se nota.', ['larguero']),
      ('Soldá los once travesaños, controlando escuadra cada tres.', ['trav']),
      ('Soldá la lanza larga en V, que en este trailer entra hasta la mitad del chasis.', ['lanza']),
      ('Amurá el eje doble, respetando la separación entre ejes que pide el fabricante.', ['eje','rueda']),
      ('Soldá las dos roderas de chapa antideslizante, alineadas con la trocha del auto.', ['rodera']),
      ('Armá las dos rampas y probalas con un auto antes de pintar.', ['rampa']),
      ('Pintá todo, abajo primero, y montá luces, guardabarros y malacate.', ['rodera']),
    ]
    return Plano('TR', 'Porta autos de doble eje 6,10 m', pz, pasos, (45, 60), 'Avanzado',
      'Trailer porta autos con largueros de perfil C 120, once travesaños, doble eje, roderas de chapa antideslizante '
      'y dos rampas. Es el trabajo más grande de toda la biblioteca.',
      'Talleres, compra-venta de autos, auxilios y pistas de carrera. Un solo porta autos bien hecho te paga un mes '
      'entero de taller, pero pedí el 50 % de adelanto: el material solo ya es una fortuna.',
      HERR_CHAPA + ['nivel de burbuja', 'agujereadora', 'caballetes nivelados'],
      ['Con doble eje, la separación entre ejes y la posición respecto del centro de carga no se improvisan: seguí lo '
       'que dice el fabricante del eje o el trailer va a comerse las cubiertas.',
       'No lo hagas sin averiguar el trámite de patentamiento. Un porta autos sin papeles no se puede usar ni vender.'],
      extras=[('Doble eje con elásticos de 2.000 kg, bujes y cubos', '1 juego', 1450000),
              ('Cuatro ruedas con cubierta', '4 unidades', 760000),
              ('Kit de luces, chapa patente, cableado y guardabarros', '1 juego', 220000),
              ('Enganche, cuplín reforzado, rueda de apoyo y malacate', '1 juego', 420000)],
      variante='6.100 x 2.440 mm · doble eje')
P.append(('TR-129', porta_autos()))

# ------------------------------------------------------------------ trailer para lancha
def trailer_lancha():
    L, A, z = 5500, 1800, 420
    pz = [vx('espina', 'espina central', 'TR12060', 0, L, A/2.0, z)]
    for x in reparto(400, L-200, 6):
        pz.append(vy('trav', 'travesaño', 'TR6040', 200, A-200, x, z))
    for y in (350, A-350):
        pz.append(Pz('brazo', 'brazo de apoyo', 'TR6040', (800, A/2.0, z), (L-400, y, z+120), corte='en ángulo'))
    pz += [Pz('lanza', 'lanza', 'TR12060', (-1200, A/2.0, z), (600, A/2.0, z), corte='recto')]
    pz.append(vz('torre', 'torre del malacate', 'TC80', z, z+700, -900, A/2.0))
    pz.append(Pz('torre', 'escuadra de la torre', 'PL50', (-900, A/2.0, z+500), (-300, A/2.0, z+20), corte='en ángulo'))
    for y in (-30, A+30):
        pz.append(Pz('rueda', 'rueda', 'CH3', (L*0.62, y, 250), (L*0.62, y+(50 if y < 0 else -50), 250),
                     kind='cil', w=500, h=500, extra={'no_lista': True}))
    pz.append(vy('eje', 'eje con elásticos (se compra)', 'RD20', -60, A+60, L*0.62, 250, extra={'no_lista': True}))
    for x in reparto(1200, L-600, 4):
        pz += [vz('rodillo', 'soporte de rodillo', 'TC40', z+40, z+240, x, A/2.0-260),
               vz('rodillo', 'soporte de rodillo', 'TC40', z+40, z+240, x, A/2.0+260)]
    pasos = [
      ('Armá la espina central con la lanza, todo en una línea: este trailer trabaja a lo largo.', ['espina','lanza']),
      ('Soldá los travesaños a la espina, escuadrados.', ['trav']),
      ('Soldá los dos brazos de apoyo en diagonal: son los que sostienen el casco en los costados.', ['brazo']),
      ('Amurá el eje con elásticos a un 62 % del largo: con la lancha arriba, el peso va adelante.', ['eje','rueda']),
      ('Soldá los ocho soportes de rodillo, todos a la misma altura.', ['rodillo']),
      ('Armá la torre del malacate con su escuadra.', ['torre']),
      ('Pintá con antióxido y esmalte marino: este trailer entra al agua todas las veces.', ['torre']),
    ]
    return Plano('TR', 'Trailer para lancha de 6,7 m', pz, pasos, (27, 33), 'Avanzado',
      'Trailer de espina central con brazos de apoyo, soportes de rodillo y torre de malacate, para lanchas de hasta '
      '6,7 m. La espina central deja el casco apoyado en los rodillos y no en el chasis.',
      'Náutica, clubes y gente con lancha. Es un trabajo de nicho que se paga muy bien porque hay pocos que lo hagan '
      'bien, y el que lo necesita no tiene alternativa.',
      HERR_CHAPA + ['nivel de burbuja'],
      ['Este trailer se moja en agua y a veces salada. Antióxido de dos componentes y esmalte marino, no esmalte común.',
       'La altura de los rodillos la da el casco del cliente, no el plano. Medí con la lancha presente antes de soldar los soportes.'],
      extras=[('Eje con elásticos de 1.200 kg, bujes y cubos', '1 juego', 620000),
              ('Dos ruedas con cubierta', '2 unidades', 360000),
              ('Ocho rodillos de goma con eje', '8 unidades', 240000),
              ('Malacate, cable, luces y chapa patente', '1 juego', 290000)],
      variante='5.500 x 1.800 mm · espina central y rodillos')
P.append(('TR-117', trailer_lancha()))

# ------------------------------------------------------------------ zorra de taller
def zorra():
    L, A, H = 1200, 700, 400
    pz = marco_xy('marco', 'marco de la plataforma', 'TC50', 0, L, 0, A, H-25)
    pz += [vy('trav', 'travesaño', 'TC40', 25, A-25, x, H-25) for x in interiores(0, L, 3)]
    pz.append(chapa_h('piso', 'piso de chapa', 'CH3', 0, L, 0, A, H, extra={'sin_vista': ('planta',)}))
    pz += [vz('pata', 'pata', 'TC50', 100, H-50, x, y) for x in (90, L-90) for y in (90, A-90)]
    pz += [chapa_h('rueda', 'placa de la rueda', 'CH6', x-60, x+60, y-60, y+60, 100)
           for x in (90, L-90) for y in (90, A-90)]
    pz += [vz('manija', 'manija', 'CR25', H, H+850, 60, A/2.0),
           vx('manija2', 'agarre de la manija', 'CR25', -80, 200, A/2.0, H+850)]
    pasos = [
      ('Armá el marco de la plataforma y los tres travesaños.', ['marco','marcob','trav']),
      ('Soldá las cuatro patas cortas y las placas de las ruedas.', ['pata','rueda']),
      ('Amurá dos ruedas fijas atrás y dos giratorias con freno adelante.', ['rueda']),
      ('Soldá la manija al frente, inclinada, y su agarre arriba.', ['manija','manija2']),
      ('Puntéa el piso de chapa cada 200 mm.', ['piso']),
      ('Cargala con 300 kg antes de entregarla: si una rueda se traba, es ahora y no en lo del cliente.', ['piso']),
    ]
    return Plano('TR', 'Zorra de taller de 1,20 x 0,70', pz, pasos, (5, 7), 'Principiante',
      'Carro plano de cuatro ruedas con manija: la zorra que mueve el motor, la caja de herramientas o las barras '
      'de 6 m dentro del taller.',
      'Talleres, depósitos, corralones y herrerías. Es un trabajo chico que se vende por necesidad y se hace en una '
      'jornada: ideal para llenar un hueco entre dos trabajos grandes.',
      HERR_CHAPA,
      ['Ruedas giratorias adelante, fijas atrás. Las cuatro giratorias hacen que la zorra se vaya sola con cualquier pendiente.',
       'Las placas de las ruedas van soldadas abajo de la pata y con cuatro bulones, no con dos: con dos, en seis meses se aflojan.'],
      extras=[('Cuatro ruedas de 125 mm (dos giratorias con freno)', '1 juego', 96000)],
      variante='1.200 x 700 x 400 mm · 4 ruedas')
P.append(('TR-055', zorra()))
