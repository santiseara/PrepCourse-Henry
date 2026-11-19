# -*- coding: utf-8 -*-
"""Pasa el quiz de Helados que Venden (AR, heladosquevenden.impultienda.ar) a LATAM neutro.

Sigue la regla del 14/11 de quizzes-reglas-de-armado: se construye SOBRE SU DOCUMENTO
(su <style>, su markup y su motor sin tocar una regla) y solo cambian las palabras,
las imagenes con texto argentino y el bloque de configuracion.
Cada par tiene que matchear: si uno falla, el script corta.

Uso: python3 build_helados_latam.py
"""
import os, re, sys

SRC = os.path.expanduser('~/Desktop/helados/landing/index.html')
OUT = os.path.expanduser('~/Desktop/helados/landing/quiz_latam.html')

h = open(SRC, encoding='utf-8').read()
ini = h.index('<style>\n:root{\n--bg:#FFF7F3')
fin = h.index('</script>', h.index("<script>\n(function ()")) + len('</script>')
doc = h[ini:fin]
print('bloque original:', len(doc), 'bytes')

# ---------------------------------------------------------------- precios
# AR$ -> USD (LATAM neutro, pago unico). Los valores salen del CONFIG de ellos.
PRECIOS = [
    ("precio: '$16.990', precioAntes: '$177.900', ahorro: '$160.910',",
     "precio: 'US$ 12', precioAntes: 'US$ 136,90', ahorro: 'US$ 124,90',"),
    ("vProductos: '$124.950', vBonos: '$52.950',",
     "vProductos: 'US$ 94,95', vBonos: 'US$ 41,95',"),
    ("v1: '$39.990', v2: '$24.990', v3: '$19.990', v4: '$19.990', v5: '$19.990',",
     "v1: 'US$ 29,99', v2: 'US$ 19,99', v3: 'US$ 14,99', v4: 'US$ 14,99', v5: 'US$ 14,99',"),
    ("b1: '$12.990', b2: '$9.990', b3: '$9.990', b4: '$9.990', b5: '$9.990',",
     "b1: 'US$ 9,99', b2: 'US$ 7,99', b3: 'US$ 7,99', b4: 'US$ 7,99', b5: 'US$ 7,99',"),
    ("costoPote: '$2.000', precioPote: '$6.000', tresPotes: '$18.000', total: '$120.000'",
     "costoPote: 'US$ 1,50', precioPote: 'US$ 5', tresPotes: 'US$ 15', total: 'US$ 100'"),
]

