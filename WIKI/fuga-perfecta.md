# Fuga Perfecta

> Juegos de escape para imprimir y jugar en casa (PDF, AR). Clon de **casocriminal.shop** con ángulo ampliado: no solo pareja, también **familias y grupos de amigos**. Arrancó el 24/11/2026. (fuente: doc de la oferta de Santiago + 22 ads despiezados de los dos competidores)

## Ideas clave

- **El competidor no es otro juego: es salir.** Todo el mensaje se construye contra la noche de "¿qué hacemos?" que termina en Netflix.
- **El 4x1:** 3 salas completas (El Vagón, La Cabaña, El Búnker) + 7 desafíos express. Precio $19.990, tachado $59.990, garantía de 30 días reales (la de Caso Criminal son 7 días que se anulan al descargar).
- **El mecanismo que vende:** cada etapa da un número y ese número abre el sobre siguiente. Si te equivocás, no abre. Convierte un mazo de papeles en una cadena y hace imposible hacer trampa.
- **El traidor es nuestro ángulo exclusivo.** En El Búnker va un sobre extra por jugador; en uno dice "tu trabajo es que no salgan, y que no se note". Caso Criminal no puede hacerlo porque el escape cooperativo no tiene a nadie acusando a nadie.
- **Order bump:** El Kit del Escapista (+$5.900): candados de papel, cronómetro para imprimir, pulseras de equipo, certificado de escape. No vende más contenido, vende que la noche se sienta real.

## Los dos competidores, medidos

Bajados y despiezados el 24/11: **10 ads de casocriminal.shop** (88 activos) y **12 de atwistofdate.co.uk** (54 activos).

- **Un solo copy para toda la cuenta.** Los ~54 de Twist corren el mismo texto de 5 líneas con emojis; los 88 de Caso Criminal lo mismo. **No varían el texto: varían el video.**
- ⛔ La biblioteca los sirve a **360x640**: valen como molde de edición, nunca como b-roll ([[guiones-y-anuncios]], regla del 18/11).

### Molde A · el corto (7 a 16 s), SIN voz
- Música viral de fondo, con vocal en inglés ("I'll Be There for You" de Friends aparece dos veces, "Way Down We Go", pop/R&B de TikTok).
- **Una sola placa POV arriba**, fija todo el video: caja blanca con texto negro, o caja negra translúcida con texto blanco. Ejemplos: *"POV: Encontráis un plan en pareja que no consiste en salir a cenar ni ver una serie"*, *"No necesitas tablero: lo imprimes y empiezas"*, *"Netflix is cool but what if we solved an escape room?"*.
- **Banner de oferta abajo**, fijo todo el video: *"OFERTA SOLO HOY · 4×1 EN JUEGOS DE INVESTIGACIÓN"*.
- Un encuadre picado fijo sobre la mesa con **jump cuts de ~1 s** (timelapse de la noche), o 8-9 planos de detalle de 1 s.
- 🎬 **El mejor recurso que tienen:** el cronómetro proyectado en la pared del fondo, que va de 59:58 a 00:20 mientras la pareja juega. Cuenta la historia entera sin una palabra.

### Molde B · el largo (20 a 35 s), CON voz en off
- **Voz femenina joven (25-30), entusiasta, ritmo rápido, tono de amiga que te recomienda algo.** Británica en Twist, española en Caso Criminal.
- **13 a 22 cortes, promedio de 1,1 a 2,2 s** por plano. Más rápido todavía que nuestro estándar de 1,9-2,9.
- Placa de hook arriba los primeros 2-3 s y después se va. **Subtítulos dinámicos palabra por palabra** en el centro.
- Cama musical de pop acústico instrumental por debajo. Algún SFX puntual: high-five, risas, papel.
- **Cierre sin placa, sin logo y sin botón**: termina en la pareja celebrando o en un pulgar arriba.
- Estructura: dolor concreto → "probá esto" → qué es (se descarga e imprime al instante) → qué trae (enumerado y concreto) → cómo se siente → cuánto dura → cierre.
- Hay un **formato listicle** que vale copiar: *"Cheap date ideas that DON'T involve food"* → 1, 2, 3 con precio y duración de cada uno en placa.

