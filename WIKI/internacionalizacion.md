# Internacionalización

> La misma oferta en varios mercados es "múltiples ofertas en profit". Qué países targetear según el mercado, localizar en vez de traducir, densidad poblacional y la decisión de moneda. (fuente: RAW/2026-10-10-wiki-previa/internacionalizacion.md)

Vector de escala una vez que una oferta está validada y el mercado inicial se satura. Es el último eslabón del bucle del negocio ([[filosofia-de-marketing]]).

## Mercados

**Base histórica:** Argentina.

**Mercados habituales:** México · Estados Unidos · España · Uruguay · Chile · Colombia · resto de LatAm · Europa · Norteamérica · Reino Unido · Canadá · Australia · Nueva Zelanda.


## Replicar la oferta: el método de las «múltiples ofertas en profit»

La estrategia que más apalanca todo el sistema, y que suena a más trabajo del que es:

> «**No necesitás más de una sola oferta.** Tengo múltiples ofertas en profit porque tengo **esa misma oferta en diferentes mercados**.»

### Lo que hace falta

1. **Un funnel validado** — TSL, VSL o quiz, da igual cuál
2. **5–6 anuncios validados**
3. **Una pasarela que cobre en ese mercado**

Y nada más. En particular, **no hace falta LLC**: con Hotmart se puede validar la oferta en otro mercado sin empresa en EE.UU., sin Stripe y sin Shopify Payments. Ver [[shopify-y-checkout]].

### El problema que resuelve

En un mercado chico y barato como Argentina el CPC es bajísimo, pero **te topás con un techo**: al querer escalar, el CPC sube y la oferta no da más de sí. Estás en 300–500 USD/día y capeado.

La oferta no está agotada — **el mercado sí**.

### Los números cambian por completo

Dato concreto de una oferta suya fuera:

> **ROAS 2 con un CPC de 1,82 USD** y un **AOV de ~60 USD**.

Un CPC de 1,82 sería descarte inmediato en LatAm ([[metricas-y-kpis]]). Ahí funciona porque el ticket y el AOV son de otra escala. **Nunca se compara una métrica aislada entre mercados: se compara el conjunto.**

### Cómo traducir la tienda — el procedimiento

**Todo en la misma tienda.** No hace falta crear una nueva.

**1. Publicar el idioma en Shopify**
Configuración → **Idiomas** → agregar idioma → asignar a dominio → **Publicar**.

**2. Traducir con Translate & Adapt**
App de Shopify. «Traducir automáticamente» → tarda **~10 minutos**.

**3. El truco del URL**
Se añaden las **siglas del idioma después del dominio**: `tudominio.com/**en**/...`

Con eso la misma página se sirve en el otro idioma. Y funciona igual para el **carrito** y el **checkout**: mismo `/en/` en el URL del carrito y todo el flujo de pago aparece traducido.

**4. Lo que la IA no traduce**
- **Las imágenes hay que traducirlas a mano** (Canva, Higgsfield, Sora). Si la landing es de imágenes apiladas, es trabajo manual
- Si la landing es **con código**, se le pide a la IA que la traduzca — trivial. Otra ventaja del código sobre las imágenes ([[pagina-de-ventas]])

**5. Los anuncios**
Traducir el guion con ChatGPT → generar la voz en **ElevenLabs** o Google Studio. Ver [[ugc-y-video-generativo]].

**6. Opcional, y él no lo hace**
Dominio en inglés y fanpage en inglés. Si querés lanzar rápido, no hace falta.

> **Requisito duro:** Shopify Payments, o Stripe + PayPal. **Con Mercado Pago no se puede vender multiidioma**, sea de Argentina, Chile o Colombia. Ver [[shopify-y-checkout]].

### Lo que cambia en el ticket

El motivo real de hacerlo. Cifras de su tienda en habla inglesa, mostradas en pantalla:

