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
- **Estilos:** avatar de IA del herrero (gorra gris, camisa), podcast de dos herreros, dibujos animados (Buck), UGC de chicas, y **voz en off sobre B-roll de soldadura + fichas de planos**. Para nosotros, solo el último.
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
- **Videos finales:** `anuncios/HF-V7…HF-V12-*.mp4`, de 46 a 61 s.

### Dos cosas que salieron de este render (reglas)
- **`fit_w` va en 1.0, no en 1.2.** Con 1,2 la ficha se escala más ancha que la pantalla y se recorta un 8% por lado: se perdía el título del plano y la columna de la derecha de las tablas (la de los precios y la de los largos de corte). Con 1.0 entra entera con margen.
- **Revisar los tramos tardíos del B-roll.** El clip `7566063571134680350.mp4` (Y) lleva el cartel en inglés *"And that's how you do that"* desde el segundo 97 hasta el final, y se coló en el V8. En `gen2.py` quedó el diccionario `LIMITE = {'Y': 96}` para cortar ese tramo. Antes de dar una tanda por buena, mirar frames de los videos terminados, no solo de los clips.
- **Ojo con la ocurrencia de las palabras ancla.** En el V8 anclé la pérgola en `'cinco,'` ocurrencia 0, que es la primera palabra del guion ("Cinco trabajos…"), y el render se cortó con `max() arg is an empty sequence`. Cuando el hook repite una palabra del cuerpo, contar las ocurrencias.

## Preguntas abiertas
- **Producto:** ¿de dónde sale la biblioteca de planos en español? Las 8 páginas del carrusel "Abrí un plano" son del original y están en inglés.
- Imágenes con algo de texto en inglés que quedaron: `planilla-impresa` ("CUT LIST – WELDING BENCH"), la nota manuscrita de la tapa del bonus 2 y los carteles chicos de `casa-de-hierros`.
- ¿Garantía de 60 días o 7, como en otras ofertas?
- Upsells del checkout: falta analizarlos y armarlos.
- ImpulTienda con un HTML de 2,5 MB: si no lo acepta, subir la carpeta de imágenes y pasar a URLs.

## Relacionado
[[infinity-3d]] · [[bachas-de-concreto]] · [[landings-funnels-y-upsells]] · [[quizzes-reglas-de-armado]] · [[internacionalizacion]]

## Fuentes
- Biblioteca de anuncios de Meta, page id 964653193405481 (2026-10-22)
- https://the-weekend-fabricator.impultienda.ar/ (2026-10-22)
