# Kit Patitas Felices

> Oferta nueva para Argentina (2026-10-16): 200 recetas naturales para perros + 4 bonos, a $16.990. Clon de la oferta brasileña "Tigela Cheia" (tigela-cheia.lovable.app, R$24,90).

## Ideas clave
- **Producto (igual al de ellos):** 200 recetas + 4 bonos (Tabla de porción por peso de 3 a 45 kg, Lista Roja de 27 alimentos prohibidos, Planificador de domingo y 12 Recetas de festejo). Mockups en el historial de Higgsfield: tapa navy "PATITAS felices" y app en el celular.
- **Su ganador lejos:** "Olha a carinha dela quando eu começo a cozinhar". Tiene más de 25 copias y es siempre la misma plantilla de IA con otro dueño y otro perro: hook "mirá lo que hace / la carita" → ingredientes ("cosas que ya tenés en casa, en 15 minutitos está listo") → "él sabe la diferencia" → "una de las 200 recetas, con la porción justa para su tamaño" → "y encima 4 bonos por menos de X" → "tocá el botón y hacé la primera hoy". Dura 20–25 s, con voz en off y música de fondo.
- **Otros formatos que corren:** receta de paté en UGC (molleja de pollo, 49 s, su 2.º en impresiones), comparación balanceado vs. comida de verdad, historia de "no comía" (solo texto y música) y problema (coceira, 80 s).
- **Precio en el guion:** el competidor lo dice ("por menos de 25 reais"). Acá va "por menos de diecisiete mil pesos" o "dieciséis mil novecientos noventa".

## Cómo se arman los videos (pipeline)
1. Sus videos tienen los **subtítulos quemados** y no hay versión limpia para bajar. Se sacan con `OUTPUTS/scripts-vsl/rmsubs.py` (inpainting de OpenCV en la franja de 68–86% de alto) y la marca de agua con `delogo`.
2. Su plano final (persona + perro + libro o app "Tigela Cheia") se reemplaza: Nano Banana Pro edita el cuadro con 2 referencias (el cuadro + nuestra tapa) y Kling 2.6 lo anima en 5 s (5 créditos). Los videos de Kling se bajan por curl desde la URL de cloudfront, porque Chrome bloquea las descargas múltiples.
3. **Voz:** la hace Santiago en ElevenLabs (voz Sofía). **Regla: recortar silencios y ponerla a 1.2x** (2026-10-16).
4. Edición: `OUTPUTS/scripts-vsl/ad_edit.py`. Mete nuestro plano final en "Y encima viene con 4 bonos", re-temporiza las visuales, pone subtítulos como los de ellos (mayúsculas, 3 palabras, la que suena en amarillo, a la altura de los quemados) y música de fondo baja.
- Entregas: `~/Desktop/patitas-felices/final/`.

## Registro de correcciones
- **2026-10-16 · Guiones repetidos.** De la primera tanda (9 guiones sobre la plantilla ganadora): "los primeros dos guiones son iguales, hay varios iguales". Regla: aunque el competidor duplique la misma plantilla, en una tanda cada guion usa otra estructura ganadora suya (plantilla, receta UGC, comparación, historia). Hizo 1, 3, 4, 5 y 9, más uno de los nuevos (10 paté / 11 historia).
- **2026-10-16 · Visuales en HD, sin portugués y edición variada.** Aprobó el primer video ("me gustó") y pidió: "usá visuales en HD, que no se vean mal", "no pongas visuales que tengan textos en portugués, o si las ponés, que lo tengan en español" y "andá variando la edición". Reglas:
  - Bajar siempre la `video_hd_url` (720x1280), que está en los scripts de la Ads Library, y no la SD de 360p. Chrome bloquea las descargas automáticas después de la primera de cada sitio: hay que pedirle a Santiago que las habilite y bajar cada video desde su propia pestaña.
  - Las páginas del libro en portugués se traducen con Nano Banana y se animan con Kling, y se insertan con `--insert`. Los textos quemados blancos y sin borde se borran con el modo `white` de `rmsubs.py`.
  - Cada video de la tanda lleva otro estilo de subtítulos (`--style` classic, pop, box, lower, tiktok o story) y otro extra (zoom lento, barra de progreso, título de hook).
  - **Kling:** antes de generar, esperar a que la imagen termine de subir (que el preview deje de ser `blob:`). Si no, genera texto a video sin la imagen y se pierden créditos. Así se perdieron 4 clips (20 créditos).
- **2026-10-16 · Voz rara y lenta → Roma en Eleven v4.** De los guiones 4 y 9 hechos con Sofía (Multilingual v2, estabilidad 30) dijo: "quedó mal la voz, suena muy rara, habla lento y feo". Desde ahora la voz la genero yo en ElevenLabs (cuenta con créditos que abrió Santiago), con la voz **"Roma"** (español argentino, biblioteca) y el modelo **Eleven v4**, con estabilidad 50 y velocidad 0.98 (habla a ~3,3 palabras/s). Recorte de silencios más suave (0.25 s / quedan 0.13 s) + 1.2x. Los subtítulos se arman con el texto exacto del guion (`--script`), porque Whisper escucha mal algunas palabras ("Entráis sitio").
- **2026-10-16 · Voz en off.** "Acordate de recortar silencios y de ponerle velocidad 1.2." Se arma 1 video primero y, si lo aprueba, el resto.

## Preguntas abiertas
- ¿Landing propia en Lovable clonada de la de ellos?

## Relacionado
[[guiones-y-anuncios]] · [[funnel-hacking]] · [[ugc-y-video-generativo]] · [[vsl-reglas-de-armado]]

## Fuentes
- Ads Library de tigela-cheia.lovable.app (55 anuncios activos, 2026-10-16), transcripciones en `~/Desktop/patitas-felices/work/transcripts.json`.
