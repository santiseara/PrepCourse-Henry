# Quizzes: reglas de armado (checklist viva)

> Reglas y correcciones de Santiago para armar quiz funnels en HTML. **Leer completo antes de crear o editar cualquier quiz.** Cada corrección nueva se suma acá, con fecha. Si otro chat recibe esta carpeta, esta página alcanza para no repetir errores ya corregidos. La estrategia del formato (por qué funciona, métricas) está en [[quiz-funnel]].

## Cómo usar esta página
1. Antes de empezar un quiz, recorré la **checklist de entrega** (al final) y las reglas de cada sección.
2. Si Santiago corrige algo que sirve para **futuros** quizzes, sumalo al **registro de correcciones** y, si corresponde, a la regla de su sección.
3. Las correcciones puntuales de una oferta (un precio, un link) van en el registro, pero no como regla general.

## 1. Pedido típico
- "Copiá este quiz que corro en [país], cambiale el nombre del producto, hacelo en HTML y dame las imágenes."
- Los quizzes son **del propio Santiago** (los corre él, por ejemplo en InLead). Se modelan para otro producto o país.
- Plataforma de destino: **ImpulTienda**. Santiago pega el HTML y sube las imágenes ahí.

## 2. Fidelidad al original
- **Comunicación 100% igual**: mismos textos, el mismo orden de pasos, colores destacados y componentes. No "mejorar" el copy sin que lo pida, ni siquiera los errores de tipeo.
- **Renombrar solo la marca** que indica (ej. "Sana Pilates" → "Pilates Hormonal"). El nombre del **método** ("Pilates Asiático") queda igual salvo que diga otra cosa. Si hay duda, preguntar al final, sin frenar la entrega.
- Si el quiz es de otro idioma, **localizar** al español argentino con voseo (no traducir literal). Ejemplos: "RG" pasa a "DNI", "kkkk" a "jajaja", "reais" a "pesos".
- **No inventar datos** que el original no tiene: ratings ("4,9 de 5"), cantidad de opiniones, estadísticas. Corrección del 2026-10-12.

## 3. Cómo sacar el contenido del original
- **InLead** encripta el contenido del quiz en `__NEXT_DATA__` (campo `q`). No descifrarlo por código, porque el sistema de permisos lo bloquea. Se abre la página en Chrome, se ubica el array de pasos en el estado de React y se vuelca a la página para leerlo con `get_page_text`.
- Sacar también los colores de las palabras destacadas (estilos `color:` de cada `<strong>`) y el tema: color principal, fondo, fuente y bordes.
- Recorrer el original en el navegador para ver los componentes especiales: regla de altura/peso, gráfico, carga, oferta.
- **xquiz.link** (2026-10-14): el contenido viene sin cifrar en el payload de Next.js (`self.__next_f.push`). Se baja el HTML con `curl`, se decodifica y se saca el objeto `funnel` (`nodes`, `theme`, `navigation`). Cada página se abre directo con `/<slug>` para ver cómo se ve. Las imágenes están en `imagedelivery.net` y llegan a 512 px como máximo.
- **ImpulTienda con HTML propio (`custom_html`, 2026-10-24):** el quiz entero viaja en texto plano en el HTML de la tienda. Se baja con `curl -sL <url de la tienda>` y el bloque que pegó Santiago queda entre el `<body>` y los scripts de la tienda: markup, un `<style>` y un `<script>`. Se corta con `sed -n` y se edita directo. Las imágenes están en `i.postimg.cc` y en el `storage` de Supabase de la tienda, y se reusan tal cual. Ojo con el `<title>` y el `<meta description>`: quedan los de la tienda que clonó, así que no sirven para identificar la oferta.
- **HTML propio del competidor (2026-10-26, `calisteniafeminina.site`):** cada vez más quizzes escalados no usan plataforma: son **una sola página HTML en texto plano**. Se baja entera con `curl -sL` y adentro está todo — el array `STEPS` con preguntas, opciones y feedback, la sales page y los links de checkout. El flujo suele ser portada = 1ª pregunta → pasos → pantalla de análisis → **`vsl.html`** (VSL solo, sin oferta) → `/sales-page`. Ojo con el stack que traen: cloaker por geolocalización, TrackTurbo (pixel + UTMs) y player de VSLwave; **nada de eso se copia**. Las imágenes cuelgan de `/images/` y se bajan una por una.
- **InLead exportado dentro de ImpulTienda (2026-10-26, `calisteniaasiaticahombres.impultienda.ar`):** la tienda usa `custom_html`, pero adentro va un funnel de InLead **exportado en texto plano** como `window.FUNNEL` (JSON con `steps`, `design` y `navigation`). **No está cifrado**: se baja con `curl -sL`, se corta la línea del `window.FUNNEL` y se parsea con Python. Cada paso trae `layers` con `text`, `options` (con `value`, `label` y `image`), `height`/`weight`, `loading`, `charts`, `faq`, `bonuses` y `offer`. Las imágenes cuelgan del `storage` de Supabase de la tienda y se bajan numeradas (`…_landing-NN.webp`). Con eso alcanza: no hace falta recorrer el quiz en el navegador.
- **Lovable (`*.lovable.app`, 2026-10-15):** el quiz entero está en texto plano en el bundle `assets/routes-*.js` (preguntas, opciones, oferta, FAQ, popup de salida y testimonios). Se baja con `curl` y los colores salen de `:root` en `assets/styles-*.css` (vienen en `oklch`, se pueden usar tal cual). Las imágenes están en `/__l5e/assets-v1/…` y `/assets/…`. No hace falta abrir el navegador.
- **Lovable que sirve las imágenes desde `media.inlead.cloud` = quiz exportado de InLead (2026-11-04, [[monjaro-violeta]]).** El funnel sigue viniendo en texto plano en `assets/routes-*.js`, pero las imágenes son las de InLead y **el nombre del archivo trae el tamaño**: `…-xs-…`, `…-sm-…`, `…-md-…`. Las `xs` son de **96×80 px** y **no existe una versión más grande** (probado `sm`, `md`, `lg`, `xl`, `2x`: todos 404). Conviene chequearlo **antes** de planificar: si las siluetas de una pregunta son `xs`, esa pregunta va con íconos o hay que generarlas.
- **Lovable con backend propio (Supabase) = el contenido NO está en el bundle (2026-11-04, [[dancego]]).** Si en `assets/index-*.js` aparecen `from("funnel_steps")`, `from("funnel_elements")` y un panel de administración, el quiz se sirve desde la base y no viaja en texto plano. Se recorre en Chrome paso a paso leyendo `img.src` y `img.alt` con `javascript_tool` (clickear los botones por su texto es mucho más rápido que por coordenadas). **Las imágenes sí están todas en el bundle**: se saca la lista de `/lovable-uploads/<uuid>.png`, se bajan de una y se miran juntas en una **hoja de contactos** armada con Pillow. Eso evita abrir 81 archivos.
- **Ojo con lo que devuelve `javascript_tool`:** si el resultado incluye una URL con `?fbclid=…` o un pixel con query string, la llamada se bloquea entera. Devolver solo el nombre del archivo (`src.split('?')[0].split('/').pop()`).
- **Quiz para el mercado en inglés (2026-10-15):** se localiza al inglés de EE. UU.: moneda en USD con los mismos números, nombres de testimonios y chats americanizados, "Turma" → "Class", medios de pago locales (Pix, Boleto, Elo) afuera.
- **Rapidez (2026-10-14):** con el JSON de pasos ya alcanza. Mirar en el navegador solo los componentes raros, sin recorrer paso por paso, y no generar imágenes con IA salvo la que tiene texto que no se puede editar (la tapa).

