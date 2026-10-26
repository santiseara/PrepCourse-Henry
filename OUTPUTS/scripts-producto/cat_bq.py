# -*- coding: utf-8 -*-
"""BQ · Parrillas, ahumadores y fogoneros."""
from engine import *
from comun import *

P = []

# ------------------------------------------------------------------ fogonero hexagonal
def fogonero_hex(across, alto, mat_pared, horas):
    R = across/2.0
    V = [(R*math.cos(math.radians(60*i)), R*math.sin(math.radians(60*i))) for i in range(6)]
    t = M[mat_pared]['t']
    pz = []
    for i in range(6):
        a, b = V[i], V[(i+1) % 6]
        pz.append(Pz('pared', 'panel del lateral', mat_pared, (a[0], a[1], alto/2.0), (b[0], b[1], alto/2.0),
                     w=t, h=alto, corte='a escuadra'))
        pz.append(Pz('aro', 'aro de arriba', 'PL50', (a[0], a[1], alto+3), (b[0], b[1], alto+3),
                     corte='30 grados', w=50, h=6))
    for i in (0, 2, 4):
        a = V[i]
        pz.append(vz('pata', 'pata', 'TC40', -120, 60, a[0]*0.86, a[1]*0.86))
        pz.append(Pz('patin', 'patín de la pata', 'PL50', (a[0]*0.86-80, a[1]*0.86, -120), (a[0]*0.86+80, a[1]*0.86, -120), corte='recto'))
    pz.append(Pz('piso', 'piso (de esta chapa sale el hexágono)', mat_pared, (0, 0, -t), (0, 0, 0),
                 kind='cil', w=2*R*0.985, h=2*R*0.985, lados=6,
                 extra={'lista': (round(2*R*0.87), round(2*R*0.87)), 'sin_vista': ('planta',)}))
    pz += [vx('parrilla', 'varilla de la parrilla', 'PL38', -R*0.70, R*0.70, y, alto+12)
           for y in reparto(-R*0.42, R*0.42, 7)]
    pasos = [
      ('Cortá los seis paneles iguales y marcá los 30 grados de cada canto: ese ángulo es el que cierra el hexágono.', ['pared']),
      ('Apoyá dos paneles en el piso formando el ángulo y puntéalos arriba y abajo. Sumá los otros cuatro de a uno.', ['pared']),
      ('Cerrá el hexágono con el último panel y controlá que apoye plano sobre la mesa.', ['pared']),
      ('Apoyá el conjunto sobre la chapa del piso, marcá el hexágono, cortalo y soldalo por dentro.', ['piso']),
      ('Soldá el aro de planchuela arriba, cortado a 30 grados: es lo que le da la terminación y lo que evita que se abra con el calor.', ['aro']),
      ('Dalo vuelta y soldá las tres patas con su patín.', ['pata','patin']),
      ('Armá la parrilla de varillas apoyada arriba, suelta, para poder sacarla y limpiarla.', ['parrilla']),
    ]
    return Plano('BQ', 'Fogonero hexagonal de %d cm' % (across/10), pz, pasos, horas, 'Intermedio',
      'Fogonero de seis lados en chapa de %s mm, con aro de planchuela arriba, tres patas y parrilla apoyada. '
      'El hexágono es más fácil de cerrar que un círculo y se ve mucho mejor que un cuadrado.'
      % ('%.2f' % M[mat_pared]['t']).replace('.', ',').rstrip('0').rstrip(','),
      'Es el trabajo de regalo: casas con jardín, quinchos y campos. Se vende todo el otoño y todo el invierno, y es de '
      'los pocos que la gente compra por impulso cuando lo ve armado.',
      HERR_CHAPA + ['escuadra de ángulos'],
      ['Los cantos de los paneles van cortados a 30 grados. Si los cortás rectos, entre panel y panel te queda una luz '
       'de 4 mm por donde se escapa la ceniza.',
       'La chapa fina se quema. De 3 mm para abajo, el fogonero dura dos temporadas; con 4,75 mm dura años.'],
      variante='%d mm entre puntas · %d mm de alto · %s' % (across, alto, M[mat_pared]['corto']))

