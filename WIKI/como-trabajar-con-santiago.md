# Cómo trabajar con Santiago

> Reglas de interacción, pedidos típicos y glosario. **Leer antes de cualquier tarea creativa.** (fuente: RAW/2026-10-10-contexto-maestro-santiago.md)

## Rol de Claude
Experto en **ofertas de infoproductos low ticket** y **anuncios de direct response**. Por defecto trabajo sobre [[scented-stones]] y aplico [[guiones-y-anuncios]].

## Herramientas que uso
- Para variables y backend, partir de los prompts de [[biblioteca-de-prompts]] cuando estén en `RAW/prompts/`.
- **Campañas en Meta:** crear todo en pausa, mostrar el resumen, esperar el OK y verificar el estado real de cada campaña, conjunto y anuncio ([[claude-con-meta-ads]]).
- **"Cazar"** → usar la skill `cazar` ([[caza-de-ofertas]], documentada entera) y sumarle los filtros de [[funnel-hacking]]: mismo URL, sin marca personal, 1 semana o más. Lo que busca Santiago: **low ticket, escondida (no la que ve todo el mundo), sin marca personal, ya escalada o empezando a escalar, y que venda.**

## Pedidos típicos
"Dame más guiones / variables de este ganador" · "Dame natives" · "Dame la descripción de X" · "Descripción para ads con emojis, no tan larga" · "Armemos los upsells" · "Analizá la landing de mi competidor" · "Palabras clave para cazar en PT/EN" · "Resumen de la oferta X para otro chat" · "Variante del guión Y pero X".

## Reglas de interacción
- **"Me gustó el X"** → copiar la onda (tono, energía, cercanía), no el guion: hooks, protagonistas y situaciones nuevas ([[guiones-y-anuncios]], registro del 2026-10-14).
- **"Mejores" o "variables"** → otro ángulo de verdad, misma DNA. Partir de la DNA de [[scented-stones]].
- **"En inglés y español"** → las dos versiones completas.
- **"X minutos"** → unas 150 palabras por minuto.
- **"No quiero precio"** → "baratísimo" o "dirt cheap".
- **Etsy** → sacarlo y poner WhatsApp.
- **"Muy catastrófico"** → benefit-forward, FREE today o abundancia.
- **"Largo"** → 400–500 palabras.
- **Métricas:** no pedirlas. Santiago las manda cuando haga falta.
- **Entrega para copiar y pegar (siempre):** todo guion, hook, native o descripción va en bloque de código en el chat, se guarda además en `OUTPUTS/AAAA-MM-DD-<titulo>.md` en texto plano (sin citas `>` ni negritas dentro del texto a copiar) y se copia al portapapeles con `pbcopy`. Desde el chat no puede copiar bien.
- **Formato limpio de guiones (regla fija, 2026-10-13):** cada guion lleva solo el título **Guion N** en negrita y subrayado y abajo **solo el texto que se lee**. **No se escriben** etiquetas de estructura (Hook, Problema, Valor, Beneficios, CTA), ni B-roll (`[BROLL: …]`), ni segundos, ni ángulo, nivel de conciencia, primer frame, conteo de palabras o duración. La estructura la uso yo para armar el guion, no va escrita. En el chat: título en negrita fuera del bloque y el guion en un bloque de código. En el portapapeles: texto enriquecido (RTF) con el título en negrita y subrayado. Si hace falta explicar algo (ángulos, decisiones), va en el mensaje, fuera de los guiones.
- **Las natives también van completas en el chat (regla fija, 2026-11-02).** Santiago: *"Dame los prompt y descripciones, no me sirve que me las mandes así"*, después de que le entregara las natives 15 y 16 con un **resumen** de cada una y el link al archivo. Regla: una native entregada es **el prompt de imagen y la descripción enteros, cada uno en su bloque de código en el chat**, listos para copiar y pegar, igual que un guion. El resumen (narradora, objeto, ángulo) va **además**, nunca en lugar del texto. Vale para prompts, descripciones, natives, hooks y cualquier pieza que tenga que copiar: si no está el texto completo en el chat, la entrega no está hecha.
- **Oferta en inglés:** guiones y hooks siempre en 🇬🇧 inglés y 🇪🇸 español con voseo, las dos versiones completas. **Excepción: las natives van solo en inglés** (prompt y descripción), sin versión en español (2026-10-14).

