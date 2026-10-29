# Herrero de Finde (oferta AR)

> Clon para Argentina de **The Weekend Fabricator** (EE.UU./AU): más de 1.200 planos de herrería listos para fabricar, con lista de cortes, orden de soldadura y precio de venta sugerido, más 12 bonus. Landing larga de venta directa (sin quiz ni VSL) en ImpulTienda. (fuente: pedido de Santiago del 2026-10-22)

## Ideas clave
- **Competidor:** página "The Weekend Fabricator" en Meta, page id `964653193405481`, unos 367 anuncios activos (octubre de 2026). Corre desde fines de septiembre y también tiene ads en italiano ("Guardalo prima di sabato").
- **Embudo:** ad → landing larga → `/checkout` de ImpulTienda (`the-weekend-fabricator.impultienda.ar`). El checkout usa upsells inline (`/checkout?upsells=2`). Está montado en ImpulTienda con plantilla `custom_html`, igual que las landings de Santiago.
- **Precio original:** US$ 27, tachado US$ 99, "valor total $583". Garantía de 60 días.
- **Sus ads:** primary text "🔥 The Pack Every Welder Needs" (1.200 planos, medidas exactas, descarga inmediata, "less than a takeout order"), título "Start this weekend" o "🔥 1,200+ Ready-to-Build Metal Plans", y videos con "Pick one. Build it this weekend 👇". Hay una variante de trailers ("Build trailers with confidence…").
- **Ángulo de la landing:** "Hacé tus primeros $1.000 con la soldadora que ya tenés". No te falta mano, te faltan números. Escalera de ingresos (nunca vendiste / ya soldás por plata), calculadora de margen por trabajo y visor de planos interactivo con selector de unidades.

## Adaptación a Argentina (2026-10-22)
- **Marca:** "Herrero de Finde" (logo "Herrero de **Finde**"). A confirmar.
- **Precio:** $14.990, tachado $49.990, ahorro $35.000. Valores de bonus pasados a pesos (valor total $324.870, bonus $280.880).
- **Plata:** dólares ×1.000 (hero "tu primer $1.000.000", escalera $1.125.000 / $2.540.000, calculadora y tarjetas de planos). Son referencias del original convertidas: validarlas.
- **Medidas:** milímetros por defecto (el visor arranca en MM, con PULGADAS como opción), barras de 6 m, "casa de hierros", parrillas y fogoneros primero.
- **Pago:** "Tarjeta y Mercado Pago" en vez de Apple Pay.
- **Nombres:** reseñas y muro con nombres argentinos (Matías, Lucas, Tomás, Anahí…).

## Activos
- Carpeta `~/Desktop/herrero-de-finde/`: `landing/herrero-de-finde-landing.txt` (2,5 MB, imágenes embebidas) y `landing/herrero-de-finde-PRUEBA.html`, `imagenes/` (71 WebP) y `anuncios/` (guiones y los 6 videos) y copia en `OUTPUTS/2026-10-22-landing-herrero-de-finde.html`.
- **Versión Shopify (2026-10-22):** `landing/herrero-de-finde-shopify.liquid` (124 KB) como plantilla de página Liquid (`{% layout none %}` + `{{ content_for_header }}`). Toma las imágenes de Contenido → Archivos con `file_url` y todas llevan el prefijo `hdf-` para no pisarse con las de otras ofertas. Los botones van a `/cart/67602537513178:1` (variante del producto; el ID del producto es 15282933170394). **Publicada el 2026-10-22 en `txg7mz-en.myshopify.com/pages/herrero-de-finde`**, con las 151 imágenes cargando bien. Primero los botones iban a `/cart/67602537513178:1`, que salta el carrito y va directo al checkout. Santiago: "yo quiero que vaya directo al carrito". Ahora el botón suma la variante con `/cart/add.js` (si no estaba ya en el carrito) y abre `/cart` con los UTMs. Si falla el JS, usa `/cart/add?id=…&quantity=1`. Los pasos están en [[shopify-y-checkout]].
- Configuración arriba del HTML: `HDF_CONFIG.LINK_CHECKOUT` (por defecto `/checkout`). Todos los botones pasan los UTMs de la URL.
- Imágenes rehechas con Pillow: 24 tarjetas de planos (títulos, categorías y precios en ARS), 7 reseñas en español y las 12 tapas de bonus. Sello de garantía en SVG.

## Análisis de sus ads (2026-10-22)
- **Muestra:** 334 tarjetas activas (660 anuncios contando copias) y 180 videos únicos. 170 en inglés y 9 en italiano. Todo bajado y transcripto en `~/Desktop/herrero-de-finde/anuncios/work/` (`videos/`, `transcripts.json`, `rows.json`).
- **Señales de ganador que usé:** copias del mismo video (lo duplican en varios conjuntos), cuántas versiones nuevas sacan del mismo hook (lo siguen iterando) y que siga activo semanas después de lanzado. No elegí por fecha de arranque.
- **Estilos (contados uno por uno el 2026-10-28):** voz en off sobre B-roll + fichas **122 videos (67,8 %, 406 copias)**, **avatar de IA a cámara 32 (17,8 %, 120 copias)**, UGC con persona 12 (6,7 %), podcast de dos herreros 8 (4,4 %), dibujos animados (Buck) 6 (3,3 %). Hasta ahora nosotros usamos solo el primero. Detalle en la sección *El avatar del competidor* de más abajo.
- **Familias de hooks más iteradas:**
  1. **"Dos trailers por mes, paga la cuota de la camioneta"** (+25 versiones, avatar y B-roll). El video 003 en B-roll tiene 20 copias (el segundo más copiado).
  2. **"$X en materiales, $Y por el [trabajo], un finde"** (11 versiones: portón, parrilla, rack, fogonero…). Video 005 y 027 con 9 copias.
  3. **Listas "5 trabajos que se venden a más de $X"** (+20 versiones, las más nuevas). Video 031 con 9 copias.
  4. **"Sumá lo que tenés en el garage"** (5 versiones; 024 y 032 con 9 copias).
  5. **"Tres cosas que podés soldar y que la gente paga"** (007, 9 copias; 083 variante).
  6. **"Escuchá: por menos que un tanque de nafta te llevás todo esto"** (4 versiones en 3 días, del 18 al 20/10).
  - Otras: "$1.300 de hierro, el plano dice cobrá…" (002, 21 copias, pero es avatar) y "30 piezas de hierro" (animación de armado, 19–22/10).
- **Su edición (voz en off):** etiqueta naranja arriba con el título ("5 BUILDS THAT SELL FOR $1,500+", "ONE FARM GATE", "1 OF 5"), fichas de planos con chip oscuro ("$119 IN STEEL", "$888 → $1,730–$2,250"), grabación de pantalla del celular con las carpetas, B-roll de soldadura y chispas, subtítulos de 1 a 3 palabras en mayúscula condensada blanca con la palabra clave en naranja, y CTA "Tap Learn More". Voz de hombre, ritmo rápido, cortes cada 1,5–2 s.
- **Guiones en español (6, uno por familia):** `OUTPUTS/2026-10-22-guiones-herrero-de-finde.md` (también en `anuncios/guiones.md`). Traducidos casi literales, pesos ×1.000 y sin precio del producto.

## Cómo se armaron los videos (2026-10-22)
1. **Voz:** Google AI Studio, Gemini 3.8 Flash TTS, voz **Knox**. No hay voces en español en el plan gratis, así que el acento sale del Style: *"Argentine man around 40 from Buenos Aires, a hands-on welder (herrero) narrating a punchy DIY ad on TikTok in Rioplatense Spanish with a natural Argentine accent (sh sound for ll and y, voseo). Confident, direct, energetic and conversational, brisk pace, no announcer tone."*
   - **Lo que funciona:** escribir el guion con teclado real, tocar Run, **dejar que el audio termine de sonar** (si no, Run queda gris para el siguiente) y bajarlo con el botón Download. Llega a `~/Downloads/Generated Audio … .wav`.
   - **Lo que no funciona:** capturar el `<audio>` por JS (ahora suena por WebAudio y el `src` queda en 2 KB) y los loops JS viejos que siguen vivos: uno pisó `V1.wav` con un archivo vacío. Antes de editar, revisar la duración de cada voz.
   - Para elegir la voz, el panel se abre desde la tarjeta "Speaker settings" de la derecha. Escape cierra el menú de Style. Después hay que hacer clic en el cuadro de texto antes de tipear.
