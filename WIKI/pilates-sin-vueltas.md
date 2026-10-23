# Pilates sin Vueltas

> Biblioteca de clases **para instructoras de pilates** (no para alumnas): 100 clases de 60 min ya armadas + 500 ejercicios ilustrados. Mercado Argentina, en pesos, ImpulTienda. Es el modelado 1 a 1 de **Centerline Pilates**, un ganador en inglés con 41 anuncios activos. Funnel: ad → landing → checkout (sin quiz). (fuente: Facebook Ads Library page 998425433348426, relevada 22/10/2026)

## ⚠️ No confundir con [[pilates-hormonal]]
Son dos ofertas distintas y opuestas: Pilates Hormonal le vende a la **alumna** de 40/45+ que quiere bajar la panza, con quiz y VSL. Pilates sin Vueltas le vende a la **instructora** que pierde horas armando clases. Mismo nicho, avatar inverso.

## Ficha
| Campo | Valor |
|---|---|
| Producto | 100 clases completas de 60 min por nivel y objetivo + 500+ ejercicios ilustrados (foco, músculos, respiración, errores comunes, progresiones) + Manual de la Instructora. Acceso digital de por vida |
| Avatar | Instructora de pilates: recién recibida o con años, que planifica gratis dos horas por cada hora que cobra |
| Equipamiento cubierto | Mat, elementos, pilates en la pared, reformer, cadillac, wunda chair y barril |
| Adaptaciones | Embarazo, adultos mayores, lesiones de lumbar, rodilla y hombro |
| Precio | $17.999 (ancla $44.999, 60% OFF) · pago único · contador de 15:00 |
| Garantía | 7 días |
| Bonos | Planificador de Clases · Ficha de Evaluación de la Alumna · Calendario de 30 Días · Progresión de 8 a 12 Semanas · Cómo conseguir más alumnas |
| Landing | `https://pilates-sin-vueltas.impultienda.ar/` |

## 🎯 El ganador: Centerline Pilates
- Page ID `998425433348426` · **41 anuncios activos** · todos al mismo URL: `centerlinepilates.impultienda.ar` · sin marca personal · 3 semanas corriendo. Pasa el filtro estricto de [[funnel-hacking]].
- **Corre en inglés sobre ImpulTienda .ar a US$ 27** (ancla US$ 67). Misma plataforma que usa Santiago, mercado inverso al suyo.
- Headline: "The Pilates Instructor's Library" → "Teach professional Pilates classes without ever winging it again". Lema: *"Open it, pick it, teach it."*
- **Un solo primary text para los 41 anuncios.** No testean copy, testean video.

### Cómo evolucionaron los creativos (lo más importante)
| Tanda | Anuncios | Formato | Ángulo |
|---|---|---|---|
| 1 oct | 11 | cortos de 0:27 a 0:48 + un VSL de 3:06 | dolor de planificar: domingo a la noche, cuaderno en blanco, 5 min antes de la clase |
| 6 oct | 10 | 5 cortos + 5 largos (1:38-2:02) | la cuenta de las horas no pagas, clientas que se van por repetir secuencia, la formación que no enseña a armar clases |
| 12 oct | 10 | 4 cortos + 6 largos | plata y vida: segundo trabajo, cancelaciones, mensajes a las 10 de la noche, el reformer que junta abrigos, el curso de fin de semana |
| **20 oct** | **10** | **todos de 1:51 a 2:08. Cero cortos** | **la alumna imposible que te rompe la clase que planeaste** |

**Abandonaron el formato corto.** Lo que escalan hoy es el video largo de "alumna imposible".

### 🧬 La DNA de la tanda del 20/10 (plantilla rígida, los 10 iguales)
1. **Escena de una alumna concreta** en presente y en segunda persona: entra alguien cuyo cuerpo no entra en la clase que tenías armada.
2. **La consecuencia**: se va, no vuelve, y nunca sabés por qué.
3. **El giro que saca la culpa** (frase fija en los 10): *"No es que te falte formación. Es que nadie te dio nunca [X] escrita, lista para dar."*
4. **El producto**: 100 clases de 60 min con dosis, tiempo y **la consigna exacta para decir en voz alta**.
5. **La adaptación**, bajada a la escena del hook: apta embarazo, 50+, progresión y regresión.
6. **500 ejercicios ilustrados** + un detalle a medida de esa escena (límites de rango, versiones en silla y pared, cues para un cuerpo que no siente).
7. **El manual**: "no estás leyendo la clase de otra, entendés por qué está armada así".
8. **Precio como ROI**: "menos de lo que cobrás por una clase particular", pago único, para siempre, sin abono.
9. **Cierre "Dejá de X"** que recoge la escena del hook.
10. **CTA fijo**: "Tocá el botón de abajo y mirá la oferta".

