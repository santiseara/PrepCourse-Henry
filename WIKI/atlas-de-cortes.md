# The Women's Cutting Atlas (Atlas de Cortes)

> Oferta nueva en inglés: guía visual de cortes femeninos para peluqueras y estilistas (una página por corte con divisiones, mecha guía, ángulos y el error a evitar). Es un clon de "Estilismo Con Propósito", que corre en español. (fuente: FB Ads Library, page 1341320769058929, revisada el 2026-10-21)

## Ideas clave
- **Producto del competidor:** "Atlas Visual de Cortes Femeninos" (algunos ads dicen "Mapa visual"). Pack con bonus a la vista en el cierre: guía de flequillos, tijeras y herramientas, diagnóstico de errores y cortes según el rostro ("colección completa"). Las páginas que se ven dicen "79 de 151": unas 150 páginas.
- **Avatar:** estilista que ya sabe cortar pero duda en los cortes que no hace seguido. Nunca se la trata de mala profesional: "no es falta de técnica, es memoria".
- **Página nueva:** el primer ad es del 11/10. El 21/10 tenía unos 130 anuncios, todos en video con el mismo copy. Los más duplicados (x3) son del 19/10.

## DNA de sus ganadores
| Ganador | Hook | Duplicados |
|---|---|---|
| "Saber ≠ recordar" | "Saber hacer un corte no es lo mismo que recordarlo cuando la clienta ya está sentada en el sillón" | 2 videos x3 = 6 ads |
| "La foto" | "La clienta te muestra una foto, reconocés el corte, tomás la tijera y ahí empezás a dudar" | 2 videos x3 = 6 ads |
| "A mitad del corte" | "Vas por la mitad del corte y de pronto no recordás qué sigue" | x3 |
| "¿Cuántos cortes dejás de hacer?" | El copy del ad original del 11/10 | x3 |
| Otros (18/10) | "Cada corte mal ejecutado tiene un costo" · "un lado te quedó distinto al otro" · "bob en ángulo, ¿por dónde arrancás?" | x1 |

- **Estructura (20 a 35 s):** situación concreta en el salón → "no es falta de técnica, es no tener divisiones, guía y ángulos a mano en ese momento" → lista de cortes (pixie, bob, long bob, capas, butterfly) → "por eso creamos el Atlas…" → una página por corte → "Hacé clic y empezá a usarlo hoy mismo".
- **Desactivador de objeciones:** "consultar no te hace menos profesional" y "es para consultar, no para estudiar".
- **Formato visual:** voz en off sin cara, B-roll de manos seccionando pelo (cabezas de práctica y salón), mockups de las páginas del atlas, pack de bonus al cierre y subtítulos de 1 a 3 palabras en caja rosa o fucsia.

## 🌐 Nuestra landing (2026-10-21)
> Leída del HTML que pasó Santiago. (fuente: ~/Downloads/CODIGO-PARA-COPIAR.txt)
- **Nombre:** *The Women's Cutting Atlas*. La marca del pie es "Styling With Purpose".
- **Promesa:** "Stop losing clients and money over a cut you're not sure how to do". Chequear sectioning, elevation y guide section en segundos, sin buscar en un video largo en medio del servicio.
- **Producto:** "Cut Maps", un mapa por corte con sectioning, elevation, guide y una secuencia numerada. Ejemplos: zonas de la cabeza, distribución natural, pixie con flequillo, línea diagonal hacia adelante, adaptación a rulos, bob graduado y butterfly. Módulos: principios, formas base, cortes cortos, medios y largos, y texturizados. También pixie, bob, long bob, butterfly, shag y wolf cut.
- **Dolores:** el corte que no hacés seguido (nudo en el estómago), el tutorial que no encontrás, la duda a mitad del corte, ofrecer siempre los mismos 3 o 4 cortes y la duda después del servicio.
- **Beneficios:** seguridad real, respuesta en segundos, menos correcciones, más cortes en el menú, tiempo recuperado.
- **Oferta:** $27 USD (ancla $177: atlas $97 + bonus), pago único, contador de 15 minutos, garantía de 7 días, acceso por email. Funciona en el celular o impreso.
- **5 bonus:** flequillos ($15), diagnóstico visual de cortes ($13), tijeras y herramientas ($18), capas sin líneas ($15), formas de rostro ($19).
- ⚠️ **Pendientes en la landing:** 6 capturas de reseñas en inglés. Los mockups del pack y de la colección ya los pasó Santiago el 2026-10-21.

