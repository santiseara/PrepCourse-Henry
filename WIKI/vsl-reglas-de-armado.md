# VSL: reglas de armado (checklist viva)

> Reglas y correcciones de Santiago para armar VSLs con avatar (después del quiz o en la landing). **Leer antes de escribir un guion de VSL o editar uno.** Cada corrección nueva se suma acá, con fecha. Contexto técnico de avatares y voces en [[ugc-y-video-generativo]]. Reglas del quiz en [[quizzes-reglas-de-armado]].

## 0. Pipeline rápido (regla de Santiago, 2026-10-15: "agilizar y hacer otras cosas mientras algo se procesa")
Nunca en serie. El orden para cualquier video con avatar (VSL, OTO o ad):
1. **Calcular el largo antes de escribir.** HeyGen (voz roma) habla a ~0,27 s por palabra y el recorte de silencios saca otro ~10%. Para **4–5 min editados: ~850 palabras**; para 30 s: ~110.
2. **Guion aprobado → HeyGen YA.** Creación rápida, clic en el textbox (con `find`) y pegar el guion entero con `document.execCommand('insertText', false, T)` por JS: es instantáneo y no se cuelga como el tipeo largo. Se envía con el botón "Generar script".
3. **Mientras HeyGen renderiza** (unos 45 s → 3 min y unos 4 min → 12–15 min):
   - B-rolls en Higgsfield: los prompts uno atrás del otro en una sola tanda, y mirar antes el historial. **El tipeo a veces no entra en el textarea** (y "Generate" relanza el prompt anterior): cargar cada prompt por JS con el setter nativo de `HTMLTextAreaElement` + evento `input`, y hacer clic en el botón "Generate" por JS. Así salen 4 en ~15 s;
   - placas (mk_gfx.py), `plan.json`, `heads.json`, `capmap.json` y `stickers.json`;
   - verificar con un script que todas las frases del plan existan en el guion (normalizado).
4. **Al bajarlo:** esperar a que termine el `.crdownload`, copiarlo y correr `edit_vsl_quiz.py` **en segundo plano**. Mientras edita: WIKI, changelog, guion del próximo.
5. **Precios en `heads.json`: anclarlos a las palabras de ANTES del número** ("para siempre, por", "te lo llevás por"). Whisper transcribe los montos en cifras ("14 .990") y la frase en palabras no aparece, así que se pierde el "cha-ching". En `capmap.json` sumar las variantes en cifras ("14 .990 pesos", "40 mil pesos").
6. Revisar con una hoja de contactos (1 cuadro cada 3 s) y un par de cuadros a resolución completa. Comprimir con crf 21 y maxrate 8M.
- **Formatos de edición disponibles** (`edit_vsl_quiz.py`, 5.º campo del plan): `split` (avatar arriba y placa o B-roll abajo), `full` (B-roll solo), `gs` (avatar grande recortada delante del B-roll) y `pip` (B-roll con la avatar chiquita en la esquina). En un VSL largo conviene alternar los cuatro.

## 0b. Voces con Google AI Studio (2026-10-19, pedido de Santiago: "usá google AI studio para las voces")
- ⛔ **Un ad de voz en off no gasta un solo crédito** (2026-10-22: "cuando hacemos de voz en off, no tenés que gastar créditos en NADA"). Ni la voz, ni imágenes, ni video generativo. Voz de AI Studio, B-roll de stock gratuito, planos de producto de los stills de la landing. Nada de Higgsfield ni ElevenLabs.
- La voz la genero **yo** manejando Chrome, nunca se le pide a Santiago que la genere.
- Página: `aistudio.google.com/generate-speech` → "Create new dialog". La extensión de Chrome necesita **permiso para el sitio** (sin eso no hay capturas ni clics; JS sí anda).
- **Modelo: Gemini 3.1 Flash TTS Preview.** Es gratis y deja generar varias veces. El Gemini 3.8 Flash TTS (el que viene por defecto) da **una sola** generación gratis y después pide una clave paga; Voice Design también es pago.
- Voz femenina cálida: **Sulafat** (Warm). Otras: Gacrux (Mature), Achernar (Soft). El selector de acento solo trae acentos del inglés: dejar Neutral y dirigir el acento con el **Scene** y la nota del director del hablante (porteña de 50 años, rioplatense, "sh" en ll/y, audio de WhatsApp a una amiga, sin tono de locutora).
- **Un guion por generación** (~40 s tarda unos 30–40 s). La generación de 1:49 de un tirón no se pudo bajar.
- **El botón Download no baja nada** (Chrome lo bloquea). El audio completo queda en `document.querySelector('audio').src` como data URI WAV: se manda por `fetch` POST a un receptor local (`recv2.py`, `127.0.0.1:8767`). La primera vez Chrome pide permiso de **red local** y Santiago lo tiene que aceptar.
- 🆕 **2026-10-23 · Con Gemini 3.1 Flash TTS Preview esto cambió:** el botón **Download sí baja el WAV** a `~/Downloads/Generated Audio <fecha> - <hora>.wav` (no hace falta receptor), y el `<audio>` del DOM ya no sirve (solo tiene un pitido de 0,04 s; el audio va por Web Audio). El acento se dirige desde **Audio Profile** y **Scene**; el selector *Accent* sigue siendo solo de inglés y el *Pace* por defecto lee lento: conviene **Natural**.
- 🆕 **2026-10-26 · El botón de descarga de AI Studio es chico y falla en silencio.** En la tanda de 365 Actividades el clic caía 20 px a la derecha del ícono y **no pasaba nada**: `ls -t ~/Downloads/*.wav` devolvía el WAV viejo de otra oferta y se colaron audios de Herrero de Finde en los guiones. Reglas: hacer zoom sobre la barra del player para ubicar el ícono exacto, y **verificar la fecha del archivo** (no solo el md5) antes de moverlo a `vo/`. Además, cuando se escribe el guion y se hace clic en Run en la misma tanda de acciones, el primer clic a veces no dispara: conviene verificar que cambió la duración del player antes de bajar.
- 🆕 **2026-10-29 · Después de escribir el guion por JS, el primer clic en Run no dispara.** En la tanda de [[solar-installer-pro]] pasó en 3 de los 6 guiones: se setea el textarea con el setter nativo, se hace clic en Run y **no pasa nada**; el segundo clic sí genera. La señal es mirar el player antes de bajar: si la **duración total sigue siendo la del audio anterior**, no se generó (y el botón Download baja el viejo sin avisar). Regla: después de cada Run, zoom sobre la barra del player y comparar la duración contra la de la generación anterior; si es la misma, clic en Run otra vez. Al final, pasar Whisper por los seis WAV y verificar que cada uno diga su guion.
- 🆕 **2026-10-26 · Varias generaciones por carga de página (Gemini 3.1 Flash TTS).** Ya no hace falta recargar entre guion y guion: se hace clic en el bloque, `cmd+a`, se escribe el guion nuevo y se vuelve a correr. **Disparar siempre con clic en el botón Run**: con `cmd+Return` hubo un caso (V4 de Chía 28D) en que no se disparó y el Download bajó el audio anterior con el mismo md5. Los 6 ads de la tanda salieron de una sola carga.
- 🆕 **2026-10-23 · Confirmar cada generación antes de bajarla.** Enviar con clic en el textarea + `cmd+Return` (el clic en Run no dispara si el audio anterior está sonando), captura a los 6 s para ver el botón **Stop**, y después comparar **md5 y duración** con el archivo anterior. Si no, el Download vuelve a bajar el audio de antes sin ningún aviso: en la tanda de pilates salieron tres pares de archivos idénticos. Al final, pasar Whisper por los WAV y verificar que cada uno diga su guion.

