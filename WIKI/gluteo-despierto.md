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
> ⚠️ **Se entregó dos veces.** La primera versión clonaba **nuestro** motor (Fraunces + Inter, paleta ciruela, Índice de
> Activación Glútea, 22 pasos). Santiago la rebotó: *"No, no entendiste, quiero el mismo diseño que ellos, pero que diga
> cosas distintas"*. Quedó guardada en `OUTPUTS/2026-11-14-quiz-gluteo-despierto-v1-motor-propio.html`, pero **la que vale
> es la v2**. Ver la regla del 14/11 en [[quizzes-reglas-de-armado]].

**La v2 es el documento del competidor con los textos reescritos.** Se bajó su quiz entero con `curl -sL`, se cortó el
documento del `custom_html` y se reemplazó, paso por paso, cada texto. **No se tocó ni una regla de su CSS, ni su sprite
de íconos, ni una línea de su motor**: quedan sus 30 pasos, su violeta `#970FA9`, sus botones verdes, sus flechitas, su
aviso rojo de la portada y sus tres pantallas de carga con porcentaje.

El reemplazo se hace con un script, no a mano: `OUTPUTS/scripts-quiz/build_gluteo_despierto.py`. Parte el documento por
`<section class="paso">`, aplica a cada paso su lista de pares (viejo → nuevo) y **falla si alguno no aparece** o si
queda algún rastro del competidor. Si mañana hay que retocar un texto, se toca ahí y se vuelve a correr.

**Lo que cambia:**
- **Los 24 cuestionarios y sus ~120 opciones, reescritos uno por uno** en voseo, con el mismo golpe y otro fraseo
  (*"¿Cuánto tiempo por día podés dedicarle a entrenar?"* → *"¿Cuántos minutos por día le podés dar de verdad?"*).
- **El mecanismo.** Las 3 fases del Protocolo (Despertar · Aislar · Cargar) reemplazan su *Método Anti-Lesión + Rutina
  Express + Protocolo Sin Sentadillas*. Su promesa de **20 minutos y 4 semanas** pasa a **15 minutos y 28 días**.
- **El diagnóstico.** Sus *3 patrones detectados / 1 mentira revelada / 1 solución personalizada* pasan a
  **1 músculo dormido / 1 mentira que te vendieron / 1 protocolo de 28 días**.
- **Los 3 testimonios**, con nombre + ciudad argentina (Rosario, La Plata, Córdoba).
- **Una FAQ más que ellos** (*"¿Es una suscripción?"*), que es la objeción madre del low ticket. Es su mismo componente.
- **La línea de cuotas de Mercado Pago**, que ellos no tienen: va **debajo** de la caja de precio, no adentro
  (metida en el `<span>` del original parte el precio en cinco renglones). Una sola regla de CSS nueva, `.cuotas`, con
  el verde que su propia caja ya usa.
- **El bloque de configuración arriba del script** (`CHECKOUT`, `PIXEL_ID`, `VSL_MP4`, `BOTON_SEGUNDO`) y el pixel de
  Meta con `AddToCart` en los CTAs, que su versión no traía.

**Imágenes: 13 de 15 son suyas.** Las que no llevan marca ni texto se reusan tal cual (las 3 de las cargas, el
antes/después, los 3 resultados, los 3 avatares, los sellos de compra y el de garantía). Se rehicieron las dos que sí la
llevaban:
- **El logo**: el de ellos es un durazno con cinta métrica. El nuestro es un durazno con **tres ondas de activación** —
  el músculo que se enciende. Dibujado con Pillow y **mirado a 135, 96 y 60 px** antes de aceptarlo.
- **La portada**: mismo formato que la de ellos (dos bandas violetas arriba, el díptico antes/después, el pie violeta),
  con *SIN / CON el Protocolo del Glúteo Dormido* y *"Mariana despertó el glúteo y paró la cola en 28 días, en el living
  de su casa. SIN UNA SOLA SENTADILLA."*

**Verificado por código** en un iframe de 390 px: **los 30 pasos recorridos, 0 desbordes, 0 imágenes rotas, 0 errores**
de consola; los **9 CTAs** de la oferta al checkout **arrastrando `utm_source`, `utm_campaign` y `fbclid`**; y el `.txt`
autocontenido (1.010 KB) con **las 15 imágenes y el favicon en base64**, ninguna rota.

## Preguntas abiertas
- **El nombre del método y de la marca los elegí yo** ("Glúteo Despierto" / "Protocolo del Glúteo Dormido"). Si Santiago prefiere otro, se cambia en `build_gluteo_despierto.py` y se vuelve a correr.
- **13 de las 15 imágenes son del competidor** (las neutras, sin marca ni texto). Es lo que manda la §4 de la checklist y lo que mantiene su diseño, pero **corremos en su mismo feed**: si Santiago quiere fotos 100 % propias, se generan con IA y se reemplazan en `imagenes/`.
- **El subdominio de ImpulTienda no está confirmado.** El checkout quedó **relativo** (`/checkout`), que resuelve solo en la tienda donde se pegue el HTML ([[quizzes-reglas-de-armado]], regla del 11/11). Cuando esté el subdominio se cambia **una línea** del `CONFIG`.
- **Falta el VSL.** `VSL_MP4` está vacío y `BOTON_SEGUNDO` en 0, igual que el competidor (su botón de diagnóstico también se ve de entrada). El de ellos es un **MP4 propio de 720p** servido desde los recursos de su tienda, no un player externo.
- **Los 3 testimonios son de ejemplo**, marcados en rojo en el HTML. Reemplazarlos por reales antes de poner plata.
- Falta la tanda de anuncios y el backend (los 2 upsells del competidor son el molde más cercano).

## Relacionado
[[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[funnel-hacking]] · [[embudo-post-compra]] · [[pilates-hormonal]] · [[origen-pilates]] · [[landings-funnels-y-upsells]]

## Fuentes
- Biblioteca de Anuncios de Meta, búsqueda `guiapiernasycola.impultienda.ar` y `glúteos sin sentadillas cola parada` (AR), 14/11/2026
- `curl -sL https://guiapiernasycola.impultienda.ar/` — quiz, oferta, precios, bonos y upsells en texto plano
- Entregable: `OUTPUTS/2026-11-14-quiz-gluteo-despierto.html` · paquete en `~/Desktop/gluteo-despierto/`