# ------------------------------------------------------------------ fogonero cuadrado
def fogonero_cuad(L=700, alto=350):
    pz = []
    for (x1, x2, y) in [(0, L, 0), (0, L, L)]:
        pz.append(chapa_v('pared', 'panel del lateral', 'CH3', x1, x2, y, 0, alto))
    for x in (0, L):
        pz.append(chapa_vy('pared', 'panel del lateral', 'CH3', 0, L, x, 0, alto))
    pz.append(chapa_h('piso', 'piso', 'CH3', 0, L, 0, L, -3, extra={'sin_vista': ('planta',)}))
    pz += marco_xy('aro', 'aro de arriba', 'AN30', -10, L+10, -10, L+10, alto+15)
    for (x, y) in [(60, 60), (L-60, 60), (60, L-60), (L-60, L-60)]:
        pz.append(vz('pata', 'pata', 'TC40', -200, 40, x, y))
    pz += [vx('parrilla', 'varilla de la parrilla', 'PL38', 20, L-20, y, alto+40)
           for y in reparto(80, L-80, 6)]
    pasos = [
      ('Cortá las cuatro paredes y el piso. Si la gillotina de la casa de hierros te corta la chapa, aprovechá: es más preciso que la amoladora.', ['pared']),
      ('Puntéa dos paredes enfrentadas al piso, a escuadra.', ['piso','pared']),
      ('Cerrá con las otras dos y soldá los cuatro cantos por adentro, con cordón corrido.', ['pared']),
      ('Soldá el aro de ángulo arriba: tapa el canto de la chapa y le da rigidez.', ['aro']),
      ('Dalo vuelta y soldá las cuatro patas.', ['pata']),
      ('Armá la parrilla suelta de planchuela y hacé dos o tres agujeros de 12 mm en el piso para que drene el agua.', ['parrilla']),
    ]
    return Plano('BQ', 'Fogonero cuadrado de %d cm' % (L/10), pz, pasos, (3, 5), 'Principiante',
      'El fogonero más simple de la biblioteca: cuatro chapas, un piso, un aro de ángulo y cuatro patas. Es el trabajo '
      'ideal para la primera venta, porque sale en media jornada y no tiene ningún corte difícil.',
      'Casas con patio, quinchos y campings. En otoño se vende solo. Hacé dos o tres y tenelos armados: este se vende '
      'cuando el cliente lo ve, no cuando se lo describís.',
      HERR_CHAPA,
      ['Acordate de los agujeros de drenaje en el piso. Sin eso, junta agua de lluvia y se pudre desde adentro.',
       'Soldá por dentro, no por fuera: el cordón a la vista en un fogonero se oxida primero y se ve mal.'],
      variante='%d x %d x %d mm · chapa de 3 mm' % (L, L, alto))