2. **B-roll:** 63 TikToks de búsquedas en TikTok (herrería, portones, parrillas, fogoneros, trailers), bajados con `yt-dlp -f best`. Quedaron 27 limpios en `anuncios/work/tiktoks/`. Los descartados tienen caras hablando, textos propios, marcas de agua (Steel Projects) o bandas negras.
   - Las hojas de contacto se numeran por orden de archivo. Para elegir, **verificar el ID por el sufijo**, no por el número de la hoja: la primera vez mapeé mal varios.
3. **Fichas de planos:** las 24 tarjetas en español de la landing más 5 nuevas (portón de campo, fogonero cuadrado, trailer 1,50 x 2,40 en dos versiones, chasis 1,80 x 1,20) y un celular con las 10 carpetas de la biblioteca. Están en `anuncios/work/stills/`.
4. **Edición:** `OUTPUTS/scripts-vsl/edit_herrero.py plan.json salida.mp4`, una copia de `edit_infinity.py` con la estética de ellos:
   - etiqueta naranja arriba con el título;
   - chip oscuro de plata (materiales en blanco → precio de venta en verde; la flecha va con Arial Unicode porque Barlow no la tiene);
   - fichas sobre fondo claro arriba (y = 360);
   - subtítulos Montserrat ExtraBold de 2 palabras (palabra activa en naranja, y = 1300);
   - placa final oscura "FABRICÁ TRABAJOS COMO ESTOS" + chip verde "+1.200 PLANOS · 12 BONUS" + "Tocá Más información";
   - cortes de 1,4 a 2,4 s y voz a 1,1x.
   - **v2 (2026-10-22, "está medio aburrida"):** su música (los 3 temas de sus ads, separados de la voz, en `anuncios/work/music/bed_A/B/C.wav`, a −8 dB), voz a 1,18x, golpe de zoom en cada corte y zoom constante, destello blanco + whoosh cada 3 cortes, placas que entran saltando, sello "VENDIDA" sobre las fichas, subtítulos con la palabra activa en amarillo y barra de progreso naranja arriba. Las fichas van más grandes (`fit_w` 1,2, `fit_y` 300).
   - Los planes salen de `anuncios/work/plans/gen.py`.
5. **Entregables:** `~/Desktop/herrero-de-finde/anuncios/HF-V1…V6-*.mp4` (1080x1920, de 33 a 72 s).

## Registro de correcciones
- **2026-10-22 · Videos: "está medio aburrida".** Regla para los videos de voz en off sobre B-roll: no alcanza con cortes rápidos. Llevan **música de fondo** (idealmente la del competidor), **movimiento constante** (zoom en todo el plano y golpe en cada corte), **destellos con whoosh**, placas animadas y **barra de progreso**.
- **2026-10-22 · "Me encantó la landing".** Único pedido: los primeros textos del hero (eyebrow, título, promesa y bajada) **centrados**. Se aplicó con una regla CSS sobre `.hero`.

## Resultados de la primera tanda (2026-10-23)
- 6 conjuntos ABO, un video por conjunto. **76,57 USD gastados, 7 compras, CPA 10,94 USD.** Tabla completa en `OUTPUTS/2026-10-23-registro-herrero-de-finde.md`.
- **Lo que compró:** los conjuntos que vendieron abren con **plata o un número en el primer segundo**. El mejor es la **comparación de costo** (V6, "por menos que un tanque de nafta", CPA 7,05), después las **listas de costo de material → precio de venta** (V5 11,39 · V4 13,56 · V3 10,71).
- **Lo que no:** el V1 (anécdota "un tipo me dijo…", trailers) es el único con cero ventas. En este nicho la historia antes de la plata no entra.
- El V2 ("sumá lo que tenés en el garage") se apagó con el segundo mejor CPA (8,70) y un solo presupuesto gastado. Su ángulo vuelve mejorado en el V11.
- **Regla que sale de acá:** todo guion de Herrero de Finde arranca con un número o una comparación de plata en el primer segundo, y el cuerpo siempre trae costo de material → precio de venta sugerido.
- **Tanda V7–V12 (2026-10-23):** `OUTPUTS/2026-10-23-guiones-herrero-de-finde-v7-v12.md`. Comparación de costo (alambre tubular), lista de 5 trabajos que te piden y nunca cotizás, una hoja de portón en un finde, escalera para el que nunca vendió (fogonero), inventario del garage y recorrido hoja por hoja de lo que hay adentro.
- **Regla nueva: los números salen de fichas reales.** En el borrador del V8 y del V9 había precios inventados (reja de ventana, asador con carro, portón corredizo). Se reemplazaron por planos que existen de verdad, con los precios de la landing: protector de cabina (TK-082, $283.000 → $590.000-$765.000), botellero (FN-139, $327.000 → $885.000-$1.150.000), hoja de portón 3,66 (FM-068, $883.000 → $1.480.000-$1.925.000), escalera de hierro (ST-064, $1.322.000 → $2.440.000-$3.170.000) y pérgola (ST-015, $1.429.000 → $2.605.000-$3.385.000). Antes de escribir un número en un guion, se busca la ficha; si no existe, se cambia el ítem.

## Material nuevo para los videos V7–V12 (2026-10-23)
- **Las 4 hojas de un plano en español**, generadas por código: `anuncios/work/stills/mk_hojas.py` → `hoja-1-dibujo.png` (tres vistas + medida total), `hoja-2-compras.png` (lista de compras y total $961.000 → precio de venta), `hoja-3-cortes.png` (tabla A-H con largo de corte) y `hoja-4-soldadura.png` (14 pasos). Mismo estilo que las fichas. **Reemplazan a las `hdf-pagina-*.webp` del original, que están en inglés y llevan la marca del competidor.**
- **Planes de edición:** `anuncios/work/plans/gen2.py` genera `V7.json` a `V12.json` con la estética v2 (música, zoom, destellos, barra de progreso) y comparte `usage.json` con la tanda anterior para no repetir recortes.
- **Textos de voz:** `anuncios/work/vo/V7.txt` a `V12.txt`.
- **Voces (2026-10-24):** las 6 grabadas en AI Studio con Knox y el mismo Style argentino de la tanda anterior (`V7.wav` a `V12.wav`, de 54 a 72 s en crudo). La extensión de Chrome había perdido la pestaña seis veces el 23/10; al día siguiente funcionó sin tocar nada.
- **Videos finales:** `anuncios/HF-V7…HF-V12-*.mp4`, de 46 a 61 s. **Para subir van 3** (V7, V8 y V11); V9, V10 y V12 quedan de banco ([[guiones-y-anuncios]], registro del 2026-10-24).

### Dos cosas que salieron de este render (reglas)
- **`fit_w` va en 1.0, no en 1.2.** Con 1,2 la ficha se escala más ancha que la pantalla y se recorta un 8% por lado: se perdía el título del plano y la columna de la derecha de las tablas (la de los precios y la de los largos de corte). Con 1.0 entra entera con margen.
- **Revisar los tramos tardíos del B-roll.** El clip `7566063571134680350.mp4` (Y) lleva el cartel en inglés *"And that's how you do that"* desde el segundo 97 hasta el final, y se coló en el V8. En `gen2.py` quedó el diccionario `LIMITE = {'Y': 96}` para cortar ese tramo. Antes de dar una tanda por buena, mirar frames de los videos terminados, no solo de los clips.
- **Ojo con la ocurrencia de las palabras ancla.** En el V8 anclé la pérgola en `'cinco,'` ocurrencia 0, que es la primera palabra del guion ("Cinco trabajos…"), y el render se cortó con `max() arg is an empty sequence`. Cuando el hook repite una palabra del cuerpo, contar las ocurrencias.

## El V7 es el ganador (2026-10-25)
- **6 ventas en el día con CPA de 1 USD.** La primera tanda entera había hecho 7 ventas a 10,94 de promedio y su mejor conjunto (V6, tanque de nafta) estaba en 7,05. El V7 baja el CPA un orden de magnitud.
- **Por qué gana:** compara contra un **consumible del oficio** (rollo de alambre tubular), no contra un gasto de la vida como la nafta. Es jerga que solo entiende un herrero, así que el hook filtra el público en la primera palabra. Después da el giro **consumible → activo** ("el alambre se te termina en dos trabajos, esto te queda para siempre"), que ancla el precio sin nombrarlo.
- Lo completan: dolor de oficio y no de bolsillo ("dibujar, probar y volver a cortar es lo que te come el finde y el material"), las diez carpetas nombradas una por una, **un solo** ejemplo con números y chico al final, y CTA con día ("así el sábado ya estás cortando").
- **DNA para variar:** gasto que ya hacés en el taller → esto cuesta menos y no se gasta → **una sola** de las cuatro hojas explicada en detalle → una ficha real con costo y precio de venta → CTA con fecha.
- **Regla:** el objeto de comparación tiene que ser **jerga de taller**. Cuanto más específico del oficio, más barato el clic. La comparación genérica (nafta, café) convierte peor.

