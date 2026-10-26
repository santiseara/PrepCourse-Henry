# -*- coding: utf-8 -*-
"""Los bonus escritos: instructivos en PDF."""
import os
from engine import *
from doc import Doc
from paginas import ML, MR, ANCHO

def _canvas(ruta, titulo):
    c = rl_canvas.Canvas(ruta, pagesize=(A4W, A4H))
    c.setTitle('Herrero de Finde · ' + titulo)
    c.setAuthor('Herrero de Finde')
    return c

# ============================================================ BONUS 2
def cobralo_bien(ruta, planos=None):
    c = _canvas(ruta, 'Cobralo Bien')
    d = Doc(c, 'Cobralo Bien', 'El kit para presupuestar sin regalar tu trabajo', 'Bonus 02')
    d.portada('La fórmula que usan los talleres, el presupuesto que mandás desde el celular y lo que contestás '
              'cuando te dicen que está caro.',
              ['La cuenta completa: material, insumos, tu hora y margen',
               'Lo que se cobra aparte y casi nadie cobra',
               'El modelo de presupuesto para mandar por WhatsApp',
               'Las tres frases que frenan el regateo',
               'Los seis errores que te hacen trabajar gratis'])

    d.h1('Primero: por qué casi todos cobran mal')
    d.p('El herrero que recién arranca cotiza mirando el hierro. Suma lo que le costó el material, le pone "algo" '
        'de ganancia y tira un número. Después descubre que el trabajo le llevó catorce horas, que compró dos discos, '
        'media garrafa de gas y un litro de antióxido, que fue dos veces a medir y que tuvo que llevarlo en la '
        'camioneta de un amigo. De la ganancia no quedó nada.')
    d.p('El problema no es que cobre poco. Es que no sabe qué está cobrando. Esta es la cuenta completa.')

    d.h1('La fórmula')
    d.caja('La cuenta, en orden',
           'HIERRO que consume el trabajo  +  INSUMOS (12 % del hierro)  +  TUS HORAS × EL VALOR DE TU HORA  =  PRECIO PISO. '
           'Y el techo del rango es ese precio piso multiplicado por 1,30.')
    d.h2('1. El hierro que consume el trabajo')
    d.p('Ojo con esto, porque es donde más se equivocan: no es lo que pagaste en el mostrador. Si compraste una barra '
        'de 6 metros y usaste 2,40, el trabajo consumió 2,40 metros. El resto te quedó en recortes y lo vas a usar en '
        'el próximo. Cada plano de la biblioteca te da los dos números separados, y la Planilla de Cortes te los calcula solos.')
    d.h2('2. Los insumos: el 12 % del hierro')
    d.p('Discos de corte y de desbaste, gas o alambre tubular, electrodos, mechas, antióxido, esmalte, thinner, '
        'lija, cinta, guantes. Nada de eso aparece en la factura de la casa de hierros y todo eso lo pagaste vos. '
        'En un trabajo normal se lleva entre el 10 y el 15 % de lo que costó el hierro. Usá 12 % y no lo pienses más.')
    d.h2('3. Tus horas por el valor de tu hora')
    d.p('Esta es la parte que la gente regala. Tu hora vale lo mismo si estás soldando que si estás midiendo, '
        'comprando, lijando o pintando. Contá todas. Si no sabés cuánto vale tu hora, empezá por preguntarte cuánto '
        'querés ganar por mes y dividilo por las horas que podés trabajar de verdad. En la biblioteca usamos un valor '
        'de referencia; cambialo por el tuyo en la Planilla de Cortes y todos los precios se recalculan.')
    d.h2('4. El rango, no el número')
    d.p('El precio piso es el mínimo con el que no trabajás gratis. El techo es ese número por 1,30. Entre uno y otro '
        'está lo que podés cobrar de más cuando entregás rápido, cuando la terminación es prolija y cuando el cliente '
        'ya vio fotos de otros trabajos tuyos. Empezá cotizando en el medio del rango.')

    d.h1('Lo que se cobra aparte')
    d.p('Nada de esto entra en la cuenta de arriba. Si lo regalás, estás pagando vos por trabajar.')
    d.bullets([
        '**Traslado y entrega.** Un portón de 3,60 m no entra en un auto. La nafta, el flete o el favor que le vas a '
        'pedir a alguien se cobran.',
        '**Instalación y amure.** Amurar, nivelar, soldar bisagras en el lugar y dejarlo funcionando es otro trabajo. '
        'Cotizalo como tal.',
        '**El apuro.** Si lo quiere para el viernes y vos tenías el sábado ocupado, eso tiene precio. No es abuso: es '
        'el valor de mover tu agenda.',
        '**Los viajes a medir.** Dos visitas son dos horas de tu día más el combustible.',
        '**El diseño a medida.** Si te pide algo distinto del plano, el cambio se cotiza aparte, con las horas de '
        'dibujo y de prueba incluidas.',
        '**La pintura especial.** Epoxi, galvanizado en frío o un color a elección no cuestan lo mismo que el negro '
        'satinado de siempre.',
    ])

    d.h1('El presupuesto que mandás por WhatsApp')
    d.p('Un presupuesto que se lee en diez segundos se contesta el mismo día. Uno que es un bloque de texto se '
        'contesta "cualquier cosa te aviso". Este es el formato: copialo y cambiá lo que está entre corchetes.')
    d.caja('Para copiar y pegar',
           'Hola [nombre], te paso el presupuesto del [trabajo]. · MEDIDAS: [largo x ancho x alto] mm. · MATERIAL: '
           'caño estructural [medida], chapa de [espesor] mm, todo nuevo. · TERMINACIÓN: desbaste completo, una mano '
           'de fondo antióxido y dos de esmalte sintético en el color que elijas. · PLAZO: [X] días desde la seña. · '
           'PRECIO: $[número] final. · Incluye [lo que incluye]. No incluye [traslado / instalación]. · Para arrancar '
           'necesito el 50 % y el resto contra entrega. El presupuesto vale 7 días porque el hierro se mueve.',
           color=CREMA)
    d.h2('Por qué el 50 % de adelanto no se negocia')
    d.p('Con ese adelanto comprás el material. Nunca pongas plata tuya en el hierro de otro: si el cliente se arrepiente, '
        'te quedaste con un portón a medida que no le sirve a nadie más. Decilo así, tal cual, y nadie se ofende: '
        '"con la seña compro el material, por eso arranco cuando está".')

    d.h1('Las tres frases que frenan el regateo')
    d.frase('"Te lo puedo hacer más barato, pero sacando cosas. ¿Qué preferís que saque?"')
    d.p('El que regatea quiere pagar menos, no quiere menos trabajo. Cuando le pedís que elija qué sacar, se da cuenta '
        'de que el precio tiene adentro cosas que él quiere. Casi siempre termina pagando el precio original.')
    d.frase('"Ese precio es con el material nuevo y con dos manos de esmalte. Si querés te cotizo la versión básica."')
    d.p('Le estás mostrando que lo que mirás no es el mismo trabajo que el del que le pasó un precio más bajo. '
        'La comparación deja de ser contra el precio y pasa a ser contra la calidad.')
    d.frase('"Lo tengo que tener en el taller [X] días. Si te sirve para [fecha], te lo reservo con la seña."')
    d.p('Movés la conversación del precio a la fecha. El que de verdad lo necesita, señala.')

    d.h1('Los seis errores que te hacen trabajar gratis')
    d.bullets([
        '**Dar el precio en el momento.** De memoria y con el cliente mirándote siempre sale bajo. "Te lo paso esta '
        'noche por WhatsApp" es una frase que vale plata.',
        '**No contar las horas de ida y vuelta.** Medir, comprar, ir a buscar el hierro, entregar. Son horas de tu día.',
        '**Cotizar sin ver el lugar** cuando el trabajo se instala. Un portón en una pared torcida es el doble de trabajo.',
        '**Cobrar el mismo precio que el año pasado.** El hierro se movió. Actualizá la tabla de la Planilla de Cortes '
        'y volvé a cotizar.',
        '**Hacer "un agregadito" gratis.** El agregado se cotiza o no se hace. Hacerlo gratis enseña que tu trabajo '
        'no vale nada.',
        '**Aceptar un precio para "entrar".** El cliente barato no te trae clientes buenos: te trae otros clientes baratos.',
    ])
    d.caja_oscura('REGLA DE ORO', [
        'Si cuando terminás el trabajo te quedó menos de lo que querías ganar por hora, no fue el cliente: fue la cotización.',
        'Anotá las horas reales de cada trabajo durante un mes. Vas a cotizar distinto el mes que viene.',
        'El precio sugerido de cada plano ya tiene esta cuenta hecha. Es un piso, no un techo.'])
    if planos: extra_cobralo(d, planos)
    d.cerrar(); c.save()

