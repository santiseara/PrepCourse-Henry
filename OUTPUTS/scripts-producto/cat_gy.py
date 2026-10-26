# -*- coding: utf-8 -*-
"""GY · Gimnasio en casa y racks."""
from engine import *
from comun import *

P = []

# ------------------------------------------------------------------ jaula de potencia
def jaula(L, A, H, mat='TC80'):
    w = M[mat]['w']
    pz = []
    for (x, y) in [(w/2.0, w/2.0), (L-w/2.0, w/2.0), (w/2.0, A-w/2.0), (L-w/2.0, A-w/2.0)]:
        pz.append(vz('columna', 'columna', mat, 0, H, x, y))
        pz.append(chapa_h('base', 'base de amure', 'CH6', x-90, x+90, y-90, y+90, 0))
    pz += [vx('arriba', 'travesaño de arriba', mat, 0, L, w/2.0, H-w/2.0),
           vx('arriba', 'travesaño de arriba', mat, 0, L, A-w/2.0, H-w/2.0),
           vy('arribab', 'travesaño de arriba', mat, 0, A, w/2.0, H-w/2.0),
           vy('arribab', 'travesaño de arriba', mat, 0, A, L-w/2.0, H-w/2.0)]
    pz += [vy('bajo', 'travesaño de abajo', 'TC50', 0, A, w/2.0, 120),
           vy('bajo', 'travesaño de abajo', 'TC50', 0, A, L-w/2.0, 120)]
    pz.append(vx('dominadas', 'barra de dominadas', 'CR38', 0, L, A/2.0, H-60))
    for z in reparto(400, H-300, 14):
        for (cx, cy) in [(w/2.0, w/2.0), (L-w/2.0, w/2.0), (w/2.0, A-w/2.0), (L-w/2.0, A-w/2.0)]:
            pz.append(Pz('agujero', 'perforación de 25 mm', 'RD8', (cx, cy-w/2.0-1, z), (cx, cy+w/2.0+1, z),
                         kind='cil', extra={'no_lista': True}, w=26, h=26, lados=10))
    pasos = [
      ('Cortá las cuatro columnas exactamente iguales y marcá las perforaciones en las cuatro juntas, apoyadas y alineadas.', ['columna']),
      ('Agujereá las columnas de a dos, con la agujereadora a 90 grados. Un agujero torcido hace que el soporte no entre.', ['agujero']),
      ('Armá los dos pórticos: dos columnas, el travesaño de arriba y el de abajo.', ['columna','arriba','bajo']),
      ('Controlá que los dos pórticos sean gemelos y que las perforaciones queden enfrentadas.', ['bajo']),
      ('Parálos y unilos con los travesaños de arriba. Medí las diagonales de la planta.', ['arribab']),
      ('Soldá la barra de dominadas al medio, arriba.', ['dominadas']),
      ('Soldá las cuatro bases y amurá la jaula al piso con brocas de 12. No la uses sin amurar.', ['base']),
    ]
    return Plano('GY', 'Jaula de potencia %s' % med2(L, A), pz, pasos, (10, 14), 'Intermedio',
      'Jaula de sentadillas de caño %s con perforaciones cada 50 mm, barra de dominadas arriba y bases para amurar. '
      'Aguanta barra cargada y un tipo colgado sin moverse.' % M[mat]['corto'],
      'Gimnasios de garaje, boxes de crossfit chicos y gente que se armó el gimnasio en casa. Es el trabajo más caro '
      'de la categoría y el que más se busca en Marketplace.',
      HERR_PLUS + ['mecha de 25', 'nivel de burbuja'],
      ['Las perforaciones de las cuatro columnas tienen que coincidir. Marcá y agujereá las cuatro juntas, nunca de a una.',
       'Va amurada al piso o cargada con discos en la base. Una jaula suelta se vuelca con el primer fallo de una sentadilla.'],
      dims=[dict(vista='frente', tipo='v', a=400, b=450, ref=L*0.5, off=-18, lado=-1, txt='50 mm entre agujeros')],
      variante='%d x %d x %d mm · perforaciones cada 50 mm' % (L, A, H))

