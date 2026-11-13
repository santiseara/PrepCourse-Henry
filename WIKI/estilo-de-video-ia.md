# Estilo de video con IA — la onda por defecto

> **Regla fija desde el 4/11/2026.** Cuando Santiago pide "un video con IA", esto es lo que espera, sin que lo tenga que repetir. Sale del despiece completo de un ad brasileño de pilates 50+ que le gustó (`OUTPUTS/2026-11-04-analisis-ad-pilates-brasil.md`): *"para que cuando yo pida un video con IA se entienda que quiero de esto… no específicamente estas mismas situaciones, sino la onda"*. La onda, no el tema: cada video cambia avatar, nicho, situación y guion.

## Regla 0 — el modelo es SIEMPRE Veo

> **Corrección de Santiago, 11/11/2026:** *"el modelo que tenés que usar siempre es el de Veo… salieron súper mal los videos, mal los audios, mal lo visual, se re nota que es IA"*.

**Todo video con IA se genera con Veo 3.1 (Fast) por [[apimart]]. `wan2.7-r2v` queda descartado para anuncios.** No se pregunta ni se evalúa alternativa: si el pedido es "video con IA", es Veo.

Por qué Veo y no un avatar con voz clonada:
- **El audio lo actúa el modelo.** El diálogo va escrito en el prompt y Veo lo dice con entonación, pausas y respiración propias de la escena. Con `wan2.7-r2v` la voz salía de una muestra TTS clonada: plana, con tonada que se iba de clip en clip y lipsync de maniquí. Eso es lo que sonaba falso.
- **La escena se mueve.** Veo genera gente que actúa dentro de un plano (cámara en mano, luz real, cuerpos que pesan). El avatar hablando a cámara desde una foto fija se lee como IA a los dos segundos.
- **Nada de parches de montaje.** No hay que medir F0, ni igualar RMS, ni regenerar por tonada: si una toma sale mal, se regenera y listo.

Lo que esto implica en la práctica: **una toma = 8 s y 0 a 3 líneas de diálogo**, el primer cuadro sale de una imagen (`gemini-nano-banana-2.1-ext` para componer la escena con las caras de referencia), el acento se escribe en el prompt (`ACENTO` rioplatense con voseo) y cada toma se verifica con Whisper + MMS. El pipeline entero está en la skill `mini-novela` (sirve igual para un ad de 25 s: son 4 o 5 tomas en vez de 50).

## Las 8 reglas de oro

1. **Un avatar hablando a cámara en selfie, de punta a punta.** Nada de voz en off sobre B-roll. La persona es el video.
2. **Clips de 8 segundos, uno detrás del otro, con corte seco.** Un video de 90 s son 11 clips. Nunca un clip de 3 s ni uno de 15.
3. **Todos los clips salen de la MISMA imagen de referencia.** Por eso arrancan en la misma pose y se leen como jump cuts de un video casero. Es el truco que hace que no parezca un rejunte.
4. **Una sola voz en todo el video**, con muestra de referencia fija, nunca descrita de nuevo en cada clip. Tonada publicitaria, enérgica, ~**185 palabras por minuto**.
5. **Cero silencio.** Hay voz el 99 % del tiempo. Los únicos huecos son de medio segundo y marcan cambio de bloque.
6. **Subtítulos karaoke obligatorios:** MAYÚSCULAS, sans bold, blanco con contorno negro grueso, **palabra activa en amarillo**, 2 a 4 palabras por placa, una placa cada 1,1-1,3 s, centrado abajo.
7. **Una sola transición en todo el video** (un flash blanco de ~0,4 s) y sólo para cambiar de personaje o de bloque. Todo lo demás, corte seco. Cero whoosh, cero efecto de sonido.
8. **9:16, sin logo, sin marca de agua, sin placa final.** Termina en la cara del avatar.

## La prueba va adentro del plano

El recurso más fuerte del ad: **la persona habla al frente y el resultado se ve atrás, en la misma toma** (la hija cuenta el caso de la madre mientras la madre entrena de fondo). Después se regenera el mismo plano con el cuerpo cambiado y se rotula **"DIA 01" / "DIA 49"**.