## La tanda 1 (24/11/2026) — 10 creativos

Guiones en `OUTPUTS/2026-11-24-guiones-fuga-perfecta-tanda1.md`, despiece de la produccion en
`OUTPUTS/2026-11-24-fuga-perfecta-tanda1-produccion.md`. **7 del molde B (voz) y 3 del molde A (sin voz)**,
repartidos entre pareja, amigos, familia y grupo.

| # | Formato | Angulo | Publico | Dur. |
|---|---|---|---|---|
| 1 | Voz | Contra Netflix (el que mas corren) | Pareja | 31,8 s |
| 2 | Voz | **El traidor**, nuestro angulo exclusivo | Amigos | 26,3 s |
| 3 | Voz · listicle con placas numeradas | Las 3 salas, una por una | Grupo | 28,3 s |
| 4 | Voz | Sin pantallas en la sobremesa | Familia | 26,0 s |
| 5 | Voz | Reaccion de un tercero | Amigos | 25,1 s |
| 6 | Voz · comparacion | Las cuentas contra una sala fisica | Grupo | 25,3 s |
| 7 | Voz | La objecion ("pense que era una boludez") | Pareja | 25,1 s |
| 8 | Sin voz · POV | Contra Netflix, el vagon | Pareja | 12,0 s |
| 9 | Sin voz · POV | No necesitas tablero | Todos | 10,0 s |
| 10 | Sin voz · POV, caja negra | Una hora sin celular | Familia | 14,0 s |

- **Editores:** `OUTPUTS/scripts-vsl/edit_fuga.py` (molde largo, clon de `edit_alivio.py` con caja de hook
  blanca, banner de oferta fijo abajo y paleta de lacre) y `edit_fuga_pov.py` (molde corto sin voz).