# ============================================================ BONUS 3
def checklist(ruta, planos=None):
    c = _canvas(ruta, 'El Checklist Cero Errores')
    d = Doc(c, 'Checklist Cero Errores', 'Una hoja para imprimir y colgar arriba del banco', 'Bonus 03')
    d.portada('El repaso de un minuto que te ahorra el sábado. Imprimilo, colgalo arriba del banco de trabajo y '
              'pasale el dedo antes de cada etapa.',
              ['Antes de comprar el hierro', 'Antes del primer corte', 'Antes del primer punto',
               'Antes de soldar a fondo', 'Antes de pintar', 'Antes de entregar'])
    d.h1('Antes de comprar el hierro')
    d.check(['Leí la hoja 3 del plano y tengo la lista de cortes a mano.',
             'Confirmé el espesor del caño: "de 50" puede ser de 1,6 o de 2 mm.',
             'Pregunté si cortan en la casa de hierros y si entra en mi vehículo.',
             'Revisé qué recortes tengo en el taller antes de comprar de más.'])
    d.h1('Antes del primer corte')
    d.check(['Medí la barra entera: muchas vienen 5,95 m y no 6 m.',
             'Marco con punta de metal o rayador, no con fibra gruesa.',
             'Mido todas las piezas desde la misma punta, no encadenadas una atrás de otra.',
             'Voy a cortar de mayor a menor.',
             'Tengo con qué escribir la letra de cada pieza apenas la corto.',
             'El disco es el correcto y está entero.'])
    d.h1('Antes del primer punto')
    d.check(['Desbasté la rebaba de todos los cortes.',
             'Presenté todas las piezas en seco y miré el conjunto.',
             'La mesa o los caballetes están nivelados.',
             'Tengo las dos escuadras o los sargentos listos.',
             'Limpié la pintura, el óxido y la grasa de donde va el cordón.',
             'La masa está puesta sobre la pieza, no sobre la mesa pintada.'])
    d.h1('Antes de soldar a fondo')
    d.check(['Medí las dos diagonales y dan iguales.',
             'Controlé el nivel en los dos sentidos.',
             'Las piezas que tienen que ser gemelas las apoyé una sobre la otra para comparar.',
             'Voy a soldar alternando lados y puntas, nunca todo seguido de un lado.',
             'Probé el amperaje en un recorte del mismo espesor.'])
    d.h1('Antes de pintar')
    d.check(['Saqué toda la escoria y pasé disco de láminas por cada cordón.',
             'Maté los cantos vivos: nadie se tiene que cortar con este trabajo.',
             'Desengrasé con thinner o aguarrás y está seco.',
             'No hay humedad ni va a llover en las próximas horas.',
             'Tengo el fondo antióxido y el esmalte del mismo sistema.'])
    d.h1('Antes de entregar')
    d.check(['Probé que abra, cierre, suba, baje o ruede como tiene que hacerlo.',
             'Le saqué las fotos con el trabajo limpio, de día y con fondo liso.',
             'Está la segunda mano de esmalte y está seca.',
             'Le avisé al cliente el día y la hora.',
             'Tengo el saldo acordado por escrito.'])
    d.caja('Una sola regla',
           'Medí dos veces y cortá una. El 80 % del hierro que termina en el tacho de recortes se fue por una medida '
           'que alguien dio por sabida.')
    extra_checklist(d)
    d.cerrar(); c.save()