## Quizzes y landings en HTML
- Antes de armar o editar uno, leer [[quizzes-reglas-de-armado]] y recorrer su checklist.
- Cada corrección suya que sirva para el futuro se anota ahí **en el momento** (registro con fecha + regla), sin que lo pida. Después, commit y push.

## Una página terminada se toca solo donde duele (regla fija, 2026-11-04)
Santiago: *"Si la página ya estaba terminada, no tenías que cambiar nada más que los botones de CTA redirijan al checkout"*.
- Cuando pide **arreglar una cosa** de una landing o un quiz que ya dio por terminado, se arregla **esa cosa y nada más**. No se aprovecha el viaje para cambiar imágenes, textos, precios ni secciones.
- Lo que uno encuentre de paso (un pendiente viejo, un recurso roto, una mejora) **se le avisa en una línea y se espera**. No se ejecuta solo.
- Vale igual para los pendientes anotados en el `changelog.md`: estar anotados no los autoriza.
- Hermana de la regla de [[monjaro-violeta]]: *lo que tiene una oferta no se deduce, se pregunta*.

## Lo que se manda a elegir va solo (regla fija, 2026-10-28)
Santiago: *"quedó todo hecho un desorden, vos tenés que subirme solo 3 voces, en una carpeta que sea voces, yo te digo cuál usar y listo, no me tenés que subir absolutamente todo"*.
- Cuando tiene que **elegir** (voces, hooks, imágenes, cortes), se le entregan **solo las opciones**, numeradas `1 - …`, `2 - …`, `3 - …`, en **una carpeta propia con nombre claro** dentro de `~/Desktop/<oferta>/` (por ejemplo `anuncios/voces/`). Tres opciones, nada más.
- **Nunca se le abre una carpeta de trabajo.** Todo lo intermedio (crudos, bloques cortados, json de alineación, versiones) queda en `work/` y no se muestra.
- Las opciones se entregan **como van a sonar o verse en el video final** (la voz ya con su velocidad y sus pausas), no en crudo.

## En la carpeta de entrega van solo los archivos que van (regla fija, 2026-11-05)
Santiago, al ver los 6 videos de [[orzzen-automatas]] duplicados: *"Porque tengo muchos videos, dejame solo los que van"*.
- Yo había dejado los renders con nombre de trabajo (`V1.mp4` … `V6.mp4`) **al lado** de las copias numeradas (`5-11 - 1.mp4` …): doce archivos para seis videos.
- Regla: el render crudo se **mueve**, no se copia. En la carpeta que él abre queda **un archivo por pieza**, con el nombre de tanda `DD-M - N`, y nada más. Los `_tmp` del editor se borran apenas termina el render.
- Es la misma idea que "lo que se manda a elegir va solo": él no tiene que decidir cuál de dos archivos iguales es el bueno.

## Trabajar en la compu de Santiago (regla fija, 2026-10-25)
- **Todo el laburo se hace en su Mac, siempre.** Santiago: *"acordate de laburar en mi compu SIEMPRE"*. Voces, renders, descargas, imágenes y archivos van a su disco, no a un entorno remoto ni a una carpeta temporal del sistema.
- En la práctica: las voces se graban con su Chrome en AI Studio, los videos se renderizan con los scripts locales de `OUTPUTS/scripts-vsl/`, y los entregables terminan en `~/Desktop/<oferta>/` según la regla de carpetas de arriba.
- **Reconfirmada el 2026-10-28:** *"Trabaja en mi compu SIEMPRE, guardalo como regla eso"*. Vale también para las herramientas por navegador: HeyGen, AI Studio y Higgsfield se usan desde **su Chrome, con sus sesiones iniciadas** (la cuenta de HeyGen que usamos es la de **Juan**, sesión ya abierta), y todo lo que se genera se baja a su disco.
- Los archivos intermedios que no son entregables van al scratchpad de la sesión, nunca sueltos en el Escritorio ni en `/tmp`.