Las 10 escenas: clase de prueba · señora de 74 que no baja al piso · posparto de 8 semanas · prótesis de rodilla · hombre grande y rígido · hipermóvil que no siente nada · túnel carpiano y hombro congelado · osteoporosis sin flexión de columna · clases online (cuatro cuadraditos negros) · "ya pago una app por mes".

### Formato de video (replicable sin cara)
9:16 · **b-roll de estudio** (reformers, clases grupales, luz natural) · voz en off femenina · cartel grande de hook arriba con caja y borde amarillo · subtítulos karaoke en amarillo y blanco · logo abajo a la derecha. Sin avatar, sin cara, sin música cantada. Voz en off en Google AI Studio ([[vsl-reglas-de-armado]]).

## Competencia en español
- **ClaseLista · Para Instructoras** (page `1349747274893052`): 3 anuncios desde el 12/10, "150 clases de pilates por US$ 9,90", cuenta en BRL apuntando a Argentina. Todavía está testeando, pero es el mismo movimiento que estamos haciendo nosotros y con más clases y menos precio. Revisar en 2 o 3 días si sube el número de anuncios.
- **Candelapilates / Hada Pilates Academy**: formación de instructoras con marca personal. Otra categoría, se descarta como modelo ([[funnel-hacking]]).

## Producción de los videos (22/10/2026, cero créditos)
Pipeline reusado de [[group-work-playbook]]: `edit_gwp.py` + `gen_pilates_plans.py`, en `~/Desktop/pilates-sin-vueltas/anuncios/work/`.
- **Voz:** Google AI Studio, voz **Sulafat**. ⚠️ **La interfaz cambió el 22/10:** con el modelo 3.8 por defecto ya no está el campo *Scene* ni el de *persona*, y el bloque de texto tiene el placeholder `<gasp> That's a great idea!` en vez de `[amused]`. El buscador de voces es "Search 2,000+ voices" (el regex viejo `/search voices/i` ya no matchea).
- 🆕 **2026-10-23 · Al elegir Gemini 3.1 Flash TTS Preview vuelven *Scene* y *Sample Context*,** y el panel del hablante trae **Audio Profile** ("Describe the voice persona") más una **Director's note** con Style, Pace y Accent. Ahí se dirige el rioplatense: el Accent solo trae acentos del inglés (queda en **Neutral**) y el acento argentino sale del **Audio Profile** + el **Scene**.
- 🆕 **2026-10-23 · El botón Download ya funciona.** Baja el WAV a `~/Downloads/Generated Audio <fecha> - <hora>.wav`. No hace falta receptor local ni leer el data URI del `<audio>` (con 3.1 el `<audio>` del DOM solo tiene un pitido de 0,04 s: el audio va por Web Audio).
- ⚠️ **Las voces en español son de pago:** filtrar Language = Spanish deja la lista vacía con "Link a Paid Key". Se sigue usando una voz inglesa (Sulafat) y se dirige el rioplatense desde el Style. Sale a ~190 palabras por minuto, así que un guion de 184 palabras da 58 s.
- **B-roll:** Mixkit, serie **48544 a 48567** = un estudio de reformers real, toda en 1080p, el mismo look que el ganador. Descartados por ser primeros planos anatómicos (riesgo con las políticas de Meta y no pegan con el público de instructoras): 48547, 48549, 48550, 48551, 48552, 48553, 48563, 48565. `mk48544` dura solo 4,09 s: tope 3,8.
- ⚠️ **Planos de apertura:** `mk48562` y `mk48564` arrancan con un primer plano tapado o un reformer vacío y quedan mal de miniatura. Los buenos para abrir: `mk48557`, `mk48567`, `mk48544`, `mk48556`, `mk48561`, `mk45761`.
- **Stills:** las fichas de clase y de ejercicio de la propia landing (`~/Desktop/pilates-sin-vueltas/imagenes/img*.webp`), ancladas a la palabra exacta del guion.
- ⚠️ **Los anchors llevan acento.** `norm()` del editor solo saca lo que no es `\w`, así que las tildes quedan: hay que escribir `índice`, no `indice`.
- ⚠️ **El CDP corta a los 45 s**, así que la generación de voz se lanza sin `await` (`window._gen(n).then(...)`) y después se consulta `window._wavs`.
- 🆕 **2026-10-23 · Verificar SIEMPRE que la generación arrancó.** La mitad de las tandas no se generó y el botón Download bajó de nuevo el audio anterior: salieron tres archivos repetidos de a pares sin ningún aviso. Reglas: enviar con **clic en el textarea + `cmd+Return`** (el clic en el botón Run no dispara si el audio anterior está sonando), sacar una captura a los 6 s y confirmar que aparece **Stop**, y después del `mv` comparar **md5 y duración** contra el anterior. Al final, transcribir los WAV con Whisper y chequear que cada uno diga su guion.