| | Valor |
|---|---|
| Front | **29 USD** |
| Ticket promedio diario | 34 · 36 · 37,87 · **48 USD** |
| Semana completa | ~37 USD de ticket promedio, ~10.000 USD en ventas |

Frente a los 15–20 USD de ticket habituales en LatAm.

> «Podés duplicarle o triplicarle el ticket del front, exactamente el mismo producto, y **no vas a tener ningún tipo de fricción** al momento del pago.»

Es el mismo PDF. Lo que cambia es el poder adquisitivo del mercado.

### No todas las ofertas agarran en todos los mercados

Contrapeso necesario, de un caso real en mentoría: una oferta que vendía bien en LatAm se pasó a inglés y **dos días sin una sola venta**, pese a tener buenos números de tráfico —muchos inicios de checkout y carritos abandonados—. Bajar el precio no lo arregló.

El diagnóstico de Santiago:

> «Hay ofertas que en un mercado no agarran. Podés probar esa oferta en Italia, Francia o Rusia. **Pero si no agarra, no le insistas. No le gastes mucho dinero.**»

Misma disciplina que en [[validacion-de-oferta]]: la replicación es barata, pero no es gratis, y no convierte una oferta en universal. Si el cuello está en el checkout, se puede intentar mejorar la oferta antes de abandonar ([[diagnostico-de-checkout]]).

### Mercados menos obvios

Además de los habituales, menciona **Rusia, mercado árabe y Rumania**. La lógica: si una comunicación funciona, puede funcionar en culturas donde nadie está corriendo esa oferta.

Existe una clase en el canal sobre **traducir una tienda de Shopify por completo**.

### Cómo encaja con la caducidad de las ofertas

Las ofertas mueren a los 3–4 meses ([[modelo-low-ticket]]). Replicarlas en mercados nuevos es la forma más barata de **extender la vida de una oferta ya validada** antes de tener que buscar otra: el trabajo duro —comunicación, funnel, creativos— ya está hecho y pagado.

## Densidad poblacional: el criterio que decide el techo

Por qué unos mercados escalan y otros no:

> La sostenibilidad y el potencial de escala salen de la **densidad poblacional**. Más audiencia = los creativos se saturan más lento = la oferta aguanta más presupuesto.

| Mercado | Tamaño | Nota |
|---|---|---|
| **Tier 1 habla inglesa** | ~400 millones | **El de mayor potencial**: mayor ticket promedio, más escalabilidad y sostenibilidad |
| **LatAm habla hispana** | Muy grande | Buen equilibrio tamaño/dificultad |
| País individual | Chico | Techo rápido |

> ⚠️ **El mercado inglés es más difícil de entrar.** **No se recomienda para empezar.**

El orden natural: validar en tu país → LatAm → habla inglesa.

## A qué países targetear

El targeting que se usa por mercado.

### Si estás empezando: tu propio país

Vender en tu país con **tu pasarela local** (Mercado Pago argentino, mexicano, uruguayo…) integrada a Shopify. Es lo que hizo él antes de poder costear una LLC.

Alternativas si te bloquearon la pasarela local:

| Vía | Coste | Alcance |
|---|---|---|
| **Hotmart** | — | Todo el mundo |
| **LLC** | 400–500 USD de apertura | Todo el mundo, a los pocos días |
| **Shopify Payments** | — | Solo si resides en EE.UU./Europa o tienes ciudadanía europea |

### Mercado LatAm

Targeting habitual: **Estados Unidos** (por el volumen de hispanohablantes), **Chile, Colombia, Perú, Uruguay, México y Europa** (a veces solo España).

**Argentina se excluye** de ese conjunto — porque corre la misma oferta en una tienda Shopify aparte con Mercado Pago, lo que **sube la conversión del checkout**.

### Mercados en inglés

**Tier 1**: Estados Unidos, Canadá, Reino Unido, Australia, Nueva Zelanda. Los de mayor capacidad de compra.

Ampliación posible con **ticket más barato**: Sudáfrica, o directamente **Worldwide** (hay angloparlantes en India, Indonesia y toda Europa).