## 4. Imágenes
- **Reutilizar** las imágenes del original que no tienen marca ni texto en otro idioma.
- Las que tienen **marca vieja o texto en otro idioma** se rehacen:
  - Texto plano sobre un fondo liso (banda dorada, título de tapa): se reemplaza con Pillow, con la misma tipografía y el mismo color. La foto queda idéntica.
  - Texto en perspectiva o en varios objetos (mockups): se genera de nuevo con IA.
- **IA de imágenes: Higgsfield con GPT Image 1.5**, calidad **High** y **1:1** para la columna del quiz. Para el modelo, buscar "GPT Image 1.5" en el selector; por defecto aparece GPT Image 2.
  - Generar **desde texto** cuando se pueda. Subir una referencia obliga a aceptar el "Media upload agreement", y eso **requiere el OK de Santiago**.
  - La imagen final se descarga del CDN cambiando `_min.webp` por `.png` (1024×1024).
- **Mockup del producto: celular con la app, potente y premium.** Nada de libros sueltos ("parecen libros sueltos y se ve horrible", 2026-10-12). Un iPhone flotando con la UI de la app (logo, video de la clase, progreso del reto, accesos), fondo cálido de estudio y luz suave.
- **CTA temprano en el hero, que NO va al checkout (2026-11-03, "sino queda re abajo el botón para comprar").** Debajo de los chips del hero va un botón que **ancla a la sección de "qué vas a recibir"** (`href="#incluye"`), no al checkout: el que recién llega ve toda la oferta antes de decidir. No lleva la clase `js-cta` (si la lleva, el JS le pisa el `href` con el link de pago y además dispara `AddToCart`), y la sección destino necesita `scroll-margin-top` porque la barra de urgencia es sticky.
- **La caja de oferta se presenta completa, estilo "launch promotion" (2026-11-03, "quedó re peruano, necesito que sea más completo, con toda la información de lo que se lleva, el producto, los bonos").** Una caja de precio con solo tachado + precio + botón se ve barata. El layout que pidió Santiago (referencia: `scentedstone.lovable.app`, bloque *Launch Promotion*), de arriba abajo:
  1. chapita ocre **★ PRECIO DE LANZAMIENTO ★** montada sobre el borde de la tarjeta
  2. **nombre del producto** grande en la serif display + bajada del mecanismo en mayúsculas chicas
  3. **precio tachado**, chapita verde con el **ahorro en pesos**, **precio de hoy** gigante y la línea de cuotas
  4. caja crema **"Todo lo que te llevás"**: un ✓ por ítem del producto (sin precio al lado), y el **acceso de por vida destacado aparte** en una tarjeta blanca
  5. caja de **borde punteado con 🎁**: "+ N regalos incluidos, sin costo", el valor tachado y una chapita verde **HOY: GRATIS**
  6. botón ancho, y abajo la micro-confianza (pago seguro · acceso por mail en 2 minutos)
  Los precios salen de los `data-` del CONFIG (`data-old`, `data-new`, `data-ahorro`, `data-valorbonus`, `data-cuotas`), nunca hardcodeados. Ojo con heredar `display:block` en los `<b>` de adentro: parte el "Valor $45.600" en tres líneas.
- **Los atributos `width`/`height` del `<img>` llevan las dimensiones REALES del archivo (2026-11-03, "la foto queda cortada y no se ve lo del costado").** En la landing de [[academia-del-trazo]] el mockup estaba declarado `width="460" height="460"` siendo 1122×1402: cualquier plantilla que respete esos atributos mete la foto en un box cuadrado y le come los costados (se perdía el badge "+ CURSO EN VIDEO"). Se miden con `PIL` antes de escribir el tag, y la imagen del hero se blinda para que ninguna plataforma la recorte:
  ```css
  .hero-img{width:100%;max-width:520px;height:auto!important;aspect-ratio:auto!important;object-fit:contain!important}
  ```
  Verificado inyectando CSS hostil (`img{height:520px;aspect-ratio:1/1;object-fit:cover}`): la imagen sigue entera. Se chequea midiendo en el navegador que `ratio renderizado == ratio natural` a 300, 350, 520 y 720 px de contenedor.
