# -*- coding: utf-8 -*-
"""Glúteo Despierto: el mismo diseño del quiz del competidor, con TODOS los textos nuevos.

Se parte del documento del competidor tal cual (su <style>, su sprite de iconos, su
markup y su motor) y se reemplaza, paso por paso, cada texto. No se toca ni una
regla de CSS ni una linea del render: lo unico que cambia son las palabras, las
imagenes y el bloque de configuracion.
"""
import re, sys, os

# ===========================================================================
# EL CHECKOUT — es lo unico que hay que tocar cuando cambia la tienda.
# Puede ser absoluto ("https://tu-tienda.impultienda.ar/checkout") o relativo
# ("/checkout", que resuelve a la tienda donde se pegue el HTML).
# Se verifica con: curl -sIL -o /dev/null -w "%{http_code}" <url>  -> 200
# ===========================================================================
CHECKOUT_URL = '/checkout'

SRC = 'comp_doc.html'
OUT = os.path.expanduser('~/Desktop/gluteo-despierto/landing/quiz.html')

doc = open(SRC, encoding='utf-8').read()

fallos = []

def rep(texto, pares, donde):
    """Reemplaza cada par exactamente una vez. Anota los que no aparecen."""
    for viejo, nuevo in pares:
        if texto.count(viejo) < 1:
            fallos.append('%s :: NO ESTA :: %s' % (donde, viejo[:70]))
            continue
        texto = texto.replace(viejo, nuevo, 1)
    return texto

# ===========================================================================
# 1. IMAGENES — las neutras del competidor se reusan, el logo, el icono y la
#    portada son propios (las dos llevaban su marca).
# ===========================================================================
IMGS = {
    'pc-logo':          '../imagenes/logo.webp',
    'pc-icono':         '../imagenes/icono.webp',
    'pc-portada':       '../imagenes/portada.webp',
    'pc-analisis':      '../imagenes/carga-1.webp',
    'pc-patrones':      '../imagenes/carga-2.webp',
    'pc-conectando':    '../imagenes/carga-3.webp',
    'pc-antes-despues': '../imagenes/antes-despues.webp',
    'pc-resultado-1':   '../imagenes/resultado-1.webp',
    'pc-resultado-2':   '../imagenes/resultado-2.webp',
    'pc-resultado-3':   '../imagenes/resultado-3.webp',
    'pc-avatar-1':      '../imagenes/avatar-1.webp',
    'pc-avatar-2':      '../imagenes/avatar-2.webp',
    'pc-avatar-3':      '../imagenes/avatar-3.webp',
    'pc-sellos-compra': '../imagenes/sellos-compra.webp',
    'sello-garantia-30-dias': '../imagenes/sello-garantia.webp',
}

def ruta(m):
    url = m.group(0)
    for clave, destino in IMGS.items():
        if clave in url:
            return destino
    if url.endswith('.mp4'):
        return ''          # el VSL se carga aparte
    fallos.append('IMAGEN SIN MAPEAR :: ' + url[-70:])
    return url

doc = re.sub(r'https://aekpgsbqjzqntlbucbts\.supabase\.co/storage/[^"\s]+', ruta, doc)

# ===========================================================================
# 2. HEAD
# ===========================================================================
doc = rep(doc, [
 # una sola regla nueva, con el verde que ya usa su caja de precio
 ('.precio-der span{font-size:15px;line-height:1.15}',
  '.precio-der span{font-size:15px;line-height:1.15}\n'
  '.cuotas{margin:10px 0 0;text-align:center;font-size:15px;line-height:1.3;color:#047C38}\n'
  '.cuotas strong{font-weight:700}'),
 ('<title>Guía Piernas y Cola Sin Sentadillas</title>',
  '<title>Glúteo Despierto — Cola parada en 28 días, sin sentadillas</title>\n'
  '<meta name="description" content="Tu cola no crece porque el glúteo está dormido. '
  'Hacé el test y descubrí el Protocolo del Glúteo Dormido.">'),
], 'head')

# ===========================================================================
# 3. LOS 29 PASOS — se parte por <section class="paso">, se reescribe cada uno
#    y se vuelve a pegar. Asi ningun texto repetido (hay varios "A veces me
#    siento incomoda") se pisa con el de otro paso.
# ===========================================================================
cortes = [m.start() for m in re.finditer(r'<section class="paso', doc)]
fin_ultimo = doc.index('</div>\n<script>') if '</div>\n<script>' in doc else doc.index('<script>')
cabecera = doc[:cortes[0]]
cola = doc[fin_ultimo:]
pasos = [doc[cortes[k]: (cortes[k+1] if k+1 < len(cortes) else fin_ultimo)] for k in range(len(cortes))]
assert len(pasos) == 30, len(pasos)

P = {}

