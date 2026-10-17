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
- **xquiz.link** (2026-10-14): el contenido viene sin cifrar en el payload de Next.js (`self.__next_f.push`). Se baja el HTML con `curl`, se decodifica y se saca el objeto `funnel` (`nodes`, `theme`, `navigation`). Cada página se abre directo con `/<slug>` para ver cómo se ve. Las imágenes están en `imagedelivery.net` y llegan a 512 px como máximo.
- **Lovable (`*.lovable.app`, 2026-10-15):** el quiz entero está en texto plano en el bundle `assets/routes-*.js` (preguntas, opciones, oferta, FAQ, popup de salida y testimonios). Se baja con `curl` y los colores salen de `:root` en `assets/styles-*.css` (vienen en `oklch`, se pueden usar tal cual). Las imágenes están en `/__l5e/assets-v1/…` y `/assets/…`. No hace falta abrir el navegador.
- **Quiz para el mercado en inglés (2026-10-15):** se localiza al inglés de EE. UU.: moneda en USD con los mismos números, nombres de testimonios y chats americanizados, "Turma" → "Class", medios de pago locales (Pix, Boleto, Elo) afuera.
- **Rapidez (2026-10-14):** con el JSON de pasos ya alcanza. Mirar en el navegador solo los componentes raros, sin recorrer paso por paso, y no generar imágenes con IA salvo la que tiene texto que no se puede editar (la tapa).

## 4. Imágenes
- **Reutilizar** las imágenes del original que no tienen marca ni texto en otro idioma.
- Las que tienen **marca vieja o texto en otro idioma** se rehacen:
  - Texto plano sobre un fondo liso (banda dorada, título de tapa): se reemplaza con Pillow, con la misma tipografía y el mismo color. La foto queda idéntica.
  - Texto en perspectiva o en varios objetos (mockups): se genera de nuevo con IA.
- **IA de imágenes: Higgsfield con GPT Image 1.5**, calidad **High** y **1:1** para la columna del quiz. Para el modelo, buscar "GPT Image 1.5" en el selector; por defecto aparece GPT Image 2.
  - Generar **desde texto** cuando se pueda. Subir una referencia obliga a aceptar el "Media upload agreement", y eso **requiere el OK de Santiago**.
  - La imagen final se descarga del CDN cambiando `_min.webp` por `.png` (1024×1024).
- **Mockup del producto: celular con la app, potente y premium.** Nada de libros sueltos ("parecen libros sueltos y se ve horrible", 2026-10-12). Un iPhone flotando con la UI de la app (logo, video de la clase, progreso del reto, accesos), fondo cálido de estudio y luz suave.
- **Revisar marcas de agua** (pngtree, freepik, etc.) en cada imagen del original y sacarlas. En los PNG transparentes, la marca suele tener alfa bajo, así que alcanza con borrar los píxeles con alfa menor a ~110 (2026-10-14).
- **Nada de capturas pixeladas.** Testimonios escritos, garantía y bloques de texto se arman en **HTML** (tarjetas nítidas), no como imagen. Corrección del 2026-10-12.
- **Foto redonda de la experta (2026-10-15, "se ve mal"):** armar una versión de la foto **sin ningún texto** (pintar el fondo) y recortar de ahí un plano abierto (cabeza entera, hombros y algo del producto), **sin agrandar** el recorte. Si se agranda, se pixela. Nunca recortar de la original con el nombre viejo.
- **Garantía en la paleta del quiz (2026-10-15, "se ve mal"):** no copiar la estética de la imagen original (fondo negro y rojo chillón) si choca con el diseño. Usar una tarjeta con los colores del quiz, sello dorado grande arriba, título en la fuente display y texto centrado. Los textos curvos del sello tienen que quedar adentro del círculo, sin pisar bordes ni anillos.
- Logo: si cambia la marca, rehacerlo con el mismo ícono y el mismo estilo tipográfico.