# ============================================================ BONUS 4
def terminacion(ruta, planos=None):
    c = _canvas(ruta, 'Terminación de Taller')
    d = Doc(c, 'Terminación de Taller', 'Pintura y antióxido que aguantan el invierno a la intemperie', 'Bonus 04')
    d.portada('Dos trabajos iguales, uno pintado bien y otro pintado rápido: a los seis meses no se parecen en nada. '
              'Y el que se pela te lo traen de vuelta.',
              ['Los cuatro pasos que no se saltean', 'Qué usar en cada trabajo',
               'Cuánto rinde y cuánto hay que esperar', 'Por qué se pela una pintura'])
    d.h1('Los cuatro pasos')
    d.h2('1. Desbaste')
    d.p('Escoria afuera, cordones pasados con disco de láminas y cantos vivos matados. Si la pieza se va a tocar con '
        'la mano, no puede quedar ningún filo. Este paso no es estético: una rebaba es el lugar exacto por donde '
        'arranca el óxido, porque ahí la pintura queda más fina.')
    d.h2('2. Limpieza')
    d.p('Desengrasá con thinner o aguarrás y dejá secar. La grasa de la mano, el aceite del caño nuevo y el polvo de '
        'amolar son las tres razones más comunes por las que una pintura no agarra. El caño estructural viene con una '
        'película de aceite de fábrica: si pintás arriba, se pela en semanas.')
    d.h2('3. Fondo antióxido')
    d.p('Una mano pareja, sin cargar. El fondo no tapa: agarra. Si el trabajo va a la intemperie, dos manos cruzadas, '
        'la segunda cuando la primera está seca al tacto pero todavía fresca (tres a cuatro horas). Insistí en los '
        'cordones, en las uniones y en los cantos: ahí es donde la pintura se adelgaza sola.')
    d.h2('4. Esmalte')
    d.p('Dos manos de esmalte sintético, con doce a veinticuatro horas entre una y otra. Nunca pintes con humedad '
        'alta, con el sol pegando sobre la pieza ni abajo de 10 grados. El esmalte que se seca demasiado rápido queda '
        'con piel de naranja y se cuartea en un año.')

    d.h1('Qué usar en cada trabajo')
    d.tabla(['Trabajo', 'Fondo', 'Terminación', 'Por qué'],
            [['Portón, cerco, baranda', 'Antióxido convencional, 2 manos', 'Esmalte sintético, 2 manos',
              'Está afuera todo el año y se mira de cerca'],
             ['Trailer y carro', 'Antióxido, 2 manos (abajo primero)', 'Esmalte o poliuretano',
              'Piedra, barro y agua salada en la ruta'],
             ['Parrilla y fogonero', 'Nada en la zona de fuego', 'Pintura de alta temperatura',
              'El esmalte común se quema y hace humo tóxico'],
             ['Mueble de interior', 'Convertidor de óxido o fondo', 'Esmalte satinado o mate',
              'Se toca con la mano, el brillo marca las huellas'],
             ['Gimnasio y racks', 'Antióxido', 'Esmalte sintético o epoxi',
              'Golpes de discos y de barras'],
             ['Estructura y cochera', 'Antióxido, 2 manos', 'Esmalte sintético',
              'Pintala antes de techar: después no llegás'],
             ['Pieza que va enterrada', 'Asfáltico o brea', '—',
              'La pintura común no aguanta bajo tierra']],
            [96, 118, 110, 180])
    d.caja('La zona de fuego no se pinta',
           'En una parrilla o en un fogonero, la chapa que toca el fuego va sin pintura o con pintura de alta '
           'temperatura, nunca con esmalte sintético. El esmalte se quema, humea y deja olor en la comida. Las patas '
           'y la estructura sí se pintan normal.')

    d.h1('Cuánto rinde y cuánto hay que esperar')
    d.bullets([
        '**Rendimiento:** un litro de antióxido cubre entre 8 y 10 m² por mano sobre hierro desbastado.',
        '**Secado al tacto:** 3 a 4 horas el antióxido, 6 a 8 el esmalte, siempre con buena ventilación.',
        '**Entre manos:** 4 horas para el antióxido, 12 a 24 para el esmalte. Si apurás, la segunda mano levanta la primera.',
        '**Secado duro:** 7 días. Hasta ahí, el trabajo se raya con cualquier cosa. Avisale al cliente.',
        '**Pistola o pincel:** la pistola rinde más y queda mejor, pero el pincel llega a los rincones. En un portón, pistola para el paño y pincel para las uniones.',
    ])
    d.h1('Por qué se pela una pintura')
    d.bullets([
        '**Pintaste sobre aceite o grasa.** El caño nuevo viene aceitado. Desengrasá siempre.',
        '**Pintaste sobre óxido suelto.** El fondo no convierte el óxido viejo: hay que sacarlo con cepillo o con disco.',
        '**Mezclaste sistemas.** Esmalte sintético arriba de un fondo epoxi, o al revés, se arruga. Usá el mismo sistema.',
        '**Pintaste con humedad.** El agua queda abajo de la película y empuja la pintura desde adentro.',
        '**Cargaste la mano.** Una mano gruesa se seca por afuera y queda blanda adentro: se marca con la uña a la semana.',
    ])
    d.caja_oscura('LO QUE SUMA PRECIO SIN COSTARTE CASI NADA', [
        'Matar los cantos y desbastar los cordones: es lo primero que toca el cliente.',
        'Pintar también el lado que no se ve. El que lo mira por abajo es siempre el que paga.',
        'Entregar con la pintura seca y sin olor. Un trabajo que todavía huele a thinner parece sin terminar.'])
    extra_terminacion(d)
    d.cerrar(); c.save()

