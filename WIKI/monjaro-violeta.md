# Monjaro Violeta Japonés

> Oferta nueva para **Argentina**: la receta de una bebida de remolacha ("monjaro natural japonés") con protocolo de 30 días. Se modela del quiz brasileño de **Vovó Mei** (`monja-roxo.lovable.app`), que corre ~37 anuncios activos. Embudo: quiz → VSL → checkout. (fuente: conversación del 2026-11-04)

## Ideas clave
- **El original es brasileño y está escalando.** Página de Facebook *Vovó Mei*, ~37 anuncios activos, casi todos videos de 2 a 3 minutos, publicados entre el 9 de octubre y el 3 de noviembre de 2026. Biblioteca de Anuncios: `view_all_page_id=1359437227259333`.
- **Casi todos los anuncios muestran `instagram.com` como destino**: solo dos dejan ver el dominio real (`MONJARO-ROXO.LOVABLE.APP`, con el copy *"Receita Mounjaro / MOUNJARO ROXO JAPONÊS"*). El resto va por el mismo embudo.
- **"MONJARO", no "Mounjaro".** La marca del original está escrita mal a propósito: usa el gancho del fármaco sin escribir su nombre. **Se mantiene** en nuestra versión.
- **El quiz es largo: 68 pasos en el archivo = 34 reales**, duplicados en dos ramas (mujer / hombre) desde la pregunta de género. Nuestra versión son **27 pasos** para mujer (30 si declara una condición de salud).
- **La oferta no está en el quiz.** El último paso del original es solo un VSL; el precio y el carrito viven detrás del player. En el nuestro, la oferta va **abajo del VSL y oculta** hasta `SEGUNDOS_OFERTA` ([[quizzes-reglas-de-armado]] §5).

## Ficha de la oferta
| | |
|---|---|
| Producto | Monjaro Violeta Japonés — protocolo de 30 días |
| Público | **Mujeres y hombres** (el quiz se bifurca por género, igual que el original) |
| Idioma | Español argentino con voseo |
| Precio | **$14.990 ARS**, tachado $49.990 (70% OFF), 3 cuotas de $4.997 *(a confirmar)* |
| Checkout | `https://monjaro-violeta.impultienda.ar/checkout` *(a confirmar)* |
| Avatar | **Abuela Mei** (Vovó Mei): señora japonesa, pelo gris, túnica violeta |
| Mecanismo | La bebida de remolacha tomada en un horario exacto: "trabaja mientras dormís" |
| Promesa | Bajar 10 kg en 30 días (la del original) |
| Regalos | 5 PDFs por un valor declarado de $73.500 |

## El original: `monja-roxo.lovable.app`
- **Stack:** Lovable. El funnel entero viaja **en texto plano** en `assets/routes-*.js` — preguntas, opciones, alertas, testimonios y comparativa. No hace falta recorrerlo en el navegador ([[quizzes-reglas-de-armado]] §3).
- **Las imágenes no son de Lovable:** cuelgan de `media.inlead.cloud/uploads/24117/…`, o sea que el quiz **se exportó de InLead**. Los nombres traen el tamaño (`-xs-`, `-sm-`, `-md-`): las siluetas de tipo de cuerpo son **96×80 px** y no existen en tamaños más grandes (probado `sm`, `md`, `lg`, `xl`, `2x`: todos 404).
- **Los 34 pasos:** objetivo (multi) · género · zona de grasa (multi) · edad · kilos a bajar · nombre · tipo de cuerpo · cómo te afecta (multi) · conformidad · dificultades del día (multi) · **video de la Vovó Mei** · qué te impide · placa "cómo funciona" · beneficios (multi) · testimonio · peso · altura · peso deseado · rutina (multi) · sueño · agua · frutas (multi) · análisis · **resultado con IMC + alerta** · condición de salud (sí/no → campo → análisis → mensaje) · ~~WhatsApp / e-mail~~ · cuerpo soñado · análisis · antes/después · **VSL final**.
- **Dos players distintos:** el del paso 11 (`6ab0462b14e8c28e3b7cd846`) y el del paso final (`6ab046138aae747f61704d5e`), los dos de la cuenta `cd0d2f60-1b53-4b39-8198-42435c3310fd`.
- **Cinco alertas de IMC**, una por franja, y la barra va de verde a rojo con la bolita en la franja que corresponde.