# ------------------------------------------------- textos (voseo -> neutro)
TEXTOS = [
    # ---- pantalla 1
    ('Helado en pote con <span class="tag">base italiana</span>',
     'Helado en vasito con <span class="tag">base italiana</span>'),
    ('Aprendé a hacerlo en tu casa y vendelo para fin de año',
     'Aprende a hacerlo en tu casa y véndelo para fin de año'),
    ('Helados en pote + Postres de las Fiestas + Palitos + Saludables + Kit Vendé',
     'Helados en vasito + Postres de las Fiestas + Paletas + Saludables + Kit Vende'),
    ('adaptada para que la hagas en tu casa y <b>empieces a vender.</b>',
     'adaptada para que la hagas en tu casa y <b>empieces a vender.</b>'),
    ('No hace falta que arranques sabiendo todo.',
     'No hace falta que empieces sabiendo todo.'),
    ('✅ +100 recetas de helado en pote + postres helados de las Fiestas',
     '✅ +100 recetas de helado en vasito + postres helados de las Fiestas'),
    ('✅ A calcular los costos y ponerle precio al pote',
     '✅ A calcular los costos y ponerle precio al vasito'),
    ('✅ Cómo vender en las fiestas y las juntadas de fin de año',
     '✅ Cómo vender en las fiestas y las reuniones de fin de año'),
    ('Respondé 2 preguntas rápidas y te armamos tu plan para preparar —y vender— tus primeros potes',
     'Responde 2 preguntas rápidas y te armamos tu plan para preparar —y vender— tus primeros vasitos'),
    # ---- pantalla 2 y 3
    ('¿Cuánto tiempo le podés dedicar a tus helados?',
     '¿Cuánto tiempo le puedes dedicar a tus helados?'),
    ('¿Qué es lo que más te frena para arrancar?',
     '¿Qué es lo que más te frena para empezar?'),
    ('No sé cuánto cobrar el pote', 'No sé cuánto cobrar el vasito'),
    # ---- pantalla 4
    ('Y tampoco necesitás experiencia en pastelería',
     'Y tampoco necesitas experiencia en repostería'),
    ('Recibís el paso a paso para arrancar de cero:',
     'Recibes el paso a paso para empezar de cero:'),
    ('<b>Terminación:</b> los detalles para un resultado lindo y cremoso',
     '<b>Terminación:</b> los detalles para un resultado bonito y cremoso'),
    ('<b>Precios:</b> cómo calcular tus costos y ponerle precio al pote',
     '<b>Precios:</b> cómo calcular tus costos y ponerle precio al vasito'),
    ('<b>Venta:</b> cómo presentar tus potes y cerrar pedidos de fin de año',
     '<b>Venta:</b> cómo presentar tus vasitos y cerrar pedidos de fin de año'),
    ('¡Sí! Quiero hacer mi primer pote', '¡Sí! Quiero hacer mi primer vasito'),
    # ---- pantalla 5
    ('Después de la base, <b>terminás cada sabor a tu manera</b>: frutilla a la crema, maracuyá, clásicos y especiales.',
     'Después de la base, <b>terminas cada sabor a tu manera</b>: fresa a la crema, maracuyá, clásicos y especiales.'),
    ('El resultado: helados en pote con una terminación prolija, <b>una pinta que da ganas</b> y listos para vender.',
     'El resultado: helados en vasito con una terminación pareja, <b>que dan ganas apenas los ves</b> y listos para vender.'),
    # ---- pantalla 6
    ('Mirá lo que dicen nuestros alumnos', 'Mira lo que dicen nuestros alumnos'),
    ('“Siempre quise tener una plata que fuera mía.',
     '“Siempre quise tener un ingreso que fuera mío.'),
    ('“Mi señora siempre quiso tener un ingreso propio, pero nunca sabía por dónde arrancar.',
     '“Mi esposa siempre quiso tener un ingreso propio, pero nunca sabía por dónde empezar.'),
    ('“Ya había dejado de buscar algo que me funcionara. Acá pude entender el camino, desde la base hasta el precio del pote.',
     '“Ya había dejado de buscar algo que me funcionara. Aquí pude entender el camino, desde la base hasta el precio del vasito.'),
    ('Frutilla a la crema', 'Fresa a la crema'),
    ('¡Ahora te toca a vos!', '¡Ahora te toca a ti!'),
    ('Si llegaste hasta acá, ya tenés lo más importante:',
     'Si llegaste hasta aquí, ya tienes lo más importante:'),
    ('No hace falta que arranques sabiendo todo: <span class="t-rose">el paso a paso te lleva desde la base hasta el precio del pote.</span>',
     'No hace falta que empieces sabiendo todo: <span class="t-rose">el paso a paso te lleva desde la base hasta el precio del vasito.</span>'),
    ('¡Estoy lista! Mostrame mi plan', '¡Estoy lista! Muéstrame mi plan'),
    # ---- pantalla 7
    ('¡Estás a un paso de <span class="hl">tus primeros potes!</span>',
     '¡Estás a un paso de <span class="hl">tus primeros vasitos!</span>'),
    # ---- pantalla 8 · productos
    ('Recetario Maestro: Base Italiana + 100 Helados en Pote',
     'Recetario Maestro: Base Italiana + 100 Helados en Vasito'),
    ('Almendrado, bombón suizo, semifríos y helado de pan dulce: el postre frío de Navidad y Año Nuevo.',
     'Torta helada, bombón suizo, semifríos y helado de panettone: el postre frío de Navidad y Año Nuevo.'),
    ('Palitos y Helados de Agua', 'Paletas y Helados de Agua'),
    ('Palitos frutales y de crema, baratos de hacer y los que más piden los chicos en verano.',
     'Paletas de fruta y de crema, económicas de hacer y las que más piden los niños en verano.'),
    ('Helados Saludables: Sin Azúcar, Sin TACC y Veganos',
     'Helados Saludables: Sin Azúcar, Sin Gluten y Veganos'),
    ('Kit Vendé desde tu Casa', 'Kit Vende desde tu Casa'),
    ('Cómo ponerle precio, presentar, envasar y entregar tus potes, con 30 mensajes de WhatsApp listos para cerrar pedidos.',
     'Cómo ponerle precio, presentar, envasar y entregar tus vasitos, con 30 mensajes de WhatsApp listos para cerrar pedidos.'),
    ('🎁 Y si entrás hoy, te llevás 5 bonos GRATIS:',
     '🎁 Y si entras hoy, te llevas 5 bonos GRATIS:'),
    # ---- pantalla 8 · bonos
    ('cargás tus ingredientes y te dice cuánto cobrar cada pote. Chau a «no sé cuánto cobrar».',
     'cargas tus ingredientes y te dice cuánto cobrar cada vasito. Adiós al «no sé cuánto cobrar».'),
    ('los trucos para que no se haga escarcha ni cristales y quede cremoso como el de heladería. Chau a «¿y si no me sale?».',
     'los trucos para que no se haga escarcha ni cristales y quede cremoso como el de heladería. Adiós al «¿y si no me sale?».'),
    ('elegí un diseño, poné tus sabores y mandalo por WhatsApp para tomar pedidos.',
     'elige un diseño, pon tus sabores y mándalo por WhatsApp para tomar pedidos.'),
    ('<b>Vendé Helados en Regla</b> — carnet de manipulador de alimentos, bromatología de tu municipio y monotributo, explicado simple. Chau a «¿se puede vender helado casero?».',
     '<b>Envasado y Entrega</b> — qué envase usar, cómo etiquetar, cuánto dura en el congelador y cómo entregar sin que se derrita. Adiós al «¿y si se me arruina en el camino?».'),
    # ---- pantalla 8 · cuenta
    ('Se paga sola con 3 potes', 'Se paga sola con 3 vasitos'),
    ('Si vendés cada pote a', 'Si vendes cada vasito a'),
    ('3 potes', '3 vasitos'),
    ('Recuperás lo que pagaste con tu primera tanda, y todo lo que vendas después es tuyo.',
     'Recuperas lo que pagaste con tu primera tanda, y todo lo que vendas después es tuyo.'),
    ('Acceso inmediato · Pagá con Mercado Pago o tarjeta',
     'Acceso inmediato · Paga con tarjeta o con el medio de pago de tu país'),
    ('Ingredientes de un pote', 'Ingredientes de un vasito'),
    ('Lo que se cobra un pote casero', 'Lo que se cobra un vasito casero'),
    ('Vendé 20 potes en las fiestas', 'Vende 20 vasitos en las fiestas'),
    ('Ejemplo ilustrativo: tus precios y resultados pueden variar.',
     'Ejemplo ilustrativo: tus precios y resultados pueden variar según tu país.'),
    ('Todo el contenido <em>ordenado para vos</em>', 'Todo el contenido <em>ordenado para ti</em>'),
    ('de tus helados en pote.', 'de tus helados en vasito.'),
    ('Aprendés la base italiana, seguís el paso a paso y tenés un material para consultar <span class="t-rose">siempre que lo necesites</span>',
     'Aprendes la base italiana, sigues el paso a paso y tienes un material para consultar <span class="t-rose">siempre que lo necesites</span>'),
    ('Mirá el resultado que vas a aprender a preparar:',
     'Mira el resultado que vas a aprender a preparar:'),
    # ---- pantalla 8 · testimonios
    ('“Hice el pote de frutilla a la crema para el cumple de mi hija y voló en minutos. Todos me preguntaron dónde lo había comprado.”',
     '“Hice el vasito de fresa a la crema para el cumpleaños de mi hija y voló en minutos. Todos me preguntaron dónde lo había comprado.”'),
    ('“Arranqué con una tanda para los vecinos y ya tengo pedidos para todos los fines de semana. El paso a paso es fácil de seguir.”',
     '“Empecé con una tanda para los vecinos y ya tengo pedidos para todos los fines de semana. El paso a paso es fácil de seguir.”'),
    ('“Los potes quedan hermosos y muy presentables para entregar. Ya los llevé de regalo y todos pensaron que eran de heladería.”',
     '“Los vasitos quedan hermosos y muy presentables para entregar. Ya los llevé de regalo y todos pensaron que eran de heladería.”'),
    ('Lo que dicen quienes ya hacen helado en casa', 'Lo que dicen quienes ya hacen helado en casa'),
    # ---- pantalla 8 · garantia
    ('Entrá, hacé tus primeras tandas y probá vender. Si en 30 días sentís que no era para vos, nos escribís y <b>te devolvemos el 100 % de tu plata.</b>',
     'Entra, haz tus primeras tandas y prueba vender. Si en 30 días sientes que no era para ti, nos escribes y <b>te devolvemos el 100 % de tu dinero.</b>'),
    ('O te encanta, o no pagás nada.', 'O te encanta, o no pagas nada.'),
    # ---- pantalla 8 · FAQ
    ('¿Necesito tener experiencia en pastelería?', '¿Necesito tener experiencia en repostería?'),
    ('¿Tengo garantía?', '¿Tengo garantía?'),
    ('Sí, de 30 días. Si no es para vos, nos escribís y te devolvemos el 100 %.',
     'Sí, de 30 días. Si no es para ti, nos escribes y te devolvemos el 100 %.'),
    ('¿Puedo vender helado casero en Argentina?', '¿Puedo vender el helado que preparo?'),
    ('Sí. El bono Vendé Helados en Regla te explica, paso a paso, el carnet de manipulador de alimentos, lo que pide bromatología en tu municipio y el monotributo.',
     'Sí. El Kit Vende desde tu Casa te explica cómo presentarlo, envasarlo y entregarlo, y el bono de Envasado y Entrega, cómo conservarlo para que llegue perfecto. Los permisos para vender comida dependen de cada país y ciudad: conviene consultarlos en tu municipio.'),
    ('¿Cuánto cobro cada pote?', '¿Cuánto cobro cada vasito?'),
    ('Depende de tu zona y de tus costos. Con la Planilla de Costos y Precios cargás lo que gastaste y te dice a cuánto venderlo para que te quede ganancia.',
     'Depende de tu país, tu zona y tus costos. Con la Planilla de Costos y Precios cargas lo que gastaste y te dice a cuánto venderlo para que te quede ganancia.'),
    ('Sí. La base italiana y la Guía Cremoso sin Máquina están pensadas para que no se haga escarcha ni cristales, con lo que tenés en tu cocina.',
     'Sí. La base italiana y la Guía Cremoso sin Máquina están pensadas para que no se haga escarcha ni cristales, con lo que tienes en tu cocina.'),
    ('Los 5 productos del Combo (Recetario Maestro, Postres Helados de las Fiestas, Paletas y Helados de Agua, Helados Saludables y Kit Vende desde tu Casa) más los 5 bonos',
     'Los 5 productos del Combo (Recetario Maestro, Postres Helados de las Fiestas, Paletas y Helados de Agua, Helados Saludables y Kit Vende desde tu Casa) más los 5 bonos de regalo'),
    # ---- pantalla 8 · cierre
    ('Tu primer helado en pote <em>puede empezar acá</em>', 'Tu primer helado en vasito <em>puede empezar aquí</em>'),
    ('Aprendé la base italiana, seguí el paso a paso y tené un material para consultar siempre que lo necesites, <b>a tiempo para los pedidos de fin de año.</b>',
     'Aprende la base italiana, sigue el paso a paso y ten un material para consultar siempre que lo necesites, <b>a tiempo para los pedidos de fin de año.</b>'),
    # ---- legales
    ('Podés vender los helados que prepares con las recetas. No podés comp',
     'Puedes vender los helados que prepares con las recetas. No puedes comp'),
    # ---- motor (PLAN y carga)
    ('preparás la base, terminás los sabores y vas armando tus pedidos.',
     'preparas la base, terminas los sabores y vas armando tus pedidos.'),
    ('<b>Empezá por la base italiana y la Guía Cremoso sin Máquina</b>',
     '<b>Empieza por la base italiana y la Guía Cremoso sin Máquina</b>'),
    ('<b>Empezá por la Planilla de Costos y Precios</b>: cargás tus ingredientes y te dice cuánto cobrar cada pote.',
     '<b>Empieza por la Planilla de Costos y Precios</b>: cargas tus ingredientes y te dice cuánto cobrar cada vasito.'),
    ('<b>Empezá por el Kit Vende desde tu Casa</b>', '<b>Empieza por el Kit Vende desde tu Casa</b>'),
]