## Tanda que se produce: V13–V15 + V19–V21 (2026-10-25)
- Santiago: **3 variables propias del V7 y 3 de ganadores del competidor que no hubiéramos hecho, sin avatar.**
- **Propias (DNA del V7):** caja de discos (lista de cortes, TK-024), carga del tubo de mezcla (orden de soldadura, BQ-090) y el hierro tirado en recortes (lista de compras, SH-148).
- **Del competidor:** V19 de su video 011, 9 copias ("el cliente te pregunta qué más sabés hacer", FN-107); V20 de sus 030 y 041, 6 copias ("ellos te dan un perchero de herraduras, acá un porta autos", TR-129); V21 de su 100, 5 copias ("tu amigo te pide un fogonero, ¿cuánto le cobrás?", BQ-028).
- **Cómo se eligieron:** ranking por copias del mismo video en `anuncios/work/rows.json`, descarte de las seis familias ya usadas (trailers, costo→precio, listas de 5, inventario del garage, tres cosas, comparación de costo) y **verificación visual por frames** para sacar los de avatar. Se descartaron así 051 (avatar PIP), 016 (dibujos animados, Buck) y 036 (podcast de dos).
- Guiones en `OUTPUTS/2026-10-25-guiones-herrero-de-finde-tanda-v13-v21.md`. Planes en `anuncios/work/plans/gen3.py`, voces en `vo/V13…V21.wav`, videos `anuncios/HF-V13…HF-V21.mp4`.
- Banco sin producir (V16, V17, V18): plano suelto (TR-072), cotizar a ojo (GY-096) y el sábado perdido (BQ-028), en `OUTPUTS/2026-10-25-guiones-herrero-de-finde-v13-v18.md`.

### Tres cosas que salieron de esta tanda (reglas)
- **Las anclas y los hooks van con tilde, copiados del texto real.** Escribí `'Toca'`, `'cobras?'`, `'Mas barato…'` y el render avisó `"cobras?" n.º 0 no aparece`, además de poner las etiquetas en pantalla con faltas de ortografía. Ahora `gen3.py` se valida contra el `.txt` de voz antes de renderizar: cada ancla se reemplaza por la forma exacta del guion y se corrige la ocurrencia si se pasa.
- **Verificar que el audio descargado sea el nuevo.** Al bajar el V19 justo después de tocar Run, AI Studio entregó **el wav del guion anterior** (mismo md5 que el V15). Regla: antes de guardar, mirar que el reproductor esté sonando el audio nuevo (cambia la duración) y comparar el md5 contra los ya guardados.
- **Voice Design es de pago.** Al entrar a una voz desde la portada de AI Studio se abre "Create voice · Voice Design", que pide vincular una clave de API paga. El camino gratis es **Create new dialog** → cambiar la voz del Speaker 1 a Knox desde Speaker settings.

## Tanda V13–V18 (borrador, 2026-10-25)
- `OUTPUTS/2026-10-25-guiones-herrero-de-finde-v13-v18.md`, también en `anuncios/guiones-v13-v18.md`. Seis variables de la DNA del V7: caja de discos (lista de cortes, TK-024), carga del tubo de mezcla (orden de soldadura, BQ-090), el hierro tirado en recortes (lista de compras, SH-148), lo que cobran por un plano suelto (dibujo en tres vistas, TR-072), lo que perdés cotizando a ojo (precio sugerido, GY-096) y el sábado perdido dibujando (las cuatro hojas, BQ-028).
- De 175 a 196 palabras: a 1,20x quedan en 58–65 s, el largo del V7.
- Santiago pidió 6 aunque su regla de variables es 3. Se le marcó que son 6 apuestas sobre un dato de un solo día y que lo prudente sería subir 3 y esperar la confirmación del V7.
- Faltan las voces y el render.

## Tanda V28–V33 (2026-10-26)

- **Guiones:** `OUTPUTS/2026-10-26-guiones-herrero-v28-v33.md`. Tres variables de la DNA del V7 (electrodos → el precio sugerido · media chapa → las tres vistas · el flete → la lista de compras) y tres de bizop (arrancar sin poner un peso · la cuenta de cuatro sábados · a quién le vendo).
- **Antes, 6 renovaciones** (Guiones 22 a 27) sobre los cuerpos del CJTO 5 y del CJTO 6: `OUTPUTS/2026-10-26-renovaciones-herrero-v22-v27.md`.
- **Material nuevo para los videos, con los números del producto:** `anuncios/work/stills/mk_fichas.py` genera una ficha por plano (isométrico + hierro + precio + horas) importando el generador del producto, así el número que se dice coincide con el que se ve. Se sumaron además tres páginas reales exportadas del PDF: `hoja-trabajo.png` (hoja 1 de BQ-090, con el precio), `hoja-vistas.png` (hoja 2 de FN-107) y `catalogo-clientes.png` (del Bonus 12).
- **Planes:** `anuncios/work/plans/gen4.py`, con **validación propia de anclas**: compara cada ancla y cada overlay contra el `.txt` de voz, corrige la forma exacta (tildes incluidas) y corta la generación si una palabra no existe. Atajó el error de `comprar.` por `compre.` antes de renderizar.
- **Voces:** Knox + el Style argentino de siempre, las seis grabadas. Los videos quedaron de 46 a 57 segundos.
- **Cuando la extensión de Chrome se cuelga, no hay que abrir pestañas nuevas:** pierde el grupo una y otra vez. Lo que lo arregló fue `list_connected_browsers` + `select_browser` con el deviceId: reconecta y **devuelve la pestaña original intacta**, con la voz y el Style ya configurados. Media hora de pestañas nuevas se resolvió con esas dos llamadas.
### Tres cosas que salieron de este render (reglas)
- **Dos clips más del B-roll quedaron vetados.** `B` (7253123425676365083) lleva el cartel en inglés *"Watch us build our custom fire pit"* **de 0 a 9 s**: en `gen4.py` está `DESDE = {'B': 10.5}`. `c` (7691053148219198752) cierra con la **placa de marca de otra herrería** ("Edouane SB Welding") desde el segundo 256: `LIMITE = {'Y': 96, 'c': 254}`. Los dos se colaron en el primer render y se vieron recién al mirar los frames del video terminado.
- **Las etiquetas del hook van con tilde.** Salieron "MAS CARO", "MAS QUE MEDIA CHAPA" y "MAS BARATO" en pantalla. El hook es texto que se dibuja, no se transcribe: hay que escribirlo bien a mano.
- **No renderizar dos videos al mismo tiempo.** Dos procesos a la vez sobre la carpeta del Escritorio dieron `Operation timed out` al concatenar los segmentos (ffmpeg error 196) y perdieron dos renders. De a uno.

- **Ojo con la cuenta de Google:** cuando la extensión abre una ventana nueva, AI Studio puede cargar con otra cuenta del navegador (apareció `damianmartinaguilar@…` en vez de `searasantiago58@…`). Verificar la cuenta del pie izquierdo antes de generar.

## Las renovaciones V22–V27 no funcionaron (2026-10-27)

Santiago: *"no funcionaron las que hicimos, hay que hacer mejores, creo que deberíamos variar la edición, guiones más llamativos, alineados a la landing"*.

**Por qué no movieron la aguja (diagnóstico):**
1. **Cuatro de las seis eran el mismo hook.** V22 a V25 son la misma familia del V7 (un consumible del taller contra esto: electrodos, flete, media chapa, careta). Cambiar el objeto no es cambiar el hook: el público que ya vio el V7 ve lo mismo. La propia [[renovacion-de-creativos]] pide cambiar el **formato** del hook, no solo su contenido.
2. **La edición era idéntica a la del ganador.** Misma etiqueta naranja, mismo chip oscuro, mismos subtítulos amarillos, mismo ritmo. Para Meta es la misma huella creativa y cae en el mismo segmento saturado ([[guiones-y-anuncios]]: iterar solo el hook sube el CPM).
3. **No había message match con la landing.** El cuerpo vendía una herramienta barata de taller y la landing abre con "Hacé tu primer $1.000.000". Es la causa del `landing → checkout` de 9,21 % del 26/10.