# ============================================================ BONUS 5
def taller(ruta, planos=None):
    c = _canvas(ruta, 'El Taller de $500.000')
    d = Doc(c, 'El Taller de $500.000', 'Qué comprar, en qué orden, y qué saltearte', 'Bonus 05')
    d.portada('No necesitás un galpón ni una máquina de 3 millones para empezar a vender trabajos. Necesitás cinco '
              'cosas, en este orden.',
              ['El orden de compra, de la primera a la última',
               'Qué herramienta cara podés saltear al principio',
               'Las plantillas caseras que reemplazan equipos',
               'Lo que sí o sí tiene que ser bueno'])
    d.h1('El orden, de la primera a la última')
    d.p('Esta lista está ordenada por lo que te permite facturar antes, no por lo que es más lindo tener. '
        'Comprá en este orden y vas a estar vendiendo trabajos antes de terminar la lista.')
    d.tabla(['Orden', 'Herramienta', 'Para qué', 'Cuándo comprarla'],
            [['1', 'Soldadora inverter', 'Todo. Es el oficio.', 'Primera compra'],
             ['2', 'Amoladora angular de 4 1/2"', 'Cortar, desbastar, limpiar', 'Primera compra'],
             ['3', 'Máscara fotosensible', 'No quedarte ciego', 'Primera compra'],
             ['4', 'Escuadra y cinta de 5 m', 'Que todo salga derecho', 'Primera compra'],
             ['5', 'Sargentos y morsetos (4 como mínimo)', 'Son tus dos manos extra', 'Primera semana'],
             ['6', 'Mesa de soldar (hacela vos)', 'Que nada se descuadre', 'Primer trabajo'],
             ['7', 'Agujereadora y juego de mechas', 'Amures, bisagras, bulones', 'Primer mes'],
             ['8', 'Amoladora de 7" o sierra sensitiva', 'Cortes largos y rectos', 'Cuando cortes mucho'],
             ['9', 'Caballetes (hacelos vos)', 'Trabajos largos', 'Primer mes'],
             ['10', 'Pistola de pintar y compresor', 'Terminación de otro nivel', 'Cuando pintes seguido']],
            [34, 168, 150, 110])
    d.h1('Qué podés saltear al principio')
    d.bullets([
        '**Soldadora MIG grande.** Una inverter de electrodo de 160 A hace el 90 % de los trabajos de la biblioteca. '
        'La MIG es más rápida y más prolija, pero es una compra de cuando ya estás vendiendo.',
        '**Dobladora y roladora.** Casi ningún plano de la biblioteca necesita doblar o rolar. Cuando aparezca el '
        'trabajo que lo pide, se terceriza y se cobra aparte.',
        '**Plasma.** Es una maravilla y no lo vas a usar hasta que hagas cortes curvos seguido.',
        '**Mesa de corte de sierra.** Una amoladora con disco fino y un tope bien hecho cortan igual de derecho.',
        '**Galpón.** Un garaje con la puerta abierta y un matafuego alcanza para arrancar.',
    ])
    d.h1('Lo que sí o sí tiene que ser bueno')
    d.bullets([
        '**La máscara.** Es lo único que no se recupera: la vista. Fotosensible, con regulación, de marca conocida.',
        '**La escuadra.** Una escuadra barata que no es escuadra te arruina todos los trabajos y nunca vas a entender por qué.',
        '**Los sargentos.** Los baratos se abren con el calor. Compralos de a poco pero compralos buenos.',
        '**El disco de corte.** El barato dura un tercio y salta. Sale más caro.',
    ])
    d.h1('Las plantillas que reemplazan equipos caros')
    d.bullets([
        '**Escuadra de armado de 90°** (plano SH de la biblioteca): dos de estas reemplazan a una persona sosteniendo.',
        '**Tope de corte para la amoladora:** un pedazo de ángulo amurado a la mesa, a medida, y todos los cortes salen iguales.',
        '**Plantilla de repetición:** si vas a hacer seis banquetas, armá una plantilla con dos recortes de ángulo. '
        'Te ahorra una hora por banqueta.',
        '**Caballetes con travesaño:** la mesa grande que no podés comprar todavía.',
        '**Calibre de separación:** un recorte del largo exacto para repartir barrotes sin medir uno por uno.',
    ])
    d.caja('La compra que más plata te devuelve',
           'La mesa de soldar. No la compres: hacela con un plano de la biblioteca. Te cuesta el hierro, te lleva un '
           'sábado, y a partir de ahí todo lo que fabriques sale derecho. Es la herramienta que fabrica a las demás.')
    d.caja_oscura('SEGURIDAD: LO QUE NO SE NEGOCIA', [
        'Máscara y guantes siempre, aunque sea "un punto nomás". El golpe de arco se siente ocho horas después.',
        'Protección ocular también para amolar: el disco salta y el esquirlazo no avisa.',
        'Nunca soldar sobre tambores, bidones o caños cerrados sin ventilar.',
        'Matafuego a mano y nada inflamable a menos de 10 metros: las chispas vuelan.'])
    extra_taller(d)
    d.cerrar(); c.save()