## Activos
- **Guiones v2 (los vigentes, 22/10):** `OUTPUTS/2026-10-22-guiones-pilates-sin-vueltas-v2.md`. Seis variables del mismo ángulo, cada una con estructura, bajada de producto y cierre propios.
- Guiones v1 (descartados, 22/10): `OUTPUTS/2026-10-22-guiones-pilates-sin-vueltas.md`. Copiaban la plantilla fija del competidor y Santiago los rechazó: "si todos sus guiones dicen lo mismo, no lo hagamos así".
- Videos: `~/Desktop/pilates-sin-vueltas/anuncios/PSV-V1.mp4` a `PSV-V6.mp4` (voz en off sobre b-roll de estudio).
- 🆕 **Rehechos el 23/10 con acento argentino.** Santiago: "tiene una voz que habla muy neutro y parece que son videos para LATAM". Se regeneraron las seis voces con el Audio Profile porteño (ver arriba) y se corrigió el guion 1: **"Me operaron la rodilla" → "Me operé de la rodilla"**, porque el TTS pronunciaba "operaron" raro. Las voces nuevas salen un poco más largas (1:02 a 1:10 contra 0:53-0:58), dentro del tope de 1:30. Las voces viejas quedaron en `work/vo/V1_neutro.wav.bak`.
- Carpeta de trabajo: `~/Desktop/pilates-sin-vueltas/` con `imagenes/`, `landing/` y `anuncios/`.

## Reglas para los ads
- **Máximo 1:30 por video** (regla de Santiago del 22/10), aunque el ganador vaya a 2 minutos.
- Cada video toma **una escena distinta**: nunca repetir la alumna ni el detalle a medida ([[guiones-y-anuncios]], registro del 21/10).
- El precio va como ROI ("menos que una clase particular"), nunca como número ([[guiones-y-anuncios]]).
- No culpar a la instructora: el giro de "no es que te falte formación" es justamente lo contrario, y es el corazón del ganador.
- Nada de promesas clínicas ni de tratamiento: es material educativo para profesionales.

## Preguntas abiertas
- ¿El ancla de $44.999 aguanta en Argentina, o conviene acercarse a los US$ 9,90 de ClaseLista?
- ¿Vale la pena probar un VSL de 3 minutos como el de ellos, o el tope de 1:30 lo descarta?
- ¿Hay OTO armado? La original no muestra upsell visible en la landing.
- De dónde sale el b-roll de estudio con reformers: ¿stock o generado?

## Relacionado
[[pilates-hormonal]] · [[funnel-hacking]] · [[guiones-y-anuncios]] · [[ugc-y-video-generativo]] · [[modelo-low-ticket]] · [[internacionalizacion]]

## Fuentes
- Facebook Ads Library, page 998425433348426 (Centerline Pilates), relevada 22/10/2026: 38 videos descargados y transcriptos
- Landing propia: pilates-sin-vueltas.impultienda.ar
- Landing original: centerlinepilates.impultienda.ar
- OUTPUTS/2026-10-22-guiones-pilates-sin-vueltas.md
