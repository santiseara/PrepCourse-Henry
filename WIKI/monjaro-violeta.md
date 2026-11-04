# Monjaro Violeta Japonés

> Oferta nueva para **Argentina**: la receta de una bebida de remolacha ("monjaro natural japonés") con protocolo de 30 días. Se modela del quiz brasileño de **Vovó Mei** (`monja-roxo.lovable.app`), que corre ~37 anuncios activos. Embudo: quiz → VSL → checkout. (fuente: conversación del 2026-11-04)

## Ideas clave
- **El original es brasileño y está escalando.** Página de Facebook *Vovó Mei*, ~37 anuncios activos, casi todos videos de 2 a 3 minutos, publicados entre el 9 de octubre y el 3 de noviembre de 2026. Biblioteca de Anuncios: `view_all_page_id=1359437227259333`.
- **Casi todos los anuncios muestran `instagram.com` como destino**: solo dos dejan ver el dominio real (`MONJARO-ROXO.LOVABLE.APP`, con el copy *"Receita Mounjaro / MOUNJARO ROXO JAPONÊS"*). El resto va por el mismo embudo.
- **"MONJARO", no "Mounjaro".** La marca del original está escrita mal a propósito: usa el gancho del fármaco sin escribir su nombre. **Se mantiene** en nuestra versión.
- **El quiz es largo: 68 pasos en el archivo = 34 reales**, duplicados en dos ramas (mujer / hombre) desde la pregunta de género. Nuestra versión son **27 pasos** para mujer (30 si declara una condición de salud).
- **La oferta no está en el quiz.** El último paso del original es solo un VSL; el precio y el carrito viven detrás del player. En el nuestro, la oferta va **abajo del VSL y oculta** hasta `SEGUNDOS_OFERTA` ([[quizzes-reglas-de-armado]] §5).

## Ficha de la oferta
| | |
|---|---|
| Producto | Monjaro Violeta Japonés — protocolo de 30 días |
| Público | **Mujeres y hombres** (el quiz se bifurca por género, igual que el original) |
| Idioma | Español argentino con voseo |
| Precio | **$14.990 ARS**, tachado $49.990 (70% OFF), 3 cuotas de $4.997 *(a confirmar)* |
| Checkout | `https://monjaro-violeta.impultienda.ar/checkout` *(a confirmar)* |
| Avatar | **Abuela Mei** (Vovó Mei): señora japonesa, pelo gris, túnica violeta |
| Mecanismo | La bebida de remolacha tomada en un horario exacto: "trabaja mientras dormís" |
| Promesa | Bajar 10 kg en 30 días (la del original) |
| Regalos | 5 PDFs por un valor declarado de $73.500 |

## El original: `monja-roxo.lovable.app`
- **Stack:** Lovable. El funnel entero viaja **en texto plano** en `assets/routes-*.js` — preguntas, opciones, alertas, testimonios y comparativa. No hace falta recorrerlo en el navegador ([[quizzes-reglas-de-armado]] §3).
- **Las imágenes no son de Lovable:** cuelgan de `media.inlead.cloud/uploads/24117/…`, o sea que el quiz **se exportó de InLead**. Los nombres traen el tamaño (`-xs-`, `-sm-`, `-md-`): las siluetas de tipo de cuerpo son **96×80 px** y no existen en tamaños más grandes (probado `sm`, `md`, `lg`, `xl`, `2x`: todos 404).
- **Los 34 pasos:** objetivo (multi) · género · zona de grasa (multi) · edad · kilos a bajar · nombre · tipo de cuerpo · cómo te afecta (multi) · conformidad · dificultades del día (multi) · **video de la Vovó Mei** · qué te impide · placa "cómo funciona" · beneficios (multi) · testimonio · peso · altura · peso deseado · rutina (multi) · sueño · agua · frutas (multi) · análisis · **resultado con IMC + alerta** · condición de salud (sí/no → campo → análisis → mensaje) · ~~WhatsApp / e-mail~~ · cuerpo soñado · análisis · antes/después · **VSL final**.
- **Dos players distintos:** el del paso 11 (`6ab0462b14e8c28e3b7cd846`) y el del paso final (`6ab046138aae747f61704d5e`), los dos de la cuenta `cd0d2f60-1b53-4b39-8198-42435c3310fd`.
- **Cinco alertas de IMC**, una por franja, y la barra va de verde a rojo con la bolita en la franja que corresponde.

