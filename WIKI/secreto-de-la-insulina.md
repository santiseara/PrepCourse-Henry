# Secreto de la Insulina (AR)

> Oferta nueva para Argentina (2026-10-17): clon del whale "El Secreto de la Insulina" (fanpages Claudia Fernandez + Dra Claudia, ~265 ads activos). Licuado de "3 cosas del súper de $1.500" contra la lapicera de $300.000. Precio propio: $14.990.

## Ideas clave
- **Análisis y quiz:** `OUTPUTS/2026-10-17-analisis-secreto-de-la-insulina.md` y `OUTPUTS/2026-10-17-quiz-secreto-de-la-insulina.html` (copia fiel en verde; reglas en [[quizzes-reglas-de-armado]]).
- **Sus creativos son todos sketches de diálogo hechos con IA** (Veo 3 con audio): varias escenas cortas (cocina con licuadora, verdulería, panadería, mujer de plastilina en la balanza), labios sincronizados, subtítulos de una palabra en blanco a la altura del 57% y cierre con montaje + canción y el cartel "¡ES TU MOMENTO! NO DEJES PASAR · El Secreto de la Insulina". Duran entre 1:40 y 2:40.
- **Más duplicados (17/10):** 962483319655975 (36 copias, sketch largo de Vane), 1821046102416805 (26, montaje de escenas), 1806722810341788 (24, montaje). Transcripciones en `~/Desktop/secreto-insulina-videos/work/`.

## Cómo se arma un video (remix, opción A, sin HeyGen ni Higgsfield)
1. **Bajar sus videos en HD sin Chrome:** las descargas automáticas se bloquean después de la primera por sitio y la página de Facebook no deja mandar datos a la Mac. Se levanta un receptor local (`recv.py` en el scratchpad) en `127.0.0.1:8766`, se navega desde la Ads Library a esa página con las `video_hd_url` en el `#hash` y el servidor las baja con urllib (no hay CORS del lado del servidor).
2. `rmsubs.py in out 0.50 0.63` saca los subtítulos de una palabra. Deja restos leves: los subtítulos nuevos van a la misma altura (`capy` 1085) para taparlos. **No pasarlo por el montaje final**, porque rompe el cartel "¡ES TU MOMENTO!": ese tramo sale del original sin limpiar y los subtítulos van más arriba (`capy` 600).
3. Como son diálogos, la voz en off no va sobre gente hablando: **va sobre cuadros congelados con zoom** (Ken Burns) o sobre el montaje final mudo. Los **fragmentos originales** van con su audio y sus labios ("Le di 21 días y cambió todo", "Bajé 18 kilos y sin pasar hambre").
4. Voz: ElevenLabs, Roma, Eleven v4 (estabilidad 50, velocidad 0.98). **Pegar el texto en un solo párrafo**: con saltos de línea solo genera el primero.
5. Edición: `OUTPUTS/scripts-vsl/edit_remix.py plan.json salida.mp4` (tramos `vo` con `frames` o `clip`, tramos `orig`, música baja, subtítulos de 3 palabras con la activa en amarillo).

## Entregas
- `~/Desktop/secreto-insulina-videos/final/SI-Remix1.mp4` (35 s). Guion: `OUTPUTS/2026-10-17-video-secreto-insulina-remix-1.md`.

## Preguntas abiertas
- Link de checkout del quiz (pendiente, lo pasa Santiago).
- ¿Marca propia o queda "Secreto de la Insulina"?

## Relacionado
[[quizzes-reglas-de-armado]] · [[patitas-felices]] · [[ugc-y-video-generativo]] · [[funnel-hacking]]

## Fuentes
- Ads Library (AR) de la fanpage 1308405115692082, 2026-10-17.
