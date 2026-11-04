# DanceGo

> Oferta nueva AR: bajar de peso bailando en casa, 10 minutos por día. Quiz de 35 pasos clonado de `funilv1.appdancego.com` (BR), pasado a español argentino y **despintado**: el original es un arcoíris y acá va papel crema + tinta + un solo acento.

## Ideas clave
- **El original es brasileño y corre con tráfico de Facebook** (`funilv1.appdancego.com`, llega con `fbclid`, `fbp`, `fbc` y `utm_source=l.facebook.com`). Producto: app con +100 clases de baile, desafío de 28 días, comunidad de WhatsApp. Precio BR: **7× R$ 6,26 o R$ 37,90 al contado**, tachado R$ 197.
- **El mecanismo es el gancho**: "el baile quema 140% más calorías que los ejercicios tradicionales y aburridos" + "aunque no sepas bailar". El avatar es mujer que **no va al gimnasio y le da vergüenza**.
- **El original es largo a propósito** (35 pasos): mucha pregunta de personalización, dos pantallas de carga, un resultado con IMC y una previsión con fecha. La oferta está al final, sin VSL.
- Lo que pidió Santiago el 2026-11-04: *"Mejoramelo, no quiero que se vea recontra colorido, quiero que las imágenes se vean bien."*

## Qué se cambió del original
| | Original | Nuestro |
|---|---|---|
| Paleta | degradé rosa→violeta→amarillo en barra, títulos palabra por palabra de 4 colores, botones amarillo chillón | papel crema `#FBF8F4`, tinta `#1C1A19`, **un** acento frambuesa `#B23A5B`; verde `#216B4F` solo para "bien"/comprar, rojo solo para riesgo |
| Fotos de edad | las mismas fotos, tapadas con un overlay de degradé rosa/violeta/verde/naranja | las mismas fotos **sin overlay y con recorte apretado a la cara** (720×960, 3:4), con la edad sobre una banda oscura encima de la foto |
| Paso de estilos de música | swipe de 7 tapas neón hechas con IA | **sacado entero** (Santiago, 2026-11-04) |
| Comunidad de WhatsApp y perfil de Instagram | capturas de pantalla pixeladas | **armadas en HTML** (burbujas de chat y ficha de perfil) |
| Maqueta de la app | captura del celular con la UI en portugués | **el celular dibujado en HTML/CSS**, con los textos en castellano |
| Ritmos | Sertanejo universitario, Funk brasileño, Gospel | **Cumbia, Cuarteto, Salsa y bachata** (los otros 4 quedan) |
| Paso de e-mail | pedía e-mail antes del nombre | **sacado** (los datos van en el checkout) |
| Largo | 35 pasos | **26 pasos** (ver abajo) |

## Detalles / notas
- **Stack del original: Lovable + Supabase propio.** El bundle (`assets/index-*.js`) trae el panel de administración y las imágenes, pero **el contenido del quiz vive en la base** (`funnel_steps`, `funnel_elements`, `products`…): no está en texto plano. Se saca recorriendo el quiz en Chrome y leyendo `img.src`/`alt` paso a paso.
- Las 81 imágenes cuelgan de `/lovable-uploads/<uuid>.png` y **están todas listadas en el bundle**: se bajan de una y se miran juntas en una hoja de contactos.
- Precio nuestro (provisorio, en el `CONFIG`): **$14.990**, tachado $49.990, 70% OFF, 3 cuotas de $4.997, bonos por $38.900.
- Checkout provisorio: `https://dancego.impultienda.ar/checkout`.
- El quiz **no lleva VSL** por ahora: `SEGUNDOS_OFERTA: 0` y la oferta se ve de entrada, como el original. Si se le carga un VSL en `<template id="vsl-template">`, con poner los segundos la oferta se esconde sola.

## Portada (2ª versión, 2026-11-04)
- Chapita oscura **+155 mil mujeres bailando** con un punto verde, titular a 2.05rem y las 4 fotos a sangre con la edad encima.
- Las 4 fotos son las mismas del original, **recortadas apretado**: antes la persona ocupaba un tercio de la tarjeta y las cuatro parecían la misma mujer. Ahora se distinguen las edades.
- Se revisaron las carpetas de las otras ofertas buscando un set de edades mejor y **no hay**: las de [[monjaro-violeta]] son parejas sobre negro a 300 px.
- En un teléfono de 390 px, la portada entera (chapita + titular + las 4 fotos) entra en la primera pantalla: 677 px de 798.

## Los 9 pasos que se sacaron (2026-11-04)
De 35 a **26**. Fuera:
- **Estilos de música** (swipe de 7 ritmos) — pedido de Santiago
- **Bloque de hábitos**: agua, sueño, rutina de trabajo, qué tan activa y niveles de energía — no cambian el resultado, y con energía se fue el emoji de pilas (🔋🔋🔋) que se veía mal
- **"Elegí tu nivel en el baile"** — duplicaba "¿probaste alguna actividad de baile antes?"
- **La edad exacta** (slider, después del resultado) — ya se pregunta en la portada
- **"¿Hace cuánto estuviste en el mejor cuerpo de tu vida?"** — no personalizaba nada

Quedan los que **personalizan el resultado** (objetivo, físico de hoy, cuerpo deseado, metabolismo, experiencia, frecuencia, duración, lesiones, altura, peso, meta) y los de **compromiso emocional** (eventos, motivación, evento próximo, confianza), más los puentes, la nota, el resultado y la previsión.

## Preguntas abiertas
- ¿La marca queda **DanceGo** o se renombra?
- ¿Precio final y link real de checkout?
- ¿Va VSL en el último paso? Si va, cambia `SEGUNDOS_OFERTA`.
- ¿Se recorta el bloque de hábitos (agua, sueño, rutina de trabajo, qué tan activa, energía)? Son 5 pasos que el quiz podría no necesitar.

## Relacionado
[[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[landings-funnels-y-upsells]] · [[pilates-hormonal]] · [[tai-chi-fit]]

## Fuentes
- `https://funilv1.appdancego.com/` y `/pgvendas` (recorrido completo del 2026-11-04)
- Entregable: `OUTPUTS/2026-11-04-quiz-dancego.html`
