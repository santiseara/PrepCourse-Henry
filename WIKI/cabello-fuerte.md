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

## Registro de correcciones (18/11/2026, al cerrar la tanda)

- 🐞 **Las placas fijas van en UNA capa, no una entrada por placa.** El anuncio 8 lleva 9 placas (5 estados
  del ranking + 4 titulares) sobre 171 s y ffmpeg se murió con `-9` (lo mató el sistema por memoria): cada
  `-loop 1 -i placa.png` retiene cuadros de 1080×1920. `capa_extras()` arma la línea de tiempo de todas las
  placas, compone lo que esté activo en cada tramo, **recorta a la franja útil** y entrega un solo MOV con
  alfa. Igual que `capa_subtitulos()`, que ya lo hacía bien.
- 🐞 **El titular verde del anuncio 8 va al pecho (y = 0,57), no arriba.** Pegado al título del sticker se come
  la fila ÓPTIMO / BUENO / MALO. Medido sobre el original: la palabra ocupa **~82 % del ancho** (fuente 140,
  no 76).
- 🐞 **Los tiempos de las placas se anclan a NUESTRA voz, no a los del original.** Se buscan las palabras en
  `alineacion/<guion>.json` (Minoxidil 5,94 · Biotina 15,14 · Shampoo anticaída 27,48 · Clase online 60,70).
  Es la misma regla que ya costó cara en [[dieta-3-fases]] con los subtítulos.
- 🐞 **`limpia_subs.py` no veía los subtítulos de letra blanca sobre caja de color ni sobre banda gris.** Pedía
  contorno negro alrededor de cada letra y los daba por brillos de la imagen: sobrevivían enteros los
  `PODE`, `GRATUITA`, `SEM ATACAR` y `NA PRÓXIMA TERÇA FEIRA`. Lo que se agregó:
  - **anillo de color plano** vale igual que el anillo negro (`_anillo_plano`);
  - **el recuadro de color se detecta como tal** (`cajas_de_color`): rectángulo lleno, ancho, con letras
    blancas adentro — el detector de letras lo tomaba como una letra gigante y lo descartaba;
  - el rectángulo **se estira hasta tapar la caja entera** (`_estirar_a_la_caja`, con tope de 44 px para que
    un fondo liso no se coma media imagen);
  - **los renglones cortos cuentan**: el piso de ancho bajó de 12 % a 4,5 % (el `NA` suelto del anuncio 3);
  - el repintado va a **media resolución y desenfoque 3** (antes un tercio y 5): sobre textura fina —la piel
    del folículo 3D— el borrón se notaba más que el subtítulo.
- ⚠️ **El control de restos se hace sobre los planos que de verdad entran al video.** La primera revisión
  marcó portugués en los anuncios 3, 4 y 7 y resultó que esos planos los reemplaza el avatar. Hay que
  saltear los índices de `presentador` / `avatares[].idx` antes de contar. Lo que sí quedaba sucio era otra
  cosa: un `raiz` quemado en un plano de b-roll del anuncio 2.

## Preguntas abiertas
- ¿La landing y el quiz se replican también, o se manda a un checkout directo?
- El creativo #6 es una animación 3D de un villano que estrangula el folículo: falta decidir si se genera con Veo o se reusa el del original.

## Relacionado
[[guiones-y-anuncios]] · [[vsl-reglas-de-armado]] · [[estilo-de-video-ia]] · [[caza-de-ofertas]] · [[funnel-hacking]] · [[quiz-funnel]]

## Fuentes
- Biblioteca de anuncios de Meta, page id 1114993291702956 (18/11/2026)
- `~/Desktop/cabello-fuerte/work/` (originales, transcripciones, despiece)
- `OUTPUTS/2026-11-18-guiones-cabello-fuerte.md`
