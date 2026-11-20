# Secreto de la Insulina (AR)

> Oferta para Argentina: licuado de "3 cosas del súper de $1.500" contra la lapicera de Ozempic de $300.000.
> Arrancó el 2026-10-17 como clon del whale argentino (fanpages Claudia Fernandez + Dra Claudia, ~265 ads activos).
> Desde el **2026-11-20** la oferta ya es **propia y corre en Brasil** (`segredo-insulina-quiz.vercel.app`, R$ 37),
> y lo que se hizo fue **traerla de vuelta a Argentina**: el mismo quiz, en voseo, a **$16.990**.

## El quiz argentino (20/11/2026) — el brasileño propio, calcado

- **Entregable:** `~/Desktop/secreto-insulina/landing/secreto-insulina-quiz.txt` (**746 KB**, listo para
  pegar en ImpulTienda, las 14 fotos adentro). Prueba: `secreto-insulina-PRUEBA.html`. Fuente editable:
  `landing/quiz.html` + `imagenes/`. Copia: `OUTPUTS/2026-11-20-quiz-secreto-insulina-ar.html`.
- **El original es una SPA de React de Lovable**, no un HTML: las 28 pantallas viajan como componentes
  JSX minificados en `assets/index-*.js` (cómo se desarma, en [[quizzes-reglas-de-armado]], regla del 20/11).
  Se clonó **su diseño exacto** — tokens del `:root`, Poppins, coral `25 100% 50%`, verde `145 63% 42%`,
  `.quiz-option` / `.btn-quiz` / `.gradient-text` / la barra de progreso — sobre un motor propio en JS plano.
- **Las 28 pantallas, en orden:** portada con la médica → edad → tipo de cuerpo → zonas → "no estás sola"
  (87,4 %) → nota de divulgación → nombre → qué te molesta → intentos previos → "tu cuerpo aprendió a
  resistir" → frenos → lapicera vs. mezcla → metas → hinchazón → cómo actúa (4 tarjetas) → peso → altura →
  peso deseado → rutina → sueño → gráfico de previsión → compromiso → qué resultado primero →
  **carga del análisis** → análisis listo (IMC + alertas + diagnóstico dinámico) → testimonios →
  **armando la rutina (8,5 s)** → oferta.
- **Precio: $16.990**, tachado **$134.900** (el x7,94 del original), **6 cuotas de $2.832** con Mercado
  Pago. Checkout **relativo `/checkout`** hasta que Santiago pase el definitivo: se cambia **una sola
  línea**, `CONFIG.CHECKOUT`.
- **Las tres cifras del mecanismo viven en el `CONFIG`:** mezcla `$1.500`, lapicera `$300.000`, semana `$4.500`.
- **El logo se retipeó, no se regeneró:** "SEGREDO DA" → "SECRETO DE LA" sobre la misma parábola, con
  Montserrat Black y el color exacto (`#FE8602`); **INSULINA quedó intacta**
  (`OUTPUTS/scripts-quiz/logo_secreto_insulina.py`).
- ⚠️ **La captura falsa del G1 (Globo) no se clonó** (regla del 18/11). En su lugar va una **tarjeta de
  divulgación sin marca**, en HTML: volanta *SALUD · NOTA DE DIVULGACIÓN*, titular, la foto de la médica
  con faja de epígrafe, dos párrafos y el pie *"No reemplaza la consulta con un profesional de la salud"*.
- 🚩 **Pendiente de decisión de Santiago:** el **paso 22 (el compromiso)** quedó porque pidió copiar todo,
  pero la regla del 19/11 lo saca en todo quiz de salud. Es un `ir()` menos y no califica nada.
- 🐞 **Heredado del original, replicado a propósito:** la tabla de la estadística del paso 5 está indexada
  por rangos de edad que **no existen** en el paso 2, así que siempre muestra 87,4 % / 40 años.

## Ideas clave
- **Análisis y quiz:** `OUTPUTS/2026-10-17-analisis-secreto-de-la-insulina.md` y `OUTPUTS/2026-10-17-quiz-secreto-de-la-insulina.html` (copia fiel en verde; reglas en [[quizzes-reglas-de-armado]]).
- **Sus creativos son todos sketches de diálogo hechos con IA** (Veo 3 con audio): varias escenas cortas (cocina con licuadora, verdulería, panadería, mujer de plastilina en la balanza), labios sincronizados, subtítulos de una palabra en blanco a la altura del 57% y cierre con montaje + canción y el cartel "¡ES TU MOMENTO! NO DEJES PASAR · El Secreto de la Insulina". Duran entre 1:40 y 2:40.
- **Más duplicados (17/10):** 962483319655975 (36 copias, sketch largo de Vane), 1821046102416805 (26, montaje de escenas), 1806722810341788 (24, montaje). Transcripciones en `~/Desktop/secreto-insulina-videos/work/`.

