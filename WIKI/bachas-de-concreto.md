# Bachas de concreto (oferta en inglés)

> Clon para EE.UU. del curso argentino "De Cemento a Negocio" (página "Martin Ferreyra" en Meta, ~79 anuncios activos en octubre de 2026). Se traducen sus mejores ads y se editan sobre B-roll de TikToks de terceros, porque sus visuales tienen marca de agua. (fuente: pedido de Santiago del 2026-10-18)

## Ideas clave
- **Producto:** curso para fabricar bachas (lavatorios) de concreto fino desde cero y venderlas. Materiales, mezclas, moldes caseros, acabado premium, cómo presentarlas y venderlas.
- **Competidor:** biblioteca de Meta, page id `748547031665721`. Todos sus ads son **voz en off de 60 a 108 s** sobre video de fabricación, con CTA "Hacé clic en Más información".
- **Sus 3 ADN ganadores** (los más viejos que siguen activos, ordenados por antigüedad):
  1. **"Hoy genero más de 1.200.000 por mes con algo que solo quería probar"** (desde el 3/10, el más viejo). Primera bacha → "¿la vendés?" → pedidos → no empecé siendo experto.
  2. **"Lo que empezó como un momento para desconectarme terminó siendo mi trabajo"** (6 variantes del 7 al 9/10). Foto en Instagram → "¿Dónde la compraste? ¿Cuánto sale?" → primer pedido → otro → hoy me dedico a esto.
  3. **"Más de 700 mil en una semana fabricando bachas. ¿Te imaginás?"** (6 variantes del 7 al 9/10). Objeción (experiencia, herramientas caras) → qué aprendés (materiales, acabado premium, moldes sin gastar una fortuna) → CTA.
- En los ads nuevos (del 12 al 16/10) usa el nombre del método y testimonios de "700 mil por semana". Los más viejos no nombran el producto.

## Cómo se arma un video
1. **Descargar sus ads:** el CSP de Facebook bloquea mandarlos a un servidor local. Lo que anda es bajar todos los `<video>` desde la página con `fetch`, concatenarlos en un único Blob y una sola descarga (`fb_ads_concat.bin`), y después partirlo por tamaños en Python. Se transcriben con faster-whisper (modelo `base` alcanza para leer el guion), empezando por los más viejos.
2. **Visuales:** TikToks que pasa Santiago, bajados con `yt-dlp` (instalado con `pip install --user`). TikTok falla seguido, así que se reintenta en loop. Salen sin marca de agua.
3. **Voz: Google AI Studio → Generate speech** (Gemini 3.8 Flash TTS, gratis y sin créditos). **Voz de hombre de unos 40: Knox** (Masculine, "warm and conversational", tono grave), con el estilo: *"American man around 40, a hands-on craftsman telling his own story on TikTok. Warm, genuine, confident and conversational, a little excited, brisk natural pace, no announcer tone."* El texto se pega en el bloque, se genera con **cmd+Enter** (Run queda bloqueado mientras suena el audio anterior: primero hay que pausarlo) y se baja con el ícono de descarga (`Generated Audio ….wav`). Ojo: si el menú de Style queda abierto, lo que tipeás no entra en el bloque de texto. "Roma" no existe en AI Studio (es de ElevenLabs y HeyGen).
4. **Edición:** `OUTPUTS/scripts-vsl/edit_broll.py plan.json salida.mp4` en modo **pool**:
   - Hay 40 recortes de los 7 TikToks, sin tramos con blur. El 2026-10-19 se sumaron 4 TikToks de @tunegocioenconcreto (`7555698286653443384` bacha roja colada, `7509688033600572728` bacha blanca lijada, `7555149079676718392` bacha moldeada sobre la base, `7527454540250074424` mesa de GRC con agua que perla), y ahora son ~70 recortes. Del 7555149079676718392 hay que excluir los frascos con marca (16–18 s) y el molde blanco casi vacío (8–10 s). El colado rojo va una sola vez por video, porque todos sus tramos se ven iguales.
   - **Anchors** (`"anchors": [[palabra, aparición, clave, segundo]]`): el plano que suena con esa palabra muestra lo que dice ("pouring" → colado, "Mixing" → balde, "mold" → bacha desmoldada). El CTA ("Learn") va siempre sobre una bacha terminada.
   - Ningún recorte se repite dentro de un video, nunca van dos planos seguidos del mismo TikTok y aparecen los 7.
   - Entre videos se priorizan los recortes menos usados (`usage.json` compartido): se editan en orden y con el mismo `usage.json`. Si un recorte se reusa, va espejado.
   - Voz sin silencios a 1.2x, un corte cada ~4–5 s (al final de una palabra), zoom suave, subtítulos de 3 palabras con la activa en amarillo y música baja.
   - **Efectos puntuales, no en cada corte:** cha-ching cuando nombra la plata ("dollars", "income", "pays"), ding en un momento clave (el primer pedido, "I'm Mark Ross"), pop en "Learn More" y un solo whoosh en el primer corte.
   - Antes de entregar: pasar `blurdetect` de ffmpeg por los videos y por los clips nuevos, porque los TikToks traen transiciones con blur.
5. **Entrega:** `~/Desktop/bachas-concreto/` con los videos y `guiones-videos.md`.