- **Portada con el texto quemado en otro idioma: se recorta y el lockup se rehace en HTML (2026-11-04, [[monjaro-violeta]]).** En vez de regenerar la tapa con IA (créditos, y la IA escribe mal el castellano), se recorta **solo el arte** (la foto, el producto, el fondo), se le aplica un **alfa en diagonal** —el fundido arranca antes en las columnas donde había texto y más abajo donde está la persona— y se guarda en PNG/WebP con transparencia, así se funde con el fondo de la página. El título se rehace **en HTML con CSS** (`background-clip:text` para el degradé, `text-shadow` para el glow, un `<span>` con `skewX` para la banda del brochazo): queda nítido, se edita en un segundo y no cuesta un crédito.
- **Chapas de color plano con una palabra adentro (2026-11-04).** `MULHER` → `MUJER` se resuelve con Pillow: se detecta el verde por rango de color para sacar el bounding box, se repinta **solo el rectángulo interior** (sin tocar los bordes, así las esquinas redondeadas se conservan solas) y se re-tipea centrado con **Arial Black**. Si la palabra nueva es más larga, se baja el cuerpo de la fuente en vez de achicar la chapa.
- **"No quiero que se vea recontra colorido" (2026-11-04, [[dancego]]): lo feo casi nunca son las fotos, es lo que les ponen encima.** En DanceGo las fotos del original eran buenas (estudio, fondo gris, ropa deportiva neutra, mismo encuadre) y se veían horribles porque tenían **un overlay de degradé rosa/violeta/verde/naranja**. Sacando el overlay y reusando el archivo original, el set entero queda premium sin generar una sola imagen. **Antes de rehacer nada, mirar si la foto está tapada por CSS.** La paleta pasa a: papel crema + tinta + **un** acento; el verde solo significa "bien" y el rojo solo "riesgo".
- **Carteles de IA con el texto quemado (tapas de ritmos, portadas de módulos): se rehacen tipográficos en CSS, no con IA (2026-11-04).** Color plano apagado + el nombre en la serif display + una línea chica arriba. Quedan nítidos, coherentes entre sí, se editan en un segundo y no cuestan un crédito.
- **La maqueta del celular se dibuja en HTML/CSS (2026-11-04).** Clonar la captura de la app del competidor arrastra su idioma y su paleta. Un `<div>` con marco redondeado, barra de estado, tarjeta de desafío, lista de logros y barra de pestañas se lee nítido en cualquier pantalla y los textos quedan en castellano.
- **Siluetas de tipo físico (2026-10-26, "las imágenes son muy malas"):** los recortes que traen los quizzes suelen ser **PNG/WebP con alfa y basura en los píxeles transparentes**, chicos (300–500 px) y con el modelo cortado a la altura del mentón. Sobre blanco se ven baratísimos. El arreglo: recortar al **bounding box del alfa** (umbral ~24), montarlos sobre una **tarjeta cuadrada de 600 px con un degradé gris muy suave** y dejarlos todos del mismo tamaño y con la misma línea de piso. Quedan como un set, no como recortes sueltos.
- **Recolorear una imagen reusada: siempre desde el original y en un solo pase** (2026-10-26). Se mapea **solo el matiz de origen** (el azul vive en 0,55–0,70; la piel en ~0,05) conservando saturación y luminosidad. Encadenar pases —azul → rojo → verde— arrastra el rango de matices y termina pintando caras y manos.
- **Dónde buscar fotos mejores (2026-10-26):** la vía es Biblioteca de Anuncios → el ad muestra el dominio → se baja el HTML de la landing y del `/start`. Fuentes que sirvieron para hombres 40+: **`menletics.com`** (imágenes en `funnelmedia.flmng.live/cdn-cgi/image/width=1200,.../menletics/landing/…`, selector de edad, flexiones, gimnasio) y **`musclebooster.welltech.com`** (`/_astro/…`; pedírselas al host final, `musclebooster.fitness` devuelve vacío). **Lo que NO sirve:** `quiz.calistenia.app` sirve sus siluetas a 96×96, y los funnels grandes (Menletics, GreatApps) tienen el quiz detrás de un "acepto términos" o de un token de API: no se tildan casillas de consentimiento por el usuario ni se sacan tokens.
- **La portada puede no llevar foto** (2026-10-26). Si la primera pregunta tiene opciones con imagen (el selector de edad), la foto de arriba **empuja las opciones abajo del fold** y compite con ellas. Sin foto, el orden es logo → chapita → titular → bajada → opciones, y las opciones entran enteras en la primera pantalla. Al sacarla hay que revisar los textos que la referencian ("mirá los resultados…"), que quedan huérfanos.
- **Una pregunta clara no lleva foto** (2026-10-26, "esta imagen quedó muy mal, no quiero imagen ahí"). La foto de un paso tiene que **aportar** —mostrar la opción (cuerpos, zonas de dolor) o el test que se pregunta (flexiones)—. Si es solo decorativa (un tipo mirando a cámara, alguien cabizbajo), **se saca**: el paso queda más limpio con la pregunta y las opciones solas.
- **Si falta una sola foto de un set, se genera esa** (2026-10-26). Pedirla con el mismo encuadre, fondo y vestuario que las reales (ej. "fondo negro, remera verde oliva, brazos cruzados, plano de cintura para arriba") y entra sin que se note. Si faltan varias, mejor sacar las fotos de esa pregunta y dejarla con íconos.
- **Revisar marcas de agua** (pngtree, freepik, etc.) en cada imagen del original y sacarlas. En los PNG transparentes, la marca suele tener alfa bajo, así que alcanza con borrar los píxeles con alfa menor a ~110 (2026-10-14).
- **Nada de capturas pixeladas.** Testimonios escritos, garantía y bloques de texto se arman en **HTML** (tarjetas nítidas), no como imagen. Corrección del 2026-10-12.
- **Foto redonda de la experta (2026-10-15, "se ve mal"):** armar una versión de la foto **sin ningún texto** (pintar el fondo) y recortar de ahí un plano abierto (cabeza entera, hombros y algo del producto), **sin agrandar** el recorte. Si se agranda, se pixela. Nunca recortar de la original con el nombre viejo.
- **Garantía en la paleta del quiz (2026-10-15, "se ve mal"):** no copiar la estética de la imagen original (fondo negro y rojo chillón) si choca con el diseño. Usar una tarjeta con los colores del quiz, sello dorado grande arriba, título en la fuente display y texto centrado. Los textos curvos del sello tienen que quedar adentro del círculo, sin pisar bordes ni anillos.
- **Quiz propio, sin original (2026-10-18, "las imágenes me dan ganas de irme del quiz", "se ve muy low ticket"):** nunca resolver las imágenes con ilustraciones SVG ni emojis grandes. Portada, opciones con imagen, género, recetas o resultados y oferta llevan **fotos profesionales** hechas en Higgsfield (GPT Image 1.5, High, 1:1), todas con el mismo estilo (misma luz, mesa y paleta) para que se vean como un solo producto. Los emojis quedan solo como íconos chicos en las opciones de lista.
- **Higgsfield:** antes de generar, **sacar las imágenes de referencia que quedaron cargadas** de otro proyecto (miniaturas arriba del prompt). Con el plan Plus se pueden lanzar ~4 imágenes a la vez; si se lanzan más, aparece la oferta de upgrade ("Skip Special Offer" para volver).
- Logo: si cambia la marca, rehacerlo con el mismo ícono y el mismo estilo tipográfico.