## 0c. Voz propia en AI Studio + lipsync en HeyGen (2026-10-25, Protocolo Chía 28D)
Cuando la voz de HeyGen no gusta, la voz se hace en **Google AI Studio** (gratis) y HeyGen solo pone la cara: en *Escena única* → "subir/grabar" → **Subir audio** el avatar sincroniza los labios con el WAV/MP3 que uno sube (hasta 100 MB). El costo es el mismo que por texto: **~56 créditos cada 3:30 de video con Avatar IV**.
- **Límite nuevo de AI Studio (Gemini 3.1 Flash TTS): una sola generación por carga de página.** Después el botón Run queda con `aria-disabled="true"` y no se destraba con nada: hay que **recargar la página y volver a configurar** (escena, Audio Profile, Pace, voz). Por eso conviene partir el guion en **bloques de 550–600 palabras (~3:30 de audio)**, no en trozos chicos: un VSL de 2.950 palabras sale en 5 recargas.
- El botón **Download baja el audio anterior** si la generación todavía no terminó. Hay que esperar a que el botón Stop desaparezca y **comparar el md5** del archivo nuevo contra el anterior. Si es igual, no se generó.
- **Subida a HeyGen:** el `file_upload` del navegador tiene tope de 10 MB, así que los bloques van en **MP3 192k** (~4 MB) en vez de WAV (~10 MB). Después del upload hay que **esperar ~20 s** a que aparezca solo el cartel "Confirmar Audio" y recién ahí tocar "Agregar audio": si uno toca antes, el clic cae en la lista y elige otro archivo.
- Como el MP3 es solo para el lipsync, al final **se reemplaza el audio del video por el WAV original** (misma duración, calce exacto).
- **Revisión de la voz (obligatoria):** `OUTPUTS/scripts-vsl/revisar_voz.py audio.wav guion.txt` compara palabra por palabra contra el guion y marca lo que falta, lo que sobra, las palabras estiradas (>1,1 s) y los huecos (>1,3 s). Los números transcriptos como dígitos ("28", "140") y cosas como "quema grasa"→"que magrasa" son ruido del transcriptor, no errores. Lo que sí hay que revisar a mano con el modelo **medium** es cualquier palabra cambiada: así se encontró que un bloque se comía "hambre" y otro leía mal "SSL".
- Ojo con `-ss` antes de `-i` en los WAV de AI Studio: el encabezado engaña y devuelve audio vacío. Usar `atrim` o `-ss` después de `-i`.

## 0d. Dos cosas que arruinan un avatar de HeyGen (2026-10-27, Calistenia Rusa)
- ⬜ **Barras blancas arriba y abajo.** Si la foto del avatar no es 9:16, HeyGen la rellena con **blanco** y el video sale con dos franjas (en la toma parada del Coach Santi: 241 px arriba y 241 abajo). Santiago: *"que el avatar parado no se le vean los bordes blancos arriba y abajo"*. Se arregla **sin volver a generar**, con `OUTPUTS/scripts-vsl/prep_avatar_calistenia_rusa.py entrada.mp4 salida.mp4`: mide las filas casi blancas, recorta el contenido real y lo escala a 1080×1920 centrado. La persona queda entera de pies a cabeza y solo se pierde fondo a los costados. Correrlo **antes** del editor.
- 💬 **El testimonio va como captura de chat de WhatsApp**, no como foto de un señor. Pedido de Santiago: *"en la parte del testimonio podrías poner como si fuera la captura del chat de wpp, con lo que le dice el alumno"*. **No se hace con ChatGPT ni con ninguna IA de imagen**: el texto sale deformado. Se arma en HTML y se captura con **Chrome headless** (`--headless=old`, `--window-size=1080,1920`), que da un chat pixel perfect — ver `OUTPUTS/scripts-vsl/gfx_wpp_calistenia_rusa.py`. Detalles que lo hacen creíble: cabecera #075E54 con "en línea", fondo #E4DDD4, burbujas #FFF / #DCF8C6, **colita solo en el primero de cada tanda**, doble tilde celeste solo en los mensajes propios y la barra de "Mensaje" abajo.
  - El clip va en modo **`full`** (en `split` se perdería medio chat) con un zoom lentísimo. Como en `full` el subtítulo quemado cae en **CAP_Y_FULL = 1640**, los mensajes tienen que terminar **arriba de los 1200 px**: así el subtítulo queda en el fondo vacío del chat y no tapa ninguna burbuja.
  - El flag `--default-background-color=0` hace que Chrome **no escriba el PNG** y no avisa: no usarlo.

## 1. Pedido típico
- "Te paso el VSL de una oferta mía. Usá **exactamente el mismo guion**, adaptado a la oferta nueva, con acento **rioplatense**, para el público de la oferta."
- Se entrega **terminado**: avatar con labios sincronizados, B-rolls, subtítulos y edición, a **velocidad 1.3x**, en una carpeta del escritorio. **No se mete en el quiz** hasta que lo pida.

## 1b. Bajar el VSL original de Panda Video (2026-10-26)
El embed del quiz da el id: `player-vz-XXXX.tv.pandavideo.com/embed/?v=<uuid>`. El HLS sale **sin autenticación** en `https://b-vz-XXXX.tv.pandavideo.com/<uuid>/playlist.m3u8` (master con 360p, 480p y 720p). Con el 360p alcanza:
- audio para transcribir: `ffmpeg -i .../360p/video.m3u8 -vn -ac 1 -ar 16000 vsl.wav` y después faster-whisper (`small`, `language='es'`) con los tiempos por segmento;
- video para el mapa de B-rolls: `-c copy` y una hoja de contactos con `fps=1/5`. En una sola imagen se ve el minuto exacto de cada B-roll, cada placa y el estilo de los subtítulos.
- ffmpeg en la Mac de Santiago está en `~/bin/ffmpeg` (symlink al binario de `imageio_ffmpeg`); no hay ffmpeg de sistema ni Homebrew.

## 1c. Verificar las anclas ANTES de renderizar (2026-10-26, Calistenia Rusa)
Un `plan.json` con una frase mal elegida tira abajo todo el render después de 10 minutos de trabajo: ffmpeg corta con `Value -4700000.000000 for parameter 'durationi' out of range`, que es un B-roll con **duración negativa**. Pasa porque `find()` devuelve **la primera** aparición de la frase en la transcripción, así que si el ancla de fin también existe antes del inicio, el clip sale al revés.

Antes de lanzar la edición hay que correr un verificador contra el **`words0.json` ya transcripto** (no contra el guion) que chequee las tres cosas:
1. que la frase **exista en la transcripción**;
2. que el **fin caiga después del inicio**;
3. que el ancla sea **única** — si aparece más de una vez, avisar.

Chequear solo que la frase esté en el guion **no alcanza** y da falsos OK.

