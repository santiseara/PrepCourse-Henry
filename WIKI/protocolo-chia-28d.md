# Protocolo Chía 28D

> Oferta nueva para **LATAM** (español neutro): protocolo de chía de 28 días para bajar de peso, clon del VSL de **Protocolo Chía 4S** (Argentina), competidor con más de 700 anuncios prendidos. (fuente: video del competidor en `~/Documents/`, análisis del 2026-10-24)

## Ideas clave
- El activo que se clona es un **VSL post-quiz de 17:46** en vertical: abre con "gracias por responder las preguntas, tu protocolo personalizado ya está listo".
- Mecanismo del competidor: **células L dormidas → GLP-1 → la chía forma un gel** (demo del vaso de agua) → cuatro fases semanales **Sembrar, Sanar, Soltar, Sumar** ("4S"). En nuestra versión las cuatro fases entran en los **28 días** del nombre.
- Oferta del competidor: protocolo personalizado + **app web** (progreso, plan alimenticio, centro de aprendizaje) + bono Recetario Cero Culpa (200 recetas) + bono WhatsApp 24/7, a **$24.999 ARS** pago único con anclaje 200.000 / 140.000 / 100.000, garantía de 60 días y 20 cupos.
- La edición es la receta completa de [[vsl-reglas-de-armado]]: subtítulos de 2–3 palabras con la clave en amarillo, chips verdes de fase, checklist verde acumulativa, anclas tachadas, badge fijo de precio, escudo de garantía, botón con dedo y placa final.
- **Pedido de Santiago (2026-10-24):** mismo guion y misma edición, pero en **acento neutro de LATAM** (el original es voseo argentino) y con los b-rolls del original si se pueden reusar.

## Detalles / notas
- El archivo del competidor está mal nombrado ("The Temari Atelier…"): el contenido es el VSL de chía.
- En el checkout el producto figura como "Protocolo Mounjaro de chía": usan el nombre del fármaco como gancho de marca.
- **Los b-rolls del original se pueden reusar** recortándolos del MP4 y sacándoles el subtítulo quemado con `OUTPUTS/scripts-vsl/rmsubs.py`.
- **La oferta original es de Santiago** (2026-10-24): se reusan también los **3 testimonios** y las pantallas de **la app y el checkout**, no hace falta grabarlos de cero.
- Análisis completo, inventario de b-rolls minuto a minuto y plan de producción: `OUTPUTS/2026-10-24-protocolo-chia-28d-analisis-y-plan-vsl.md`.
- Carpeta de la oferta: `~/Desktop/protocolo-chia-28d/` (`imagenes/`, `landing/`, `anuncios/`, `vsl/`).
- Avatar propuesto: nutricionista latina de unos 38 años, bata blanca sobre polera verde oliva, anteojos redondos. Prompt en `~/Desktop/protocolo-chia-28d/vsl/PROMPT-AVATAR.txt`.

## Avance (2026-10-24)
- **Avatar creado en HeyGen: "Valeria Chia 28D"** (personaje virtual desde foto, voz "Buddy - Voice 3", español de México neutro). La foto está en `~/Desktop/protocolo-chia-28d/imagenes/avatar-valeria.png`.
- Guion dividido en 4 bloques (`part01` a `part04.txt`) por el tope de 5.000 caracteres de HeyGen.
- **Bloque 1 generado y bajado:** `~/Desktop/protocolo-chia-28d/vsl/HEYGEN-parte01.mp4` (4:48, 1080x1920). Costó 231 créditos con Avatar 6 Pro y dejó la cuenta en 6: los bloques 2, 3 y 4 quedaron rechazados por falta de créditos ([[vsl-reglas-de-armado]] §3c).
- **55 b-rolls recortados del original** y limpiados de subtítulos quemados con `rmsubs.py`: `~/Desktop/protocolo-chia-28d/vsl/brolls/clean/`. Sin testimonios ni pantallas de la app y el checkout del competidor.
- Precio definido: **17 USD**, anclas 140 / 97 / 70. Entregable **con app web** (la armamos nosotros).
- **Bloques 2 a 4 generados con Avatar IV a 720p** (79 + 78 + 62 créditos) y unidos con `OUTPUTS/scripts-vsl/unir_partes.py` en `VSL-CRUDO-UNIDO.mp4` (18:26, 1080x1920). El bloque 1 quedó con Avatar 6 Pro: gesticula más que el resto y se nota el salto a los 4:48. Santiago: "no pasa nada".
- **Bloque de testimonios armado**: `~/Desktop/protocolo-chia-28d/vsl/testimonios/TESTIMONIOS.mp4` (1:22). Son los 3 testimonios del original (8:18–9:46) con las menciones a la marca vieja sacadas: se cortó "el protocolo Chía 4S" y "Alejandra" del audio, y donde el subtítulo quemado igual decía "GRACIAS DOCTOR ALEJANDRA" se borró con `rmsubs.py` y se escribió "GRACIAS DOCTORA" con el mismo estilo (Arial Black 82, amarillo en la primera palabra).
- **Pantallas de la app (10:35–11:11) y del checkout (13:30–13:59)** recortadas y limpias: `b0637 b0645 b0650 b0656 b0661 b0666` y `b0810 b0816 b0824 b0833`. Ojo: el checkout del original muestra **ARS 24.999** y la app dice "Protocolo Chia 4S" en el encabezado; hay que rehacer esas capturas cuando esté nuestro checkout en USD.
- **Quiz armado** (copia del original, en neutro y a 17 USD): `~/Desktop/protocolo-chia-28d/landing/protocolo-chia-28d-quiz.txt` + `PRUEBA.html`. 5 pasos → pantalla de análisis → VSL con el botón a los **840 s (14:00)**, porque en nuestro VSL el precio se dice a las **13:46**.

## Preguntas abiertas
- Pasarela para cobrar 17 USD en LATAM (el checkout original cobra en ARS con Mercado Pago).
- Hosting del VSL (VTurb o Panda) para pegar el embed en `<template id="vsl-template">` del quiz.
- ¿El logo del quiz sigue siendo el de "Mounjaro de Chía" o se rehace con "Protocolo Chía 28D"?

## Relacionado
[[vsl-reglas-de-armado]] · [[funnel-hacking]] · [[internacionalizacion]] · [[ugc-y-video-generativo]] · [[quiz-funnel]]

## Fuentes
- Video del competidor (VSL Protocolo Chía 4S) y su transcripción: `~/Desktop/protocolo-chia-28d/vsl/TRANSCRIPCION-ORIGINAL-4S.txt`
