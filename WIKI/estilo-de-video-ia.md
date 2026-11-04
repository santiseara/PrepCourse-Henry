# Estilo de video con IA — la onda por defecto

> **Regla fija desde el 4/11/2026.** Cuando Santiago pide "un video con IA", esto es lo que espera, sin que lo tenga que repetir. Sale del despiece completo de un ad brasileño de pilates 50+ que le gustó (`OUTPUTS/2026-11-04-analisis-ad-pilates-brasil.md`): *"para que cuando yo pida un video con IA se entienda que quiero de esto… no específicamente estas mismas situaciones, sino la onda"*. La onda, no el tema: cada video cambia avatar, nicho, situación y guion.

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
- [ ] **Subtítulos:** ninguno tapado, ninguno cortado, nada de texto quemado del modelo.
- [ ] **Audio:** voz al frente (picos cerca de −4 dBFS), sin silencios, sin efectos.

## Lo que esto cambia de tus reglas actuales

- [[guiones-y-anuncios]] fija **cortes de 1,9 a 2,9 s** y voz a **speed 1,30**: eso es para los ads de **voz en off con clips de TikTok**, que siguen igual. **Este formato es el otro carril:** avatar IA, planos de 8 s, voz a ritmo natural rápido (185 ppm) y sin recorte de silencios, porque rompe el lipsync.
- El tope de 30 segundos tampoco aplica acá: la referencia que le gustó dura **88 s** y recién nombra el CTA al segundo 58.

## Preguntas abiertas

- ¿El avatar de las ofertas de Santiago sale de HeyGen Avatar IV (lo que usa hoy) o pasa a `wan2.7-r2v` por [[apimart]], que es el que permite los 8 s con la misma referencia y voz fija?
- ¿Las fotos de testimonio de dónde salen cuando la oferta es nueva y no hay clientes todavía?
- ¿La cama musical va o no va? En la referencia casi no se oye.

## Relacionado

[[ugc-y-video-generativo]] · [[guiones-y-anuncios]] · [[vsl-reglas-de-armado]] · [[apimart]] · [[skills-launch-expert]] · [[hooks]]

## Fuentes

- `OUTPUTS/2026-11-04-analisis-ad-pilates-brasil.md` (despiece completo)
- `~/Desktop/referencias-video-ia/pilates-brasil/` (video + hojas de contactos)
