# Tai Chi Fit

> Revivir la oferta de Tai Chi que ya vendió muchísimo, ahora con mejor embudo: **quiz + VSL**. El quiz se modela del de **Calistenia Militar Femenina** (AR, ~48 ads activos) y el guion del VSL va a salir de una página de calistenia asiática para hombres. (fuente: conversación del 2026-10-26)

## Ideas clave
- **Tai Chi Fit ya fue un ganador.** Santiago: *"me generó muchísimo dinero, vendió demasiado"*. Lo que falla no es la oferta, son los embudos y los anuncios: por eso se rearma de cero con quiz + VSL.
- **El cambio que tiene que convertir es el VSL.** El quiz es el envase; el VSL es donde se juega la venta.
- **Modelo del quiz: Calistenia Militar Femenina.** Lo eligió porque es *"cortito, simple y directo"*: 10 pasos y afuera.
- **Todo lo militar pasa a oriental**, no se toca el resto: misma comunicación, mismo orden de pasos, mismos componentes ([[quizzes-reglas-de-armado]] §2).

## Ficha de la oferta
| | |
|---|---|
| Producto | Tai Chi Fit — reto de 28 días |
| Público | **Solo mujeres** (lo mantiene del original) |
| Idioma | Español argentino con voseo |
| Precio | **$14.990 ARS**, tachado $49.990 (70% OFF), 3 cuotas de $4.997 |
| Checkout | ImpulTienda — `https://taichi-fit.impultienda.ar/checkout` **(confirmado 2026-11-05, sin guion entre "tai" y "chi")** |
| Instructora | Maestra Valentina (+10 años · 50.000+ alumnas) — **asiática, unos 50 años, sentada, fondo liso** (decisión del 2026-11-03 para el avatar del VSL) |
| Niveles | Aprendiz → Practicante → Discípula → Maestra |
| Mecanismo | Fases Raíz · Fluir · Grulla |

## El original: Calistenia Militar Femenina
- **Anunciante:** página "Calistenia Militar Femenina", ~48 ads activos en AR desde fines de julio de 2026, todos con el mismo copy y creativos de video de 50 s a 2 min.
- **Landing:** `calisteniafeminina.site` — marca **FEMME FORCE**, producto "Calistenia Militar", **US$ 9,90** tachado US$ 47 en Hotmart.
- **Embudo:** portada (= 1ª pregunta, la edad) → 9 pasos más → pantalla de análisis de 3,3 s → **`vsl.html`** (VSL de VSLwave, sin oferta a la vista) → `/sales-page` (todo el bloque de venta).
- **Stack:** HTML propio (no InLead), TrackTurbo para pixel y UTMs, cloaker por geolocalización y player de VSLwave.
- **Los 10 pasos:** edad · nivel actual · flexiones seguidas · objetivo · zona · molestias (multi, con fotos) · tiempo por día · dónde entrena · qué la frenó · peso y altura con slider.
- **Lo que hace bien:** la portada ya es la primera pregunta (no hay botón "Empezar"), el avance es instantáneo al tocar (sin pantallas de feedback), y la sales page entera está personalizada con las respuestas.

## Qué se adaptó y qué no
| Original | Tai Chi Fit | Por qué |
|---|---|---|
| "¿Cuántas flexiones podés hacer seguidas?" | **"¿Cuánto podés quedarte parada en un pie sin apoyarte?"** | El test de fuerza no aplica; el de equilibrio es *el* test de Tai Chi y calibra igual |
| Rango militar (Recluta → Sargenta) | Nivel (Aprendiz → Maestra) | — |
| Cap. Valentina, ex-militar | Maestra Valentina | — |
| "Ganar fuerza y resistencia" | "Ganar energía y flexibilidad" | Promesa real del Tai Chi |
| "En el gym" | "En el patio o la terraza" | — |
| Archivo clasificado / acceso autorizado / agentes | Manuscrito / acceso concedido / alumnas | Mantiene el marco de "conocimiento prohibido", que al Tai Chi le queda mejor todavía |
| Paleta oliva + camuflaje | **Jade + bambú + bermellón sobre papel de arroz** | — |
| US$ 9,90 en Hotmart | $14.990 ARS en ImpulTienda + cuotas de Mercado Pago | — |
| Los 10 pasos, su orden y su lógica | **Igual** | [[quizzes-reglas-de-armado]] §2 |