def aplicar(txt, pares, etiqueta):
    faltan = []
    for a, b in pares:
        if a not in txt:
            faltan.append(a)
            continue
        txt = txt.replace(a, b)
    if faltan:
        print(f'\n⛔ {etiqueta}: {len(faltan)} pares NO matchearon:')
        for f in faltan:
            print('   ·', repr(f[:110]))
        sys.exit(1)
    return txt

doc = aplicar(doc, PRECIOS, 'precios')
doc = aplicar(doc, TEXTOS, 'textos')

# ---------------------------------- segunda tanda: plantillas, legales y alts
TEXTOS2 = [
    # precios de respaldo dentro de los <template> (el JS los pisa con CONFIG, pero parpadean)
    ('<div class="off">AHORRÁS <span data-m="ahorro">$160.910</span></div>',
     '<div class="off">AHORRAS <span data-m="ahorro">US$ 124,90</span></div>'),
    ('<div class="from">Valor total <s data-m="precioAntes">$177.900</s></div>',
     '<div class="from">Valor total <s data-m="precioAntes">US$ 136,90</s></div>'),
    ('<div class="now" data-m="precio">$16.990</div>', '<div class="now" data-m="precio">US$ 12</div>'),
    ('<span class="pill" data-m="precio">$16.990</span>', '<span class="pill" data-m="precio">US$ 12</span>'),
    ('🍓 Menos de lo que cobrás por 3 vasitos de helado', '🍓 Menos de lo que cobras por 3 vasitos de helado'),
    ('🔒 Pago seguro · Garantía de 30 días o te devolvemos tu plata',
     '🔒 Pago seguro · Garantía de 30 días o te devolvemos tu dinero'),
    ('tu precio de lanzamiento sigue reservado, aprovechalo ahora',
     'tu precio de lanzamiento sigue reservado, aprovéchalo ahora'),
    # bonos: los valores tachados de las tarjetas
    ('<s data-m="b1">$12.990</s>', '<s data-m="b1">US$ 9,99</s>'),
    ('<s data-m="b2">$9.990</s>', '<s data-m="b2">US$ 7,99</s>'),
    ('<s data-m="b3">$9.990</s>', '<s data-m="b3">US$ 7,99</s>'),
    ('<s data-m="b4">$9.990</s>', '<s data-m="b4">US$ 7,99</s>'),
    ('<s data-m="b5">$9.990</s>', '<s data-m="b5">US$ 7,99</s>'),
    # bono 5 nuevo
    ('data-alt="Bono 5 · Vendé Helados en Regla"', 'data-alt="Bono 5 · Envasado y Entrega"'),
    # legales
    ('Si el material no es para vos, escribinos dentro de los 30 días posteriores a la compra',
     'Si el material no es para ti, escríbenos dentro de los 30 días posteriores a la compra'),
    ('El nombre y el email que cargás en el checkout.', 'El nombre y el correo que cargas en el checkout.'),
    ('Para entregarte tu compra, mandarte el acceso, responder tus consultas y gestionar la garantía.',
     'Para entregarte tu compra, enviarte el acceso, responder tus consultas y gestionar la garantía.'),
    ('Podés manejar las cookies desde tu navegador.', 'Puedes manejar las cookies desde tu navegador.'),
    ('Podés pedirnos ver, corregir o borrar tus datos cuando quieras.',
     'Puedes pedirnos ver, corregir o borrar tus datos cuando quieras.'),
    ('Tus resultados dependen de tu dedicación, tus precios y la demanda de tu zona.',
     'Tus resultados dependen de tu dedicación, tus precios y la demanda de tu zona.'),
    # motor
    ('tu primera base esta semana y tus primeros potes listos para ofrecer antes de las fiestas.',
     'tu primera base esta semana y tus primeros vasitos listos para ofrecer antes de las fiestas.'),
    # sello de pago argentino (Mercado Pago, Naranja X, Cabal) -> el nuestro, neutro
    ('src="https://cdn.impultienda.ar/store-resources/626b1144-c6ee-4928-a7a7-b3390d1ef56e/1793972014299_10-sello-compra-segura-278c4014.webp" alt="Compra 100% segura: Visa, Mastercard, American Express, Mercado Pago, Naranja X, Cabal"',
     'src="IMG_SELLO_PAGO" alt="Compra 100 % segura: Visa, Mastercard, American Express y los medios de pago de tu país"'),
    ('IMAGEN 13 · Freezer con potes', 'IMAGEN 13 · Congelador con vasitos'),
    ('<td data-m="vProductos">$124.950</td>', '<td data-m="vProductos">US$ 94,95</td>'),
    ('<td data-m="vBonos">$52.950</td>', '<td data-m="vBonos">US$ 41,95</td>'),
    ('<s data-m="precioAntes">$177.900</s>', '<s data-m="precioAntes">US$ 136,90</s>'),
    ('<tr class="h"><td>Hoy pagás</td><td data-m="precio">$16.990</td></tr>',
     '<tr class="h"><td>Hoy pagas</td><td data-m="precio">US$ 12</td></tr>'),
    ('<b data-m="precioPote">$6.000</b>', '<b data-m="precioPote">US$ 5</b>'),
    ('<span data-m="tresPotes">$18.000</span>', '<span data-m="tresPotes">US$ 15</span>'),
    ('el Combo: <b data-m="precio">$16.990</b>', 'el Combo: <b data-m="precio">US$ 12</b>'),
    ('<s data-m="v1">$39.990</s>', '<s data-m="v1">US$ 29,99</s>'),
    ('<s data-m="v2">$24.990</s>', '<s data-m="v2">US$ 19,99</s>'),
    ('<s data-m="v3">$19.990</s>', '<s data-m="v3">US$ 14,99</s>'),
    ('<s data-m="v4">$19.990</s>', '<s data-m="v4">US$ 14,99</s>'),
    ('<s data-m="v5">$19.990</s>', '<s data-m="v5">US$ 14,99</s>'),
    ('<span data-m="costoPote">$2.000</span>', '<span data-m="costoPote">US$ 1,50</span>'),
    ('<span data-m="precioPote">$6.000</span>', '<span data-m="precioPote">US$ 5</span>'),
    ('<span data-m="total">$120.000</span>', '<span data-m="total">US$ 100</span>'),
]
doc = aplicar(doc, TEXTOS2, 'plantillas y legales')