- **Mutear las páginas que uso (regla fija, 2026-10-26).** Santiago: *"y mutea las paginas que uses"*. Antes de generar nada en AI Studio (o en cualquier página que reproduzca audio), inyectar: mute de todos los `<audio>`/`<video>` con un MutationObserver para los que aparezcan después, y un Proxy sobre `AudioContext` que mande la salida por un gain en 0 (AI Studio reproduce por WebAudio, así que mutear el `<audio>` solo no alcanza). Se reinyecta en cada pestaña nueva.

## Voces fijas (REGLA FIJA, 2026-11-01)
Santiago: *"Usa las voces que siempre usas, si es de hombre usa de hombre, si es mujer usa mujer, no quiero una nueva por cada oferta, si la quisiera te lo voy a decir."*
- **Mujer → Sulafat** (AI Studio, Warm). **Hombre → Orus** (AI Studio, Firm, lower middle pitch).
- **No se eligen voces por oferta y no se le mandan 3 opciones a elegir.** La decisión que queda de mi lado es solo **si la voz va de hombre o de mujer**, según el avatar de la oferta. Lo demás ya está decidido.
- El acento, la edad y el tono se dirigen desde el **Style** de AI Studio, no cambiando de voz.
- Solo se estrena una voz nueva **si él la pide**. Extiende la regla del 27/10 ("usá siempre las voces que te digo que sirven, no innoves una nueva cada vez") a todas las ofertas y herramientas.


### ⛔ El sexo de la voz lo decide el NICHO, no el ganador (REGLA FIJA, 2026-11-26)
Santiago, sobre la tanda 1 de [[puertas-de-acm]]: *"Es un nicho de hombres, cuando es así la voz tiene
que ser de hombre, ajustalo con alguna que quede bien."*
- Yo había puesto **mujer** porque el ganador corre locutora (le medí el F0 a sus ads: 198-219 Hz) y la
  regla decía "según el avatar de la oferta". **Clonar su locutora no es el criterio.** Si el que compra
  es un herrero, un carpintero, un tornero o un albañil, la voz va de **hombre**, aunque el ganador la
  use de mujer. Al revés también: nicho de mujeres → mujer.
- Las voces no cambian: **hombre → Orus, mujer → Sulafat**. Lo que cambia es cuál de las dos se elige.

### 🐞 Orus suena a mujer en el modelo 3.1: el sexo de la voz se MIDE (2026-11-26)
Con **`gemini-3.1-flash-tts-preview`**, Orus salió a **195 Hz de F0** — 18 Hz por debajo de Sulafat, o
sea indistinguible de una voz de mujer. Con **`gemini-2.5-flash-preview-tts`** la misma voz y el mismo
bloque de estilo dan **122-136 Hz**, que es un hombre de verdad.
- **Para una voz de hombre, el modelo es `gemini-2.5-flash-preview-tts`.** El 3.1 queda para mujer.
- ⛔ **Preguntarle a Gemini "¿es hombre o mujer?" NO sirve**: con la pregunta corta contestó "HOMBRE"
  para las dos voces, y con la pregunta larga contestó "Hombre" hasta para Sulafat. Lo único que
  distingue es **el F0 por cepstrum** sobre el wav: hombre 110-145 Hz, mujer 190-225 Hz. Una
  autocorrelación simple tampoco sirve, engancha el primer armónico y da ~220 Hz para las dos.
- Se mide **antes de generar la tanda**, con un control de un renglón, y se verifican **los seis** después.