# ---- 0 · portada ---------------------------------------------------------
P[0] = [
 ('alt="Antes y después: sin y con el Truco de la Cola"',
  'alt="Antes y después: sin y con el Protocolo del Glúteo Dormido"'),
 ('<strong>Atención: debido al alto volumen de accesos, esta </strong>',
  '<strong>Atención: por la cantidad de gente entrando, este </strong>'),
 ('<strong class="rojo">oportunidad se libera gratis solo 1 vez por persona</strong>',
  '<strong class="rojo">diagnóstico se abre gratis una sola vez por persona</strong>'),
 ('<strong class="marca-roja">Si salís, perdés tu turno.</strong>',
  '<strong class="marca-roja">Si cerrás la página, perdés el lugar.</strong>'),
 ('<span>Obtener el Truco de la Cola Ahora</span>', '<span>Quiero Despertar Mi Glúteo</span>'),
 ('Acceso liberado por los próximos: ', 'Tu lugar queda guardado por: '),
]

# ---- 1 · edad ------------------------------------------------------------
P[1] = [
 ('¿Qué edad tenés?', 'Para arrancar, ¿qué edad tenés?'),
 ('<strong>18 a 24 años</strong>', '<strong>De 18 a 24 años</strong>'),
 ('<strong>25 a 34 años</strong>', '<strong>De 25 a 34 años</strong>'),
 ('<strong>35 a 44 años</strong>', '<strong>De 35 a 44 años</strong>'),
 ('<strong>45 años o más</strong>', '<strong>45 años o más</strong>'),
]

# ---- 2 · objetivo --------------------------------------------------------
P[2] = [
 ('¿Cuál es tu MAYOR objetivo con el entrenamiento de piernas y cola?',
  '¿Qué es lo que MÁS querés lograr con tus piernas y tu cola?'),
 ('Tener la cola parada y las piernas torneadas', 'Levantar la cola y marcar las piernas'),
 ('Ganar fuerza y definición muscular', 'Tener fuerza y músculo de verdad'),
 ('Que me entre la ropa que amo', 'Volver a entrar en la ropa que me gusta'),
 ('Volver a sentirme segura y sensual', 'Sentirme linda otra vez'),
 ('Tener un cuerpo que me haga sentir orgullosa al mirarme al espejo',
  'Mirarme al espejo sin esquivar la vista'),
]

# ---- 3 · tiempo ----------------------------------------------------------
P[3] = [
 ('¿Cuánto tiempo por día podés dedicarle a entrenar?',
  '¿Cuántos minutos por día le podés dar de verdad?'),
 ('Menos de 15 minutos (vivo a las corridas)', 'Menos de 15 (vivo a las corridas)'),
 ('15 a 30 minutos (puedo meter algo rápido)', 'Entre 15 y 30 (algo rápido meto)'),
 ('30 a 45 minutos (tengo un tiempo razonable)', 'Entre 30 y 45 (tengo un rato)'),
 ('Más de 45 minutos (tengo flexibilidad)', 'Más de 45 (me sobra el tiempo)'),
]

# ---- 4 · carga 1 ---------------------------------------------------------
P[4] = [
 ('Analizando tu información', 'Leyendo tus respuestas'),
 ('alt="Antes y después de entrenar sin sentadillas"', 'alt="Antes y después del Protocolo"'),
 ('Edad y objetivos identificados', 'Edad y objetivo registrados'),
 ('Tiempo disponible calculado', 'Minutos por día calculados'),
 ('Historial de entrenamiento registrado', 'Perfil de entrenamiento armado'),
]

# ---- 5 · intentos --------------------------------------------------------
P[5] = [
 ('¿Ya intentaste entrenar piernas antes?', '¿Ya probaste entrenar piernas alguna vez?'),
 ('Sí, pero abandoné porque no veía resultados', 'Sí, y lo dejé porque no pasaba nada'),
 ('Sí, pero dejé por dolor/molestias', 'Sí, y lo dejé porque me dolía'),
 ('Sí, pero no pude ser constante', 'Sí, pero nunca lo sostuve'),
 ('No, nunca entrené en serio', 'No, nunca entrené en serio'),
 ('Entreno a veces, pero sin mucha disciplina', 'Entreno de a ratos, sin método'),
]

# ---- 6 · frustracion -----------------------------------------------------
P[6] = [
 ('¿Cuál es tu mayor frustración con el entrenamiento de piernas/cola hoy?',
  '¿Qué es lo que más te frustra hoy con tus piernas y tu cola?'),
 ('No veo resultados aunque entreno', 'Entreno y la cola sigue igual'),
 ('Me duelen mucho las rodillas al hacer sentadillas', 'Las sentadillas me matan las rodillas'),
 ('No sé si estoy haciendo los ejercicios correctos', 'No sé si hago bien los ejercicios'),
 ('No tengo tiempo para ir al gimnasio', 'No me da el tiempo para el gimnasio'),
 ('Ya probé de todo y nada me funciona', 'Probé de todo y nada me movió el amperímetro'),
]

# ---- 7 · dolor -----------------------------------------------------------
P[7] = [
 ('¿Sentís algún tipo de dolor o molestia al hacer sentadillas?',
  '¿Te duele algo cuando hacés sentadillas?'),
 ('Sí, mucho dolor, no puedo hacerlas', 'Sí, me duele tanto que ni las hago'),
 ('Sí, siento una molestia moderada', 'Sí, una molestia que me banco'),
 ('A veces siento algo raro', 'A veces siento algo raro'),
 ('Casi nunca siento algo', 'Casi nunca me molesta'),
 ('Nunca hice sentadillas como para saber', 'Nunca las hice, no sabría decirte'),
]