- Placa de día: blanco bold con sombra suave, arriba a la izquierda.
- **Los primeros 4 segundos van sin subtítulos**, sólo con la placa: la atención va entera a la escena.
- Al regenerar el "después" hay que **revisar el fondo**: la IA cambia detalles (en el ad apareció una manta en el sofá que antes no estaba). Mismo prompt, misma referencia, y aun así se mueve.

## Fotos reales: la única excepción a "nada de fotos"

La regla general sigue ([[guiones-y-anuncios]]): nada de stock, nada de mockups, nada de capturas. **La excepción son las fotos del testimonio**: antes/después de una persona real, sin retocar, con grano de celular.

- Van **a pantalla completa**, con el avatar en **picture-in-picture abajo a la derecha** (~40 % del alto), **hablando**: la prueba ocupa la pantalla y la voz nunca se corta.
- **La cara de cualquier tercero se tapa con un emoji** 😀.

## La estructura de guion (90 segundos)

| Bloque | Tiempo | Qué hace |
|---|---|---|
| 1. Hook de prueba viva | 0-14 s | Alguien cuenta el caso de otro **mientras el resultado se ve atrás**. "Día 01" → "Día 49" |
| 2. Oferta con fecha | 14-19 s | "Este lunes arranca un grupo nuevo". La escasez es el calendario, no el precio |
| 3. Mecanismo en una línea | 19-30 s | Rápido, sin impacto, sin aparatos, específico para ese cuerpo: tres objeciones en 11 s |
| 4. Escalera de resultados por tiempo | 30-44 s | Día 1 → 3 días → 1 semana → "todos te empiezan a elogiar" (el social va último) |
| 5. Caso con nombre, edad y cifra | 44-58 s | "Carla, 59 años, 15 kilos" + foto real |
| 6. CTA + escasez | 58-65 s | El botón, con nombre exacto |
| 7. Entregables | 65-81 s | Recién acá qué incluye, con un mecanismo con nombre propio |
| 8. CTA repetido y cierre personal | 81-88 s | "Te espero adentro" |

**Nunca aparece:** precio, descuento, cuenta regresiva, "últimas vacantes", jerga técnica ni cifras de plata.

### El pulso del guion
- Hook acelerado (**205-260 ppm**), mecanismo más lento (130-200), **un solo freno** antes de la prueba ("mirá esta transformación", 90 ppm) y cierre a toda velocidad (**235-290 ppm**).
- Una frase por clip, sin frases colgadas entre dos clips.

## Control de calidad (antes de entregar)

- [ ] **Duración de los planos:** todos entre 6 y 8,5 s. Si hay uno de 3 s, se rehízo mal el corte.
- [ ] **Mismo arranque:** los clips del mismo personaje empiezan en la misma pose. Si uno arranca distinto, se generó sin la imagen de referencia.
- [ ] **Voz pareja:** una sola voz, mismo timbre y mismo ritmo de punta a punta (medir ppm por bloque).
- [ ] **Lip sync:** los labios se mueven con la voz, sin desfase visible. Medición: hoja de 12 cuadros seguidos en una sílaba fuerte; además, correlación boca/audio con pico cerca de 0 (±150 ms es normal, los labios se adelantan un poco).
- [ ] **Fondo estable** entre clips del mismo plano (muebles, mantas, cuadros).
- [ ] **Manos:** revisar dedos en los cuadros donde gesticula.
- [ ] **Anatomía y física (2026-11-13):** ningún brazo o pierna de más, ninguna mano que salga de donde no va, y **ningún objeto flotando**: el celular que graba tiene que estar apoyado en algo que se vea (mesa, repisa, trípode) o sostenido por una mano. Se revisa **cuadro por cuadro en la hoja de contactos de cada toma**, no solo en el primero: el brazo duplicado suele aparecer a mitad del plano, cuando el personaje gesticula.
- [ ] **Subtítulos:** ninguno tapado, ninguno cortado, nada de texto quemado del modelo.
- [ ] **Audio:** voz al frente (picos cerca de −4 dBFS), sin silencios, sin efectos.

## Lo que esto cambia de tus reglas actuales