### Otros mercados

| Mercado | Táctica |
|---|---|
| Italia, Francia | Targetear el país directamente |
| Francés | O bien **Europa + idioma francés** (hay francófonos en varios países) |
| Rusia | **Worldwide + idioma ruso** — Meta no permite targetear Rusia directamente |

### El método para depurar

1. Correr unos días **por continente** (América del Norte, del Sur, Central, Europa, Caribe)
2. Calcular por país el **revenue por visita** y compararlo con el **costo por clic**
3. Dejar solo los países rentables — **después de 100–300 conversiones**, no antes

Es la misma ecuación de siempre ([[metricas-y-kpis]]), aplicada como filtro geográfico.

> Dato de contexto del mismo video: 10 tiendas activas, margen aproximado del **40%**. La cifra de facturación se transcribe de forma ambigua («más de $10,000» frente a los 119K del título), así que **no es fiable en el estado actual del material**.

## Cuándo salir del mercado local

**Umbral:** cuando ya tienes facturación sostenible, **100–300 USD de ganancia al día** (`RAW/formacion/mentorias/mentoria-2025-11-13.md`).

El argumento es de tamaño de audiencia: Argentina son ~44 millones de personas. Sumar Uruguay, Chile, Colombia, Ecuador y México es del orden de **10× la audiencia**.

Y tiene una consecuencia operativa concreta que Santiago mide:

> «Tiro una dúplica en una CBO a 50 dólares y **me dura una semana**. En Argentina muy pocas veces me duró.»

Más audiencia = **los creativos se saturan más lento** = escalado más estable y sostenible. Conecta con [[renovacion-de-creativos]]: parte del desgaste de creativos en mercados chicos es simple agotamiento del público.

Con experiencia, los productos nuevos se lanzan **directamente afuera**.

**No hace falta Shopify Payments para empezar:** se puede validar en Hotmart, que cobra en todo el mundo. Ver [[shopify-y-checkout]].

## Localizar, no traducir

El principio está declarado sin ambigüedad: no se traducen anuncios. Se adapta **lenguaje, acento, avatar, referencias, precio, mercado, oferta y copy**.

| Mercado | Registro |
|---|---|
| Argentina | Español argentino / rioplatense (a veces marplatense) |
| LatAm | Español latino neutro |
| EE.UU., Reino Unido, Canadá, Australia, NZ | Inglés |

El avatar también cambia por mercado, no solo el idioma. Ver [[ugc-y-video-generativo]].

## Implicaciones técnicas

**La decisión de moneda tiene consecuencias reales**, y es probablemente el punto de fricción más importante de la expansión:

- Con **Shopify Markets**: checkout en moneda local, mejor conversión, pero **el upsell post-pago solo se ve en países con moneda dólar**
- Sin Markets, **todo en USD**: se pierde algo de conversión de checkout, pero se habilita el upsell post-pago para todos

Para subir el AOV, la segunda opción es la que habilita el upsell post-pago. Ver [[shopify-y-checkout]] y [[aumento-de-aov]].

Hay lección dedicada a **multiidioma** en la tienda.

## CPM por mercado

El CPC tolerable cambia radicalmente:

- **LatAm**: 0,10–0,50 USD
- **Estados Unidos**: hasta 1 USD

Pero los números del funnel también cambian (ticket, AOV, conversión), así que la comparación siempre es del conjunto, no de una métrica. Ver [[metricas-y-kpis]].

Táctica relacionada: **testear varias cuentas publicitarias para «relojear» el CPM** — hay lección específica. Correr el mismo producto en varias cuentas permite comparar y escalar más agresivo. Ver [[escalado-en-meta-ads]].

## Infraestructura financiera

Evaluada para cobrar internacionalmente: **AstroPay, Payoneer, Trust Wallet** (con su tarjeta de débito), SWIFT/BIC, transferencias entre Payoneer y AstroPay. Ver [[stack-de-herramientas]].

## Fuente de ofertas

