# -*- coding: utf-8 -*-
"""FM · Portones de campo, comederos y corrales."""
from engine import *
from comun import *

P = []

# ------------------------------------------------------------------ hoja de portón de campo
def porton_campo(cod, L, H=1150, nhoriz=5):
    pz = marco_xz('marco', 'marco de la hoja', 'TC50', 0, L, 0, H, 0)
    for z in interiores(0, H, nhoriz-2):
        pz.append(vx('horiz', 'travesaño horizontal', 'TR4020', 25, L-25, 0, z))
    pz.append(Pz('diag', 'diagonal', 'TR4020', (30, 0, 30), (L-30, 0, H-30), corte='en ángulo'))
    pz += [chapa_v('oreja', 'oreja de la bisagra', 'CH6', 0, 120, -6, z-50, z+50) for z in (150, H-150)]
    pz.append(chapa_v('pestillo', 'pletina del pestillo', 'CH6', L-140, L, -6, H/2.0-60, H/2.0+60))
    pasos = [
      ('Cortá el marco a 45 grados y presentalo sobre la mesa. Esta hoja tiene que ser perfectamente rectangular.', ['marco','marcob']),
      ('Puntéa las cuatro esquinas, medí las dos diagonales y corregí antes de soldar a fondo.', ['marco','marcob']),
      ('Repartí los %d travesaños horizontales y puntealos de a uno, alternando de punta a punta.' % (nhoriz-2), ['horiz']),
      ('Marcá la diagonal con la hoja ya escuadrada, cortala con el ángulo real y puntéala. Va de la bisagra de abajo hacia el pestillo de arriba.', ['diag']),
      ('Soldá las dos orejas de las bisagras del lado del poste, a 150 mm de cada punta.', ['oreja']),
      ('Soldá la pletina del pestillo del lado opuesto, a media altura.', ['pestillo']),
      ('Dalo vuelta, soldá del otro lado, desbastá y pintá con dos manos de antióxido: este trabajo vive a la intemperie.', ['pestillo']),
    ]
    return Plano('FM', 'Hoja de portón de campo de %s' % metros(L), pz, pasos,
      (5, 7) if L < 3500 else (7, 9), 'Principiante',
      'Hoja de portón de campo de %s x %s: marco de caño 50 x 50, %d travesaños de 40 x 20 y una diagonal que va de la '
      'bisagra de abajo al pestillo de arriba. Liviana para abrirla con una mano y rígida para que no se descuelgue.'
      % (metros(L), metros(H), nhoriz-2),
      'Campos, quintas, chacras y loteos. Es el trabajo más repetido del interior: el que te compra una hoja te compra '
      'dos, y el vecino te pide la suya cuando ve que la tuya no se arrastra.',
      HERR_BASE + ['nivel de burbuja'],
      ['La diagonal va de abajo-bisagra a arriba-pestillo. Al revés, trabaja al revés y la hoja se descuelga igual.',
       'Soldá la hoja apoyada sobre la mesa o sobre cuatro caballetes nivelados. Si la armás en el piso de tierra, sale alabeada.'],
      dims=[dict(vista='frente', tipo='v', a=0, b=H, ref=L*0.5, off=18, lado=1)],
      variante='%d x %d mm · marco de 50 x 50' % (L, H))
P.append(('FM-068', porton_campo('FM-068', 3660)))
P.append(('FM-031', porton_campo('FM-031', 2440)))
P.append(('FM-084', porton_campo('FM-084', 4270, 1200, 6)))