# ============================================================ BONUS 7
def vende(ruta, planos=None):
    c = _canvas(ruta, 'Vendé lo que Fabricás')
    d = Doc(c, 'Vendé lo que Fabricás', 'El plan de 30 días, del primer trabajo al primer cobro', 'Bonus 07')
    d.portada('Fabricar ya sabés. Esto es lo otro: sacar la foto correcta, publicar donde hay que publicar y '
              'contestar de manera que la conversación termine en una seña.',
              ['La foto que vende y la que hunde el precio',
               'Dónde publicar y qué escribir',
               'Qué contestar cuando preguntan "cuánto sale"',
               'El plan día por día, semana por semana'])
    d.h1('La foto es el producto')
    d.p('El cliente no compra el trabajo: compra la foto del trabajo. Dos parrillas idénticas, una fotografiada en el '
        'piso del taller con la bolsa de cemento atrás y la otra apoyada contra una pared lisa con luz de día, se '
        'venden a precios distintos. Es la misma parrilla.')
    d.bullets([
        '**De día y afuera.** La luz del taller amarillea todo. Sacá el trabajo a la vereda o al patio.',
        '**Fondo liso.** Una pared, un portón cerrado, el pasto. Nada de herramientas, cables ni la camioneta atrás.',
        '**Desde la altura del pecho, no desde arriba.** La foto desde arriba achica y hace ver el trabajo barato.',
        '**Tres fotos como mínimo:** el trabajo entero, un detalle de una unión bien terminada y el trabajo en uso '
        'o en su lugar.',
        '**Limpio y pintado.** Nunca publiques algo sin pintar, aunque lo entregues así.',
        '**Sin filtros.** El cliente quiere ver el hierro real.',
    ])
    d.caja('El detalle que más vende',
           'Una foto bien de cerca de una esquina a 45 grados, con el cordón desbastado y la pintura pareja. '
           'Esa foto dice "esto lo hizo alguien que sabe" mejor que cualquier texto.')

    d.h1('Dónde publicar')
    d.bullets([
        '**Marketplace.** Es donde está el comprador de mueble, parrilla, trailer y gimnasio. Publicá cada trabajo '
        'como producto, con precio. Sin precio, la mitad no pregunta.',
        '**Grupos de compra y venta de tu zona.** Son los que te dan los trabajos de barrio, que son los que empiezan la rueda.',
        '**Grupos del nicho.** Fierreros, cuatriciclos, asadores, crossfit, campo. Ahí el que ve tu trailer sabe exactamente qué está mirando.',
        '**Instagram o el estado de WhatsApp.** No para vender: para que los que ya te conocen vean que estás fabricando.',
        '**La vidriera más barata:** el trabajo terminado en la vereda de tu casa el fin de semana. Más de un trabajo '
        'se vendió porque pasó un vecino.',
    ])
    d.h2('Qué escribir en la publicación')
    d.caja('Modelo de publicación',
           '[Trabajo] de [medidas] en caño estructural de [medida] y chapa de [espesor]. Fabricado a mano, con fondo '
           'antióxido y dos manos de esmalte. Lo hago en el color que quieras y en la medida que necesites. Entrega '
           'en [X] días. Precio: $[número]. Consultá por otras medidas.', color=CREMA)
    d.p('Medidas, material, terminación, plazo y precio. Nada de "excelente calidad" ni "no dude en consultar": '
        'eso lo escribe todo el mundo y no dice nada.')

    d.h1('Qué contestar')
    d.bullets([
        '**"¿Cuánto sale?"** → El precio, el plazo y una pregunta. "Sale $X, lo tengo listo en 5 días. ¿Lo querés en '
        'esa medida o lo necesitás más grande?" La pregunta mantiene viva la conversación.',
        '**"¿Es lo último?"** → "Ese es el precio con material nuevo y dos manos de esmalte. Si querés, te cotizo una '
        'versión más simple."',
        '**"Lo pienso y te aviso."** → "Dale. Te dejo la medida anotada. Si lo querés para [fecha], avisame esta semana '
        'porque después se me ocupa el taller."',
        '**"¿Hacés X?"** (algo que no tenés publicado) → Sí, si está en la biblioteca. Abrí el plano, mirá el precio '
        'sugerido y pasalo. Ese es el momento en que la biblioteca se paga sola.',
        '**El que no contesta más.** → Un mensaje a los tres días con una foto nueva del trabajo terminado. Uno solo. '
        'No insistas más que eso.',
    ])

    d.h1('El plan de 30 días')
    d.h2('Semana 1 · Fabricá algo que se pueda mostrar')
    d.bullets([
        'Elegí de la biblioteca un trabajo marcado como Principiante, de 3 a 6 horas, que puedas hacer con lo que ya tenés.',
        'Compralo, fabricalo y pintalo bien. Este no es para vender: es tu vidriera.',
        'Sacale las tres fotos como dice este bonus.',
    ])
    d.h2('Semana 2 · Publicá y hacete ver')
    d.bullets([
        'Publicá ese trabajo en Marketplace con precio, y en dos grupos de tu zona.',
        'Fabricá un segundo trabajo, de otra categoría, mientras esperás.',
        'Contestá todo el mismo día. La velocidad de respuesta vende más que el precio.',
    ])
    d.h2('Semana 3 · Convertí consultas en presupuestos')
    d.bullets([
        'A cada consulta, presupuesto formal con el modelo del Bonus 02.',
        'Ofrecé siempre una segunda opción: la medida más grande o el complemento (la mesa auxiliar junto con la parrilla).',
        'Pedí la seña del 50 % para reservar fecha.',
    ])
    d.h2('Semana 4 · Entregá y pedí la próxima')
    d.bullets([
        'Entregá limpio, seco y en la fecha. La fecha cumplida es la mitad de la recomendación.',
        'Sacá la foto del trabajo instalado en lo del cliente: esa es la mejor foto que vas a tener.',
        'Pedile que te recomiende. Textual: "si conocés a alguien que necesite algo de herrería, pasale mi número".',
        'Volvé a publicar con las fotos nuevas. Arranca el mes dos.',
    ])
    d.caja_oscura('LO QUE HACE LA DIFERENCIA AL MES DOS', [
        'Tener siempre un trabajo terminado para mostrar, no solo fotos de trabajos entregados.',
        'Contestar el mismo día, aunque sea para decir "lo cotizo esta noche".',
        'Cumplir la fecha. En este oficio, el que entrega cuando dijo tiene trabajo todo el año.'])
    if planos: extra_vende(d, planos)
    d.cerrar(); c.save()