# ---- 8 · abandono por dolor ---------------------------------------------
P[8] = [
 ('¿Con qué frecuencia abandonás un entrenamiento por dolor o molestias?',
  '¿Cada cuánto cortás un entrenamiento porque algo te duele?'),
 ('Siempre, por eso ya no entreno más', 'Siempre, por eso dejé de entrenar'),
 ('Seguido (+3 veces por mes)', 'Seguido, más de 3 veces al mes'),
 ('A veces (1 o 2 veces por mes)', 'Una o dos veces por mes'),
 ('Casi nunca me pasa', 'Casi nunca me pasa'),
 ('Nunca abandono, pero siento molestias', 'Nunca corto, pero termino dolorida'),
]

# ---- 9 · "no naci" -------------------------------------------------------
P[9] = [
 ('¿Alguna vez pensaste "yo no nací para tener la cola parada"?',
  '¿Alguna vez pensaste que tu cola "es así y no cambia"?'),
 ('Sí, lo pienso todo el tiempo', 'Sí, lo pienso todo el tiempo'),
 ('Sí, lo pensé algunas veces', 'Sí, se me cruzó varias veces'),
 ('A veces me siento así', 'Algún día malo, sí'),
 ('No, creo que puedo lograrlo', 'No, sé que se puede cambiar'),
 ('Nunca lo pensé', 'Nunca me lo planteé'),
]

# ---- 10 · cuanto tarda ---------------------------------------------------
P[10] = [
 ('¿Cuánto tardás en ver resultados con los entrenamientos tradicionales?',
  'Con lo que entrenaste hasta ahora, ¿en cuánto viste algún cambio?'),
 ('Nunca vi un resultado real', 'Nunca vi un cambio real'),
 ('Más de 6 meses (muchísimo tiempo)', 'Más de 6 meses, una eternidad'),
 ('3 a 6 meses (tarda demasiado)', 'Entre 3 y 6 meses, tardísimo'),
 ('1 a 3 meses (razonable)', 'Entre 1 y 3 meses, aceptable'),
 ('No sé, nunca entrené lo suficiente', 'Ni idea, nunca llegué tan lejos'),
]

# ---- 11 · ropa ajustada --------------------------------------------------
P[11] = [
 ('¿Te sentís insegura al usar ropa ajustada?', '¿Te da cosa ponerte ropa ajustada?'),
 ('¡Sí, muchísimo! Evito esa ropa', 'Muchísimo, directamente no la uso'),
 ('Sí, me siento bastante insegura', 'Bastante, me siento incómoda'),
 ('A veces me siento incómoda', 'A veces nomás'),
 ('Un poco, pero la uso igual', 'Un poco, pero me la pongo igual'),
 ('No, me siento segura', 'No, estoy cómoda con eso'),
]

# ---- 12 · plata gastada --------------------------------------------------
P[12] = [
 ('¿Alguna vez invertiste en entrenamientos, programas y gimnasios que no funcionaron?',
  '¿Ya pusiste plata en gimnasios o planes que no te sirvieron?'),
 ('¡Sí, ya gasté un montón y no tuve resultados!', 'Sí, gasté un montón al pedo'),
 ('Sí, ya lo intenté 3 veces o más', 'Sí, tres veces o más'),
 ('Sí, lo intenté 1 o 2 veces', 'Sí, una o dos veces'),
 ('No, pero me da miedo tirar la plata', 'No, y justamente me da miedo'),
 ('Nunca invertí en esto', 'Nunca gasté en esto'),
]

# ---- 13 · pileta / bikini ------------------------------------------------
P[13] = [
 ('¿Evitás ir a la playa, a la pileta o usar bikini por vergüenza de tu cuerpo?',
  '¿Esquivás la pileta, la playa o la malla por tu cuerpo?'),
 ('¡Sí, lo evito por completo!', 'Sí, directamente no voy'),
 ('Voy, pero me siento muy insegura', 'Voy, pero la paso incómoda'),
 ('A veces me siento incómoda', 'A veces me pasa'),
 ('Voy, pero me gustaría sentirme mejor', 'Voy, aunque me gustaría estar mejor'),
 ('Ya me sentí mejor antes...', 'Antes me sentía mejor que ahora'),
]

# ---- 14 · carga 2 --------------------------------------------------------
P[14] = [
 ('Identificando patrones en tus respuestas', 'Cruzando tus respuestas'),
 ('Dolores y frustraciones mapeados', 'Dolores y frenos mapeados'),
 ('Bloqueos identificados', 'Bloqueos detectados'),
 ('Perfil de comportamiento analizado', 'Perfil de constancia analizado'),
]