## 4b. Coherencia de componentes (2026-10-14)
- **Barra del IMC:** si el resultado dice "Sobrepeso", la bolita va **cerca de Sobrepeso** (~85%), nunca en Saludable.
- **Peso y altura (y peso deseado):** van **siempre** con un **medidor** (barra), aunque el original use botones +/− (2026-10-17) (un slider con el número grande en kg o cm y una regla), no con un campo de texto. Así es más fácil completarlos.
- **Si el quiz se bifurca por género, los textos tienen que concordar (2026-11-04, [[monjaro-violeta]]).** No alcanza con duplicar las preguntas de cada rama: los textos compartidos ("¿estás list**o**?", "Quedate tranquil**o**", "List**o**, Ana") quedan en masculino para todas las mujeres. La solución: un token `{{o}}` que el motor reemplaza por `a` u `o` según el género elegido, y por `a` mientras todavía no eligieron.
- **Zonas del cuerpo:** usar nombres que se entiendan en Argentina: "Caderas" en vez de "Cartucheras". Sacar "Flancos".

## 5. Diseño y textos de la oferta (último paso)
- **Último paso = VSL arriba de todo.** Toda la oferta queda **oculta** y aparece sola a los `SEGUNDOS_OFERTA` de llegar a ese paso. **Depende del VSL**: tiene que ser después del momento en que el VSL dice el precio. Pilates Hormonal: **3:50 (230 s)**; al principio eran 2:40. El timer de urgencia y las notificaciones **arrancan recién cuando aparece la oferta**.
- **La pantalla de resumen va corta** (2026-10-26, "tiene mucha info, se hace muy larga"). Una sola tarjeta con las barras del diagnóstico y **un** aviso, 4 chips como máximo, y el gráfico de previsión con 3 logros. Todo lo que el VSL va a decir igual no va acá.
- **El color de marca no puede significar "mal"** (2026-10-26). Si la paleta es verde, las barras de riesgo (IMC, testosterona) igual van de verde a rojo y el aviso de cupos queda en rojo: el verde tiene que seguir leyéndose como "bien" en todo el quiz.
- **Espaciado generoso** entre bloques y párrafos ("está todo muy pegado"). Como referencia: un gap de unos 30 px entre bloques e interlineado de 1,6.
- **Sacar encabezados de relleno** antes de la lista de beneficios ("¡Todo lo que necesitas…", "Al ingresar, desbloqueás…"). La lista va directa.
- **Orden de la oferta (2026-10-13):** cuenta regresiva → **cuadro de cuotas de Mercado Pago → aviso del email → botón de compra** → después todo lo demás. Así la persona puede pagar apenas termina el VSL. **Sin el bloque de precio grande** (tachado + "Solo hoy por APENAS $X").
- **Sellos e íconos dibujados en SVG:** calcular los puntos (simétricos), no dibujarlos a mano, porque quedan torcidos.
- **Texto curvo de un sello: solo en el arco de arriba** (2026-10-26). Si el `textPath` recorre el círculo entero, la mitad de abajo sale **al revés**. Va un arco de media vuelta (`M x1,cy A r,r 0 0 1 x2,cy`) con `startOffset="50%"` y `text-anchor="middle"`, y lo de abajo como texto horizontal común. El radio del arco tiene que dejar aire contra el anillo, o los acentos se pisan con el borde.
- **Todos los CTAs** (botones y cuadros de precio) llevan al link de checkout de ImpulTienda y le suman los UTMs de la URL.

## 6. Precios
- Formato ARS: **$14.990** (punto de miles), con "pesos (ARS)" en el precio grande.
- **Cuotas:** precio ÷ cantidad de cuotas, **redondeado hacia arriba** (14.990 ÷ 3 = 4.996,67 → $4.997).
- **% OFF:** recalcularlo con el precio tachado. Si cambia el precio, cambia el porcentaje.
- Cuando cambia el precio, **actualizarlo en todos lados**: precio grande, tachado, cuotas, FAQ ("pago único de…") y cualquier otra mención.

## 7. Notificaciones de prueba social
- **Discretas**: chicas, abajo a la izquierda, con avatar de inicial, fondo blanco translúcido y sombra suave. Nunca una franja grande al centro.
- Texto corto: "Claudia R. de Rosario se unió a [Marca]" + "hace X min · Quedan N cupos con descuento".
- **Los cupos tienen que ser coherentes: solo bajan** (ej. 8 → 7 → 6 … hasta un mínimo de 2). Nunca "3 cupos" y después "7 cupos". Corrección del 2026-10-12.
- Frecuencia: cada ~16 s, visibles ~4,5 s.

## 7b. El VSL dentro del quiz (2026-10-25)
- **Player propio por defecto, no embed.** Un `<video>` nuestro con el MP4 servido desde nuestro hosting: arranca solo apenas la persona llega al último paso, `playsinline`, **sin controles ni barra de progreso** para que no puedan adelantar hasta la oferta.
- **"El video tiene que arrancar de una."** Como el último paso se llega siempre después de clics (el quiz), hay activación de usuario: se intenta `play()` **con sonido** y, solo si el navegador lo rechaza, se pasa a `muted` y se muestra un cartel grande a toda pantalla **"TOCA PARA ACTIVAR EL SONIDO"**. Nunca arrancar en silencio de entrada.
- **El botón se desbloquea por el tiempo VISTO del video** (`timeupdate` + `currentTime`), no por un reloj: si pausan o se les corta, el botón espera. Se deja igual un `setTimeout` de respaldo con el mismo número, por si el video no informa su tiempo (embed externo o error de carga).
- **MP4 para web**: 720x1280, CRF 25, AAC 96k, `-movflags +faststart`. 17 minutos quedan en ~146 MB. El hosting tiene que aceptar *Range requests* o el video no puede ir cargando mientras se reproduce (`python3 -m http.server` **no** las acepta: sirve para probar que arranca, no para probar el salto de tiempo).
- VTurb/Panda: `VIDEO_URL` vacío y el embed adentro del `<template id="vsl-template">`. El botón **sigue saliendo por tiempo real del video**: Panda lo informa por `panda_timeupdate` y VTurb por `window.smartplayer.instances[0].video.currentTime`; el reloj queda solo de respaldo.
- **Panda arranca en silencio.** Por más que el embed traiga `allow="autoplay"`, el player sale mudo con su propio cartel ("Pulse aquí para activar el sonido"). Eso se configura en el panel de Panda, no desde el HTML: si Santiago pide que arranque con sonido o que el cartel hable como el resto del quiz, hay que tocarlo ahí. Confirmado en Protocolo Chía 28D el 2026-10-25.

