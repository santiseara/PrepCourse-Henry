# Reseteo del Nervio Vago 28

> Oferta nueva para **LATAM** (español neutro): plan de **28 días para resetear el nervio vago** —respiración lenta, tarareo, agua fría y movimientos de cuello, 5 a 15 minutos por día— con quiz de 36 pasos. Clon del quiz argentino que corre en `nervio-vago.impultienda.ar`. Pedido de Santiago el 16/11: *"Necesito que me hagas este quiz. Pero va a ser para latam, así que ajustá el acento al neutro"* + *"Usa las mismas imágenes, todo igual, si alguna se ve mal, ajustala"*.

## Ideas clave
- **El avatar es mujer de 35 a 55+** que vive cansada, ansiosa, con la cabeza nublada y el cuello duro. Todo el copy del original está en **femenino** (*estresada, cansada, descansada*) aunque el paso 2 pregunte Mujer/Hombre: se respetó tal cual.
- **El mecanismo es el nervio vago trabado = "modo alerta".** El cable que une cerebro, corazón, pulmones y estómago; cuando se traba, el cortisol no baja, se duerme mal y se digiere mal. La promesa: el nervio vago **se entrena**.
- **Producto:** el plan de 28 días día por día + 3 bonos (SOS Ansiedad, Dormir de corrido, Comer para desinflamarte). Garantía de 7 días.
- **Checkout: `https://resetnervio-vago.impultienda.ar/checkout`** (lo pasó Santiago el 16/11; chequeado con `curl -sIL`: 200 y 0 redirecciones). Vive en **un solo lugar**, el `CONFIG.CHECKOUT`.
- **Precio puesto: US$ 9,99 (antes US$ 29,99), pago único.** ⚠️ **Lo elegí yo**, siguiendo el piso de [[energia-vital]] para LATAM neutro — el original corre AR$ 14.999 / AR$ 19.990. Vive en **un solo lugar** del `CONFIG`, así que cambiarlo es una línea.

## La plataforma: un quiz NATIVO del builder de ImpulTienda
Este no es un `custom_html` como los otros: es el **motor propio de ImpulTienda** (*engine v2 — block-based screens*). El quiz entero viaja **sin cifrar** en un `<script id="quiz-data" type="application/json">` con `spec.steps`, `theme`, `checkoutBase` y las claves de su Supabase. El CSS está entero en `/_astro/q-home.*.css` y el motor en un `<script>` inline de ~39 KB. Detalle del método en [[quizzes-reglas-de-armado]] §3.

**Qué hace el motor que conviene saber:**
- Cada pantalla es una **pila de bloques** (`text`, `options`, `multi`, `image`, `html`, `button`, `gauge`, `chart`, `benefits`, `checklist`, `testimonial`, `faq`, `banner`, `timer`, `loading`, `field`).
- **Las ramas se resuelven por puntaje**, no por salto: una pantalla con `outcome:{min,max}` solo se muestra si el puntaje acumulado cae en su banda, y `go()` saltea las que no matchean en la dirección del viaje.
- `*palabra*` en cualquier texto se pinta con el color de acento; `{name}` se reemplaza por el nombre capturado.
- El CTA navega **por JS** (`location.href = checkoutHref()`), no por `href`: arrastra solo los UTMs y los click id guardados en `sessionStorage.impultienda_utm`.

## Los 36 pasos (y el A/B que traía escondido)
El original corre **un A/B de embudo**, no de copy. La portada tiene **dos bloques de opciones de edad superpuestos**: el segundo da `score 1000000` y el CSS muestra uno u otro según `html[data-abvsl]`, que se sortea 50/50 en `localStorage`.

- **Carril A (pasos 0-29): el quiz largo.** Portada de edad → género → prueba social → 5 síntomas → placa del nervio vago → 3 frases de identificación → 2 de impacto emocional → placa de modo alerta → antigüedad → cafeína → sueño (multi) → cambios en el cuerpo (multi) → estresores (multi, con caja de empatía) → qué mejorar (multi) → para qué → tiempo por día → placa de la calma → compromiso → nombre y mail → carga de 6 s → **uno de 3 resultados** por puntaje (leve 0-45 · media 46-85 · alta 86+), cada uno con su gauge, su curva de previsión y la oferta entera.
- **Carril B (pasos 30-35): quiz corto de 5 preguntas + VSL.** Las mismas preguntas condensadas y un resultado con el video vertical de su presentadora, con la oferta **oculta hasta el segundo 216,6** del video.