# ============================================================ BONUS 8
def soldar(ruta, planos=None):
    c = _canvas(ruta, 'Soldá como un Pro')
    d = Doc(c, 'Soldá como un Pro', 'El manual de soldadura, desde cero', 'Bonus 08')
    d.portada('El que hace que todo lo demás funcione. Si recién arrancás, leé esto antes de abrir el primer plano.',
              ['Qué máquina y qué electrodo usar', 'Cómo elegir el amperaje sin adivinar',
               'Cómo se prende y cómo se mueve el arco', 'Las cuatro posiciones y cuándo usar cada una',
               'Qué te está diciendo el cordón cuando sale feo'])
    d.h1('La máquina')
    d.p('Para todo lo que hay en esta biblioteca alcanza con una inverter de electrodo revestido de 160 a 200 amperes, '
        'o con una MIG chica con alambre tubular. La inverter es más barata, anda con cualquier enchufe decente y no '
        'depende del gas. La MIG es más rápida y más prolija, sobre todo en chapa fina.')
    d.tabla(['Si vas a soldar', 'Conviene', 'Por qué'],
            [['Caño estructural de 1,6 a 3 mm', 'Electrodo 6013 de 2,5 mm o MIG', 'Poco calor, poca deformación'],
             ['Chapa de 2 a 3 mm', 'MIG o electrodo de 2 mm, por puntos', 'La chapa fina se perfora fácil'],
             ['Chapa de 4,75 y 6 mm', 'Electrodo 6013 o 7018 de 3,25', 'Necesita penetración'],
             ['Perfil C, UPN, estructuras', 'Electrodo 7018 de 3,25 o 4', 'Cordón más resistente'],
             ['Hierro redondo y planchuela', 'Electrodo 6013 de 2,5', 'Es lo más común y lo más fácil']],
            [150, 160, 200])
    d.h2('Electrodo 6013 y 7018, en criollo')
    d.bullets([
        '**6013:** el común, el que se prende fácil y deja un cordón prolijo. Para casi todo lo de esta biblioteca.',
        '**7018:** más resistente, para estructuras que van a cargar peso. Pide más amperaje, se prende más difícil y '
        'se humedece: guardalo en un lugar seco.',
        '**Alambre tubular (MIG sin gas):** rápido y cómodo para trabajar afuera porque el viento no le hace nada. '
        'Deja más escoria, hay que cepillar más.',
    ])
    d.h1('El amperaje')
    d.p('La regla rápida: unos 30 a 40 amperes por cada milímetro de diámetro del electrodo. Un 6013 de 2,5 mm anda '
        'entre 70 y 100 A; uno de 3,25 mm, entre 100 y 140 A. Pero el número exacto lo da la prueba: agarrá un recorte '
        'del mismo espesor que la pieza y tirá un cordón antes de tocar el trabajo del cliente.')
    d.tabla(['Lo que ves', 'Qué pasa', 'Qué hacer'],
            [['Se pega el electrodo', 'Poco amperaje', 'Subí 10 A y acercá el arco'],
             ['Chisporrotea y salpica mucho', 'Demasiado amperaje', 'Bajá 10 A'],
             ['Se hace un agujero', 'Mucho calor para ese espesor', 'Bajá amperaje y soldá por puntos'],
             ['Cordón alto y angosto', 'Vas muy rápido o falta calor', 'Más lento, o subí un poco'],
             ['Cordón ancho y chato', 'Vas muy lento', 'Avanzá más rápido']],
            [140, 150, 220])
    d.h1('Cómo se suelda, paso por paso')
    d.bullets([
        '**Limpiá.** Pintura, óxido y grasa afuera. El arco no atraviesa la suciedad: la convierte en porosidad.',
        '**Masa sobre la pieza.** Nunca sobre la mesa pintada ni a tres metros. Mal puesta, el arco no prende y te '
        'vuelve loco buscando el problema.',
        '**Prendé raspando,** como un fósforo, y levantá apenas. La distancia del arco es más o menos el diámetro del electrodo.',
        '**Inclinación:** el electrodo a unos 70 u 80 grados respecto de la pieza, inclinado hacia donde vas.',
        '**Movimiento:** derecho y parejo para cordones cortos. Si necesitás llenar más, hacé zigzag suave, nunca círculos grandes.',
        '**Velocidad:** la que mantiene el baño de fusión del mismo ancho. Mirá el baño, no el arco.',
        '**Cortá y limpiá.** Picá la escoria y cepillá antes del siguiente cordón. La escoria atrapada abajo del cordón '
        'siguiente es una falla segura.',
    ])
    d.h1('Las cuatro posiciones')
    d.bullets([
        '**Plana (abajo de la mano).** La más fácil y la que tenés que buscar siempre: girá la pieza, no el cuerpo.',
        '**Horizontal.** El baño tiende a caer: menos amperaje y electrodo más inclinado hacia arriba.',
        '**Vertical.** De abajo hacia arriba para penetrar, de arriba hacia abajo solo en chapa fina. Bajá el amperaje un 10 %.',
        '**Sobre cabeza.** Evitala mientras puedas. Si no hay otra, cordones cortos y amperaje bajo.',
    ])
    d.caja('El secreto que no es secreto',
           'El 90 % de los cordones feos se arreglan girando la pieza para soldar en posición plana. Antes de soldar '
           'incómodo, pensá dos segundos cómo darla vuelta.')
    d.h1('Qué te está diciendo el cordón')
    d.tabla(['Defecto', 'Se ve así', 'Causa', 'Solución'],
            [['Porosidad', 'Agujeritos en el cordón', 'Suciedad, humedad o viento', 'Limpiar, tapar el viento'],
             ['Mordedura', 'Canaleta al costado del cordón', 'Mucho amperaje o mala inclinación', 'Bajar amperaje'],
             ['Falta de fusión', 'El cordón se despega del borde', 'Poco calor o arco largo', 'Subir amperaje, arco corto'],
             ['Escoria atrapada', 'Manchas oscuras adentro', 'No cepillaste entre pasadas', 'Picar y cepillar siempre'],
             ['Salpicadura', 'Bolitas pegadas alrededor', 'Mucho amperaje, arco largo', 'Bajar y acercar'],
             ['Deformación', 'La pieza se tuerce', 'Mucho calor seguido de un lado', 'Alternar lados y puntos']],
            [86, 140, 150, 134])
    d.h1('Lo que evita el 90 % de los problemas')
    d.bullets([
        '**Puntos antes que cordones.** Siempre. Puntos, medir, corregir y recién ahí soldar.',
        '**Alterná.** Un punto de un lado, uno del otro, uno en una punta, uno en la otra. El calor seguido tuerce todo.',
        '**Dejá enfriar.** En chapa fina, soldá un poco y esperá. Apurarse es la forma más cara de arruinar una pieza.',
        '**Probá en un recorte.** Cada vez que cambiás de espesor o de electrodo.',
        '**Cepillo y piqueta a mano.** Un cordón limpio es un cordón que podés mirar y corregir.',
    ])
    d.caja_oscura('CUANDO TE SALGA BIEN, SACALE FOTO', [
        'Un cordón parejo, con el dibujo de monedita, desbastado y pintado, es tu mejor publicidad.',
        'La foto de una unión bien terminada vende más que la foto del trabajo entero.',
        'Esa foto va primero en tu publicación: es lo que te separa del que suelda a los ponchazos.'])
    extra_soldar(d)
    d.cerrar(); c.save()

# ============================================================ secciones extra
def extra_cobralo(d, planos):
    por_cod = dict((p.codigo, p) for p in planos)
    ejemplos = []
    for cod in ('FM-068', 'BQ-090', 'SH-004'):
        p = por_cod.get(cod)
        if p: ejemplos.append(p)
    d.h1('Tres cotizaciones completas, con los números a la vista')
    d.p('Así se arma el precio de tres trabajos de la biblioteca. Los valores son los de la edición de octubre de '
        '2026: lo que cambia siempre es el valor de tu hora y el precio del hierro en tu zona.')
    for p in ejemplos:
        bajo, alto = p.precio_venta()
        d.h2('%s · %s' % (p.codigo, p.nombre))
        d.tabla(['Concepto', 'Cuenta', 'Importe'],
                [['Hierro que consume', 'lo que gasta el trabajo, no la barra entera', pesos(p.costo_material())],
                 ['Insumos', '12 % del hierro', pesos(p.insumos())],
                 ['Mano de obra', '%d h × %s' % (p.horas[0], pesos(VALOR_HORA)), pesos(p.horas[0]*VALOR_HORA)],
                 ['PRECIO PISO', 'la suma de las tres líneas', pesos(bajo)],
                 ['Techo del rango', 'piso × 1,30', pesos(alto)],
                 ['Te queda', 'precio piso menos el hierro', pesos(bajo - p.costo_material())]],
                [120, 230, 160])
    d.caja('Lo que este cuadro te enseña',
           'En casi todos los trabajos, la mano de obra pesa más que el hierro. Por eso bajar el precio "porque el '
           'material salió barato" es el error más común del oficio: no estás vendiendo hierro, estás vendiendo tus horas.')
    d.h1('Cuando el hierro se mueve')
    d.bullets([
        '**No actualices plano por plano.** Abrí la Planilla de Cortes, andá a la hoja Materiales y cambiá el factor. '
        'Si subió 18 %, poné 1,18 y toda la planilla se recalcula.',
        '**Revisá el factor una vez por mes.** Pedí el precio de una barra de caño 50 x 50 x 2 y compará contra la tabla.',
        '**Los presupuestos vencen.** Poné "este presupuesto vale 7 días" en todos. No es desconfianza: es como trabaja el rubro.',
        '**Si ya cerraste el precio y el hierro subió,** comprá el material el mismo día que recibís la seña. Para eso es la seña.',
    ])

