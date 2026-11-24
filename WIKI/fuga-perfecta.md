# Fuga Perfecta

> Juegos de escape para imprimir y jugar en casa (PDF, AR). Clon de **casocriminal.shop** con ángulo ampliado: no solo pareja, también **familias y grupos de amigos**. Arrancó el 24/11/2026. (fuente: doc de la oferta de Santiago + 22 ads despiezados de los dos competidores)

## Ideas clave

- **El competidor no es otro juego: es salir.** Todo el mensaje se construye contra la noche de "¿qué hacemos?" que termina en Netflix.
- **El 4x1:** 3 salas completas (El Vagón, La Cabaña, El Búnker) + 7 desafíos express. Precio $19.990, tachado $59.990, garantía de 30 días reales (la de Caso Criminal son 7 días que se anulan al descargar).
- **El mecanismo que vende:** cada etapa da un número y ese número abre el sobre siguiente. Si te equivocás, no abre. Convierte un mazo de papeles en una cadena y hace imposible hacer trampa.
- **El traidor es nuestro ángulo exclusivo.** En El Búnker va un sobre extra por jugador; en uno dice "tu trabajo es que no salgan, y que no se note". Caso Criminal no puede hacerlo porque el escape cooperativo no tiene a nadie acusando a nadie.
- **Order bump:** El Kit del Escapista (+$5.900): candados de papel, cronómetro para imprimir, pulseras de equipo, certificado de escape. No vende más contenido, vende que la noche se sienta real.

## Los dos competidores, medidos

Bajados y despiezados el 24/11: **10 ads de casocriminal.shop** (88 activos) y **12 de atwistofdate.co.uk** (54 activos).

- **Un solo copy para toda la cuenta.** Los ~54 de Twist corren el mismo texto de 5 líneas con emojis; los 88 de Caso Criminal lo mismo. **No varían el texto: varían el video.**
- ⛔ La biblioteca los sirve a **360x640**: valen como molde de edición, nunca como b-roll ([[guiones-y-anuncios]], regla del 18/11).

### Molde A · el corto (7 a 16 s), SIN voz
- Música viral de fondo, con vocal en inglés ("I'll Be There for You" de Friends aparece dos veces, "Way Down We Go", pop/R&B de TikTok).
- **Una sola placa POV arriba**, fija todo el video: caja blanca con texto negro, o caja negra translúcida con texto blanco. Ejemplos: *"POV: Encontráis un plan en pareja que no consiste en salir a cenar ni ver una serie"*, *"No necesitas tablero: lo imprimes y empiezas"*, *"Netflix is cool but what if we solved an escape room?"*.
- **Banner de oferta abajo**, fijo todo el video: *"OFERTA SOLO HOY · 4×1 EN JUEGOS DE INVESTIGACIÓN"*.
- Un encuadre picado fijo sobre la mesa con **jump cuts de ~1 s** (timelapse de la noche), o 8-9 planos de detalle de 1 s.
- 🎬 **El mejor recurso que tienen:** el cronómetro proyectado en la pared del fondo, que va de 59:58 a 00:20 mientras la pareja juega. Cuenta la historia entera sin una palabra.

### Molde B · el largo (20 a 35 s), CON voz en off
- **Voz femenina joven (25-30), entusiasta, ritmo rápido, tono de amiga que te recomienda algo.** Británica en Twist, española en Caso Criminal.
- **13 a 22 cortes, promedio de 1,1 a 2,2 s** por plano. Más rápido todavía que nuestro estándar de 1,9-2,9.
- Placa de hook arriba los primeros 2-3 s y después se va. **Subtítulos dinámicos palabra por palabra** en el centro.
- Cama musical de pop acústico instrumental por debajo. Algún SFX puntual: high-five, risas, papel.
- **Cierre sin placa, sin logo y sin botón**: termina en la pareja celebrando o en un pulgar arriba.
- Estructura: dolor concreto → "probá esto" → qué es (se descarga e imprime al instante) → qué trae (enumerado y concreto) → cómo se siente → cuánto dura → cierre.
- Hay un **formato listicle** que vale copiar: *"Cheap date ideas that DON'T involve food"* → 1, 2, 3 con precio y duración de cada uno en placa.

## La tanda 1 (24/11/2026)

6 guiones en `OUTPUTS/2026-11-24-guiones-fuga-perfecta-tanda1.md`: 4 del molde B (voz) y 2 del molde A (sin voz), repartidos entre pareja, amigos y familia.

1. Contra Netflix (pareja) — **producido**, 31,8 s, 16 planos
2. El traidor (amigos)
3. Listicle de las 3 salas
4. Familia sin pantallas
5. POV corto de pareja
6. POV corto "no necesitás tablero"

- **Editor:** `OUTPUTS/scripts-vsl/edit_fuga.py` (clon de `edit_alivio.py` con caja de hook blanca, banner de oferta fijo abajo y paleta de lacre).
- **Voz:** Sulafat a `speed 1.20`, estilo de amiga porteña, `gemini-2.5-flash-preview-tts` (control de 8 palabras: 2,69 s, limpio).
- **Visuales:** las 8 que pasó Santiago (clips IA de 720x1280, 8 s) alcanzaron para el video 1 entero. Muestran el producto: sobres con lacre, cronómetro, candado de combinación, las hojas de los desafíos, el sobre del SABOTEADOR.

## Detalles / notas

- 🐞 **Dos de los clips IA tienen texto mal escrito.** El de los 7 desafíos dice *"DESAFÃO EXPRESS"* (tilde rota). Se arregla reencuadrando (`zoom 1.55`, `ybias 1.0`), no se tira el clip.
- ⛔ **tikwm estuvo caído el 24/11** (502 sostenido durante media hora). **yt-dlp no es reemplazo**: la última versión que corre en el Python 3.9 del sistema es `2025.10.14` y ya no extrae TikTok. Pasar `--cookies-from-browser` no está permitido. Las páginas de video de TikTok sirven el stream por **blob/MSE**, así que tampoco se baja desde el navegador. **Si tikwm se cae, por ahora no hay plan B: se espera.**
- ✅ **Las páginas de tag de TikTok sí se raspan** (confirma la regla del 16/11). Rindieron: `familygamenight` (83), `familygamesnight` (87), `murdermysteryparty` (100), `escaperoomathome` (77), `gamenightwithfriends` (66), `juegosdemesa` (30). **No rindieron:** `gamenight` (página no disponible, el tag está ocupado por videojuegos) ni `boardgamenight`/`escaperoom`/`datenightathome` (la SPA no cargó). Total: **407 IDs únicos**.
- Los despieces completos quedaron en el scratchpad de la sesión del 24/11.

## Preguntas abiertas

- ¿El contador de la landing va de 10 minutos (nuestra regla fija) o largo como el de ellos, que usan más de 12 horas?
- ¿Se mantiene el precio $5.000 abajo de Caso Criminal, o sube? (el criterio de Santiago es que el precio sube y no baja)
- Faltan: escribir las tres salas, el logo y la galería de jugadores de la landing.

## Relacionado

[[guiones-y-anuncios]] · [[como-trabajar-con-santiago]] · [[estilo-de-video-ia]] · [[noche-de-citas-cristiana]] · [[funnel-hacking]] · [[modelo-low-ticket]]

## Fuentes

- Doc de la oferta: *FUGA PERFECTA — Documento de la oferta* (Google Docs, 24/11/2026)
- Biblioteca de anuncios de Meta: `atwistofdate.co.uk` y `casocriminal.shop` (24/11/2026)
- OUTPUTS/2026-11-24-guiones-fuga-perfecta-tanda1.md