La internacionalización funciona también en sentido inverso: **Brasil y Estados Unidos son la fuente de ofertas a modelar**, precisamente porque van por delante y lo que allí funciona aún no se está corriendo en el mercado local. Ver [[seleccion-y-modelado-de-oferta]].

## Complementos prácticos

- **VSL en otro idioma:** grabar el avatar en HeyGen **sin subtítulos** y usar la traducción de un clic para generar las otras versiones desde la misma grabación.
- **Doblaje barato:** aislar el audio sobre un **video negro** y traducirlo con HeyGen. Sale mucho más barato que el doblaje dedicado de ElevenLabs.
- **Escala por región:** targetear región completa (Norteamérica, Sudamérica, Centroamérica y Caribe, Europa) con el resto abierto. Después cruzar el **revenue por sesión por país** (lifetime, desde la tienda) con el **costo por visita desglosado por país** en Ads Manager, y quedarse solo con los países donde el revenue por sesión supera al costo por visita.

Relacionado: [[modelo-low-ticket]] · [[shopify-y-checkout]] · [[metricas-y-kpis]]

## Conexiones con tu operación actual
- **"No necesitás más de una oferta."** Con [[scented-stones]] validada, la jugada de más palanca es **replicarla en otros mercados**, no buscar otra oferta ([[ofertas]]).
- **Lo hiciste al revés del manual.** El orden recomendado es tu país → LatAm → inglés, porque "el inglés es más difícil y no se recomienda para empezar". Tu winner nació en Tier 1 inglés. El camino natural ahora es bajar: **LatAm en español neutro, Argentina con voseo**, y probar Italia, Francia o Worldwide en inglés.
- **Localizar, no traducir:** en español la persona puede ser **Carmela Vega**, que ya existe en tus ofertas de AR, en lugar de Emma Carter. Las referencias cambian (ferias, cumpleaños de 15, bautismos) y el precio también: en LatAm el ticket ronda los 15–20 USD.
- **"Si no agarra, no le insistas":** es lo que hiciste con el alemán ([[guiones-y-anuncios]]).
- **Mercado Pago no permite multiidioma.** Para AR hace falta una tienda aparte.

## Clonar un anuncio ganador a otro idioma sin rehacerlo (2026-11-02, tanda rusa de piedras)
Pedido de Santiago: *"haceme estos mismos anuncios pero en ruso, todo igual"*. El resultado es el **mismo video** (misma imagen, misma música, misma duración), solo cambia el idioma. Receta, en `OUTPUTS/scripts-vsl/` + `OUTPUTS/scripts-vsl/render_idioma.py` (copia de trabajo en `~/Desktop/<oferta>/anuncios/<idioma>/work/render_ru.py`):

1. **Transcribir el original** con Gemini (`gemini-3.5-transcribe`) y preguntarle género, edad y si hay música.
2. **Separar la pista con demucs** (`--two-stems=vocals`): se tira la voz vieja y **se conserva la cama musical original**. Es lo que hace que suene igual y no haga falta buscar música.
3. **Guion traducido y medido**: se escribe ~15 % más corto que el inglés (el ruso es más largo) y se ajusta el tempo al final para que la voz calce **exacto** con el largo del video, así ningún plano se corre.
4. **Voz** con la voz fija de siempre (mujer → Sulafat) y el acento dirigido desde el Style ([[como-trabajar-con-santiago]]).
5. **Subtítulos quemados**: se borran los del idioma original por *inpainting* de la banda (OpenCV TELEA, máscara = blanco + color de la caja + borde negro) y se escriben los nuevos con **la misma tipografía, el mismo color de caja y la misma posición**, medidos del original. Para fuentes con cirílico: Bitter Black (serif pesada), Montserrat ExtraBold y Nunito (sans).
6. **Nivel de voz**: se iguala el `mean_volume` de la voz separada del original, para no romper la mezcla.

