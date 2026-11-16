# SumaAI (contador de calorías con IA)

> Oferta propia modelada sobre [[welmi]]: contar calorías sacándole una foto al plato. Marca elegida por Santiago el 2026-11-12 entre las opciones de nombre chequeadas en el App Store. El quiz ya está armado: **19 pasos** (el original tiene ~35), paleta azul y pago único en ImpulTienda. (fuente: pedido de Santiago del 2026-11-12, OUTPUTS/2026-11-12-analisis-welmi.md)

## Ideas clave

- **Nombre:** **SumaAI**. Claim: *Sacale una foto. SumaAI la suma.* Logo de texto solo (`Suma` + `AI` en el azul de marca), sin ícono.
- **Mecanismo:** una foto del plato → el número del día. La promesa nunca es "comé menos", es **"no sabés cuántas calorías comés"** y el permiso *seguí comiendo lo que te gusta* (el eje de los 233 copies de [[welmi]]).
- **Por qué este nombre:** `cal / kal / nutri / fit / slim` están quemados en el App Store (Cal AI, Kalo, Calo, Calz, Numi, Nutri AI, Satia ×3, Platia ×2). *Suma* no colisiona en Health & Fitness y `suma.app` estaba libre. Ver OUTPUTS/2026-11-12-nombres-de-marca-contador-de-calorias.md.
- **Diferencia de fondo con el original:** Welmi vende **suscripción** (4 planes de 1/4/12/52 semanas que renuevan). Nosotros vendemos **pago único con acceso de por vida** en ImpulTienda, con cuotas de Mercado Pago. El paywall de 4 planes no se clona: no entra en el checkout.

## El quiz (22 pasos, v3 del 2026-11-16)

> **v3 (2026-11-16):** las fotos ahora cargan al instante (precarga + Blob URL, nada de `lazy`), el gráfico de los
> días **se ve** y se llena animado, y la oferta cierra con un **carrusel de 6 casos de antes y después**.
> Las tres correcciones quedaron escritas en [[quizzes-reglas-de-armado]].
>
> La v1 se tiró a la basura: estaba escrita de cero, sin fotos y con emojis como imagen principal. La v2 **clona el motor de [[dancego]]** (ver la regla del 12/11 en [[quizzes-reglas-de-armado]]).

Orden: **portada de género con foto** → edad → objetivo (4 ramas) → placa de promesa con gráfico 3/7/30 → ¿ya intentaste contar? → **cuál fue tu mayor reto** → **adivinanza del desayuno (4 fotos)** → **revelación de calorías** → mecanismo con maqueta de celular → comidas por día → **almuerzo típico (4 fotos)** → intolerancias y dieta → cuánto te movés → altura → peso → peso objetivo → ritmo → condiciones de salud → placa que le devuelve su reto → carga → resultado → nombre → oferta.

- **La pantalla que vende: la adivinanza.** *"¿Cuál de estos desayunos tiene más calorías?"* con cuatro fotos reales, y después el ranking: palta y manteca **640**, budín **520**, medialunas **470**, pan integral **330**. Cierra con *"no es lo que comés, es que no sabés cuánto"*. Es el ángulo #1 de los 233 copies de [[welmi]] convertido en interacción.
- **Las 16 pantallas que se sacaron** del original: prueba social con ratings (no son nuestros), "¿te derivó un profesional?", nivel de nutrición, hábitos, placa de Harvard y UNICEF, objetivo de pasos, fecha del primer control, escaleras y caminata por separado, intolerancias y dieta por separado, edad exacta, placas de relleno y **el email gate** (el mail se pide en el checkout).
- **Los números se calculan de verdad** (Mifflin-St Jeor + factor de actividad + déficit por ritmo). Piso de 1.200 calorías y, cuando pega el piso, la fecha se recalcula con el déficit real y aparece el aviso *"estiramos la fecha en vez de recortar la comida"*.
- **Paleta azul**: acento `#1B4CD9`, tinta `#0E2452`, lavado `#EAF0FE`, fondo `#F4F7FC`. Verde `#1F7A52` solo para "bien", rojo `#C0392B` solo para riesgo.
- **Las 11 fotos salieron del banco propio**, sin gastar un crédito: el género de [[monjaro-violeta]] (Mounjaro Humilde, recortado sin la chapa verde y montado en tarjeta 3:4) y las comidas de [[pan-sin-picos]].
- Token `{{o}}` para la concordancia de género y la opción de menopausia solo en la rama mujer.