## La voz en off sale por API, no por el navegador (regla fija, 2026-11-02)
Santiago pasó su clave de Google AI Studio: *"para que no tengas que usar mi compu y puedas trabajar mucho más rápido"*.
- **`OUTPUTS/scripts-vsl/tts_gemini.py`** con `GEMINI_API_KEY` (guardada en `~/.config/herrero/gemini.env`, fuera del repo). Modelo **`gemini-2.5-flash-preview-tts`**: los TTS 3.x **leen en voz alta las instrucciones de estilo** cuando se usan por API, así que no sirven.
- Las voces fijas no cambian (hombre → **Orus**, mujer → **Sulafat**); el acento y la edad se dirigen desde el Style, que va como párrafo arriba del guión y cierra con *"Lee únicamente el texto que viene a continuación:"*.
- Esto **no levanta** la regla de trabajar en su Mac: los archivos, los renders y los entregables siguen cayendo en su disco. Lo que desaparece es el navegador (pestañas perdidas, una generación por carga de página, muteos).
- **El acento se verifica**: se le manda el wav a Gemini y se le pregunta qué variedad de español escucha. Es gratis y evita renderizar una tanda entera con el acento equivocado.
- ⛔ **18/11/2026: el default pasó a `gemini-3.1-flash-tts-preview`, porque `gemini-3.8-flash-tts` LEE EN VOZ ALTA el bloque de estilo.** Esto se da vuelta con cada versión del modelo, así que **antes de cada tanda se corre un control de 7 palabras con el mismo estilo**: si dura 3-4 s está limpio, si dura 30 s está leyendo las instrucciones. Detalle en [[quizzes-reglas-de-armado]] (regla del 18/11).
- **Si `gemini-2.5-flash-preview-tts` devuelve 429 (cuota), el reemplazo es `gemini-3.1-flash-tts-preview`** (registro del 2026-11-02, tanda rusa de piedras): con la misma voz Sulafat **no leyó las instrucciones de estilo en voz alta**. Verificar igual el primer wav antes de renderizar la tanda. `gemini-2.5-pro-preview-tts` comparte la cuota y también da 429.

### ⛔ La voz no susurra: el estilo manda más que la velocidad (regla fija, 2026-11-25)
Santiago, sobre la tanda 1 de [[the-artist-method]]: *"Porque susurra la voz, que suene normal, como la
que te dije ayer que me gustó"*.
- **Lo que la hace susurrar es el bloque de Style, no la voz.** Yo había escrito *"speaking softly and
  close to the microphone, calm, unhurried"* y Sulafat obedeció: salió en susurro a 122 ppm.
- **El estilo que funciona es el de [[fuga-perfecta]] del 24/11**, traducido: una mujer grabándose con el
  celular para mostrarle algo que le encanta a una amiga, **hablando rápido y vivo, a volumen normal**,
  con entonación despareja, *"talking, not reading"*, y los negativos explícitos: **never breathy, never
  whispered, never a soft bedtime or meditation voice**. Con eso da 172-211 ppm en crudo y volumen normal.
- **El control se hace sobre un guion entero, nunca sobre 7 palabras.** La frase corta dio "británico"
  dos veces y "susurra" siempre; el guion completo dio General American y volumen normal. Y se pregunta
  por **las tres cosas**: acento, volumen (¿susurra o habla normal?) y energía.
- **Hay que verificar los 6, no uno.** En esta tanda cinco salieron bien y el sexto no: su texto hablaba
  de calma y silencio, y el modelo **lee el ánimo del contenido**. Para esos se le escribe al estilo el
  contraste a propósito: *"the words talk about calm, but SHE IS NOT CALM: full chest voice throughout"*.
- **El `speed 1.20` no es un número fijo, es un objetivo de ppm.** Con un estilo que ya lee rápido, 1.20
  atropella. Lo que se mantiene constante es el **ritmo final de 167-188 ppm**; el speed de cada video sale
  de dividir. En `gen_tam_plans.py` eso quedó automático (`velocidad()` mide el wav y despeja).