**Qué se hace distinto en la tanda V34–V39:** un formato de hook distinto por video, el cuerpo apuntado a la promesa de la landing y una edición nueva (abajo).

## Tanda V34–V39: renovaciones alineadas a la landing (2026-10-27)

- **Guiones:** `OUTPUTS/2026-10-27-renovaciones-herrero-v34-v39.md`. Seis formatos de hook distintos: la frase de la landing (*"No te falta mano. Te faltan números"*), demo de pantalla (*"un plano abierto en el celular"*), la pregunta del cliente (*"el que tira el número se lleva el trabajo"*), lista de los cuatro números, ROI (*"el primer trabajo lo paga diez veces"*) y la escalera del principiante (*"la soldadora ya está paga"*).
- **Alineación con la landing:** cada guion usa las frases del hero y del cuerpo de la página — "con la soldadora que ya tenés", "te faltan números: qué cortar, cuánto hierro comprar, en qué orden soldarlo y cuánto cobrar", "un solo trabajo lo paga diez veces", "60 días de garantía". El que hace clic encuentra la misma promesa escrita igual.
- **Los números salen del producto**, no del banco viejo convertido de dólares: FM-068 portón de campo (124 mil → 475–620 mil), BQ-090 parrilla argentina (406 mil → 1,030–1,340 M), FN-022 mesa de comedor (235 mil → 645–840 mil), SH-148 mesa para motos (241 mil → 750–975 mil), TK-024 rack (122 mil → 520–675 mil) y BQ-007 fogonero de 70 cm (143 mil → 305–395 mil).
- **Voces:** Knox + el Style argentino de siempre, las seis en AI Studio (50 a 62 s en crudo), con las páginas muteadas.

### La edición v3 (estética de la landing)
Editor nuevo: `OUTPUTS/scripts-vsl/edit_herrero_v3.py` (copia de `edit_herrero.py`), planes en `anuncios/work/plans/gen5.py`.
- **Paleta de la landing** en lugar de la del competidor: rust `#E2561B`, ámbar `#F2A33C`, ink `#F7F3EE`, fondo `#0F0D0B` y verde `#5FC97E`.
- **Placa de apertura tipo hero**: eyebrow "HERRERO DE FINDE" en rust y el hook en ink sobre panel oscuro, igual que el encabezado de la página (antes: caja naranja llena).
- **Etiquetas tipo plano**: panel blueprint con grilla fina y filete rust al costado.
- **Cotización** en panel oscuro con filete rust: hierro en ink → precio de venta en verde.
- **Regla de medidas arriba** (ticks de milímetros) en lugar de la barra de progreso lisa; la barra rust avanza por debajo.
- **Subtítulos de 3 palabras** con la palabra activa en ámbar (antes 2 palabras en amarillo).
- **Cierre con la marca**: "HERRERO DE **FINDE**", chip verde "+1.200 PLANOS · 12 BONUS", botón rust "Tocá Más información" y "60 DÍAS DE GARANTÍA · UN SOLO PAGO".
- **Clips nuevos de pantalla**: `anuncios/work/stills/mk_demo.py` arma `demo-hojas.mp4` y `demo-scroll.mp4`, el plano real abierto en un celular pasando las cuatro hojas y scrolleando. Entran solo donde están ancladas, nunca se espejan (tienen texto).
- **Ritmo distinto**: voz a 1,30, cortes de 2,2 a 3,2 s (antes 1,9–2,4) y destello cada 4 cortes (antes cada 3).

### Un clip más vetado (2026-10-27)
- `J` (7468781029281533230) lleva el cartel en inglés *"Trailer Build Part 4: Mobility"* **de 0 a 5 s**. Se coló en el primer render del V36. En `gen5.py` quedó `DESDE = {'B': 10.5, 'J': 5.5}`. Vetos acumulados: `LIMITE = {'Y': 96, 'c': 254}` y `DESDE = {'B': 10.5, 'J': 5.5}`.
- Se encontró con la hoja de contactos del video terminado a 1 cuadro cada 2 s, que es la regla que salió de 100 Paper Squishies: mirar el render, no solo los clips.

### El pool repetía la misma fuente (2026-10-27)
- Después de vetar el tramo sucio, el V36 abrió con **tres planos seguidos del mismo clip** (el trailer): al mover el veto, los recortes nuevos de ese clip quedaban con `usage` en cero y el puntaje los elegía igual. En `edit_herrero_v3.py` la penalización por repetir fuente dentro del mismo video pasó de `×3` a **`×30`** (y de 6 a 12 la de repetir el clip anterior). Con eso cada fuente entra una sola vez por video.
- Regla práctica: cuando se veta un tramo y se regenera el pool, hay que **volver a mirar la hoja de contactos**: cambia la repartición de todos los planos, no solo la del clip vetado.

## Tanda con avatar A1–A3 (2026-10-28)

Primera tanda con cara. Sale del conteo de la sección *El avatar del competidor*: es el cambio de formato más grande disponible y el único que el competidor valida con plata. Los otros tres de la tanda (35, 37 y 38) quedan en voz en off.

- **Guiones:** `OUTPUTS/2026-10-28-guiones-herrero-avatar-A1-A3.md`. Son los **34, 36 y 39 reescritos en primera persona**, que es el registro que el avatar habilita: A1 "a mí no me faltaba mano, me faltaban números" (portón FM-068), A2 "le dije que le avisaba, nunca le avisé" (mesa FN-022) y A3 "mi soldadora estuvo dos años juntando polvo" (fogonero BQ-007). Cada uno abre con la confesión y recién después muestra el producto.
- **El avatar:** un solo personaje de HeyGen, **"HERRERO"**, con **dos looks** (parado en la puerta del taller y sentado en el banco), creados desde dos fotos que hizo Santiago. El prompt de las fotos está en `OUTPUTS/2026-10-28-prompt-avatar-herrero-de-finde.md` y la regla de cómo se pide en [[ugc-y-video-generativo]].
- **La voz no gasta créditos:** Avatar IV acepta **subir el audio** (pestaña *Audio* en vez de *Guion*), así que la voz sale de AI Studio como siempre. Voz elegida por Santiago: **Enzo** (antes probamos Knox y Daro), con el Style rioplatense reforzado.
- **Los dos looks se alternan sin pagar render extra:** el guion se corta en dos bloques (confesión parado / explicación sentado), se sube un audio por bloque y se concatenan. Total de segundos igual, mismo costo.
- **Costo real: 41 créditos los seis bloques** (de 600 en la cuenta de Juan). Un bloque de 13 s salió 4 créditos: ~18 por minuto, la mitad de lo que calculamos con el dato de Calistenia.
- **Editor nuevo:** `OUTPUTS/scripts-vsl/edit_herrero_avatar.py` (copia de `edit_herrero_v3.py` con la base cambiada). El avatar es el plano por defecto y se corta a fichas, hojas del plano, el plano en el celular y B-roll **solo en las palabras marcadas** (`cutaways`: palabra, ocurrencia, clip, segundo, duración). La voz sale del propio video: no se recortan silencios ni se cambia la velocidad, porque rompería el lipsync. Planes en `OUTPUTS/scripts-vsl/gen_herrero_avatar_plans.py`.
- **Entregables:** `~/Desktop/herrero-de-finde/anuncios/HF-A1-no-me-faltaba-mano.mp4` (51 s), `HF-A2-nunca-le-avise.mp4` (50 s) y `HF-A3-la-soldadora-juntaba-polvo.mp4` (46 s).

### Cuatro cosas que salieron de esta tanda (reglas)
- **El audio se acelera antes de subirlo a HeyGen, no después.** Se le aplica el mismo `silenceremove` + `atempo` de los ads de voz en off (acá 1,15) y HeyGen sincroniza los labios con ese audio. Después del render no se puede tocar la velocidad sin romper el lipsync.
- **Mutear AI Studio con `AudioContext.suspend()` cuelga el Run.** El botón queda gris hasta que el audio "termina de sonar", y un contexto suspendido no avanza nunca. La forma correcta de mutear es **rutear lo que se conecta a `destination` por un gain en 0**: suena en silencio pero el reproductor avanza. Para no esperar los 50 s, se hace clic al final de la barra del reproductor.
- **Al generar varias voces seguidas, verificar cuál se bajó.** De tres descargas seguidas una no se guardó y las otras dos quedaron con nombres por minuto. Se identifican transcribiendo los primeros 8 segundos, no por el orden.
- **En los cortes, el que manda es el nuevo.** Si un corte pisa al anterior, se acorta el anterior; y si al anterior le quedarían menos de 0,6 s, se cae el anterior. Antes se ignoraba el nuevo y se perdía la placa final en dos de los tres videos.

