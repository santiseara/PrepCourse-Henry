# Pan Sin Picos (AR)

> Oferta nueva para Argentina (2026-10-18): recetario de panes para diabéticos, sin trigo, sin azúcar y sin leche. Modelado de "Mesa y Sabor" (~200 ads activos en AR, venta por WhatsApp). Santiago la vende con quiz + checkout de ImpulTienda. "Pan Sin Picos" es un nombre provisorio.

## Ideas clave
- **Original:** fanpage Mesa y Sabor (`view_all_page_id=916286824910053`). Copy: "🍞 Panes Sin Trigo, Sin Leche y Sin Azúcar! 🤯 Dejá de privarte de tu pan favorito… listos en solo 10 minutos… Guía con 50 recetas exclusivas". El CTA va a WhatsApp ("200+ recetas ¡La solución que estabas buscando!"). Creativo: video de una mujer en la cocina con el pan.
- **Quiz propio** (no hay quiz original para copiar): `OUTPUTS/2026-10-18-quiz-pan-sin-picos.html`. Tiene 17 pasos y 11 preguntas pensadas para que se sienta personalizado: para quién es, género, edad, diagnóstico, qué extraña, qué más tiene que evitar, qué le pasa con el pan común, tiempo, qué tiene en la cocina, objetivo y nombre.
- **Valor dentro del quiz:** gráfico ilustrativo de la glucosa (harina blanca contra pan sin trigo), 3 panes recomendados según lo que extraña y lo que evita, y una **receta de regalo** que cambia según las respuestas (pan en taza en el microondas, pan de sartén o pan chato de lino sin huevo; con polvo de hornear sin TACC si es celíaco/a).
- **Oferta:** sin VSL por ahora (hay un `<template id="vsl-template">` opcional). Orden: cuenta regresiva de 10 min → cuotas de Mercado Pago → aviso del email → botón → celular con la app personalizada → qué incluye y 3 bonus → adaptaciones → garantía de 30 días → FAQ → aviso médico.
- Paleta tostado/caramelo (#c0621f) con verde "apto" (#2f7d4f). Fuentes Fraunces + Poppins. Sin imágenes: todo en SVG/CSS (pan de la portada, celular).

## Decisiones tomadas sin confirmar (revisar con Santiago)
- Precio $14.990, tachado $39.990, 3 cuotas de $4.997 (63% OFF).
- Sin testimonios: no hay testimonios reales para usar y no se inventan datos ([[quizzes-reglas-de-armado]] §2).
- Dato del interstitial: "1 de cada 8 adultos en Argentina tiene diabetes o la glucemia elevada" (4.ª ENFR 2018, 12,7%).
- Bonus: Guía de reemplazos, Untables y rellenos sin azúcar, Lista de compras.

## Entregas
- `~/Desktop/pan-sin-picos/` → `pan-sin-picos-quiz.txt` (para ImpulTienda) y `pan-sin-picos-PRUEBA.html`.

## Preguntas abiertas
- Nombre definitivo, precio, link de checkout y píxel.
- ¿Imágenes reales (foto del pan, mockup con IA en Higgsfield) o queda ilustrado?
- ¿Testimonios? Si hay comentarios reales del original o de clientes, se suman en HTML.
- ¿Habrá VSL? Si hay, se pega en el template y se ajusta `SEGUNDOS_OFERTA`.

## Relacionado
[[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[secreto-de-la-insulina]] · [[funnel-hacking]]

## Fuentes
- Ads Library (AR) de Mesa y Sabor, 2026-10-18.
