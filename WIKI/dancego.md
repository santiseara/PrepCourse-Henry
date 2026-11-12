# DanceGo

> Oferta nueva AR: bajar de peso bailando en casa, 10 minutos por día. Quiz de 35 pasos clonado de `funilv1.appdancego.com` (BR), pasado a español argentino y **despintado**: el original es un arcoíris y acá va papel crema + tinta + un solo acento.

## Ideas clave
- **El original es brasileño y corre con tráfico de Facebook** (`funilv1.appdancego.com`, llega con `fbclid`, `fbp`, `fbc` y `utm_source=l.facebook.com`). Producto: app con +100 clases de baile, desafío de 28 días, comunidad de WhatsApp. Precio BR: **7× R$ 6,26 o R$ 37,90 al contado**, tachado R$ 197.
- **El mecanismo es el gancho**: "el baile quema 140% más calorías que los ejercicios tradicionales y aburridos" + "aunque no sepas bailar". El avatar es mujer que **no va al gimnasio y le da vergüenza**.
- **El original es largo a propósito** (35 pasos): mucha pregunta de personalización, dos pantallas de carga, un resultado con IMC y una previsión con fecha. La oferta está al final, sin VSL.
- Lo que pidió Santiago el 2026-11-04: *"Mejoramelo, no quiero que se vea recontra colorido, quiero que las imágenes se vean bien."*

## Qué se cambió del original
| | Original | Nuestro |
|---|---|---|
| Paleta | degradé rosa→violeta→amarillo en barra, títulos palabra por palabra de 4 colores, botones amarillo chillón | papel crema `#FBF8F4`, tinta `#1C1A19`, **un** acento frambuesa `#B23A5B`; verde `#216B4F` solo para "bien"/comprar, rojo solo para riesgo |
| Fotos de edad | las mismas fotos, tapadas con un overlay de degradé rosa/violeta/verde/naranja | las mismas fotos **sin overlay y con recorte apretado a la cara** (720×960, 3:4), con la edad sobre una banda oscura encima de la foto |
| Paso de estilos de música | swipe de 7 tapas neón hechas con IA | **sacado entero** (Santiago, 2026-11-04) |
| Comunidad de WhatsApp y perfil de Instagram | capturas de pantalla pixeladas | **armadas en HTML** (burbujas de chat y ficha de perfil) |
| Maqueta de la app | captura del celular con la UI en portugués | **el celular dibujado en HTML/CSS**, con los textos en castellano |
| Ritmos | Sertanejo universitario, Funk brasileño, Gospel | **Cumbia, Cuarteto, Salsa y bachata** (los otros 4 quedan) |
| Paso de e-mail | pedía e-mail antes del nombre | **sacado** (los datos van en el checkout) |
| Largo | 35 pasos | **26 pasos** (ver abajo) |

## Detalles / notas
- **Stack del original: Lovable + Supabase propio.** El bundle (`assets/index-*.js`) trae el panel de administración y las imágenes, pero **el contenido del quiz vive en la base** (`funnel_steps`, `funnel_elements`, `products`…): no está en texto plano. Se saca recorriendo el quiz en Chrome y leyendo `img.src`/`alt` paso a paso.
- Las 81 imágenes cuelgan de `/lovable-uploads/<uuid>.png` y **están todas listadas en el bundle**: se bajan de una y se miran juntas en una hoja de contactos.
- Precio nuestro (provisorio, en el `CONFIG`): **$14.990**, tachado $49.990, 70% OFF, 3 cuotas de $4.997, bonos por $38.900.
- **Checkout confirmado por Santiago el 2026-11-04: `https://dancego.impultienda.ar/checkout`.** Los 4 CTAs del último paso (los tres botones "Comprar ahora"/"Quiero empezar ahora" y la chapita **HOY: GRATIS**) salen todos de ahí, con los UTM pegados. Ver la regla del 2026-11-04 en [[quizzes-reglas-de-armado]].
- El quiz **no lleva VSL** por ahora: `SEGUNDOS_OFERTA: 0` y la oferta se ve de entrada, como el original. Si se le carga un VSL en `<template id="vsl-template">`, con poner los segundos la oferta se esconde sola.

## Portada (2ª versión, 2026-11-04)
- Chapita oscura **+155 mil mujeres bailando** con un punto verde, titular a 2.05rem y las 4 fotos a sangre con la edad encima.
- Las 4 fotos son las mismas del original, **recortadas apretado**: antes la persona ocupaba un tercio de la tarjeta y las cuatro parecían la misma mujer. Ahora se distinguen las edades.
- Se revisaron las carpetas de las otras ofertas buscando un set de edades mejor y **no hay**: las de [[monjaro-violeta]] son parejas sobre negro a 300 px.
- En un teléfono de 390 px, la portada entera (chapita + titular + las 4 fotos) entra en la primera pantalla: 677 px de 798.