Cuidado con el *timeline* de la capa de subtítulos: hay que armarla con **instantes absolutos**, no acumulando duraciones, o el solape de cada línea corre los subtítulos varios segundos.

**Después del clon vienen las variables, y para esas no hace falta material nuevo (2026-11-11, Brasil).** Cuando un mercado ya tiene su tanda clonada, el paso siguiente no es clonar más: son **guiones nuevos del mismo ganador** en ese idioma. El visual se arma con los propios ads clonados usados como pool de recortes, con un zoom que deja el subtítulo quemado fuera del encuadre ([[renovacion-de-creativos]]). Sale una tanda sin bajar un clip ni gastar un crédito, y los planos no se parecen a los que el segmento ya vio.

### Correcciones acumuladas

- **2026-11-03 · Del segundo idioma en adelante, no se rehace nada del video.** Las bandas ya limpias (`tmpN/band.mp4`) y los stems de demucs **no dependen del idioma**: se copian del pase anterior y el idioma nuevo pasa a ser solo **guion + voz + subtítulos**. El pase polaco de piedras salió en minutos porque reusó todo el material del pase ruso. Guardar siempre `band.mp4`, los stems y las fuentes al terminar una tanda (`~/Desktop/<oferta>/anuncios/_assets/`).
- **2026-11-03 · El tempo del VO tiene techo: ~1.35**, y se mide **antes** de renderizar (`duración del wav ÷ duración del video`). Si se pasa, el arreglo que más rinde **no es recortar el guion sino pedirle ritmo al Style**: agregar *"mów bardzo szybko, w tempie reklamy, bez pauz między zdaniami"* (hablá muy rápido, en tempo de publicidad, sin pausas entre frases) bajó PL2 de 73 s a 56 s y PL4 de 91 s a 72 s **con el mismo texto** — de tempo 1.45 a 1.12 y 1.14. Recortar el guion es el segundo recurso.
- **2026-11-03 · La misma toma de TTS varía muchísimo.** PL4 con texto recortado un 5 % salió igual de largo que el original (91,3 s vs 90,9 s): la diferencia la hace el ritmo de esa toma, no el largo del texto. Conviene **generar, medir y quedarse con la toma más corta** antes de renderizar, nunca asumir que el recorte alcanzó.
- **2026-11-03 · Verificar los glifos del idioma antes de renderizar**, igual que con los emojis ([[guiones-y-anuncios]]). Se renderizan `ą ć ę ł ń ó ś ź ż` (o el set del idioma) con cada fuente y se compara con el tofu de un carácter que seguro falta; si coinciden, la fuente no tiene el glifo y dibujaría cuadraditos. Bitter, Montserrat ExtraBold y Nunito tienen cirílico **y** polaco.
- **2026-11-03 · Localizar moneda y plataformas, no solo el idioma.** En polaco: **złoty** (no dólares, que matan la credibilidad), **OLX** en lugar de WhatsApp Business, e **imieniny** (onomástico) en la lista de ocasiones junto a fiestas y bodas. El CTA usa el texto real del botón de Meta en ese idioma (*Dowiedz się więcej*).
- **2026-11-03 · Polonia se targetea directo**, a diferencia de Rusia (que necesita Worldwide + idioma ruso).

