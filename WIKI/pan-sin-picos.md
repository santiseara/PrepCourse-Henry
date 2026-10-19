# Pan Sin Picos (AR)

> Oferta nueva para Argentina (2026-10-18): recetario de panes para diabéticos, sin trigo, sin azúcar y sin leche. Modelado de "Mesa y Sabor" (~200 ads activos en AR, venta por WhatsApp). Santiago la vende con quiz + checkout de ImpulTienda. "Pan Sin Picos" es un nombre provisorio.

## Ideas clave
- **Original:** fanpage Mesa y Sabor (`view_all_page_id=916286824910053`). Copy: "🍞 Panes Sin Trigo, Sin Leche y Sin Azúcar! 🤯 Dejá de privarte de tu pan favorito… listos en solo 10 minutos… Guía con 50 recetas exclusivas". El CTA va a WhatsApp ("200+ recetas ¡La solución que estabas buscando!"). Creativo: video de una mujer en la cocina con el pan.
- **Quiz propio** (no hay quiz original para copiar): `OUTPUTS/2026-10-18-quiz-pan-sin-picos.html`. Tiene 17 pasos y 11 preguntas pensadas para que se sienta personalizado: para quién es, género, edad, diagnóstico, qué extraña, qué más tiene que evitar, qué le pasa con el pan común, tiempo, qué tiene en la cocina, objetivo y nombre.
- **Valor dentro del quiz:** gráfico ilustrativo de la glucosa (harina blanca contra pan sin trigo), 3 panes recomendados según lo que extraña y lo que evita, y una **receta de regalo** que cambia según las respuestas (pan en taza en el microondas, pan de sartén o pan chato de lino sin huevo; con polvo de hornear sin TACC si es celíaco/a).
- **Oferta:** sin VSL por ahora (hay un `<template id="vsl-template">` opcional). Orden: cuenta regresiva de 10 min → cuotas de Mercado Pago → aviso del email → botón → celular con la app personalizada → qué incluye y 3 bonus → adaptaciones → garantía de 30 días → FAQ → aviso médico.
- Paleta tostado/caramelo (#c0621f) con verde "apto" (#2f7d4f). Fuentes Fraunces + Poppins.
- **Fotos (v2, 2026-10-18):** 11 fotos de Higgsfield (GPT Image 1.5, High, 1:1) con el mismo estilo de recetario: mesa de madera clara, luz de ventana cálida y lino crema. Son portada, mujer, hombre, pancitos, tostadas, pizza, medialunas, sándwich, budín, pan en taza y pan de lino. Van embebidas en WebP (~480 KB); el HTML final pesa ~700 KB.
- **Link para mostrar:** https://claude.ai/artifact/KmVbkS3rmp2Jm8ea4Ve4Jc (versión de vista previa; el checkout no funciona ahí).

## Decisiones tomadas sin confirmar (revisar con Santiago)
- Precio $14.990, tachado $39.990, 3 cuotas de $4.997 (63% OFF).
- Sin testimonios: no hay testimonios reales para usar y no se inventan datos ([[quizzes-reglas-de-armado]] §2).
- Dato del interstitial: "1 de cada 8 adultos en Argentina tiene diabetes o la glucemia elevada" (4.ª ENFR 2018, 12,7%).
- Bonus: Guía de reemplazos, Untables y rellenos sin azúcar, Lista de compras.

## Entregas
- `~/Desktop/pan-sin-picos/` → `pan-sin-picos-quiz.txt` (para ImpulTienda), `pan-sin-picos-PRUEBA.html`, `pan-sin-picos-site.zip` (para Netlify Drop) y las fotos `img-*.png` (1024×1024).

## Registro de correcciones
- **2026-10-18 · "Las imágenes son muy malas… se ve muy low ticket. El quiz está perfecto."** Se reemplazaron el pan en SVG y los emojis grandes por fotos profesionales. Regla general en [[quizzes-reglas-de-armado]] §4.

## Preguntas abiertas
- Nombre definitivo, precio, link de checkout y píxel.
- ¿Testimonios? Si hay comentarios reales del original o de clientes, se suman en HTML.
- ¿Habrá VSL? Si hay, se pega en el template y se ajusta `SEGUNDOS_OFERTA`.

## Relacionado
[[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[secreto-de-la-insulina]] · [[funnel-hacking]]

## Fuentes
- Ads Library (AR) de Mesa y Sabor, 2026-10-18.
