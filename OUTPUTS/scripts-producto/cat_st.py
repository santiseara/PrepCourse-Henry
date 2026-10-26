# -*- coding: utf-8 -*-
"""ST · Cocheras, estructuras y techos."""
from engine import *
from comun import *

P = []

# ------------------------------------------------------------------ pérgola
def pergola(L, A, H=2400):
    pz = []
    for (x, y) in [(50, 50), (L-50, 50), (50, A-50), (L-50, A-50)]:
        pz.append(vz('columna', 'columna', 'TC100', 0, H, x, y))
        pz.append(chapa_h('base', 'base de amure', 'CH6', x-110, x+110, y-110, y+110, 0))
    pz += [vx('viga', 'viga principal', 'TR12060', 0, L, 50, H-30),
           vx('viga', 'viga principal', 'TR12060', 0, L, A-50, H-30)]
    for x in reparto(150, L-150, 7):
        pz.append(vy('listón', 'listón del techo', 'TR6040', 0, A, x, H+10))
    pz += [Pz('escuadra', 'escuadra de la columna', 'PL76', (x, y, H-330), (x + (300 if x < L/2 else -300), y, H-30),
              corte='en ángulo') for x in (50, L-50) for y in (50, A-50)]
    pasos = [
      ('Replanteá en el piso los cuatro puntos de las columnas y controlá las diagonales antes de agujerear nada.', ['base']),
      ('Soldá la base de amure a cada columna, perfectamente a escuadra.', ['columna','base']),
      ('Amurá las cuatro columnas con brocas de 12 y apuntalalas a plomo en los dos sentidos.', ['base']),
      ('Soldá las dos vigas principales arriba, de columna a columna, con nivel.', ['viga']),
      ('Soldá las ocho escuadras de planchuela: son las que le sacan el movimiento a toda la estructura.', ['escuadra']),
      ('Repartí los siete listones del techo cada %d mm y soldalos arriba de las vigas.' % int(L/8), ['listón']),
      ('Dos manos de antióxido y dos de esmalte. Esto vive bajo sol y lluvia todo el año.', ['listón']),
    ]
    return Plano('ST', 'Pérgola %s' % med2(L, A), pz, pasos, (14, 20), 'Intermedio',
      'Pérgola de cuatro columnas de caño 100 x 100, vigas de 120 x 60 y listones repartidos arriba. Se le puede '
      'sumar policarbonato, caña o una planta: la estructura es la misma.',
      'Casas con patio, quinchos, bares con vereda y clubes. Es un trabajo de presupuesto alto que casi siempre '
      'arranca con "¿cuánto me sale una pérgola?" por WhatsApp. Cotizala con la visita incluida.',
      HERR_PLUS + ['nivel de burbuja', 'brocas de 12', 'puntales'],
      ['Las bases van amuradas a una platea o a un dado de hormigón. Sobre baldosa suelta, el primer viento fuerte la levanta.',
       'Nunca sueldes las vigas de arriba con las columnas solo apuntaladas de un lado: ponelas a plomo en los dos '
       'sentidos y recién ahí soldá.'],
      variante='%d x %d x %d mm · 7 listones' % (L, A, H))