# ------------------------------------------------------------------ rig de entrenamiento
def rig(L=2440, A=1200, H=2740):
    pz = []
    for x in (40, L/2.0, L-40):
        for y in (40, A-40):
            pz.append(vz('columna', 'columna', 'TC80', 0, H, x, y))
            pz.append(chapa_h('base', 'base de amure', 'CH6', x-90, x+90, y-90, y+90, 0))
    for y in (40, A-40):
        pz.append(vx('viga', 'viga de arriba', 'TC80', 0, L, y, H-40))
    for x in (40, L/2.0, L-40):
        pz.append(vy('vigab', 'viga de arriba', 'TC80', 0, A, x, H-40))
    pz += [vx('dominadas', 'barra de dominadas', 'CR50', 0, L/2.0, A/2.0, H-120),
           vx('dominadas', 'barra de dominadas', 'CR50', L/2.0, L, A/2.0, H-120)]
    for x in (40, L/2.0, L-40):
        pz.append(vy('bajo', 'travesaño de abajo', 'TC50', 0, A, x, 150))
    pz += [Pz('escuadra', 'escuadra de la viga', 'PL76', (x-300, 40, H-40), (x, 40, H-340), corte='en ángulo')
           for x in (L/2.0, L)]
    pasos = [
      ('Cortá las seis columnas iguales y marcá todas las perforaciones de una sola vez.', ['columna']),
      ('Armá los tres pórticos en el piso: dos columnas, travesaño de abajo y viga de arriba.', ['columna','bajo','vigab']),
      ('Levantá el primer pórtico, apuntalalo y controlá plomo en los dos sentidos.', ['bajo']),
      ('Sumá los otros dos pórticos y unilos con las vigas largas de arriba.', ['viga']),
      ('Soldá las dos barras de dominadas entre pórticos.', ['dominadas']),
      ('Soldá las escuadras de planchuela en las esquinas de arriba: son las que le sacan el movimiento lateral.', ['escuadra']),
      ('Amurá las seis bases al piso con brocas de 12 y recién ahí soldá todos los cordones a fondo.', ['base']),
    ]
    return Plano('GY', 'Rig de entrenamiento %s' % med2(L, A), pz, pasos, (16, 24), 'Avanzado',
      'Estructura de seis columnas con dos estaciones, barras de dominadas y vigas de caño 80 x 80. Es la estructura '
      'que convierte un garaje en un box.',
      'Boxes de crossfit, gimnasios de barrio y clubes. Es un trabajo de presupuesto grande: si cerrás uno al mes, '
      'con eso solo vivís.',
      HERR_PLUS + ['mecha de 25', 'nivel de burbuja', 'puntales'],
      ['Nunca lo armes parado desde cero. Armá los pórticos en el piso y levantalos: es más rápido, más seguro y sale a plomo.',
       'Va amurado al piso sí o sí. Y si el piso es carpeta sobre contrapiso flojo, hay que anclar con químico.'],
      variante='%d x %d x %d mm · 2 estaciones' % (L, A, H))