## Los 9 pasos que se sacaron (2026-11-04)
De 35 a **26**. Fuera:
- **Estilos de música** (swipe de 7 ritmos) — pedido de Santiago
- **Bloque de hábitos**: agua, sueño, rutina de trabajo, qué tan activa y niveles de energía — no cambian el resultado, y con energía se fue el emoji de pilas (🔋🔋🔋) que se veía mal
- **"Elegí tu nivel en el baile"** — duplicaba "¿probaste alguna actividad de baile antes?"
- **La edad exacta** (slider, después del resultado) — ya se pregunta en la portada
- **"¿Hace cuánto estuviste en el mejor cuerpo de tu vida?"** — no personalizaba nada

Quedan los que **personalizan el resultado** (objetivo, físico de hoy, cuerpo deseado, metabolismo, experiencia, frecuencia, duración, lesiones, altura, peso, meta) y los de **compromiso emocional** (eventos, motivación, evento próximo, confianza), más los puentes, la nota, el resultado y la previsión.

## Radiografía de los ads del original (2026-11-06)
Página de Facebook **DanceGo**, `page_id 964798933379484`: **31 ads activos**. Los 4 más viejos están en circulación desde el **7 de enero de 2026** — diez meses corriendo. Es una ballena.

**El guion que aguanta diez meses es uno solo.** Cuatro creativos distintos (dos presentadoras, dos edes) dicen exactamente el mismo texto, palabra por palabra:
1. *"¿No te gusta el gimnasio y querés bajar de peso divirtiéndote?"* — apertura por objeción
2. *"Dejame presentarte la app DanceGo"*
3. *"Más de 100 entrenamientos para hacer en casa"*
4. *"Clases de baile para principiantes con paso a paso, entrenamientos avanzados y clases en vivo todas las semanas"*
5. *"Todo desde la comodidad de tu casa, de tu living"*
6. **El mecanismo:** *"Yo conecto la app a la tele y empiezo a bailar"*
7. *"Pierdo calorías y encima me divierto"*
8. **La frase que está en TODOS sus ads:** *"La primera semana lo vas a sentir. La segunda lo vas a ver. La tercera lo van a ver los demás."*
9. *"¿Y sabés qué es lo mejor? Sin anualidad, sin mensualidad"*
10. Comunidad de WhatsApp con tips diarios de alimentación y entrenamiento, otras alumnas, clases en vivo
11. CTA: *"Tocá acá abajo. Pero tocá ya, que te estoy esperando para bailar juntas."*

**Los 4 formatos que corren en paralelo:**
| Formato | Largo | Qué es |
|---|---|---|
| **A · UGC + b-roll** (el de los 4 más viejos) | 78–82 s | Creadora a cámara en su living con la tele de fondo, cortes a clase de baile y a mujeres bailando en casa, placas de beneficio, progreso "Día 1 / 9 / 16 / 25" con la panza y la creadora en PIP, cierre en negro con **CLIQUE EM SAIBA MAIS** en amarillo y flecha roja |
| **B · clip crudo + banda** | 37 s | **Un solo clip sin cortes** de una mujer bailando de espaldas frente a la tele, con banda amarilla arriba (testimonio) y banda blanca abajo (*"¿Querés aprender? Tocá Saber más"*). Sin voz en off. El más barato de producir |
| **C · voz en off rápida** | 48 s | Cortes cortos, placas de una palabra con transición de fuego (PREGUIÇA, FALTA DE AUTOESTIMA, VERSÃO), pantallas de la app, comunidad, comida. Ángulo emocional: *"cada paso es una victoria contra la pereza y contra la falta de autoestima"* |
| **D · split PIP** | 60 s | Pantalla partida (b-roll arriba, presentadora abajo), antes/después, íconos de comunidad, botón rojo **SAIBA MAIS!** fijo en el último tercio |

**Lo que se copia de su edición:** banda de hook de dos líneas arriba desde el cuadro cero, placas de beneficio ancladas a la palabra que las nombra, la pantalla de la app y la comunidad de WhatsApp como insertos, subtítulos bajos de pocas palabras con la palabra activa resaltada, y una placa de cierre con el CTA y la flecha. **Lo que no se copia:** la paleta arcoíris; las placas van en el frambuesa de nuestra landing (ver [[guiones-y-anuncios]]).