- **Voz:** Sulafat a `speed 1.20` con `gemini-2.5-flash-preview-tts` y **un solo bloque de estilo**,
  `voz/style.txt` (amiga portena contandole un plan que le encanto, ritmo normal de conversacion). Las
  siete entre **167 y 188 ppm**: ninguna leyo el bloque de estilo. La primera tanda habia salido con dos
  estilos distintos y se oia (correccion de Santiago del 24/11: *"quiero que todos tengan la voz de el
  video que arranca Si las noches"*); los 2 a 7 se rehicieron con el estilo del 1.
- **Musica:** sale **del audio de sus propios anuncios**, no de un generador (correccion de Santiago del
  24/11: *"pusiste cualquier musica, es una verga"*), y va de **corrida continua, nunca en bucle**
  (segunda correccion: *"se repite la misma parte todo el video, la idea es que dejes correr esa cancion"*).
  Los 7 con voz llevan **"Daydream" del Gunter Kallmann Choir**, que es el tema que Caso Criminal usa en
  `caso-05`: identificado con huella acustica, confirmado midiendo (cruce de cromas **0,981**, y el ad
  arranca en el **segundo 3,97** del tema, a velocidad normal), y bajado entero de archive.org (3:20).
  Los 7 arrancan en ese mismo segundo 3,97 y dejan correr el tema: sin bucle y sin cortes.
  `scripts-vsl/cama3.py` con `CAMA_CRUDA=1` (el arreglo de agudos es solo para pistas arrancadas de un ad).
  El camino de los stems (`scripts-vsl/stems.py`, demucs sobre sus ads largos) sirvio para descartar que
  el tema estuviera mas largo en otro ad suyo: de los 198 que tienen, ninguno lo tiene. Los 3 sin voz llevan `caso-01` (pop indie con vocal femenina, 15,6 s) al
  frente, que ya daba de sobra para 10-14 s. Todo se levanta en agudos porque la Biblioteca sirve el audio
  en HE-AAC a 48 kbps. `cama2.py` (el que repetia la pista) queda obsoleto.
- **Visuales: 21 clips, 32 encuadres, 94 ventanas.** Las 8 que paso Santiago (el producto) mas **12
  generados con `seedance_2_0_mini` en Higgsfield** (8 creditos cada uno, 8 s a 720x1280, el mismo formato
  que los suyos): la pareja aburrida con el control, los cuatro amigos sobre el mapa, la familia en la
  mesa, el grupo festejando, el pinboard con hilos, el cenital de manos, el celular contra los libros.
  **Cada video tiene su pool:** el producto siempre, mas el b-roll del publico de ese angulo.
- **Entrega:** `Ebook Dami / Ebook Fuga Perfecta (AR) / Videos terminados`, masters en
  `~/Desktop/Fuga Perfecta/anuncios/` como `24-11 - N.mp4`.

## Detalles / notas

- ⛔ **El b-roll de esta oferta no se espeja.** El editor da vuelta un plano cuando lo repite; con estos
  clips eso escribia *"ANABAC AL"* por *"LA CABANA"* y daba vuelta "ETAPA 5" y los numeros del cronometro.
  Todos los encuadres van con **`"flip": false`**. Se ve recien en la hoja del render.
- 🐞 **Dos de los clips IA tienen texto mal escrito.** El de los 7 desafíos dice *"DESAFÃO EXPRESS"* (tilde rota). Se arregla reencuadrando (`zoom 1.55`, `ybias 1.0`), no se tira el clip.
- ⛔ **tikwm estuvo caído el 24/11** (502 sostenido durante media hora). **yt-dlp no es reemplazo**: la última versión que corre en el Python 3.9 del sistema es `2025.10.14` y ya no extrae TikTok. Pasar `--cookies-from-browser` no está permitido. Las páginas de video de TikTok sirven el stream por **blob/MSE**, así que tampoco se baja desde el navegador. **Si tikwm se cae, por ahora no hay plan B: se espera.**
- ⛔ **TikTok no sirvio para esta oferta: 407 ids, 155 clips bajados, 0 utiles.** El nicho en TikTok son
  caras hablando a camara, Monopoly, juegos de vasos y texto quemado en todos los cuadros. Los 4 que
  pasaron el filtro de 6 cuadros se cayeron al mirarlos a 1 cuadro por segundo. **Lo que falta para variar
  visuales es generar b-roll nuevo con IA**, del mismo estilo que las 8 que ya hay.
- ✅ **Las páginas de tag de TikTok sí se raspan** (confirma la regla del 16/11). Rindieron: `familygamenight` (83), `familygamesnight` (87), `murdermysteryparty` (100), `escaperoomathome` (77), `gamenightwithfriends` (66), `juegosdemesa` (30). **No rindieron:** `gamenight` (página no disponible, el tag está ocupado por videojuegos) ni `boardgamenight`/`escaperoom`/`datenightathome` (la SPA no cargó). Total: **407 IDs únicos**.
- Los despieces completos quedaron en el scratchpad de la sesión del 24/11.

## Dónde están las visuales (25/11/2026)

Despiece completo con todos los links en `OUTPUTS/2026-11-25-visuales-fuga-perfecta.md`.

- **Las 8 de Flow (el producto)** → Drive, carpeta nueva **Ebook Fuga Perfecta (AR) / Contenido**
  (`1yYTu6sMN7kFUj5KSYS3C7CI82nqkvHQo`), numeradas 01 a 08 por lo que muestra cada una.
- **Los 13 de Higgsfield (`seedance_2_0_mini`, el b-roll de gente)** van en la misma carpeta con
  prefijo **IA**, para que se distingan de los del cliente de un vistazo. Santiago los pidió en el Drive
  igual que los suyos: **las visuales de una oferta van completas a su carpeta, las del cliente y las
  generadas.** Los links directos de CloudFront quedan en el OUTPUT.
- **Copia local durable:** `~/Desktop/Fuga Perfecta/visuales/flow/` y `.../visuales/ia/`. Antes vivían
  solo en el scratchpad de la sesión del 24/11, que se borra solo: **el b-roll de una oferta se copia a
  su carpeta del Desktop el mismo día, no se deja en el scratchpad**.
- **TikTok no tiene nada que pasar acá:** 407 IDs, 155 clips, 0 útiles (ver más arriba).

## Renovaciones (25/11/2026): 3 variables del Guion 2

Pedido de Santiago: *"3 renovaciones, y quiero que sean todas variables del video que empieza como 'Es un
juego..'. Variables buenas, respetando estructura, ángulo y sentido"*. Guiones en
`OUTPUTS/2026-11-25-guiones-fuga-perfecta-renovaciones.md`.

| # | Hook | Formato del hook | Dur. |
|---|---|---|---|
| R1 | *Hay un sobre en este juego que no se abre delante de nadie* | la regla secreta | 30,1 s |
| R2 | *Esta noche uno de tus amigos te va a mentir en la cara, y lo vas a invitar vos* | acusación en segunda persona | 26,1 s |
| R3 | *Terminamos el juego y seguíamos discutiendo quién nos había estado frenando* | storytime / lo de después | 28,6 s |

- **El cuerpo no se toca** ([[renovacion-de-creativos]]): sobre a solas → en uno dice lo contrario → que
  nadie salga y que no se note → mentir con los números, la etapa equivocada, perder tiempo → se descubre
  cuando el reloj llega a cero → lo imprimís hoy y lo jugás esta noche.
- **El `usage` es COMPARTIDO entre las tres** (`usage_ren.json`), no uno por video. Así el repartidor de
  planos evita lo que ya usó la anterior y las tres salen con b-roll distinto: es la respuesta directa a
  la corrección del 24/11 (*"usás en todos las mismas visuales"*). Con un usage por video el pool arranca
  de cero cada vez y los tres eligen lo mismo.
- **Voz:** Sulafat, `style.txt` de la tanda del 24/11, `speed 1.20`. ⚠️ **Las tres salieron de modelos
  distintos porque la cuota diaria se agotó en medio**: R1 con `gemini-2.5-flash-preview-tts`, R2 con
  `gemini-3.1-flash-tts-preview` y R3 con `gemini-3.8-flash-tts` (que lee el style en voz alta: se cortó
  el wav en el segundo 18,22, donde arranca la primera palabra del guion). Medido antes de aceptarlas:
  F0 de 200, 210 y 218 Hz, una dispersión **menor que la que ya tenía la tanda del 24/11** entre sus
  propios videos (184 a 195 Hz), así que no se oye el cambio de modelo.
- **Música:** la misma de la tanda, "Daydream" del Gunter Kallmann Choir, corrida continua desde el
  segundo 3,97, `CAMA_CRUDA=1`. Medida contra el habla: **−14,0 / −13,8 / −13,6 dB**, en la referencia
  de −13 dB que aprobó.
- ⛔ **El recorte `v3z@0.1` se cayó del pool.** Es el zoom 1,7 sobre el arranque de la carta de madera:
  textura crema desenfocada donde no se lee nada, y en el primer R2 ocupaba casi 3 s seguidos. Se vio en
  la hoja del render, no en el pool.
- Scripts: `OUTPUTS/scripts-vsl/gen_fuga_ren.py` (clona `plan2.json` y le cambia voz, hook, anclas y
  semilla) y el mismo `edit_fuga.py`, que **se parcheó para leer los efectos de `~/SFX/alias`** en vez de
  llamar a `sfx.py` ([[efectos-de-sonido]]); esta tanda no lleva ninguno, igual que la del 24/11.
- **Entrega:** `Ebook Fuga Perfecta (AR) / Videos terminados`, másters en
  `~/Desktop/Fuga Perfecta/anuncios/` como `25-11 - R1.mp4` a `R3.mp4`.

## Preguntas abiertas

- ¿El contador de la landing va de 10 minutos (nuestra regla fija) o largo como el de ellos, que usan más de 12 horas?
- ¿Se mantiene el precio $5.000 abajo de Caso Criminal, o sube? (el criterio de Santiago es que el precio sube y no baja)
- Faltan: escribir las tres salas, el logo y la galería de jugadores de la landing.

## Relacionado

[[guiones-y-anuncios]] · [[como-trabajar-con-santiago]] · [[estilo-de-video-ia]] · [[noche-de-citas-cristiana]] · [[funnel-hacking]] · [[modelo-low-ticket]]

## Fuentes

- Doc de la oferta: *FUGA PERFECTA — Documento de la oferta* (Google Docs, 24/11/2026)
- Biblioteca de anuncios de Meta: `atwistofdate.co.uk` y `casocriminal.shop` (24/11/2026)
- OUTPUTS/2026-11-24-guiones-fuga-perfecta-tanda1.md

## Los estaticos (25/11/2026)

Caso Criminal corre **3 anuncios de imagen** (todos pausados hoy; sus 88 activos son video) y A Twist Of
Date **ninguno**. Los tres son la misma receta: fondo hueso, **cintas de peligro negras y amarillas con el
nombre de la marca** cruzando arriba y abajo, pildora amarilla con el gancho, **titular condensado gigante**,
los tres folders kraft con papeles asomando, un badge "4X1" (en lupa o redondo), un sello rojo de urgencia y
la pildora blanca de prueba social con tres caritas y el tilde azul. Cambian solo el titular y donde va cada
badge.

El socio de Santiago ya hizo dos: una version oscura del molde de la lupa y una foto de living de noche.
Las dos nuestras salen de **los otros dos moldes**, los que el socio no uso:
- **`Ultimas horas - contador 4x1.png`** — molde del contador: pildora "3 SALAS + 7 DESAFIOS AL PRECIO DE 1",
  titular "ULTIMAS HORAS", caja negra con "01:20:17", lupa con el 4X1, prueba social abajo.
- **`Promo 4x1 - el plan que tu noche necesita.png`** — molde crema: prueba social arriba, pildora
  "EL PLAN QUE TU NOCHE NECESITA", titular "PROMO 4X1", badge redondo 4X1 abajo a la izquierda y sello rojo
  "LA OFERTA TERMINA HOY" abajo a la derecha.

Producto adaptado: **tres sobres de papel madera cerrados con lacre rojo**, rotulados CONFIDENCIAL +
EL VAGON / LA CABAÑA / EL BUNKER, con el plano del vagon, la lista de pasajeros (nombres y ciudades
argentinas) y la hoja del cronometro asomando.

- **Como se hicieron:** `gpt_image_2` en Higgsfield con el estatico de ellos como **imagen de referencia**
  y la orden de conservar la grilla y cambiar solo marca, producto y textos. Dos pasadas: la primera a
  `1k/medium` (1,25 creditos) para validar la composicion, la segunda a `2k/high` (7 creditos) corrigiendo
  la ortografia. 1520x2688, exportadas a 1080x1920.
- ⚠️ **La Ñ no la escribe.** Tres pasadas seguidas escribieron "LA CABANA". Se resolvio **dibujando la tilde
  por codigo**: se resta la N de la Ñ en BarlowCondensed-ExtraBold para sacar el glifo de la tilde, se escala
  al ancho de la N real (proporcion 18/27) y se estampa con el color de tinta medido sobre el propio trazo.
- Los modelos de imagen de Gemini (nano banana incluido) tienen **cuota 0** en esta API key: no son opcion.