# -------- los data-alt: barrido mecanico (no los ve el usuario, pero no dejan rastro)
ALT = [('pote de helado', 'vasito de helado'), ('Pote de helado', 'Vasito de helado'),
       ('Potes de helado', 'Vasitos de helado'), ('potes de helado', 'vasitos de helado'),
       ('helados en pote', 'helados en vasito'), ('Helado en pote', 'Helado en vasito'),
       ('100 helados en pote', '100 helados en vasito'),
       ('Freezer lleno', 'Congelador lleno'), ('de frutilla', 'de fresa'),
       ('sin TACC', 'sin gluten')]
def alts(m):
    v = m.group(1)
    for a, b in ALT:
        v = v.replace(a, b)
    return 'data-alt="' + v + '"'
doc = re.sub(r'data-alt="([^"]*)"', alts, doc)

# ------------------------------------------- configuracion nuestra
import json
MAPA = json.load(open('/tmp/mapa.json'))
CHECKOUT = 'https://helados-que-vendenn.impultienda.ar/checkout'

doc = doc.replace("checkoutUrl: '/checkout',", "checkoutUrl: '%s',\nbaseImagenes: 'PEGA_ACA_LA_CARPETA_DE_RECURSOS/',   // ej: https://cdn.impultienda.ar/store-resources/<tu-id>/" % CHECKOUT)
doc = doc.replace('href="/checkout"', 'href="%s"' % CHECKOUT)

