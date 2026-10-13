# VSL: reglas de armado (checklist viva)

> Reglas y correcciones de Santiago para armar VSLs con avatar (después del quiz o en la landing). **Leer antes de escribir un guion de VSL o editar uno.** Cada corrección nueva se suma acá, con fecha. Contexto técnico de avatares y voces en [[ugc-y-video-generativo]]. Reglas del quiz en [[quizzes-reglas-de-armado]].

## 1. Pedido típico
- "Te paso el VSL de una oferta mía. Usá **exactamente el mismo guion**, adaptado a la oferta nueva, con acento **rioplatense**, para el público de la oferta."
- Se entrega **terminado**: avatar con labios sincronizados, B-rolls, subtítulos y edición, a **velocidad 1.3x**, en una carpeta del escritorio. **No se mete en el quiz** hasta que lo pida.

## 2. Guion
- **Estructura 1 a 1 con el original**: los mismos bloques en el mismo orden (hook, presentación, diagnóstico por el test, empatía, mecanismo, trampa, solución, producto, testimonio, bonos, anclaje, precio, escasez, garantía y cierre).
- **Alinear todo a la oferta y al quiz**: precio y tachado, bonos, minutos por día, garantía, nombre del método, entregables. El VSL no puede contradecir al quiz.
- **Tono hablado, que no suene robot** (2026-10-12):
  - frases cortas;
  - muletillas naturales ("mirá", "eh", "al toque", "decime una cosa");
  - pausas con "...".
  - **Presentación: "Soy la Maestra Caro"**, nunca "Me llamo Maestra Caro" ("queda muy raro").
- Números en palabras dentro del texto para la voz ("catorce mil novecientos noventa pesos").
- **No copiar claims médicos falsos** del original. Ejemplo: decir que la terapia hormonal "crea dependencia" se cambia por "dietas extremas o pastillas milagrosas". Avisarle el cambio a Santiago.
- **No fabricar testimonios en video** de "clientas reales" con IA. Si el original tenía uno, la avatar lee un testimonio que ya existe en el funnel.

## 3. Avatar y voz
- **Avatar: HeyGen** (decisión del 2026-10-12, en lugar de Higgsfield). Lo usa Santiago desde su sesión en Chrome.
- La experta de Pilates Hormonal es la **Maestra Caro**: mujer asiática, foto en `~/Downloads/WhatsApp Image 2026-10-09 at 13.26.36 (1).jpeg`.
- La voz tiene que sonar **muy real**, combinar con la avatar y sincronizar bien los labios. Acento rioplatense.

## 3b. Créditos de Higgsfield: no usar siempre el mejor modelo (2026-10-12)
- **Intercalar modelos baratos** para B-rolls e imágenes. "Si no, me consume todos los créditos."
- El modelo caro solo va en los planos que más se ven (el hook o un plano clave). El resto, en el modelo más barato que se vea bien.
- Antes de generar una tanda, decirle cuántos créditos se van a gastar.
- Referencia de precios (página de precios de Higgsfield, 2026-10-12): Kling 3.0 a 1080p ~8,75 por clip de 5 s · Kling 3.0 a 720p ~7/5 s · Seedance 2.0 Fast a 720p ~12/5 s · Seedance 2.0 a 720p ~22/5 s. Lipsync: Kling Speak a 720p ~1 crédito por segundo.
- **Los más baratos para B-roll (~5 créditos por clip de 5 s):** Kling 2.6 sin sonido, Wan 2.6 a 480p, Kling Omni 3 (referencia de imagen o primer y último frame) a 720p. Siguen Grok Video y Wan 2.6 a 720p (~7). Siempre **sin sonido** y a **5 s**.
- Mezcla sugerida para 12 B-rolls: 2–3 en Kling 3.0 (hook, anatomía 3D) y el resto en Kling 2.6 o Wan 2.6. Son unos 65 créditos en lugar de 105.

## 4. Edición (basada en el VSL original de Calistenia Asiática)
- Formato 9:16, avatar sentada a cámara.
- **Subtítulos siempre**: palabra por palabra, en blanco y mayúscula, sobre una franja negra a la altura del pecho.
- **B-roll cada 10–20 s** (más seguido al inicio): anatomía 3D, mujeres del público, la app, pilates, espejo.
- Placas:
  - **bonos** sobre el avatar en blanco y negro, con un 🎁;
  - **precio** grande en verde con una flecha roja hacia abajo;
  - **tilde verde** en el "¡Felicitaciones!".
- Recortar silencios y exportar a **1.3x**.

