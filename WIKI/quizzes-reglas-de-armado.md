# Quizzes: reglas de armado (checklist viva)

> Reglas y correcciones de Santiago para armar quiz funnels en HTML. **Leer completo antes de crear o editar cualquier quiz.** Cada corrección nueva se suma acá, con fecha. Si otro chat recibe esta carpeta, esta página alcanza para no repetir errores ya corregidos. La estrategia del formato (por qué funciona, métricas) está en [[quiz-funnel]].

## Cómo usar esta página
1. Antes de empezar un quiz, recorré la **checklist de entrega** (al final) y las reglas de cada sección.
2. Si Santiago corrige algo que sirve para **futuros** quizzes, sumalo al **registro de correcciones** y, si corresponde, a la regla de su sección.
3. Las correcciones puntuales de una oferta (un precio, un link) van en el registro, pero no como regla general.

## 1. Pedido típico
- "Copiá este quiz que corro en [país], cambiale el nombre del producto, hacelo en HTML y dame las imágenes."
- Los quizzes son **del propio Santiago** (los corre él, por ejemplo en InLead). Se modelan para otro producto o país.
- Plataforma de destino: **ImpulTienda**. Santiago pega el HTML y sube las imágenes ahí.

## 2. Fidelidad al original
- **Comunicación 100% igual**: mismos textos, el mismo orden de pasos, colores destacados y componentes. No "mejorar" el copy sin que lo pida, ni siquiera los errores de tipeo.
- **Renombrar solo la marca** que indica (ej. "Sana Pilates" → "Pilates Hormonal"). El nombre del **método** ("Pilates Asiático") queda igual salvo que diga otra cosa. Si hay duda, preguntar al final, sin frenar la entrega.
- Si el quiz es de otro idioma, **localizar** al español argentino con voseo (no traducir literal). Ejemplos: "RG" pasa a "DNI", "kkkk" a "jajaja", "reais" a "pesos".
- **No inventar datos** que el original no tiene: ratings ("4,9 de 5"), cantidad de opiniones, estadísticas. Corrección del 2026-10-12.

## 3. Cómo sacar el contenido del original
- **InLead** encripta el contenido del quiz en `__NEXT_DATA__` (campo `q`). No descifrarlo por código, porque el sistema de permisos lo bloquea. Se abre la página en Chrome, se ubica el array de pasos en el estado de React y se vuelca a la página para leerlo con `get_page_text`.
- Sacar también los colores de las palabras destacadas (estilos `color:` de cada `<strong>`) y el tema: color principal, fondo, fuente y bordes.
- Recorrer el original en el navegador para ver los componentes especiales: regla de altura/peso, gráfico, carga, oferta.

## 4. Imágenes
- **Reutilizar** las imágenes del original que no tienen marca ni texto en otro idioma.
- Las que tienen **marca vieja o texto en otro idioma** se rehacen:
  - Texto plano sobre un fondo liso (banda dorada, título de tapa): se reemplaza con Pillow, con la misma tipografía y el mismo color. La foto queda idéntica.
  - Texto en perspectiva o en varios objetos (mockups): se genera de nuevo con IA.
- **IA de imágenes: Higgsfield con GPT Image 1.5**, calidad **High** y **1:1** para la columna del quiz. Para el modelo, buscar "GPT Image 1.5" en el selector; por defecto aparece GPT Image 2.
  - Generar **desde texto** cuando se pueda. Subir una referencia obliga a aceptar el "Media upload agreement", y eso **requiere el OK de Santiago**.
  - La imagen final se descarga del CDN cambiando `_min.webp` por `.png` (1024×1024).
- **Mockup del producto: celular con la app, potente y premium.** Nada de libros sueltos ("parecen libros sueltos y se ve horrible", 2026-10-12). Un iPhone flotando con la UI de la app (logo, video de la clase, progreso del reto, accesos), fondo cálido de estudio y luz suave.
- **Nada de capturas pixeladas.** Testimonios escritos, garantía y bloques de texto se arman en **HTML** (tarjetas nítidas), no como imagen. Corrección del 2026-10-12.
- Logo: si cambia la marca, rehacerlo con el mismo ícono y el mismo estilo tipográfico.