# ------------------------------------------------------------------ cochera
def cochera(L, A, alto_bajo=2300, alto_alto=2750):
    pz = []
    for x in (60, L-60):
        pz.append(vz('columna', 'columna alta', 'TC100', 0, alto_alto, x, 60))
        pz.append(vz('columna2', 'columna baja', 'TC100', 0, alto_bajo, x, A-60))
        pz.append(chapa_h('base', 'base de amure', 'CH6', x-110, x+110, -50, 170, 0))
        pz.append(chapa_h('base', 'base de amure', 'CH6', x-110, x+110, A-170, A+50, 0))
        pz.append(Pz('cabio', 'cabio', 'TR12060', (x, 0, alto_alto-30), (x, A, alto_bajo-30), corte='en ángulo'))
    for i, t in enumerate(reparto(0.05, 0.95, 5)):
        y = A*t; z = alto_alto - 30 + (alto_bajo - alto_alto)*t + 70
        pz.append(vx('correa', 'correa', 'C100', 0, L, y, z))
    pz += [Pz('escuadra', 'escuadra de la columna', 'PL76', (x, 60, alto_alto-400), (x + (350 if x < L/2 else -350), 60, alto_alto-30),
              corte='en ángulo') for x in (60, L-60)]
    pz.append(chapa_h('chapa', 'chapa del techo (se compra a medida)', 'CH16', 0, L, 0, A, alto_alto+40,
                      extra={'no_lista': True, 'sin_vista': ('planta',)}))
    pasos = [
      ('Replanteá las cuatro columnas en el piso y controlá diagonales: una cochera fuera de escuadra se nota desde la vereda.', ['base']),
      ('Soldá las bases a las columnas y amurá las cuatro, apuntaladas y a plomo.', ['columna','columna2','base']),
      ('Soldá los dos cabios inclinados, de la columna alta a la baja. Esa pendiente es la que hace que el agua corra.', ['cabio']),
      ('Soldá las escuadras de las columnas altas.', ['escuadra']),
      ('Repartí las cinco correas sobre los cabios, perpendiculares, cada %d mm.' % int(A/5), ['correa']),
      ('Dos manos de antióxido antes de poner la chapa: una vez techada no llegás más.', ['correa']),
      ('Amurá la chapa con tornillos autoperforantes y arandela de goma, uno cada dos ondas en los apoyos.', ['chapa']),
    ]
    return Plano('ST', 'Cochera a un agua %s' % med2(L, A), pz, pasos, (18, 26), 'Avanzado',
      'Cochera de cuatro columnas de 100 x 100 con cabios inclinados y cinco correas de perfil C. Pendiente de %d mm '
      'para que el agua corra sola. La chapa se compra cortada a medida.' % (alto_alto - alto_bajo),
      'Casas, consorcios y comercios. Es el trabajo de mayor presupuesto que podés hacer con herramientas de taller '
      'común, y siempre trae el pedido del vecino de al lado.',
      HERR_PLUS + ['nivel de burbuja', 'brocas de 12', 'puntales', 'escalera'],
      ['La pendiente mínima es 5 %. Con menos, el agua se queda, entra por los tornillos y te llaman por goteras.',
       'Nunca trabajes solo levantando cabios de 5 metros. Es el momento en que pasan los accidentes.'],
      variante='%d x %d mm · un agua, pendiente de %d mm' % (L, A, alto_alto - alto_bajo))