## Tanda de voz en off V40–V42 (2026-10-28)

Las otras tres de la tanda del día, en el formato de siempre (voz en off + B-roll + fichas, edición v3). No son renovaciones de hooks viejos: **hooks nuevos y fichas nuevas**, porque las seis de la V34–V39 ya habían rotado las mismas seis fichas dos veces.

- **Guiones:** `OUTPUTS/2026-10-28-renovaciones-herrero-v40-v42.md`. V40 *"Nunca más dibujar en un cartón"* (portón de dos hojas FM-004), V41 *"El cliente señala una foto y vos ya tenés el plano"* (jaula de potencia GY-013, con el Catálogo para Clientes adentro) y V42 *"Lo que cobra un dibujante por un solo plano"* (invernadero ST-012, ancla de precio contra lo que cuesta un plano a pedido).
- **Fichas nuevas, sacadas del motor del producto** con `anuncios/work/stills/mk_fichas.py` (que lee `OUTPUTS/scripts-producto/expansion.py`): FM-004 portón de dos hojas de 2,60 m (188 mil → 785 mil–1,020 M, 12–16 h), GY-013 jaula de potencia 1,10 × 1,10 (155 mil → 655–850 mil, 10–14 h) y ST-012 invernadero de 4 × 3 m (372 mil → 1,375–1,790 M, 20–28 h). Verificadas por transcripción contra lo que dice la voz.
- **Voz: Enzo**, la que eligió Santiago en la tanda con avatar, con el Style de siempre y la voz a 1,30. Antes se usaba Knox en los de voz en off.
- **Planes:** `anuncios/work/plans/gen6.py` (copia de `gen5.py` con `MUS = {40: 'A', 41: 'B', 42: 'C'}`).
- **Entregables:** `HF-V40-nunca-mas-el-carton.mp4` (48 s), `HF-V41-el-cliente-senala-la-foto.mp4` (43 s) y `HF-V42-lo-que-cobra-un-dibujante.mp4` (44 s).

### Dos cosas que salieron de esta tanda (reglas)
- **La línea de abajo de la placa final venía cortada en todos los videos.** `QUÉ CORTAR · CUÁNTO HIERRO · CUÁNTO COBRAR` a 40 px mide más de 1080 px: salía sin la "Q" ni la "R" desde la V34. Ahora `edit_herrero_v3.py` y `edit_herrero_avatar.py` **achican la tipografía hasta que entre** (de 40 a 22 px, margen de 90 px). Los videos anteriores a hoy siguen con la placa cortada; si se vuelven a subir, conviene re-renderizarlos.
- **Las fichas no se repiten más de dos tandas.** El motor del producto genera cualquiera de los 1.205 planos con sus números reales, así que no hay motivo para volver a mostrar el mismo portón. Antes de escribir una tanda, sacar fichas nuevas con `mk_fichas.py`.

## Tanda de voz en off V43–V48 (2026-10-29)

Seis renovaciones pedidas por Santiago: *"todo voz en off, pero hagamos un poco más simple la edición, tampoco tanto, para variar, hagamos buenas variables, que apunten al objetivo de mi landing"*.

- **Guiones:** `OUTPUTS/2026-10-29-renovaciones-herrero-v43-v48.md`. Seis formatos de hook nuevos, ninguno repetido de la V34–V42: V43 cronología (*"Viernes lo bajás. Martes te lo pagan"*), V44 la cuenta del primer millón (*"tu primer millón es un portón corredizo"*), V45 objeción + bonus (*"si todavía soldás flojo, adentro viene el curso"*), V46 enemigo (*"los planos gratis se cortan en el paso difícil"*), V47 proyección (*"el martes a la noche, cobrada"*) y V48 garantía invertida (*"o fabricás y cobrás, o te devuelven la plata"*).
- **El objetivo de la landing adentro de cada guion:** "tu primer millón con la soldadora que ya tenés", "lo armás el sábado, lo vendés antes de fin de mes", "no te falta mano, te faltan números", el curso de soldadura en video incluido, "por qué no 5.000 planos" (V46) y los 60 días con los archivos de regalo (V48). Todas frases que el que hace clic vuelve a leer en la página.
- **Fichas nuevas** (ninguna repetida de las dos tandas anteriores, con `mk_fichas.py`): BQ-009 parrilla argentina con carro (229 mil → 690–895 mil), FM-001 portón corredizo de 2,50 m (338 mil → 860 mil–1,120 M), SH-001 mesa de soldar (124 mil → 330–430 mil), ST-005 escalera recta de 8 escalones (342 mil → 1,150–1,495 M), FN-014 isla de cocina (219 mil → 725–940 mil) y ST-004 cochera a un agua 3 x 5 m (659 mil → 1,600–2,080 M).
- **Voces: Enzo**, con el Style rioplatense de siempre y la voz a 1,30. En **Gemini 3.8 Flash TTS**, porque Enzo no existe en el 3.1 Flash TTS Preview; las seis salieron de una sola carga de página y verificadas por transcripción.
- **Planes:** `anuncios/work/plans/gen7.py` (primer armado, con fotos), **`gen8.py`** (sin fotos) y **`gen9.py`** (el que quedó: sin fotos y con el pool limpio), con una sola cama musical (`bed_A`) para los seis.
- **Entregables:** `HF-V43-viernes-bajas-martes-cobras.mp4` (43 s), `HF-V44-tu-primer-millon.mp4` (44 s), `HF-V45-el-curso-viene-adentro.mp4` (43 s), `HF-V46-los-planos-gratis.mp4` (45 s), `HF-V47-el-martes-cobrada.mp4` (41 s) y `HF-V48-o-fabricas-o-te-devuelven.mp4` (41 s).

### La edición v4 (más simple)
Editor nuevo: `OUTPUTS/scripts-vsl/edit_herrero_v4.py` (copia de la v3 con tres cosas parametrizadas).
- **Apertura sin panel:** el hook va en ink sobre el propio video, con sombra y un filete rust abajo, en lugar de la placa hero con eyebrow.
- **Sin regla de medidas arriba** (`progress: False`), **sin destellos ni whooshes** (`flash: 0`, `whoosh: []`).
- **Subtítulos de 3 palabras sin palabra resaltada ni saltito** (`hi` en ink, `pop: False`).
- **Cortes más largos**: 3,0 a 4,0 s (antes 2,2–3,2) y **golpe de zoom suave** en cada corte (`punch: 0.07`, antes 0,16).
- **Dos placas por video** (etiqueta del trabajo + cotización) más el cierre de marca, en vez de las cuatro o cinco de la v3.
- Lo que no cambia: paleta de la landing, fichas del motor del producto, hojas reales del PDF, el celular con las diez carpetas y la placa final con el CTA.

### Un clip más vetado (2026-10-29)
- `Y` (7566063571134680350) lleva el cartel en inglés *"Step by step instructions on how to build a Firepit"* **de 0 a 8 s**. Apareció en el primer render del V43 porque el pool nuevo (recortes de 3,4 s) empezaba el clip en 4,9 s. En `gen7.py` quedó `DESDE = {'B': 10.5, 'J': 5.5, 'Y': 8.5}`. Vetos acumulados: `LIMITE = {'Y': 96, 'c': 254}` y ese `DESDE`.
- Confirma la regla: **cuando cambia el largo de los recortes del pool, hay que volver a mirar la hoja de contactos del render**, porque los tramos sucios que antes no entraban pasan a entrar.

### Nada de fotos: el visual es 100% TikTok (2026-10-29)
Santiago, después de ver la tanda: *"seguís poniendo fotos, tienen que ser todos de tiktok"*.
- **Regla:** en un ad de voz en off **no entra ni un plano de foto fija**. Nada de fichas, hojas del PDF, mockups, catálogos ni grabaciones de pantalla del celular: el 100 % del visual son **clips de TikTok del nicho**. El producto se cuenta con la **voz** y con las **placas de texto** encima del video (etiqueta del trabajo, chip de cotización y cierre de marca).
- En la práctica, `gen8.py` es `gen7.py` sin la sección de `stills/`, sin los demos de pantalla (`D1`/`D2`) y **con `anchors: []`**: el pool queda en 376 recortes de 3,4 s de los 25 TikToks limpios y el editor reparte solo, con la penalización ×30 que evita repetir fuente dentro del mismo video.
- Con los cortes de 3,0–4,0 s, cada video pasó de ~6 fotos + ~7 clips a **12–14 clips de TikTok**. Alcanza de sobra: 25 fuentes contra 14 planos.
- **Antes de re-renderizar** se restaura `usage.json` desde el backup previo a la tanda, para que la repartición arranque limpia y no se amontonen los recortes que ya habían subido de uso.
- Lo que la foto hacía (mostrar la hoja mientras la voz la describe) queda a cargo del guion: las placas de precio ahora son el único soporte visual del número, así que **la etiqueta y el chip de cotización no son opcionales**.