# ---- 15 · 6 meses --------------------------------------------------------
P[15] = [
 ('Si seguís como estás hoy, ¿cómo te ves dentro de 6 meses?',
  'Si todo sigue igual, ¿cómo te imaginás en 6 meses?'),
 ('Con la misma frustración, sin ningún resultado', 'Igual de frustrada, sin un solo cambio'),
 ('Todavía intentando y fallando', 'Probando y fallando otra vez'),
 ('Seguramente ya habré abandonado del todo', 'Ya habré largado todo'),
 ('Espero estar mejor, pero no sé cómo', 'Espero estar mejor, pero no sé cómo'),
 ('¡Voy a tener el cuerpo que quiero!', 'Con el cuerpo que quiero, seguro'),
]

# ---- 16 · tiempo perdido -------------------------------------------------
P[16] = [
 ('¿Cuánto tiempo calculás que ya perdiste probando entrenamientos que no funcionan?',
  '¿Cuánto tiempo calculás que ya tiraste en planes que no andaban?'),
 ('¡Muchísimo! Más de 3 años intentando', 'Un montón, más de 3 años'),
 ('1 a 3 años en el mismo ciclo', 'Entre 1 y 3 años dando vueltas'),
 ('6 meses a 1 año', 'De 6 meses a un año'),
 ('Algunos meses', 'Unos pocos meses'),
 ('Estoy empezando ahora', 'Recién estoy arrancando'),
]

# ---- 17 · otras mujeres --------------------------------------------------
P[17] = [
 ('¿Cómo te sentís cuando ves a otras mujeres con el cuerpo que vos querés?',
  '¿Qué sentís cuando ves a otra con el cuerpo que vos querés?'),
 ('Frustrada y con envidia', 'Frustración, y un poco de envidia'),
 ('Triste, porque creo que nunca lo voy a lograr', 'Tristeza, porque creo que yo no puedo'),
 ('Motivada, pero sin fe', 'Ganas, pero sin fe'),
 ('Inspirada y esperanzada', 'Inspiración, me dan ganas'),
 ('Feliz por ellas y decidida a lograrlo también', 'Alegría por ella y decisión por mí'),
]

# ---- 18 · dejaste de hacer algo -----------------------------------------
P[18] = [
 ('¿Alguna vez dejaste de hacer algo importante por la inseguridad con tu cuerpo?',
  '¿Te perdiste algo importante por no sentirte cómoda con tu cuerpo?'),
 ('Sí, muchas veces (eventos, viajes, citas)', 'Sí, un montón: salidas, viajes, citas'),
 ('Sí, algunas veces', 'Sí, algunas veces'),
 ('Una o dos veces', 'Una o dos veces'),
 ('Casi no voy, pero fui igual', 'Casi me lo pierdo, pero fui'),
 ('No, nunca dejé de hacer nada', 'No, nunca dejé de ir a nada'),
]

# ---- 19 · autoestima -----------------------------------------------------
P[19] = [
 ('¿Qué impacto tiene esa inseguridad en tu autoestima hoy?',
  '¿Cuánto te pega eso en la autoestima hoy?'),
 ('Muy alto - afecta todo en mi vida', 'Muchísimo, me condiciona todo'),
 ('Alto - lo pienso todos los días', 'Bastante, lo pienso todos los días'),
 ('Moderado - me molesta bastante', 'Lo justo, pero me molesta'),
 ('Bajo - puedo manejarlo', 'Poco, lo manejo'),
]

# ---- 20 · ignorarlo empeora ---------------------------------------------
P[20] = [
 ('¿Estás de acuerdo en que ignorar este problema solo va a empeorar todo con el tiempo?',
  '¿Coincidís en que dejarlo pasar lo único que hace es empeorarlo?'),
 ('¡Sí, totalmente! ¡Necesito cambiar YA!', '¡Totalmente! Necesito cambiarlo YA'),
 ('Sí, tiene sentido.', 'Sí, tiene sentido.'),
 ('Tal vez, no lo había pensado', 'Puede ser, no lo había pensado'),
]

# ---- 21 · que temes ------------------------------------------------------
P[21] = [
 ('Si nada cambia en los próximos meses, ¿qué es lo que más TEMÉS que pase?',
  'Si nada cambia en los próximos meses, ¿qué es lo que más MIEDO te da?'),
 ('¡Perder por completo la autoestima y dejar de cuidarme!',
  'Perder la autoestima del todo y dejar de cuidarme'),
 ('Seguir en este ciclo de frustración para siempre', 'Quedarme en este loop para siempre'),
 ('Rendirme de una vez y conformarme', 'Bajar los brazos y conformarme'),
 ('Que mi salud y mi bienestar empeoren', 'Que se me resienta la salud'),
]

# ---- 22 · carga 3 --------------------------------------------------------
P[22] = [
 ('Conectando tus necesidades con la solución ideal', 'Buscando el protocolo que te corresponde'),
 ('Impacto emocional medido', 'Nivel de urgencia medido'),
 ('Urgencia identificada', 'Bloqueo principal identificado'),
 ('Compromiso en análisis', 'Compromiso evaluado'),
]