# ------------------------------------------------------------------ escalera recta
def escalera(H, L, n):
    paso = L/float(n)
    alza = H/float(n)
    pz = []
    for y in (0, 900):
        pz.append(Pz('zanca', 'zanca', 'C120', (0, y, 0), (L, y, H), corte='en ángulo'))
    for i in range(1, n+1):
        x = paso*i; z = alza*i
        pz.append(chapa_h('peldaño', 'peldaño', 'CHA3', x-paso+20, x-20, 0, 900, z-30,
                          extra={'lista': (int(paso-40), 900)}))
        pz.append(vy('frente', 'contrahuella', 'PL50', 0, 900, x-paso+20, z-60))
    pz.append(vz('poste', 'poste de arranque', 'TC50', 0, 1000, 0, 900))
    pz.append(vz('poste', 'poste de llegada', 'TC50', H, H+1000, L, 900))
    pz.append(Pz('pasamano', 'pasamanos', 'CR38', (0, 900, 950), (L, 900, H+950), corte='en ángulo'))
    for i in range(1, n, 2):
        x = paso*i; z = alza*i
        pz.append(Pz('baranda', 'barrote de la baranda', 'RD12', (x, 900, z), (x, 900, z+900), corte='recto'))
    pasos = [
      ('Marcá las dos zancas juntas: apoyalas una sobre la otra y marcá los %d escalones de una sola vez.' % n, ['zanca']),
      ('Cortá los ángulos de arranque y de llegada de las dos zancas con la misma plantilla.', ['zanca']),
      ('Apoyá las zancas paralelas sobre caballetes, separadas 900 mm, y controlá que las marcas queden enfrentadas.', ['zanca']),
      ('Soldá las contrahuellas de planchuela de abajo hacia arriba, controlando con el nivel escalón por escalón.', ['frente']),
      ('Puntéa los peldaños de chapa antideslizante sobre las contrahuellas.', ['peldaño']),
      ('Soldá los dos postes y el pasamanos siguiendo la pendiente de la zanca.', ['poste','pasamano']),
      ('Soldá los barrotes de la baranda y rematá todo. Antes de amurarla, probá subiendo: el escalón se siente, no se mide.', ['baranda']),
    ]
    return Plano('ST', 'Escalera recta de %d escalones' % n, pz, pasos, (16, 24), 'Avanzado',
      'Escalera de dos zancas de perfil C con peldaños de chapa antideslizante, contrahuella de planchuela y baranda '
      'con pasamanos. Alzada de %d mm y pedada de %d mm: la combinación que se sube sin pensarla.' % (int(alza), int(paso)),
      'Entrepisos, galpones, locales con altillo y casas en obra. Es un trabajo caro, que pocos hacen bien y que '
      'siempre tiene apuro: el que necesita la escalera ya tiene el entrepiso hecho.',
      HERR_CHAPA + ['nivel de burbuja', 'escuadra grande'],
      ['Alzada y pedada tienen que ser todas iguales. Una diferencia de 10 mm en un escalón hace tropezar: es el '
       'reclamo más común de una escalera.',
       'Las dos zancas se marcan juntas. Si marcás una y después la otra, los peldaños te quedan torcidos y se ve de lejos.'],
      dims=[dict(vista='frente', tipo='v', a=0, b=alza, ref=paso*0.5, off=-16, lado=-1, txt='alzada %d mm' % int(alza))],
      variante='%d mm de alto · %d escalones · ancho 900 mm' % (H, n))

# ------------------------------------------------------------------ baranda de galería
def baranda_galeria(L=3000, H=1000):
    pz = [vx('pasamano', 'pasamanos', 'TR6040', 0, L, 0, H-20),
          vx('bajo', 'travesaño bajo', 'TR4020', 0, L, 0, 120)]
    for x in reparto(40, L-40, 4):
        pz.append(vz('parante', 'parante', 'TC50', 0, H, x, 0))
        pz.append(chapa_h('base', 'base de amure', 'CH6', x-70, x+70, -70, 70, 0))
    for x in interiores(0, L, 21):
        pz.append(vz('barrote', 'barrote', 'TC20', 120, H-20, x, 0))
    pasos = [
      ('Cortá los barrotes todos iguales con tope en la sierra: en una baranda, un barrote distinto se ve a 10 metros.', ['barrote']),
      ('Apoyá el pasamanos y el travesaño bajo paralelos sobre la mesa, a la separación exacta.', ['pasamano','bajo']),
      ('Marcá la posición de los barrotes en los dos al mismo tiempo, con una plantilla.', ['barrote']),
      ('Puntéa los barrotes de los extremos, controlá escuadra y después soldá todos los del medio.', ['barrote']),
      ('Soldá los parantes con sus bases.', ['parante','base']),
      ('Desbastá todos los puntos que quedan a la vista: una baranda se toca con la mano todos los días.', ['base']),
    ]
    return Plano('ST', 'Baranda de galería de %s' % metros(L), pz, pasos, (6, 9), 'Principiante',
      'Baranda de 1 m de alto con barrotes cada 110 mm (la separación que piden las normas para que no pase la cabeza '
      'de un chico), pasamanos de caño rectangular y bases para amurar.',
      'Galerías, balcones, escaleras y entrepisos. Es un trabajo repetitivo que se vende por metro: cotizá por metro '
      'lineal y hacete una plantilla antes del primer tramo.',
      HERR_BASE + ['agujereadora', 'brocas de 10'],
      ['La separación entre barrotes no pasa de 110 mm. Es seguridad, y es lo primero que mira un arquitecto.',
       'Hacete la plantilla de posición de barrotes. Diez metros de baranda a ojo se nota en la primera foto.'],
      variante='%d x %d mm · barrotes cada 110 mm' % (L, H))