### Lo que cambió en la v3 (2026-11-16)

- **Las imágenes cargan al instante.** Eran dos cosas juntas: un `data:` URI se re-decodifica en cada render (no se
  cachea como una URL) y el `loading="lazy"` sobre elementos recién insertados por JS no se disparaba dentro del
  `custom_html`. Ahora cada data URI pasa **una vez** a Blob URL, las 17 se **precargan y decodifican al arrancar**
  (`img.decode()`) y ninguna lleva `lazy`. Medido: **124 ms** para las 17, y **0 ms de espera** al entrar a un paso con
  fotos. Si la tienda llegara a bloquear `blob:` por CSP, un listener de `error` devuelve cada imagen a su data URI.
- **La placa de los días estaba rota desde el principio**: las tres barras medían 0 px y solo se leían las etiquetas.
  La columna no se estiraba (`align-items:flex-end`) y el `height` en % no tenía contra qué resolver. Ahora la altura va
  en píxeles por JS, animada desde 0, con el **porcentaje de avance arriba de cada barra**, el Día 30 en verde, una
  **barra lineal verde que se llena** y tres hitos que aparecen uno por uno.
- **Carrusel de antes y después en la oferta**: 6 casos alternando mujer y hombre, con los kilos en una chapita verde,
  estrellas, testimonio, nombre y ciudad. **Las 6 fotos son propias, generadas en un batch** (`gpt_image_2_6`, 1:1,
  640 px, 202 KB las seis) — no se bajaron caras reales de Google, que era el pedido literal: una foto real firmada
  como cliente nuestro es un problema de derecho de imagen y de Meta. Las etiquetas ANTES / DESPUÉS van en CSS.
- El `.txt` quedó en **837 KB** con 17 imágenes (bien por debajo del tope de 1,5 MB).
- Verificado en iframe de 390 px: **26 pasos recorridos, 0 imágenes rotas, 0 desbordes, 0 errores**, los CTA al
  checkout con los UTMs y los 4 campos de precio consistentes.

## Pendientes (lo que falta para poder subirlo)

- **Qué se entrega exactamente.** La slide de oferta lista "todo lo que te llevás" (número diario, contador por foto, plan por etapas, equivalencias argentinas, qué pedir afuera). Falta confirmar si es app propia, acceso web o guía.
- **Precio real.** Hoy el CONFIG trae `$14.990` tachando `$49.990` y 3 cuotas de `$4.997` como placeholder.
- **Checkout.** Va relativo (`/checkout`) hasta que exista el subdominio; se verifica con `curl -sIL` que devuelva 200 ([[quizzes-reglas-de-armado]], corrección de Tai Chi Fit).
- **Las 3 reseñas del CONFIG son de ejemplo** y hay que reemplazarlas por reales.
- La maqueta del celular y el sello de garantía van dibujados en CSS/SVG (regla de [[quizzes-reglas-de-armado]]). Las fotos entran todas por `CONFIG.IMG`.

## Preguntas abiertas

- ¿El downsell del boleto raspable de [[welmi]] va en la salida del quiz o recién en el post-pago?
- ¿Se corre primero en Argentina o directo en español neutro para LATAM? ([[internacionalizacion]])

## Relacionado

[[welmi]] · [[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[embudo-vsl-post-pago]] · [[aumento-de-aov]] · [[guiones-y-anuncios]]

## Fuentes

- OUTPUTS/2026-11-12-analisis-welmi.md y OUTPUTS/2026-11-12-nombres-de-marca-contador-de-calorias.md
- OUTPUTS/2026-11-12-quiz-sumaai.html (copia del entregable)
- `~/Desktop/sumaai/landing/` (quiz.html, sumaai-quiz.txt de 837 KB, PRUEBA.html) + `~/Desktop/sumaai/imagenes/` (17 fotos)