# ------------------------------------------------------------------ portón corredizo
def porton_corredizo():
    L, H = 3000, 1800
    pz = marco_xz('marco', 'marco del portón', 'TC60', 0, L, 0, H, 0)
    for x in interiores(0, L, 3):
        pz.append(vz('parante', 'parante vertical', 'TC40', 30, H-30, x, 0))
    pz.append(vx('medio', 'travesaño del medio', 'TC40', 30, L-30, 0, H/2.0))
    pz += [Pz('diag', 'diagonal', 'TC40', (30, 0, 30), (L/2.0, 0, H-30), corte='en ángulo'),
           Pz('diag', 'diagonal', 'TC40', (L-30, 0, 30), (L/2.0, 0, H-30), corte='en ángulo')]
    for x in reparto(400, L-400, 2):
        pz.append(chapa_h('carro', 'base del carro de rueda', 'CH6', x-80, x+80, -60, 60, -10))
    pz.append(vx('riel', 'perfil riel inferior', 'C100', 0, L, 0, -70))
    pz.append(chapa_v('chapa', 'chapa de cierre', 'CH16', 30, L-30, 30, 30, H-30, extra={'sin_vista': ('frente',)}))
    pasos = [
      ('Armá el marco de caño 60 a 45 grados, escuadrado sobre la mesa.', ['marco','marcob']),
      ('Soldá el travesaño del medio y después los tres parantes verticales.', ['medio','parante']),
      ('Puntéa las dos diagonales en V: son las que impiden que el portón se venza en el voladizo.', ['diag']),
      ('Soldá el perfil riel abajo, al ras, bien recto: de esto depende que corra suave.', ['riel']),
      ('Soldá las dos bases de los carros y amurá las ruedas.', ['carro']),
      ('Puntéa la chapa de cierre cada 200 mm, siempre alternando lados para que no se arquee.', ['chapa']),
      ('Pintá con antióxido los dos lados y probá el corrido completo antes de entregarlo.', ['chapa']),
    ]
    return Plano('FM', 'Portón corredizo de 3 m', pz, pasos, (10, 14), 'Intermedio',
      'Portón corredizo de 3 x 1,80 m con marco de caño 60, diagonales en V, riel de perfil C abajo y chapa de cierre. '
      'El voladizo es lo que mata a los portones corredizos: por eso las diagonales van en V y no sueltas.',
      'Casas de barrio, galpones y quintas. Es un trabajo de presupuesto medio que casi siempre viene con el cerco, '
      'así que cotizá los dos juntos.',
      HERR_CHAPA + ['nivel de burbuja'],
      ['El riel abajo tiene que quedar recto como una regla. Soldalo con puntos alternados y nunca de corrido: se arquea.',
       'Si la chapa de cierre la soldás de un solo lado y de corrido, el portón se dobla como una banana. Puntos cortos, cruzados.'],
      variante='3.000 x 1.800 mm · con riel y carros')
P.append(('FM-102', porton_corredizo()))

# ------------------------------------------------------------------ tranquera
def tranquera(L=3000, H=1200):
    pz = [vz('parante', 'parante', 'CR50', 0, H, 40, 0),
          vz('parante', 'parante', 'CR50', 0, H, L-40, 0)]
    for z in reparto(80, H-80, 5):
        pz.append(vx('caño', 'caño horizontal', 'CR38', 0, L, 0, z))
    pz.append(Pz('diag', 'diagonal', 'CR38', (60, 0, 100), (L-60, 0, H-100), corte='en ángulo'))
    pz += [chapa_v('oreja', 'oreja de la bisagra', 'CH6', 0, 130, -6, z-50, z+50) for z in (180, H-180)]
    pasos = [
      ('Cortá los cinco caños horizontales exactamente iguales: si uno sale 10 mm más corto, la tranquera queda en rombo.', ['caño']),
      ('Marcá en los dos parantes las cinco alturas, con los parantes apoyados juntos.', ['parante']),
      ('Puntéa el caño de arriba y el de abajo, controlá escuadra y recién ahí sumá los tres del medio.', ['caño']),
      ('Soldá la diagonal de punta a punta, en el mismo plano.', ['diag']),
      ('Soldá las dos orejas de bisagra en un parante.', ['oreja']),
      ('Rematá todos los cordones alrededor del caño redondo y pintá: en caño redondo el óxido se mete por la junta.', ['oreja']),
    ]
    return Plano('FM', 'Tranquera de caño de %s' % metros(L), pz, pasos, (4, 6), 'Principiante',
      'Tranquera clásica de caño redondo de %s: dos parantes de 2", cinco caños de 1 1/2" y una diagonal. Liviana, se abre ' % metros(L) +
      'con una mano y no junta viento como una hoja llena.',
      'Campos y chacras. Es el trabajo que te piden de a pares y con fecha: cuando arrancan los trabajos de campo, '
      'nadie quiere esperar.',
      HERR_BASE,
      ['Soldar caño redondo contra caño redondo pide bocado. Si no querés hacer bocados, aplastá la punta con la maza '
       'y soldá el aplastado: es lo que se hace en el campo.',
       'Dejá los parantes 60 mm más largos abajo: así la tranquera no raspa el piso cuando el terreno se asienta.'],
      variante='%d x %d mm · caño redondo' % (L, H))