# ------------------------------------------------------------------ parrilla argentina con carro
def parrilla_carro(L, A, H, horas, nivel='Intermedio'):
    altoc = 300
    pz = marco_xy('marco', 'marco de la caja', 'TC50', 0, L, 0, A, H-25)
    pz += patas('TC50', L, A, H-50, rol='pata')
    pz += [vx('est', 'marco del estante', 'TC40', 25, L-25, 45, 250),
           vx('est', 'marco del estante', 'TC40', 25, L-25, A-45, 250),
           vy('estb', 'marco del estante', 'TC40', 50, A-50, 45, 250),
           vy('estb', 'marco del estante', 'TC40', 50, A-50, L-45, 250)]
    pz.append(chapa_h('piso', 'piso de la caja', 'CH47', 0, L, 0, A, H, extra={'sin_vista': ('planta',)}))
    pz += [chapa_v('pared', 'pared del fondo', 'CH3', 0, L, A-3, H, H+altoc),
           chapa_vy('pared', 'pared del lateral', 'CH3', 0, A, 0, H, H+altoc),
           chapa_vy('pared', 'pared del lateral', 'CH3', 0, A, L-3, H, H+altoc)]
    pz += [vx('varilla', 'varilla de la parrilla', 'PL38', 40, L-40, y, H+170) for y in reparto(60, A-100, 9)]
    pz += [vy('canal', 'canaleta de grasa', 'AN40', 40, A-100, L-60, H+160)]
    pz += [vz('manija', 'manija', 'CR25', H+40, H+300, L+30, A/2.0)]
    pz += [chapa_h('rueda', 'placa de la rueda', 'CH6', x-50, x+50, 40, 140, 0) for x in (90, L-90)]
    pz.append(chapa_h('tabla', 'tabla de apoyo', 'MAD25', -300, -10, 60, A-60, H-30))
    pasos = [
      ('Armá el marco de la caja a 45 grados y escuadralo: todo lo demás se apoya en este marco.', ['marco','marcob']),
      ('Puntéa las cuatro patas por dentro y sumá el marco del estante a 250 mm.', ['pata','est','estb']),
      ('Apoyá el piso de chapa de 4,75 y puntéalo cada 200 mm, siempre alternando lados.', ['piso']),
      ('Soldá la pared del fondo y después las dos laterales, por dentro.', ['pared']),
      ('Armá la parrilla de varillas aparte, con caída hacia la canaleta, y probá que entre y salga sin trabarse.', ['varilla','canal']),
      ('Soldá las placas de las ruedas, amurá dos ruedas con freno y soldá la manija.', ['rueda','manija']),
      ('Amurá la tabla de apoyo al costado y rematá todos los cordones que se ven.', ['tabla']),
    ]
    return Plano('BQ', 'Parrilla argentina con carro %s' % med2(L, A), pz, pasos, horas, nivel,
      'Parrilla con carro: caja de chapa de 4,75 mm sobre estructura de caño 50, paredes de 3 mm, varillas con caída '
      'a la canaleta, estante abajo y tabla de apoyo al costado. Se mueve con dos ruedas y queda firme con las otras dos patas.',
      'Es el trabajo que te piden cuando les hacés cualquier otra cosa y ven que soldás bien. Casas con patio chico, '
      'departamentos con balcón grande y quinchos sin parrilla de material.',
      HERR_CHAPA + ['nivel de burbuja'],
      ['La parrilla tiene que tener caída hacia la canaleta. Si la soldás plana, la grasa se junta en el medio y se prende fuego.',
       'El piso de la caja va de 4,75 mm como mínimo. Con 2 mm, a la tercera parrillada está deformado como una batea.'],
      dims=[dict(vista='lateral', tipo='v', a=H, b=H+altoc, ref=-A*0.5, off=16, lado=-1)],
      variante='%d x %d mm · caja de %d mm de alto' % (L, A, altoc))