## 8. Entrega (siempre)
> Desde el 2026-10-22, todo va dentro de `~/Desktop/<oferta>/` (`landing/`, `imagenes/`, `anuncios/`), no suelto en el Escritorio ([[como-trabajar-con-santiago]]).

1. **HTML final** en `~/Desktop/<producto>-quiz.txt`, copiado también con `pbcopy`. **Santiago lo quiere completo, listo para pegar en ImpulTienda**, con las imágenes embebidas (WebP en base64, ~1 MB) y el embed del VSL de **Panda Video** dentro de `<template id="vsl-template">`. Cuando hay cambios, se **reemplaza** el .txt viejo.
2. **Carpeta de imágenes** `~/Desktop/<producto>-imagenes/` con nombres claros (`p1-mujer.png`, `zona-papada.png`, `mockup.png`…). Sacar las que ya no se usan.
3. **HTML de prueba** `~/Desktop/<producto>-PRUEBA.html`: el mismo HTML con las imágenes **embebidas** (WebP en base64, ~1 MB), para abrir en Chrome sin la carpeta. Lo abro con `open -a "Google Chrome"`.
4. Copia en `OUTPUTS/AAAA-MM-DD-quiz-<producto>.html`.
5. Arriba del HTML, un **bloque de configuración** con `IMAGENES` (nombre → URL de ImpulTienda), `LINK_CHECKOUT`, `PIXEL_ID` y `SEGUNDOS_OFERTA`. El VSL va en `<template id="vsl-template">`.
6. **Probarlo en el navegador** antes de entregar: todos los pasos, sin imágenes rotas y con la oferta apareciendo a tiempo.

## ✅ Checklist antes de entregar
- [ ] Textos iguales al original, solo con la marca cambiada
- [ ] Ningún dato inventado
- [ ] Ninguna imagen con la marca vieja ni con texto en otro idioma
- [ ] Mockup: celular con app, sin libros
- [ ] Testimonios y garantía en HTML nítido
- [ ] Último paso: embed de Panda arriba y oferta oculta hasta después del precio en el VSL
- [ ] Espaciado amplio en la oferta
- [ ] Precio, tachado, cuotas, % OFF y FAQ consistentes
- [ ] Todos los CTAs con el link de checkout correcto
- [ ] Notificaciones discretas con cupos que solo bajan
- [ ] .txt + carpeta de imágenes + PRUEBA.html + copia en OUTPUTS


## 2026-11-04 · Dos cosas que deforman el quiz y no se ven en el escritorio

**1. El atributo `height=""` del `<img>` le gana al `aspect-ratio` del CSS.** La regla del 2026-11-03 manda poner en `width`/`height` las medidas reales del archivo. El efecto secundario: una foto de 640×853 declarada así y maquetada con `aspect-ratio:3/4` sale de **853 px de alto** igual, porque el atributo fija el alto y `aspect-ratio` solo actúa con `height:auto`. En DanceGo el antes/después ocupaba una pantalla entera. La solución es una sola línea en el reset:

```css
img{max-width:100%;height:auto;display:block}
```

y, donde importa de verdad, el blindaje completo: `height:auto!important;aspect-ratio:X!important;object-fit:cover`.

**2. Las grillas de dos columnas se desbordan a 373 px.** Una opción con ícono + texto + casilla entra bien a 540 px y se pasa 4 px en un teléfono. Se arregla apretando solo la variante en grilla (`padding:13px 11px`, ícono de 28 px, texto .88rem, flecha oculta), sin tocar la lista de una columna.

**Cómo se chequea, de una sola pasada:** se carga el quiz en un `<iframe>` de 390 px dentro de una pestaña abierta y se recorre **entero por código** (clickear `.opt/.pick/.rowpick`, el `♥` del swipe y `#next`), midiendo en cada paso `scrollWidth - clientWidth`. Devuelve la lista de pasos que se desbordan y en cuántos píxeles. Al final, verificar que todos los `.btn` tengan `text-align:center`.


## 2026-11-04 · Una foto de portada mala casi siempre es un recorte malo

Santiago, sobre las 4 fotos de edad de [[dancego]]: *"Las imagenes del principio son muy malas."* Eran retratos de estudio **buenos** (1024×1024, fondo gris parejo, misma ropa, misma luz) y se veían espantosos por el encuadre: la persona ocupaba un tercio de la tarjeta y el resto era gris vacío. A 170 px de ancho las cuatro parecían **la misma mujer**, y el rango de edad no se leía.

**El arreglo no fue cambiar la foto, fue apretar el recorte.** Zoom ~1.95 sobre el alto, centro vertical en 0.26–0.27 (la cara arriba, porque abajo va la banda), salida 720×960 en 3:4. Con la cara llenando la tarjeta se ven de una las arrugas, el pelo cano y la edad de cada una: pasan a ser cuatro personas distintas.

**Reglas:**
- Antes de salir a buscar o generar fotos nuevas, **probar el recorte apretado de las que ya hay** y mirarlas al tamaño real. Es gratis y resuelve la mayoría de los casos.
- En una tarjeta de opción, **el sujeto tiene que llenar el encuadre**. Si hay más fondo que persona, el recorte está mal.
- Cuando la opción es un **rango de edad**, lo que tiene que entrar en el recorte es la **cara**, no el cuerpo: la edad se lee ahí. Para tipo de cuerpo es al revés.
- **La etiqueta va encima de la foto**, sobre una banda oscura (`linear-gradient` de transparente a `rgba(23,22,26,.88)`), no debajo en una franja blanca: la tarjeta gana alto de imagen y se ve más llamativa. Sin la banda, el texto blanco se pierde contra el fondo claro del estudio.
- "Más llamativo" **sin volver a lo colorido** se consigue con jerarquía, no con color: chapita oscura arriba con la prueba social, titular más grande (2.05rem) y foto a sangre.

## 2026-11-04 · Antes de decir "usemos una que ya tengamos", mirar si existe

Santiago pidió reusar imágenes de otras ofertas. Se revisaron las carpetas de `~/Desktop/` (Monjaro Violeta, Tai Chi Fit, Dibujo Creativo, Drawing World) y **no había ningún set de edades de mujeres** que sirviera: las de Monjaro son parejas (hombre + mujer) recortadas sobre negro a 300 px. Conviene **mirar primero y decirlo**, en vez de prometer un reuso que no existe. Una hoja de contactos con Pillow de todas las carpetas se arma en un minuto y responde la pregunta de una.