### Cuota de TTS: 10 por día y por modelo, y se acaba (registro 2026-11-25)
Rehacer una tanda de 6 voces agota el día: `gemini-2.5-flash-preview-tts`, `gemini-3.1-flash-tts-preview`
y `gemini-2.5-pro-preview-tts` (este con `limit: 0`) devolvieron todos 429.
- **La salida es AI Studio desde su Chrome**, que tiene cuota aparte. En el playground de voz hay que
  **cambiar el modelo al mismo que el resto de la tanda** (Gemini 3.1 Flash TTS Preview): con el 3.8 que
  viene por defecto la voz sale blanda aunque el estilo diga lo contrario.
- Con el 3.1 la UI cambia: el campo de estilo desaparece y el texto de dirección va en **"Scene"**.
- 🐞 Al tipear en el desplegable de Style, el primer clic **elige el preset "Whisper"** y el texto del
  guion se mete en el campo de estilo. Hay que apuntar al textbox por `ref` y cerrar con Escape antes de
  escribir el guion.

## Créditos (regla fija, 2026-10-24)
- **Siempre la opción más barata que sirva, en todo**: modelo, resolución y cantidad de generaciones. Santiago: *"acordate de usar siempre lo mas barato, para todo"*. El modelo caro solo si lo pide.
- En HeyGen, **siempre Avatar IV**, nunca el modelo caro que viene por defecto ([[vsl-reglas-de-armado]] §3c).
- **No se estrena nada en una entrega.** (2026-10-27, voz gallega del VSL de Calistenia Rusa: *"usá siempre las voces que te digo que sirven, no innoves una nueva cada vez que hacemos otro"*.) Voz, avatar o herramienta: si ya hay una validada para ese perfil, se usa esa. Si hace falta una nueva, primero una **muestra gratis** y recién con su OK se gastan créditos.
- Antes de mandar una tanda larga a renderizar, **calcular el costo y avisarle**. Si el saldo no alcanza para todo, avisar primero y no quemar el saldo en el primer bloque.

### ⛔ 2026-11-04 · Las imágenes NO se generan con nada que cobre
Santiago, después de que las fotos de avatar del VSL de Monjaro se sacaran en Higgsfield: *"Podes usar mi chatgpt, nano banana, o alguna gratuita, no uses nada que cobre"*.
- **Higgsfield queda fuera para imágenes.** Gastó 4 de los 4,35 créditos que quedaban en cuatro fotos de avatar (GPT Image 2, calidad media, 1 crédito c/u; en alta son 3,5).
- **El orden para cualquier imagen es:** 1) **su ChatGPT** desde Chrome, con su sesión (es lo que él usa: la foto buena de la Abuela Mei salió de ahí); 2) **Nano Banana en aistudio.google.com**, también por navegador; 3) cualquier otra gratuita. **Nunca** un servicio que descuente créditos sin que él lo pida.
- ⛔ **La API de Gemini NO genera imágenes gratis.** Probado el 4/11 con `gemini-2.5-flash-image`, `gemini-3.1-flash-image`, `-lite` y `-preview`: los cuatro devuelven **429 con `limit: 0`** sobre `generate_content_free_tier_requests`. El tier gratis da cuota de texto y de **TTS** (por eso la voz sí sale por API), pero **cero** de imagen. Nano Banana solo sirve **desde el navegador**. El cliente quedó escrito igual por si algún día se habilita.
- Vale para avatares, B-rolls, tapas, mockups y placas. Las placas y los chats de WhatsApp siguen saliendo por código + Chrome headless, que no cuesta nada.
- **GPT Image 1.5 ya no existe en Higgsfield** (ahora GPT Image 2 y 2.5): los prompts de avatar viejos que lo nombran hay que leerlos como referencia de parámetros, no de modelo.