🆕 **2026-10-27 · Chequear contra `words0.json` tampoco alcanza.** El editor no busca las anclas ni en el guion ni en la transcripción cruda: alinea las dos con `difflib` y **reemplaza las palabras de Whisper por las del guion** donde el opcode es `equal` o `replace` del mismo largo. Lo que queda es una lista mezclada — casi todo el guion, pero con lo que Whisper oyó distinto en los tramos donde la alineación no calza (los números, sobre todo). Validar contra `words0.json` me hizo "arreglar" cuatro anclas que ya estaban bien y romper una (`empezá ahora.` pasó a `y empieza ahora`, que no existe en la lista final). El validador bueno es **`OUTPUTS/scripts-vsl/validar_anclas.py <work> <n> <guion.txt>`**, que reproduce los tres pasos del editor (sacar inventadas → unir guiones sueltos → reemplazar por el guion) y después busca. Regla práctica: **las anclas se escriben con las palabras del guion**, salvo donde hay números, que van con lo que diga Whisper o directamente se evitan.

🆕 **2026-10-29 · El validador tiene que normalizar las palabras EXACTAMENTE igual que el editor.** Este fue el error más caro de los post-pago de [[herrero-de-finde]]: el generador de planes usaba un `norm()` que dejaba la puntuación y el editor usa `re.sub(r'[^\w]', '', w.lower())`, que la saca toda. O sea que el ancla `'pantalla:'` para el generador era **única** y para el editor era **una de cinco** `pantalla` — y se comía la primera, a 11 segundos en vez de a 3:09. Lo mismo con `'vos.'` (5 candidatas), `'horas.'` (2) y `'precio,'` (8). Los tres VSL salían "OK" con cortes y placas en el lugar equivocado.

La regla, para cualquier generador de planes:
1. **El `norm()` del validador es el mismo objeto que el del editor**, copiado literal, con un comentario que lo diga. Si se tocan por separado, el validador miente.
2. El ancla se sigue escribiendo **con la puntuación del guion** (`pantalla:` vs `pantalla,` es lo que elige la aparición), pero el validador tiene que **traducir ese índice** al que va a contar el editor y escribir **ese** `occ` en el JSON.
3. El validador **imprime, para cada ancla, a qué palabra cayó y cuántas candidatas ve el editor**. "Existe" no alcanza: una placa de precio puede salir en el segundo 24 de un VSL de 3:26 y matar la venta.
4. **Chequear que las anclas queden en orden creciente.** Una lista de cortes escrita en orden del guion que resuelve a tiempos desordenados es la señal de que una se enganchó en una aparición de más arriba.

🆕 **2026-10-29 · El sello que cae justo en el corte desaparece sin avisar.** `edit_herrero_avatar.py` recorta el sello para que no pase al plano siguiente (`t1 = min(t1, proximo_corte - 0.02)`). Si el ancla cae **en el borde del corte**, `t1` queda antes que `t0` y ffmpeg no dibuja nada: el render sale "OK" con el sello perdido. Ahora el editor **avisa cuando una placa queda con menos de 0,4 s** y no la manda. Dos reglas visuales de la misma tanda:
- **La placa de hook va siempre sobre el avatar.** Si `hook_until` termina después del primer cutaway quedan dos gráficas encimadas; se corta el hook antes o se saca ese corte.
- **Sellos y chips se anclan a palabras que caigan sobre el avatar**, no adentro de un cutaway: un sello sobre una captura queda ilegible.

**Whisper escribe los números en cifras.** El guion dice "veintiocho días", "siete minutos", "diecisiete mil novecientos noventa" y la transcripción dice **"28 días"**, **"7 minutos"**, **"17.990"** — y a veces una sí y otra no en el mismo video. La regla: **las anclas no llevan números**. Se ancla en las palabras de al lado ("En mi aplicación vas a tener", "fue creado exactamente", "Movimientos sin impacto").

## 1d. Mirar cada B-roll antes de montarlo (2026-10-27, Calistenia Rusa)
Dos planos se colaron en el primer render y recién aparecieron en la hoja de contactos del final:
- **Una imagen del competidor con su coach y texto en español** (un diagrama de "Más energía / Menos estrés / ALIMENTACIÓN" con el Maestro Kaito en el medio). Vino de mapear mal el número de archivo del set del quiz. **Cada B-roll se mira a tamaño real antes de cargarlo al plan**, no solo en una miniatura de contacto.
- **Un plato de pan** en el momento del menú antiinflamatorio para bajar la panza. El B-roll no solo tiene que ser del tema: **no puede contradecir la promesa**.

**Reusar un plano del VSL viejo: revisar el subtítulo quemado.** El plano de la balanza del original servía (es oferta propia, §4d lo permite), pero trae el subtítulo **"BAJA COMO QUERRÍAS"** incrustado y la fuente es 360p, así que recortarlo lo dejaba borroso. Salió más barato y mejor **generarlo de nuevo** (5 créditos) que pelearse con el original. Antes de reusar un tramo, extraer un cuadro y mirarlo.

## 2. Guion
- **Estructura 1 a 1 con el original**: los mismos bloques en el mismo orden (hook, presentación, diagnóstico por el test, empatía, mecanismo, trampa, solución, producto, testimonio, bonos, anclaje, precio, escasez, garantía y cierre).
- **Alinear todo a la oferta y al quiz**: precio y tachado, bonos, minutos por día, garantía, nombre del método, entregables. El VSL no puede contradecir al quiz.
- **Tono hablado, que no suene robot** (2026-10-12):
  - frases cortas;
  - muletillas naturales ("mirá", "eh", "al toque", "decime una cosa");
  - pausas con "...".
  - **Presentación: "Soy la Maestra Caro"**, nunca "Me llamo Maestra Caro" ("queda muy raro").
- Números en palabras dentro del texto para la voz ("catorce mil novecientos noventa pesos").
- **No copiar claims médicos falsos** del original. Ejemplo: decir que la terapia hormonal "crea dependencia" se cambia por "dietas extremas o pastillas milagrosas". Avisarle el cambio a Santiago.
- **No fabricar testimonios en video** de "clientas reales" con IA. Si el original tenía uno, la avatar lee un testimonio que ya existe en el funnel.
  - **Excepción decidida por Santiago (2026-10-14, Mounjaro Humilde):** si él lo pide, el testimonio en primera persona lo hace su avatar de HeyGen **"Karina testimonio"** (voz roma).