# el mapa de imagenes pasa a ser nombre de archivo (el motor le pega baseImagenes adelante)
i = doc.index('imagenes: {'); j = doc.index('\n}', i)
nuevo = 'imagenes: {\n' + ',\n'.join("%s: '%s'" % (k, MAPA[k]) for k in sorted(MAPA, key=int)) + '\n'
doc = doc[:i] + nuevo + doc[j+1:]

# una sola linea nueva en su motor: si la imagen no es absoluta, le pone la base
doc = doc.replace("var url = CONFIG.imagenes[n];",
  "var url = CONFIG.imagenes[n];\nif (url && url.indexOf('http') !== 0 && url.indexOf('data:') !== 0) url = (CONFIG.baseImagenes || '') + url;")

# el sello de pago neutro
doc = doc.replace('src="IMG_SELLO_PAGO"', 'src="PEGA_ACA_LA_CARPETA_DE_RECURSOS/sello-pago.webp"')

# ------------------------------------------- barrido final de rastros argentinos
RASTROS = ['pote', 'Pote', 'frutilla', 'Frutilla', 'palito', 'Palito', 'monotributo', 'Monotributo',
           'bromatolog', 'Bromatolog', 'Mercado Pago', 'Argentina', 'plata', 'freezer', 'Freezer',
           'TACC', 'pan dulce', 'Vendé', 'vendé', 'Aprendé', 'aprendé', 'Mirá', 'mirá', 'Entrá',
           'Hacé', 'hacé', 'Probá', 'Seguí', 'Elegí', 'Poné', 'Cumplí', 'Pedí', 'tenés', 'podés',
           'necesitás', 'querés', 'sabés', 'vos', 'acá', 'Empezá', 'Calculá', 'Pagá', 'ponele']
print('\n--- rastros que quedan (revisar a mano) ---')
for r in RASTROS:
    n = len(re.findall(r'(?<![A-Za-zÁÉÍÓÚáéíóúñ])' + re.escape(r), doc))
    if n:
        print(f'  {r}: {n}')

open(OUT, 'w', encoding='utf-8').write(doc)
print('\n✅', OUT, len(doc), 'bytes')