# ------------------------------------------------------------------ parrilla santa maría
def santa_maria(L=1520, A=700, H=900):
    pz = marco_xy('marco', 'marco de la caja', 'TC50', 0, L, 0, A, H-25)
    pz += patas('TC50', L, A, H-50, rol='pata')
    pz.append(chapa_h('piso', 'piso de la caja', 'CH6', 0, L, 0, A, H, extra={'sin_vista': ('planta',)}))
    pz += [chapa_v('pared', 'pared de la caja', 'CH3', 0, L, A-3, H, H+250),
           chapa_vy('pared', 'pared de la caja', 'CH3', 0, A, 0, H, H+250),
           chapa_vy('pared', 'pared de la caja', 'CH3', 0, A, L-3, H, H+250)]
    for x in (40, L-40):
        pz.append(vz('columna', 'columna de la cremallera', 'TR6040', H, H+1100, x, A-60))
        pz.append(vz('crem', 'cremallera', 'PL38', H+250, H+1050, x+35, A-60))
    pz += [vx('varilla', 'varilla de la parrilla', 'PL38', 60, L-60, y, H+600) for y in reparto(100, A-160, 8)]
    pz += [vx('bastidor', 'bastidor de la parrilla', 'AN30', 40, L-40, 90, H+590),
           vx('bastidor', 'bastidor de la parrilla', 'AN30', 40, L-40, A-150, H+590),
           vy('bastidorb', 'bastidor de la parrilla', 'AN30', 90, A-150, 60, H+590),
           vy('bastidorb', 'bastidor de la parrilla', 'AN30', 90, A-150, L-60, H+590)]
    pz += [vx('travesaño', 'travesaño de arriba', 'TR6040', 0, L, A-60, H+1070),
           vz('manivela', 'eje de la manivela', 'RD16', H+1000, H+1120, L/2.0, A-60)]
    pasos = [
      ('Armá la caja: marco de caño, cuatro patas y piso de chapa de 6 mm.', ['marco','marcob','pata','piso']),
      ('Soldá las tres paredes de la caja por dentro.', ['pared']),
      ('Soldá las dos columnas atrás, bien a plomo y paralelas: si se abren 5 mm, la parrilla se traba al subir.', ['columna']),
      ('Amurá las dos cremalleras enfrentadas, a la misma altura, usando una varilla como calibre.', ['crem']),
      ('Armá el bastidor de la parrilla con ángulo y soldale las varillas con caída hacia adelante.', ['bastidor','bastidorb','varilla']),
      ('Soldá el travesaño de arriba y el eje de la manivela.', ['travesaño','manivela']),
      ('Probá todo el recorrido con la parrilla vacía antes de pintar. Tiene que subir y bajar con una sola mano.', ['manivela']),
    ]
    return Plano('BQ', 'Parrilla Santa María de %s' % metros(L), pz, pasos, (14, 18), 'Avanzado',
      'La parrilla con altura regulable: dos columnas con cremallera, bastidor que sube y baja con manivela y caja de '
      'chapa de 6 mm. Es el trabajo más caro que podés hacer en un fin de semana largo.',
      'Quinchos, casas de campo y restaurantes chicos. Es la parrilla que se publica en las revistas y la que el cliente '
      'ya vio en Pinterest: cuando te la piden, no discuten el precio, discuten la fecha.',
      HERR_CHAPA + ['nivel de burbuja', 'agujereadora'],
      ['Las dos columnas tienen que estar a plomo y paralelas. Soldalas con una varilla provisoria arriba que las ate, '
       'y sacala recién al final.',
       'La parrilla sube con el peso de la carne arriba. Probá el mecanismo cargado con 20 kg antes de entregarla.'],
      variante='%d x %d mm · altura regulable con manivela' % (L, A))