### Revisión completa del pool de TikTok (2026-10-29)
Al sacar las fotos, el B-roll pasó a cubrir el 100 % del video y aparecieron tramos sucios que antes quedaban tapados. Se revisó **clip por clip** con hoja de contactos (un frame cada 1,7 s, con el tiempo estampado) más una pasada automática de `cropdetect` a 1 fps para las bandas negras. Resultado, en `gen9.py`:
- **Fuera del pool entero:** `V` (7565696076930452750) — el clip completo tiene bandas negras arriba y abajo (es 720x1218).
- **`LIMITE`** (hasta dónde se puede usar): `Y` 96 s · `c` 254 s · **`T` 36 s** (desde los 37 s: bandas negras y la cara del creador a cámara) · **`M` 73 s** (cierra con el logo de CapCut) · **`X` 45 s** (cierra con "GRACIAS POR VER" sobre negro).
- **`DESDE`** (desde dónde): `B` 10,5 · `J` 5,5 · `Y` 8,5 · **`X` 4,5** (arranca con el cartel "MESA PA SOLDAR" y la barra del reproductor).
- **`HUECOS`** (tramos salteados en el medio): `U` 6,5–11,5 y 28,5–33 (bandas) · **`Z` 76–82** (cartel "¿Qué dice la tuertita papá?") · `e` 12–14,5, 34,5–37,5 y 47,5–50,5 · `b` 155–160 · `d` 16–19.
- Quedan **336 recortes** de 3,4 s sobre 24 clips, para 12–14 planos por video.
- **Regla:** el `cropdetect` encuentra las bandas negras solo; los carteles quemados y las caras hay que mirarlos. Las dos cosas se revisan **antes** de renderizar, no después, y la hoja de contactos de cada clip se guarda con el tiempo estampado para poder vetar tramos exactos.

## El embudo del 2026-10-26 (diagnóstico)

Datos del día: **landing 695 → checkout 64 (9,21%) → compra 33 (51,56%)**, conversión total 4,75%, order bumps 0%. Análisis completo en `OUTPUTS/2026-10-26-embudo-herrero-diagnostico.md`.

- **El embudo no está roto, está mal repartido.** La conversión total (4,75%) duplica el objetivo de 2,5–3% y el cierre del checkout (51,56%) duplica el KPI de 25–30%. El que flojea es **landing → checkout: 9,21%**, zona de perdedor según [[lectura-de-resultados]] (ganadores ~15, neutros ~12,5).
- **Un cierre del 51% es síntoma, no suerte:** a la pasarela solo llega el que ya decidió del todo. La landing sobre-filtra.
- **Cuánto vale:** cada punto de landing → checkout son 3,6 ventas por día. Pasar de 9,21 a 12% da +30% de ventas con el mismo gasto; a 15%, +64%.
- **Lo medido en la landing publicada:** 21.706 px de alto (29 pantallas de celular), 8 botones, el primero al 8% y el segundo al **32%** — siete pantallas sin salida a comprar justo donde está lo que más persuade. **No hay barra sticky ni contador.** LCP de 7,4 s con el H1 esperando la fuente de Google (medido con sesión de admin encima: falta medirlo limpio).
- **Message match:** el V7 ganador vende una herramienta de taller barata ("un rollo de alambre tubular te sale más caro que esto") y el hero abre con "Hacé tu primer $1.000.000" más dos tablas de proyección de ingresos. Son dos niveles de conciencia distintos.
- **Paso 0 antes de tocar la landing:** mirar el landing → checkout **por anuncio**. Hoy subió tanda nueva (V22–V33) y la causa 6 de [[diagnostico-de-checkout]] es que el ratio se cae por los creativos, no por el funnel.
- **Lo que no se toca:** el checkout, el precio y la oferta.

### Los CTA del tramo muerto (2026-10-26)
Primer ajuste del diagnóstico de arriba. La landing queda igual; solo se suman salidas a comprar.
- **Dos botones nuevos** en el tramo que iba del 8% al 32% sin ninguno: uno debajo de la foto del portón vendido (cierre de *"Esto es para vos si…"*) y otro debajo de *"¿Por qué no 5.000 planos?"*, al cerrar el visor de planos. Quedan al **17% y al 22%**. Mismo markup y mismas clases que los que ya estaban (`a.btn.rv` con `href="/checkout"`), así heredan el JS del carrito sin tocarlo.
- **Barra de compra fija** (`.stickycta`, antes del cierre del `body`, fuera del `footer`): precio a la izquierda y botón a la derecha. Aparece recién cuando el primer CTA quedó arriba y **se esconde sola cuando hay cualquier botón en pantalla**, así no tapa nada ni se superpone con los CTA existentes. Verificada en 10 posiciones de la página.
- Aplicado a los tres archivos: `herrero-de-finde-shopify.liquid`, `herrero-de-finde-landing.txt` y `herrero-de-finde-PRUEBA.html`. Copias previas en `landing/.backup-26oct/`.
- **Ojo:** la versión publicada en Shopify tiene los botones con `href="/cart/{variante}:1"` (va directo al checkout) y **no** trae el JS que los manda a `/cart`. El archivo local sí. Si se sube el archivo local tal cual, el botón pasa a abrir el carrito y cambia el embudo justo mientras se mide.

## Los 3 OTO post-pago (2026-10-26)

Escalera propuesta sobre el front de $14.990. Detalle en `OUTPUTS/2026-10-26-upsells-herrero-de-finde.md`.

| | Producto | Precio | Downsell |
|---|---|---|---|
| OTO 1 | **El Sistema de Planos a Medida™ 📐💰** — adaptar cualquier plano a la medida que pide el cliente | $24.990 | $12.990 |
| OTO 2 | **Asistente Personalizado 1 a 1 🤖✨** — el chat (decidido por Santiago) | $29.990 | $14.990 |
| OTO 3 | **El Sistema del Hierro al Costo™ 🔩💰** — comprar el material como distribuidor | $12.990 | $6.990 |

- **Sectores vírgenes que se eligieron:** la medida que no existe en la biblioteca y el precio del hierro. Los 12 bonus cubren qué fabricar, cómo cortarlo, cómo soldarlo, cómo terminarlo, cuánto cobrar, qué conviene y cómo venderlo; **nadie toca a cuánto comprar el material ni cómo adaptar un plano a otra medida**.
- **El OTO 1 lo habilita el generador:** `expansion.py` ya re-escala cualquiera de las 60 familias paramétricas, así que el entregable tiene costo marginal casi cero.
- **El ticket más alto va segundo**, como pide [[embudo-vsl-post-pago]]. AOV proyectado $28.335 con take rates de 25/15/20 → ratio 1,89 sobre el front (KPI 1,5).
- **Banco si se cambia alguno:** Colgalo Derecho (transporte e instalación), Que Te Paguen (seña, inflación, el que no paga) y Herrería Fina (inoxidable, aluminio, forja).
- **Los títulos siguen la fórmula de la pantalla de [[scented-stones]]:** nombre de producto + ™ + dos emojis ([[aumento-de-aov]], "Cómo se titula un OTO"). Títulos, precios y descripciones listos en `OUTPUTS/2026-10-26-otos-herrero-titulo-precio-descripcion.md`.
- ⚠️ **No corre en Shopify con Mercado Pago:** Checkout Pro no devuelve a una página propia. Para el post-pago hace falta ImpulTienda ([[shopify-y-checkout]]).

## Banco de fichas verificadas (2026-10-25)
Precios leídos de las imágenes de `anuncios/work/stills/plan-*.webp`. **Antes de poner un número en un guion, sale de acá.**