# ---- 23 · forma comprobada ----------------------------------------------
P[23] = [
 ('Si existiera una forma COMPROBADA de tener piernas torneadas y la cola parada SIN SENTADILLAS, ¿la probarías?',
  'Si existiera una forma de levantar la cola SIN UNA SOLA SENTADILLA, ¿la probarías?'),
 ('¡SÍ! ¡Empezaría HOY mismo!', '¡SÍ! Arrancaría hoy mismo'),
 ('Sí, seguro que la probaría', 'Sí, la probaría sin dudar'),
 ('Sí, pero con algo de desconfianza', 'Sí, aunque con un poco de duda'),
 ('Tal vez, depende de qué sea', 'Depende de qué sea'),
]

# ---- 24 · 20 minutos -> 15 minutos --------------------------------------
P[24] = [
 ('¿Estarías dispuesta a dedicarle solo 20 minutos por día durante 4 semanas para tener el resultado que querés?',
  '¿Te bancás 15 minutos por día durante 28 días para lograrlo?'),
 ('¡SÍ! ¡Es poquito, lo hago fácil!', '¡SÍ! Son 15 minutos, los saco de donde sea'),
 ('Sí, 20 minutos es perfecto para mí', 'Sí, 15 minutos me cierra perfecto'),
 ('Sí, me voy a hacer el tiempo', 'Sí, me hago el tiempo'),
 ('Tal vez pueda', 'Capaz que sí'),
]

# ---- 25 · resultado mas importante --------------------------------------
P[25] = [
 ('¿Qué resultado sería el MÁS importante para vos en los próximos 30 días?',
  'En los próximos 30 días, ¿qué resultado te cambiaría el ánimo?'),
 ('¡Ver cómo se me levanta la cola a simple vista!', 'Ver la cola más parada en el espejo'),
 ('Sentir cómo mis piernas se ponen firmes y torneadas', 'Sentir las piernas firmes y marcadas'),
 ('Poder ponerme aquella ropa con confianza', 'Ponerme esa ropa sin pensarlo dos veces'),
 ('Recuperar mi autoestima y sentirme bien', 'Volver a sentirme bien conmigo'),
 ('Entrenar sin dolor y con resultados reales', 'Entrenar sin dolor y que se note'),
]

# ---- 26 · empezarias hoy -------------------------------------------------
P[26] = [
 ('Si te mostrara EXACTAMENTE cómo entrenar sin dolor de rodillas y tener resultados en 4 semanas, ¿empezarías HOY?',
  'Si te muestro EXACTAMENTE cómo despertar el glúteo en 28 días, ¿arrancás HOY?'),
 ('¡SÍ! ¡Estoy lista para empezar YA!', '¡SÍ! Estoy lista para arrancar YA'),
 ('Sí, empezaría hoy mismo', 'Sí, hoy mismo'),
 ('Sí, pero primero quiero ver cómo funciona', 'Sí, pero primero quiero ver cómo es'),
 ('Tal vez, lo tengo que pensar', 'Lo tengo que pensar'),
 ('No, prefiero quedarme como estoy', 'No, prefiero dejar todo como está'),
]

# ---- 27 · compromiso -----------------------------------------------------
P[27] = [
 ('¿Te COMPROMETÉS a seguir exactamente lo que te voy a mostrar para tener el cuerpo que siempre quisiste?',
  '¿Te COMPROMETÉS a seguir el protocolo exactamente como te lo doy?'),
 ('¡SÍ! ¡Estoy 100% comprometida!', '¡SÍ! Estoy 100% comprometida'),
 ('Sí, lo voy a seguir al pie de la letra', 'Sí, al pie de la letra'),
 ('Sí, voy a dar lo mejor de mí', 'Sí, voy a poner todo'),
 ('Tal vez, depende de qué sea', 'Depende de qué sea'),
]

# ---- 28 · diagnostico + VSL ---------------------------------------------
P[28] = [
 ('Diagnóstico completo', 'Tu diagnóstico está listo'),
 ('Analizamos tus respuestas e identificamos <strong class="morado">EXACTAMENTE</strong> qué es lo que te impide tener piernas torneadas y la cola parada.',
  'Cruzamos tus respuestas y encontramos <strong class="morado">EXACTAMENTE</strong> por qué tu cola no cambia aunque entrenes.'),
 ('3 patrones detectados', '1 músculo dormido'),
 ('1 mentira revelada', '1 mentira que te vendieron'),
 ('1 solución personalizada', '1 protocolo de 28 días'),
 ('<strong>¡Mirá el video de abajo para desbloquear el Truco de la Cola ahora!</strong>',
  '<strong>¡Mirá el video de abajo y te muestro el Protocolo del Glúteo Dormido!</strong>'),
 ('<p>&#x23F3; Estás a 30 segundos de conseguir</p><p>una cola y unas piernas lindas SIN SENTADILLAS</p>',
  '<p>&#x23F3; Estás a 30 segundos de entender</p><p>por qué tu glúteo no se enciende</p>'),
 ('<span>Quiero Mi Guía Ahora</span>', '<span>Quiero Mi Protocolo Ahora</span>'),
]