## Tanda 1 de ads (2026-11-06)
Tres renovaciones de voz en off con la DNA del ganador, cada una con hook, cuerpo y CTA propios (no se repite una sola frase entre las tres, aunque el original sí repita):
1. **El gimnasio entra en la tele de tu living** — objeción del gimnasio + el mecanismo de conectar la app a la tele + la escalera de las tres semanas + sin mensualidad.
2. **Diez minutos mientras se hace la cena** — facilidad y constancia: el desafío de 28 días personalizado, el registro de peso, los ritmos.
3. **En tu casa nadie te ve aprender** — vergüenza y autoestima: bailar como diversión, la comunidad de WhatsApp y la garantía de 7 días.

- Voz **Sulafat** por API (`gemini-3.1-flash-tts-preview`, porque el 2.5 dio 429), acento rioplatense verificado, `speed 1.30`.
- **Visual 100 % TikTok:** clips bajados de `#bailoterapia` y `#zumbaencasa`; en `work/tiktoks/` quedaron **29** y **26 entraron al corte** (los 3 ads comparten el mismo pool: cambia el guion, la voz, el seed del orden de cortes y el color de las placas). Reparto real: **19 de clase grupal de bailoterapia / rumbaterapia + 7 del plano firma** (mujer bailando sola en el living). El plano firma es el que escasea: si se arma otra tanda, hay que cazar living, no salón.
- **Los clips son largos** (la mayoría de 60 s): cada uno aporta 4 o 5 ventanas de 4 s, por eso con 26 alcanzó para los 3 ads sin repetir un plano. Las cuentas que más aportaron: **@karlagaviria6** (6 clips), **@vibrafit7** (3), **@pao_c_music_baila** (2, y uno de ellos es el más visto del pool con 26,5 M).
- **Listado completo con link de TikTok, cuenta, qué se ve y tramos usados** en `OUTPUTS/2026-11-07-visuales-tiktok-dancego.md` y en `~/Desktop/dancego/anuncios/visuales-tiktok.md` (se armó para pasárselo al socio).
- Inserts dibujados por código con `OUTPUTS/scripts-vsl/gfx_dancego.py`: la pantalla de la app (desafío día 11 de 28 y los ritmos) y el grupo de WhatsApp. **No hace falta que la app exista para lanzar.**
- Scripts: `gen_dancego_plans.py` + `edit_dancego.py`. Entrega en `~/Desktop/dancego/anuncios/` como `6-11 - 1` a `6-11 - 3`, de 45 a 47 s.

## Tanda 2 — los 4 testeos del ganador (2026-11-07)
**El ganador es `6-11 - 1.mp4`** (*"Hay un gimnasio adentro de la tele de tu living y todavía no lo prendiste"*). Santiago, el 7/11: *"ese ad está siendo una locura hoy"*.

**Por qué funciona (diagnóstico antes de variar):** el hook no promete bajar de peso, **le mueve el gimnasio de lugar**: reencuadra un objeto que ya tiene (la tele del living) como la solución, y de un saque mata las tres fricciones del gimnasio — ir, el horario y que la vean. Después destraba la objeción madre ("no sé bailar") con el paso a paso (*"te dicen qué pie mover y cuándo. No hay forma de hacerlo mal"*), cierra con la escalera de las tres semanas y saca el riesgo con el "sin mensualidad".

**Los 4 (`7-11 - 1` a `7-11 - 4`, de 36 a 43 s):**
| # | Tipo | Hook | Qué cambia |
|---|---|---|---|
| 1 | Variable cercana | "Tu living ya tiene todo lo que necesitás para entrenar: una tele y dos metros de piso" | Cuerpo del ganador intacto; entra por el inventario del living |
| 2 | Variable cercana | "El gimnasio al que más vas a ir es el que no te hace salir de tu casa" | Cuerpo del ganador; entra por la objeción del gimnasio |
| 3 | Video nuevo | "El gimnasio más cerca que tenés está a tres pasos del sillón" | Cuerpo propio: el viaje al gimnasio vs. tres pasos, horario propio, los ritmos |
| 4 | Video nuevo | "Esa tele del living laburó toda la semana para que te sientes" | Cuerpo propio: misma tele, misma hora, mismo sillón — cambia la posición, no la rutina |

- **1 y 2 corren con el pool del ganador** (seed nuevo, color de caja distinto). **3 y 4 llevan el living nuevo.**
- Voz Sulafat por API con **`gemini-2.5-flash-preview-tts`** (esta vez no dio 429), `speed 1.30`, verificada con Whisper: arranca por la primera palabra del guion.
- Guiones en `OUTPUTS/2026-11-07-guiones-dancego-tanda-7-11.md`. Planes: `OUTPUTS/scripts-vsl/gen_dancego_plans_7.py`.