| Plan | Trabajo | Material | Precio de venta | Horas |
|---|---|---|---|---|
| BQ-028 | Fogonero hexagonal 122 cm | $470.000 | $805.000–$1.045.000 | 6–9 |
| BQ-053 | Parrilla Santa María 152 cm | $961.000 | $1.590.000–$2.070.000 | 14–18 |
| BQ-069 | Ahumador offset 76 x 152 | $1.995.000 | $3.145.000–$4.090.000 | 20–30 |
| BQ-090 | Parrilla argentina 183 x 76 | $921.000 | $1.550.000–$2.015.000 | 12–16 |
| BQ-130 | Ahumador vertical 76 x 168 (chapa 3 mm) | $1.115.000 | $1.990.000–$2.585.000 | 16–22 |
| BQ-133 | Ahumador offset de competición 91 x 213 | $3.220.000 | $4.830.000–$6.280.000 | 30–40 |
| FN-022 | Mesa de comedor con patas en X 2,44 x 1,02 | $654.000 | $1.430.000–$1.860.000 | 12–15 |
| FN-107 | Estructura de isla de cocina 213 x 91 | $708.000 | $1.430.000–$1.860.000 | 10–13 |
| GY-020 | Jaula de potencia 132 x 152 x 244 | $682.000 | $1.235.000–$1.610.000 | 10–14 |
| GY-096 | Rig de entrenamiento 2,44 x 2,74 | $1.271.000 | $2.235.000–$2.910.000 | 16–24 |
| SH-128 | Mesa de fabricación 3 x 1,2 estructura pesada | $1.900.000 | $2.985.000–$3.880.000 | 10–14 |
| SH-148 | Mesa de trabajo para motos 213 cm | $846.000 | $1.440.000–$1.870.000 | 10–14 |
| TK-024 | Rack overland para caja de 2,44 | $456.000 | $855.000–$1.115.000 | 8–12 |
| TK-060 | Bandeja plana para camioneta 274 x 203 | $1.794.000 | $2.975.000–$3.870.000 | 20–28 |
| TR-072 | Trailer con rampa 2,08 x 4,88 | $3.765.000 | $5.570.000–$7.245.000 | 28–34 |
| TR-117 | Trailer para lancha de 6,7 m | $3.543.000 | $5.015.000–$6.520.000 | 27–33 |
| TR-129 | Porta autos 2,44 x 6,10 doble eje | $7.946.000 | $11.275.000–$14.660.000 | 45–60 |
| TR-148 | Base para tiny house 2,44 x 7,32 | $11.165.000 | $15.560.000–$20.225.000 | 50–70 |

**Fichas nuevas del 2026-10-28** (sacadas del motor, van en la V40–V42): FM-004 portón de dos hojas de 2,60 m ($188.000 → $785.000–$1.020.000, 12–16 h), GY-013 jaula de potencia 1,10 × 1,10 ($155.000 → $655.000–$850.000, 10–14 h) y ST-012 invernadero de 4 × 3 m ($372.000 → $1.375.000–$1.790.000, 20–28 h).

Las usadas en guiones anteriores: TK-082 protector de cabina ($283.000 → $590.000–$765.000), FN-139 botellero ($327.000 → $885.000–$1.150.000), FM-068 hoja de portón 3,66 ($883.000 → $1.480.000–$1.925.000), ST-064 escalera ($1.322.000 → $2.440.000–$3.170.000), ST-015 pérgola ($1.429.000 → $2.605.000–$3.385.000) y el fogonero cuadrado ($170.000 → $415.000–$535.000).

## El producto: la Biblioteca de Planos y los 12 bonus (2026-10-26)

> Resuelve la pregunta abierta de "¿de dónde sale la biblioteca de planos en español?". **El producto está hecho, generado por código, y es propio: no hay nada del competidor adentro.** Después de dos devoluciones de clientes se ajustó para que entregue exactamente lo que promete la publicación: **1.205 planos en 8 categorías y los 12 bonus**.

- **Carpeta:** `~/Desktop/herrero-de-finde/productos/` — 21 archivos.
- **Generador:** `OUTPUTS/scripts-producto/`. Se rehace entero con `python3 armar_todo.py <carpeta>` en menos de 3 minutos.

### Qué se entrega (13 archivos)
| Archivo | Qué es |
|---|---|
| `Herrero de Finde - Biblioteca de Planos (1205 planos).pdf` | **Un solo PDF con todo: 4.866 páginas, 144 MB.** Portada, qué hay en la descarga, cómo se lee un plano, tabla de la casa de hierros, cómo cobrar, control antes de cortar, **índice de los 1.205 planos con su página**, un separador por categoría y los planos con sus cuatro hojas. Cierra con los 40 que más dejan. |
| `BONUS 01` | **La Planilla de Cortes (.xlsx)**: cargás las piezas y te dice las barras, el conversor mm ↔ pulgadas con fracción en dieciseisavos, el presupuesto y un factor único para actualizar precios |
| `BONUS 02` a `08` | Los instructivos escritos: Cobralo Bien, Checklist Cero Errores, Terminación de Taller, El Taller de $500.000, Los que Dejan Plata, Vendé lo que Fabricás y el manual Soldá como un Pro |
| `BONUS 09` a `11` | Packs de planos extra: 120 escaleras y barandas, 150 portones y cercos, 10 estructuras de patio (**280 planos más**, ninguno repetido de la biblioteca) |
| `BONUS 12` | El Catálogo para Clientes: 114 páginas, una ficha con imagen por cada trabajo distinto, sin precios, para que el cliente señale |

**Cantidades por categoría, las de la landing:** trailers 180 · parrillas 145 · gimnasio 120 · portones de campo 210 · taller 165 · camioneta 95 · muebles 180 · estructuras 110.

**Santiago (2026-10-26):** *"quiero el pdf y cada bono"*. La biblioteca va en **un archivo único**, no partida por categoría; los bonus sí, cada uno por separado. El generador puede hacer las dos formas (`libro.construir_unico` y `libro.construir_categoria`).

### Cómo está armado cada plano (4 hojas, igual que promete la landing)
1. **El trabajo:** isométrico sombreado del trabajo terminado, tiempo, nivel, hierro que lleva, la lista de compra de la casa de hierros (barras enteras) y el precio de venta sugerido con la cuenta a la vista.
2. **El dibujo:** frente, lateral y planta **a la misma escala**, con cotas en **mm y pulgadas**, más un **detalle ampliado** que el motor ubica solo buscando el nudo con más uniones.
3. **La lista de cortes:** cada pieza con su letra, largo, pulgadas y tipo de corte; **diagrama de aprovechamiento** en barras de 6 m con 3 mm de sierra y el sobrante; un isométrico con las letras marcadas y el control previo al primer corte.
4. **El armado:** hasta 12 pasos, **cada uno con su propio isométrico** donde lo que se suma en ese paso va en naranja y lo ya armado en gris. Más los dos errores que arruinan ese trabajo y la terminación.

### El motor (qué sabe hacer)
- Geometría 3D de vigas, chapas inclinadas (`ref=`) y cilindros (`kind='cil'`, con `lados` para hexágonos), proyección isométrica con pintor por caras subdivididas y vistas ortogonales con silueta.
- **Lista de cortes automática** agrupando por material + largo + corte, letras A, B, C… y nesting *first-fit decreasing* en barras de 6 m. Las piezas de más de 6 m se marcan "se empalma" y se cuentan como dos barras.
- **Costos:** tabla de 48 materiales con precio por barra de 6 m o por m². Distingue **lo que pagás en el mostrador** (barras enteras) de **lo que consume el trabajo** (metros usados + 8 % de desperdicio), que es lo que entra en el precio.
- **Precio sugerido:** material × 1,12 (insumos) + horas × $48.000, y el techo del rango es eso × 1,30. La misma fórmula aparece explicada en la guía y calculada en la planilla.
- **60 familias paramétricas:** cada una genera todas las medidas que quieras (`expansion.py`). Los 1.205 planos salen de esas familias; subirlo a 2.000 es cambiar un número.

### Los códigos de los ads existen adentro
**BQ-028** fogonero hexagonal de 122 cm, **BQ-053** Santa María, **BQ-090** parrilla argentina, **TR-072** trailer con rampa, **TR-129** porta autos, **FM-068** hoja de portón de 3,66, **SH-148** mesa para motos, **TK-024** rack overland, **TK-082** protector de cabina, **ST-015** pérgola, **ST-064** escalera, **FN-022** mesa de patas en X, **FN-107** isla de cocina, **GY-020** jaula, **GY-096** rig. Los 115 planos curados conservan su código; el resto se numeró alrededor.