P.append(('FM-045', tranquera()))
P.append(('FM-051', tranquera(4000, 1300)))
P.append(('FM-038', tranquera(2500, 1100)))
P.append(('FM-015', porton_campo('FM-015', 3000)))
P.append(('FM-023', porton_campo('FM-023', 2000, 1100, 4)))
P.append(('FM-090', porton_campo('FM-090', 5000, 1250, 6)))

# ------------------------------------------------------------------ comedero para hacienda
def comedero(cod, L, A, H):
    pz = []
    t = 30
    pz.append(chapa_h('fondo', 'fondo de la canoa', 'CH3', 0, L, 120, A-120, H))
    slant = math.sqrt(120.0**2 + 260.0**2)
    pz += [Pz('lado', 'lateral de la canoa', 'CH3', (0, 60, H+130), (L, 60, H+130),
              w=3, h=slant, corte='a escuadra', ref=(0, -120, 260)),
           Pz('lado', 'lateral de la canoa', 'CH3', (0, A-60, H+130), (L, A-60, H+130),
              w=3, h=slant, corte='a escuadra', ref=(0, 120, 260))]
    pz += [chapa_vy('punta', 'tapa de la punta', 'CH3', 0, A, 0, H, H+260),
           chapa_vy('punta', 'tapa de la punta', 'CH3', 0, A, L-3, H, H+260)]
    pz += [vx('borde', 'caño del borde', 'CR38', 0, L, 20, H+260),
           vx('borde', 'caño del borde', 'CR38', 0, L, A-20, H+260)]
    for x in reparto(250, L-250, 3):
        pz += [Pz('pata', 'pata', 'TC50', (x, 60, 0), (x, 150, H), corte='en ángulo'),
               Pz('pata', 'pata', 'TC50', (x, A-60, 0), (x, A-150, H), corte='en ángulo'),
               vy('patin', 'patín de la pata', 'TC50', 0, A, x, 25)]
    pasos = [
      ('Cortá la chapa del fondo y las dos de los laterales. Los laterales van inclinados: ese ángulo lo da el plano.', ['fondo']),
      ('Puntéa un lateral al fondo, de punta a punta, con puntos cada 150 mm.', ['lado']),
      ('Sumá el otro lateral y controlá que la boca de arriba sea pareja de las dos puntas.', ['lado']),
      ('Cerrá las dos puntas y soldá por adentro: la soldadura por dentro es la que no junta agua.', ['punta']),
      ('Soldá el caño del borde arriba de cada lateral: tapa el filo de la chapa y da rigidez.', ['borde']),
      ('Dalo vuelta y soldá los tres caballetes de patas con sus patines.', ['pata','patin']),
      ('Hacé dos agujeros de drenaje de 20 mm en el fondo, en las dos puntas, y pintá todo por dentro y por fuera.', ['fondo']),
    ]
    return Plano('FM', 'Comedero para hacienda de %s' % metros(L), pz, pasos, (7, 10), 'Intermedio',
      'Canoa de chapa de 3 mm con laterales inclinados, borde de caño redondo y tres caballetes de patas con patín. '
      'El borde de caño es el detalle que hace que el animal no se corte y que la chapa no se abra.',
      'Campos de cría, tambos y criaderos. Se venden de a varios y siempre antes del invierno. Es un trabajo de chapa '
      'simple con buen precio por hora.',
      HERR_CHAPA,
      ['Los agujeros de drenaje van sí o sí. Un comedero que junta agua pudre el alimento y te lo devuelven.',
       'Soldá por adentro y rematá los cordones: cualquier filo o poro ahí adentro lastima al animal y junta suciedad.'],
      variante='%d x %d mm · canoa de 260 mm de hondo' % (L, A))