### La caza de living nuevo rindió 8 de 67
`#zumbaencasa` desde el perfil de Chrome (tikwm bloquea los listados por hashtag y por usuario con Cloudflare; el endpoint de un video suelto sigue andando). De **67 clips bajados sobrevivieron 8**: el resto es texto quemado, **memes de gatos bailando** (el formato dominante del tag) o splits de estudio. Los 8 están en `work/tiktoks2/` y listados con su ventana en `work/casa2_ok.txt`.
- **Un cartel arriba no siempre se saca con `zoom 1.30`.** El clip `7694458671287356686` salió con el "me 🫶 zumba" cortado a la mitad en el primer cuadro del video 3; con **`zoom 1.52`** quedó afuera. Regla práctica: el zoom tiene que recortar más alto que la posición del cartel (z=1.30 recorta 23 % de la altura, y ese cartel estaba al 25 %).
- **En `gen_*_plans.py`, numerar las claves con `enumerate` sobre un archivo con comentarios desfasa el pool.** Las claves arrancaron en `Z3` y `first=['Z1', 1]` reventó el editor con `StopIteration`. Contador propio, incrementado solo cuando la línea tiene contenido.

## Tanda 3 — tres renovaciones del ganador (2026-11-09)
Sigue mandando el mismo ganador (`6-11 - 1`). La tanda del 7/11 fueron **cuatro declaraciones sobre el mismo objeto** (el living, la tele): eso es cambiar el objeto, no el hook ([[renovacion-de-creativos]], checklist del 27/10). Esta vez van **tres formatos distintos** sobre el **cuerpo validado copiado textual**:

| # | Formato del hook | Hook | Entra por |
|---|---|---|---|
| 1 | Pregunta del cliente | "Lo que más me preguntan es siempre lo mismo: ¿y si no sé bailar?" | la objeción madre |
| 2 | Storytime en primera persona | "Mi primera clase la bailé con la puerta del living cerrada" | la vergüenza |
| 3 | Lista de tres | "Anotá tres cosas que no necesitás para empezar a entrenar hoy" | lo que no hace falta |

- **La estética también cambia**: caja de subtítulo crema sobre tinta / ciruela / petróleo, tres ritmos de corte (`cut` 1.5-2.3 / 2.1-3.2 / 1.6-2.5) y **2, 4 y 3 palabras por placa**. Los tres abren con un plano de living (Z8, Z5, Z7), no con salón.
- **Planos nuevos sin bajar un solo clip**: las ventanas ya revisadas se muestrean con **offset +2 s** y **TOPE 9** en vez de 5. El pool pasó de ~130 a **228 recortes** y las claves no coinciden con las de `usage7.json`, así que el editor prefiere lo no usado. Es la regla del 3/11 de [[renovacion-de-creativos]] aplicada sin revisión nueva de material.
- Voz Sulafat por API con `gemini-2.5-flash-preview-tts`, `speed 1.30`, verificada (rioplatense, lee solo el guion). El verificador de acento ahora pide **`gemini-3.5-flash`**: `gemini-2.5-flash` devuelve 404 ("no longer available to new users") y `gemini-flash-latest` y `gemini-3.8-flash` dieron 503.
- Guiones en `OUTPUTS/2026-11-09-guiones-dancego-tanda-9-11.md`. Planes: `OUTPUTS/scripts-vsl/gen_dancego_plans_9.py`. Entrega: `9-11 - 1` a `9-11 - 3`.

### Dos cosas que hay que mirar cuando se amplía un pool
1. **Una palabra que se repite en el guion mueve la placa final al principio.** El `end` del video 1 estaba anclado a `mirá` y ese guion dice "Mirá cómo es por dentro" en el hook: la placa de cierre arrancó en el segundo 6 y tapó 38 de los 44 segundos. **Regla: la palabra que ancla la placa final se elige entre las que aparecen una sola vez** (acá, `plan`), y se verifica con un cuadro a mitad del video.
2. **Ampliar el pool mete planos que nadie revisó.** Con TOPE 9 entraron recortes nuevos de clips viejos: se revisó el pool entero (228 recortes, 2 cuadros cada uno, en hojas de 45) y **el único veto fue `R1` (`7704573729669451039`): un salón con una piñata colgando, plano lejano y confuso**. El texto quemado de `E1`, `E2`, `I1`, `Z1` y `Z2` **no es problema**: todos llevan `zoom` con `ybias 1.0`, que recorta de arriba justo donde está el cartel.

## Tanda 4 — tres renovaciones leyendo la cuenta (2026-11-10)
Santiago pasó la captura de los 6 conjuntos (todos a $10 menos el 14, ya en $20):

| Conjunto | Formato del hook | Compras | CPA |
|---|---|---|---|
| 13 · *El que todas* | (no es nuestro) | 2 | **$3,63** |
| 14 · *Mas que un* | (no es nuestro) | 2 | **$5,14** |
| 10 · *Anota* | lista de tres | 1 | $6,57 |
| 9 · *Mi primera* | storytime en primera persona | 1 | $6,69 |
| 11 · *Lo que* | pregunta del cliente | **0** | — |
| 12 · *Nadie me habia* | (no es nuestro) | **0** | — |