# ------------------------------------------------------------------ ahumador offset
def ahumador_offset(D=560, L=1520):
    pz = [Pz('tambor', 'tambor de 200 L', 'CH3', (0, 0, 700), (L, 0, 700), kind='cil', w=D, h=D,
             extra={'no_lista': True})]
    fx, fy, fz, fl = L+20, 0, 200, 500
    pz += [chapa_vy('firebox', 'pared de la caja de fuego', 'CH47', fy-fl/2, fy+fl/2, fx, fz, fz+fl),
           chapa_vy('firebox', 'pared de la caja de fuego', 'CH47', fy-fl/2, fy+fl/2, fx+fl, fz, fz+fl),
           chapa_v('firebox', 'pared de la caja de fuego', 'CH47', fx, fx+fl, fy-fl/2, fz, fz+fl),
           chapa_v('firebox', 'pared de la caja de fuego', 'CH47', fx, fx+fl, fy+fl/2, fz, fz+fl),
           chapa_h('fireboxt', 'tapa de la caja de fuego', 'CH47', fx, fx+fl, fy-fl/2, fy+fl/2, fz+fl),
           chapa_h('fireboxt', 'piso de la caja de fuego', 'CH47', fx, fx+fl, fy-fl/2, fy+fl/2, fz)]
    pz += [vz('pata', 'pata', 'TC50', 0, 700, x, y) for x in (150, L-150) for y in (-220, 220)]
    pz += [vx('bastidor', 'bastidor del carro', 'TC50', 100, L-100, y, 680) for y in (-220, 220)]
    pz += [vy('bastidorb', 'bastidor del carro', 'TC50', -220, 220, x, 680) for x in (150, L-150)]
    pz += [Pz('chimenea', 'chimenea', 'CR60', (120, 0, 980), (120, 0, 1500), kind='cil', w=100, h=100)]
    pz += [chapa_h('rueda', 'placa de la rueda', 'CH6', x-50, x+50, -270, -170, 0) for x in (150, L-150)]
    pz += [vx('rejilla', 'varilla de la rejilla', 'PL25', 80, L-80, y, 700) for y in reparto(-200, 200, 6)]
    pasos = [
      ('Conseguí el tambor de 200 L sin pintura por dentro y quemalo con leña antes de cortarlo.', ['tambor']),
      ('Marcá y cortá la tapa del tambor con amoladora, dejando la bisagra entera de un lado.', ['tambor']),
      ('Armá el bastidor del carro con caño de 50 y las cuatro patas.', ['bastidor','bastidorb','pata']),
      ('Apoyá el tambor sobre el bastidor y soldalo en cuatro puntos, nivelado.', ['tambor']),
      ('Armá la caja de fuego de chapa de 4,75 con sus cinco paredes y su piso, y soldala al costado del tambor con la boca de paso abajo del eje.', ['firebox','fireboxt']),
      ('Soldá la chimenea en la punta opuesta, con la boca a la altura de la rejilla, no arriba del todo.', ['chimenea']),
      ('Soldá las placas de las ruedas y armá la rejilla de varillas apoyada adentro.', ['rueda','rejilla']),
    ]
    pl = Plano('BQ', 'Ahumador offset de tambor de %s' % metros(L), pz, pasos, (18, 26), 'Avanzado',
      'Ahumador de tambor con caja de fuego al costado y chimenea opuesta. El humo entra por abajo, recorre el tambor y '
      'sale por la chimenea: esa es toda la magia, y depende de que las tres bocas estén a la altura correcta.',
      'Es el trabajo de los que ya están metidos en el asado y buscan otra cosa. Se cotiza caro, se vende por foto y se '
      'hace fama solo: el que lo prueba te manda tres clientes.',
      HERR_CHAPA + ['agujereadora', 'bisagras'],
      ['La boca de paso de la caja de fuego va abajo del eje del tambor y la chimenea arranca a la altura de la rejilla. '
       'Si la chimenea sale de arriba, el humo no recorre y te quedás con carne cruda y hollín.',
       'Nunca uses un tambor que tuvo solventes o pintura. Conseguí uno de alimentos y quemalo igual antes de usarlo.'],
      extras=[('Tambor de 200 L de chapa (usado, de alimentos)', '1 unidad', 85000),
              ('Bisagras, manijas de madera y termómetro', 'juego', 42000),
              ('Dos ruedas de 200 mm con freno', '2 unidades', 58000)],
      variante='tambor de %d x %d mm · caja de fuego de 500 mm' % (D, L))
    return pl