## 4b. Coherencia de componentes (2026-10-14)
- **Barra del IMC:** si el resultado dice "Sobrepeso", la bolita va **cerca de Sobrepeso** (~85%), nunca en Saludable.
- **Peso y altura (y peso deseado):** van **siempre** con un **medidor** (barra), aunque el original use botones +/− (2026-10-17) (un slider con el número grande en kg o cm y una regla), no con un campo de texto. Así es más fácil completarlos.
- **Zonas del cuerpo:** usar nombres que se entiendan en Argentina: "Caderas" en vez de "Cartucheras". Sacar "Flancos".

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
| 2026-10-17 | Secreto de la Insulina | "Quiero que sea igual al de él, basémonos en lo validado, el de Mounjaro no funcionó" | §2: cuando pasa el quiz de un competidor escalado, se copia **ese** quiz paso a paso (textos, orden, lógica). No se arma desde una plantilla propia ni se "mejora" el copy |
| 2026-10-17 | Secreto de la Insulina | Colores: "verde medio oscurito" en vez del naranja original | Paleta verde (#1f6b47); el logo naranja se recolorea a verde con Pillow (mismo diseño) |
| 2026-10-17 | Secreto de la Insulina | La promesa es la cantidad de kilos que la persona quiere bajar, en 21 días | Kilos = peso actual − peso deseado, sin multiplicadores (el original inflaba ×1,2) |
| 2026-10-17 | Secreto de la Insulina | "Las medidas de peso y altura las quiero con barra siempre" | §4b: peso, altura y peso deseado siempre con medidor (barra), aunque el original use botones +/− |
| 2026-10-15 | Chinese Embroidery | La garantía y la foto de Juliana "se ven mal" | §4: garantía en la paleta del quiz; foto de la experta sin texto, plano abierto y sin agrandar |
| 2026-10-15 | Chinese Embroidery | Checkout `https://chinese-embroidery.impultienda.ar/checkout` y precio 27 USD (no 27.90) | §6: en USD, precio redondo si así lo pasa; actualizarlo en todos lados (caja de precio y tachado del popup) |
| 2026-10-14 | Mounjaro Humilde | VSL final de Panda en el último paso; "QUIERO MI PLAN" al 1:20 → `https://mounjaro-humilde.impultienda.ar/checkout` | Los botones de los VSL del quiz usan el tiempo real de Panda (`panda_timeupdate`, filtrado por iframe) y, si no llega, un reloj desde `panda_play` |
| 2026-10-14 | Mounjaro Humilde | VSL de la nutri (Panda) en el paso 12, con el botón Continuar a los 30 s; sacar el audio de la página de resultados | Embed de Panda en `<template id="vsl-nutri">` y `SEGUNDOS_BOTON_VSL_NUTRI` |
| 2026-10-14 | Mounjaro Humilde | "Cartucheras" → "Caderas" y sacar "Flancos" | §4b zonas |
| 2026-10-14 | Mounjaro Humilde | Imagen "Todavía no sé" con marca de agua | §4 marcas de agua |
| 2026-10-14 | Mounjaro Humilde | El IMC decía "Sobrepeso" con la barra en "Saludable" | §4b barra del IMC |
| 2026-10-14 | Mounjaro Humilde | Peso y altura con medidor | §4b medidor |
| 2026-10-14 | Mounjaro Humilde | Sacar la pantalla de "¿Dónde preferís recibir tu plan? WhatsApp / E-mail" | No incluir el paso de elegir canal |
| 2026-10-15 | Mounjaro Humilde | Sacar también el paso del e-mail: "en el checkout se lo pedimos también" | **No pedir e-mail ni WhatsApp en el quiz**: los datos de contacto se piden en el checkout |
| 2026-10-14 | Mounjaro Humilde | "¿Por qué tardás tanto?" | §3 rapidez: armar desde el JSON, sin recorrido completo ni IA de más |
| 2026-10-13 | Landing Palabras de la Obediencia | Copiar la landing de VSL sin footer ni políticas; botón verde "COMPRAR AHORA" a los 2:45 del VSL de Panda | Landing de VSL: el botón se dispara con el tiempo real del video (`panda_timeupdate` por postMessage) y no con un reloj |
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