for k, pares in P.items():
    pasos[k] = rep(pasos[k], pares, 'paso %d' % k)

# ===========================================================================
# 4. LA OFERTA (el ultimo paso, que es el mas largo)
# ===========================================================================
OF = [
 ('¡Tu plan personalizado está listo!', '¡Tu Protocolo de 28 días está listo!'),
 ('Según tus respuestas, identificamos que podés <strong>conseguir piernas torneadas y la cola parada en 4 semanas</strong> &#x2014; incluso con rodillas sensibles.',
  'Según tus respuestas, podés <strong>despertar el glúteo y tener la cola parada en 28 días</strong> &#x2014; aunque tengas las rodillas sensibles.'),
 ('Aprovechá ahora tu descuento: ', 'Tu descuento queda guardado por: '),
 # la linea de cuotas de Mercado Pago va DEBAJO de la caja, no adentro:
 # metida en el <span> parte el precio en cinco renglones y desbalancea la caja.
 ('<span>en un solo pago</span></div></div>',
  '<span>en un solo pago</span></div></div>\n'
  '<p class="cuotas">o <strong>3 cuotas de AR$\u00a06.664</strong> con Mercado Pago</p>'),
 ('<span>Quiero Transformar Mis Piernas y Cola en 4 Semanas</span>',
  '<span>Quiero Despertar Mi Glúteo en 28 Días</span>'),
 ('alt="Compra segura, satisfacción garantizada, privacidad protegida"',
  'alt="Compra segura, satisfacción garantizada, privacidad protegida"'),
 # la caja de precio PARECE un boton (verde, con borde y radio): tiene que
 # llevar al checkout como cualquier CTA. En el original no llevaba a nada.
 ('<div class="precio">', '<div class="precio" data-cta>'),
 ('<p class="caja-tit">Lo que vas a recibir</p>', '<p class="caja-tit">Lo que te llevás hoy</p>'),
 ('<strong>Método Anti-Lesión</strong>: La técnica exacta para tonificar glúteos y piernas protegiendo tus rodillas de cualquier impacto;',
  '<strong>Fase 1 &#x2014; Despertar</strong>: los 7 días que vuelven a encender el glúteo antes de pedirle que crezca;'),
 ('<strong>Rutina Express de 20 Minutos</strong>: Entrenamientos rápidos enfocados en hipertrofia femenina para las que viven a las corridas;',
  '<strong>Fase 2 &#x2014; Aislar</strong>: 15 minutos por día de movimientos que el cuádriceps no le puede robar al glúteo;'),
 ('<strong>Protocolo "Sin Sentadillas"</strong>: Reemplazamos los ejercicios peligrosos por movimientos aislados que activan 3x más el glúteo;',
  '<strong>Fase 3 &#x2014; Cargar</strong>: las 10 sesiones finales, donde la cola termina de pararse. Ni una sentadilla en los 28 días;'),
 ('<strong>Bonus Exclusivo</strong>: Cronograma de 4 semanas para acelerar la quema de grasa localizada y la celulitis.',
  '<strong>Bonus</strong>: el cronograma de los 28 días, día por día, para imprimir y colgar en la heladera.'),
 ('<span>Quiero Empezar Mi Transformación</span>', '<span>Quiero Empezar Hoy</span>'),
 ('Las que siguieron el plan, tuvieron resultados:', 'Las que ya hicieron los 28 días:'),
 # testimonios
 ('alt="Mariana Torres"', 'alt="Mariana T. de Rosario"'),
 ('<div class="autor">Mariana Torres</div>', '<div class="autor">Mariana T. &#x2014; Rosario</div>'),
 ('<div class="desc">¡Por fin encontré algo que no me hace mierda las rodillas!</div>',
  '<div class="desc">¡Por fin algo que no me deja las rodillas hechas pelota!</div>'),
 ('alt="Ana Clara T."', 'alt="Ana Clara G. de La Plata"'),
 ('<div class="autor">Ana Clara T.</div>', '<div class="autor">Ana Clara G. &#x2014; La Plata</div>'),
 ('<div class="desc">Tenía mucho dolor de rodilla y había dejado de entrenar piernas. Esta guía me salvó la autoestima, pero me trajo un problema: ¡la cola ya no me entra en los pantalones viejos! &#x1F605;</div>',
  '<div class="desc">Había dejado piernas por la rodilla. A la semana ya sentía el glúteo trabajando, cosa que nunca me había pasado. Ahora tengo otro problema: los jeans viejos no me entran atrás. &#x1F605;</div>'),
 ('alt="Clara Martínez"', 'alt="Valeria S. de Córdoba"'),
 ('<div class="autor">Clara Martínez</div>', '<div class="autor">Valeria S. &#x2014; Córdoba</div>'),
 ('<div class="desc">Mi personal decía que sin las pesas del gimnasio no había resultado. ¡Estaba equivocado! La Guía quema un montón, las piernas quedan duritas y mi cola está claramente feliz jajaja. Valió cada peso.</div>',
  '<div class="desc">Mi entrenador decía que sin las máquinas del gimnasio no había caso. Mentira. Lo hice en el living, 15 minutos por día, y las piernas quedaron durísimas. Valió cada peso.</div>'),
 ('<span>Quiero Mi Cola Parada</span>', '<span>Quiero Empezar la Fase 1</span>'),
 # antes / despues
 ('<p class="caja-tit">Antes de comprar</p>', '<p class="caja-tit">Como venís hasta hoy</p>'),
 ('<span>Dolor de rodillas</span>', '<span>Las rodillas te frenan antes que las piernas</span>'),
 ('<span>Vergüenza de usar bikini y ropa ajustada</span>',
  '<span>Esquivás la malla y la ropa ajustada</span>'),
 ('<span>Horas perdidas en el gimnasio sin ver resultados</span>',
  '<span>Horas de gimnasio sin un solo cambio</span>'),
 ('<span>Frustración con la flacidez de la cara interna del muslo</span>',
  '<span>El glúteo dormido y el cuádriceps haciendo todo el trabajo</span>'),
 ('<p class="caja-tit">Después de la Guía Piernas y Cola Sin Sentadillas</p>',
  '<p class="caja-tit">Después de los 28 días de Glúteo Despierto</p>'),
 ('<span>Piernas firmes y marcadas</span>', '<span>Piernas firmes y la cola parada</span>'),
 ('<span>Confianza al mirarte al espejo</span>', '<span>Te mirás al espejo y te gusta</span>'),
 ('<span>Ejercicios que protegen tus articulaciones</span>',
  '<span>Cero sentadillas, cero impacto en las rodillas</span>'),
 ('<span>Cola redondita y feliz</span>', '<span>15 minutos por día, en el living de tu casa</span>'),
 ('<span>Quiero Piernas Marcadas</span>', '<span>Quiero Las Piernas Firmes</span>'),
 # FAQ
 ('<h3>¿Funciona aunque no haga sentadillas?</h3>', '<h3>¿Funciona sin hacer ni una sentadilla?</h3>'),
 ('<p>¡Sí! El Método activa los músculos de las piernas y los glúteos con ejercicios sin impacto, que incluso son más eficaces para quienes tienen las rodillas sensibles.</p>',
  '<p>¡Sí! El Protocolo trabaja el glúteo con movimientos que nacen en la cadera, sin impacto. Son los que más lo activan y, encima, los más cómodos para rodillas sensibles. La sentadilla no aparece en ninguno de los 28 días.</p>'),
 ('<h3>¿Cuánto tiempo para ver resultados?</h3>', '<h3>¿En cuánto se empieza a notar?</h3>'),
 ('<p>Los resultados visibles de tono muscular se pueden notar ya en las primeras semanas de dedicación al plan de 20 minutos.</p>',
  '<p>La mayoría siente el glúteo trabajando en la primera semana &#x2014; que es justamente para lo que está la Fase 1. Lo que se ve en el espejo llega después, con las fases 2 y 3.</p>'),
 ('<h3>Tengo condromalacia/dolor de rodilla, ¿puedo hacerlo?</h3>',
  '<h3>Tengo condromalacia o dolor de rodilla, ¿puedo hacerlo?</h3>'),
 ('<p>¡Sí! La guía fue diseñada específicamente para eliminar la compresión articular de la sentadilla tradicional, enfocándose en ejercicios seguros.</p>',
  '<p>¡Sí! Para eso está armado así: sacamos todo lo que comprime la rodilla y dejamos lo que trabaja desde la cadera. Si tenés una lesión diagnosticada, mostrale el plan a tu médico antes de arrancar.</p>'),
 ('<h3>¿Necesito equipamiento?</h3>', '<h3>¿Necesito pesas o máquinas?</h3>'),
 ('<p>No. El método es 100% adaptable para hacerlo en casa solo con el peso del cuerpo o con objetos simples de la casa.</p>',
  '<p>No. Todo se hace con el peso del cuerpo o con cosas que ya tenés en casa: una silla, una toalla, una mochila.</p>\n<hr>\n<h3>¿Es una suscripción?</h3>\n<p>No. Es un pago \u00fanico de AR$\u00a019.990 con acceso de por vida. No hay mensualidad ni renovación automática.</p>'),
 # garantia
 ('Riesgo CERO con nuestra Garantía Blindada', 'Riesgo CERO: 30 días de garantía'),
 ('Tenés 30 días para probar la Guía Piernas y Cola Sin Sentadillas. Si no sentís que tus piernas trabajan de verdad o no te gusta el contenido, te devolvemos el 100% de tu plata. ',
  'Tenés 30 días para probar Glúteo Despierto. Si no sentís el glúteo trabajando de verdad, o simplemente no te gusta, te devolvemos el 100% de tu plata. '),
 ('<span>Quiero Mi Gu\u00eda Por AR$\u00a019.990</span>', '<span>Quiero Mi Protocolo Por AR$\u00a019.990</span>'),
 # alts sueltos
 ('alt="Resultado: antes y después de la Guía"', 'alt="Antes y después de los 28 días"'),
 ('alt="Resultado: cola más firme en 4 semanas"', 'alt="Cola más firme en 28 días"'),
 ('alt="Antes y después sin sentadillas"', 'alt="Antes y después, sin una sola sentadilla"'),
 ('alt="Resultado de la Guía Piernas y Cola Sin Sentadillas"', 'alt="Resultado del Protocolo del Glúteo Dormido"'),
]
pasos[29] = rep(pasos[29], OF, 'oferta')