## Cómo se arma un video (remix, opción A, sin HeyGen ni Higgsfield)
1. **Bajar sus videos en HD sin Chrome:** las descargas automáticas se bloquean después de la primera por sitio y la página de Facebook no deja mandar datos a la Mac. Se levanta un receptor local (`recv.py` en el scratchpad) en `127.0.0.1:8766`, se navega desde la Ads Library a esa página con las `video_hd_url` en el `#hash` y el servidor las baja con urllib (no hay CORS del lado del servidor).
2. `rmsubs.py in out 0.50 0.63` saca los subtítulos de una palabra. Deja restos leves: los subtítulos nuevos van a la misma altura (`capy` 1085) para taparlos. **No pasarlo por el montaje final**, porque rompe el cartel "¡ES TU MOMENTO!": ese tramo sale del original sin limpiar y los subtítulos van más arriba (`capy` 600).
3. Como son diálogos, la voz en off no va sobre gente hablando: **va sobre cuadros congelados con zoom** (Ken Burns) o sobre el montaje final mudo. Los **fragmentos originales** van con su audio y sus labios ("Le di 21 días y cambió todo", "Bajé 18 kilos y sin pasar hambre").
4. Voz: ElevenLabs, Roma, Eleven v4 (estabilidad 50, velocidad 0.98). **Pegar el texto en un solo párrafo**: con saltos de línea solo genera el primero. Para una tanda, **todas las voces en una sola generación** (una sola descarga, porque Chrome bloquea las siguientes) y después se cortan por guion alineando con Whisper.
5. Edición: `OUTPUTS/scripts-vsl/edit_remix.py plan.json salida.mp4` (tramos `vo` con `frames` o `clip`, tramos `orig`, música baja, subtítulos de 3 palabras con la activa en amarillo).

## Entregas
- **Todo en una sola carpeta plana: `~/Desktop/secreto-insulina/`** (quiz .txt y PRUEBA, imágenes `img-*.webp`, videos `SI-Remix1..6.mp4`, `guiones-videos.md`). El material de trabajo (videos de referencia, limpios, voces, planes) va al scratchpad, no al escritorio.
- Guiones: `OUTPUTS/2026-10-17-videos-secreto-insulina-remix-1-6.md`.

## Registro de correcciones
- **2026-10-17 · "No quiero que el principio sea estático."** El Remix 1 arrancaba con un cuadro congelado. Regla: **el video arranca siempre con imagen en movimiento** (un fragmento original con su audio como hook). Los congelados solo van en el medio, cortos (1,5–2,5 s) y con zoom más marcado (hasta 1,2x).
- **2026-10-17 · "Entregame todo en una misma carpeta, no me crees carpetas distintas."** Regla: una oferta = una carpeta en el escritorio.
  ⚠️ **Reemplazada el 2026-10-22** por la estructura que ya usan [[limpia-dolor]] y [[helados-que-venden]]:
  `~/Desktop/<oferta>/` con `landing/`, `imagenes/` y `anuncios/`. Lo que Santiago no quería eran carpetas
  sueltas por entrega (`-videos`, `-imagenes`), no las tres subcarpetas fijas. El material de trabajo sigue
  yendo al scratchpad.

## Preguntas abiertas
- **Link de checkout** (pendiente, lo pasa Santiago). Mientras tanto el quiz va con `/checkout` relativo.
- ¿El paso del compromiso se saca (regla del 19/11) o queda?
- ¿Marca propia o queda "El Secreto de la Insulina"?
- Falta el pixel de Meta (`CONFIG.PIXEL_ID`, hoy vacío).

## Relacionado
[[quizzes-reglas-de-armado]] · [[patitas-felices]] · [[ugc-y-video-generativo]] · [[funnel-hacking]]

## Fuentes
- Ads Library (AR) de la fanpage 1308405115692082, 2026-10-17.
- `segredo-insulina-quiz.vercel.app` (la versión brasileña propia), bundle `assets/index-DX5_2SFZ.js`, 2026-11-20.