- [[guiones-y-anuncios]] fija **cortes de 1,9 a 2,9 s** y voz a **speed 1,30**: eso es para los ads de **voz en off con clips de TikTok**, que siguen igual. **Este formato es el otro carril:** avatar IA, planos de 8 s, voz a ritmo natural rápido (185 ppm) y sin recorte de silencios, porque rompe el lipsync.
- El tope de 30 segundos tampoco aplica acá: la referencia que le gustó dura **88 s** y recién nombra el CTA al segundo 58.

## Registro de correcciones

- **2026-11-11 · El modelo es Veo, siempre.** Está arriba, en la Regla 0. La primera tanda de DanceGo salió con `wan2.7-r2v` y Santiago la rechazó entera: *"mal los audios, mal lo visual, se re nota que es IA"*. **Nunca más elegir modelo de video por precio.** La voz clonada sobre una foto fija es el defecto, no la solución; lo barato salió caro (US$8,63 tirados). Si el saldo no alcanza para hacerlo con Veo, se avisa antes de generar, no se baja de modelo.
- **2026-11-11 · El largo por defecto son 4 o 5 escenas, no 88 segundos.** Pedido textual: *"videos de 4/5 escenas, podés repetir algunas, no siempre, pero a veces sí, que salgan bien, metele un poco de velocidad, cortá silencios, y que suenen reales, que hablen fluido, cuidado con las entonaciones o el acento, tiene que sonar argentino, no raro"*. Lo que cambia de las 8 reglas de arriba:
  - **4 o 5 tomas por video, de 5 a 9 s cada una → 22 a 26 s de ad.** Los 88 s de la referencia brasileña son el techo del formato, no el molde.
  - **Repetir plano es parte del formato:** el video 1 de [[dancego]] usa tres veces el mismo plano del "día 21" y cambia solo lo que cuenta. Es lo que hace el original.
  - **Sí se cortan los silencios y sí se acelera.** La regla de [[guiones-y-anuncios]] ("UGC con avatar: speed 1,08 y sin recorte de silencios porque rompe el lipsync") vale para una voz en off pegada encima. Acá el corte saca **el mismo tramo del video y del audio**, así que no hay nada que desincronizar: queda como jump cut. Medido: silencios internos > 0,26 s recortados + **×1,05** global de imagen y sonido.
  - **El acento se resuelve con la muestra de voz, no con el prompt.** Una muestra de 9-10 s de Sulafat / Orus pasada como `reference_voice` hace que el video hable en rioplatense; describir el acento en el prompt solo refuerza. Y las entonaciones raras se detectan midiendo el F0 de cada toma: la que se sale de ±8 % se regenera (US$0,53), no se arregla en el montaje.
  - **Escenas de la vida real, dichas por quien las vive:** antes y después, el marido sorprendido, el juego con la hija. El avatar que explica a cámara es el cierre, no el video entero.