**Lo que dice la lectura:** de la tanda del 9/11 vendieron **la lista** y **el storytime**; la **pregunta del cliente** vendió cero en 512 personas. Lo concreto y en primera persona rinde, lo meta no. La **frecuencia está entre 1,02 y 1,09**: todavía no hay fatiga de público, así que lo que se renueva es el hook, no el alcance.

⚠️ **Tres de los seis conjuntos corren creativos que no salieron de acá** (*Mas que un*, *El que todas*, *Nadie me habia*) y dos de ellos son los de mejor CPA. No están en las tandas del 6/11, 7/11 ni 9/11. Pedido a Santiago el 10/11; sin ese guion no se puede renovar lo que mejor anda.
⚠️ **No sabemos en qué cuenta publicitaria corre DanceGo.** Se probaron cinco por MCP sin encontrarla; queda pendiente para poder leer gasto, CTR y frecuencia por anuncio en vez de la captura.

**Los tres nuevos (`10-11 - 1` a `10-11 - 3`, de 46 a 50 s), cuerpo validado textual:**
| # | Formato del hook | Hook | Entra por |
|---|---|---|---|
| 1 | Prueba social con cifra | "Ciento cincuenta mil mujeres están bailando en el living de su casa ahora mismo, y casi ninguna sabía bailar cuando empezó" | la cifra de la portada de la landing |
| 2 | Reencuadre del costo | "No te estoy pidiendo que agregues nada a tu día. Te estoy pidiendo que muevas diez minutos de sillón" | el tiempo que ya tiene |
| 3 | Mecanismo emocional | "Lo que me sacó del sillón no fue la fuerza de voluntad. Fue una canción que me gustaba" | la motivación |

- **Estética nueva:** caja de subtítulo **crema sobre frambuesa / tinta sobre crema / crema sobre verde** (el 9/11 fue crema-sobre-tinta, blanco-sobre-ciruela y blanco-sobre-petróleo), cortes de 1,4-2,2 / 1,8-2,7 / 2,2-3,4 y **3, 2 y 4 palabras** por placa.
- **Planos nuevos sin bajar material:** offset de **+0,8 s** sobre las mismas ventanas (el 9/11 fue +2,0), con `usage7.json` penalizando lo ya usado. 231 recortes de 35 clips.
- La placa de cierre se ancla a **`plan`**, que aparece una sola vez en los tres guiones (la regla del 9/11). Verificado: entra a los 44 s de 47,9 en el V3.
- **Control por OCR en vez de hoja de contactos** (`scan_carteles.py`, la herramienta del 10/11): 145 cuadros con texto en los tres videos, todo propio (los insertos de la app y del grupo de WhatsApp, las placas) salvo dos cosas de b-roll que son inofensivas: *"need Jesus"* impreso en la remera de la bailarina del living y un cartel de **RUTA DE EVACUACIÓN** en la pared del salón.
- Voz Sulafat por API con **`gemini-3.1-flash-tts-preview`** (el 2.5 volvió a dar 429), `speed 1.30`, verificada con Whisper.
- Guiones en `OUTPUTS/2026-11-10-guiones-dancego-tanda-10-11.md`. Planes: `OUTPUTS/scripts-vsl/gen_dancego_plans_11.py`.

## Tanda 5 — tres ads con IA hechos con wan2.7 · ❌ RECHAZADA (2026-11-11)
Pedido de Santiago: *"Tenemos que hacer renovaciones para danza, quiero que hagamos ads con IA, con apimart… videos de 4/5 escenas, podés repetir algunas… metele un poco de velocidad, cortá silencios, y que suenen reales… tiene que sonar argentino, no raro. Videos llamativos, de antes y después, de marido sorprendido, juegos con la hija"*.

> ❌ **Santiago los rechazó enteros:** *"salieron súper mal los videos, mal los audios, mal lo visual, se re nota que es IA"*. Se rehicieron con Veo (Tanda 6, abajo). Esta sección queda como registro de lo que no funciona: **avatar `wan2.7-r2v` con voz TTS clonada**. Los tres mp4 quedaron en `~/Desktop/dancego/anuncios/rechazados/`.

**Es el otro carril, no una renovación más de hook.** Hasta acá los 13 ads de DanceGo eran voz en off sobre clips de TikTok. Estos tres son el formato de [[estilo-de-video-ia]]: **escenas actuadas generadas con IA**, una sola voz fija por personaje, sin un solo clip de b-roll. Se hicieron con la skill `antes-despues-ia` ([[skills-de-video-ia]]) por [[apimart]].