def extra_checklist(d):
    d.h1('Los diez errores más caros')
    d.bullets([
        '**Cortar sin desbastar la rebaba anterior.** Todo apoya mal y la suma de errores te descuadra el marco.',
        '**Medir encadenado.** Pieza tras pieza, el error se suma. Medí siempre desde la misma punta.',
        '**Soldar sobre pintura u óxido.** El cordón queda poroso y se parte donde menos lo esperás.',
        '**Cordón corrido en chapa fina.** La chapa se arquea como una banana y no vuelve.',
        '**No medir las diagonales.** Es el único control que importa y lleva veinte segundos.',
        '**Armar sobre piso de tierra.** La pieza toma la forma del piso.',
        '**Dejar la masa en la mesa.** El arco no prende bien y te comés media hora buscando el problema.',
        '**Pintar con humedad.** A los dos meses la pintura se infla sola.',
        '**Entregar sin probar.** Que abra, cierre, ruede o suba se prueba en el taller, no en lo del cliente.',
        '**No anotar las horas reales.** Si no las anotás, el próximo presupuesto va a estar igual de mal que este.',
    ])
    d.h1('Planilla de control del trabajo')
    d.p('Imprimí esta hoja por cada trabajo que hagas durante un mes. Con cuatro hojas llenas vas a cotizar mejor que '
        'con cualquier curso.')
    d.tabla(['Dato', 'Anotá acá'],
            [['Plano y medidas', '________________________________________'],
             ['Fecha de inicio / entrega', '________________________________________'],
             ['Hierro que compré', '________________________________________'],
             ['Lo que pagué en el mostrador', '________________________________________'],
             ['Horas reales de taller', '________________________________________'],
             ['Horas de viajes y compras', '________________________________________'],
             ['Discos, gas, pintura', '________________________________________'],
             ['Lo que cobré', '________________________________________'],
             ['Lo que me quedó por hora', '________________________________________'],
             ['Qué haría distinto', '________________________________________']],
            [190, 320])
    d.caja('La pregunta de la última fila',
           'Casi siempre la respuesta es la misma las primeras veces: "cobrar más" o "hacer la plantilla antes de '
           'arrancar". Las dos cosas se arreglan solas cuando las anotás.')

def extra_terminacion(d):
    d.h1('Hierro con óxido viejo: cómo se recupera')
    d.bullets([
        '**Óxido superficial, color naranja claro:** cepillo de acero o disco de láminas, desengrase y fondo. Listo.',
        '**Óxido con escamas:** cepillo de copa en la amoladora hasta llegar al metal. Si quedan escamas, la pintura '
        'se va a levantar con ellas.',
        '**Óxido profundo con picaduras:** cepillo y convertidor de óxido. El convertidor no reemplaza al fondo: '
        'se aplica antes.',
        '**Pintura vieja que todavía agarra:** lijá para dar mordiente y pintá arriba con el mismo sistema. Si no '
        'sabés qué sistema es, probá en una esquina: si el thinner la levanta, es sintética.',
        '**Galvanizado:** no agarra el antióxido común. Necesita un fondo específico para galvanizados (wash primer).',
    ])
    d.h1('El kit mínimo de pintura')
    d.tabla(['Qué', 'Para qué', 'Cuánto'],
            [['Fondo antióxido', 'Todo trabajo de hierro', '4 litros rinden 8 a 10 trabajos chicos'],
             ['Esmalte sintético negro satinado', 'El 70 % de lo que vendés', '4 litros'],
             ['Thinner o aguarrás', 'Desengrasar y limpiar', '1 litro'],
             ['Pintura de alta temperatura', 'Parrillas y fogoneros', '1 aerosol'],
             ['Convertidor de óxido', 'Trabajos de reparación', '1 litro'],
             ['Pinceles de 1 1/2" y 2 1/2"', 'Rincones y uniones', '2 de cada uno'],
             ['Rodillo chato de pelo corto', 'Paños grandes', '2'],
             ['Lija al agua 180 y 320', 'Entre manos', '5 hojas']],
            [150, 180, 180])
    d.h1('Problemas de pintura y qué hacer')
    d.tabla(['Lo que pasa', 'Por qué', 'Qué hacer'],
            [['Piel de naranja', 'Pintura muy espesa o mucho calor', 'Diluir 10 % y pintar a la sombra'],
             ['Chorreaduras', 'Mano muy cargada', 'Lijar cuando seque y dar mano fina'],
             ['Se arruga', 'Segunda mano antes de tiempo', 'Lijar todo y empezar de nuevo'],
             ['No seca', 'Humedad o frío', 'Esperar; no agregar más manos'],
             ['Burbujas', 'Humedad abajo de la película', 'Lijar hasta el metal en esa zona'],
             ['Marca la uña a la semana', 'Mano gruesa', 'Avisar: el secado duro son 7 días']],
            [130, 180, 200])

def extra_taller(d):
    d.h1('El taller en tres etapas')
    d.h2('Etapa 1 · Para empezar a facturar')
    d.p('Soldadora inverter, amoladora de 4 1/2", máscara fotosensible, escuadra, cinta, cuatro sargentos y un juego '
        'de discos. Con eso ya podés fabricar y vender la mitad de los trabajos marcados como Principiante en la '
        'biblioteca. El resto lo vas comprando con lo que facturás.')
    d.h2('Etapa 2 · Para trabajar cómodo')
    d.p('La mesa de soldar (hacela vos con un plano de la biblioteca), dos caballetes, agujereadora con mechas, '
        'morsa, cepillo de copa y un banco con estante. Acá es donde tu trabajo empieza a verse prolijo, porque '
        'todo lo que armás sobre una mesa plana sale derecho.')
    d.h2('Etapa 3 · Para ganar tiempo')
    d.p('MIG con alambre tubular, amoladora de 7" o sierra sensitiva, compresor con pistola, estantería y rack de '
        'barras. Esta etapa no te hace fabricar cosas nuevas: te hace fabricar lo mismo en la mitad del tiempo, '
        'que es lo mismo que cobrar el doble por hora.')
    d.h1('Comprar usado: qué mirar')
    d.bullets([
        '**Soldadora:** pedí probarla con un electrodo. Mirá que el ventilador gire y que no huela a quemado.',
        '**Amoladora:** apretá el eje con la mano: si tiene juego, el rodamiento está jugado.',
        '**Morsa:** que cierre parejo y que el tornillo no tenga juego lateral.',
        '**Compresor:** escuchá si carga y corta solo. Mirá el tanque por abajo: si está picado, no lo compres.',
        '**Lo que nunca se compra usado:** la máscara, los discos y los guantes.',
    ])
    d.h1('Dónde va cada cosa')
    d.bullets([
        '**La mesa, en el medio.** Tenés que poder caminar alrededor: la mitad de los trabajos se arman girando.',
        '**El hierro, contra la pared y horizontal.** Barras paradas en un rincón es hierro que no vas a usar '
        'porque no ves lo que tenés. Para eso está el rack de barras.',
        '**Los recortes, en un carro.** Clasificados por perfil. El recorte que no encontrás lo volvés a comprar.',
        '**La soldadora, con el cable corto.** El cable largo tirado en el piso es el 100 % de los tropezones.',
        '**El matafuego, en la salida.** No adentro del taller: en el camino hacia afuera.',
    ])