# ------------------------------------------------------------------ alero de entrada
def alero(L=2000, A=1200, H=2400):
    pz = [vx('muro', 'perfil contra el muro', 'C100', 0, L, 0, H)]
    for x in (40, L-40):
        pz.append(Pz('cabio', 'cabio', 'TR6040', (x, 0, H), (x, A, H-180), corte='en ángulo'))
        pz.append(Pz('tensor', 'tensor', 'PL50', (x, 0, H-700), (x, A-200, H-150), corte='en ángulo'))
    pz.append(Pz('cabio', 'cabio del medio', 'TR6040', (L/2.0, 0, H), (L/2.0, A, H-180), corte='en ángulo'))
    for i, t in enumerate(reparto(0.1, 0.95, 3)):
        pz.append(vx('correa', 'correa', 'TR4020', 0, L, A*t, H - 180*t + 50))
    pz += [chapa_h('placa', 'placa de amure al muro', 'CH6', x-70, x+70, -8, 8, H-80, extra={'lista': (140, 160)})
           for x in (80, L/2.0, L-80)]
    pasos = [
      ('Amurá el perfil contra el muro con brocas de 12, perfectamente nivelado: de eso depende todo lo demás.', ['muro','placa']),
      ('Soldá los tres cabios al perfil del muro, con la caída hacia afuera.', ['cabio']),
      ('Soldá los dos tensores en diagonal: son los que sostienen el voladizo.', ['tensor']),
      ('Repartí las tres correas sobre los cabios.', ['correa']),
      ('Pintá todo antes de techar.', ['correa']),
      ('Amurá la chapa o el policarbonato con tornillos y arandela de goma.', ['correa']),
    ]
    return Plano('ST', 'Alero de entrada de %s' % metros(L), pz, pasos, (6, 9), 'Intermedio',
      'Alero en voladizo de 1,20 m sobre la puerta: tres cabios, dos tensores en diagonal y tres correas. '
      'Todo el secreto está en el amure al muro y en los tensores.',
      'Casas, locales, entradas de edificio y accesos de galpón. Es un trabajo chico que resuelve un problema evidente: '
      'si llueve, el cliente se moja mientras busca la llave.',
      HERR_PLUS + ['nivel de burbuja', 'brocas de 12', 'escalera'],
      ['Amurá a ladrillo macizo u hormigón. En ladrillo hueco hay que pasar de lado a lado con varilla roscada, no con tarugo.',
       'Sin los tensores diagonales, el alero se vence hacia abajo en el primer año. No los saques "porque se ven".'],
      variante='%d x %d mm · voladizo con tensores' % (L, A))