## Qué se adaptó y qué no
| Original | Nuestro | Por qué |
|---|---|---|
| Los 34 pasos, su orden y su lógica | **Igual** | [[quizzes-reglas-de-armado]] §2 |
| "Onde prefere receber seu plano?" + WhatsApp + e-mail (4 pasos) | **Sacado** | Regla fija: los datos de contacto se piden en el checkout (registro del 2026-10-15) |
| `MONJARO ROXO JAPONÊS` | **MONJARO VIOLETA JAPONÉS** | "Roxo" no significa nada en castellano. La marca mal escrita se mantiene |
| Vovó Mei | **Abuela Mei** | — |
| Maria Conceição – Porto Alegre, RS | **Mariela Benítez – Rosario, Santa Fe** | Localización ([[quizzes-reglas-de-armado]] §2) |
| "Morango", "Abacaxi", "Maça" | **Frutilla, Ananá, Manzana** | Argentino, no neutro |
| Audio del testimonio (en portugués) | **Sacado** | No se puede reusar un audio en otro idioma y no vale la pena grabarlo para un paso intermedio |
| Infografía "COMO FUNCIONA" con texto quemado en portugués | **Placa de 3 pasos en HTML** | §4: los bloques de texto van en HTML nítido, no como imagen |
| Siluetas de tipo de cuerpo de 96×80 px | **Tarjetas con emoji y descripción** | §4: si faltan varias fotos del set, la pregunta va con íconos. No hay versión grande de esas siluetas |
| Paleta violeta del original | **Igual**, en oscuro (violeta #8A1FC4 + magenta #E626C8) | El original ya es violeta: no hay nada que recolorear |
| Sin oferta en el quiz | **Caja de oferta completa** estilo launch promotion | §4, corrección del 2026-11-03 |

## Imágenes
- **27 webp, 458 KB en total.** El `.txt` con todo embebido pesa **679 KB**, bien abajo del límite que aguanta ImpulTienda.
- **Reusadas tal cual:** las 4 parejas de edad, las 4 balanzas, las 6 frutas, los cuerpos de zona, las comparativas de hombre y mujer, los antes/después y la cara de la Abuela Mei.
- **Limpiadas:** los recortes con alfa sucio (bordes dentados) se pasaron por un umbral de alfa 110 + recorte al bounding box.
- **Rehechas con Pillow:** las chapas verdes de género (`MULHER` → **MUJER**, `HOMEM` → **HOMBRE**), con Arial Black sobre el mismo verde #039E00.
- **La portada** (`hero-monjaro.webp`) es el arte del original **sin el cartel en portugués**: se recortó la banda de arriba (jugo, remolachas, torii y la cara de la Abuela) y se le puso un **alfa en diagonal** que la funde con el fondo de la página. El lockup "MONJARO / VIOLETA / JAPONÉS" se rehízo **en HTML con CSS**, así queda nítido y editable.

## Estado
- ✅ **Quiz entero armado y probado en el navegador** (2026-11-04): `~/Desktop/monjaro-violeta/`.
  - Probados: portada, multi-select, bifurcación por género, fotos de edad y kilos, campo de nombre con `{{nombre}}`, placa de cómo funciona, testimonio, los 3 medidores, la pantalla de carga, el **IMC con la bolita en la franja correcta** (82 kg / 1,65 m → 30,1 → Obesidad → bolita al 90%), la rama de condición de salud (campo → carga → mensaje personalizado), la comparativa y la oferta entera con contador, cupos y notificaciones.
  - **Textos sensibles al género** con el token `{{o}}`: "¿estás list**a**/list**o**?", "Quedate tranquil**a**/**o**", "List**a**/List**o**, Ana".
  - Atajos de prueba: `?oferta=1` va directo a la oferta y `?paso=N` arranca en el paso N.
- ⏳ **Falta el VSL** (lo hacemos después): el embed de Panda va en `<template id="vsl-template">` y `SEGUNDOS_OFERTA` queda en **230 de prueba** hasta saber el segundo exacto en que nuestro VSL dice el precio.
- ⏳ **Falta el video corto de la Abuela Mei** del paso 11: va en `<template id="vsl-mei">`. **Si queda vacío, el paso se saltea solo** y el quiz sigue funcionando.
- ⏳ Falta confirmar **nombre del producto, precio y link de checkout**.

## Aviso de riesgo (anti-bloqueo)
La landing arranca con **"bajá 10 kg en 30 días"**, usa **antes y después** y el nombre de un fármaco deformado. Son justo las tres cosas que [[protocolo-chia-28d]] marcó como motivo de rechazo en Meta **aunque el guion del anuncio esté limpio**, porque Meta revisa el destino. Se dejó igual al original por fidelidad (§2), pero conviene tener a mano una versión de la portada sin kilos ni plazo ("Tu plan de 30 días con lo que ya hay en tu cocina") por si rebotan las cuentas.

## Preguntas abiertas
- ¿El producto se llama **Monjaro Violeta Japonés** o le ponemos otro nombre?
- ¿El precio es $14.990 o va otro? ¿El checkout es `monjaro-violeta.impultienda.ar`?
- ¿Metemos el video corto de la Abuela Mei en el paso 11 o lo dejamos fuera?
- ¿Los 5 regalos quedan como están o los cambiamos antes de escribir el VSL?

## Relacionado
[[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[protocolo-chia-28d]] · [[secreto-de-la-insulina]] · [[tai-chi-fit]] · [[vsl-reglas-de-armado]]

## Fuentes
- Biblioteca de Anuncios de Meta, página **Vovó Mei** (`view_all_page_id=1359437227259333`), consultada el 2026-11-04
- `https://monja-roxo.lovable.app/` y su bundle `assets/routes-5Qd2Kwpp.js`
- Entregables: `~/Desktop/monjaro-violeta/` y `OUTPUTS/2026-11-04-quiz-monjaro-violeta.html`