| # | Escena | Hook | Entra por |
|---|---|---|---|
| 1 | El marido que la filmaba para reírse | "Mi señora me dijo que iba a bajar de peso bailando en el living de casa. Yo la empecé a filmar para reírme en un mes" | la reacción de un tercero (ángulo validado de [[guiones-y-anuncios]]) |
| 2 | La hija que le pedía que bailara con ella | "Mi hija me pide que baile con ella desde que empezó el jardín. Yo siempre le decía lo mismo: después, mi amor" | la culpa y el juego con la hija |
| 3 | El espejo, cinco semanas después | "Esta soy yo el día que decidí que no iba a pisar un gimnasio nunca más en mi vida" | el antes/después propio |

- **Cuerpo validado del ganador `6-11 - 1` comprimido a 4-5 frases**: conectar la app a la tele, los diez minutos sin que nadie te mire, el paso a paso, la escalera de las tres semanas (video 3) y el "sin mensualidad". El CTA es el mismo: tocar en Más información y responder el test de un minuto.
- **4 o 5 escenas por video y la escena se repite a propósito**: el video 1 usa tres veces el mismo plano del "día 21" (cambia lo que cuenta, no el plano), que es justo lo que hace el ad brasileño de referencia.
- **Velocidad**: el montaje recorta los silencios internos (`pausas [0.26, 0.10]`) y encima va un **×1,05 global** de video y audio. Quedaron en **25,8 / 24,5 / 21,9 s** a 240-260 palabras por minuto.
- **Voz**: Sulafat (mujer) y Orus (hombre) generadas por API a velocidad natural y pasadas como `reference_voice` a wan2.7 — el acento rioplatense no se "pide" en el prompt, **viene pegado a la muestra**. Las 15 tomas dicen el guion exacto (parecido 0,98-1,00 con Whisper) y el voseo aguanta ("tenés que tocar", "arrancás", "bajé").
- **8 imágenes y 18 tomas por US$8,63.** Saldo de ApiMart después de la tanda: US$21,38.
- Guiones en `OUTPUTS/2026-11-11-guiones-dancego-ia-11-11.md`. Proyecto completo en `~/Desktop/dancego/anuncios/ia/{v1,v2,v3}/`. Entrega: `11-11 IA - 1` a `11-11 IA - 3`.
- ⚠️ **Llevan el rótulo "Caso ilustrativo · imágenes con IA"** abajo a la izquierda: las tres mujeres del antes/después no existen. Es la regla 7 de la skill. Si Santiago lo quiere afuera, se saca en el último pase de ffmpeg, pero entonces no se pauta como testimonio real.

### Lo que hay que mirar la próxima vez
- **La muestra de voz de referencia no puede pasar de 10 s**: con 11 s wan2.7 devuelve `duration should be at most 10s` (la tarea sale `refunded`, no cobra).
- **El tono de wan se mueve entre tomas aunque la voz de referencia sea la misma.** Con `tono.py` (F0 mediano por toma) salieron tres fuera de ±8 %: regenerar la toma cuesta **US$0,53** y salió más barato y más limpio que montar seed-vc. Al marido le tomó dos intentos quedar parejo (+24 % → -1,6 %).
- **Una placa anclada a la última palabra no llega a verse** (el fade de entrada dura 0,18 s): la de "semana 3" estaba en *demás.* y había que anclarla en *tercera*.
- **Las palabras que el subtítulo convierte en cifra no sirven de ancla**: *diez* ya no existe en el timeline, es *10*.
- **Las placas se pisan con la etiqueta del día** (que vive en y=330): van en y=170. Y en los planos cerrados a cámara tapan la cara: ahí van abajo, entre el subtítulo y el botón (y 1360-1560).

## Tanda 6 — los tres ads rehechos con Veo (2026-11-12)

Misma idea que la tanda 5 (el marido, la hija, el espejo) pero generada con **Veo 3.1 Fast**, que **actúa el diálogo él mismo**: el texto va dentro del prompt y el audio sale del propio modelo, sin TTS ni voz clonada. Es la [[estilo-de-video-ia]] Regla 0 y es lo que hace que suene a persona y no a avatar.

| # | Escena | Largo | Placas |
|---|---|---|---|
| 1 | El marido que la filmaba para reírse | 28,7 s | DÍA 01 → DÍA 21 |
| 2 | La hija que le pedía que bailara con ella | 30,6 s | DÍA 01 → DÍA 30 |
| 3 | El espejo, cinco semanas después | 31,1 s | DÍA 01 → SEMANA 05 |