## 3. Avatar y voz
- **Avatar: HeyGen** (decisión del 2026-10-12, en lugar de Higgsfield). Lo usa Santiago desde su sesión en Chrome.
- La experta de Pilates Hormonal es la **Maestra Caro**: mujer asiática, foto en `~/Downloads/WhatsApp Image 2026-10-09 at 13.26.36 (1).jpeg`.
- **Dos tomas del mismo personaje: una por bloque** (2026-10-26). Cuando Santiago pasa dos fotos "por si querés intercalar", se crean los dos avatares y se usa **uno por bloque de HeyGen** (sentado para diagnóstico y mecanismo, parado para oferta y cierre). Da variedad en el corte justo en el pivote del VSL y no cuesta un render extra.
- ⛔ **2026-10-27 · La voz masculina argentina NO se elige en HeyGen.** El VSL de Calistenia Rusa salió con **Agustín**, que HeyGen lista como *Spanish (Argentina)*, y Santiago lo rechazó: *"Tiene acento gallego, te dije que era argentino, me gastaste créditos al pedo, usá siempre las voces que te digo que sirven, no innoves una nueva cada vez"*. Reglas:
  1. **La etiqueta de idioma de HeyGen no garantiza el acento.** Ninguna de sus cuatro "Spanish (Argentina)" masculinas suena rioplatense.
  2. ⭐ **Voz de hombre argentino = "damian"**, el clon de ElevenLabs que Santiago ya tiene en HeyGen (*Mis voces → damian*, Multilingüe, Male). Es la que él mismo indicó el 27/10: *"usá esa para la voz, está ahí"*. Se asigna al avatar con **… → Agregar al Avatar → Establecer como voz predeterminada**, y después la Creación rápida ya la trae puesta. Como es una voz de HeyGen, el guion va **por texto**: no hace falta AI Studio ni el lipsync por audio del §0c.
     - Para **voz en off sin avatar** (ads), la de hombre argentino sigue siendo **Knox en AI Studio** con el Style de [[herrero-de-finde]], que es gratis.
     - Antes de generar, **mirar qué hay en "Mis voces"**: ahí están las voces que él ya validó. La Biblioteca de HeyGen es el último lugar donde buscar, no el primero.
  3. **No se estrena una voz en una entrega.** Si hace falta una voz nueva, primero una **muestra de 20 s gratis** y recién con el OK se gasta un crédito.

- **Voces argentinas en HeyGen:** en el selector, filtro *Idioma → Spanish (Argentina)*. Hay cuatro masculinas: **Agustín** (Middle Aged, Engaging, Podcasts — la que mejor calza con un coach a cámara), Casual Fernando, Narrator Mateo y Mateo Plácido.
- **Avatar IV en vertical cuesta más de lo calculado** (2026-10-26): dos bloques de 3.710 y 2.942 caracteres salieron **66 y 56 créditos** (122 en total), contra los ~80 que daba la cuenta de 17 créditos por minuto. Para presupuestar, usar **~25 créditos por minuto**.
- La voz tiene que sonar **muy real**, combinar con la avatar y sincronizar bien los labios. Acento rioplatense.

- **Las Tres Conexiones (Argentina, crianza):** experta **Juliana Alves**, mujer de unos 45 años con anteojos. La avatar se creó en HeyGen el 2026-10-13 desde la foto `~/Downloads/ChatGPT Image 13 oct 2026, 15_53_13.png` ("Crear un personaje virtual" → "Subir foto"), con la misma voz "voz roma". Precio $15.990, anclaje "sesiones de doscientos mil pesos", garantía de 30 días. Guion: `OUTPUTS/2026-10-13-vsl-tres-conexiones-argentina-guion.md`.
- **Subir archivos a HeyGen o Higgsfield desde Claude:** el botón abre el selector nativo de archivos. Antes de hacer clic se intercepta `HTMLInputElement.prototype.click` para los `type=file` y después se usa `file_upload` sobre el input. El archivo tiene que estar en el scratchpad o en el proyecto.

## 3b. Créditos de Higgsfield: no usar siempre el mejor modelo (2026-10-12)
- **Intercalar modelos baratos** para B-rolls e imágenes. "Si no, me consume todos los créditos."
- El modelo caro solo va en los planos que más se ven (el hook o un plano clave). El resto, en el modelo más barato que se vea bien.
- Antes de generar una tanda, decirle cuántos créditos se van a gastar.
- Referencia de precios (página de precios de Higgsfield, 2026-10-12): Kling 3.0 a 1080p ~8,75 por clip de 5 s · Kling 3.0 a 720p ~7/5 s · Seedance 2.0 Fast a 720p ~12/5 s · Seedance 2.0 a 720p ~22/5 s. Lipsync: Kling Speak a 720p ~1 crédito por segundo.
- **Los más baratos para B-roll (~5 créditos por clip de 5 s):** Kling 2.6 sin sonido, Wan 2.6 a 480p, Kling Omni 3 (referencia de imagen o primer y último frame) a 720p. Siguen Grok Video y Wan 2.6 a 720p (~7). Siempre **sin sonido** y a **5 s**.
- Mezcla sugerida para 12 B-rolls: 2–3 en Kling 3.0 (hook, anatomía 3D) y el resto en Kling 2.6 o Wan 2.6. Son unos 65 créditos en lugar de 105.

## 3b-bis. B-rolls sin quemar créditos (2026-10-26, Calistenia Rusa)
Con 49 créditos de Higgsfield se cubrieron los 17 momentos de B-roll de un VSL de 6 minutos gastando **25**:
- **Solo se generan los planos que no existen en ningún lado**: las anatomías 3D (cortisol, testosterona, fibras profundas, grasa). Modelo `cinematic_studio_video_v2`, `mode: std`, 5 s, `sound: off`, 9:16 → **5 créditos cada uno** (verificar con `get_cost: true` antes de la tanda). Si el prompt parece un preset, el server devuelve `preset_recommendation`: se reenvía con `declined_preset_id`.
- **Todo lo demás sale de fotos que ya tenemos** (las del quiz, las de los competidores) convertidas en clips de 5 s con un **zoom lento de ffmpeg**: `scale=2160:-2,zoompan=z='min(1.0012^on,1.18)':d=150:s=1080x1920:fps=30`. Alternar zoom in y out entre clips. Cuestan cero y en el corte no se distinguen de un B-roll filmado.
- Pedir siempre **"full body in frame"** en las anatomías: sin eso salen torsos flotantes recortados que parecen maniquíes.

## 3c. Créditos de HeyGen por modelo (medido el 2026-10-24, Protocolo Chía 28D)
- ⛔ **REGLA FIJA (2026-10-24): en HeyGen se usa SIEMPRE Avatar IV.** Santiago, después de que el primer bloque del VSL de chía se llevara 231 de 237 créditos con Avatar 6 Pro: *"Usa el avatar IV siempre, me gastaste todos los creditos"*. Nunca Avatar 6 (Pro ni Turbo) ni ningún modelo nuevo que venga por defecto, aunque gesticule mejor. **Antes de enviar, revisar qué modelo está elegido en Creación rápida** (el selector vuelve solo al modelo caro).
- **Avatar 6 · Pro (Beta): ~48 créditos por minuto.** Un bloque de 4.489 caracteres salió en 4:48 y costó **231 créditos**. Hace gestos con las manos y expresiones guiadas por el guion: es lo más parecido al original con avatar real.
- **Avatar IV: ~17 créditos por minuto** (los videos "CHIA G2/G3" de 1:02 costaron 17 cada uno). Movimiento genérico, sin gesto de manos.
- Un VSL de 18 minutos cuesta unos **870 créditos con Avatar 6 Pro** y unos **300 con Avatar IV**. Antes de arrancar un VSL largo, calcular esto y avisarle a Santiago.
- **El cuadro de Creación rápida tiene un tope de 5.000 caracteres**: un VSL largo se encola en bloques de ~4.500 (unas 780 palabras, 4:45 de video) y se unen en la edición.
- Si no alcanzan los créditos, los videos se encolan igual y quedan en Proyectos con el cartel "No tienes suficientes créditos": no se pierden créditos, pero hay que volver a enviarlos.