## Detalles / notas
- **Experto: Mark Ross.** Se lo puede nombrar cuando suma: "Mark Ross's method" en los testimonios, y "I'm Mark Ross" cuando habla el experto (guion C).
- **Visuales a cuidar:**
  - `@modina.concreto/7639408597457210644` tiene un cartel con el nombre y el teléfono arriba. Se usa con zoom 1.9 recortado abajo.
  - `@modina.concreto/7671339958967225618` tiene transiciones con blur en 3,3–4,5 s, 13,6–13,9 s y 16,9–17,2 s. Hay que excluirlas.
  - `@concepto.cemento/7389081667157150982` muestra la interfaz de la cámara desde los 8 s.
  - `@tunegocioenconcreto/7458959238283513094` muestra etiquetas en español (Bulimix, "Polímero") entre los 19 y los 22 s.
- **Adaptación a EE.UU.:** los pesos pasan a dólares creíbles ($3,000 por mes y $1,200 por semana), sin nombre de experto ni de producto, con CTA "Tap Learn More".
- **Largo:** se respetó el largo del competidor (45 a 76 s editados), no el máximo de 30 s de [[guiones-y-anuncios]], porque el pedido fue traducir sus ganadores.

## Activos
- Videos del 2026-10-18: `BC-A-hoy-gano-3000.mp4` (57 s), `BC-B-momento-para-mi.mp4` (71 s) y `BC-C-1200-en-una-semana.mp4` (42 s), rehechos con voz de hombre (Knox).
- Guiones en inglés y español: `OUTPUTS/2026-10-18-guiones-bachas-concreto-en.md`.
- Variables A2, B2 y C2 (mismo ángulo, guion nuevo): `OUTPUTS/2026-10-18-variables-bachas-concreto-en.md`. Videos `BC-A2-garaje-3200.mp4`, `BC-B2-mi-hora-en-el-garaje.mp4` y `BC-C2-400-a-800-por-bacha.mp4`.

- **Ganador (2026-10-19): Guion B** ("What started as a simple way to unwind…", `BC-B-momento-para-mi.mp4`), con 4 ventas. Su estructura: un rato para desconectar → probé de todo y no era habilidoso → video de bachas de diseño → "parecía difícil, pero era paso a paso" → método desde cero → primera pieza ("no podía creer que la hice yo") → la muestro sin querer vender → un tercero pregunta dónde la compré y cuánto sale → primer pedido, otro, otro → hoy me dedico a esto y lo sigo disfrutando → CTA con Mark Ross. Variables B3 a B7 (mismo ángulo, cada una con otro disparador, otro tercero que la ve y otro CTA): `OUTPUTS/2026-10-19-variables-bachas-B-what-started.md`.

- Videos del 2026-10-19 (variables del ganador B): `BC-B3-estres-y-vecino.mp4` (64 s) y `BC-B5-garaje-de-papa.mp4` (65 s), con B-roll nuevo y anchors.
- **Video UGC con Mark Ross (2026-10-19):** `~/Desktop/bachas-concreto/BC-UGC-Mark-Ross.mp4` (39 s).
  - Avatar de HeyGen "Mark Ross" (delantal, taller), Avatar IV, voz "Orson - Firm & Measured", Creación rápida en vertical 1080p. Salió de 50 s y costó 14 créditos.
  - Edición con `edit_vsl_quiz.py` (SPEED=1.1) alternando los 4 modos: pantalla dividida, B-roll solo, Mark grande recortado y Mark chiquito sin fondo. Tiene 18 B-rolls anclados a frases ("looking like this" → la bacha amarilla desmoldada; "the mix, the mold, the finish" → 3 cortes rápidos) y 4 headlines verdes: FULL TIME INCOME con cha-ching, y FIRST ORDER, STEP BY STEP y TAP LEARN MORE con pop.
  - Carpeta de trabajo: `~/Desktop/bachas-concreto/work-mark/`. Ahí están `brolls/` con los 9 TikToks nombrados (roja, blanca, molde, mesa, amarilla, negra, oval, terrazo, azul), `plan_mark.json` y `heads_mark.json`.
  - Evitar en pip/gs los planos donde aparece otra persona a cámara (el de `azul` a los 6–14 s), porque quedan dos caras.
- Guion UGC para la avatar de HeyGen **"Mark Ross"** (ángulo del ganador B, en primera persona como creador del método, ~156 palabras ≈ 40 s): `OUTPUTS/2026-10-19-guion-ugc-mark-ross-bachas.md`.

## Preguntas abiertas
- ¿Nombre del producto en inglés, landing y precio?
- Faltan sus ganadores de imagen (si los tiene) y el texto principal en inglés.

## Registro de correcciones
- **2026-10-18 · Voz de hombre, no de mujer.** La primera tanda salió con Nika (femenina) y Santiago la rechazó: "la voz tiene que ser de un hombre, de unos 40 años". Regla: en esta oferta la voz siempre es masculina, de unos 40 (Knox). Además, el experto es **Mark Ross** y se lo puede nombrar si hace falta.

- **2026-10-18 · B-roll sin repetir y efectos con sentido.** Sobre la tanda con voz de hombre: "se repiten muchas veces los mismos brolls, usá más… no quiero que se repitan" y "se hace muy cansador el efecto de sonido de 'Swap' cada vez que pasa algo… podés usar el cha-ching cuando nombra la ganancia". Reglas:
  - En un video no se repite ningún recorte, se rotan todos los clips y nunca van dos planos seguidos del mismo clip.
  - Nada de whoosh en cada corte: los efectos van solo donde el guion los pide (cha-ching en la plata, ding en un momento clave, pop en el CTA).

## Relacionado
[[guiones-y-anuncios]] · [[patitas-felices]] · [[secreto-de-la-insulina]] · [[internacionalizacion]] · [[funnel-hacking]]

## Fuentes
- Biblioteca de anuncios de Meta, página "Martin Ferreyra" (consultada el 2026-10-18)
- TikToks de visuales que pasó Santiago (7, uno repetido)
