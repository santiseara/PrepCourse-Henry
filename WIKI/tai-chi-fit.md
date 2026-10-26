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
| Checkout | ImpulTienda — `https://tai-chi-fit.impultienda.ar/checkout` *(a confirmar)* |
| Instructora | Maestra Valentina (+10 años · 50.000+ alumnas) |
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

## Estado
- ✅ Quiz entero armado y probado paso por paso: `~/Desktop/tai-chi-fit/`.
- ⏳ **Falta el VSL.** El guion se va a modelar de la página de calistenia asiática para hombres que Santiago todavía no mandó.
- ⏳ `SEGUNDOS_OFERTA` está en 230 de prueba: se fija con el segundo exacto en que **nuestro** VSL dice el precio.
- ⏳ Falta confirmar el link de checkout.
- ⏳ Los anuncios quedan para después del quiz.

## Preguntas abiertas
- ¿El link de checkout de ImpulTienda es `tai-chi-fit.impultienda.ar`?
- ¿El VSL va con MP4 propio (player nuestro) o con Panda?
- ¿Se reusa algo del producto viejo de Tai Chi Fit o se arma de nuevo?

## Relacionado
[[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[pilates-hormonal]] · [[vsl-reglas-de-armado]] · [[funnel-hacking]]

## Fuentes
- Conversación del 2026-10-26 (pedido de Santiago + ad de la Biblioteca de Anuncios `id=1409155014494163`)
- `https://calisteniafeminina.site/` y `https://calisteniafeminina.site/vsl.html`
- Entregables: `~/Desktop/tai-chi-fit/` y `OUTPUTS/2026-10-26-quiz-tai-chi-fit.html`