## Imágenes
- **Reusadas del original** (sin marca ni texto en otro idioma): portada antes/después, las 4 transformaciones y las 5 fotos de zonas con dolor.
- **Nuevas, hechas con Higgsfield** (gpt_image_2, 1k, High, 1:1 — 3,5 créditos cada una): el hero de 3 mujeres practicando Tai Chi al amanecer y el retrato de la Maestra Valentina. Se rehicieron porque las del original tenían **la marca FEMME FORCE en el celular** y ropa militar.

## El VSL del original (bajado y transcripto el 2026-11-03)
El VSL que corre detrás de ese mismo quiz está en `calisteniafeminina.site/vsl.html` con un player de **VSLwave**. El `data-id` del HTML (`ko71du5bkg`) no es el video: es un **A/B de dos VSL** (`99iah5dfnf` y `731e0gpt30`, 50/50) que se resuelve en `https://cdn.vslwave.site/c/<id>.json`. El master real de cada variante vive en `https://cdn.vslwave.site/v/<video>/<media>/master.m3u8` y baja sin autenticación (el `<video>/master.m3u8` sin el media id da 404).
- **Dura 18:33 y tiene 4.709 palabras**, en 4:5 (360x450 · 540x676 · 720x900). Nuestro VSL son ~1.000 palabras: entra el 21%, así que **no se clona 1 a 1, se destila**.
- Es un **VSL brasileño traducido** a español neutro ("tú", "hermosa", "mi amor"): en el minuto 18:03 la locutora lee en voz alta *"Bloco uno"* y el video **termina cortado a mitad de frase**.
- **La edición está partida al medio:** hasta ~7:30 B-roll denso (transformaciones, mujeres comunes, anatomía 3D, testimonios a cámara); de ahí al final son **diez minutos de talking head puro**, que es donde va toda la oferta. Esa mitad es la que hay que comprimir.
- **Subtítulos:** mayúsculas, 2–3 palabras, **sin franja negra**, con la palabra clave en **amarillo** y el resto en blanco, a la altura del pecho. Distinto del nuestro (franja negra).
- Mapa de los 20 bloques, qué entra, qué sale y por qué: `OUTPUTS/2026-11-03-mapa-vsl-original-calistenia-militar.md`. Transcripción con tiempos: `OUTPUTS/2026-11-03-transcripcion-vsl-calistenia-militar.txt`.
- **Lo que no se copia:** el soporte por WhatsApp (nuestra oferta no lo tiene), las "8.000 mujeres" (el quiz dice 50.000+ alumnas), todo el Ozempic y la escasez por plazas de soporte.
- Dato: la presentadora del original **también se llama Valentina** — de ahí salió nuestra Maestra Valentina en octubre.

## El guion del VSL (2026-11-03)
- **8 minutos, 1.730 palabras**, en dos bloques de HeyGen de 4.461 y 4.910 caracteres (tope 5.000).
- **La tasa real de nuestro pipeline es ~205 palabras por minuto**, medida sobre dos VSL propios de duración conocida: Pilates Hormonal (1.503 palabras → 6:44) y Calistenia Rusa (1.162 → 6:00). La regla vieja de "850 palabras = 4–5 min" de [[vsl-reglas-de-armado]] §0 **subestima**: con esa cuenta este guion habría salido de 5 minutos.
- **Mecanismo propio: "tu raíz"** — en lugar del "motor metabólico femenino" del original. Encaja con la Fase Raíz que el quiz ya promete y evita el claim del cortisol.
- **El villano es el cuerpo que vive en alerta** (hombros que suben, cadera que se cierra, equilibrio que se va), no una hormona: no hay claim médico que defender.
- **El open loop del original se mantiene** (el error de los primeros cinco minutos del día) y se cierra con una corrección real de tres minutos antes de levantarse de la cama.
- Los **5 bonos del quiz con sus valores** y el total de $167.600, el precio $14.990 con las 3 cuotas y la garantía de 30 días: todo dicho **en palabras** para la voz.