## 4a. Edición del VSL de LATAM de crianza ("VSL Mama", 2026-10-13)
- El original no tiene B-rolls ni placas: es la avatar a cámara con **subtítulos de a una palabra** (blanco con borde negro, fuente tipo Bangers, a la altura del pecho).
- Para la versión argentina se copia esa edición y **solo se varían los B-rolls**. Pedido de Santiago: **"no pongas el tiktok entero, sino recortes en partes específicas"**, de 2 a 3 s cada uno y variados. Un recorte cada 10–15 s, y se alternan:
  - TikToks de problema (grito, berrinche, no hace caso);
  - clips de Higgsfield con la solución (mamá a la altura del hijo, contacto visual, nene que guarda los juguetes, hora de dormir, mamá con la guía en el celular).
- **Antes de generar en Higgsfield, revisar el historial**: puede que Santiago ya haya generado B-rolls que sirven (2026-10-13: había 5 y se usaron 4).
- Script: `OUTPUTS/scripts-vsl/edit_tres_conexiones.py`. Además de la edición, mezcla la música y los efectos.

## 4. Edición (basada en el VSL original de Calistenia Asiática)
- Formato 9:16, avatar sentada a cámara.
- **Subtítulos siempre**: palabra por palabra, en blanco y mayúscula, sobre una franja negra a la altura del pecho.
- **B-roll cada 10–20 s** (más seguido al inicio): anatomía 3D, mujeres del público, la app, pilates, espejo.
- Placas:
  - **bonos** sobre el avatar en blanco y negro, con un 🎁;
  - **precio** grande en verde con una flecha roja hacia abajo;
  - **tilde verde** en el "¡Felicitaciones!".
- Recortar silencios y exportar a **1.3x**.

## 4b. Música y efectos de sonido (2026-10-13)
- **Música siempre:** suave por debajo de la voz, pero **activa y que enganche, no relajada**.
  - Se compone original con `OUTPUTS/scripts-vsl/music.py` (118 BPM, Am–F–C–G, bombo en negras, bajo con "pump" y arpegio), así no hay reclamos de derechos en Meta.
  - Mezcla: música unos 15 dB por debajo de la voz (voz -15 LUFS, música -30) y ducking con sidechain cuando ella habla.
- **Efectos, pocos y solo en momentos clave:**
  - **"cha-ching" cada vez que dice el precio ($14.990)**;
  - "pop" con brillo en cada bono;
  - sello en la garantía;
  - "ding" en el tilde inicial;
  - "whoosh" al entrar la app y el testimonio.
  Unos 10 en total. **No llenarlo de efectos.** Se sintetizan con `sfx.py`.
- Los efectos van en el momento exacto de la palabra: se transcribe el video final con Whisper y se ubica cada uno sobre la palabra.

### 🆕 2026-10-29 · La cama musical por defecto es la de Herrero, a -8 dB
- Santiago, sobre la tanda 1 de Solar Installer Pro: *"pone la misma musica que pones en la de herrero, un poquito mas alta, te quedo muy baja, tampoco tan alta"*.
- **Cama por defecto para los ads de voz en off:** `herrero-de-finde/anuncios/work/music/bed_A.wav` (93 s, no necesita loop). Se copia a la carpeta de la oferta como `music/bed_herrero.wav`.
- **Volumen: `music_db: -8`.** Es el valor de los ads de Herrero v13–v21 y el nuevo piso para todas las ofertas. **-11 quedó muy baja** (era lo que tenía la tanda 1 de Solar). No pasarse de -8: a -6 ya tapa la voz.
  - Recordar que `music_db` es **relativo al RMS de la voz** (el editor normaliza la cama contra la voz antes de aplicarlo), así que el valor sirve igual con cualquier pista.
- Sigue valiendo **una sola cama por tanda**. Separar la música del anuncio del competidor con demucs es un buen punto de partida, pero si no suena mejor que la de Herrero, va la de Herrero.
- **Para re-renderizar una tanda que a Santiago ya le gustó y solo cambiarle la música:** resetear `work/usage.json` a `{}` y renderizar V1→V6 **en el mismo orden**. El pool se elige con `random.Random(seed)` + el estado de `usage.json`, así que desde cero y en orden salen **exactamente los mismos planos**. Respaldar antes los MP4 y los `all.txt` de cada `*_tmp` para comparar.

## 4d. Reusar tramos del VSL original (testimonios, app, checkout) (2026-10-24, Protocolo Chía 28D)
- Cuando la oferta original **es de Santiago**, los testimonios y las capturas de la app y del checkout **se reusan tal cual** del MP4 viejo en vez de grabarlos de nuevo. Preguntar antes: si el original es de un competidor, no se tocan.
- Un tramo con **voz propia** (testimonios) no entra por `plan.json`: `plan.json` solo pone b-rolls mudos encima de la avatar. El bloque se arma aparte y se **inserta** en el render final con `OUTPUTS/scripts-vsl/insertar_bloque.py base.mp4 bloque.mp4 <segundo> salida.mp4`. El segundo se calcula sobre la línea del guion donde la avatar lo presenta.
- **Sacar la marca vieja en los dos canales.** No alcanza con cortar el audio: el subtítulo quemado va adelantado y sigue mostrando el nombre viejo. Para cada mención:
  1. se corta el audio+video del tramo (con los tiempos palabra por palabra de Whisper);
  2. si el subtítulo igual lo muestra, se borra esa banda con `rmsubs.py` y se escribe el reemplazo en un `.ass` con el mismo estilo (Arial Black 82, borde 7, blanco con la primera palabra en amarillo, `\pos(540,1392)` para el subtítulo de un testimonio vertical).
- Cortar siempre en una frase cerrada: terminar un testimonio a mitad de palabra se nota muchísimo.
- **Avisar los desfasajes que quedan**: si el checkout viejo muestra otro precio u otra moneda que la del guion nuevo, hay que rehacer esa captura cuando exista el checkout propio.

## 4e. Revisión obligatoria antes de entregar un VSL clonado (2026-10-25, Protocolo Chía 28D)
Los b-rolls recortados del video del competidor **traen medio segundo de su presentadora en cada punta** (el corte cae en la transición). Mirar el centro del clip no alcanza: 18 de 45 clips tenían a la presentadora del original al principio o al final, y en el render quedaba 1 segundo de otra mujer con nuestros subtítulos encima.
- **Detector automático**: se arma una huella (32x64 en grises) promediando frames de un clip que sea 100% presentadora y se compara contra todos los frames de todos los clips (1 muestra cada 0,1 s). Distancia < 60 = presentadora. `OUTPUTS/scripts-vsl/detectar_presentadora.py`.
- Con el mapa de tramos sucios se elige **el tramo limpio más largo** de cada clip y se lo vuelve a poner encima, estirado con `setpts` si es más corto que la ventana, **con el mismo LOOK** (grano, saturación, micro-movimiento) para que no se note el parche.
- Los **subtítulos quedan debajo del parche**: hay que re-quemarlos. Se filtran las líneas de `subs.ass` que caen en esas ventanas a un `.ass` chico y se queman después de los overlays.
- **Orden importante**: si se tapa un clip al que ya se le había borrado el subtítulo quemado con `delogo`, el parche **vuelve a traer el subtítulo viejo**. El `delogo` va siempre *después* de los overlays.
- Revisar siempre **tres frames por b-roll** (inicio +0,25 s, centro y final −0,25 s), no solo el centro.
- Mirar también lo que el clip trae quemado: precios viejos (`$24.999`), badges fijos del competidor y placas de su oferta aparecen en cualquier clip sacado después del minuto en que el original los pone en pantalla.