# ------------------------------------------------------------------ banco plano
def banco_plano(regulable=False, L=1100, A=300, H=450):
    pz = marco_xy('marco', 'marco del asiento', 'TC50', 0, L, 0, A, H-25)
    pz += [vz('pata', 'pata', 'TC50', 0, H-50, 60, A/2.0),
           vz('pata', 'pata', 'TC50', 0, H-50, L-60, A/2.0),
           vy('piso', 'patín del piso', 'TC50', -80, A+80, 60, 25),
           vy('piso', 'patín del piso', 'TC50', -80, A+80, L-60, 25)]
    pz.append(chapa_h('asiento', 'tabla del asiento', 'FEN18', 0, L, -20, A+20, H-25, extra={'sin_vista': ('planta',)}))
    if regulable:
        pz += [Pz('crem', 'cremallera de respaldo', 'PL50', (L-350, A/2.0, H-30), (L-350, A/2.0, H+250), corte='recto'),
               vy('eje', 'eje de la bisagra', 'RD16', 0, A, L-120, H-20)]
    pasos = [
      ('Armá el marco del asiento a 45 y escuadralo.', ['marco','marcob']),
      ('Soldá las dos patas centradas, bien a plomo.', ['pata']),
      ('Soldá los dos patines del piso: dan el ancho de apoyo y evitan que el banco se tumbe.', ['piso']),
      ('Controlá apoyando el banco en el piso con peso arriba antes de soldar a fondo.', ['piso']),
    ] + ([('Soldá el eje de la bisagra y la cremallera del respaldo, probando las cuatro posiciones.', ['crem','eje'])] if regulable else []) + [
      ('Rematá todos los cordones, pintá y amurá la tabla con espuma y tapizado desde abajo.', ['asiento']),
    ]
    return Plano('GY', 'Banco %s de musculación' % ('regulable' if regulable else 'plano'), pz, pasos,
      (5, 7) if regulable else (3, 5), 'Intermedio' if regulable else 'Principiante',
      'Banco de press de caño 50 x 50 con patines anchos de apoyo%s. La tabla la hacés con fenólico de 18, espuma de '
      'alta densidad y cuerina.' % (' y respaldo regulable en cuatro posiciones' if regulable else ''),
      'Gimnasios de casa y gente que compró la barra pero no tiene dónde acostarse. Es un trabajo chico que se puede '
      'hacer en serie y vender con el rack.',
      HERR_BASE + ['agujereadora'],
      ['Los patines del piso tienen que ser más anchos que el banco. Si los hacés al ras, el banco se tumba de costado.',
       'La altura de 450 mm no se toca: es la que deja los pies apoyados. Más alto, no sirve para press.'],
      variante='1.100 x 300 x 450 mm%s' % (' · 4 posiciones' if regulable else ''))

# ------------------------------------------------------------------ rack de discos
def rack_discos(L=900, A=400, H=900):
    pz = []
    for y in (30, A-30):
        pz += [vz('parante', 'parante', 'TC50', 0, H, 30, y),
               vz('parante', 'parante', 'TC50', 0, H, L-30, y),
               vx('base', 'larguero de la base', 'TC50', 0, L, y, 25)]
    pz += [vx('arriba', 'travesaño de arriba', 'TC50', 0, L, 30, H-25),
           vx('arriba', 'travesaño de arriba', 'TC50', 0, L, A-30, H-25),
           vy('cost', 'travesaño del costado', 'TC50', 0, A, 30, H-25),
           vy('cost', 'travesaño del costado', 'TC50', 0, A, L-30, H-25)]
    for x in reparto(160, L-160, 3):
        pz.append(Pz('perno', 'perno de discos', 'CR50', (x, A/2.0, 180), (x, A/2.0, 180+320), corte='recto'))
        pz.append(chapa_h('plato', 'plato del perno', 'CH6', x-70, x+70, A/2.0-70, A/2.0+70, 170))
    pz.append(vx('barra', 'soporte de barras', 'CR50', 0, L, A-30, H-120))
    pasos = [
      ('Armá los dos laterales con parantes y largueros de base.', ['parante','base']),
      ('Unilos arriba con los travesaños y controlá las diagonales.', ['arriba','cost']),
      ('Marcá la posición de los tres pernos y soldá los platos de chapa.', ['plato']),
      ('Soldá los tres pernos a 90 grados: si quedan caídos, los discos se salen.', ['perno']),
      ('Soldá el soporte de barras atrás, arriba.', ['barra']),
      ('Rematá todo y pintá. Este trabajo se carga con 200 kg: no dejes ningún punto sin cordón.', ['barra']),
    ]
    return Plano('GY', 'Rack de discos y barras %s' % med2(L, A), pz, pasos, (5, 7), 'Principiante',
      'Rack de tres pernos para discos olímpicos y soporte de barras atrás. Es el complemento obligatorio de cualquier '
      'jaula y el que te compran siempre después.',
      'El mismo que te compró el rack o la jaula. Ofrecelo en el mismo presupuesto: casi nadie lo rechaza.',
      HERR_BASE,
      ['Los pernos van perfectamente horizontales. Con 2 grados de caída, los discos se van solos con el movimiento.',
       'El plato de chapa abajo de cada perno no es decoración: reparte el peso y evita que el perno se arranque.'],
      variante='%d x %d x %d mm · 3 pernos de 2"' % (L, A, H))