- **5 tomas de 8 s por video**, recortadas a lo hablado, con los silencios internos achicados y **×1,08** de video y audio juntos. El cuerpo sigue siendo el del ganador `6-11 - 1`.
- **El antes/después se ve dentro del plano**: el "día 21" se genera **editando el cuadro del día 01** (misma pieza, mismos muebles, misma persona), así el único cambio es el cuerpo. El video 1 repite ese plano tres veces.
- **Lo barato salió caro:** la tanda rechazada con wan2.7 costó **US$8,63**; esta, con Veo, **US$3,02** (18 imágenes + 20 tomas, incluidas 6 regeneraciones). Saldo después: **US$18,35**.
- **Las líneas van con tildes.** Sin tilde, Veo dijo "tienes" en vez de "tenés" en **las tres tomas de cierre**, y en una se inventó una dirección web. Con tilde salió bien a la primera.
- **Los números raros se esquivan**: "veintiún días" lo leyó *veintiuno días*; se cambió por "tres semanas" (la placa igual dice DÍA 21).
- **El filtro de Veo bloquea el contacto físico con un chico** (la mamá haciendo girar a la nena de las manos). Reescrita sin contacto, salió. Esas tomas no se cobran.
- Guiones en `OUTPUTS/2026-11-12-guiones-dancego-veo.md`. Proyecto en `~/Desktop/dancego/anuncios/veo/{v1,v2,v3}/`. Entrega: `12-11 Veo - 1` a `12-11 Veo - 3`.
- ⚠️ Siguen con el rótulo **"Caso ilustrativo · imágenes con IA"**: las tres mujeres no existen.

## Tanda 7 — cuatro ads mas con Veo: dos antes/despues y dos situaciones argentinas (2026-11-12)

Pedido de Santiago: *"Necesito que hagamos mas ads con IA para danza, quiero 4 hoy, el video del antes y desp le fue muy bien, asi que quiero que 2 sean con ese mismo formato, distintos, pero asi. Y los otros dos quiero que sean situaciones mas argentinas, y que llamen la atencion, acordate que hay que meter varias escenas en los videos"*. El que le fue bien es **`12-11 Veo - 3` (El espejo)**: antes/despues en primera persona.

| # | Tipo | Escena | Largo | Placas |
|---|---|---|---|---|
| 4 | Antes/despues | El jean que guardo dos anos | 30,8 s | DIA 01 → SEMANA 06 |
| 5 | Antes/despues | Se filma el primer dia para probar que no servia | 32,1 s | DIA 01 → DIA 30 |
| 6 | Situacion argentina | La vecina que sube a quejarse del ruido | 31,1 s | — |
| 7 | Situacion argentina | El asado del domingo: *"¿que te estas tomando?"* | 30,8 s | — |

- **Los dos antes/despues cambian el objeto de la prueba**, no solo la cara: el 4 es una **prenda** (el mismo jean, cerrado seis semanas despues) y el 5 es la **habilidad** (el dia 01 se traba con la clase, el dia 30 la sigue entera). El 3 que esta corriendo es el espejo y la remera.
- **Las dos situaciones argentinas llevan dos personajes que dialogan** (la vecina de bata del palier; la cunada que la senala con el tenedor en el asado) y abren con conflicto en el primer segundo. Cierran con la misma protagonista a camara y el boton.
- Cuerpo validado del ganador `6-11 - 1` en los cuatro: la tele del living, los diez minutos, el paso a paso, el "sin mensualidad" y el CTA del test de un minuto. El 5 lleva ademas la escalera de las tres semanas.
- **20 tomas + 15 imagenes = US$3,55** (3 regeneraciones incluidas). Saldo despues: **US$14,81**.
- ⚠️ **El ganador `12-11 Veo - 3` NO lleva el rotulo "Caso ilustrativo · imagenes con IA"** (se verifico cuadro por cuadro): lo que dice la tanda 6 mas arriba estaba mal. Estos cuatro se entregan igual que el que esta corriendo, **sin rotulo**.
- Guiones en `OUTPUTS/2026-11-12-guiones-dancego-veo-tanda2.md`. Proyecto en `~/Desktop/dancego/anuncios/veo/{v4,v5,v6,v7}`. Entrega: `12-11 Veo - 4` a `12-11 Veo - 7`.

