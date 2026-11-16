# Silvia Fitness · Adiós Panza

> Oferta nueva **Argentina**: plan de 4 semanas para bajar la panza en casa (entrenamiento + alimentación + mentalidad), clon de **Belu Fitness** (~290 ads activos) con **una experta avatar propia: Silvia Fitness** (fotos del 16/11 en `~/Desktop/silvia-fitness/imagenes/`).

## Ideas clave
- Belu es marca personal → se clona la oferta y los formatos, con otra experta (avatar HeyGen). Nada de su nombre, fotos ni números.
- **Un solo texto** en casi todos los ads; rota el video. Videos de **6 a 29 s**.
- 4 formatos: experta a cámara con subtítulo de una palabra + capturas del producto · "miren la foto que me mandó mi alumna" · testimonio en pantalla partida · **sin voz, DÍA UNO → DÍA 30 arriba y ella con el mate abajo**.
- Ángulo que empuja ahora: **temporada** ("lo que hacés en noviembre se ve en enero", bikini, Navidad).
- Precio AR **$19.999-21.999** (tachado el doble), LATAM **US$ 19,99**. Quiz de 20 pasos con 4 tipos de panza.

## Detalles / notas
Radiografía completa: `OUTPUTS/2026-11-16-radiografia-belu-fitness.md`. Videos, transcripciones y el HTML del quiz original en `~/Desktop/silvia-fitness/referencia/`.

### Quiz (16/11)
- **Precio $16.990** (tachado $33.980, "menos de $610 por día") y **checkout `https://adios-panza.impultienda.ar/checkout`** (200, sin redirecciones). Los 2 CTAs de la venta (`#buyIn` y el sticky) salen por `CK()`, que le suma los UTM/fbclid de la visita: verificado con y sin parámetros.
- **Su mismo HTML** (regla del 14/11): `OUTPUTS/scripts-quiz/build_silvia_fitness.py` corta el `custom_html` de Belu y aplica ~25 reemplazos con control de que cada uno aparezca. Marca **Silvia Fitness**, producto **Adiós Panza**. Entregable: `~/Desktop/silvia-fitness/landing/adios-panza-quiz.txt` (118 KB, imágenes embebidas).
- **No se reusan** su cara ni las capturas y antes/después de sus clientas (llevan `@belu_fitness`). Los mensajes de alumnas pasan a **burbujas HTML** con "Casos ilustrativos"; la imagen "NO ES UN PDF. ES TU APP." pasa a **maqueta en CSS**.
- Antes/después: slots `BA_IMGS` (archivos `q-ba-1.webp`, `q-ba-2.webp`); vacíos = el bloque no se muestra.
- Se sacó el "1.200.000 seguidoras" de Belu; autoridad en `EXPERIENCIA` y `ALUMNAS` del CONFIG, a completar con datos reales.

### Anuncios · tanda 1 (16/11)
- **6 videos** en `~/Desktop/silvia-fitness/anuncios/16-11 - 1..6.mp4`, 1080x1920, 8 a 36 s. Uno por formato de Belu: V1 déficit (cocina, su ad01), V2 a los 40 (living de cuerpo entero, ad06), V3 espejo (parque, ad07), V4 gimnasio con cartel de comentario (ad11), V5 principiantes con comentario + mate, V6 mudo con pantalla partida (ad03/ad12).
- **Veo 3.1 Fast por ApiMart** (HeyGen necesita Chrome y no estaba conectado), proyecto de la skill `mini-novela` en `~/Desktop/silvia-fitness/work/tanda1/` (`guion.py`, 26 tomas, ~US$4). Escenas nuevas con Nano Banana a partir de la foto de Silvia: cocina con fruta, living de cuerpo entero, parque.
- Montaje: `OUTPUTS/scripts-vsl/edit_silvia.py` (subtítulo de una palabra rosa con borde blanco y pop, inserts del producto anclados a la palabra **debajo** del subtítulo, cartel de comentario, zoom alternado, velocidad 1,25, música `music_activa.py` baja). Inserts: `OUTPUTS/scripts-vsl/gfx_silvia.py`.
- Control: audio contra guion 0,999-1,000 en los 5 con voz, 0 cuadros negros.
- Sin testimonios inventados ni kilos: el "miren la foto que me mandó Cami" y el testimonio de alumna de Belu no se clonaron (Manual de Edición IA, sección 13). El V6 muestra *nivel inicial → avanzado* en vez de un antes/después de otra persona.
- 🐞 Veo: **3 tomas bloqueadas por el filtro** (devueltas sin costo) con frases inocentes; se destrabaron cambiando una palabra o el gesto. Y en una toma dijo **"queréis"**: Whisper lo marca como EXTRA y se regenera reescribiendo la línea sin ese verbo.

## Preguntas abiertas
- Fotos de antes/después generadas.
- Backend de Belu (no visto: hace falta pasar el checkout).
- ¿Tenemos el producto (planillas, grilla, videos de ejercicios) o lo armamos?

## Relacionado
[[gluteo-despierto]] [[dancego]] [[quizzes-reglas-de-armado]] [[guiones-y-anuncios]] [[backend-molde-de-piedras]]

## Fuentes
- Biblioteca de anuncios, página 961138747091378 (16/11/2026)