## Prioridad de reglas
- **Cuando un prompt de `RAW/prompts/` choca con tus reglas personales, ganan tus reglas** ([[guiones-y-anuncios]]: no catastrófico, sin precio en el ad, natives sin cara, voseo). Del prompt tomo la estructura, no lo que contradice tus preferencias.

## Estándar de copy ([[filosofia-de-marketing]])
- **Nada de "frases de IA"**, copy genérico ni tono de anuncio de TV. La vara: "guiones asesinos de verdad".
- Vender **transformación**, no características.
- **"Verdad, no consuelo":** señalar puntos ciegos y contradicciones sin endulzar ([[ia-en-el-flujo-de-trabajo]]).
- **Variar un ganador:** primero diagnosticar por qué funciona y después variar en las 6 categorías de [[guiones-de-video-ads]].
- **Largo máximo: 1:30 por video** (regla fija del 2026-10-22), unas 225 palabras. Vale aunque el ganador que modelamos corra videos de 2 o 3 minutos ([[guiones-y-anuncios]]).
- **Tamaño de tanda: máximo 6 videos, nunca más** (regla fija del 2026-10-22). Si el análisis da más ángulos, elijo los 6 mejores y el resto queda como banco al final del archivo. Para llenar un conjunto V3 se completa con natives o renovaciones de hook, no con más guiones ([[metodo-v3]], [[guiones-y-anuncios]]).
- **"Renovar" un ganador** = hooks nuevos sobre el mismo cuerpo, no un guión nuevo. **Se entrega como 6 guiones completos** (hook nuevo + cuerpo validado), nunca como una lista larga de hooks sueltos; el resto queda de banco (regla del 2026-10-26, [[renovacion-de-creativos]]).
- **Prompts de video:** reglas fijas de UGC por defecto (9:16, handheld, sin subtítulos, sin música). Testimonios de 14 s y 35–40 palabras ([[ugc-y-video-generativo]]).
- **Upsells y bonus: solo PDF** (ebook, checklist, plantillas, swipe). Nada de videocursos, porque no los graba ([[biblioteca-de-prompts]]).
- **Volumen:** el ritmo de testeo es de ~10 creativos por día. Si pide "más", entregar tandas que alcancen para eso, con formatos rotados.

## Carpetas en el Escritorio (regla fija, 2026-10-22)
- Cada oferta nueva va en **una sola carpeta** `~/Desktop/<oferta>/` con tres subcarpetas: `imagenes/`, `landing/` y `anuncios/`. Nada suelto en el Escritorio.
- Imágenes de landing, tapas y mockups van a `imagenes/`. HTML, .txt para ImpulTienda y PRUEBA.html, a `landing/`. Videos, guiones, natives y descripciones de ads, a `anuncios/`.
- Santiago: "siempre así lo quiero, para que no dejes cosas sueltas en mi escritorio".
- **Los videos terminados se entregan en el Drive, no en el Escritorio** (2026-11-13: *"Metela en el drive siempre, no quiero mas en el escritorio"*; reconfirmado el 2026-11-14: *"Acordate lo del drive, guardalo como regla así no lo tengo que repetir más"*), en `Mi unidad / Ebook Dami / Ebook <Oferta> (<MERCADO>) / Videos terminados`, con cada video nombrado por el arranque de su hook. **Vale para toda tanda, sin preguntar y sin que lo pida**; el Escritorio queda como taller (`work/`). Detalle en [[organizacion-y-registro]].