def extra_vende(d, planos):
    datos = []
    for p in planos:
        bajo = p.precio_venta()[0]
        datos.append(((bajo - p.costo_material())/float(p.horas[0]), p))
    datos.sort(key=lambda t: -t[0])
    vistos = set(); filas = []
    for porhora, p in datos:
        clave = p.nombre.split(' de ')[0].split(' 1')[0][:24]
        if clave in vistos: continue
        vistos.add(clave)
        filas.append([p.codigo, p.nombre, '%d-%d h' % p.horas, pesos(p.precio_venta()[0]), pesos(redondear(porhora, 1000))])
        if len(filas) >= 12: break
    d.h1('Los doce trabajos que más rápido se pagan')
    d.p('Ordenados por lo que te queda por hora de taller. Son los que conviene fabricar primero cuando lo que '
        'necesitás es que la rueda empiece a girar.')
    d.tabla(['Código', 'Trabajo', 'Horas', 'Se vende a', 'Te queda por hora'],
            filas, [52, 200, 54, 100, 104])
    d.h1('Precio de lista: la decisión que te ahorra mil mensajes')
    d.p('Elegí seis u ocho trabajos de la biblioteca, calculá el precio con la planilla y armá tu lista. Cuando te '
        'preguntan, contestás en diez segundos con el precio y el plazo. El que improvisa cada precio tarda dos días '
        'en contestar y pierde la mitad de las consultas.')
    d.bullets([
        '**Publicá siempre con precio.** Sin precio, la mitad de la gente no pregunta.',
        '**Una sola medida por publicación.** "Desde $X" confunde y después discutís.',
        '**Actualizá la lista una vez por mes,** cuando revisás el factor del hierro.',
    ])
    d.h1('Cuando no te contestan')
    d.bullets([
        '**A las 48 horas:** una foto nueva del trabajo terminado y una línea. "Te mando una foto del último que hice."',
        '**A la semana:** el cierre amable. "¿Lo dejamos para más adelante?" Esa pregunta destraba más de lo que parece.',
        '**Después, nada.** Si vuelve, vuelve. Perseguir clientes baja tu precio.',
        '**Guardá los contactos** en una lista con el trabajo que preguntaron. En tres meses, cuando tengas una foto '
        'nueva de ese mismo trabajo, les escribís una vez.',
    ])
    d.caja_oscura('LA VENTA QUE MÁS VECES SE REPITE', [
        'El complemento. Al que le hacés la parrilla ofrecele la mesa auxiliar; al que le hacés el rack, el banco.',
        'Va en el mismo presupuesto, como opcional, con su precio al lado. Uno de cada tres lo suma.',
        'Es la venta más barata que vas a hacer: ya ganaste al cliente y ya estás comprando hierro.'])

def extra_soldar(d):
    d.h1('Preparación de juntas')
    d.bullets([
        '**A tope en chapa de hasta 3 mm:** juntas al ras, con una luz de medio milímetro. No hace falta biselar.',
        '**A tope de 4 mm para arriba:** biselá los dos bordes a 30 grados con la amoladora. Sin bisel, el cordón '
        'queda arriba y no penetra: es una unión que se ve bien y no aguanta.',
        '**En T (lo más común en caño):** cordón en los dos lados si la pieza carga; en uno solo si es decorativa.',
        '**En solapa:** la más tolerante. Si recién arrancás y podés elegir, diseñá en solapa.',
        '**Caño contra caño redondo:** necesita bocado. Marcá con un papel enrollado, cortá con amoladora y limá hasta '
        'que apoye en todo el contorno. Si no querés hacer bocados, aplastá la punta con la maza y soldá el aplastado: '
        'es lo que se hace en el campo y aguanta.',
    ])
    d.h1('Chapa fina sin perforar')
    d.bullets([
        '**Bajá el amperaje** hasta donde el arco todavía prenda: en chapa de 1,6 mm, un 6013 de 2 mm a 50-60 A.',
        '**Puntos, no cordones.** Un punto de 15 mm cada 150 o 200 mm. Dejá enfriar y volvé.',
        '**Alterná de punta a punta,** nunca avanzando seguido: así el calor se reparte y la chapa no se arquea.',
        '**Apoyá la chapa contra algo macizo** (un hierro grueso por detrás): se lleva el calor y evita el agujero.',
        '**Si perforaste:** no insistas encima. Dejá enfriar, limpiá y rellená desde los bordes hacia el centro.',
    ])
    d.h1('Cuidar la máquina')
    d.bullets([
        '**Enchufe y prolongación.** Una prolongación fina hace caer la tensión y la máquina suelda mal. 2,5 mm² mínimo, lo más corta posible.',
        '**Sopleteala por dentro cada tanto.** El polvo de amolar es conductor y es lo que mata las inverter.',
        '**No la dejes en el piso donde barrés.** Arriba de un cajón o colgada.',
        '**Electrodos secos.** El 7018 húmedo hace porosidad. Guardalos en un tubo cerrado.',
        '**Cambiá el cable de masa** apenas la pinza no cierre bien. La mitad de los problemas de arco son de masa.',
    ])
    d.caja('Cómo practicar en una tarde',
           'Conseguí recortes de caño de 2 mm. Primero: diez cordones rectos sobre una chapa, sin unir nada, hasta que '
           'salgan parejos. Segundo: diez uniones en T. Tercero: armá un cuadrado de 300 x 300 y medí las diagonales. '
           'Cuando el cuadrado te dé igual en las dos diagonales, ya podés hacer cualquier plano marcado como '
           'Principiante de la biblioteca.')