P.append(('FM-120', comedero('FM-120', 3000, 600, 500)))
P.append(('FM-127', comedero('FM-127', 2000, 500, 450)))

# ------------------------------------------------------------------ panel de corral
def panel_corral():
    L, H = 3000, 1600
    pz = [vz('parante', 'parante', 'CR50', 0, H, 40, 0),
          vz('parante', 'parante', 'CR50', 0, H, L-40, 0)]
    for z in reparto(200, H-100, 5):
        pz.append(vx('caño', 'caño horizontal', 'CR38', 0, L, 0, z))
    pz += [vz('medio', 'parante del medio', 'CR38', 180, H-80, L/2.0, 0)]
    pz += [chapa_v('oreja', 'oreja de unión', 'CH6', 0, 140, -6, z-60, z+60) for z in (300, H-300)]
    pasos = [
      ('Cortá los cinco caños horizontales iguales con tope en la sierra: todos los paneles tienen que ser intercambiables.', ['caño']),
      ('Apoyá los dos parantes paralelos sobre la mesa y marcá las cinco alturas.', ['parante']),
      ('Puntéa el caño de arriba y el de abajo, escuadrá y sumá los tres del medio.', ['caño']),
      ('Soldá el parante del medio.', ['medio']),
      ('Soldá las dos orejas de unión de un lado: son las que enganchan con el panel siguiente.', ['oreja']),
      ('Pintá o galvanizá en frío. Estos paneles viven afuera y se golpean todo el tiempo.', ['oreja']),
    ]
    return Plano('FM', 'Panel de corral de 3 m', pz, pasos, (3, 5), 'Principiante',
      'Panel de corral de caño redondo, 3 x 1,60 m, con orejas de unión para engancharlos entre sí. Se hacen todos '
      'iguales y se venden por cantidad: el margen está en la repetición.',
      'Campos, remates, ferias y corrales de encierre. Es el trabajo ideal para hacer en serie en un galpón: una '
      'plantilla, cinco cortes iguales y a repetir.',
      HERR_BASE,
      ['Hacete la plantilla antes del primer panel. Diez paneles sin plantilla te llevan el doble de tiempo y salen distintos.',
       'Las orejas van todas del mismo lado y a la misma altura. Si no, los paneles no enganchan entre sí.'],
      variante='3.000 x 1.600 mm · 5 caños · se enganchan entre sí')
P.append(('FM-056', panel_corral()))