- **2026-11-12 · Los mp4 se corrompen si se trabaja dentro de `~/Desktop`.** Durante la tanda 7 de [[dancego]] cuatro clips quedaron truncados (12 KB) y otros cuatro se encogieron solos despues de descargarse bien; `curl` fallaba con *Failure writing output to destination* y PyAV con *Operation timed out* al abrirlos. **Regla: generar, verificar y montar en disco local** (la carpeta de trabajo de la sesion) y copiar al Desktop **solo el mp4 terminado**, verificando despues con `ffprobe` que el tamano y la duracion esten bien. Si un clip ya generado se corrompe, no se vuelve a pagar: el `task_id` queda en `costos.jsonl` y se baja de nuevo con `GET /v1/tasks/{id}`.
- **2026-11-12 · El antes/despues se genera editando el cuadro del antes.** No alcanza con dos retratos del mismo personaje: la pieza, los muebles y la luz cambian y se nota. Se le pasan a nano-banana **dos referencias** (el cuadro del "antes" + el retrato del "despues") y se pide **mantener todo menos el cuerpo**. Y el cambio de cuerpo hay que pedirlo fuerte y por partes: con "slimmer" a secas no se ve nada. Script: `OUTPUTS/scripts-vsl/escena_despues.py`.
- **2026-11-12 · Las lineas cortas de dialogo cruzado se las inventa un poco.** En dos tomas de dos personajes Veo agrego palabras ("ahi", "tenias") y leyo *"pille"* por *"pie"*. **Se reescribe la linea, no se regenera igual**: un arranque duro ("Pará.") o cambiar la palabra floja ("me va marcando los pasos") lo arregla a la primera.
- **2026-11-12 · El rotulo "Caso ilustrativo · imagenes con IA" no esta en el ad que corre.** Se verifico cuadro por cuadro sobre `12-11 Veo - 3`. Las tandas nuevas salen igual que el que esta andando; si se quiere el rotulo, se agrega a los cuatro en un pase de ffmpeg y se avisa.
- **2026-11-13 · Lo que se manda a aprobar va montado, nunca crudo.** Le mostré a Santiago las 4 tomas del hook de la novela 1 pegadas una atrás de otra, sin montar, y la devolución fue: *"tiene muchísimos silencios, va todo muy lento, no coordinan los labios, la escena está mal hecha"*. Las tomas estaban bien: una toma de Veo son 8 s fijos y el personaje se queda quieto antes y después de decir su línea, así que **en crudo todo formato de Veo parece lento y desincronizado**. El montaje recorta cada toma a su tramo hablado y achica los huecos: el mismo hook pasó de **31,7 s a 17,1 s solo con el recorte**, y a 15,6 s con la velocidad. Regla: aunque sea para aprobar caras, voces o acento, el piloto se entrega **ya montado** (recorte + velocidad), y si hace falta ver una toma cruda se avisa en una línea por qué.
- **2026-11-13 · Las novelas largas van aceleradas.** Mismo pedido: *"habría que meterle velocidad"*. Para el formato novela el montaje va con **`PAUSA=0.35`** (huecos entre líneas) y **`VEL` entre 1,10 y 1,18**, que acelera imagen y sonido juntos y por eso no rompe el lipsync. Sin acelerar queda con el ritmo de la referencia brasileña, que es más lento que lo que él quiere para Argentina.
- **2026-11-13 · Una toma con el cuerpo roto no se entrega, se regenera.** Santiago, pidiendo renovaciones de [[dancego]]: *"fijate que las visuales salgan bien, hay muchas que los brazos se duplican, o el celular se sostiene solo, muy malas"*. Los dos defectos que más aparecieron: **brazos duplicados** (un tercer brazo que asoma cuando el personaje gesticula o cuando dos personajes se cruzan en el plano) y **objetos que se sostienen solos** (el celular que la filma flotando en el aire). Reglas que salen de ahí:
  - El **selfie filmado por un tercero no se pide nunca en abstracto**: en el prompt va **quién sostiene el teléfono o dónde está apoyado** ("the phone is propped against a stack of books on the table"), porque si no Veo lo deja flotando.
  - Las tomas con **dos personajes muy juntos o con contacto** son las que más brazos duplican: se separan en el encuadre o se pide contacto explícito y simple (una mano en el hombro, no un abrazo).
  - El control visual **es por toma y cuadro por cuadro** (checklist de arriba), antes del montaje. Una toma con el cuerpo roto **se regenera**, no se corrige en edición ni se tapa con un corte.

## Preguntas abiertas

- ✅ **Resuelto el 11/11: sale de Veo 3.1 Fast por [[apimart]]** (mirá la Regla 0). Se probó `wan2.7-r2v` con voz de Gemini TTS como `reference_voice` y se descartó el mismo día: audio plano y visual que se nota. HeyGen queda para doblaje.
- ¿Las fotos de testimonio de dónde salen cuando la oferta es nueva y no hay clientes todavía?
- ¿La cama musical va o no va? En la referencia casi no se oye.

## Relacionado

[[ugc-y-video-generativo]] · [[guiones-y-anuncios]] · [[vsl-reglas-de-armado]] · [[apimart]] · [[skills-launch-expert]] · [[hooks]]

## Fuentes

- `OUTPUTS/2026-11-04-analisis-ad-pilates-brasil.md` (despiece completo)
- `~/Desktop/referencias-video-ia/pilates-brasil/` (video + hojas de contactos)
