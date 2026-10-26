# Calistenia Rusa (Coach Santi)

> Oferta nueva para hombres 40+ en Argentina. El ángulo es la **diferenciación**: todos venden *calistenia militar*, nosotros vendemos **calistenia rusa**. Embudo quiz + VSL. El quiz se modela del de **Calistenia Asiática H40+** (oferta propia de Santiago en ImpulTienda), recortado de 21 preguntas a 14 porque la venta la hace el VSL. (fuente: conversación del 2026-10-26)

## Ideas clave
- **La diferenciación es el producto.** Santiago: *"cuando todos venden calistenia militar, nosotros nos diferenciamos ahi"*. El mercado AR ya está saturado de "Calistenia Militar" (ver [[tai-chi-fit]], que se modeló del quiz de Calistenia Militar Femenina). Rusa = mismo deseo, envase nuevo.
- **El quiz es el envase, el VSL es la venta.** Por eso se pidió *"un quiz simple, porque va a tener vsl"*. Todo lo que el VSL va a decir igual se saca del quiz.
- **Coach Santi** reemplaza al Maestro Kaito del original. Falta definir si es una persona real (foto) o un personaje.
- El mecanismo se mantiene: **activación de las fibras profundas** / musculatura interna dormida, 7 minutos por día, sin equipo. Lo que cambia es el origen: en vez de samuráis japoneses del siglo XVII, la **escuela de preparación física rusa**.

## Ficha de la oferta
| | |
|---|---|
| Producto | Calistenia Rusa — protocolo de 28 días |
| Público | **Hombres 40+** (igual que el original) |
| Idioma | Español argentino con voseo |
| Precio | **$17.990 ARS**, tachado $47.990 (62% OFF), 3 cuotas de $5.997 |
| Checkout | `https://calistenia-rusa.impultienda.ar/checkout` *(a confirmar)* |
| Coach | Coach Santi |
| Paleta | **Rojo #C8102E + grafito #101418 sobre blanco** (el original es azul iOS) |
| Tipografía | Oswald (display) + Inter |

## El original: Calistenia Asiática H40+
- **Es una oferta propia de Santiago**, corriendo en `calisteniaasiaticahombres.impultienda.ar`. Marca interna: *Lastafit*. Maestro Kaito, calistenia asiática.
- **Técnicamente:** ImpulTienda con `custom_html`, pero adentro va un **funnel de InLead exportado en texto plano** como `window.FUNNEL` (un JSON con `steps`, `design` y `navigation`). No está cifrado: se baja con `curl -sL` y se parsea directo. Las imágenes cuelgan del `storage` de Supabase de la tienda (`…/1790743888573_landing-NN.webp`, 92 archivos).
- **38 pasos:** 21 preguntas + 9 bridges de texto + loading + previsión + perfil + VSL con oferta + una segunda página de venta duplicada.
- **Oferta del original:** de $47.990 por $17.990, pago único, 30 días de garantía, 4 bonos y planes alternativos (1 mes / 3 meses / anual) al final.

## Qué se recortó y qué quedó
**Quedaron 14 preguntas** (decisión de Santiago, opción "media"):

| # | Pregunta |
|---|---|
| 1 | Edad (es la portada, no hay botón "Empezar") |
| 2 | ¿Ya probaste la calistenia rusa? |
| 3 | ¿Cuál es tu objetivo? (3 fotos) |
| 4 | ¿Cómo es tu cuerpo hoy? (4 fotos) |
| 5 | ¿Qué cuerpo querés? (3 fotos) |
| 6 | ¿Qué te molesta? (multi, emojis) |
| 7 | ¿Con qué frecuencia entrenás? |
| 8 | ¿Cuántas flexiones seguidas? |
| 9 | ¿Última vez que sentiste orgullo de tu cuerpo? |
| 10 | ¿Dolores? (multi, 2 fotos + "Ninguna") |
| 11 | ¿Cómo preferís empezar? (intensidad) |
| 12 | Altura (medidor) |
| 13 | Peso actual (medidor) |
| 14 | Peso deseado (medidor) |

Después: **pantalla de análisis → perfil (IMC + testosterona + chips + gráfico de previsión) → VSL con la oferta oculta**.

**Se fueron:** los 2 muros de texto del método, el bridge de bienvenida, partes del cuerpo, sentadilla, flexibilidad, día típico, biotipo (+ su pantalla de resultado), bridge de dolores, bridge de intensidad, agua, sueño, alimentación, energía, bridge de testosterona, "¿estás listo?", "plan casi listo" y la segunda página de venta duplicada.

## Imágenes
- **29 reusadas del original** (ninguna tiene marca ni texto): portada antes/después, las 3 del objetivo, las 4 del cuerpo actual, las 3 del cuerpo deseado, las 2 de zonas con dolor, los 4 antes/después de testimonios, 5 caras, los medios de pago y el sello "Empresa recomendada 2025".
- **Portada recoloreada:** la flecha del antes/después venía azul (paleta del original) y se pasó a rojo con Pillow, mapeando el matiz azul a rojo y conservando saturación y luminosidad. La foto queda idéntica.
- **Mockup nuevo con Higgsfield** (gpt_image_2, 1k, High, 1:1): celular negro flotando con la app en modo oscuro, estrella roja, "CALISTENIA RUSA", progreso "Día 8 de 28" y botón rojo. Salió bien al primer intento.
- **Descartadas:** todas las fotos del Maestro Kaito (asiático, rodete) y los mockups de la app con la marca vieja.

## Estado
- ✅ Quiz entero armado y probado paso por paso: `~/Desktop/calistenia-rusa/`.
- ⏳ **Falta el VSL.** Es el próximo paso.
- ⏳ `SEGUNDOS_OFERTA` está en 230 de prueba: se fija con el segundo exacto en que **nuestro** VSL dice el precio.
- ⏳ Falta confirmar el link de checkout y decidir la cara del Coach Santi.
- ⏳ Los anuncios quedan para después del VSL.

## Preguntas abiertas
- ¿El Coach Santi es Santiago (foto real) o un personaje generado?
- ¿El checkout es `calistenia-rusa.impultienda.ar`?
- ¿El precio queda en $17.990 como el de Calistenia Asiática?
- ¿El VSL va con MP4 propio (player nuestro) o con Panda?

## Relacionado
[[quizzes-reglas-de-armado]] · [[vsl-reglas-de-armado]] · [[tai-chi-fit]] · [[quiz-funnel]] · [[ofertas]] · [[shopify-y-checkout]]

## Fuentes
- `https://calisteniaasiaticahombres.impultienda.ar/` (quiz original, oferta propia)
- Conversación del 2026-10-26. Entregable: `OUTPUTS/2026-10-26-quiz-calistenia-rusa.html`