## Registro de correcciones
| Fecha | Quiz | Corrección | Regla |
|---|---|---|---|
| 2026-11-04 | Quiz DanceGo | "Las imagenes del principio son muy malas, usa algunas que ya hayamos usado y que se vean mejor, hacelo mas llamativo, las del tipo de musica sacalas" | Las fotos estaban bien: el problema era el **encuadre**. Recorte apretado a la cara (zoom 1.95, 720×960), etiqueta sobre banda oscura encima de la foto, chapita de prueba social y titular más grande. Los 7 ritmos quedaron **sin imagen**: tarjeta tipográfica sola |
| 2026-11-04 | Quiz DanceGo | "Mejoramelo, no quiero que se vea recontra colorido, quiero que las imagenes se vean bien" | §4: el problema era el **overlay de degradé** sobre fotos que ya estaban bien. Paleta de papel crema + tinta + un acento; tapas de ritmos y maqueta de celular rehechas en CSS; capturas de WhatsApp e Instagram pasadas a HTML; `img{height:auto}` global y chequeo de desborde a 390 px |
| 2026-11-04 | Landing Academia del Trazo | "Esos botones también tienen que redirigir, TODOS LOS BOTONES" (captura de la chapita verde **HOY: GRATIS** de la caja de regalos) | §4: **todo lo que parece un botón lleva al checkout**, no solo los `.btn`. Una chapa de color con bordes redondeados (`.free`, pastillas de precio, sellos) se toca igual que un botón: o va dentro de un `<a class="js-cta">`, o el JS le pone `cursor:pointer` y un `click` a `/checkout` con las UTMs. Antes de entregar: listar en consola **todos** los `<a>` y `<button>` más los elementos con fondo opaco y `border-radius`, y revisar que ninguno quede muerto. El botón del hero (`VER TODO LO QUE INCLUYE`) **dejó de ser ancla** y también va al checkout |
| 2026-11-04 | Landing Academia del Trazo | "Si la página ya estaba terminada, no tenías que cambiar nada más que los botones de CTA redirijan al checkout" | **Alcance:** un arreglo puntual sobre una página ya terminada toca **solo eso**. Las imágenes del CDN del original, el `PIXEL_ID` vacío y cualquier otro pendiente anotado **se avisan en una línea y se esperan**; estar en el `changelog.md` no los autoriza. Ver [[como-trabajar-con-santiago]] |
| 2026-11-04 | Tai Chi Fit | "Que todo eso aparezca recién a los 4 minutos… y abajo del VSL ya les pongas un botón de CTA que los redirija directo a checkout, como para que no tengan que deslizar tanto" | §5: además de la oferta diferida, va un **botón de checkout pegado abajo del video** (`#cta-vsl`), que aparece con el mismo disparador que la oferta y lleva `data-cta` para heredar el link y los UTMs. Y el retraso puede ser **un tiempo redondo que pide Santiago**, no siempre el segundo exacto del precio en el VSL |
| 2026-11-04 | Tai Chi Fit | El apelativo por defecto seguía siendo **"Guerrera"** (del quiz militar original) y se veía 3 veces en el último paso | Cuando se cambia el **tema** de un quiz modelado (§2), el barrido no puede quedarse en los textos de las preguntas: hay que revisar también **el nombre por defecto** (`state.nombre||'...'`), los textos del mockup de la app y los comentarios del CSS. En Tai Chi Fit pasó a **"Aprendiz"**, que es el primer nivel del propio quiz |
| 2026-11-03 | Landing Academia del Trazo | "Quiero que pongas un botón de cta entre medio de esos textos, porque sino queda re abajo el botón para comprar… que no lleve al checkout, sino que lleve a la presentación de la oferta" | §4: botón en el hero anclado a la sección de "qué vas a recibir", sin `js-cta` |
| 2026-11-03 | Landing Academia del Trazo | "Esto quedó re peruano, necesito que sea más completo, con toda la información de lo que se lleva, el producto, los bonos" | §4: caja de oferta completa estilo *launch promotion* (chapita, nombre, precio, lista de ✓, acceso de por vida destacado, caja punteada de regalos con valor tachado, botón y micro-confianza) |
| 2026-11-03 | Landing Academia del Trazo | "Fijate que la foto queda cortada y no se ve lo del costado" | §4: `width`/`height` del `<img>` con las dimensiones reales del archivo + blindaje `height:auto!important;aspect-ratio:auto!important;object-fit:contain!important` en el mockup del hero |
| 2026-10-26 | Calistenia Rusa | "Sacá la foto del principio, la del antes y después" | §4: si la primera pregunta ya tiene opciones con imagen, la portada va sin foto. Revisar los textos que la referencien |
| 2026-10-26 | Calistenia Rusa | "Esta imagen quedó muy mal, no quiero imagen ahí, y la del tipo durmiendo que ponés después también sacala" | §4: la foto de un paso solo va si muestra la opción o el test. La decorativa se saca |
| 2026-10-26 | Calistenia Rusa | "Las imágenes son muy malas, busca otros quiz de calistenia militar que tengan mejores fotos, y usa esas" | §4: las fotos se sacan de los competidores del mismo nicho vía Biblioteca de Anuncios → dominio → HTML de la landing. Las siluetas con alfa sucio se limpian y se montan en tarjeta. Si una sola falta, se genera con el encuadre del set |
| 2026-10-26 | Calistenia Rusa | "La slide que muestra el resumen tiene mucha info, se hace muy larga, hagámosla más corta" | §5: la pantalla de resultado va corta — una tarjeta con las barras, 4 chips, 3 logros |
| 2026-10-26 | Calistenia Rusa | "Los colores reemplaza el rojo por un verde que quede bien, medio oscurito" | Verde #1F6B47 (el mismo de [[secreto-de-la-insulina]]). Las barras de riesgo y el aviso de cupos quedan en rojo, para que el verde siga significando "bien" |
| 2026-10-26 | Calistenia Rusa | "Quiero que hagamos un quiz simple, porque va a tener vsl… quitarle algunas preguntas que sintamos que están de más, y dejarlo bien clean" | Cuando el embudo lleva VSL, el quiz **se recorta**: se van todos los bridges de texto (el VSL los dice mejor), las preguntas redundantes y el bloque de hábitos (agua, sueño, alimentación, energía), y la segunda página de venta duplicada. Quedan las preguntas que **personalizan el resultado** (objetivo, cuerpo actual y deseado, molestias, nivel, dolores, altura y pesos) y las de compromiso emocional. Antes de cortar se le muestra la lista de pasos que quedan y la de los que se van, y elige él |
| 2026-10-26 | Calistenia Rusa | Flecha azul del antes/después sobre una paleta roja | Cuando la paleta cambia de tema, las **imágenes reusadas con elementos gráficos de color** (flechas, marcos, destacados) se recolorean con Pillow mapeando el matiz y conservando saturación y luminosidad. La foto queda idéntica y no hace falta IA |
| 2026-10-26 | Tai Chi Fit | "Usá su mismo quiz, que es cortito, simple y directo, y donde diga cosas de militar lo adaptás a Tai Chi" | Cuando el quiz modelado tiene un **tema** (militar, espacial, etc.) se cambia el tema entero —vocabulario, rangos, paleta e íconos— pero **no** la cantidad de pasos, su orden ni su lógica. Las preguntas que dependen del producto (ej. "cuántas flexiones hacés") se reemplazan por el test equivalente de la disciplina nueva (ej. equilibrio en un pie), nunca se borran |
| 2026-10-24 | Protocolo Chía 28D | "No es landing, es quiz, este es el link del quiz, tmb lo tenemos que armar" | El quiz del VSL se copia igual (5 pasos, pantalla de análisis, VSL arriba y CTA con retraso) y solo se pasa a español neutro y al precio nuevo. `SEGUNDOS_OFERTA` se calcula con el segundo exacto en que **nuestro** VSL dice el precio, no con el número del original |
| 2026-10-22 | Landing Herrero de Finde | "Me encantó la landing… los primeros textos, que estén alineados al centro" | En landings, los textos del hero (eyebrow, titular, promesa y bajada) van centrados aunque el original los alinee a la izquierda |
| 2026-10-18 | Pan Sin Picos | "Las imágenes son muy malas, me dan ganas de irme del quiz, se ve muy low ticket" (pan en SVG y emojis) | §4: fotos profesionales con IA y un mismo estilo en todo el quiz; nada de ilustraciones ni emojis como imagen principal |
| 2026-10-17 | Secreto de la Insulina | "Quiero que sea igual al de él, basémonos en lo validado, el de Mounjaro no funcionó" | §2: cuando pasa el quiz de un competidor escalado, se copia **ese** quiz paso a paso (textos, orden, lógica). No se arma desde una plantilla propia ni se "mejora" el copy |
| 2026-10-17 | Secreto de la Insulina | Colores: "verde medio oscurito" en vez del naranja original | Paleta verde (#1f6b47); el logo naranja se recolorea a verde con Pillow (mismo diseño) |
| 2026-10-17 | Secreto de la Insulina | La promesa es la cantidad de kilos que la persona quiere bajar, en 21 días | Kilos = peso actual − peso deseado, sin multiplicadores (el original inflaba ×1,2) |
| 2026-10-17 | Secreto de la Insulina | "Las medidas de peso y altura las quiero con barra siempre" | §4b: peso, altura y peso deseado siempre con medidor (barra), aunque el original use botones +/− |
| 2026-10-15 | Chinese Embroidery | La garantía y la foto de Juliana "se ven mal" | §4: garantía en la paleta del quiz; foto de la experta sin texto, plano abierto y sin agrandar |
| 2026-10-15 | Chinese Embroidery | Checkout `https://chinese-embroidery.impultienda.ar/checkout` y precio 27 USD (no 27.90) | §6: en USD, precio redondo si así lo pasa; actualizarlo en todos lados (caja de precio y tachado del popup) |
| 2026-10-14 | Mounjaro Humilde | VSL final de Panda en el último paso; "QUIERO MI PLAN" al 1:20 → `https://mounjaro-humilde.impultienda.ar/checkout` | Los botones de los VSL del quiz usan el tiempo real de Panda (`panda_timeupdate`, filtrado por iframe) y, si no llega, un reloj desde `panda_play` |
| 2026-10-14 | Mounjaro Humilde | VSL de la nutri (Panda) en el paso 12, con el botón Continuar a los 30 s; sacar el audio de la página de resultados | Embed de Panda en `<template id="vsl-nutri">` y `SEGUNDOS_BOTON_VSL_NUTRI` |
| 2026-10-14 | Mounjaro Humilde | "Cartucheras" → "Caderas" y sacar "Flancos" | §4b zonas |
| 2026-10-14 | Mounjaro Humilde | Imagen "Todavía no sé" con marca de agua | §4 marcas de agua |
| 2026-10-14 | Mounjaro Humilde | El IMC decía "Sobrepeso" con la barra en "Saludable" | §4b barra del IMC |
| 2026-10-14 | Mounjaro Humilde | Peso y altura con medidor | §4b medidor |
| 2026-10-25 | Protocolo Chía 28D | "Poneme el vsl en el quiz, y quiero que el botón de cta aparezca a los 16 minutos, el video tiene que arrancar de una" | §7b: player propio con autoplay con sonido y botón por tiempo visto del video |
| 2026-10-14 | Mounjaro Humilde | Sacar la pantalla de "¿Dónde preferís recibir tu plan? WhatsApp / E-mail" | No incluir el paso de elegir canal |
| 2026-10-15 | Mounjaro Humilde | Sacar también el paso del e-mail: "en el checkout se lo pedimos también" | **No pedir e-mail ni WhatsApp en el quiz**: los datos de contacto se piden en el checkout |
| 2026-10-14 | Mounjaro Humilde | "¿Por qué tardás tanto?" | §3 rapidez: armar desde el JSON, sin recorrido completo ni IA de más |
| 2026-10-13 | Landing Palabras de la Obediencia | Copiar la landing de VSL sin footer ni políticas; botón verde "COMPRAR AHORA" a los 2:45 del VSL de Panda | Landing de VSL: el botón se dispara con el tiempo real del video (`panda_timeupdate` por postMessage) y no con un reloj |
| 2026-10-12 | Pilates Hormonal | Sacar "¡Todo lo que necesitas…" y "Al ingresar, desbloqueás…" | §5 sin encabezados de relleno |
| 2026-10-12 | Pilates Hormonal | Más espacio entre textos | §5 espaciado |
| 2026-10-12 | Pilates Hormonal | Precio $14.990, tachado $49.990, cuotas recalculadas | §6 |
| 2026-10-12 | Pilates Hormonal | Mockup de libros sueltos "horrible": celular con app | §4 mockup |
| 2026-10-12 | Pilates Hormonal | Testimonios escritos en imagen se veían mal | §4 HTML nítido |
| 2026-10-12 | Pilates Hormonal | Notificaciones feas e incoherentes (cupos 3 → 7) | §7 |
| 2026-10-12 | Pilates Hormonal | Imagen de garantía mejorada | §4 HTML nítido |
| 2026-10-12 | Pilates Hormonal | Todos los CTAs → `https://pilates-hormonal.impultienda.ar/checkout` | §5 CTAs (link propio de la oferta) |
| 2026-10-12 | Pilates Hormonal | Último paso: VSL arriba y oferta oculta 2:40 | §5 |
| 2026-10-13 | Pilates Hormonal | VSL de Panda (9:16) cargado; la oferta pasa a aparecer a los 3:50 | §5 |
| 2026-10-13 | Pilates Hormonal | Sacar el bloque de precio $14.990/tachado; las cuotas y el botón van primero, debajo de la cuenta regresiva | §5 orden de la oferta |
| 2026-10-13 | Pilates Hormonal | El sello de garantía estaba torcido | §5 sellos en SVG |
| 2026-10-13 | Pilates Hormonal | El .txt final va completo, con las imágenes embebidas, para pegarlo en ImpulTienda | §8 |
| 2026-10-12 | Pilates Hormonal | Imágenes con GPT Image 1.5 en Higgsfield | §4 |

## Preguntas abiertas
- ¿"Pilates Asiático" pasa a llamarse "Pilates Hormonal" en los textos o queda como nombre del método?
- ¿El sello de pago seguro (Visa, Mercado Pago) también se pasa a HTML?
- ~~¿Los 2:40 son fijos?~~ No: dependen de cada VSL (Pilates Hormonal: 3:50).
- ¿ImpulTienda acepta pegar un HTML de ~1 MB? Si no, volver al .txt liviano con las URLs de las imágenes subidas.

## Relacionado
[[quiz-funnel]] · [[imagenes-y-mockups]] · [[shopify-y-checkout]] · [[como-trabajar-con-santiago]] · [[landings-funnels-y-upsells]]

## Fuentes
- Conversación del 2026-10-12 (quiz de Pilates Hormonal, modelado de Sana Pilates). Entregable: `OUTPUTS/2026-10-12-quiz-pilates-hormonal.html`

## 2026-10-27 · Entregar el quiz para ImpulTienda

- El entregable es **un solo `.txt` autocontenido** que se pega en el `custom_html`: `OUTPUTS/scripts-vsl/inline_quiz.py <quiz.html> <salida.txt>` mete cada imagen de `CONFIG.IMG` como data URI.
- **Pasar todo a webp con tope de 1000 px de ancho.** Sin eso, un `mockup.png` de 1,1 MB se vuelve 1,5 MB en base64 y el archivo entero pasa de 2,4 MB. Con la conversión quedan 858 KB sin pérdida visible.
- **El embed de un VSL va dentro de `<template id="vsl-template">` y solo el `<iframe>`**, sin el `<div>` envoltorio que dan Panda o VTurb: el marco del quiz ya resuelve el 9:16.
- **Si el pedido es "que el botón aparezca a los X minutos", el disparador es el reloj**, no el `timeupdate` del reproductor: con el tiempo del video, el que adelanta se saltea la espera. El reloj arranca cuando se monta el player, o sea cuando entran a la última slide.
- Antes de entregar, probar con una copia de `SEGUNDOS_OFERTA` chiquito y verificar que la oferta aparece sola.

## 2026-10-27 · La marca del logo tiene que significar algo

Santiago, sobre la estrella del encabezado de Calistenia Rusa: *"no me gusta la estrella, hay dos opciones, o ponés algo más relacionado a la calistenia, o nada"*. Reglas:
- **Una estrella genérica no es un logo**: no dice nada de la oferta. O la marca es del tema, o va solo el texto.
- A **30 px** casi nada se lee. De cuatro intentos (dominada, brazo flexionado, bandera humana, anillas) solo sobrevivieron las **anillas de gimnasia**: dos círculos colgando de una barra, trazo 2.3 sobre un SVG de 19 px. El brazo flexionado quedó como mancha y la bandera humana se lee como una bandera común.
- Antes de elegir, **renderizar los candidatos al tamaño real** (30 px) en una página aparte con Chrome headless y mirarlos. A 60 px todos parecen buenos y después no se entiende ninguno.
- **Terminó eligiendo el texto solo.** Le mostré las anillas ya puestas y respondió: *"no, sacale el logo, dejá solo lo de calistenia rusa coach santi"*. Es la segunda vez en la misma tarea que prefiere quitar antes que agregar (ya había sacado dos fotos de pasos y la del encabezado). Regla: **cuando duda entre una marca y nada, la respuesta es nada** — y conviene ofrecer esa opción primero en vez de presentar un ícono nuevo.

## 2026-10-27 · Un botón en flex no centra el texto que se parte en dos líneas

Santiago: *"el botón de cta del final está alineado a la izquierda"*. Era el CTA de abajo del VSL, el que aparece con la oferta: en pantalla de teléfono "Obtener mi plan personalizado ahora" se parte en dos renglones y **el segundo quedaba pegado a la izquierda**.

La causa: `.btn` es `display:flex` con `justify-content:center`. Eso centra la **caja** del texto dentro del botón, pero adentro de esa caja el texto sigue alineado según `text-align`, que hereda `start`. Con una sola línea no se nota; con dos, sí. El CTA del cierre no mostraba el problema porque está dentro de `.prueba`, que ya tiene `text-align:center`.

**Regla: todo `.btn` lleva `text-align:center` además del `justify-content:center`.** Y al revisar un quiz, mirar los botones **en ancho de teléfono**, que es donde las etiquetas largas se parten.

**Cómo revisar en ancho real sin salir del navegador:** Chrome headless con `--window-size=390,...` **no aplica el viewport** (maqueta ancho y recorta, y parece que hubiera desborde cuando no lo hay). Lo que sí funciona es cargar la página en un **`<iframe>` de 390 px** dentro de una pestaña ya abierta: ahí el viewport es real, corren las media queries y se puede medir con `getBoundingClientRect()` sobre `contentDocument`.