# ------------------------------------------------------------------ soporte de sentadillas
def squat_stand(L=1200, A=700, H=1800):
    pz = []
    for x in (60, L-60):
        pz.append(vz('columna', 'columna', 'TC60', 0, H, x, A/2.0))
        pz.append(vy('base', 'patín de la base', 'TC60', 0, A, x, 30))
        pz.append(Pz('escuadra', 'escuadra de la base', 'PL50', (x, A/2.0, 400), (x, A-80, 60), corte='en ángulo'))
        pz.append(Pz('escuadra', 'escuadra de la base', 'PL50', (x, A/2.0, 400), (x, 80, 60), corte='en ángulo'))
    for z in reparto(900, H-200, 10):
        pz += [Pz('agujero', 'perforación de 25 mm', 'RD8', (x, A/2.0-32, z), (x, A/2.0+32, z),
                  kind='cil', extra={'no_lista': True}, w=26, h=26, lados=10) for x in (60, L-60)]
    pz.append(vx('union', 'travesaño de unión', 'TC50', 0, L, A/2.0, 300))
    pasos = [
      ('Cortá las dos columnas iguales y marcá las perforaciones en las dos juntas.', ['columna']),
      ('Agujereá de a dos columnas apoyadas, para que los agujeros queden enfrentados.', ['agujero']),
      ('Soldá el patín de la base abajo de cada columna, a escuadra.', ['base']),
      ('Soldá las dos escuadras de planchuela de cada columna: son las que impiden que se vaya para adelante.', ['escuadra']),
      ('Uní las dos columnas con el travesaño bajo y controlá que queden paralelas.', ['union']),
      ('Soldá todo, pintá y probá con la barra apoyada antes de entregar.', ['union']),
    ]
    return Plano('GY', 'Soporte de sentadillas de %d mm' % H, pz, pasos, (6, 8), 'Intermedio',
      'Dos columnas con base en T y perforaciones cada 50 mm, unidas por un travesaño bajo. Es la versión barata de '
      'la jaula: ocupa la mitad del lugar y hace el 80 % del trabajo.',
      'El que entrena en el garaje y no tiene lugar para una jaula. Se vende más que la jaula justamente por el precio '
      'y porque entra en cualquier lado.',
      HERR_PLUS + ['mecha de 25'],
      ['Las escuadras van hacia adelante, del lado donde se apoya la barra. Si las ponés atrás, el soporte se tumba.',
       'Sin el travesaño bajo, las dos columnas trabajan separadas y se abren. No lo saques "para que entre la barra": va abajo.'],
      variante='%d x %d x %d mm · perforaciones cada 50 mm' % (L, A, H))