## Qué se adaptó y qué no
| Original | Nuestro | Por qué |
|---|---|---|
| Los 34 pasos, su orden y su lógica | **Igual** | [[quizzes-reglas-de-armado]] §2 |
| "Onde prefere receber seu plano?" + WhatsApp + e-mail (4 pasos) | **Sacado** | Regla fija: los datos de contacto se piden en el checkout (registro del 2026-10-15) |
| `MONJARO ROXO JAPONÊS` | **MONJARO VIOLETA JAPONÉS** | "Roxo" no significa nada en castellano. La marca mal escrita se mantiene |
| Vovó Mei | **Abuela Mei** | — |
| Maria Conceição – Porto Alegre, RS | **Mariela Benítez – Rosario, Santa Fe** | Localización ([[quizzes-reglas-de-armado]] §2) |
| "Morango", "Abacaxi", "Maça" | **Frutilla, Ananá, Manzana** | Argentino, no neutro |
| Audio del testimonio (en portugués) | **Sacado** | No se puede reusar un audio en otro idioma y no vale la pena grabarlo para un paso intermedio |
| Infografía "COMO FUNCIONA" con texto quemado en portugués | **Placa de 3 pasos en HTML** | §4: los bloques de texto van en HTML nítido, no como imagen |
| Siluetas de tipo de cuerpo de 96×80 px | **Tarjetas con emoji y descripción** | §4: si faltan varias fotos del set, la pregunta va con íconos. No hay versión grande de esas siluetas |
| Paleta violeta del original | **Igual**, en oscuro (violeta #8A1FC4 + magenta #E626C8) | El original ya es violeta: no hay nada que recolorear |
| Sin oferta en el quiz | **Caja de oferta completa** estilo launch promotion | §4, corrección del 2026-11-03 |

## Imágenes
- **27 webp, 458 KB en total.** El `.txt` con todo embebido pesa **679 KB**, bien abajo del límite que aguanta ImpulTienda.
- **Reusadas tal cual:** las 4 parejas de edad, las 4 balanzas, las 6 frutas, los cuerpos de zona, las comparativas de hombre y mujer, los antes/después y la cara de la Abuela Mei.
- **Limpiadas:** los recortes con alfa sucio (bordes dentados) se pasaron por un umbral de alfa 110 + recorte al bounding box.
- **Rehechas con Pillow:** las chapas verdes de género (`MULHER` → **MUJER**, `HOMEM` → **HOMBRE**), con Arial Black sobre el mismo verde #039E00.
- **La portada** (`hero-monjaro.webp`) es el arte del original **sin el cartel en portugués**: se recortó la banda de arriba (jugo, remolachas, torii y la cara de la Abuela) y se le puso un **alfa en diagonal** que la funde con el fondo de la página. El lockup "MONJARO / VIOLETA / JAPONÉS" se rehízo **en HTML con CSS**, así queda nítido y editable.

## El VSL del original (bajado y transcripto el 2026-11-04)
Los dos videos del embudo salen del player de **ConverteAI/VTurb** (cuenta `cd0d2f60-1b53-4b39-8198-42435c3310fd`). El `player.js` de cada uno trae el **id del video** adentro, y el master está en `https://cdn.converteai.net/<cuenta>/<video>/main.m3u8`, sin autenticación. Bajan con ffmpeg y `-c copy`.
| | Player | Video | Dura |
|---|---|---|---|
| VSL del último paso | `6ab046138aae747f61704d5e` | `6ab045f46b009725a74f6379` | **2:29** · 404x720 |
| Video corto del paso 11 | `6ab0462b14e8c28e3b7cd846` | `6ab046178aae747f61704d70` | **1:39** · 202x360 |

- **El VSL es cortísimo: 2:30 y 431 palabras** (~172 ppm). Nada que ver con los 18 minutos del VSL de Calistenia Militar: acá la venta entera entra en dos minutos y medio.
- **Lo hablan dos personajes, y el 70% del video no es la experta:**
  1. **0:00–0:11 · Abuela Mei** (la experta) felicita y dice que el plan personalizado ya está armado con las respuestas del quiz. Es el puente desde el quiz.
  2. **0:11–1:58 · la testimonial**, una mujer rubia de unos 50 con anteojos, filmada en **su cocina real lavando los platos**, formato UGC casero. Todo el cuerpo del VSL es su testimonio.
  3. **1:58–2:30 · vuelve la Abuela Mei** para la garantía, la frase bandera y el CTA.
- **Los 10 beats del testimonio:** la panza que no se iba · conoció el método hecho a medida · ingredientes que ya tenía en casa y 8 kg en 15 días · la autoestima · "pensé que era complicado y se hace en minutos" · "estaba con el pie atrás, ya había caído en promesas falsas" · qué incluye · precio único y sin mensualidad · el anclaje de la consultoría · la lista de alimentos que frenan el metabolismo.
- **Visual:** la experta en una cocina rústica con estantes de frascos de barro, delantal marrón y colgante de jade, con el vaso de jugo y la remolacha sobre la mesada. B-rolls de la bebida sirviéndose, limón, ananá, jengibre y clips reales de antes/después. **Subtítulos de una sola palabra, en amarillo con borde negro, a la altura del pecho** (igual que el VSL de Calistenia Militar: amarillo sobre blanco, sin franja).
- **El CTA es una placa amarilla con una flecha roja** que baja: *"PEGAR MEU PLANO"*.
- **El video corto del paso 11 (1:39)** es la presentación de la experta: nombre, credencial de medicina tradicional japonesa, las seguidoras, por qué hay que contestar las preguntas (no existe la misma receta para dos mujeres distintas) y el mecanismo (el "fuego digestivo", drenar líquidos, desinflamar el intestino).
- Transcripciones completas: `OUTPUTS/2026-11-04-transcripcion-vsl-monjaro-original.txt` y `OUTPUTS/2026-11-04-transcripcion-mei-corto-original.txt`. Los MP4 quedaron en `~/Desktop/monjaro-violeta/vsl/`.

## Nuestro VSL (2026-11-04)
- **2:41 y 553 palabras**, en tres bloques de HeyGen: Abuela Mei (50 palabras) → Mariela, la testimonial (382) → Abuela Mei (98). Guion: `OUTPUTS/2026-11-04-vsl-monjaro-violeta-guion.md`.
- **Mismo esqueleto que el original, beat por beat**, con la oferta nuestra adentro.
- **El acompañamiento se mantiene, porque Santiago lo tiene** (2026-11-04). En la primera versión lo saqué por la regla de Tai Chi ("el soporte por WhatsApp no lo tenemos") y él corrigió: *"Si tenemos todo eso que sacaste, no lo saques, lo tenemos"*. Vuelven el **seguimiento individual por WhatsApp**, el **grupo cerrado**, los **menús personalizados**, los **ejercicios en casa** y la **consultoría con la Abuela Mei**. Regla: lo que tiene una oferta no se deduce de otra oferta — se pregunta.
- **El anclaje es el mismo que el del original**, convertido: "una consulta con ella sale más de **ciento veinte mil pesos**" (en el original, R$ 700).
- ⚠️ **Pendiente de confirmar:** la consultoría la promete **la Abuela Mei**, que es un avatar. Hay que definir si la atiende el equipo (y entonces el texto dice "con el equipo de la Abuela Mei") o si Santiago la hace él.
- ⛔ **La oferta del quiz NO se toca** (2026-11-04). Alineé la caja del quiz con lo que dice el VSL y Santiago cortó: *"Dejala así tal cual como está, no le cambies nada a lo que ofrece"*. La caja queda con sus **5 regalos y $73.500**. El VSL puede nombrar cosas que la caja no lista; la caja es la que manda y no se edita sin que lo pida.
- **La entrega es por mail**, no por WhatsApp (el quiz no pide WhatsApp).
- **La testimonial es la misma Mariela Benítez del quiz**, con los números alineados: 8 kilos en los primeros 15 días y 16 en total.
- ✅ **`SEGUNDOS_OFERTA` = 114, medido sobre el video terminado** (ya no es una cuenta de palabras): Mariela dice "catorce mil novecientos noventa pesos" en el segundo **114,10**, o sea el **1:54**. Ya está puesto en los tres archivos del quiz.
- **Hacen falta dos avatares**, uno por personaje: `OUTPUTS/2026-11-04-prompt-avatar-abuela-mei.md` y `OUTPUTS/2026-11-04-prompt-avatar-mariela.md`. Los dos con fondo liso y vacío: la cocina del original entra por B-roll, no por la foto del avatar.
- ⛔ **Sin "mi flor"** (2026-11-04). Era `minha flor` traducido literal del original; Santiago lo sacó: *"queda raro eso… las cosas raras las sacamos"*. Regla general en [[vsl-reglas-de-armado]].

### Voces del VSL (elegidas el 2026-11-04)
| Personaje | Voz | Modelo | Por qué |
|---|---|---|---|
| **Abuela Mei** (bloques 1 y 3) | **Vindemiatrix** | `gemini-2.5-flash-preview-tts` | Elegida por Santiago entre tres muestras maduras. Son **dos mujeres hablando una atrás de la otra**, así que no podían compartir voz. |
| **Mariela**, la testimonial (bloque 2) | **Sulafat** | idem | La voz femenina fija de la casa. |
- **El style no envejece una voz.** Se probó un style forzado ("voz gastada, temblor, le falta el aire") sobre Gacrux y el oyente la bajó de 50-60 a **40 años**: el motor la hace más suave, no más vieja. Con el TTS de AI Studio **50-60 es el techo** para una abuela de 72; para más hay que ir a voz clonada.
- Descartadas: **Gacrux** (grave y pausada, la segunda mejor) y **Achernar** (suave y aireada). Las tres dieron rioplatense limpio y ninguna leyó el style en voz alta.

## Estado
- ✅ **Quiz entero armado y probado en el navegador** (2026-11-04): `~/Desktop/monjaro-violeta/`.
  - Probados: portada, multi-select, bifurcación por género, fotos de edad y kilos, campo de nombre con `{{nombre}}`, placa de cómo funciona, testimonio, los 3 medidores, la pantalla de carga, el **IMC con la bolita en la franja correcta** (82 kg / 1,65 m → 30,1 → Obesidad → bolita al 90%), la rama de condición de salud (campo → carga → mensaje personalizado), la comparativa y la oferta entera con contador, cupos y notificaciones.
  - **Textos sensibles al género** con el token `{{o}}`: "¿estás list**a**/list**o**?", "Quedate tranquil**a**/**o**", "List**a**/List**o**, Ana".
  - Atajos de prueba: `?oferta=1` va directo a la oferta y `?paso=N` arranca en el paso N.
- ✅ **VSL TERMINADO** (2026-11-04): `~/Desktop/monjaro-violeta/vsl/VSL-monjaro-violeta.mp4`, **3:17, 1080×1920, 150,7 MB**.
  - Tres bloques de HeyGen **Avatar IV**: Abuela Mei 0:18 → Mariela 2:23 → Abuela Mei 0:36. **Costó 39 créditos** de los 3.224 (~17 por minuto; la cuenta de 25/min sobrestimaba).
  - **Los dos avatares los generó Santiago con su ChatGPT** desde los prompts entregados, y se recortaron a 9:16 exacto. En `vsl/avatar-abuela-mei.png` y `vsl/avatar-mariela.png`.
  - **Voces de AI Studio con lipsync por audio subido**, no por texto: Abuela Mei con **Vindemiatrix a 160 ppm** (suena a 60-70 años) y Mariela con **Gacrux a 170 ppm** (50-55). Los wav crudos y los `-final` están en `vsl/voz/`.
  - **Verificado:** las 405 palabras del bloque largo están (no se comió la enumeración del acompañamiento), los desfases video/audio son de 0,02 s, no hay silencios de más de 1,5 s y los cortes caen donde deben.
  - A cada bloque se le devolvió el **WAV original** en lugar del MP3 que se subió para el lipsync.
- ✅ **Versión editada** (2026-11-04): `vsl/VSL-monjaro-violeta-EDITADO.mp4`, **2:40, 1080×1920, 166 MB**. Pedido de Santiago: *"metele 1.23 de velocidad… una musica activa bajita… algunos brolls… subtitulos, efectos de sonido, algunos headlines… Ponele onda, no lo llenes de cosas"*.
  - **1,23x** (3:17 → 2:40). Medido: la abuela baja de 45-55 a **40-50 años**. Compensar el tono lo empeora (35-45), así que va con `atempo` limpio.
  - **Música propia activa** (`OUTPUTS/scripts-vsl/music_activa.py`): 96 BPM, shaker, kick, marimba y pad, sin melodía. A **-24 dBFS con sidechain**: baja sola bajo la voz.
  - **5 B-rolls de ~3 s** de los que pasó Santiago, todos del tercer clip: remolacha, el agua a la licuadora, pelar remolacha, manzana y jengibre, el colado.
  - **4 headlines** en magenta sobre los números de la oferta, **subtítulos** de a dos palabras con clave en dorado, y **un whoosh** al entrar a cada B-roll (`sfx_whoosh.py`).
  - Editor: `OUTPUTS/scripts-vsl/edit_monjaro.py`.
- ⏳ **Falta subirlo a Panda Video** y pegar el embed en `<template id="vsl-template">`. Sube la versión **EDITADA**. Cuando esté, el embed de Panda va en `<template id="vsl-template">` y **`SEGUNDOS_OFERTA` pasa de 230 a 101**.
- ⏳ **Falta el video corto de la Abuela Mei** del paso 11: va en `<template id="vsl-mei">`. **Si queda vacío, el paso se saltea solo** y el quiz sigue funcionando.
- ⏳ Falta confirmar **nombre del producto, precio y link de checkout**.

## Aviso de riesgo (anti-bloqueo)
La landing arranca con **"bajá 10 kg en 30 días"**, usa **antes y después** y el nombre de un fármaco deformado. Son justo las tres cosas que [[protocolo-chia-28d]] marcó como motivo de rechazo en Meta **aunque el guion del anuncio esté limpio**, porque Meta revisa el destino. Se dejó igual al original por fidelidad (§2), pero conviene tener a mano una versión de la portada sin kilos ni plazo ("Tu plan de 30 días con lo que ya hay en tu cocina") por si rebotan las cuentas.

## Preguntas abiertas
- ¿El producto se llama **Monjaro Violeta Japonés** o le ponemos otro nombre?
- ¿El precio es $14.990 o va otro? ¿El checkout es `monjaro-violeta.impultienda.ar`?
- ¿Metemos el video corto de la Abuela Mei en el paso 11 o lo dejamos fuera?
- ¿Los 5 regalos quedan como están o los cambiamos antes de escribir el VSL?

## Relacionado
[[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[protocolo-chia-28d]] · [[secreto-de-la-insulina]] · [[tai-chi-fit]] · [[vsl-reglas-de-armado]]

## Fuentes
- Biblioteca de Anuncios de Meta, página **Vovó Mei** (`view_all_page_id=1359437227259333`), consultada el 2026-11-04
- `https://monja-roxo.lovable.app/` y su bundle `assets/routes-5Qd2Kwpp.js`
- Entregables: `~/Desktop/monjaro-violeta/` y `OUTPUTS/2026-11-04-quiz-monjaro-violeta.html`
