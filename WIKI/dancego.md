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