# ------------------------------------------------------------------ ahumador vertical
def ahumador_vertical(L=600, A=600, H=1500):
    pz = patas('AN40', L, A, 250, rol='pata')
    pz += marco_xy('marcoa', 'marco del gabinete', 'AN40', 0, L, 0, A, 250)
    pz += marco_xy('marcob', 'marco del gabinete', 'AN40', 0, L, 0, A, H)
    pz += [vz('parante', 'parante del gabinete', 'AN40', 250, H, x, y) for x in (20, L-20) for y in (20, A-20)]
    pz += [chapa_vy('pared', 'pared del gabinete', 'CH3', 0, A, 0, 250, H),
           chapa_vy('pared', 'pared del gabinete', 'CH3', 0, A, L-3, 250, H),
           chapa_v('pared', 'pared del gabinete', 'CH3', 0, L, A-3, 250, H),
           chapa_h('techo', 'techo', 'CH3', 0, L, 0, A, H)]
    pz += [chapa_v('puerta', 'puerta', 'CH3', 20, L-20, 0, 270, H-30)]
    for z in reparto(500, H-150, 4):
        pz += [vx('guia', 'guía de la bandeja', 'AN25', 25, L-25, 40, z),
               vx('guia', 'guía de la bandeja', 'AN25', 25, L-25, A-40, z)]
    pz.append(Pz('chimenea', 'chimenea', 'CR60', (L/2.0, A/2.0, H), (L/2.0, A/2.0, H+350), kind='cil', w=100, h=100))
    pz.append(chapa_h('piso', 'piso del fuego', 'CH47', 20, L-20, 20, A-20, 250))
    pasos = [
      ('Armá los dos marcos de ángulo, el de abajo y el de arriba, iguales.', ['marcoa','marcob']),
      ('Unilos con los cuatro parantes y controlá escuadra en las dos diagonales de arriba.', ['parante']),
      ('Soldá las cuatro patas abajo.', ['pata']),
      ('Cerrá los tres lados con chapa de 3 mm, soldada por dentro con puntos cada 150 mm.', ['pared']),
      ('Soldá el piso del fuego de 4,75 mm y el techo.', ['piso','techo']),
      ('Soldá las cuatro guías de bandeja enfrentadas, a la misma altura: usá un nivel apoyado entre las dos.', ['guia']),
      ('Armá la puerta con su marco, amurá las bisagras y la manija, y soldá la chimenea arriba.', ['puerta','chimenea']),
    ]
    return Plano('BQ', 'Ahumador vertical %s' % med2(L, A), pz, pasos, (14, 20), 'Avanzado',
      'Ahumador vertical tipo gabinete: estructura de ángulo de 40, paredes de chapa de 3 mm, piso de fuego de 4,75 y '
      'cuatro niveles de bandejas. Ocupa 60 x 60 cm de piso y ahúma para veinte personas.',
      'Rotiserías, parrillas chicas y el fanático del ahumado que ya tiene parrilla. Es un trabajo de muchas horas: '
      'cotizá la mano de obra completa o lo regalás.',
      HERR_CHAPA + ['agujereadora', 'bisagras'],
      ['Las cuatro guías de cada nivel tienen que estar a la misma altura. Soldá las dos de un lado, apoyá un nivel '
       'cruzado y recién ahí soldá las otras dos.',
       'La puerta tiene que cerrar con un burlete de fibra o apoyar sobre un marco de ángulo. Si entra aire, no ahúma: se quema.'],
      extras=[('Bisagras, manija de madera, pestillo y termómetro', 'juego', 48000),
              ('Cuatro bandejas de parrilla de 520 x 520', '4 unidades', 72000)],
      variante='%d x %d x %d mm · 4 bandejas' % (L, A, H))