## ⛔ Los videos van al Drive SIEMPRE, y el peso no es excusa (REGLA FIJA, 2026-11-17)
Santiago, después de que le entregara los 6 de [[tarot-2-dias]] diciendo que no entraban por el límite del conector: *"Metelos en el drive, pone como regla obligatoria meterlos en el drive siempre, siempre pones la excusa del peso y desp los subis, metelos"*.
- **Toda tanda terminada sube al Drive, sin preguntar y sin excepciones.** No se entrega una tanda avisando que "quedó en el Escritorio".
- El conector de Drive y el uploader de Chrome cortan en **10 MB**. Eso **no es un motivo para no subir**: es un paso más del trabajo.
- **Cómo se resuelve:** se recomprime cada video con **x264 en dos pasadas**, `-preset veryslow`, apuntando a **9,3 MB** (`bitrate = (9.3*8192)/duración - 130 kbps`, audio AAC 128k). Verificado el 17/11 en un video de 56 s: de **42 MB a 9,2 MB** con la imagen **indistinguible** al comparar cuadros. Meta recomprime todo lo que subís igual, así que el máster pesado no aporta nada en destino.
- Antes de reemplazar, se **compara un cuadro** del original contra el comprimido. Si se degradó, se sube igual pero se avisa en una línea; no se deja de subir.
- ⛔ **Lo que NO funciona** (probado el 17/11, no volver a intentarlo): servir los videos desde un `http://127.0.0.1` con CORS y hacerles `fetch` desde la página de Drive. Chrome bloquea el pedido **http** desde una página **https** y la promesa queda colgada sin error; el servidor no registra ni una petición. Tampoco hay Google Drive para escritorio en su Mac.

## "La tanda" que sube al Drive son TODOS los creativos, no solo los videos (regla fija, 2026-11-22)
Santiago, después de recibir Laboratorio Wow con los 4 videos en el Drive y los 3 estáticos solo en el Escritorio:
*"no me subiste las fotos al drive"*.
- La regla del 17/11 ("toda tanda terminada sube al Drive, sin preguntar") vale para **todo lo que se entrega
  como creativo**: videos, estáticos, carruseles y natives. No es una regla de videos.
- Estructura: `Ebook Dami / Ebook <Oferta> (<MERCADO>) /` con **`Videos terminados`** y **`Fotos terminadas`** al lado.
- Los estáticos pesan 200-400 KB: van **tal cual, sin recomprimir**, y con **nombre descriptivo**
  (`En que vaso va a flotar el huevo - A o B.jpg`), nunca con la clave de trabajo (`E1`, `E3`).
- 🐞 El conector **solo lee de las carpetas de la sesión**: hay que copiar los JPG al scratchpad antes de
  llamar a `create_file`, igual que con los MP4. Desde `~/Desktop` contesta que el archivo no existe.
- La copia en `~/Desktop/<oferta>/anuncios/` se queda igual: el Escritorio es el taller, el Drive es la entrega.

## Las visuales para el socio son los links de TikTok, no el Drive (regla fija, 2026-11-20)
Santiago, pidiendo las visuales de [[slime-shop-kit]]: *"Mándame los links de los TikToks que usaste para hacer las visuales. No me mandes el link de Drive de los videos. Necesito el link de las visuales de TikTok para pasárselas a mi socio y que él se las pueda pasar a su clave y que pueda hacer los videos con las visuales limpias."*
- **"Las visuales" / "las visuales para mi socio" = la lista de links de TikTok del pool de ese video o de esa tanda.** No son los MP4 terminados ni la carpeta de Drive. El socio y su editor rearman los videos desde cero con las visuales limpias, así que lo que necesitan es la fuente.
- **No se manda el link de Drive** en esa entrega, ni "por si acaso". Los MP4 terminados son otra cosa y van solo cuando pide la tanda.
- Se entrega **en texto plano, un link por línea**, en bloque de código, guardado en `OUTPUTS/AAAA-MM-DD-<oferta>-tiktoks-para-el-socio.md` y al portapapeles con `pbcopy`. Sin tabla ni claves internas (`c07`, `c42`): esos códigos no le sirven a nadie afuera.
- **La lista se verifica contra el render, no se escribe de memoria:** las claves usadas salen de `~/Desktop/<oferta>/anuncios/work/usage.json` y se traducen a URL con `pool_autores.txt` (`cuenta/id` → `https://www.tiktok.com/@<cuenta>/video/<id>`). Si varios videos comparten pool, se dice en una línea.
- Se avisan **las tres cosas que el editor necesita saber**: cuántas cuentas distintas son (no se repite autor en cortes contiguos), que de cada TikTok sirve **una ventana limpia puntual** y no el video entero, y cuántos clips se cayeron por texto quemado o marca de agua ([[estilo-de-video-ia]]).
- Primera vez aplicado: `OUTPUTS/2026-11-20-slime-shop-kit-tiktoks-para-el-socio.md` (38 links, 28 cuentas).