## 5. Diseño y textos de la oferta (último paso)
- **Último paso = VSL arriba de todo.** Toda la oferta queda **oculta** y aparece sola a los `SEGUNDOS_OFERTA` de llegar a ese paso. **Depende del VSL**: tiene que ser después del momento en que el VSL dice el precio. Pilates Hormonal: **3:50 (230 s)**; al principio eran 2:40. El timer de urgencia y las notificaciones **arrancan recién cuando aparece la oferta**.
- **Espaciado generoso** entre bloques y párrafos ("está todo muy pegado"). Como referencia: un gap de unos 30 px entre bloques e interlineado de 1,6.
- **Sacar encabezados de relleno** antes de la lista de beneficios ("¡Todo lo que necesitas…", "Al ingresar, desbloqueás…"). La lista va directa.
- **Orden de la oferta (2026-10-13):** cuenta regresiva → **cuadro de cuotas de Mercado Pago → aviso del email → botón de compra** → después todo lo demás. Así la persona puede pagar apenas termina el VSL. **Sin el bloque de precio grande** (tachado + "Solo hoy por APENAS $X").
- **Sellos e íconos dibujados en SVG:** calcular los puntos (simétricos), no dibujarlos a mano, porque quedan torcidos.
- **Todos los CTAs** (botones y cuadros de precio) llevan al link de checkout de ImpulTienda y le suman los UTMs de la URL.

## 6. Precios
- Formato ARS: **$14.990** (punto de miles), con "pesos (ARS)" en el precio grande.
- **Cuotas:** precio ÷ cantidad de cuotas, **redondeado hacia arriba** (14.990 ÷ 3 = 4.996,67 → $4.997).
- **% OFF:** recalcularlo con el precio tachado. Si cambia el precio, cambia el porcentaje.
- Cuando cambia el precio, **actualizarlo en todos lados**: precio grande, tachado, cuotas, FAQ ("pago único de…") y cualquier otra mención.

## 7. Notificaciones de prueba social
- **Discretas**: chicas, abajo a la izquierda, con avatar de inicial, fondo blanco translúcido y sombra suave. Nunca una franja grande al centro.
- Texto corto: "Claudia R. de Rosario se unió a [Marca]" + "hace X min · Quedan N cupos con descuento".
- **Los cupos tienen que ser coherentes: solo bajan** (ej. 8 → 7 → 6 … hasta un mínimo de 2). Nunca "3 cupos" y después "7 cupos". Corrección del 2026-10-12.
- Frecuencia: cada ~16 s, visibles ~4,5 s.

## 8. Entrega (siempre)
1. **HTML final** en `~/Desktop/<producto>-quiz.txt`, copiado también con `pbcopy`. **Santiago lo quiere completo, listo para pegar en ImpulTienda**, con las imágenes embebidas (WebP en base64, ~1 MB) y el embed del VSL de **Panda Video** dentro de `<template id="vsl-template">`. Cuando hay cambios, se **reemplaza** el .txt viejo.
2. **Carpeta de imágenes** `~/Desktop/<producto>-imagenes/` con nombres claros (`p1-mujer.png`, `zona-papada.png`, `mockup.png`…). Sacar las que ya no se usan.
3. **HTML de prueba** `~/Desktop/<producto>-PRUEBA.html`: el mismo HTML con las imágenes **embebidas** (WebP en base64, ~1 MB), para abrir en Chrome sin la carpeta. Lo abro con `open -a "Google Chrome"`.
4. Copia en `OUTPUTS/AAAA-MM-DD-quiz-<producto>.html`.
5. Arriba del HTML, un **bloque de configuración** con `IMAGENES` (nombre → URL de ImpulTienda), `LINK_CHECKOUT`, `PIXEL_ID` y `SEGUNDOS_OFERTA`. El VSL va en `<template id="vsl-template">`.
6. **Probarlo en el navegador** antes de entregar: todos los pasos, sin imágenes rotas y con la oferta apareciendo a tiempo.