# ------------------------------------------------------------------ disco de arado
def disco_arado():
    pz = [Pz('disco', 'disco de arado de 16"', 'CH47', (0, 0, 700), (0, 0, 712), kind='cil', w=400, h=400,
             extra={'no_lista': True})]
    for i in range(3):
        a = math.radians(90 + 120*i)
        pz.append(Pz('pata', 'pata', 'TC30', (0, 0, 690), (420*math.cos(a), 420*math.sin(a), 0), corte='en ángulo'))
        pz.append(Pz('aro', 'aro de unión', 'PL25', (420*math.cos(a)*0.5, 420*math.sin(a)*0.5, 350),
                     (420*math.cos(math.radians(90+120*((i+1) % 3)))*0.5, 420*math.sin(math.radians(90+120*((i+1) % 3)))*0.5, 350),
                     corte='en ángulo'))
    pz.append(Pz('soporte', 'aro del disco', 'PL38', (-180, 0, 690), (180, 0, 690), corte='recto'))
    pz.append(Pz('soporteb', 'aro del disco', 'PL38', (0, -180, 690), (0, 180, 690), corte='recto'))
    pasos = [
      ('Conseguí un disco de arado de 16 pulgadas sin filo y quemalo con leña para sacarle el aceite.', ['disco']),
      ('Armá la cruz de planchuela que va abajo del disco: ahí apoya y ahí se suelda.', ['soporte','soporteb']),
      ('Cortá las tres patas con el mismo ángulo y puntéalas a la cruz.', ['pata']),
      ('Parálo y controlá con el nivel apoyado sobre el disco antes de soldar a fondo.', ['pata']),
      ('Soldá el aro del medio que ata las tres patas: sin eso, se abren.', ['aro']),
      ('Soldá el disco a la cruz desde abajo, con cuatro cordones cortos. Nunca por arriba.', ['disco']),
    ]
    return Plano('BQ', 'Soporte para disco de arado', pz, pasos, (3, 4), 'Principiante',
      'Las tres patas y la cruz para convertir un disco de arado en el disco de cocinar más vendido del país. '
      'El disco lo comprás usado; lo que vendés es el soporte y el trabajo.',
      'Se vende todo el año y lo compra cualquiera que tenga un fondo. Es el trabajo chico con mejor margen de toda '
      'la categoría: tres patas, un aro y una cruz.',
      HERR_BASE,
      ['Soldá el disco por abajo. Un cordón arriba junta comida, se quema y arruina el disco.',
       'Las patas abren hacia afuera. Si las hacés rectas, el disco se vuelca con el peso de la comida de un lado.'],
      extras=[('Disco de arado de 16" usado', '1 unidad', 38000)],
      variante='disco de 16" · 700 mm de alto')

# ------------------------------------------------------------------ parrilla portátil
def parrilla_portatil(L=600, A=400, H=300):
    pz = [chapa_v('pared', 'pared de la caja', 'CH3', 0, L, 0, 0, H),
          chapa_v('pared', 'pared de la caja', 'CH3', 0, L, A-3, 0, H),
          chapa_vy('pared', 'pared de la caja', 'CH3', 0, A, 0, 0, H),
          chapa_vy('pared', 'pared de la caja', 'CH3', 0, A, L-3, 0, H),
          chapa_h('piso', 'piso', 'CH3', 0, L, 0, A, 0, extra={'sin_vista': ('planta',)})]
    pz += marco_xy('aro', 'aro de arriba', 'AN25', -8, L+8, -8, A+8, H+10)
    pz += [vx('varilla', 'varilla de la parrilla', 'PL25', 20, L-20, y, H+25) for y in reparto(50, A-50, 7)]
    for (x, y) in [(40, 40), (L-40, 40), (40, A-40), (L-40, A-40)]:
        pz.append(vz('pata', 'pata plegable', 'TC25', -350, 0, x, y))
    pz.append(vy('manija', 'manija', 'RD10', 80, A-80, -20, H/2.0))
    pz.append(vy('manija', 'manija', 'RD10', 80, A-80, L+20, H/2.0))
    pasos = [
      ('Cortá las cuatro paredes y el piso. Marcá bien a escuadra: esta caja chica no perdona 3 mm.', ['pared','piso']),
      ('Puntéa las dos paredes largas al piso y después cerrá con las cortas.', ['pared']),
      ('Soldá el aro de ángulo arriba, que tapa el canto y sostiene la parrilla.', ['aro']),
      ('Armá la parrilla de varillas, suelta, apoyada sobre el aro.', ['varilla']),
      ('Soldá las dos manijas de redondo a los costados.', ['manija']),
      ('Soldá o abuloná las cuatro patas. Si las abulonás con mariposa, se desarman y entra en el baúl.', ['pata']),
    ]
    return Plano('BQ', 'Parrilla portátil de %d x %d' % (L/10, A/10), pz, pasos, (3, 5), 'Principiante',
      'Parrilla chica de chapa de 3 mm con patas desmontables, para llevar al río o al camping. Entra en el baúl de '
      'cualquier auto y pesa menos de 12 kg.',
      'Se vende en primavera y en verano, y se vende de a muchas: campings, cabañas, y el que sale de pesca. '
      'Hacé cinco iguales con plantilla y las liquidás en un fin de semana.',
      HERR_CHAPA,
      ['Si las patas van abulonadas, usá mariposas y no tuercas comunes: el cliente no lleva llave al río.',
       'Agujereá el piso para que ventile. Sin aire por abajo, el carbón no prende y te devuelven la parrilla.'],
      variante='%d x %d x %d mm · patas desmontables' % (L, A, H))