**En nuestra versión el carril B quedó apagado** (`AB_VSL: false`) porque el VSL es de ellos y no tenemos uno propio. **No se borró nada**: está entero en el archivo y se enciende poniendo `AB_VSL: true` + `VSL_MP4`.

## Lo que se sacó del original (su stack, no se copia)
- **Su analítica de Whop** (`t.whop.tw`, `biz_JG4IGhy9TH9ZyY`).
- **Su A/B de precio**, que lee el precio real haciendo `fetch('/checkout/e-quiz-19990')` y lo reescribe en el DOM.
- **Sus claves de Supabase** (`supabaseUrl` / `supabaseKey`): quedaron vacías, así que el motor no guarda una sola respuesta en su base.
- **Sus targets de checkout por banda** (`e-quiz-19990`, `d-vsl-19990`): los 4 CTAs van a `CONFIG.CHECKOUT`, uno solo.
- **El nombre de su presentadora** (Patricia Vega) → `CONFIG.VSL_EXPERTA`.

## El pase a neutro (59 reemplazos, verificados)
Se hacen **con script**, nunca a mano: `OUTPUTS/scripts-quiz/build_nervio_vago_latam.py`. Cada par tiene que matchear o el script aborta.

- **Voseo → tuteo neutro:** *identificás→identificas, te levantás→te levantas, sentís→sientes, podés→puedes, querés→quieres, te comprometés→te comprometes, Elegí→Elige, Contestá→Responde, Dejanos→Déjanos, Pagás→Pagas, dormís→duermes, descansás→descansas, Dejás→Dejas*. Verificado contando formas: **cero** palabras en `-ás/-és/-ís` que sean verbo (quedan solo *más, demás, después, estrés, estás*, que son iguales en tuteo).
- **Léxico argentino → LATAM:** *laburo→trabajo · plata→dinero · chicos→niños · panza→estómago/barriga · mail→correo · pavada→tontería · Chau→Adiós · marido→esposo · caída de pelo→caída del cabello · "te saltás con los demás"→"les contestas mal a los demás"*.
- **La cafeína:** *"¿Cuánto mate o café tomás por día?"* → *"¿Cuánto café o té tomas por día?"*, y las opciones con emoji distinto cada una (☕ 🍵 🥛 🙅), porque sacar el mate dejaba dos ☕ en el mismo paso.
- **Prueba social:** *"+12.400 argentinas"* → *"+12.400 mujeres de Latinoamérica"*. El número es el de ellos, no se inventa.
- **Testimonios al mercado destino:** Rosario → **Guadalajara**, CABA → **Bogotá**, Córdoba → **Lima**, Silvina → **Silvana**.

## Las imágenes: las mismas, con dos recortes y una corrección
Las 10 son las del original. Ninguna tenía marca ni texto quemado, así que **no se generó ni una**. Lo que sí hubo que tocar:

1. **Las 4 fotos de edad no mostraban la cara.** Las opciones con foto se renderizan a **`height:120px` con `object-fit:cover`**, así que de un cuerpo entero de 600×800 solo se veía la **franja central** (de los hombros a las rodillas): cuatro pares de calzas lila idénticas y el rango de edad ilegible. Recortadas a la cara (380×285, centro vertical 0,28) se distingue de una la de 25 de la de 55. Es la regla de [[dancego]] del 4/11.
2. **El mate, dos veces.** El mockup del celular tenía un **mate con yerba** ocupando medio cuadro, y la foto de "modo alerta" otro al lado de la notebook. Los dos se fueron **recortando**, sin generar nada: el mockup quedó `(0,0,686,457)` —el teléfono ahora llena el encuadre— y modo alerta `(250,0,960,710)`, que de paso mejoró, porque la cara y la mano en el cuello quedan grandes.
3. **El logo quedó igual.** *Reseteo Nervio Vago* es descriptivo, sin país ni marca personal.