## 4b. Música y efectos de sonido (2026-10-13)
- **Música siempre:** suave por debajo de la voz, pero **activa y que enganche, no relajada**.
  - Se compone original con `OUTPUTS/scripts-vsl/music.py` (118 BPM, Am–F–C–G, bombo en negras, bajo con "pump" y arpegio), así no hay reclamos de derechos en Meta.
  - Mezcla: música unos 15 dB por debajo de la voz (voz -15 LUFS, música -30) y ducking con sidechain cuando ella habla.
- **Efectos, pocos y solo en momentos clave:**
  - **"cha-ching" cada vez que dice el precio ($14.990)**;
  - "pop" con brillo en cada bono;
  - sello en la garantía;
  - "ding" en el tilde inicial;
  - "whoosh" al entrar la app y el testimonio.
  Unos 10 en total. **No llenarlo de efectos.** Se sintetizan con `sfx.py`.
- Los efectos van en el momento exacto de la palabra: se transcribe el video final con Whisper y se ubica cada uno sobre la palabra.

## 4c. Entrega y Panda
- El video final se **reemplaza** en `~/Desktop/<producto>-vsl/` con el mismo nombre.
- Santiago lo sube a **Panda Video** para ponerle diseños y manda el HTML del embed, que se pega dentro de `<template id="vsl-template">` en el último paso del quiz ([[quizzes-reglas-de-armado]]).

## 5. Cómo se produjo el de Pilates Hormonal (receta que funcionó, 2026-10-13)
1. **Transcribir el VSL original** con Whisper (`faster-whisper`, modelo `small`) y sacar cuadros cada 6 s para copiar la edición.
2. **Guion** en `OUTPUTS/`, en tono hablado y con los números en palabras.
3. **HeyGen**:
   - Se abre "Nueva revisión en AI Studio" de un VSL anterior con la misma avatar (Caro Pilates, voz "voz roma", Avatar IV), así se reusa la configuración.
   - El texto se cambia **solo dentro de los bloques (segments)** del editor TipTap. Si se reemplaza el documento entero, se borra la avatar.
   - El editor **no se dibuja si la ventana de Chrome está en segundo plano**: hay que pedirle a Santiago que la traiga al frente.
   - Costo: ~108 créditos de HeyGen para 6:44 de video.
4. **B-rolls** en Higgsfield, en clips de 5 s, 9:16 y sin sonido.
   - **El filtro de seguridad rechaza "torso/abdomen de mujer" en anatomía 3D** (marcado como NSFW, se devuelven los créditos). Usar "holograma de abdomen humano en wireframe" o "maniquí anatómico".
   - Pedir "not pregnant" en planos de panza: un "bloated belly" salió como embarazo.
5. **Edición** con ffmpeg y el script `OUTPUTS/scripts-vsl/edit.py`:
   - recorte de silencios (más de 0,45 s queda en 0,20 s; con 0,30/0,10 queda sin respiro a 1.3x);
   - zoom alternado por oración;
   - B-rolls y placas anclados a frases del guion;
   - blanco y negro en bonos y precio;
   - subtítulos ASS (Montserrat ExtraBold 76, franja negra, 2–3 palabras), apagados mientras hay testimonio o bonos en pantalla;
   - 1.3x al final.
   Las placas se arman con `mkgfx.py`.

## Registro de correcciones
| Fecha | VSL | Corrección | Regla |
|---|---|---|---|
| 2026-10-12 | Pilates Hormonal | "Me llamo maestra Caro queda muy raro" → "Soy la Maestra Caro"; que no suene robot | §2 tono hablado |
| 2026-10-12 | Pilates Hormonal | El video se hace con HeyGen | §3 |
| 2026-10-12 | Pilates Hormonal | "Usá modelos más baratos, intercalá, no uses siempre el mejor" | §3b |
| 2026-10-13 | Pilates Hormonal | Música suave por debajo, activa, que enganche | §4b |
| 2026-10-13 | Pilates Hormonal | Efectos solo en momentos clave: "cha-ching" al decir el precio; no llenarlo | §4b |

## Preguntas abiertas
- ¿Qué plan de HeyGen hay y cuál es el largo máximo por video?

## Relacionado
[[ugc-y-video-generativo]] · [[quizzes-reglas-de-armado]] · [[embudo-vsl-post-pago]] · [[pagina-de-ventas]]

## Fuentes
- Conversación del 2026-10-12. Guion: `OUTPUTS/2026-10-12-vsl-pilates-hormonal-guion.md`
