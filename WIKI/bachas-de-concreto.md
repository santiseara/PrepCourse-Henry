# Bachas de concreto (oferta en inglés)

> Clon para EE.UU. del curso argentino "De Cemento a Negocio" (página "Martin Ferreyra" en Meta, ~79 anuncios activos en octubre de 2026). Se traducen sus mejores ads y se editan sobre B-roll de TikToks de terceros, porque sus visuales tienen marca de agua. (fuente: pedido de Santiago del 2026-10-18)

## Ideas clave
- **Producto:** curso para fabricar bachas (lavatorios) de concreto fino desde cero y venderlas. Materiales, mezclas, moldes caseros, acabado premium, cómo presentarlas y venderlas.
- **Competidor:** biblioteca de Meta, page id `748547031665721`. Todos sus ads son **voz en off de 60 a 108 s** sobre video de fabricación, con CTA "Hacé clic en Más información".
- **Sus 3 ADN ganadores** (los más viejos que siguen activos, ordenados por antigüedad):
  1. **"Hoy genero más de 1.200.000 por mes con algo que solo quería probar"** (desde el 3/10, el más viejo). Primera bacha → "¿la vendés?" → pedidos → no empecé siendo experto.
  2. **"Lo que empezó como un momento para desconectarme terminó siendo mi trabajo"** (6 variantes del 7 al 9/10). Foto en Instagram → "¿Dónde la compraste? ¿Cuánto sale?" → primer pedido → otro → hoy me dedico a esto.
  3. **"Más de 700 mil en una semana fabricando bachas. ¿Te imaginás?"** (6 variantes del 7 al 9/10). Objeción (experiencia, herramientas caras) → qué aprendés (materiales, acabado premium, moldes sin gastar una fortuna) → CTA.
- En los ads nuevos (del 12 al 16/10) usa el nombre del método y testimonios de "700 mil por semana". Los más viejos no nombran el producto.

## Cómo se arma un video
1. **Descargar sus ads:** el CSP de Facebook bloquea mandarlos a un servidor local. Lo que anda es bajar todos los `<video>` desde la página con `fetch`, concatenarlos en un único Blob y una sola descarga (`fb_ads_concat.bin`), y después partirlo por tamaños en Python. Se transcriben con faster-whisper (modelo `base` alcanza para leer el guion), empezando por los más viejos.
2. **Visuales:** TikToks que pasa Santiago, bajados con `yt-dlp` (instalado con `pip install --user`). TikTok falla seguido, así que se reintenta en loop. Salen sin marca de agua.
3. **Voz: Google AI Studio → Generate speech** (Gemini 3.8 Flash TTS, gratis y sin créditos). **Voz de hombre de unos 40: Knox** (Masculine, "warm and conversational", tono grave), con el estilo: *"American man around 40, a hands-on craftsman telling his own story on TikTok. Warm, genuine, confident and conversational, a little excited, brisk natural pace, no announcer tone."* El texto se pega en el bloque, se genera con **cmd+Enter** (Run queda bloqueado mientras suena el audio anterior: primero hay que pausarlo) y se baja con el ícono de descarga (`Generated Audio ….wav`). Ojo: si el menú de Style queda abierto, lo que tipeás no entra en el bloque de texto. "Roma" no existe en AI Studio (es de ElevenLabs y HeyGen).
4. **Edición:** `OUTPUTS/scripts-vsl/edit_broll.py plan.json salida.mp4`. Voz sin silencios a **1.2x**, un corte de visual cada ~4–5 s (siempre al final de una palabra), zoom suave alternado, whoosh bajo en cada corte, subtítulos de 3 palabras con la activa en amarillo y música baja. El primer plano siempre en movimiento (un desmolde).
5. **Entrega:** `~/Desktop/bachas-concreto/` con los videos y `guiones-videos.md`.

## Detalles / notas
- **Experto: Mark Ross.** Se lo puede nombrar cuando suma: "Mark Ross's method" en los testimonios, y "I'm Mark Ross" cuando habla el experto (guion C).
- **Visuales a cuidar:**
  - `@modina.concreto/7639408597457210644` tiene un cartel con el nombre y el teléfono arriba. Se usa con zoom 1.9 recortado abajo.
  - `@modina.concreto/7671339958967225618` tiene transiciones con blur en 3,3–4,5 s, 13,6–13,9 s y 16,9–17,2 s. Hay que excluirlas.
  - `@concepto.cemento/7389081667157150982` muestra la interfaz de la cámara desde los 8 s.
  - `@tunegocioenconcreto/7458959238283513094` muestra etiquetas en español (Bulimix, "Polímero") entre los 19 y los 22 s.
- **Adaptación a EE.UU.:** los pesos pasan a dólares creíbles ($3,000 por mes y $1,200 por semana), sin nombre de experto ni de producto, con CTA "Tap Learn More".
- **Largo:** se respetó el largo del competidor (45 a 76 s editados), no el máximo de 30 s de [[guiones-y-anuncios]], porque el pedido fue traducir sus ganadores.

## Activos
- Videos del 2026-10-18: `BC-A-hoy-gano-3000.mp4` (57 s), `BC-B-momento-para-mi.mp4` (71 s) y `BC-C-1200-en-una-semana.mp4` (42 s), rehechos con voz de hombre (Knox).
- Guiones en inglés y español: `OUTPUTS/2026-10-18-guiones-bachas-concreto-en.md`.

## Preguntas abiertas
- ¿Nombre del producto en inglés, landing y precio?
- Faltan sus ganadores de imagen (si los tiene) y el texto principal en inglés.

## Registro de correcciones
- **2026-10-18 · Voz de hombre, no de mujer.** La primera tanda salió con Nika (femenina) y Santiago la rechazó: "la voz tiene que ser de un hombre, de unos 40 años". Regla: en esta oferta la voz siempre es masculina, de unos 40 (Knox). Además, el experto es **Mark Ross** y se lo puede nombrar si hace falta.

## Relacionado
[[guiones-y-anuncios]] · [[patitas-felices]] · [[secreto-de-la-insulina]] · [[internacionalizacion]] · [[funnel-hacking]]

## Fuentes
- Biblioteca de anuncios de Meta, página "Martin Ferreyra" (consultada el 2026-10-18)
- TikToks de visuales que pasó Santiago (7, uno repetido)