# ===========================================================================
# 5. CONFIGURACION — todo lo que se toca, arriba del script (regla §8.5)
# ===========================================================================
cola = rep(cola, [
 ('var VTURB_CUENTA = "";      /* VTurb: id de la cuenta (scripts.converteai.net/CUENTA/players/PLAYER/v4/player.js) */',
  '/* ===== LO QUE SE TOCA =====\n'
  '   CHECKOUT  : el ÚNICO lugar con la URL de pago. Puede ser absoluta\n'
  '               ("https://tu-tienda.impultienda.ar/checkout") o relativa\n'
  '               ("/checkout", que resuelve a la tienda donde se pegue esto).\n'
  '   PIXEL_ID  : vacío si el pixel lo carga ImpulTienda.\n'
  '   BOTON_SEGUNDO: 0 = el botón del diagnóstico se ve de entrada.\n'
  '   Las imágenes cuelgan de ../imagenes/ y se embeben con inline_quiz.py. */\n'
  'var CHECKOUT = "' + CHECKOUT_URL + '";\n'
  'var PIXEL_ID = "";\n'
  'var VTURB_CUENTA = "";      /* VTurb: id de la cuenta (scripts.converteai.net/CUENTA/players/PLAYER/v4/player.js) */'),
 ('var VSL_MP4 = "";',
  'var VSL_MP4 = "";           /* el MP4 de nuestro VSL, cuando esté */'),
], 'config')