- **2026-11-07 · La banda heredada se revisa, no se asume.** El pase portugués de piedras reusó los `band.mp4` del pase ruso y el del anuncio 4 traía un **fantasma rosa** de la caja magenta inglesa: el TELEA se había comido el núcleo saturado pero no el antialias ni la sombra, y rellenó propagando ese rosa. En ruso y en polaco no se vio **por casualidad** —el texto de esos idiomas caía justo encima—, y en portugués, con otro largo de línea, quedó al descubierto. Regla: **hoja de contactos de la banda cruda antes de renderizar cada idioma nuevo**, no solo del video terminado.
- **2026-11-07 · Una caja de color saturado no se borra con inpaint solo.** La receta que funciona toca **solo dos cosas** del script de siempre: (1) **máscara del color más laxa** —en el anuncio 4, de `S>110` a `S>35` con hue 135–170, para agarrar el antialias y la sombra de la caja, que es lo que el TELEA no veía y después propagaba hacia adentro—; (2) después del inpaint, **un segundo inpaint** (radio 7 y luego radio 4 sobre la máscara dilatada) y un **blur gaussiano difuminado sobre la propia máscara**. Las cajas claras tipo rosa `#E80060` sobre fondo claro (anuncios 1 y 3) salen con el inpaint simple de siempre.
- **2026-11-07 · No tocar el filtro de "blanco Y borde oscuro juntos" al reescribir la máscara.** Al rehacer la banda del 4 se perdió la línea `m = (m & dilate(both)) | color`, que exige que el blanco tenga un borde oscuro cerca para contar como texto. Sin ella entra **toda la tela blanca del video** en la máscara y el blur borronea media banda: el fantasma rosa desaparecía, pero el fondo quedaba lavado. Con la línea puesta, la máscara cubre ~20 % de la banda y las flores, la cuerda y la mano siguen nítidas. Es el filtro que separa "texto blanco" de "cosa blanca".
- **2026-11-07 · La toma se elige por texto correcto, no solo por largo.** En portugués, la toma A del 3 se comía el *minha* de "minha contadora" y la B del 4 decía *mole essencial* por "óleo essencial" y *se eu vindo* por "se eu vendo". Se verifica con **whisper medium**, nunca con small: el small inventa errores que no existen (dio "nunca vim de nada" donde la voz decía "nunca vendi nada"). Si la toma falla una palabra, se generan dos más antes de renderizar.
- **2026-11-07 · Si el idioma sale más corto que el video, se elige la toma MÁS LARGA.** Es el caso inverso al polaco: el portugués de los anuncios 1 y 3 dio tempos por debajo de 1.0 (0.967 y 0.981), o sea que la voz se **estira** en vez de acelerarse. Estirar se escucha más que acelerar, así que ahí la regla del "quedate con la toma más corta" se da vuelta: se busca el tempo más cerca de 1.0, no el mínimo.
- **2026-11-07 · Localizar Brasil.** Moneda **real** (~5,4 R$/USD, redondeado a cifras que un brasileño diría). **WhatsApp Business se queda** —al revés de Polonia, en Brasil sí es *la* referencia de la mujer que vende desde casa—. **Amigo secreto** entra en la lista de ocasiones junto a aniversário, Natal y casamento. Y ojo con el calendario: **las estaciones están invertidas**, así que la urgencia de "esta primavera" se reemplaza por **"antes das festas"** (el Natal), que además aprieta más. CTA con el botón real de Meta: *Toque em Saiba mais*. El Style de la voz tiene que pedir explícito **"sem acento de Portugal: português do Brasil puro"**.
- **2026-11-07 · Brasil se targetea directo**, como Polonia.
- **2026-11-09 · Tres anuncios más a Brasil (BR6–BR8), y tres trampas del pase.** Los originales traían **tres estilos de subtítulo distintos** (karaoke amarillo sin caja, píldora acumulativa, píldora de una palabra), así que el pase ya no es "guion + voz": hay que medir cada estilo.
  - **La fuente se identifica por el ancho de una frase a altura de mayúscula fija.** Se mide la cap height en el fuente (42 px) y el ancho de un bloque conocido ("THERE ARE THREE" = 505 px), y se prueban las fuentes del proyecto buscando cuál reproduce ese ancho a esa altura: Nunito 800 dio 525 y Montserrat ExtraBold 582. Ganó Nunito. Para la píldora grande, "five" medía 293 px y Montserrat ExtraBold a 148 px lo clava exacto.
  - **La franja que se tapa por inpaint tiene que tener altura par.** `band=(1115,1300)` da 185 px y libx264 corta el pipe con `BrokenPipeError` sin decir por qué. Con 1114 anda.
  - **demucs sin `--two-stems=vocals` no deja `no_vocals.wav`**, deja bass/drums/other/vocals. La cama se arma sumando las tres con `amix`, no hace falta volver a correr demucs (son 20 minutos de GPU por nada).
  - **El que lleva píldora opaca no necesita inpaint**: la píldora nueva se redibuja encima del subtítulo inglés. Solo el karaoke sin caja pide tapado.
