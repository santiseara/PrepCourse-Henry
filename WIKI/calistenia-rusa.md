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
| Paleta | **Verde oscuro #1F6B47 + grafito #101418 sobre blanco** (el original es azul iOS) |
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

Después: **pantalla de análisis → perfil → VSL con la oferta oculta**.

El perfil se acortó a pedido de Santiago (*"la slide que muestra el resumen tiene mucha info, se hace muy larga"*): pasó de 2.200 px a 1.234 px. Quedó **una** tarjeta con las dos barras (IMC y testosterona) y un solo aviso, **4 chips** en vez de 6, y el gráfico de previsión con **3 logros** en vez de 5. Se fueron el aviso de riesgos del IMC, el título largo de testosterona y la línea del 83,7%.

**Se fueron:** los 2 muros de texto del método, el bridge de bienvenida, partes del cuerpo, sentadilla, flexibilidad, día típico, biotipo (+ su pantalla de resultado), bridge de dolores, bridge de intensidad, agua, sueño, alimentación, energía, bridge de testosterona, "¿estás listo?", "plan casi listo" y la segunda página de venta duplicada.

## Paleta
**Verde oscuro #1F6B47** + grafito #101418 sobre blanco. El primer armado salió en rojo soviético y Santiago lo cambió: *"los colores reemplaza el rojo por un verde que quede bien, medio oscurito"*. Es el mismo verde de [[secreto-de-la-insulina]]. Las barras de riesgo (IMC, testosterona) **no** usan el verde de marca en el extremo malo: van de verde a rojo #B3261E, y el aviso de cupos también queda en rojo, para que el color siga significando lo mismo.

## Imágenes
Primer armado: 29 reusadas del quiz original. Santiago: *"las imágenes son muy malas, busca otros quiz de calistenia militar que tengan mejores fotos, y usa esas"*.

**De dónde salieron las nuevas**
- **Menletics** (`menletics.com`, "#1 Military Calisthenics Home Workout App for Men", anunciante *Military Calisthenics HQ* en la Biblioteca con ~22 ads activos en AR). Se llega por la Biblioteca de Anuncios → el ad muestra el dominio. Sus imágenes están en `funnelmedia.flmng.live/cdn-cgi/image/width=1200,.../menletics/landing/…` y se bajan directo del HTML de `/start` y de la home. De ahí: **las 3 fotos del selector de edad** (hombres de 35, 45 y 58, fondo negro, luz de estudio), la **foto de flexiones** y las de método y entrenamiento.
- **Muscle Booster** (`musclebooster.welltech.com`, redirige desde `musclebooster.fitness`): sus imágenes están en `/_astro/`. Ojo: hay que pedirlas al host final, en `musclebooster.fitness` devuelven vacío.
- **`quiz.calistenia.app`** (Desafío de Calistenia Militar, ES): tiene las siluetas de tipo físico con nombres clarísimos (`cali-slim-man`, `cali-overweight-man`, `cali-obese-man`), pero **las sirve a 96×96**. No sirven.

**Lo que se arregló de las originales**
- Las siluetas de cuerpo actual y cuerpo deseado eran **WebP con alfa y basura en los píxeles transparentes** (bandas de colores) y medían 342 px. Se recortaron al bounding box del alfa (umbral 24), se montaron sobre una **tarjeta cuadrada de 600 px con un degradé gris muy suave** y quedaron todas iguales. Es el arreglo que más cambió la percepción.
- La flecha del antes/después pasó de azul a verde de marca con Pillow, **mapeando solo el matiz azul** (0,55–0,70). Un segundo pase sobre rojo le había pintado la cara al modelo: el recoloreo se hace **siempre desde el original y en un solo pase**.
- Las tres fotos del paso "objetivo" no tenían reemplazo bueno, así que **esa pregunta pasó a lista con íconos**.

**Pasos sin foto.** Santiago sacó dos imágenes que no sumaban: la del hombre en el gimnasio oscuro en *"¿Ya probaste la calistenia rusa?"* (*"esta imagen quedó muy mal, no quiero imagen ahí"*) y la del hombre sentado en la cama en *"¿Cuándo fue la última vez que sentiste orgullo de tu cuerpo?"*. Con las de objetivo, son **tres pasos que quedaron solo con opciones**: una pregunta clara no necesita foto, y una foto de relleno hace más daño que ninguna.

**Generadas con Higgsfield** (gpt_image_2, 1k, High, 1:1): el **mockup del celular** con la app en verde, y el **retrato del hombre de 65** que faltaba para el rango +60 (el set de Menletics llega hasta ~58). Se pidió con el mismo encuadre, fondo negro y remera verde oliva, y entra en el set sin que se note.

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