# ---------------------------------------------------------------------------
# El bloque de checkout del competidor se reemplaza entero. El suyo hacia
#   a.setAttribute("href", u.pathname + u.search)
# que TIRA EL HOST: con un checkout en otro dominio, el link se rompia al
# tocarlo. Ademas solo completaba en el click, y la caja de precio — que
# parece un boton — no llevaba a ningun lado.
# ---------------------------------------------------------------------------
viejo_checkout = cola[cola.index('/* ===== CHECKOUT:'): cola.index('/* ===== ARRANQUE:')]
nuevo_checkout = '''/* ===== CHECKOUT ==========================================================
   Un solo lugar con la URL (CHECKOUT). Todo lo que lleva al pago nace con
   ella puesta desde que carga la pagina, no recien al tocarla, y le suma los
   parametros de la visita (UTMs, fbclid). Idempotente: no engancha dos veces.
   ========================================================================= */
function urlCheckout() {
try {
var u = new URL(CHECKOUT, location.origin);
if (params) params.forEach(function (v, k) {
if (k !== "paso" && v && !u.searchParams.get(k)) u.searchParams.set(k, v);
});
return u.href;
} catch (e) { return CHECKOUT; }
}
function ligarCTAs() {
var url = urlCheckout();
[].forEach.call(document.querySelectorAll('a[href^="/checkout"], a[data-cta], [data-cta]'), function (el) {
if (el.tagName === "A") { el.setAttribute("href", url); el.setAttribute("rel", "noopener"); }
else { el.style.cursor = "pointer"; }
if (el.getAttribute("data-ligado")) return;
el.setAttribute("data-ligado", "1");
el.addEventListener("click", function (e) {
track("checkout_click");
if (PIXEL_ID && window.fbq) { try { fbq("track", "AddToCart"); } catch (x) {} }
if (el.tagName !== "A") { e.preventDefault(); location.href = urlCheckout(); }
});
});
}
ligarCTAs();
'''
cola = cola.replace(viejo_checkout, nuevo_checkout, 1)

# el pixel, al final del script (el AddToCart ya lo dispara ligarCTAs)
cola = cola.replace('})();\n</script>',
 '''if (PIXEL_ID) {
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");
fbq("init", PIXEL_ID); fbq("track","PageView");
}
})();
</script>''', 1)

# ===========================================================================
# 6. ARMAR Y CONTROLAR
# ===========================================================================
final = cabecera + ''.join(pasos) + cola

# ningun rastro del competidor
SOSPECHOSAS = ['Guía Piernas y Cola', 'Truco de la Cola', 'Método Anti-Lesión', 'Mariana Torres',
               'Clara Martínez', 'aekpgsbqjzqntlbucbts', 'pc-logo', 'pc-portada', 'Bumbum',
               '20 minutos', 'Guia Piernas']
for s in SOSPECHOSAS:
    if s in final:
        fallos.append('QUEDO TEXTO DEL COMPETIDOR :: %s (x%d)' % (s, final.count(s)))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(final)

print('escrito:', OUT, len(final), 'chars')
print('pasos:', len(pasos))
if fallos:
    print('\n--- %d PROBLEMAS ---' % len(fallos))
    for f in fallos: print(' ', f)
    sys.exit(1)
print('\nsin problemas')