## El gauge estaba invertido (y se arregló)
La métrica es **"Desregulación del nervio vago"**: cuanto más alto, **peor**. El gradiente del motor viene `rojo → ámbar → verde` de izquierda a derecha (sirve para métricas donde más es mejor), así que pintaba de **verde la banda "Alto"** justo al lado del cartel *"Desregulación alta — con el tiempo esto sube la inflamación y la presión"*. Se invierte con **una línea de CSS** (`verde → ámbar → rojo`). Es la regla fija de [[quizzes-reglas-de-armado]] §4b: el verde solo significa "bien" y el rojo solo "riesgo".

## Los dos parches al motor
Su runtime se usa tal cual salvo **una función**, reemplazada desde el script de armado (con `assert` de que el bloque
viejo matchee exactamente una vez, así un cambio futuro de ImpulTienda hace fallar el build en vez de entregar algo roto):

- **`progressBar()`.** El motor cuenta las pantallas con `outcome` como **una sola** (asume que son los 3 resultados por
  puntaje). Acá el `outcome` lo llevan **35 de las 36** porque es el mecanismo del A/B, así que daba `total = 2` y la
  barra salía **llena desde la primera pregunta**. El reemplazo cuenta solo las **pantallas de pregunta del carril
  actual** (las que llevan `showProgress`, filtradas con su propio `gateMatches()`): 25 en el carril largo, de a 4 %.

Lo demás —render, pasos, bandas, checkout, pixel— es suyo sin tocar. El CSS también, salvo la línea que invierte el
gauge.

## Verificación (en el navegador, no leyendo el código)
En un `<iframe>` de 390 px servido por `http.server`, recorrido entero por código:
- **32 pantallas** del carril A, de la portada al checkout. Cero imágenes rotas, **cero desborde** (`scrollWidth - clientWidth = 0` en todos los pasos), cero elementos de más de 392 px, **cero errores de consola**.
- **Las 10 imágenes** pasan a Blob URL y quedan **decodificadas al arrancar** (10 de 10), con la red de seguridad que las devuelve a su data URI si la tienda bloqueara `blob:`.
- **Los 2 CTAs llegan a `https://resetnervio-vago.impultienda.ar/checkout`** arrastrando los 6 parámetros (`fbclid`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_id`). Probado sobre una **copia instrumentada**, porque el motor navega por JS y disparar los CTAs de verdad mandaría visitas de prueba a la tienda.
- **La barra de progreso avanza** `4% → 8% → … → 100%`, una pantalla a la vez, y no aparece en la portada, las cargas ni el resultado.
- **Arranca siempre en la portada**: este motor no guarda el paso en `localStorage`, así que no tiene el bug del 14/11 de [[gluteo-despierto]].
- El contador de la oferta arranca en **10:00**, no heredado.

## Entregables
- `~/Desktop/nervio-vago-latam/landing/nervio-vago-quiz.txt` — **632 KB**, autocontenido, para pegar en el `custom_html`.
- `~/Desktop/nervio-vago-latam/landing/PRUEBA.html` — el mismo, para abrir en Chrome.
- `~/Desktop/nervio-vago-latam/landing/spec-latam.json` — el spec solo, por si el builder de ImpulTienda lo importa.
- `~/Desktop/nervio-vago-latam/imagenes/` — las 10 webp (253 KB en total).
- Copia en `OUTPUTS/2026-11-16-quiz-nervio-vago-latam.html` · script en `OUTPUTS/scripts-quiz/build_nervio_vago_latam.py`.

## Preguntas abiertas
- **El precio.** Puse US$ 9,99 / US$ 29,99 por el piso de LATAM neutro. ¿Va ese o otro?
- **El VSL del carril B.** Si se graba uno propio, se enciende con `AB_VSL: true`.
- **El copy está todo en femenino** aunque el quiz pregunte Mujer/Hombre. Es así en el original y se respetó; si se quiere concordancia, va el token `{{o}}` de [[monjaro-violeta]].
- Faltan los anuncios y el producto real.

## Relacionado
[[quizzes-reglas-de-armado]] · [[gluteo-despierto]] · [[dancego]] · [[energia-vital]] · [[internacionalizacion]]

## Fuentes
- `https://nervio-vago.impultienda.ar/` (bajado con `curl -sL` el 2026-11-16)
- Pedido de Santiago del 2026-11-16