# ------------------------------------------------------------------ puerta peatonal
def puerta_peatonal():
    L, H = 1000, 2000
    pz = marco_xz('marco', 'marco de la hoja', 'TC40', 0, L, 0, H, 0)
    pz += [vx('medio', 'travesaño del medio', 'TC40', 20, L-20, 0, H*0.45)]
    for x in interiores(0, L, 4):
        pz.append(vz('barrote', 'barrote', 'TC20', H*0.45, H-20, x, 0))
    pz.append(chapa_v('chapa', 'chapa de abajo', 'CH16', 20, L-20, 0, 20, H*0.45))
    pz += [chapa_v('oreja', 'oreja de la bisagra', 'CH6', 0, 110, -6, z-50, z+50) for z in (250, H-250)]
    pz.append(chapa_v('cerradura', 'refuerzo de la cerradura', 'CH3', L-120, L-20, -3, 950, 1150))
    pasos = [
      ('Armá el marco a 45 grados sobre la mesa y escuadralo con las diagonales.', ['marco','marcob']),
      ('Soldá el travesaño del medio, que divide la parte llena de la parte de barrotes.', ['medio']),
      ('Repartí los cuatro barrotes arriba y puntealos de a uno.', ['barrote']),
      ('Puntéa la chapa de abajo cada 200 mm, alternando de lado.', ['chapa']),
      ('Soldá las dos orejas de bisagra y el refuerzo de la cerradura.', ['oreja','cerradura']),
      ('Desbastá todo lo que se ve, pintá y recién ahí amurá la cerradura.', ['cerradura']),
    ]
    return Plano('FM', 'Puerta peatonal de cerco', pz, pasos, (4, 6), 'Principiante',
      'Puerta de 1 x 2 m con chapa abajo y barrotes arriba: la combinación que más se pide porque da privacidad sin '
      'parecer una celda. Marco de caño 40 y refuerzo de cerradura ya previsto.',
      'Cercos de frente, entradas de patio y accesos de servicio. Siempre va junto con el portón o el cerco: '
      'ofrecela en el mismo presupuesto.',
      HERR_CHAPA,
      ['Dejá previsto el refuerzo de la cerradura antes de pintar. Agujerear y soldar después arruina la pintura.',
       'Medí el vano dos veces y descontá 15 mm por lado. Una puerta que entra justa no entra.'],
      variante='1.000 x 2.000 mm · chapa abajo y barrotes arriba')
P.append(('FM-073', puerta_peatonal()))

# ------------------------------------------------------------------ portón de dos hojas
def porton_dos_hojas():
    L, H = 3600, 1900
    pz = []
    for off in (0, L/2.0 + 20):
        hw = L/2.0 - 20
        pz += marco_xz('marco', 'marco de la hoja', 'TC50', off, off+hw, 0, H, 0)
        pz.append(vx('medio', 'travesaño del medio', 'TC40', off+25, off+hw-25, 0, H*0.42))
        for x in interiores(off, off+hw, 3):
            pz.append(vz('barrote', 'barrote', 'TC25', H*0.42, H-25, x, 0))
        pz.append(chapa_v('chapa', 'chapa de abajo', 'CH16', off+25, off+hw-25, 0, 25, H*0.42))
        pz += [chapa_v('oreja', 'oreja de la bisagra', 'CH6', off, off+110, -6, z-50, z+50) for z in (260, H-260)]
    pasos = [
      ('Armá la primera hoja completa y usala de plantilla: la segunda tiene que ser su espejo exacto.', ['marco','marcob']),
      ('Soldá el travesaño del medio de cada hoja a la misma altura en las dos.', ['medio']),
      ('Repartí los barrotes de arriba, iguales en las dos hojas.', ['barrote']),
      ('Puntéa las chapas de abajo con puntos cortos y alternados.', ['chapa']),
      ('Apoyá las dos hojas juntas en el piso y controlá que cierren parejas antes de soldar las orejas.', ['oreja']),
      ('Soldá las orejas de bisagra en espejo y pintá las dos hojas al mismo tiempo, para que queden del mismo tono.', ['oreja']),
    ]
    return Plano('FM', 'Portón de dos hojas de 3,60 m', pz, pasos, (12, 16), 'Intermedio',
      'Dos hojas de 1,78 x 1,90 m con chapa abajo y barrotes arriba. Entra una camioneta y se abre a mano sin motor. '
      'Las dos hojas se arman una sobre la otra para que cierren justas.',
      'Frentes de casa, quintas y galpones. Es el trabajo más caro que podés hacer sin herramientas especiales, y el '
      'que más te muestra: queda en la calle, a la vista de todo el barrio.',
      HERR_CHAPA + ['nivel de burbuja'],
      ['Armá la segunda hoja apoyada sobre la primera. Si las hacés por separado, en el cierre te vas a encontrar con '
       'una luz de 15 mm que no hay forma de disimular.',
       'Pintá las dos hojas el mismo día y del mismo tarro. Dos tonos distintos en un portón se ven desde la vereda.'],
      variante='3.600 x 1.900 mm · dos hojas')
P.append(('FM-095', porton_dos_hojas()))

P.append(('FM-134', comedero('FM-134', 4000, 700, 550)))