## Detalles / notas
- Tanda 1 (21/10): 4 guiones adaptados de los ganadores + 2 variables nuestras (cuentas de la plata que se pierde por decir "ese corte no es lo mío", y la estilista con 20 años que tenía una carpetita en el cajón). Ver `OUTPUTS/2026-10-21-guiones-atlas-cortes.md`. Reescritos con los términos de la landing: Women's Cutting Atlas, Cut Maps, sectioning, elevation y guide section, sin el "error a evitar" porque los mapas no lo prometen.

## Cómo se arma un video (2026-10-21)
1. **Voz:** Google AI Studio, Gemini 3.1 Flash TTS Preview, voz femenina **Sulafat** (Warm). Scene: *"An American hairstylist in her mid 30s recording a voiceover for a TikTok ad, talking to other stylists. Warm, confident, relatable and conversational… no announcer tone"*. Se genera por JS (`_setTA(2, texto)`, click en Run y esperar que el `data:` del `<audio>` deje de crecer 3 s y pase los 300 KB). Si se captura antes, sale un WAV de 2 KB. Se manda por POST a un receptor local (127.0.0.1:8765). Salen de 32 a 39 s.
2. **B-roll:** TikToks bajados con `yt-dlp -f best` (son HEVC; con el filtro `vcodec^=h264` fallan todos). URL: `https://www.tiktok.com/@usuario/video/ID`. Seis fuentes limpias en `~/Desktop/atlas-cortes/work/tiktoks/`:
   - `7261610337856736519`: butterfly en cabeza de práctica. Usar 3–39 s y el resultado de 48–54 s. Excluir el texto del 0–2 s, el producto del 42 s y la cara del 45 s.
   - `7591869980547829047`: bob en cabeza de práctica. Tiene textos arriba, así que va con zoom 1.2 y `ybias` 1.
   - `7668379090566565128`: pixie en salón con ángulos dibujados (0°, 45°, 90°). Ideal para "elevation".
   - `7673220051054382343`: secciones con clips, clienta real.
   - `7675397335119138070`: bob rubio en salón.
   - `7429148086867479813`: bob en cabeza de práctica. Tiene el cartel "Corte Bob" abajo, así que va con zoom 1.35 y `ybias` 0.
   - Descartados: los "me lo corto en casa" (cara a cámara, otro público), los de barbería y los dúos con cara de reacción.
3. **Producto:** el mockup de páginas y el de la colección que pasó Santiago. Se recortan las páginas (Key Zones, Pixie with Fringe, Diagonal Forward Line, Curly, Natural, tapa) como placas fijas. La colección va sobre degradé berenjena en la placa final. Está en `work/stills/`. Ojo: no sacar el blanco del mockup de páginas, porque se borra el papel.
4. **Edición:** `OUTPUTS/scripts-vsl/edit_atlas.py plan.json salida.mp4`, una copia de `edit_infinity.py` con la estética del competidor: subtítulos en caja fucsia (Arial Black, minúscula, palabra activa en dorado), chips fucsia, tarjeta de precio berenjena con borde dorado y placa final "THE WOMEN'S CUTTING ATLAS" + colección + CTA fucsia. Los planes salen de `~/Desktop/atlas-cortes/work/plans/gen.py`, con anchors palabra → plano: "Sectioning" → 0°, "elevation" → 45°, "pixie" → pixie terminado, "Women's" → tapa, "Map" → página.

## Activos
- **Videos (2026-10-21):** `~/Desktop/atlas-cortes/AT-V1..V6.mp4`, de 29 a 36 s, 9:16, voz Sulafat. Guiones al lado, en `guiones-videos.md`.
  - V1 "Saber ≠ recordar", V2 "La foto", V3 "A mitad del corte" y V4 "¿Cuántos cortes rechazás?" son los del competidor.
  - V5 "La cuenta" ($70–90 → casi $1.000 por mes) y V6 "La carpetita de la estilista" son variables nuestras.
- Carpeta de trabajo: `~/Desktop/atlas-cortes/work/` (`tiktoks/`, `vo/`, `stills/`, `plans/`, `sheets/`).
- Ajustes del editor durante la tanda:
  - El anchor de la placa final gana a cualquier otro.
  - La colección queda fija hasta el último cuadro.
  - Ningún chip pisa la placa final.

## Preguntas abiertas
- ¿Funciona mejor la voz femenina (Sulafat) o conviene probar otra? Todavía no hay datos.

## Relacionado
[[guiones-y-anuncios]] · [[funnel-hacking]] · [[seleccion-y-modelado-de-oferta]] · [[bachas-de-concreto]] · [[infinity-3d]]

## Fuentes
- ~/Downloads/CODIGO-PARA-COPIAR.txt (HTML de la landing propia)
- FB Ads Library, Estilismo Con Propósito (13 videos transcritos con Whisper el 2026-10-21)