## 4f. El render va por segmentos en paralelo, nunca en un filtro único (2026-10-25)
Santiago: *"ni en pedo vas a tardar de nuevo 8 horas… esto tiene que tardar como muchísimo media hora"*. Tenía razón y el problema era el motor, no la edición.
- **Por qué tardaba 8 h:** `edit_vsl_quiz.py` armaba **un solo `filter_complex` con 70 capas** (45 b-rolls + 25 placas) aplicado a los 17 minutos enteros. Aunque una capa esté apagada en ese instante, ffmpeg copia igual el cuadro de 1080x1920 por cada capa y por cada cuadro: una cadena en serie, de un hilo, a 0,03x.
- **Cómo se hace ahora:** `RAPIDO=1` activa `OUTPUTS/scripts-vsl/render_rapido.py`. Corta la línea de tiempo en los bordes de cada b-roll, placa y zoom (~320 segmentos de 2 a 25 s), arma cada segmento con **2 o 3 capas en vez de 70**, los renderiza **de a 8 en paralelo** (`NUCLEOS`) y los pega con `-c copy`. Los subtítulos se recortan a un `.ass` por segmento con los tiempos corridos al cero.
- **Resultado medido:** 318 segmentos en **7:21** + 2:12 la pasada de audio y música = **9 minutos** para 16 minutos de video, contra 8 horas. `REUSAR=1` reaprovecha los segmentos ya hechos.
- Dos trampas al armarlo: en los segmentos con pantalla dividida las etiquetas del filtro se desfasaban (hay que usar el índice de la entrada como nombre, no un contador), y la lista del `concat` necesita **rutas absolutas** o no encuentra los segmentos.
- Con esto, **corregir una placa o un ancla y volver a tirar cuesta minutos**, así que conviene revisar y re-renderizar en vez de parchear el video final.

## 4c. Entrega y Panda
- El video final se **reemplaza** en `~/Desktop/<producto>-vsl/` con el mismo nombre.
- Santiago lo sube a **Panda Video** para ponerle diseños y manda el HTML del embed, que se pega dentro de `<template id="vsl-template">` en el último paso del quiz ([[quizzes-reglas-de-armado]]).

## 5. Cómo se produjo el de Pilates Hormonal (receta que funcionó, 2026-10-13)
1. **Transcribir el VSL original** con Whisper (`faster-whisper`, modelo `small`) y sacar cuadros cada 6 s para copiar la edición.
2. **Guion** en `OUTPUTS/`, en tono hablado y con los números en palabras.
3. **HeyGen**:
   - Se abre "Nueva revisión en AI Studio" de un VSL anterior con la misma avatar (Caro Pilates, voz "voz roma", Avatar IV), así se reusa la configuración.
   - El texto se cambia **solo dentro de los bloques (segments)** del editor TipTap. Si se reemplaza el documento entero, se borra la avatar.
   - El editor **no se dibuja si la ventana de Chrome está en segundo plano**: hay que pedirle a Santiago que la traiga al frente.
   - Costo: ~108 créditos de HeyGen para 6:44 de video.
4. **B-rolls** en Higgsfield, en clips de 5 s, 9:16 y sin sonido.
   - **El filtro de seguridad rechaza "torso/abdomen de mujer" en anatomía 3D** (marcado como NSFW, se devuelven los créditos). Usar "holograma de abdomen humano en wireframe" o "maniquí anatómico".
   - Pedir "not pregnant" en planos de panza: un "bloated belly" salió como embarazo.
5. **Edición** con ffmpeg y el script `OUTPUTS/scripts-vsl/edit.py`:
   - recorte de silencios (más de 0,45 s queda en 0,20 s; con 0,30/0,10 queda sin respiro a 1.3x);
   - zoom alternado por oración;
   - B-rolls y placas anclados a frases del guion;
   - blanco y negro en bonos y precio;
   - subtítulos ASS (Montserrat ExtraBold 76, franja negra, 2–3 palabras), apagados mientras hay testimonio o bonos en pantalla;
   - 1.3x al final.
   Las placas se arman con `mkgfx.py`.
6. **B-rolls de TikTok (2026-10-13): siempre sin marca de agua.** `yt-dlp` falla con TikTok (Python 3.9); se bajan con la API de tikwm: `curl "https://www.tikwm.com/api/?hd=1&url=<link>"` y se descarga el campo `hdplay` (o `play`). Después se revisan los cuadros para confirmar que no haya logo.

## 6. Anuncios UGC cortos con pantalla dividida (ads de Meta, 2026-10-14)
- **Referencias:** los ads de crianza en `~/Downloads`: "Qué pasa cuando.mp4" (es el de la pantalla dividida), "Mirá ni debería.mp4", "Si tu hijo.mp4" y "Toda mamá necesita.mp4". Tienen 40–55 s y música suave por debajo (las pausas nunca quedan en silencio).
- **Formato de la edición:**
  - la avatar a pantalla completa se alterna con la **pantalla dividida**: avatar arriba y B-roll abajo, desde justo debajo del mentón (y≈900 de 1920), con un **degradé coseno de ~220 px** y sin línea de corte;
  - el video **arranca con B-roll**.
- **Subtítulos:**
  - de 2 palabras, en Arial Black 64, blanco con borde negro, centrados en y≈1400;
  - no juntan dos oraciones.
