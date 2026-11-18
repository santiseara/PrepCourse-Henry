# Cabello Fuerte (Fernanda Lucas → Argentina)

> Réplica exacta de los 8 mejores creativos de **Fernanda Lucas** (Brasil), la oferta de caída de pelo en mujeres de 45-65, traducidos a castellano rioplatense para tirar en Argentina. (fuente: biblioteca de anuncios, page id `1114993291702956`, bajada el 18/11/2026)

## Ideas clave
- **La oferta no vende un producto: vende una clase en vivo gratis.** El CTA de los 8 anuncios es **INSCRIBIRSE**, no comprar. El lead va a un quiz de 10 preguntas y de ahí al VSL.
- **El mecanismo** es la menopausia: baja el estrógeno, se debilita el escudo que protege la raíz y **un "parásito capilar" / "hormona contaminadora"** infecta el folículo. Por eso la caída, el afinamiento y las peladas aparecen todos juntos.
- **El entregable prometido** es un tónico capilar casero (según el anuncio: aloe vera, ajo con limón, o una "vitamina india de la lenteja") y una receta de activos naturales para mandar a preparar a la farmacia.
- **El experto con nombre propio es siempre el mismo: "doctor Antonio Lombardi", especialista en salud capilar.** Aparece en los 8 guiones y es el que da la clase.
- **Una sola descripción para los 39 anuncios.** No rotan copy: rotan creativo.
- **Los 8 formatos son distintos entre sí a propósito**: presentadora con anteojos, doctor en consultorio, animación 3D del villano, chica en el auto, collage de varias mujeres, rubia en la cocina, mujer de 55+ con banda gris, y doctora con sticker de ranking.

## El embudo del competidor
`ad → lp.portalnoticiavital.com/<slug>/ → quiz capilar de 10 preguntas → institutofilipelli.com`

## Los 8 creativos elegidos
Orden de impresiones de la propia biblioteca, salteando el único estático.

| # | Library ID | Dur | Al aire | Formato | Subtítulo |
|---|---|---|---|---|---|
| 1 | 1640132624436255 | 3:39 | 12 oct | Presentadora morena con anteojos + b-roll | amarillo con contorno |
| 2 | 1105663372101328 | 2:49 | 27 oct (4 copias) | Doctor en consultorio + b-roll | blanco minúscula, 1 palabra |
| 3 | 1348286425043809 | 3:44 | 4 nov | Médica dermatóloga + b-roll | blanco, palabra activa en caja verde |
| 4 | 2358925368282673 | 4:34 | 27 oct | Chica en el auto + b-roll | blanco, palabra activa en caja azul |
| 5 | 3085805631768910 | 3:30 | 5 nov | Collage de varias mujeres + marido | blanco, palabra activa en caja violeta |
| 6 | 4574755996121602 | 1:22 | 5 nov | Animación 3D del villano del folículo | blanco minúscula, 1 palabra |
| 7 | 28990562903883911 | 3:11 | 13 sept | Mujer 55+ camisa rayada + b-roll | blanco sobre banda gris |
| 8 | 1166970309202354 | 2:51 | 4 nov | Doctora rubia, plano único | sticker de ranking arriba |

## Cómo se replica (pipeline)
1. **Bajar en HD.** La biblioteca muestra un `<video src>` de 360×640, pero el JSON de la página trae `video_hd_url` a **720×1280**. Hay que sacarlo del HTML, no del reproductor.
2. **Despiece.** `ffmpeg select=gt(scene,0.30)` saca los cortes; un clustering por firma de cuadro separa los planos de presentador (los que más segundos suman) de los b-rolls.
3. **Guion.** Traducción palabra por palabra al rioplatense, mismo orden y mismo largo.
4. **Voz.** Gemini TTS, voces fijas (mujer Sulafat, hombre Orus). Después se acelera con `atempo = duración_nuestra / duración_original` (tope 1,25) para que **el video dure exactamente lo mismo que el original**.
5. **Avatar.** HeyGen, **Avatar III · "Aplica sincronización de labios"** con el WAV subido: ~**7 créditos por minuto** (contra ~25 de Avatar IV por texto y ~48 de Avatar 6 Pro). Un video de 3:44 salió **21 créditos**.
6. **B-roll.** Se reusa el del original, pero **hay que borrarle los subtítulos en portugués quemados** (`limpia_subs.py`).
7. **Montaje.** `edit_cabello.py` reconstruye la misma línea de tiempo: cada plano del original en su lugar, el avatar en los planos de presentador, los subtítulos nuevos con el estilo exacto (`gfx_cabello.py`).

## Detalles / notas
- ⛔ **La cuota gratis de Gemini TTS es de 10 pedidos por día y es por clave, no por modelo** (probado el 18/11: `2.5-flash`, `2.5-pro`, `3.1-flash` y `3.8-flash` comparten el tope). Para una tanda de 8 videos hay que mandar **un guion entero por pedido** (sale sin truncar: 780 palabras en un solo llamado) y aun así entran 8-9 por día.
- ⛔ **`gemini-3.8-flash-tts` lee en voz alta el bloque de estilo** (control de 7 palabras: 19,8 s en vez de 2,5 s). El que sirve es **`gemini-2.5-flash-preview-tts`**.
- **Chrome bloquea la segunda descarga por blob de la misma página.** Para bajar varios renders de HeyGen, sacar la URL firmada del `<video>` en base64 (la herramienta censura los query strings en claro) y bajarla con `curl`.
- **Cambiar de avatar en HeyGen resetea el modelo a Avatar 6 · Pro.** Siempre elegir avatar primero y modelo después, y mirar el selector antes de generar ([[vsl-reglas-de-armado]] §3c).

## Preguntas abiertas
- ¿La landing y el quiz se replican también, o se manda a un checkout directo?
- El creativo #6 es una animación 3D de un villano que estrangula el folículo: falta decidir si se genera con Veo o se reusa el del original.

## Relacionado
[[guiones-y-anuncios]] · [[vsl-reglas-de-armado]] · [[estilo-de-video-ia]] · [[caza-de-ofertas]] · [[funnel-hacking]] · [[quiz-funnel]]

## Fuentes
- Biblioteca de anuncios de Meta, page id 1114993291702956 (18/11/2026)
- `~/Desktop/cabello-fuerte/work/` (originales, transcripciones, despiece)
- `OUTPUTS/2026-11-18-guiones-cabello-fuerte.md`