# ------------------------------------------------------------------ barra de dominadas de pared
def dominadas_pared(L=1200, A=600, H=600):
    pz = []
    for x in (60, L-60):
        pz.append(vz('parante', 'parante de pared', 'TC50', 0, H, x, 25))
        pz.append(Pz('brazo', 'brazo', 'TC50', (x, 50, H-25), (x, A, H-25), corte='recto'))
        pz.append(Pz('escuadra', 'escuadra del brazo', 'PL50', (x, A-80, H-50), (x, 50, 150), corte='en ángulo'))
        pz.append(chapa_h('placa', 'placa de amure', 'CH6', x-80, x+80, 0, 10, 0, extra={'lista': (160, 300)}))
    pz.append(vx('barra', 'barra', 'CR38', -100, L+100, A-40, H-25))
    pasos = [
      ('Cortá los dos parantes y las dos placas de amure.', ['parante','placa']),
      ('Soldá cada placa al parante, a escuadra y centrada.', ['placa']),
      ('Soldá el brazo a 90 grados del parante: medí, no lo hagas a ojo.', ['brazo']),
      ('Soldá la escuadra en diagonal: es la que aguanta todo el peso del que se cuelga.', ['escuadra']),
      ('Soldá la barra de caño redondo pasante, con 100 mm de vuelo por lado.', ['barra']),
      ('Amurá a la pared con cuatro brocas de 12 por placa, en pared de material. Probala colgándote vos antes de entregarla.', ['placa']),
    ]
    return Plano('GY', 'Barra de dominadas de pared de %s' % metros(L), pz, pasos, (3, 4), 'Principiante',
      'Dos brazos amurados a la pared con barra de caño de 1 1/2". Media jornada de trabajo, poco material y se vende '
      'muy bien porque la alternativa comprada se dobla.',
      'Gimnasios de casa, garajes y departamentos con pared de material. Es el trabajo chico ideal para vender por el barrio.',
      HERR_PLUS,
      ['Va en pared de ladrillo u hormigón, nunca en tabique de durlock. Si el cliente tiene durlock, no lo hagas: se cae con él colgado.',
       'La escuadra en diagonal no es opcional. Sin ella, el brazo se dobla hacia abajo en el primer mes.'],
      variante='%d x %d mm · barra de 1 1/2"' % (L, A))

# ------------------------------------------------------------------ torre de mancuernas
def torre_mancuernas(L=1000, A=450, H=800):
    pz = []
    for y in (30, A-30):
        pz += [vz('parante', 'parante', 'TC40', 0, H, 30, y),
               vz('parante', 'parante', 'TC40', 0, H, L-30, y),
               vx('base', 'larguero de la base', 'TC40', 0, L, y, 20)]
    for z, prof in zip(reparto(220, H-60, 3), (0, 60, 120)):
        pz += [vx('bandeja', 'larguero de bandeja', 'TC30', 0, L, 30+prof*0.3, z),
               vx('bandeja', 'larguero de bandeja', 'TC30', 0, L, A-30, z)]
        for x in reparto(80, L-80, 5):
            pz.append(vy('tope', 'tope de bandeja', 'RD12', 30, A-30, x, z+25))
    pz.append(vx('arriba', 'travesaño de arriba', 'TC40', 0, L, 30, H-20))
    pasos = [
      ('Armá los dos laterales con parantes y largueros de base.', ['parante','base']),
      ('Marcá las tres alturas de bandeja en los cuatro parantes al mismo tiempo.', ['parante']),
      ('Soldá los largueros de cada bandeja, con caída hacia atrás para que las mancuernas no se vengan.', ['bandeja']),
      ('Soldá los topes de redondo de cada bandeja, repartidos.', ['tope']),
      ('Cerrá con el travesaño de arriba y controlá las diagonales.', ['arriba']),
      ('Soldá todo a fondo: cargada, esta torre pasa los 150 kg.', ['arriba']),
    ]
    return Plano('GY', 'Torre de mancuernas %s' % med2(L, A), pz, pasos, (5, 7), 'Principiante',
      'Tres bandejas con caída hacia atrás y topes de redondo, para seis u ocho pares de mancuernas. Ocupa un metro '
      'de pared y ordena todo el gimnasio.',
      'Gimnasios chicos, estudios de entrenamiento funcional y casas. Se vende junto con el banco y el rack.',
      HERR_BASE,
      ['Las bandejas van con caída hacia atrás, no planas. Plana, la mancuerna se viene al piso con cualquier golpe.',
       'Los topes de redondo van arriba del larguero del frente, no abajo: si no, no frenan nada.'],
      variante='%d x %d x %d mm · 3 bandejas' % (L, A, H))