### Lo que falta y las dos advertencias
- **El curso de soldadura en video (Bonus 8) no está.** Se entrega el manual escrito con el mismo nombre. La landing lo promete en video y en el hero ("No son solo PDFs"). Hay que decidir: producirlo aparte o cambiar ese texto de la landing.
- **Los precios del producto son más bajos que los del banco de fichas** de arriba. Las fichas viejas salían de convertir los dólares del original ×1.000; las del producto salen de una tabla de materiales coherente entre sí. **Para guiones nuevos conviene usar los números del PDF**, que es lo que el comprador ve adentro.
- **Muchos planos son la misma familia en otra medida.** Es como está armado cualquier pack de 1.200 planos del mercado y cada variante trae su propia lista de cortes y su propio precio, pero conviene saberlo antes de prometer "1.200 trabajos distintos": trabajos distintos hay 451, medidas hay 1.205.

## El avatar del competidor: cuánto lo usan y para qué (2026-10-28)

Pregunta de Santiago: *"la página original usa muchos videos con avatar, ¿no?"*. Conteo completo en `OUTPUTS/2026-10-28-herrero-avatar-vs-voz-en-off.md`.

- **Usan avatar, pero es el segundo formato, no el principal:** 32 de 180 videos (17,8 %) y 120 de 631 copias (19 %). El nuestro —voz en off sobre B-roll y fichas— sigue siendo el 64 % de sus copias.
- **El video más copiado de toda la muestra es avatar:** el 002, con **21 copias**. Del top 10 por copias, 6 llevan avatar.
- **Es a donde están migrando:** en los 30 videos más nuevos (150–179) hay 9 con avatar, el 30 %. Y suman **personajes nuevos**: el herrero de camisa oscura de siempre, un pelirrojo con delantal de cuero (151, 168, 179) y dos mujeres (139, 153). Así renuevan formato sin inventar ángulos nuevos.
- **El formato exacto no es un talking head:** es el **avatar recortado sin fondo, parado en la mitad inferior, presente todo el video**, con el B-roll cambiando atrás y subtítulos de una sola palabra (002, 040, 046, 051, 056, 062, 079, 140, 149). Para nosotros es barato: el fondo ya lo producimos, solo se suma la capa del avatar.
- **Lo que el avatar habilita y la voz en off no:** la **primera persona**. 24 de 31 guiones de avatar (77 %) arrancan con una confesión del herrero ("yo cotizaba a ojo y perdía plata en la mitad de los trabajos"), contra el 24 % del resto. Una confesión necesita una cara que se haga cargo: sin ella queda sin dueño, que es lo que pasó con el V1 (anécdota, único conjunto con cero ventas).
- **Por qué importa ahora:** la V22–V27 falló por repetir formato y la V34–V39 cambió la edición pero sigue siendo voz en off. El avatar es el cambio de formato más grande disponible y el único validado con plata por el competidor. Tanda propuesta de 3 (A1 el V7 en primera persona, A2 "yo cotizaba a ojo" de su 004, A3 "¿qué más sabés hacer?" de su 011), con **Avatar IV** y la voz **"damian"** de HeyGen, editor derivado de `edit_atlas_avatar.py` ([[atlas-de-cortes]]). **Pendiente de decisión de Santiago.**

## Preguntas abiertas
- **Producto:** resuelto el 2026-10-26 con la Biblioteca de Planos generada por código (ver arriba). Falta rehacer con el generador las 8 páginas del carrusel "Abrí un plano" de la landing, que todavía son del original y están en inglés.
- Imágenes con algo de texto en inglés que quedaron: `planilla-impresa` ("CUT LIST – WELDING BENCH"), la nota manuscrita de la tapa del bonus 2 y los carteles chicos de `casa-de-hierros`.
- **Bonus 8:** ¿se produce el curso de soldadura en video o se cambia el texto de la landing? Hoy se entrega el manual escrito.
- ¿Garantía de 60 días o 7, como en otras ofertas?
- Upsells del checkout: falta analizarlos y armarlos.
- ImpulTienda con un HTML de 2,5 MB: si no lo acepta, subir la carpeta de imágenes y pasar a URLs.

## Los VSL de los post-pago (2026-10-28)

Los tres post-pagos ya están cargados en ImpulTienda como "Solo post-compra", **en este orden y con estos precios** (captura que pasó Santiago, 2026-10-28), que son los que dicen los guiones:

| | Producto (tal cual el botón) | Precio | Tachado |
|---|---|---|---|
| 1 | **El Sistema de Planos a Medida™ 📐💰** | $24.990 | $98.990 |
| 2 | **Asistente Personalizado 1 a 1 🤖✨** | $15.990 | $59.990 |
| 3 | **El Sistema del Hierro al Costo™ 🔩💰** | $7.990 | $29.990 |

⚠️ Con estos precios la escalera queda **descendente** (24.990 → 15.990 → 7.990) y ya no cumple la regla de [[embudo-vsl-post-pago]] de que **el ticket más alto va segundo**. Los guiones funcionan igual, pero si se quiere probar la regla alcanza con subir el precio del Asistente y retocar dos frases del VSL 2.

- **Guiones:** `OUTPUTS/2026-10-28-vsl-pospagos-herrero-de-finde.md` (copia en `~/Desktop/herrero-de-finde/pospagos/guiones-vsl-pospagos.md`). 1.030 / 958 / 804 palabras → **4:50 · 4:30 · 3:46 a 1,3x**. Duración decreciente, como pide la regla.
- **Encadenados, no independientes:** se felicita **solo en el 1**; el 2 abre retomando ("recién te hablé de las medidas que no están en la biblioteca") y el 3 abre avisando que es la última pantalla. El hilo escala: la biblioteca dice **qué fabricar** → el 1 suma **cualquier medida** → el 2 es **el que contesta cuando el papel no alcanza** → el 3 es el número del otro lado, **a cuánto comprás el hierro**. El 1 y el 2 cierran empujando a la pantalla siguiente ("y seguimos", "quedate un segundo más").
- **Cada uno con otra estructura**, para que no suene a plantilla repetida: el 1 va problema → escena → mecanismo; el 2 va escena nocturna → qué NO es → casos; el 3 va cuenta de plata → por qué pasa → manual.
- **Los números salen del motor del producto, verificados el 28/10:** el portón de campo de 3,40 m **no existe** en la biblioteca (están el de 3,00 y el de 3,66), y es el ejemplo del VSL 1; el Escalador da $117.000 de hierro → $370.000-$480.000 para esa medida; la parrilla con carro BQ-090 ($406.000 → $1.030.000-$1.340.000) es el presupuesto que arma el asistente en el VSL 2; y los $124.000 de hierro del portón FM-068 son la base de la cuenta del 20 % del VSL 3.
- **Garantía: 60 días** en los tres, la misma de la landing (la regla pide 30+).
- **Dos entregables por VSL**, sin bono sorpresa, como pide la regla del 15/10.
- **Producidos el 29/10**, en `~/Desktop/herrero-de-finde/pospagos/`:

| | Archivo | Duración | Planos |
|---|---|---|---|
| 1 | `HF-OTO1-planos-a-medida.mp4` | **4:53** | 32 |
| 2 | `HF-OTO2-asistente-1-a-1.mp4` | **4:22** | 31 |
| 3 | `HF-OTO3-hierro-al-costo.mp4` | **3:26** | 29 |

- **Cómo se produjeron:** voz **Enzo** de Google AI Studio, grabada en seis bloques (dos por VSL, cortados en `Esto no está en la página` / `Dos cosas te llevás.` / `Eso es el Sistema del Hierro al Costo`) para no pasarse del límite del TTS; cada bloque verificado por transcripción y por md5. Avatar **HERRERO** de HeyGen en **Avatar IV 1080p**, subiendo el audio ya acelerado (`atempo=1.12`, no 1,2-1,3: Enzo ya habla rápido). **204 créditos** de HeyGen para los seis bloques. Edición con `OUTPUTS/scripts-vsl/edit_herrero_avatar.py` y los planes de `pospagos/work/plans/gen_oto.py`.
- Falta: los tres downsells con ruleta.

## Relacionado
[[infinity-3d]] · [[bachas-de-concreto]] · [[landings-funnels-y-upsells]] · [[quizzes-reglas-de-armado]] · [[internacionalizacion]] · [[diagnostico-de-checkout]] · [[lectura-de-resultados]] · [[pagina-de-ventas]]

## Fuentes
- Biblioteca de anuncios de Meta, page id 964653193405481 (2026-10-22)
- https://the-weekend-fabricator.impultienda.ar/ (2026-10-22)