## Estado
- ✅ Quiz entero armado y probado paso por paso: `~/Desktop/tai-chi-fit/`.
- ✅ **Guion del VSL escrito** (2026-11-03): `OUTPUTS/2026-11-03-vsl-tai-chi-fit-guion.md` y `~/Desktop/tai-chi-fit/vsl/`. Santiago lo pidió de **8 minutos** ("así es más completo"), no de 4–6.
- ✅ **VSL terminado (2026-11-04): `~/Desktop/tai-chi-fit/vsl/Tai-Chi-Fit-VSL.mp4`**, 8:43, 1080x1920, 154 MB.
  - **Avatar "Maestra Valentina"** creado en HeyGen desde `imagenes/avatar-maestra-valentina.png` (9:16 exacto, sin barras blancas).
  - **Voz Sulafat** por API en cinco bloques, **todos con el mismo modelo** (`gemini-2.5-flash-preview-tts`) y **todos igualados a 210 palabras por minuto**, cada uno con su propio atempo.
  - **63 créditos de HeyGen en total** con "Sincronización de labios" ([[vsl-reglas-de-armado]] §3d), contra los ~210 que habría costado Avatar 6.
  - **14 B-rolls, todos clips reales de TikTok** (nada de stock ni de imágenes fijas), bajados con `yt_dlp` y recortados para sacarles el texto quemado y las marcas de otros.
  - **9 placas** (5 bonos con su valor, el total de $167.600, el precio, el sello de 30 días y el CTA) en jade y bermellón con borde dorado.
  - **Subtítulos** de 2 palabras en mayúscula, blanco con borde negro y la palabra clave en amarillo, al estilo del VSL original. Alineados contra el guion, no contra Whisper.
  - Música: la cama `bed_B` de [[herrero-de-finde]] a -8 dB con ducking.
- ✅ **VSL montado en el quiz (2026-11-04).** Embed de Panda (`76429faa-953f-465b-a471-d49836a1c952`, player `vz-588b0437-276`) dentro de `<template id="vsl-template">`. **`SEGUNDOS_OFERTA: 240`**: Santiago lo pidió a los **4 minutos** de llegar a la slide, no en el segundo del precio (7:18).
  - **Probado en el navegador**, los 10 pasos: el embed carga en 9:16 (396x704), la oferta arranca oculta, se destraba con `panda_timeupdate` a los 439 s y los 5 CTAs apuntan al checkout (el dominio se corrigió el 2026-11-05).
  - De paso se corrigió un resto del quiz militar: el apelativo por defecto decía **"Guerrera"** y pasó a **"Aprendiz"**.
  - **`#cta-vsl`: botón al checkout pegado abajo del video** (2026-11-04, pedido de Santiago: *"abajo del VSL ya les pongas un botón de CTA que los redirija directo a checkout, como para que no tengan que deslizar tanto"*). Aparece con el mismo disparador que la oferta y usa `data-cta`, así que hereda el link y los UTMs.
- ⏳ **Falta:** que el player de Panda arranque con sonido (se configura en el panel de Panda, no en el HTML).
- ✅ **Checkout confirmado (2026-11-05):** Santiago pasó `https://taichi-fit.impultienda.ar/checkout` (*"quiero que todos los botones del cta de la ultima slide redirijan a este checkout"*). Responde **200**. El dominio viejo que teníamos puesto (`tai-chi-fit`, con guion) era el que daba "Tienda no encontrada". Se cambió en `CONFIG.LINK_CHECKOUT` del `.txt`, del `.html`, del `PRUEBA.html` y de la copia en OUTPUTS, y se verificó en el navegador: **los 6 `data-cta` van a `taichi-fit.impultienda.ar/checkout` y arrastran los UTMs**.
- ⚠️ **La foto de la Maestra Valentina para el avatar.** La del quiz (`imagenes/maestra-valentina.png`) es 1:1 y HeyGen le pondría barras blancas. La v1 salió en cuerpo entero (rechazada por artificial) y la v2 con el fondo cargado. **La buena: asiática, unos 50 años, sentada, plano medio, pared lisa y vacía, look de foto de celular** ([[vsl-reglas-de-armado]] §3).
- **El guion quedó alineado con el quiz** en seis puntos que no coincidían: el manuscrito, el puente entre "tu raíz" y la Fase Raíz, Fluir como **core y glúteo** (no cadera), el espacio de una toalla, "no se trata de terminar reventada" y la versión adaptada de cada movimiento.
- ⏳ `SEGUNDOS_OFERTA` está en 230 de prueba: se fija con el segundo exacto en que **nuestro** VSL dice el precio.
- ⏳ Los anuncios quedan para después del quiz.

## Preguntas abiertas
- ¿El VSL va con MP4 propio (player nuestro) o con Panda?
- ¿Se reusa algo del producto viejo de Tai Chi Fit o se arma de nuevo?

## Relacionado
[[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[pilates-hormonal]] · [[vsl-reglas-de-armado]] · [[funnel-hacking]]

## Fuentes
- Conversación del 2026-10-26 (pedido de Santiago + ad de la Biblioteca de Anuncios `id=1409155014494163`)
- `https://calisteniafeminina.site/` y `https://calisteniafeminina.site/vsl.html`
- Entregables: `~/Desktop/tai-chi-fit/` y `OUTPUTS/2026-10-26-quiz-tai-chi-fit.html`