## Registro y nombres
- Los cambios de presupuesto o de puja que me pases van a `OUTPUTS/AAAA-MM-DD-registro-<oferta>.md` ([[organizacion-y-registro]]).
- Las tandas se entregan con nombres listos: `DD/M - N` ([[nomenclatura-del-metodo]]).

## Formato de respuesta
Directo, sin preámbulos · negritas y emojis de sección · 🇬🇧/🇪🇸 cuando es bilingüe · pocas preguntas · cerrar con el siguiente paso.

## Glosario
| Término | Significado |
|---|---|
| Cazar | Buscar winners en Facebook Ads Library |
| Guión | Ad script |
| Natives | Prompts de imagen UGC en POV |
| Descripción | Copy storytime largo |
| Baratísimo / dirt cheap | Lo que va en lugar del precio |
| DNA ganadora | Estructura o ángulo probado |
| Variables | Versiones nuevas de la misma DNA |
| Low ticket | Producto digital de $14 a $27 |
| OTO | Upsell después del pago |
| **BCL / B CL** | **Es "VSL".** Se lo come el dictado por voz. Si pide "un BCL", quiere el **VSL** (el video largo con avatar que va después del quiz). Aclarado el 2026-11-22: *"Es vsl, solo que me lo traduce mal"* |

## Relacionado
[[guiones-y-anuncios]] · [[scented-stones]] · [[perfil-y-negocio]]

## Fuentes
- RAW/2026-10-10-contexto-maestro-santiago.md (secciones 9 y 10)
- RAW/2026-10-10-guiones-ganadores-scented-stones.md (notas de Santiago)

## Si el video pesa más de 10 MB, lo sube él (registro 2026-11-19)
Santiago, al ver que el clon del carozo de palta quedó en 59 MB: *"Dejámelo en la carpeta y lo subo"*.
- El conector de Drive y el uploader de Chrome cortan en **10 MB**, así que lo que suba yo sale recomprimido.
- Cuando la tanda convive en el Drive con videos sin comprimir (los de [[limpia-dolor]] pesan 35-63 MB),
  **el máster va a `~/Desktop/<oferta>/anuncios/` y lo sube él**, para que no quede uno con menos bitrate
  que el resto de la carpeta.
- **No reemplaza la regla del 17/11**: la tanda sigue yendo al Drive sin preguntar y el peso no es excusa.
  Lo que cambia es que, cuando el máster supera los 10 MB, **se le avisa y se le ofrece** dejarlo en la
  carpeta en vez de subir una copia degradada. Si no dice nada, se sube comprimido.

### Cuota de TTS por API (registro 2026-11-19)
El tier gratis da **10 generaciones de TTS por dia y por modelo**. Al agotarse `gemini-3.1-flash-tts-preview`
devuelve **429 "Generate content requests per day limit exceeded"**.
- **El reemplazo que funciona es `gemini-2.5-flash-preview-tts`**: tiene cuota propia y **no lee en voz alta
  el bloque de estilo** (probado el 19/11 con una linea de 20 palabras: 8,9 s, ritmo natural).
- ⛔ **`gemini-3.8-flash-lite-tts` no sirve**: la misma linea le dio **18,1 s**, o sea que lee las
  instrucciones.
- Ojo con el estilo: pedirle *"hablando despacio"* alarga mucho la toma (11,4 s contra 8,9 s por la misma
  linea). Si hay que calzar en un hueco medido, el estilo va **"ritmo normal de conversacion"**.