## ✅ Checklist antes de entregar
- [ ] Textos iguales al original, solo con la marca cambiada
- [ ] Ningún dato inventado
- [ ] Ninguna imagen con la marca vieja ni con texto en otro idioma
- [ ] Mockup: celular con app, sin libros
- [ ] Testimonios y garantía en HTML nítido
- [ ] Último paso: embed de Panda arriba y oferta oculta hasta después del precio en el VSL
- [ ] Espaciado amplio en la oferta
- [ ] Precio, tachado, cuotas, % OFF y FAQ consistentes
- [ ] Todos los CTAs con el link de checkout correcto
- [ ] Notificaciones discretas con cupos que solo bajan
- [ ] .txt + carpeta de imágenes + PRUEBA.html + copia en OUTPUTS

## Registro de correcciones
| Fecha | Quiz | Corrección | Regla |
|---|---|---|---|
| 2026-10-12 | Pilates Hormonal | Sacar "¡Todo lo que necesitas…" y "Al ingresar, desbloqueás…" | §5 sin encabezados de relleno |
| 2026-10-12 | Pilates Hormonal | Más espacio entre textos | §5 espaciado |
| 2026-10-12 | Pilates Hormonal | Precio $14.990, tachado $49.990, cuotas recalculadas | §6 |
| 2026-10-12 | Pilates Hormonal | Mockup de libros sueltos "horrible": celular con app | §4 mockup |
| 2026-10-12 | Pilates Hormonal | Testimonios escritos en imagen se veían mal | §4 HTML nítido |
| 2026-10-12 | Pilates Hormonal | Notificaciones feas e incoherentes (cupos 3 → 7) | §7 |
| 2026-10-12 | Pilates Hormonal | Imagen de garantía mejorada | §4 HTML nítido |
| 2026-10-12 | Pilates Hormonal | Todos los CTAs → `https://pilates-hormonal.impultienda.ar/checkout` | §5 CTAs (link propio de la oferta) |
| 2026-10-12 | Pilates Hormonal | Último paso: VSL arriba y oferta oculta 2:40 | §5 |
| 2026-10-13 | Pilates Hormonal | VSL de Panda (9:16) cargado; la oferta pasa a aparecer a los 3:50 | §5 |
| 2026-10-13 | Pilates Hormonal | Sacar el bloque de precio $14.990/tachado; las cuotas y el botón van primero, debajo de la cuenta regresiva | §5 orden de la oferta |
| 2026-10-13 | Pilates Hormonal | El sello de garantía estaba torcido | §5 sellos en SVG |
| 2026-10-13 | Pilates Hormonal | El .txt final va completo, con las imágenes embebidas, para pegarlo en ImpulTienda | §8 |
| 2026-10-12 | Pilates Hormonal | Imágenes con GPT Image 1.5 en Higgsfield | §4 |

## Preguntas abiertas
- ¿"Pilates Asiático" pasa a llamarse "Pilates Hormonal" en los textos o queda como nombre del método?
- ¿El sello de pago seguro (Visa, Mercado Pago) también se pasa a HTML?
- ~~¿Los 2:40 son fijos?~~ No: dependen de cada VSL (Pilates Hormonal: 3:50).
- ¿ImpulTienda acepta pegar un HTML de ~1 MB? Si no, volver al .txt liviano con las URLs de las imágenes subidas.

## Relacionado
[[quiz-funnel]] · [[imagenes-y-mockups]] · [[shopify-y-checkout]] · [[como-trabajar-con-santiago]] · [[landings-funnels-y-upsells]]

## Fuentes
- Conversación del 2026-10-12 (quiz de Pilates Hormonal, modelado de Sana Pilates). Entregable: `OUTPUTS/2026-10-12-quiz-pilates-hormonal.html`