### Lo que enseno esta tanda
1. **El "despues" se genera editando el cuadro del "antes", no desde el retrato.** Asi la pieza, los muebles, la ropa tirada y la luz son los mismos y el unico cambio es el cuerpo. Script: `OUTPUTS/scripts-vsl/escena_despues.py` (nano-banana con dos referencias: el cuadro del antes + el retrato del despues).
2. **"Mas delgada" no alcanza.** La primera version de los dos "despues" salio con un cambio imperceptible. Hay que pedirlo explicito y en varias partes del cuerpo ("completely flat stomach, much thinner arms and thighs, narrow waist") y que la ropa quede visiblemente grande.
3. **Veo mete palabras de mas en las lineas cortas de dialogo cruzado**: le agrego "ahi" a la pregunta de la vecina y leyo *"que pille mover"*; a la cunada le puso "tenias" adelante. **No se regenera la misma linea: se reescribe** ("me va marcando los pasos") o se le da un arranque duro ("Pará."). Con eso salio a la primera.
4. **`reintentar.sh` no regenera si el clip ya esta**: primero hay que mover `clips/<id>.mp4` a `clips/malos/`.
5. **`voces.py` pide librosa, que no esta instalado.** Reemplazo: `OUTPUTS/scripts-vsl/timbre_voces.py` (MFCC con torchaudio) + F0 por linea. Con dos voces femeninas de edades distintas ninguno de los dos es concluyente: si los dos se contradicen, se escucha.

## Backend post-compra (2026-11-09) — ✅ escalera aprobada
Pedido de Santiago: *"armarle unos upsells a la oferta de dance go, utiliza la skill de pospagos"*. **No tenemos el backend de la competencia** (aclaración suya: *"El backend de la competencia no lo tenemos, asi que mira solo lo que ofrecemos en el front"*), así que el paso 2 del manual se saltea y la escalera sale del mapa del front propio.

- **Ejes que el front ya ocupa y quedan prohibidos en los OTOs:** más clases/ritmos · el desafío de 28 días · clases en vivo · comunidad de WhatsApp · recetario · registro de peso · puntos canjeables · acceso de por vida. Hoy **no hay order bumps**.
- **Los 4 huecos que la oferta abre y no cierra:** nadie le dice si lo está haciendo bien (y el avatar es justo la que no sabe bailar) · el día 29 · la flacidez que el baile no tonifica · **el evento próximo que el quiz pregunta y después nadie usa**.
- **Escalera:** OTO1 Asistente Personalizado 1 a 1 $24.990 → OTO2 El Plan de los 90 Días™ $17.990 → OTO3 El Sistema Anti-Flacidez™ $12.990 → OTO4 El Plan Evento Express™ $7.990, con ruletas al 50/53/47/55 %. **AOV proyectado $23.300 sobre el front de $14.990 → ratio 1,55.**
- ⚠️ **Bloqueador:** el front ya promete +150 videos, clases en vivo y puntos canjeables que todavía no existen. El backend no lo arregla, lo agrava. El OTO1 y el OTO2 se pueden producir sin la app; el OTO3 y el OTO4 necesitan video.
- Detalle completo en `OUTPUTS/2026-11-09-propuesta-upsells-dancego.md`.
- ✅ **Santiago aprobó la escalera el 9/11** (*"Buenisimo"*) y pidió **nombre + descripción de 3 renglones** por OTO, para la pantalla de upsells. En `OUTPUTS/2026-11-09-nombres-y-descripciones-otos-dancego.md` y en `~/Desktop/dancego/landing/otos-nombres-y-descripciones.txt`.
- **Cómo quedó cada descripción (molde de 3 renglones):** renglón 1 = el hueco que abre el front · renglón 2 = qué recibe, componente por componente · renglón 3 = **el que despeja la confusión con lo que ya compró** (el OTO1 aclara grupo vs. individual, el OTO2 que no son clases nuevas) o el gancho emocional (el OTO4, la coreografía para no quedarse sentada). **Sin precio adentro: el precio es un campo aparte de Impultienda.**
- Los 4 productos de downsell van con **el mismo nombre de cara a la compradora** (es el mismo entregable) y un sufijo interno `(DS)` para no confundirlos en el panel.


## Preguntas abiertas
- ¿La marca queda **DanceGo** o se renombra?
- ¿Precio final? (el link de checkout ya está confirmado)
- ¿Va VSL en el último paso? Si va, cambia `SEGUNDOS_OFERTA`.
- ¿Probamos la escalera de las tres semanas en los tres ads, como hace el original, o la dejamos solo en el guion 1?
- ¿Sumamos el formato B del original (clip crudo de una mujer bailando frente a la tele + dos bandas de texto, sin voz)? Es el más barato de todos y lo tienen corriendo.

## Relacionado
[[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[landings-funnels-y-upsells]] · [[pilates-hormonal]] · [[tai-chi-fit]]

## Fuentes
- `https://funilv1.appdancego.com/` y `/pgvendas` (recorrido completo del 2026-11-04)
- Entregable: `OUTPUTS/2026-11-04-quiz-dancego.html`
- Biblioteca de Anuncios de Meta, página DanceGo (`964798933379484`), relevamiento del 2026-11-06: 31 ads activos, 9 videos únicos bajados y transcriptos
- Entregable: `OUTPUTS/2026-11-06-guiones-dancego.md`