- **Headlines:**
  - en **rojo** (#E81A2A) con borde negro, en MAYÚSCULAS y en Arial Black 78;
  - el borde superior va en y≈200, sobre el pelo y arriba de la frente, sin tapar ojos ni cara;
  - entran con un "pop" de escala;
  - uno por idea clave, unos 11 en 36 s, de 1–2,4 s cada uno.
- **Efectos:**
  - "pop" suave en cada headline;
  - "cha-ching" en la plata (precio de venta, "lo recuperé con el primer pedido");
  - whoosh bajito cuando entra un bloque de B-roll.
- **Ritmo:** recortes de 1–3,5 s de **planos distintos** de cada clip, sin repetir, congelar ni estirar. Recorte de silencios (0,40 → 0,18 s) y **1.1x** (no 1.3x como los VSL).
- **Avatar en HeyGen:**
  - Avatares → la avatar → hover en el look → ícono de video → "Creación rápida";
  - la voz se cambia en "Mis voces" → "voz roma" → "Establecer como predeterminado";
  - el guion se pega tal cual, en 1080p vertical;
  - se descarga con el botón de descarga. El `src` del video está bloqueado para JS.
- **Script:** `OUTPUTS/scripts-vsl/edit_ugc_split.py <heygen.mp4> <carpeta_trabajo> <salida.mp4>`. La carpeta de trabajo tiene `brolls/`, `sfx/` y `fonts/`. El guion va adentro del script, en la variable `GUION`, y también corrige los subtítulos. Los B-rolls y los headlines se anclan a frases en `PLAN` y `HEAD`.
- Primer ad hecho así: `~/Desktop/scented-stones-ad/Scented-Stones-Ad-Bridal.mp4` (Scented Stones, caja para la despedida de soltera).

- **Corrección (2026-10-14): "no pongas tantos headlines arriba, porque se hace muy cansador el efecto de sonido; solo los puntos importantes".**
  - Máximo **3–4 headlines por ad**, solo en los puntos clave: el número grande del hook, la objeción que se rompe, el costo y el CTA.
  - Cada headline con un solo sonido.
  - Sin whoosh en cada B-roll.
- **Variar las ediciones entre ads (2026-10-14).** No repetir siempre la pantalla dividida. Formato 2, "orgánico de TikTok":
  - B-roll a pantalla completa con la **avatar recortada sin fondo, chiquita en la esquina de abajo a la derecha** (estilo green screen), alternada con la avatar a pantalla completa;
  - zoom de salto por oración y cortes secos;
  - subtítulos de 3 palabras en Arial Rounded, con la plata en amarillo.
  - El fondo se saca con Robust Video Matting en ONNX (`OUTPUTS/scripts-vsl/matte.py`, modelo `rvm_mobilenetv3_fp32.onnx` de los releases de GitHub del proyecto). Corre local y procesa ~4 s de video por segundo.
  - Script: `OUTPUTS/scripts-vsl/edit_ugc_pip.py`. El plan de B-rolls y los headlines van en `plan_pip.json` y `heads_pip.json`, dentro de la carpeta de trabajo.

- **Pilates Hormonal en formato 2 (2026-10-14):** `~/Desktop/pilates-hormonal-ad/Pilates-Hormonal-Ad-Cortisol.mp4` (28 s).
  - Avatar Caro Pilates con "voz roma", en español.
  - Los **12 B-rolls del VSL** (b01–b12, de Higgsfield) quedaron guardados en `~/Desktop/pilates-hormonal-ad/work/brolls/`. Antes estaban solo en un scratchpad temporal. `b05_embarazada` no se usa.
  - El script toma el idioma como 5.º argumento (`es`).

- **Formato 3, "cortes + green screen grande" (2026-10-14).** Pedido de Santiago: "variá la edición, no quiero que pongas el avatar chico".
  - B-roll a **pantalla completa sin avatar** (`full`) y avatar recortada **en grande** delante del B-roll (`gs`, bajada 330 px; el subtítulo va al pecho).
  - En el resto, avatar a pantalla completa con zoom de salto.
  - Va en el mismo script: 5.º campo de cada entrada del plan (`pip`, `full` o `gs`), y el plan se pasa como 6.º argumento.
  - Primer ad: `~/Desktop/pilates-hormonal-ad/Pilates-Hormonal-Ad-Asia.mp4` (28 s, Caro Pilates, guion "mujeres de 60 en Asia").
- **B-rolls de ejercicio en Higgsfield (2026-10-14):**
  - **5 clips con Kling 2.6** (5 créditos cada uno, 25 en total, sin audio, 5 s, 9:16): parque con asiáticas de 60, templo con niebla, sentadilla contra la pared, flexiones contra la pared en casa y plancha contra la pared con brillo en el core.
  - Guardados en `~/Desktop/pilates-hormonal-ad/work/brolls/h1–h5`.
  - Se bajan sin el botón: leyendo el `src` de los `<video>` del historial, que en Higgsfield no está bloqueado, y con `curl`.
  - La sentadilla contra la pared sirve solo los primeros 3 s, porque después la cámara se mete en el cuerpo.
- **Whisper inventa palabras al principio** cuando se le pasa el guion como `initial_prompt` (salió "Después de un minuto"). El script descarta las que no están en el guion.

- **Corrección (2026-10-14): "que las visuales no sean tan IA, que no se note tanto; no hagas nuevos B-rolls todo el tiempo, solo si es súper necesario".**
  - **Reusar primero** los B-rolls que ya están en la carpeta de trabajo. Se generan nuevos solo si falta una escena clave, y se avisa antes.
  - Elegir los planos **más "reales"** (personas haciendo algo en casa, en el gimnasio o en el parque). No usar hologramas, anatomía, brillos, templos épicos ni nada que grite IA, salvo pedido.
  - A todos los B-rolls se les da **look de celular** (`ORGANIC = True` en el script): leve movimiento de mano, -14 % de saturación, menos contraste, menos nitidez y grano.
- **Formato 1 con Caro (pantalla dividida) en el mismo script (2026-10-14):**
  - Modo `split` (degradé coseno de 220 px desde y=880, subtítulo en y=1400).
  - El B-roll se recorta desde y=340 para que no quede la cabeza de la persona bajo el degradé. Si el plano importante es la panza, en el 6.º campo del plan va otra altura (ej. 760).
  - Ad: `~/Desktop/pilates-hormonal-ad/Pilates-Hormonal-Ad-Rodillas.mp4` (27 s): split + algunos cortes a pantalla completa, 4 headlines y 0 B-rolls nuevos.
- **Ad "I thought" y su variable "Budget" (Scented Stones, 2026-10-15):**
  - El original (`~/Downloads/I thought scented.mp4`, 42 s, ángulo guía gratis, pantalla dividida) usa la avatar de HeyGen **"PERRITA RICA"** (delantal, sweater crema, piedra con lavanda en la mano) con "voz roma" en inglés. No había quedado registrado.
  - Variable: mismo body y CTA, hook nuevo ("…way out of my budget"). Edición mixta `gs` / `full` / `pip` con los 6 B-rolls de piedras ya existentes (0 nuevos). Plan y headlines en `work/plan_ithought.json` y `work/heads_ithought.json`. La toma de HeyGen salió de 55 s.
  - Santiago: "hacelos rápido, no gastes créditos de más" → **una sola generación por guion** en HeyGen y nada de B-rolls nuevos si alcanzan los que hay.
- **Tanda UGC con PERRITA RICA (Scented Stones, 2026-10-20).** Pedido: "más videos, buena edición, variedad de formatos, efectos de sonido, que sean entretenidos".
  - 5 guiones de ~115–130 palabras, cada uno con un formato propio (empaquetá conmigo, lista de 3 errores, "adiviná cuánto costó", storytime de la florista, el marido que hace las cuentas en una servilleta). Guiones: `OUTPUTS/2026-10-20-guiones-piedras-ugc-avatar-v2.md`.
  - HeyGen: avatar PERRITA RICA → "Usar en un video" → Creación rápida (Avatar IV, voz roma, vertical 1080p). Salen de 34–39 s. **Después de enviar, el cuadro tarda unos 5–10 s en vaciarse**: no pegar el guion siguiente hasta que se vacíe, o se mezclan los textos. Se pueden encolar los 5 seguidos.
  - Edición con `edit_ugc_pip.py`, mezclando los modos por video (`split`, `pip`, `gs`, `full`) para que no se repitan.
  - **Efectos nuevos en `sfx.py`:** `buzzer` (cada error de la lista), `drumroll` (antes de revelar un número), `tick` (pregunta "adiviná"), `scribble` (cuentas en papel), además de `ding`. En `heads_*.json` un texto vacío (`""`) pone **solo el efecto**, sin headline.
  - Higgsfield estaba sin sesión: se usaron solo los 6 B-rolls de piedras que ya había.
- **Whisper en bucle (2026-10-20):** en un video repitió frases inventadas al final ("Number four, books…") y se perdieron los anclajes del cierre. Se arregla con `condition_on_previous_text=False` (ya está en `edit_ugc_pip.py`). Si un ancla tiene un número con guion ("eighty-dollar"), Whisper lo transcribe en cifras ("80 dollar") y no se encuentra: anclar en las palabras de al lado.
- **Bug resuelto:** una imagen con `-loop 1` sin `-t` (más una rama `nullsink`) dejó a ffmpeg corriendo sin fin. Siempre ponerle `-t`.

## 7. VSL corto de la nutri dentro del quiz (Mounjaro Humilde, 2026-10-14)
- El "VSL" de Brasil ("Sua Receitinha Personalizada", 49 s) es el **video de la nutri Luana** del paso 12 del quiz: explica por qué se hacen las preguntas, que la receta es 100% natural y el "poder de las combinaciones".
- **Avatar:** HeyGen "Nutri Mounjaro" (Avatar IV, con la voz que trae puesta: "voz roma"), Creación rápida, vertical 1080p. Salió de 46 s y costó unos 15–20 créditos. **HeyGen se quedó en 0 créditos** y Santiago cargó más: antes de generar, revisar los créditos (menú de la cuenta → "Créditos: Quedan N").
- **Edición copiada del original** (`OUTPUTS/scripts-vsl/edit_vsl_quiz.py`, basado en `edit_ugc_pip.py`):
  - subtítulos **de a una palabra** en mayúscula (Arial Black 82, blanco con borde negro, al pecho y sobre el corte en la pantalla dividida);
  - **pantalla dividida con capturas del propio quiz** abajo (género, zonas, tipo de cuerpo, edad, dificultades). Se sacan con Chrome headless desde una copia del quiz que abre el paso `?s=N&sel=...`, y se arman en tarjetas con `mk_panels.py`;
  - B-rolls del té (los 5 de Santiago) e imágenes de antes y después del quiz a pantalla completa;
  - 3 palabras clave en **verde** con "pop" (MOUNJARO HUMILDE, 100% NATURAL, ¡RÁPIDO Y EFICAZ!);
  - 1.08x.
- Entrega: `~/Desktop/mounjaro-humilde/vsl/Mounjaro-Humilde-VSL-Nutri.mp4`. Guion: `OUTPUTS/2026-10-14-vsl-nutri-mounjaro-humilde-guion.md`.

## 8. VSL final del quiz con testimonio (Mounjaro Humilde, 2026-10-14)
- El original (1:39) tiene tres partes: la nutri ("¡Felicitaciones! armamos tu plan…"), el **testimonio de una clienta** (casi un minuto, precio "R$47,90, una única vez") y otra vez la nutri (garantía de 30 días, "la panza chata se hace en la cocina", CTA "Tocá en PEGAR MEU PLANO"). Termina con una placa de flechas.
- Versión AR: precio **$19.990** ("diecinueve mil novecientos noventa pesos"), CTA "Quiero mi plan" (el botón del quiz) y entrega **por e-mail**, porque el quiz ya no pide WhatsApp.
- HeyGen: la nutri en un solo video (intro + cierre, se corta en "Creemos") y Karina testimonio en otro (1:07). El cuadro de texto de HeyGen a veces no toma el foco: hacer clic con `find` sobre el textbox.
- Edición: el mismo `edit_vsl_quiz.py`, con nuevas opciones:
  - `NOMUSIC=1` en cada parte, y la música se pone una sola vez sobre el video unido;
  - `CAPCOLOR` en amarillo verdoso para el testimonio, como el original;
  - `capmap.json` para mostrar el precio en cifras ("$19.990" en verde);
  - `stickers.json` para el sello dorado de garantía de 30 días (`mk_gfx.py`, puntas calculadas);
  - placa final "Tocá en QUIERO MI PLAN y terminá tu inscripción" con flechas.
- **Peso:** con grano y crf 17 sale enorme (376 MB para 1:28). Se re-exporta con crf 21 y maxrate 8M (~60 MB).
- Entrega: `~/Desktop/mounjaro-humilde/vsl2/Mounjaro-Humilde-VSL-Final.mp4` (1:28). Guion: `OUTPUTS/2026-10-14-vsl2-mounjaro-humilde-guion.md`.

## Registro de correcciones
| Fecha | VSL | Corrección | Regla |
|---|---|---|---|
| 2026-10-14 | Mounjaro Humilde (VSL final) | El testimonio lo hace el avatar "Karina testimonio"; precio $19.990 | §2 excepción, §8 |
| 2026-10-12 | Pilates Hormonal | "Me llamo maestra Caro queda muy raro" → "Soy la Maestra Caro"; que no suene robot | §2 tono hablado |
| 2026-10-12 | Pilates Hormonal | El video se hace con HeyGen | §3 |
| 2026-10-12 | Pilates Hormonal | "Usá modelos más baratos, intercalá, no uses siempre el mejor" | §3b |
| 2026-10-13 | Pilates Hormonal | Música suave por debajo, activa, que enganche | §4b |
| 2026-10-13 | Mamá (Argentina) | "Los tiktoks descargalos sin marca de agua" | §5 paso 6 |
| 2026-10-13 | Tres Conexiones (Argentina) | B-rolls: recortes de partes específicas, no el TikTok entero, e ir variándolos | §4a |
| 2026-10-13 | Tres Conexiones (Argentina) | "Ya hay generados 5 brolls, tal vez los podés usar" → revisar el historial de Higgsfield antes de generar | §4a |
| 2026-10-13 | Pilates Hormonal | Efectos solo en momentos clave: "cha-ching" al decir el precio; no llenarlo | §4b |
| 2026-10-14 | Scented Stones (ad UGC) | "No pongas tantos headlines arriba, se hace muy cansador el efecto de sonido; solo los puntos importantes" | §6: 3–4 headlines por ad |
| 2026-10-14 | Scented Stones (ad UGC) | "La idea es variar las ediciones": avatar chiquita sin fondo en una esquina, full UGC orgánico de TikTok | §6: formato 2 |
| 2026-10-14 | Pilates Hormonal (ad "Asia") | "Variá la edición, no quiero que pongas el avatar chico"; 5 B-rolls nuevos de ejercicio que llamen la atención | §6: formato 3 |
| 2026-10-14 | Pilates Hormonal (ad "rodillas") | "Fijate que las visuales no sean tan IA; no hagas nuevos B-rolls todo el tiempo, solo si es súper necesario" | §6: reusar B-rolls, planos reales y look de celular |

## Preguntas abiertas
- ¿Qué plan de HeyGen hay y cuál es el largo máximo por video?

## Relacionado
[[ugc-y-video-generativo]] · [[quizzes-reglas-de-armado]] · [[embudo-vsl-post-pago]] · [[pagina-de-ventas]]

## Fuentes
- Conversación del 2026-10-12. Guion: `OUTPUTS/2026-10-12-vsl-pilates-hormonal-guion.md`
