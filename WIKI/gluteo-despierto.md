# Glúteo Despierto

> Oferta nueva para **Argentina**: rutina de glúteos y piernas en casa, **15 minutos por día, 28 días, sin sentadillas**. Modelada del quiz de **Guía Piernas y Cola Sin Sentadillas** (`guiapiernasycola.impultienda.ar`), que corre **194 ads activos**. Competimos en el **mismo mercado**, así que cambia el mecanismo, el nombre y toda la estética.

## Ideas clave
- **El competidor es una ballena.** Página *Guia Piernas y Cola*, **194 anuncios activos** (medidos el 14/11), el más viejo del **7/11** y el grueso creado entre el **12 y el 13/11**: escaló fortísimo en una semana. Un solo link title en todos: **"Truco del Bumbum - Sin sentadillas"** — se les quedó el *bumbum* del original brasileño.
- **Su mecanismo:** el "Truco de la Cola" / "Protocolo Sin Sentadillas" / "Método Anti-Lesión". El ángulo es **el dolor de rodillas**: sacan la sentadilla porque comprime la articulación.
- **Nuestro mecanismo (la diferencia):** el **Protocolo del Glúteo Dormido**. No es "la sentadilla te duele", es **"la sentadilla no te levanta la cola"**: el cuerpo le pasa el trabajo al cuádriceps y a la espalda, y el glúteo se acostumbra a no encenderse. Tres fases: **Despertar (días 1-7) · Aislar (8-18) · Cargar (19-28)**. El dolor de rodillas sigue adentro, pero como beneficio, no como ángulo madre.
- **Precio:** $19.990 (antes $99.990, 80% OFF, ahorro $80.000, 3 cuotas de $6.664). Es **el mismo que ellos**: en el mismo mercado no conviene estar más caro ni regalar margen.

## Radiografía del quiz del competidor (fuente: `curl -sL` al `custom_html` de su tienda)
El quiz entero viaja en **texto plano** dentro del HTML de la tienda ([[quizzes-reglas-de-armado]] §3). Su motor es propio: `<section class="paso">`, cargas con porcentaje, VSL en MP4 servido desde los recursos de la tienda, y el paso se recuerda 1 día en `localStorage`.

- **29 pasos, 24 preguntas.** Portada de urgencia ("se libera gratis solo 1 vez por persona", reloj de 01:00) → edad, objetivo, tiempo → carga → 9 preguntas de dolor y frustración → carga → 7 preguntas de miedo y autoestima → carga → 5 preguntas de compromiso → diagnóstico con VSL → oferta.
- **Cero fotos en las preguntas:** todas las opciones llevan emoji. Las únicas fotos son antes/después de glúteos (selfies de espejo) y el sello de garantía.
- **Su oferta:** reloj de 15:00, precio, 4 ítems de "lo que vas a recibir", 3 testimonios con avatar, antes/después, 4 FAQ, garantía de 30 días. Sin cuotas de Mercado Pago.
- **Su backend:** 2 upsells — *Panza Chata en 15 Minutos* ($3.990) y *Busto Firme y Postura en 10 Minutos* ($4.990) — y 3 bonos declarados en la tienda. Molde a mirar cuando armemos los pospagos ([[embudo-post-compra]]).

## Nuestro quiz (entregado el 14/11)
**22 pasos, 15 preguntas** — se recortaron 9 preguntas suyas que repetían el mismo golpe emocional (ver el comentario del array `STEPS` en el HTML, que las lista una por una).

Lo que **se sumó** y no está en el de ellos:
1. **La pregunta del ejercicio con 4 fotos** ("¿cuál de estos creés que activa más el glúteo?") y **la pantalla de revelación** con barras comparativas. Es el mecanismo demostrado, no contado.
2. **Dos medidores** (meses sin entrenar piernas · minutos por día), que alimentan el cálculo.
3. **El Índice de Activación Glútea (IAG)**: 0-100 calculado con sus respuestas de dolor, frustración, historia de intentos y meses parada. Barra de riesgo (Dormido → Apagado → A media → Activo), potencial a 28 días y gráfico de previsión.
4. **La maqueta de la app dibujada en HTML/CSS** con las 3 fases y la rutina del día.
5. **Antes/después en HTML** (dos listas ✗ / ✓) en vez de fotos de cuerpos: nítido, gratis y no arrastra el material del competidor al mismo feed.

**Aritmética del IAG:** arranca en 100 y baja por dolor en sentadillas (hasta 26), frustración (hasta 24), historia de intentos (hasta 16) y meses sin entrenar (hasta 24, a 0,85 por mes). Queda topeado entre 8 y 72; el potencial es el índice + 38 con techo en 94. Si eligen **menos de 15 minutos por día**, el plan se estira a **5 semanas** y la pantalla lo dice en vez de prometer las 4.

**Paleta:** ciruela `#A62B55` sobre papel cálido `#FAF6F6`. El competidor corre violeta eléctrico `#970FA9` + magenta: en el mismo feed tienen que leerse como dos marcas distintas. El verde solo significa "bien" y el rojo solo "riesgo".

**Las 8 fotos son propias**, generadas con IA en un solo batch (gpt_image_2_6): 4 retratos por rango etario (22/31/41/54, mismo fondo beige, misma remera gris, misma luz, recorte apretado a la cara en 3:4) y 4 ejercicios (sentadilla, estocada, puente, patada) con la misma mujer, el mismo living y el mismo encuadre. **El banco propio no servía**: Origen Pilates son mujeres 40+ vestidas de calle y Calistenia Rusa son todos hombres — se miró antes de generar ([[quizzes-reglas-de-armado]], regla del 4/11).

## Preguntas abiertas
- **El nombre del método y de la marca los elegí yo** ("Glúteo Despierto" / "Protocolo del Glúteo Dormido"). Si Santiago prefiere otro, es un find/replace sobre el `CONFIG` y el markup.
- **El subdominio de ImpulTienda no está confirmado.** El checkout quedó **relativo** (`/checkout`), que resuelve solo en la tienda donde se pegue el HTML ([[quizzes-reglas-de-armado]], regla del 11/11). Cuando esté el subdominio se cambia **una línea** del `CONFIG`.
- **Falta el VSL.** `SEGUNDOS_OFERTA` está en 0 y el `<template id="vsl-template">` vacío, igual que el competidor (su botón de diagnóstico también se ve de entrada). Cuando haya VSL, el número se calcula con el segundo exacto en que dice el precio.
- **En la revelación no hay porcentajes de activación, hay barras y etiquetas** (Baja / Media / Alta / Muy alta) y una línea al pie que aclara que es orientativo. No se inventó una cifra de laboratorio ([[quizzes-reglas-de-armado]] §2). Si Santiago quiere números duros, hay que buscar el estudio.
- **Los 3 testimonios son de ejemplo**, marcados en rojo en el HTML. Reemplazarlos por reales antes de poner plata.
- Falta la tanda de anuncios y el backend (los 2 upsells del competidor son el molde más cercano).

## Relacionado
[[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[funnel-hacking]] · [[embudo-post-compra]] · [[pilates-hormonal]] · [[origen-pilates]] · [[landings-funnels-y-upsells]]

## Fuentes
- Biblioteca de Anuncios de Meta, búsqueda `guiapiernasycola.impultienda.ar` y `glúteos sin sentadillas cola parada` (AR), 14/11/2026
- `curl -sL https://guiapiernasycola.impultienda.ar/` — quiz, oferta, precios, bonos y upsells en texto plano
- Entregable: `OUTPUTS/2026-11-14-quiz-gluteo-despierto.html` · paquete en `~/Desktop/gluteo-despierto/`