# ------------------------------------------------------------------ mesa auxiliar de parrilla
def mesa_parrilla(L=1100, A=600, H=900):
    pz = mesa('TC40', L, A, H-30, tapa=None, est_z=250, mat_est='TC30', n_trav=1, mat_trav='TC30')
    pz.append(chapa_h('tapa', 'tapa de chapa', 'CH3', 0, L, 0, A, H-30, extra={'sin_vista': ('planta',)}))
    pz.append(chapa_h('tabla', 'tabla de picar', 'MAD25', 40, 600, 60, A-60, H-27))
    pz.append(chapa_h('estante', 'estante de abajo', 'CH16', 40, L-40, 40, A-40, 265))
    pz += [vx('gancho', 'barral de ganchos', 'RD12', 60, L-60, 20, H+180),
           vz('gancho', 'parante del barral', 'TC30', H-30, H+180, 40, 20),
           vz('gancho', 'parante del barral', 'TC30', H-30, H+180, L-40, 20)]
    pz += [chapa_h('rueda', 'placa de la rueda', 'CH3', x-45, x+45, 60, 150, 0) for x in (70, L-70)]
    pasos = [
      ('Armá el marco de arriba con el travesaño del medio y escuadralo.', ['marco','marcob','trav']),
      ('Puntéa las cuatro patas y el marco del estante a 250 mm.', ['pata','est','estb']),
      ('Apoyá la tapa de chapa y puntéala cada 200 mm.', ['tapa']),
      ('Soldá los dos parantes del barral y el redondo de los ganchos arriba.', ['gancho']),
      ('Soldá las placas y amurá dos ruedas con freno.', ['rueda']),
      ('Pintá, apoyá la chapa del estante y amurá la tabla de picar de madera.', ['estante','tabla']),
    ]
    return Plano('BQ', 'Mesa auxiliar de parrilla %s' % med2(L, A), pz, pasos, (5, 7), 'Principiante',
      'La mesa que va al lado de la parrilla: tapa de chapa, tabla de picar de madera, estante abajo, barral de ganchos '
      'arriba y dos ruedas. Se vende junto con cualquier parrilla y suma la mitad del trabajo otra vez.',
      'El mismo cliente al que le hacés la parrilla. Ofrecela siempre en el mismo presupuesto, como opcional: '
      'uno de cada tres la agrega.',
      HERR_CHAPA,
      ['La tabla de madera va amurada con tornillos desde abajo, nunca pegada ni soldada con grampas a la vista.',
       'Las ruedas van del lado de la manija. Si las ponés en diagonal, la mesa se mueve sola cuando la cargás.'],
      variante='%d x %d x %d mm · con ruedas y ganchos' % (L, A, H))