# ------------------------------------------------------------------ invernadero
def invernadero(L=6000, A=3000, H=2000, Hc=2600):
    pz = []
    for x in reparto(0, L, 5):
        pz += [vz('columna', 'columna', 'TC50', 0, H, x, 25),
               vz('columna', 'columna', 'TC50', 0, H, x, A-25),
               Pz('cabio', 'cabio', 'TC40', (x, 0, H), (x, A/2.0, Hc), corte='en ángulo'),
               Pz('cabio', 'cabio', 'TC40', (x, A, H), (x, A/2.0, Hc), corte='en ángulo')]
    pz.append(vx('cumbrera', 'cumbrera', 'TC50', 0, L, A/2.0, Hc-25))
    for y in (25, A-25):
        pz.append(vx('viga', 'viga lateral', 'TC50', 0, L, y, H-25))
    for t in (0.5,):
        pz.append(vx('correa', 'correa', 'TR4020', 0, L, A*0.25, (H+Hc)/2.0))
        pz.append(vx('correa', 'correa', 'TR4020', 0, L, A*0.75, (H+Hc)/2.0))
    pz += [Pz('cruz', 'cruz de San Andrés', 'PL38', (0, 25, 0), (L*0.25, 25, H), corte='en ángulo'),
           Pz('cruz', 'cruz de San Andrés', 'PL38', (L*0.25, 25, 0), (0, 25, H), corte='en ángulo')]
    pasos = [
      ('Replanteá las diez columnas en el piso con hilo y escuadra 3-4-5. Un invernadero torcido no se puede plastificar.', ['columna']),
      ('Hormigoná o amurá las columnas, apuntaladas y a plomo.', ['columna']),
      ('Soldá las dos vigas laterales que atan las columnas a 2 m.', ['viga']),
      ('Armá los pares de cabios en el piso y subilos de a uno, soldando a la cumbrera.', ['cabio','cumbrera']),
      ('Soldá las correas de cada agua.', ['correa']),
      ('Soldá la cruz de San Andrés en un lateral.', ['cruz']),
      ('Pintá todo de blanco: el blanco refleja y el nylon dura el doble que sobre hierro negro al sol.', ['cruz']),
    ]
    return Plano('ST', 'Invernadero de %s' % med2(L, A), pz, pasos, (20, 28), 'Intermedio',
      'Estructura de invernadero a dos aguas de 6 x 3 m, con diez columnas, cabios, cumbrera y correas. Se cubre con '
      'nylon de 150 micrones, que compra el cliente.',
      'Quintas, viveros, escuelas rurales y huertas familiares. Es un trabajo de muchas piezas iguales: hacete la '
      'plantilla del par de cabios y el resto es repetición.',
      HERR_BASE + ['nivel de burbuja', 'escuadra grande'],
      ['Pintá de blanco y lijá cualquier filo. El nylon se corta en el primer punto de soldadura que quedó con rebaba.',
       'Dejá los extremos previstos para poner la puerta antes de cerrar: después del nylon no se corrige nada.'],
      variante='%d x %d mm · dos aguas' % (L, A))

# ------------------------------------------------------------------ escalera de gato
def escalera_gato(H=3500, A=500):
    pz = [vz('larguero', 'larguero', 'TC50', 0, H, 0, 0),
          vz('larguero', 'larguero', 'TC50', 0, H, 0, A)]
    for z in reparto(300, H-200, 12):
        pz.append(vy('peldaño', 'peldaño', 'RD20', 0, A, 0, z))
    for z in (400, H-400):
        pz += [chapa_v('amure', 'soporte de amure', 'CH6', -200, 10, 0, z-50, z+50, extra={'lista': (210, 100)}),
               chapa_v('amure', 'soporte de amure', 'CH6', -200, 10, A, z-50, z+50, extra={'lista': (210, 100)})]
    pasos = [
      ('Cortá los dos largueros iguales y marcá los doce peldaños en los dos al mismo tiempo.', ['larguero']),
      ('Apoyá los largueros paralelos a 500 mm y puntéa el primer y el último peldaño.', ['peldaño']),
      ('Controlá escuadra con las diagonales y soldá el resto de los peldaños.', ['peldaño']),
      ('Soldá los cuatro soportes de amure, dos arriba y dos abajo.', ['amure']),
      ('Rematá el cordón alrededor de cada peldaño: acá se cuelga una persona.', ['peldaño']),
      ('Amurá con brocas de 12, separada 200 mm de la pared para que entre el pie.', ['amure']),
    ]
    return Plano('ST', 'Escalera de gato de %s' % metros(H), pz, pasos, (4, 6), 'Principiante',
      'Escalera fija de pared con doce peldaños de redondo de 20 y soportes de amure. Para subir al techo, al tanque '
      'o al entrepiso sin andar buscando la escalera de mano.',
      'Galpones, talleres, consorcios y casas con tanque alto. Es un trabajo chico, rápido, y lo piden cuando ya se '
      'cansaron de subir con la escalera prestada.',
      HERR_PLUS,
      ['Separada 200 mm de la pared. Al ras, no entra el pie y la escalera no sirve.',
       'El peldaño de redondo se suelda con cordón completo alrededor. Medio cordón se parte justo cuando hay alguien arriba.'],
      variante='%d mm de alto · 12 peldaños · ancho %d mm' % (H, A))