- **2026-11-09 · Un quiz se clona a Brasil en una tarde si las fotos no tienen texto.** El quiz de [[secreto-de-la-chia]] pasó entero al portugués reusando **las 10 imágenes tal cual**: lo caro de internacionalizar un quiz no es el copy, son las imágenes con texto quemado. **Se mira eso primero** (hoja de contactos con Pillow) antes de estimar el trabajo. Lo único que no se deduce y hay que preguntar: **el checkout y el precio local** ([[quizzes-reglas-de-armado]]).
- **2026-11-07 · Los insumos durables van a `_assets`, no al scratchpad.** Los stems de demucs vivían en un scratchpad de sesión y sobrevivieron de milagro cuatro días. Al cerrar la tanda portuguesa se movieron a `~/Desktop/<oferta>/anuncios/_assets/stems/htdemucs/`, junto a las fuentes, y el script los busca ahí.

### Cuando el video es del competidor, no nuestro (2026-11-05, [[habilidades-perdidas]])

Pedido de Santiago: *"agarrá 6 de esos anuncios y únicamente blurreá sus subtítulos y metele el idioma en español neutro… las visuales no quiero que cambies nada"*. Mismo motor (`OUTPUTS/scripts-vsl/render_hp.py`), pero el material es ajeno y aparecen seis problemas que con los videos propios no existen:

- **Elegir por md5, no por ID de la biblioteca.** Los 22 anuncios mejor rankeados de una cuenta con 722 activos eran **8 archivos distintos**. Lo que parece "tanda nueva cada 3 días" es el mismo video resubido. Se baja la muestra, se hashea y se agrupa; recién ahí se sabe cuál es el control.
- **Descartar los que tienen cara hablando.** El labial no sincroniza con la voz nueva. Se revisa con hoja de contactos; en esta cuenta los tres creativos de más peso cerraban con presentador y quedaron afuera.
- **La banda de subtítulos se mide por máximo histórico, no por promedio.** El competidor usa dos líneas en unos pocos planos; un perfil promediado las pierde y la segunda línea queda sin borrar.
- **El inpaint solo no alcanza: va un blur gaussiano difuminado encima de la máscara.** Sin eso el resto del texto inglés sigue siendo legible.
- **Las cajas sólidas no se borran, se tapan.** Una barra negra con texto blanco inpaintada deja un fantasma perfectamente legible. Va una caja opaca nueva con el texto traducido.
- **El rectángulo de un sticker medido por umbral se queda corto** (deja afuera la foto de perfil del comentario, el escalón de la segunda línea del globo). La caja nueva se dibuja sobre la **unión** del rectángulo original y el texto nuevo.
- ⚠️ **Es material filmado por otro:** hay riesgo de reclamo de copyright y de que Meta lo marque como contenido duplicado. Es una decisión de negocio, no un detalle técnico.

## Fuentes
- OUTPUTS/2026-11-07-guiones-piedras-portugues-BR1-BR4.md
- OUTPUTS/2026-11-03-guiones-piedras-polaco-PL1-PL4.md
- OUTPUTS/2026-11-02-guiones-piedras-ruso-RU1-RU4.md
- RAW/2026-10-10-wiki-previa/internacionalizacion.md (página de la wiki previa, actualizada el 2026-08-10)
- Fuentes originales citadas (todavía no están en este cerebro): RAW/contexto-chatgpt.md, RAW/formacion/lecciones/multiidioma.md, RAW/formacion/lecciones/escalar-en-otras-cuentas-publicitarias-testear-varias-cuentas-publicitarias-para-relojear-el-cpm.md, RAW/youtube/_indice.md
