# Quizzes: reglas de armado (checklist viva)

### 🆕 2026-11-14 · Dos cosas que rompen una barra comparativa (y no tiran ningún error)
En la pantalla de revelación de [[gluteo-despierto]] —cuatro ejercicios ordenados por cuánto activan el glúteo— las barras
salieron primero invisibles y después mentirosas. Las dos fallas son silenciosas: no hay error de consola, el HTML es
válido y el desborde da 0.

1. **Un `<span>` con `height` no se ve: hay que darle `display:block`.** La barra era
   `<span class="track"><i style="width:95%"></i></span>` dentro de un `<span class="nm">`. Como el span es inline, el
   `height:7px` del CSS no aplica y la barra simplemente no existe en pantalla. Quedaban solo las etiquetas, y la
   comparación —que es el mecanismo demostrado— se perdía entera.
2. **Si la chapita de al lado cambia de ancho, las barras dejan de ser comparables.** Con el track en `flex:1`, la fila
   de *"MUY ALTA"* tiene menos espacio que la de *"ALTA"*, así que **el 95 % medía 155 px y el 74 % medía 145 px**: dos
   barras casi iguales para dos valores muy distintos. Se arregla fijando el ancho de la chapita
   (`width:88px;text-align:center;white-space:nowrap`). Después: 156 / 121 / 75 / 36 px, y la diferencia se lee de una.

**Cómo se chequea:** no alcanza con mirar la captura (las etiquetas distraen y parece que está bien). Se miden los
anchos renderizados y se comparan con los porcentajes del dato:
`[...d.querySelectorAll('.rev .track i')].map(e=>Math.round(e.getBoundingClientRect().width))`.
Si los píxeles no guardan la misma proporción que los números, el gráfico está mintiendo.

### 🆕 2026-11-14 · 🐞 El motor del competidor TIRA EL HOST del checkout
Al poner el checkout definitivo en [[gluteo-despierto]] apareció un bug del motor que clonamos. Su `completar()` termina así:

```js
a.setAttribute("href", u.pathname + u.search);   // ← se come el host
```

Con un checkout **relativo** (`/checkout`) no se nota: `u.pathname` ya es lo que hace falta. Con uno **absoluto**
(`https://tu-tienda.impultienda.ar/checkout`), al tocar el botón el href se reescribe como `/checkout` **del dominio
donde está el quiz** — y si el quiz vive en otra tienda, todos los CTAs mandan el tráfico pagado a una página que no
existe. **Es un bug dormido: aparece recién el día que se pone la URL real.**

Se reemplaza el bloque entero por uno que guarda la URL completa (`u.href`) y, de paso, arregla otras tres cosas de su
versión:
- **Los `href` nacen puestos desde que carga la página**, no recién en el `pointerdown`. El suyo solo completaba al
  tocar: si el JS fallaba antes, o alguien copiaba el link con el botón derecho, se llevaba el relativo.
- **El selector cubre también lo que no es `<a>`** (`a[href^="/checkout"], [data-cta]`), que es como entra la caja de
  precio.
- **Es idempotente** (`data-ligado`): llamarlo dos veces no suma dos listeners ni dispara dos `AddToCart` por clic.

⚠️ **Y la caja de precio lleva al checkout.** En el quiz del competidor `.precio` es una caja verde con borde y esquinas
redondeadas que **parece un botón** y no lleva a ningún lado. Es exactamente el caso de la corrección del 4/11 en
[[academia-del-trazo]] (*"Esos botones también tienen que redirigir, TODOS LOS BOTONES"*): se le pone `data-cta` y el JS
le da `cursor:pointer` y el clic. En este quiz pasó de **9 CTAs a 10**.

**Cómo se verifica (no leyendo el código):** se construye una vez con un checkout **absoluto de prueba**, se abre el
último paso con `?utm_source=...&utm_campaign=...&fbclid=...`, se dispara `pointerdown` en todos los `<a>` y se chequea
que **todos** sigan empezando por el host completo y arrastren los parámetros. 🐞 Ojo al comparar: `new URL()`
**normaliza el host a minúsculas**, así que un `indexOf()` contra la URL tal cual se escribió da falso negativo.

🐞 **Y antes de cada recorrido, limpiar el `localStorage`.** Este motor recuerda el paso un día (`pc_paso`): después de
probar la oferta, la siguiente carga arranca **directo en el paso 29** y el recorrido "ve" un solo paso. Parece que el
quiz está roto y lo único que pasa es que retomó donde quedó.

### 🆕 2026-11-14 · "El mismo diseño que ellos, pero que diga cosas distintas"
Santiago, sobre [[gluteo-despierto]]: *"que sea similar al de ellos, pero un poco distinto, porque va a ir en el mismo
mercado, de última le podemos cambiar el nombre al método, o mostrarlo de otra manera"*. Lo interpreté como **copiá la
estructura y hacé el resto nuestro**: cloné nuestro motor (Fraunces + Inter, paleta propia, mecánica nueva, 22 pasos).
Lo rebotó: ***"No, no entendiste, quiero el mismo diseño que ellos, pero que diga cosas distintas"***.

**La regla: "similar al de ellos" significa SU HTML, no nuestra plantilla.** Cuando pasa el quiz de un competidor
escalado, el entregable se construye **sobre su documento**: su `<style>` sin tocar una regla, su sprite de íconos, su
markup y su motor. Lo único que cambia son **las palabras, las imágenes con su marca y el bloque de configuración**.
Esto vale **también cuando corremos en su mismo mercado**: ahí lo que nos diferencia es el **copy y el mecanismo**, no
la estética. Nuestro motor (el de DanceGo → SumaAI, regla del 12/11) es para cuando **no hay** un quiz del competidor
que clonar.

**En la duda, la respuesta es su HTML.** Es más rápido, es lo validado, y cambiar el diseño es la decisión cara: si
Santiago quisiera otro diseño, lo diría.

**Cómo se hace sin romper nada: con un script de reemplazos, nunca a mano.**
(`OUTPUTS/scripts-quiz/build_gluteo_despierto.py` es el molde.)
1. `curl -sL` a la tienda y **cortar el documento del `custom_html`** entre su `<!DOCTYPE>` y su `</html>` — ojo, el
   HTML de la tienda tiene **dos** `<html>` y **dos** `<body>`: el segundo par es el del quiz.
2. **Partir por `<section class="paso"`** y aplicar los reemplazos **paso por paso**, no sobre el archivo entero. Hay
   textos repetidos entre pasos (*"A veces me siento incómoda"*, *"Sí, algunas veces"*, *"Casi nunca me pasa"*) y un
   `replace` global pisa el del paso equivocado. Ojo con el conteo: el `class="paso angosto"` de la portada y el de la
   oferta **no matchean** `<section class="paso"` con comilla.
3. **Cada par tiene que aparecer, y el script falla si no.** Son ~120 textos: sin esa verificación, uno que no matcheó
   queda en el idioma del competidor y no lo ve nadie hasta que está corriendo con plata.
4. **Al final, barrer rastros**: el nombre de su marca, su método, los nombres de sus testimonios, el dominio de su CDN
   y los números que cambiaron (si su promesa eran *20 minutos*, que no quede ni un "20 minutos").
5. 🐞 **Los precios del markup llevan espacio no separable**: `AR$\xa019.990`, no `AR$ 19.990`. Un par escrito con
   espacio común no matchea nunca. Si un reemplazo "que está ahí" falla, imprimir el fragmento con `repr()`.

**Lo que sí se agrega** (son nuestras reglas y no rompen su diseño): el bloque de configuración arriba del script
(`CHECKOUT` relativo, `PIXEL_ID`, `VSL_MP4`), el pixel de Meta con `AddToCart` en los CTAs, la línea de cuotas de
Mercado Pago y la FAQ de *"¿es una suscripción?"*, que es la objeción madre del low ticket.

⚠️ **La línea de cuotas va DEBAJO de la caja de precio, no adentro.** Metida en el `<span>` que dice "en un solo pago"
parte el precio en cinco renglones y desbalancea la caja entera. Va como un `<p>` aparte, con **una sola regla de CSS
nueva** que reusa el color que esa caja ya tiene.

**Las imágenes: se reusan las suyas que no llevan marca ni texto** (fotos de antes/después, avatares, sellos) y se
rehacen **solo** las que la llevan — normalmente el logo y la portada. La portada se rearma con **el mismo layout de la
de ellos** (bandas, díptico, pie) y nuestro texto, con Pillow. Si corremos en su mismo mercado y Santiago quiere fotos
100 % propias, se dice y se generan: es una decisión suya, no una que se toma sola.

### 🆕 2026-11-12 · Un quiz no se escribe de cero: se clona el motor del último que funcionó
Santiago, sobre la primera versión del quiz de [[sumaai]]: *"Muy malo el quiz, super simple, el logo esta corrido a un costado, no usaste imagenes buenas. Es el peor quiz que vi en mi vida, mira los quiz que hicimos siempre y aprender de una vez como hacer quiz"*. Tenía razón: estaba escrito desde cero, sin fotos y con emojis como imagen principal. Lo que faltó fue **abrir un quiz nuestro antes de escribir una línea**.

**La regla: antes de armar cualquier quiz, se abre el último entregado (hoy `OUTPUTS/2026-11-04-quiz-dancego.html`) y se clona su motor.** No se reinventa el render, ni el CSS, ni el manejo de pasos. Lo único que cambia es la paleta, los pasos y los textos.

**La anatomía que tienen todos los quizzes que funcionan** (y que un quiz "simple" no tiene):
- **Tipografías de Google: `Fraunces` (serif display) para títulos, números grandes y precios + `Inter` para el resto.** Con la fuente del sistema se ve como un formulario, no como un producto.
- **Cabecera: el logo va CENTRADO** (`.brand` con `justify-content:center`), con la marca partida en dos colores (`Suma<i>AI</i>`) y un ícono de 26 px al lado. **La flecha de volver va `position:absolute` a la izquierda**, nunca en el flujo: si se la mete en el mismo flex que la marca, el logo queda corrido a un costado.
- **Barra de progreso** debajo del logo, de borde a borde.
- **Portada con fotos a sangre** (`.pick.ov`, 3:4, etiqueta sobre banda oscura) + `cover-badge` + `h1` de 2,05rem. La primera pregunta es la portada.
- **Palabras destacadas en el acento**: `.q em` dentro de cada pregunta. Un título sin una palabra resaltada se lee plano.
- **Componentes con foto**: `.pick` (grilla 2×2), `.rowpick` (foto 94×118 en fila) y `.media` (foto ancha de puente).
- **Sliders con número gigante en serif + chapita de rango** (`.sl-tag`), nunca un `<input type=number>`.
- **Pantalla de carga con anillo girando y lista que se va tildando**, y **pantalla de resultado** con KPIs, barra de IMC y gráfico SVG de previsión.
- **Oferta en HTML estático** dentro de `#oferta` (barra de urgencia, antes/después, lista de incluye, caja `.promo` de lanzamiento, testimonios, garantía en SVG, FAQ), con `ligarCTAs()` idempotente.
- **Botones**: `.btn` con `text-align:center`, sombra de color y `.foot` pegajoso abajo.

**Y las imágenes son la mitad del trabajo, no el final.** Antes de escribir el HTML:
1. **Mirar el banco propio.** Las imágenes de los quizzes viejos están **embebidas en base64 dentro de los `.html` de `OUTPUTS/`**: se extraen con un `re.findall(r'data:image/(\w+);base64,([A-Za-z0-9+/=]{3000,})')` y se arma una hoja de contactos con Pillow. De ahí salieron las 11 fotos de SumaAI (género de Mounjaro Humilde, comidas de Pan Sin Picos) **sin gastar un crédito**.
2. Recién si falta un set entero, se busca en los competidores (Biblioteca → dominio → landing) y, último recurso, se genera con IA.
3. **Pillow no corre con `python3 -I`**: el modo aislado ignora el `site-packages` del usuario, que es donde está instalado (`pip install --user`). Para estos scripts se corre `python3` normal desde una carpeta propia.

### 🆕 2026-11-12 · Si el objetivo diario tiene piso, el déficit se recalcula (si no, la fecha miente)
- En el quiz de [[sumaai]] el objetivo diario se calcula con Mifflin-St Jeor y un déficit por ritmo (300 / 500 / 750 kcal), con **piso de seguridad de 1.200 calorías**. Caso real: mujer de 162 cm, 95 kg, 45+, sedentaria y ritmo ambicioso → TDEE 1.862, el déficit de 750 daría 1.112, así que el piso lo sube a 1.200.
- **El bug:** la pantalla mostraba 1.200 calorías pero seguía calculando la fecha con los 750 kcal de déficit. **El déficit real es `TDEE − objetivo` (662), no el que eligió la persona.** Con el número viejo prometía 36 semanas; con el real son 45. La aritmética del resultado tiene que cerrar con el número que la persona está viendo.
- Cuando pega el piso, se lo dice: *"Tu plan no baja de 1.200 calorías… estiramos la fecha en vez de recortar la comida."* Es un aviso de confianza, no una letra chica.
- **La pantalla de carga no lleva flecha de volver.** Es la forma más barata de que no vuelva a pasar el bug del 10/11 (el `setInterval` escribiendo contra un DOM que ya no existe). Además, el intervalo se apaga solo si no encuentra su elemento.
- **El contador de pasos solo cuenta las preguntas** (`opt/multi/placa/slider`), no la carga, el resultado ni la oferta: "Paso 9 de 16". Si se cuenta todo, el denominador miente.

### 🆕 2026-11-11 · Clonar al argentino un quiz propio del mercado inglés (Cápsulas Encantadas)
- **El `.txt` sale incompleto si el CONFIG usa comillas simples.** `inline_quiz.py` busca rutas **entre comillas dobles** (`r'"((?:\.\./|\./)?[^"\s]+\.(?:webp|png|jpe?g|svg))"'`). Con `1: '../imagenes/01-hero.webp'` embebió **4 de 25 imágenes** y el archivo quedó en 525 KB: parece liviano y en realidad está roto. Se mira siempre la cuenta que imprime el script contra la cantidad de fotos reales.
- **Una foto que aparece dos veces en el HTML se embebe dos veces en base64.** Las tres fotos de los chats estaban como `src="../imagenes/…"` además de en `CONFIG.imagenes`: 2.428 KB. Pasándolas a `data-img` (el motor les pone el `src` desde el CONFIG) el mismo quiz quedó en **1.403 KB**. Regla: en un quiz, **ninguna imagen se escribe en el markup**, todas salen del CONFIG.
- **Localizar los números, no traducirlos: la aritmética tiene que cerrar.** unidad × cantidad = pedido, y pedidos por semana × pedido = promesa mensual. En Cápsulas Encantadas: $2.500 × 40 = $100.000, × 10 pedidos al mes = $1.000.000. Y **las reseñas también llevan números**: la que dice "vendo cajas de 12 a $30.000" tiene que dar los mismos $2.500 por unidad.
- **El motor multi-moneda del quiz inglés se saca entero.** Detección por zona horaria, tasas del día y `precioUSD` se reemplazan por `precio`, `precioAntes`, `cantCuotas` y `cuota` fijos en pesos, más la línea de cuotas de Mercado Pago arriba del botón.
- **Texto quemado en otro idioma, sin gastar un crédito** (cuatro recursos, en este orden): 1) **buscar otra foto del set que no tenga texto** (el hero salió de la foto de la cocina y la del cierre de un recorte lateral de la que tenía el logo); 2) **HTML** para capturas de chat y chapitas de beneficio; 3) **Pillow** para repintar una chapa y re-tipear un nombre; 4) **Pillow con borrado por interpolación** para un mockup: se rellena cada caja de texto mezclando la interpolación horizontal (columnas de los costados) con la vertical (filas de arriba y abajo), un desenfoque suave arriba y se re-tipea con **Playfair Display** (misma familia serif que usan estos mockups) y **Great Vibes** para el script. Las dos tipografías se bajan de `github.com/google/fonts`.
- **Playfair en Pillow sale con números de estilo antiguo** (el "10" se lee "1o") y `features=['lnum']` **no funciona sin libraqm**. Si el título lleva un número, o se cambia el texto ("Tus Primeros Pedidos" en vez de "Primeros 10 Pedidos") o se busca otra fuente.
- **Las dos líneas de un título van con el mismo cuerpo**: se calcula el que entra para la línea más larga y se usa para las dos. Si se ajusta cada línea por separado, una sale más grande que la otra y se nota de inmediato.
- **Los avatares de las reseñas se guardan chicos.** Se ven a 48 px: 1.100 px de ancho eran 200 KB cada uno. Recortados al cuadrado y a 300 px quedan en 15 KB y el `.txt` baja 900 KB.
- **Cuando el checkout todavía no está, el link va relativo (`/checkout`), no muerto.** En ImpulTienda resuelve al checkout de la tienda donde se pegue el HTML, así que el quiz funciona desde el minuto cero y después se cambia una línea del CONFIG.

### 🆕 2026-11-10 · El caminador del quiz tiene que respetar el `disabled` (si no, se cuelga para siempre)
- Para reverificar el quiz de [[secreto-de-la-chia]] tras cambiarle el precio, el recorrido por código se colgó **dos veces**: 82 clics en `😊Papada` y después 82 clics en `Continuar`, sin avanzar un paso.
- **La regla del caminador, en este orden:** 1) llenar el `input` de texto si está vacío; 2) si hay un `[data-next]` **y no tiene `disabled`**, clickearlo; 3) si no, clickear la primera `.opt`; 4) si no hay nada, esperar (es una pantalla de carga de 8,5 s). Filtrar siempre `[data-back]`, `[data-faq]` y el `‹`.
- El error estaba en no mirar el `disabled`: en los pasos de **selección múltiple** el `Continuar` nace apagado hasta que se elige una opción, y en los de **opción única** la opción avanza sola. Clickear "lo primero visible" se come la opción y nunca toca el `Continuar`; clickear "el `data-next`" lo aprieta apagado al infinito.
- **El bucle largo va lanzado en segundo plano, no esperado dentro de la llamada.** Un `javascript_tool` que espera 70 s muere con `Detached while handling command`: hay que dejar el `async` corriendo contra `window.__st` (con `{done, log, errs}`), esperar afuera con un `sleep` y leer el estado en una segunda llamada.
- Y el motor **no deja globals**: todo está en una IIFE, así que no se puede saltar al último paso con `page=28;render()`. Hay que caminarlo (27 clics, ~40 s por los dos loaders).

### 🆕 2026-11-10 · "El mismo quiz pero en español": primero mirar si el original ya es ese
- Santiago pidió *"exactamente el mismo quiz pero en español argentino"* del clon brasileño de [[secreto-de-la-chia]]. **El argentino era el original** y ya estaba en voseo: lo que faltaba no era traducir, era **empaquetarlo** (el `.txt` autocontenido, el `PRUEBA.html` y la carpeta de imágenes). Antes de reescribir nada, se baja el que corre y se diffea contra el clon: si las diferencias son solo idioma, marca, precio y checkout, el trabajo es de empaquetado.
- **Un "ya está en voseo" se comprueba contando formas, no leyendo.** Ojo con los falsos positivos: `eres` cae dentro de *mujeres* y los `puedes` del HTML en vivo salían del **tema de Shopify** (mensajes del carrito), no del quiz. Se mira el contexto de cada uno antes de dar el dato.
- **Recorrer el quiz dos veces en el mismo iframe ensucia la medición** (la primera pasada deja el estado a mitad de camino), así que antes de cada verificación se recarga con `?x=Date.now()` y se engancha `onerror` recién después del `load`. **Pero un error repetido no se descarta por eso**: hay que ir a buscar el stack. En el quiz de la chía el `Cannot read properties of null (reading 'style')` era **real** (ver abajo), y la primera lectura fue que lo inventaba el recorrido.
- 🐞 **Un `setInterval` que escribe en el DOM se tiene que limpiar también cuando el paso se va, no solo cuando termina.** En las pantallas de carga del quiz de la chía (`analisis_carga` y `armando_rutina`) el intervalo que mueve la barra (`document.getElementById("rp").style.width`) se limpia **únicamente** dentro del `setTimeout` final. Como esos pasos **llevan la flechita de volver** (`bar = page>1 && page<28`), si la persona toca `‹` antes de que terminen: el intervalo tira un error cada 100 ms contra un elemento que ya no existe (**82 errores medidos**), y peor, el `setTimeout` sigue vivo y a los 8,5 s llama a `next()`, **arrastrando a la persona a la oferta aunque había vuelto atrás**. Al revisar un quiz hay que probar **el botón de volver dentro de cada pantalla de carga**, no solo el camino hacia adelante.
- Cuando el checkout todavía no está ("después te lo paso"), **se entrega con el que corre**, nunca con un placeholder: un `href` muerto en la slide de la oferta se come tráfico pagado. Queda anotado en rojo en la página de la oferta.

### 🆕 2026-11-09 · El .txt pesado se arregla por parámetro, y el clon deja nombres propios ajenos
- **`inline_quiz.py` ahora lee `ANCHO_MAX` y `CALIDAD` del entorno** (defaults 1000 y 86). El quiz de [[origen-pilates]] con los valores de siempre daba un .txt de **3,2 MB** — 29 imágenes de 1024 a 1254 px. Con `ANCHO_MAX=700 CALIDAD=74` quedó en **1,24 MB** sin diferencia visible en el teléfono: las fotos de paso se ven a ~340 px y las del carrusel a ~300 px. **Regla: si el .txt pasa de ~1,5 MB, se baja por env antes de tocar las imágenes de origen.**
- **Un quiz clonado trae los nombres propios del mercado de origen.** Las cuatro reseñas de Origen Pilates venían con **nombres italianos** (Francesca Rossi, Laura Bianchi, Martina Conti, Silvia Romano) heredados de la plantilla. Eso **no salta leyendo el HTML**: salta recorriendo el quiz. Al clonar, además del idioma hay que revisar nombres de personas, ciudades y monedas, y ponerlos con **nombre + ciudad del mercado destino** (Marcela F. de Rosario, Verónica S. de La Plata).
- **Los sliders arrancan en el valor del avatar, no en el de la plantilla.** Venían en 180 cm y 70 kg (hombre promedio) para una oferta de mujeres +40: van en **160 cm, 72 kg actual y 65 kg objetivo**. Hay que cambiarlo en **dos lugares**: el `<div class="rvalue">` del HTML y el tercer número de `unidades` + el `v:` del objeto del slider.
- **Verificación de los 19 pasos por código, en un iframe de 390 px servido por `python3 -m http.server`** (no `file://`: Chrome no deja leer el `contentDocument` entre orígenes opacos). El recorrido clickea la primera opción de cada paso y mide por paso: imágenes con `naturalWidth===0`, elementos de más de 392 px y el `scrollWidth` del documento. El paso de carga no tiene botón y pasa solo: es lo esperado, no un bloqueo.

### 🆕 2026-11-09 · Clonar un quiz al portugués: el artículo de la marca se duplica
- Cuando la marca **ya empieza con artículo** (*O Segredo da Chia*, *A Receita...*), cada texto que la llama después de una preposición sale con el artículo repetido: *"veja como funciona **o O** Segredo da Chia"*, *"Benefícios **do O** Segredo"*, *"rotina **do O** Segredo"*. En castellano el mismo molde no se nota (*"cómo funciona El Secreto de la Chía"*), así que no salta leyendo: salta **recorriendo el quiz**.
- **La solución es una variable, no parchear texto por texto:** `var Bs=B.replace(/^(O|A|Os|As)\s+/i,"")`. `B` se usa cuando la marca va sola o como sujeto (`Conheça O Segredo da Chia`), `Bs` cuando va detrás de artículo o preposición (`funciona o Segredo da Chia`, `do Segredo da Chia`). Si mañana cambia el nombre en el CONFIG, sigue funcionando.
- **Se detecta por código** al recorrer el quiz en el iframe de 390 px: `body.innerText.match(/\b(o|a|do|da|no|na) (O|A) [A-ZÁÉÍÓÚ]/g)` tiene que devolver vacío.
- **Localizar pt-BR, no traducir:** *panza* → **barriga**, *cola* → **bumbum**, *muslos* → **coxas**, *talle grande* → **plus size**, *plata* → **dinheiro**, *súper* → **mercado**, *bajar de peso* → **emagrecer**, *te devolvemos cada peso* → **devolvemos cada centavo**, y la fecha de la oferta con `toLocaleDateString("pt-BR")`. Las **claves internas del estado** (`"hoy"`, `I.cuerpo`, los nombres de Clarity) **no se tocan**: no se ven y mantienen comparables los embudos entre mercados.

### 🆕 2026-11-04 · El embed de Panda va completo, y cómo se prueba el disparo de la oferta
- **Se pega el `<div>` envolvente además del `<iframe>`.** El div trae `padding-top:177.77%`, que es lo que sostiene el 9:16; sin él el player colapsa. El CSS del quiz ya lo espera (`.vsl-frame>div{width:100%}`), aunque el comentario del template diga "pegá solo el iframe".
- **El quiz ya escucha a Panda de dos maneras**: el `postMessage` con `panda_timeupdate` y, como respaldo, un sondeo de `window.smartplayer.instances[0]`. Además hay un `setTimeout` por tiempo de página, por si el player no reporta nunca.
- ⚠️ **Para probar el disparo NO sirve `?oferta=1`:** ese atajo ya llama a `showOffer()`, y `showOffer` tiene un guard `if(offerShown) return`. Cualquier prueba posterior da falso negativo y parece que el código está roto.
  - **Lo que sí funciona:** copiar el HTML al scratchpad, sacarle el `showOffer()` del atajo para llegar al final con la oferta oculta, servirlo, y disparar `window.postMessage({message:'panda_timeupdate', currentTime: N})` con un valor por debajo y otro por encima del umbral. Tiene que quedar oculta en el primero y aparecer en el segundo.

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
- **ImpulTienda con HTML propio (`custom_html`, 2026-10-24):** el quiz entero viaja en texto plano en el HTML de la tienda. Se baja con `curl -sL <url de la tienda>` y el bloque que pegó Santiago queda entre el `<body>` y los scripts de la tienda: markup, un `<style>` y un `<script>`. Se corta con `sed -n` y se edita directo. Las imágenes están en `i.postimg.cc` y en el `storage` de Supabase de la tienda, y se reusan tal cual. Ojo con el `<title>` y el `<meta description>`: quedan los de la tienda que clonó, así que no sirven para identificar la oferta.
- **HTML propio del competidor (2026-10-26, `calisteniafeminina.site`):** cada vez más quizzes escalados no usan plataforma: son **una sola página HTML en texto plano**. Se baja entera con `curl -sL` y adentro está todo — el array `STEPS` con preguntas, opciones y feedback, la sales page y los links de checkout. El flujo suele ser portada = 1ª pregunta → pasos → pantalla de análisis → **`vsl.html`** (VSL solo, sin oferta) → `/sales-page`. Ojo con el stack que traen: cloaker por geolocalización, TrackTurbo (pixel + UTMs) y player de VSLwave; **nada de eso se copia**. Las imágenes cuelgan de `/images/` y se bajan una por una.
- **InLead exportado dentro de ImpulTienda (2026-10-26, `calisteniaasiaticahombres.impultienda.ar`):** la tienda usa `custom_html`, pero adentro va un funnel de InLead **exportado en texto plano** como `window.FUNNEL` (JSON con `steps`, `design` y `navigation`). **No está cifrado**: se baja con `curl -sL`, se corta la línea del `window.FUNNEL` y se parsea con Python. Cada paso trae `layers` con `text`, `options` (con `value`, `label` y `image`), `height`/`weight`, `loading`, `charts`, `faq`, `bonuses` y `offer`. Las imágenes cuelgan del `storage` de Supabase de la tienda y se bajan numeradas (`…_landing-NN.webp`). Con eso alcanza: no hace falta recorrer el quiz en el navegador.
- **Lovable (`*.lovable.app`, 2026-10-15):** el quiz entero está en texto plano en el bundle `assets/routes-*.js` (preguntas, opciones, oferta, FAQ, popup de salida y testimonios). Se baja con `curl` y los colores salen de `:root` en `assets/styles-*.css` (vienen en `oklch`, se pueden usar tal cual). Las imágenes están en `/__l5e/assets-v1/…` y `/assets/…`. No hace falta abrir el navegador.
- **Lovable que sirve las imágenes desde `media.inlead.cloud` = quiz exportado de InLead (2026-11-04, [[monjaro-violeta]]).** El funnel sigue viniendo en texto plano en `assets/routes-*.js`, pero las imágenes son las de InLead y **el nombre del archivo trae el tamaño**: `…-xs-…`, `…-sm-…`, `…-md-…`. Las `xs` son de **96×80 px** y **no existe una versión más grande** (probado `sm`, `md`, `lg`, `xl`, `2x`: todos 404). Conviene chequearlo **antes** de planificar: si las siluetas de una pregunta son `xs`, esa pregunta va con íconos o hay que generarlas.
- **Lovable con backend propio (Supabase) = el contenido NO está en el bundle (2026-11-04, [[dancego]]).** Si en `assets/index-*.js` aparecen `from("funnel_steps")`, `from("funnel_elements")` y un panel de administración, el quiz se sirve desde la base y no viaja en texto plano. Se recorre en Chrome paso a paso leyendo `img.src` y `img.alt` con `javascript_tool` (clickear los botones por su texto es mucho más rápido que por coordenadas). **Las imágenes sí están todas en el bundle**: se saca la lista de `/lovable-uploads/<uuid>.png`, se bajan de una y se miran juntas en una **hoja de contactos** armada con Pillow. Eso evita abrir 81 archivos.
- **Ojo con lo que devuelve `javascript_tool`:** si el resultado incluye una URL con `?fbclid=…` o un pixel con query string, la llamada se bloquea entera. Devolver solo el nombre del archivo (`src.split('?')[0].split('/').pop()`).
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
- **CTA temprano en el hero, que NO va al checkout (2026-11-03, "sino queda re abajo el botón para comprar").** Debajo de los chips del hero va un botón que **ancla a la sección de "qué vas a recibir"** (`href="#incluye"`), no al checkout: el que recién llega ve toda la oferta antes de decidir. No lleva la clase `js-cta` (si la lleva, el JS le pisa el `href` con el link de pago y además dispara `AddToCart`), y la sección destino necesita `scroll-margin-top` porque la barra de urgencia es sticky.
- **La caja de oferta se presenta completa, estilo "launch promotion" (2026-11-03, "quedó re peruano, necesito que sea más completo, con toda la información de lo que se lleva, el producto, los bonos").** Una caja de precio con solo tachado + precio + botón se ve barata. El layout que pidió Santiago (referencia: `scentedstone.lovable.app`, bloque *Launch Promotion*), de arriba abajo:
  1. chapita ocre **★ PRECIO DE LANZAMIENTO ★** montada sobre el borde de la tarjeta
  2. **nombre del producto** grande en la serif display + bajada del mecanismo en mayúsculas chicas
  3. **precio tachado**, chapita verde con el **ahorro en pesos**, **precio de hoy** gigante y la línea de cuotas
  4. caja crema **"Todo lo que te llevás"**: un ✓ por ítem del producto (sin precio al lado), y el **acceso de por vida destacado aparte** en una tarjeta blanca
  5. caja de **borde punteado con 🎁**: "+ N regalos incluidos, sin costo", el valor tachado y una chapita verde **HOY: GRATIS**
  6. botón ancho, y abajo la micro-confianza (pago seguro · acceso por mail en 2 minutos)
  Los precios salen de los `data-` del CONFIG (`data-old`, `data-new`, `data-ahorro`, `data-valorbonus`, `data-cuotas`), nunca hardcodeados. Ojo con heredar `display:block` en los `<b>` de adentro: parte el "Valor $45.600" en tres líneas.
- **Los atributos `width`/`height` del `<img>` llevan las dimensiones REALES del archivo (2026-11-03, "la foto queda cortada y no se ve lo del costado").** En la landing de [[academia-del-trazo]] el mockup estaba declarado `width="460" height="460"` siendo 1122×1402: cualquier plantilla que respete esos atributos mete la foto en un box cuadrado y le come los costados (se perdía el badge "+ CURSO EN VIDEO"). Se miden con `PIL` antes de escribir el tag, y la imagen del hero se blinda para que ninguna plataforma la recorte:
  ```css
  .hero-img{width:100%;max-width:520px;height:auto!important;aspect-ratio:auto!important;object-fit:contain!important}
  ```
  Verificado inyectando CSS hostil (`img{height:520px;aspect-ratio:1/1;object-fit:cover}`): la imagen sigue entera. Se chequea midiendo en el navegador que `ratio renderizado == ratio natural` a 300, 350, 520 y 720 px de contenedor.
- **Portada con el texto quemado en otro idioma: se recorta y el lockup se rehace en HTML (2026-11-04, [[monjaro-violeta]]).** En vez de regenerar la tapa con IA (créditos, y la IA escribe mal el castellano), se recorta **solo el arte** (la foto, el producto, el fondo), se le aplica un **alfa en diagonal** —el fundido arranca antes en las columnas donde había texto y más abajo donde está la persona— y se guarda en PNG/WebP con transparencia, así se funde con el fondo de la página. El título se rehace **en HTML con CSS** (`background-clip:text` para el degradé, `text-shadow` para el glow, un `<span>` con `skewX` para la banda del brochazo): queda nítido, se edita en un segundo y no cuesta un crédito.
- **Chapas de color plano con una palabra adentro (2026-11-04).** `MULHER` → `MUJER` se resuelve con Pillow: se detecta el verde por rango de color para sacar el bounding box, se repinta **solo el rectángulo interior** (sin tocar los bordes, así las esquinas redondeadas se conservan solas) y se re-tipea centrado con **Arial Black**. Si la palabra nueva es más larga, se baja el cuerpo de la fuente en vez de achicar la chapa.
- **"No quiero que se vea recontra colorido" (2026-11-04, [[dancego]]): lo feo casi nunca son las fotos, es lo que les ponen encima.** En DanceGo las fotos del original eran buenas (estudio, fondo gris, ropa deportiva neutra, mismo encuadre) y se veían horribles porque tenían **un overlay de degradé rosa/violeta/verde/naranja**. Sacando el overlay y reusando el archivo original, el set entero queda premium sin generar una sola imagen. **Antes de rehacer nada, mirar si la foto está tapada por CSS.** La paleta pasa a: papel crema + tinta + **un** acento; el verde solo significa "bien" y el rojo solo "riesgo".
- **Carteles de IA con el texto quemado (tapas de ritmos, portadas de módulos): se rehacen tipográficos en CSS, no con IA (2026-11-04).** Color plano apagado + el nombre en la serif display + una línea chica arriba. Quedan nítidos, coherentes entre sí, se editan en un segundo y no cuestan un crédito.
- **La maqueta del celular se dibuja en HTML/CSS (2026-11-04).** Clonar la captura de la app del competidor arrastra su idioma y su paleta. Un `<div>` con marco redondeado, barra de estado, tarjeta de desafío, lista de logros y barra de pestañas se lee nítido en cualquier pantalla y los textos quedan en castellano.
- **Siluetas de tipo físico (2026-10-26, "las imágenes son muy malas"):** los recortes que traen los quizzes suelen ser **PNG/WebP con alfa y basura en los píxeles transparentes**, chicos (300–500 px) y con el modelo cortado a la altura del mentón. Sobre blanco se ven baratísimos. El arreglo: recortar al **bounding box del alfa** (umbral ~24), montarlos sobre una **tarjeta cuadrada de 600 px con un degradé gris muy suave** y dejarlos todos del mismo tamaño y con la misma línea de piso. Quedan como un set, no como recortes sueltos.
- **Recolorear una imagen reusada: siempre desde el original y en un solo pase** (2026-10-26). Se mapea **solo el matiz de origen** (el azul vive en 0,55–0,70; la piel en ~0,05) conservando saturación y luminosidad. Encadenar pases —azul → rojo → verde— arrastra el rango de matices y termina pintando caras y manos.
- **Dónde buscar fotos mejores (2026-10-26):** la vía es Biblioteca de Anuncios → el ad muestra el dominio → se baja el HTML de la landing y del `/start`. Fuentes que sirvieron para hombres 40+: **`menletics.com`** (imágenes en `funnelmedia.flmng.live/cdn-cgi/image/width=1200,.../menletics/landing/…`, selector de edad, flexiones, gimnasio) y **`musclebooster.welltech.com`** (`/_astro/…`; pedírselas al host final, `musclebooster.fitness` devuelve vacío). **Lo que NO sirve:** `quiz.calistenia.app` sirve sus siluetas a 96×96, y los funnels grandes (Menletics, GreatApps) tienen el quiz detrás de un "acepto términos" o de un token de API: no se tildan casillas de consentimiento por el usuario ni se sacan tokens.
- **La portada puede no llevar foto** (2026-10-26). Si la primera pregunta tiene opciones con imagen (el selector de edad), la foto de arriba **empuja las opciones abajo del fold** y compite con ellas. Sin foto, el orden es logo → chapita → titular → bajada → opciones, y las opciones entran enteras en la primera pantalla. Al sacarla hay que revisar los textos que la referencian ("mirá los resultados…"), que quedan huérfanos.
- **Una pregunta clara no lleva foto** (2026-10-26, "esta imagen quedó muy mal, no quiero imagen ahí"). La foto de un paso tiene que **aportar** —mostrar la opción (cuerpos, zonas de dolor) o el test que se pregunta (flexiones)—. Si es solo decorativa (un tipo mirando a cámara, alguien cabizbajo), **se saca**: el paso queda más limpio con la pregunta y las opciones solas.
- **Si falta una sola foto de un set, se genera esa** (2026-10-26). Pedirla con el mismo encuadre, fondo y vestuario que las reales (ej. "fondo negro, remera verde oliva, brazos cruzados, plano de cintura para arriba") y entra sin que se note. Si faltan varias, mejor sacar las fotos de esa pregunta y dejarla con íconos.
- **Revisar marcas de agua** (pngtree, freepik, etc.) en cada imagen del original y sacarlas. En los PNG transparentes, la marca suele tener alfa bajo, así que alcanza con borrar los píxeles con alfa menor a ~110 (2026-10-14).
- **Nada de capturas pixeladas.** Testimonios escritos, garantía y bloques de texto se arman en **HTML** (tarjetas nítidas), no como imagen. Corrección del 2026-10-12.
- **Foto redonda de la experta (2026-10-15, "se ve mal"):** armar una versión de la foto **sin ningún texto** (pintar el fondo) y recortar de ahí un plano abierto (cabeza entera, hombros y algo del producto), **sin agrandar** el recorte. Si se agranda, se pixela. Nunca recortar de la original con el nombre viejo.
- **Garantía en la paleta del quiz (2026-10-15, "se ve mal"):** no copiar la estética de la imagen original (fondo negro y rojo chillón) si choca con el diseño. Usar una tarjeta con los colores del quiz, sello dorado grande arriba, título en la fuente display y texto centrado. Los textos curvos del sello tienen que quedar adentro del círculo, sin pisar bordes ni anillos.
- **Quiz propio, sin original (2026-10-18, "las imágenes me dan ganas de irme del quiz", "se ve muy low ticket"):** nunca resolver las imágenes con ilustraciones SVG ni emojis grandes. Portada, opciones con imagen, género, recetas o resultados y oferta llevan **fotos profesionales** hechas en Higgsfield (GPT Image 1.5, High, 1:1), todas con el mismo estilo (misma luz, mesa y paleta) para que se vean como un solo producto. Los emojis quedan solo como íconos chicos en las opciones de lista.
- **Higgsfield:** antes de generar, **sacar las imágenes de referencia que quedaron cargadas** de otro proyecto (miniaturas arriba del prompt). Con el plan Plus se pueden lanzar ~4 imágenes a la vez; si se lanzan más, aparece la oferta de upgrade ("Skip Special Offer" para volver).
- Logo: si cambia la marca, rehacerlo con el mismo ícono y el mismo estilo tipográfico.

## 4b. Coherencia de componentes (2026-10-14)
- **Barra del IMC:** si el resultado dice "Sobrepeso", la bolita va **cerca de Sobrepeso** (~85%), nunca en Saludable.
- **Peso y altura (y peso deseado):** van **siempre** con un **medidor** (barra), aunque el original use botones +/− (2026-10-17) (un slider con el número grande en kg o cm y una regla), no con un campo de texto. Así es más fácil completarlos.
- **Si el quiz se bifurca por género, los textos tienen que concordar (2026-11-04, [[monjaro-violeta]]).** No alcanza con duplicar las preguntas de cada rama: los textos compartidos ("¿estás list**o**?", "Quedate tranquil**o**", "List**o**, Ana") quedan en masculino para todas las mujeres. La solución: un token `{{o}}` que el motor reemplaza por `a` u `o` según el género elegido, y por `a` mientras todavía no eligieron.
- **Zonas del cuerpo:** usar nombres que se entiendan en Argentina: "Caderas" en vez de "Cartucheras". Sacar "Flancos".

## 5. Diseño y textos de la oferta (último paso)
- **Último paso = VSL arriba de todo.** Toda la oferta queda **oculta** y aparece sola a los `SEGUNDOS_OFERTA` de llegar a ese paso. **Depende del VSL**: tiene que ser después del momento en que el VSL dice el precio. Pilates Hormonal: **3:50 (230 s)**; al principio eran 2:40. El timer de urgencia y las notificaciones **arrancan recién cuando aparece la oferta**.
- **La pantalla de resumen va corta** (2026-10-26, "tiene mucha info, se hace muy larga"). Una sola tarjeta con las barras del diagnóstico y **un** aviso, 4 chips como máximo, y el gráfico de previsión con 3 logros. Todo lo que el VSL va a decir igual no va acá.
- **El color de marca no puede significar "mal"** (2026-10-26). Si la paleta es verde, las barras de riesgo (IMC, testosterona) igual van de verde a rojo y el aviso de cupos queda en rojo: el verde tiene que seguir leyéndose como "bien" en todo el quiz.
- **Espaciado generoso** entre bloques y párrafos ("está todo muy pegado"). Como referencia: un gap de unos 30 px entre bloques e interlineado de 1,6.
- **Sacar encabezados de relleno** antes de la lista de beneficios ("¡Todo lo que necesitas…", "Al ingresar, desbloqueás…"). La lista va directa.
- **Orden de la oferta (2026-10-13):** cuenta regresiva → **cuadro de cuotas de Mercado Pago → aviso del email → botón de compra** → después todo lo demás. Así la persona puede pagar apenas termina el VSL. **Sin el bloque de precio grande** (tachado + "Solo hoy por APENAS $X").
- **Sellos e íconos dibujados en SVG:** calcular los puntos (simétricos), no dibujarlos a mano, porque quedan torcidos.
- **Texto curvo de un sello: solo en el arco de arriba** (2026-10-26). Si el `textPath` recorre el círculo entero, la mitad de abajo sale **al revés**. Va un arco de media vuelta (`M x1,cy A r,r 0 0 1 x2,cy`) con `startOffset="50%"` y `text-anchor="middle"`, y lo de abajo como texto horizontal común. El radio del arco tiene que dejar aire contra el anillo, o los acentos se pisan con el borde.
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

## 7b. El VSL dentro del quiz (2026-10-25)
- **Player propio por defecto, no embed.** Un `<video>` nuestro con el MP4 servido desde nuestro hosting: arranca solo apenas la persona llega al último paso, `playsinline`, **sin controles ni barra de progreso** para que no puedan adelantar hasta la oferta.
- **"El video tiene que arrancar de una."** Como el último paso se llega siempre después de clics (el quiz), hay activación de usuario: se intenta `play()` **con sonido** y, solo si el navegador lo rechaza, se pasa a `muted` y se muestra un cartel grande a toda pantalla **"TOCA PARA ACTIVAR EL SONIDO"**. Nunca arrancar en silencio de entrada.
- **El botón se desbloquea por el tiempo VISTO del video** (`timeupdate` + `currentTime`), no por un reloj: si pausan o se les corta, el botón espera. Se deja igual un `setTimeout` de respaldo con el mismo número, por si el video no informa su tiempo (embed externo o error de carga).
- **MP4 para web**: 720x1280, CRF 25, AAC 96k, `-movflags +faststart`. 17 minutos quedan en ~146 MB. El hosting tiene que aceptar *Range requests* o el video no puede ir cargando mientras se reproduce (`python3 -m http.server` **no** las acepta: sirve para probar que arranca, no para probar el salto de tiempo).
- VTurb/Panda: `VIDEO_URL` vacío y el embed adentro del `<template id="vsl-template">`. El botón **sigue saliendo por tiempo real del video**: Panda lo informa por `panda_timeupdate` y VTurb por `window.smartplayer.instances[0].video.currentTime`; el reloj queda solo de respaldo.
- **Panda arranca en silencio.** Por más que el embed traiga `allow="autoplay"`, el player sale mudo con su propio cartel ("Pulse aquí para activar el sonido"). Eso se configura en el panel de Panda, no desde el HTML: si Santiago pide que arranque con sonido o que el cartel hable como el resto del quiz, hay que tocarlo ahí. Confirmado en Protocolo Chía 28D el 2026-10-25.

## 8. Entrega (siempre)
> Desde el 2026-10-22, todo va dentro de `~/Desktop/<oferta>/` (`landing/`, `imagenes/`, `anuncios/`), no suelto en el Escritorio ([[como-trabajar-con-santiago]]).

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


## 2026-11-04 · Dos cosas que deforman el quiz y no se ven en el escritorio

**1. El atributo `height=""` del `<img>` le gana al `aspect-ratio` del CSS.** La regla del 2026-11-03 manda poner en `width`/`height` las medidas reales del archivo. El efecto secundario: una foto de 640×853 declarada así y maquetada con `aspect-ratio:3/4` sale de **853 px de alto** igual, porque el atributo fija el alto y `aspect-ratio` solo actúa con `height:auto`. En DanceGo el antes/después ocupaba una pantalla entera. La solución es una sola línea en el reset:

```css
img{max-width:100%;height:auto;display:block}
```

y, donde importa de verdad, el blindaje completo: `height:auto!important;aspect-ratio:X!important;object-fit:cover`.

**2. Las grillas de dos columnas se desbordan a 373 px.** Una opción con ícono + texto + casilla entra bien a 540 px y se pasa 4 px en un teléfono. Se arregla apretando solo la variante en grilla (`padding:13px 11px`, ícono de 28 px, texto .88rem, flecha oculta), sin tocar la lista de una columna.

**Cómo se chequea, de una sola pasada:** se carga el quiz en un `<iframe>` de 390 px dentro de una pestaña abierta y se recorre **entero por código** (clickear `.opt/.pick/.rowpick`, el `♥` del swipe y `#next`), midiendo en cada paso `scrollWidth - clientWidth`. Devuelve la lista de pasos que se desbordan y en cuántos píxeles. Al final, verificar que todos los `.btn` tengan `text-align:center`.


## 2026-11-04 · Una foto de portada mala casi siempre es un recorte malo

Santiago, sobre las 4 fotos de edad de [[dancego]]: *"Las imagenes del principio son muy malas."* Eran retratos de estudio **buenos** (1024×1024, fondo gris parejo, misma ropa, misma luz) y se veían espantosos por el encuadre: la persona ocupaba un tercio de la tarjeta y el resto era gris vacío. A 170 px de ancho las cuatro parecían **la misma mujer**, y el rango de edad no se leía.

**El arreglo no fue cambiar la foto, fue apretar el recorte.** Zoom ~1.95 sobre el alto, centro vertical en 0.26–0.27 (la cara arriba, porque abajo va la banda), salida 720×960 en 3:4. Con la cara llenando la tarjeta se ven de una las arrugas, el pelo cano y la edad de cada una: pasan a ser cuatro personas distintas.

**Reglas:**
- Antes de salir a buscar o generar fotos nuevas, **probar el recorte apretado de las que ya hay** y mirarlas al tamaño real. Es gratis y resuelve la mayoría de los casos.
- En una tarjeta de opción, **el sujeto tiene que llenar el encuadre**. Si hay más fondo que persona, el recorte está mal.
- Cuando la opción es un **rango de edad**, lo que tiene que entrar en el recorte es la **cara**, no el cuerpo: la edad se lee ahí. Para tipo de cuerpo es al revés.
- **La etiqueta va encima de la foto**, sobre una banda oscura (`linear-gradient` de transparente a `rgba(23,22,26,.88)`), no debajo en una franja blanca: la tarjeta gana alto de imagen y se ve más llamativa. Sin la banda, el texto blanco se pierde contra el fondo claro del estudio.
- "Más llamativo" **sin volver a lo colorido** se consigue con jerarquía, no con color: chapita oscura arriba con la prueba social, titular más grande (2.05rem) y foto a sangre.

## 2026-11-04 · Antes de decir "usemos una que ya tengamos", mirar si existe

Santiago pidió reusar imágenes de otras ofertas. Se revisaron las carpetas de `~/Desktop/` (Monjaro Violeta, Tai Chi Fit, Dibujo Creativo, Drawing World) y **no había ningún set de edades de mujeres** que sirviera: las de Monjaro son parejas (hombre + mujer) recortadas sobre negro a 300 px. Conviene **mirar primero y decirlo**, en vez de prometer un reuso que no existe. Una hoja de contactos con Pillow de todas las carpetas se arma en un minuto y responde la pregunta de una.


## 2026-11-04 · "Sacalo" quiere decir el paso entero, no la imagen

Santiago había pedido *"las del tipo de musica sacalas"*. Se interpretó como "sacales las imágenes" y quedó el paso con una tarjeta tipográfica. Tuvo que repetirlo: *"Lo de los estilos de musica sacalo te dije."*

**Regla: cuando pide sacar algo de un quiz, por defecto es el paso completo.** Si de verdad lo que molesta es solo la imagen, lo dice ("sacale la foto a ese paso"). Ante la duda, preguntar antes de dejar media medida — una corrección repetida cuesta más que una pregunta.

Y al sacar un paso hay que **barrer el código que queda huérfano**: el array de datos, la rama del `render`, la función del componente, su CSS, su campo en `state` y la llamada en `bind`. Si no, el archivo se llena de muerto.

## 2026-11-04 · Un emoji repetido tres veces no es un ícono, es un borrón

Santiago: *"El emoji de las baterías se ve muy mal."* Eran las opciones de nivel de energía del original: 🔋 / 🔋🔋 / 🔋🔋🔋 / 🔋🔋🔋🔋 metidas en la chapita de 34 px. Un emoji solo funciona como ícono chico; **repetido para indicar cantidad se ve amateur** y además se desborda de la chapita.

**Regla: un emoji por opción, nunca una fila de emojis para representar una escala.** Si hace falta mostrar un nivel, va un medidor dibujado en CSS (barritas) o se saca la pregunta. También conviene revisar que no se repita el mismo emoji en dos opciones del mismo paso: queda sucio.

## Registro de correcciones
| Fecha | Quiz | Corrección | Regla |
|---|---|---|---|
| 2026-11-14 | Quiz Glúteo Despierto (modelado de Guía Piernas y Cola) | **"No, no entendiste, quiero el mismo diseño que ellos, pero que diga cosas distintas"** (después de entregar una v1 con nuestro motor) | **"Similar al de ellos" = SU HTML, no nuestra plantilla** (ver la regla del 14/11 arriba). La v2 es su documento tal cual —su CSS, su sprite, sus 30 pasos, su violeta— con **los ~120 textos reescritos por script**, que falla si un par no matchea o si queda un rastro suyo. 13 de las 15 imágenes son suyas (las neutras); logo y portada rehechos. Se suman cuotas de Mercado Pago, pixel y la FAQ de suscripción. Bugs nuevos: el `AR$\xa0` con espacio no separable, los textos repetidos entre pasos y la línea de cuotas que parte la caja de precio |
| 2026-11-12 | Quiz SumaAI (v2) | "Muy malo el quiz, super simple, el logo esta corrido a un costado, no usaste imagenes buenas. Es el peor quiz que vi en mi vida, mira los quiz que hicimos siempre y aprender de una vez como hacer quiz" | Se rehizo entero **clonando el motor de DanceGo** (ver la regla del 12/11 arriba): Fraunces + Inter, logo centrado con la flecha de volver en `absolute`, portada de género con fotos a sangre, dos pantallas de comida con fotos reales, maqueta de celular, carga con anillo, resultado con IMC y gráfico, y la oferta completa estilo lanzamiento. **11 fotos sacadas del banco propio** (base64 de los quizzes viejos de `OUTPUTS/`), cero créditos |
| 2026-11-12 | Quiz SumaAI (modelado de Welmi) | "Vamos a ir con SumaAI, quiero que me armes el quiz pero con el reebranding nuestro, sacale algunas preguntas que sean innecesarias. Y cambiale los colores, me gusta el azul" | De **35 pasos a 19**. Se van: prueba social con ratings ajenos, "¿te derivó un profesional?", nivel de nutrición, hábitos, placa de Harvard/UNICEF, objetivo de pasos, fecha del primer control, edad exacta, placas de relleno y **el email gate**. Se unifican intolerancias + dieta y caminata + escaleras + pasos. Quedan las que personalizan el resultado y las de compromiso emocional (el **mayor reto** se devuelve dos pasos después). Paleta azul `#1B4CD9` / `#0E2452` / `#F2F6FD`, con verde solo para "bien" y rojo solo para riesgo. **Un rating que no es nuestro no se clona**: ahí no aplica "fidelidad al original", aplica "no inventar datos" |
| 2026-11-11 | Quiz Cápsulas Encantadas (AR) | "Ahora quiero que hagamos este quiz pero para argentina. Lo vamos a cobrar 12.990… El link de checkout te lo paso desp" | Clon del quiz propio en inglés (*Tea Charm Studio*, 27 USD): mismos 8 pasos y mismo orden, español argentino con voseo, motor multi-moneda reemplazado por precio fijo + cuotas, nombres y ciudades argentinos, y las 5 imágenes con texto en inglés rehechas sin gastar un crédito (recorte, HTML y Pillow). Checkout relativo hasta que pase la URL. Aprendizajes nuevos: las comillas del CONFIG en `inline_quiz.py` y la foto duplicada en base64 (ver la regla del 11/11 arriba) |
| 2026-11-10 | Quiz El Secreto de la Chía (AR) | "necesito que hagamos exactamente el mismo quiz pero en español argentino" | El original **ya era** el argentino y ya estaba en voseo: el pedido se resolvió **empaquetando** (bloque del quiz bajado con `curl -sL`, `.txt` para el `custom_html`, `PRUEBA.html` con las fotos embebidas y la carpeta de imágenes). Se diffea el que corre contra el clon antes de reescribir: 139 líneas, todas de idioma, marca, precio y checkout. Checkout nuevo pendiente → se entrega con el que corre y se anota en rojo |
| 2026-11-09 | Quiz O Segredo da Chia (BR) | "Haceme exactamente este mismo quiz, pero para el mercado de Brasil… con las imágenes, con todo" | Clon 1:1 del quiz argentino al portugués: mismos 28 pasos, misma paleta y **las mismas 10 imágenes** (ninguna tenía texto quemado, se chequea con una hoja de contactos **antes** de planificar rehacer nada). Lo único que cambia: idioma, marca, precio y el `checkout` del CONFIG. Aprendizaje nuevo: el **artículo duplicado** de la marca en portugués (ver la regla del 9/11 arriba) |
| 2026-11-05 | Quiz Tai Chi Fit | "quiero que todos los botones del cta de la ultima slide redirijan a este checkout: `https://taichi-fit.impultienda.ar/checkout`" | **El subdominio de ImpulTienda no se deduce del nombre del producto.** Habíamos puesto `tai-chi-fit` (con guion) y el real es `taichi-fit`: el link daba "Tienda no encontrada" y todos los CTAs apuntaban a la nada. Antes de entregar, **el subdominio lo confirma Santiago o se verifica con `curl -sIL -o /dev/null -w "%{http_code}" <checkout>` que devuelva 200**; si no está confirmado, queda anotado en rojo en la página de la oferta. Con la URL en un solo lugar (`CONFIG.LINK_CHECKOUT`), el arreglo es una línea y se re-verifica en el navegador con `?utm_source=` |
| 2026-11-04 | Quiz DanceGo | "todos los botones de cta de la ultima slide, tienen que redirigir a este checkout" | Un solo `ligarCTAs()` con selector ancho (`#oferta a.btn, #oferta button.btn, #oferta .js-cta`), la URL siempre desde `CONFIG.LINK_CHECKOUT`, llamado **también en el arranque** para que los `href` estén puestos desde que carga, e **idempotente** (`dataset.cta`) para no sumar dos listeners y disparar dos `AddToCart` por clic. Se verifica en el navegador listando los CTAs con su `href`, y con `?utm_source=` para ver que arrastre los UTM |
| 2026-11-04 | Quiz DanceGo | "Lo de los estilos de musica sacalo te dije. El emoji de las baterias se ve muy mal. Saca algunas preguntas que esten de mas" | Se fue el paso de ritmos **entero** (y su código), más el bloque de hábitos, "nivel en el baile", la edad exacta y "tu mejor cuerpo": de 35 pasos a **26**. El emoji de pilas se fue con la pregunta de energía |
| 2026-11-04 | Quiz DanceGo | "Las imagenes del principio son muy malas, usa algunas que ya hayamos usado y que se vean mejor, hacelo mas llamativo, las del tipo de musica sacalas" | Las fotos estaban bien: el problema era el **encuadre**. Recorte apretado a la cara (zoom 1.95, 720×960), etiqueta sobre banda oscura encima de la foto, chapita de prueba social y titular más grande. Los 7 ritmos quedaron **sin imagen**: tarjeta tipográfica sola |
| 2026-11-04 | Quiz DanceGo | "Mejoramelo, no quiero que se vea recontra colorido, quiero que las imagenes se vean bien" | §4: el problema era el **overlay de degradé** sobre fotos que ya estaban bien. Paleta de papel crema + tinta + un acento; tapas de ritmos y maqueta de celular rehechas en CSS; capturas de WhatsApp e Instagram pasadas a HTML; `img{height:auto}` global y chequeo de desborde a 390 px |
| 2026-11-04 | Landing Academia del Trazo | "Esos botones también tienen que redirigir, TODOS LOS BOTONES" (captura de la chapita verde **HOY: GRATIS** de la caja de regalos) | §4: **todo lo que parece un botón lleva al checkout**, no solo los `.btn`. Una chapa de color con bordes redondeados (`.free`, pastillas de precio, sellos) se toca igual que un botón: o va dentro de un `<a class="js-cta">`, o el JS le pone `cursor:pointer` y un `click` a `/checkout` con las UTMs. Antes de entregar: listar en consola **todos** los `<a>` y `<button>` más los elementos con fondo opaco y `border-radius`, y revisar que ninguno quede muerto. El botón del hero (`VER TODO LO QUE INCLUYE`) **dejó de ser ancla** y también va al checkout |
| 2026-11-04 | Landing Academia del Trazo | "Si la página ya estaba terminada, no tenías que cambiar nada más que los botones de CTA redirijan al checkout" | **Alcance:** un arreglo puntual sobre una página ya terminada toca **solo eso**. Las imágenes del CDN del original, el `PIXEL_ID` vacío y cualquier otro pendiente anotado **se avisan en una línea y se esperan**; estar en el `changelog.md` no los autoriza. Ver [[como-trabajar-con-santiago]] |
| 2026-11-04 | Tai Chi Fit | "Que todo eso aparezca recién a los 4 minutos… y abajo del VSL ya les pongas un botón de CTA que los redirija directo a checkout, como para que no tengan que deslizar tanto" | §5: además de la oferta diferida, va un **botón de checkout pegado abajo del video** (`#cta-vsl`), que aparece con el mismo disparador que la oferta y lleva `data-cta` para heredar el link y los UTMs. Y el retraso puede ser **un tiempo redondo que pide Santiago**, no siempre el segundo exacto del precio en el VSL |
| 2026-11-04 | Tai Chi Fit | El apelativo por defecto seguía siendo **"Guerrera"** (del quiz militar original) y se veía 3 veces en el último paso | Cuando se cambia el **tema** de un quiz modelado (§2), el barrido no puede quedarse en los textos de las preguntas: hay que revisar también **el nombre por defecto** (`state.nombre||'...'`), los textos del mockup de la app y los comentarios del CSS. En Tai Chi Fit pasó a **"Aprendiz"**, que es el primer nivel del propio quiz |
| 2026-11-03 | Landing Academia del Trazo | "Quiero que pongas un botón de cta entre medio de esos textos, porque sino queda re abajo el botón para comprar… que no lleve al checkout, sino que lleve a la presentación de la oferta" | §4: botón en el hero anclado a la sección de "qué vas a recibir", sin `js-cta` |
| 2026-11-03 | Landing Academia del Trazo | "Esto quedó re peruano, necesito que sea más completo, con toda la información de lo que se lleva, el producto, los bonos" | §4: caja de oferta completa estilo *launch promotion* (chapita, nombre, precio, lista de ✓, acceso de por vida destacado, caja punteada de regalos con valor tachado, botón y micro-confianza) |
| 2026-11-03 | Landing Academia del Trazo | "Fijate que la foto queda cortada y no se ve lo del costado" | §4: `width`/`height` del `<img>` con las dimensiones reales del archivo + blindaje `height:auto!important;aspect-ratio:auto!important;object-fit:contain!important` en el mockup del hero |
| 2026-10-26 | Calistenia Rusa | "Sacá la foto del principio, la del antes y después" | §4: si la primera pregunta ya tiene opciones con imagen, la portada va sin foto. Revisar los textos que la referencien |
| 2026-10-26 | Calistenia Rusa | "Esta imagen quedó muy mal, no quiero imagen ahí, y la del tipo durmiendo que ponés después también sacala" | §4: la foto de un paso solo va si muestra la opción o el test. La decorativa se saca |
| 2026-10-26 | Calistenia Rusa | "Las imágenes son muy malas, busca otros quiz de calistenia militar que tengan mejores fotos, y usa esas" | §4: las fotos se sacan de los competidores del mismo nicho vía Biblioteca de Anuncios → dominio → HTML de la landing. Las siluetas con alfa sucio se limpian y se montan en tarjeta. Si una sola falta, se genera con el encuadre del set |
| 2026-10-26 | Calistenia Rusa | "La slide que muestra el resumen tiene mucha info, se hace muy larga, hagámosla más corta" | §5: la pantalla de resultado va corta — una tarjeta con las barras, 4 chips, 3 logros |
| 2026-10-26 | Calistenia Rusa | "Los colores reemplaza el rojo por un verde que quede bien, medio oscurito" | Verde #1F6B47 (el mismo de [[secreto-de-la-insulina]]). Las barras de riesgo y el aviso de cupos quedan en rojo, para que el verde siga significando "bien" |
| 2026-10-26 | Calistenia Rusa | "Quiero que hagamos un quiz simple, porque va a tener vsl… quitarle algunas preguntas que sintamos que están de más, y dejarlo bien clean" | Cuando el embudo lleva VSL, el quiz **se recorta**: se van todos los bridges de texto (el VSL los dice mejor), las preguntas redundantes y el bloque de hábitos (agua, sueño, alimentación, energía), y la segunda página de venta duplicada. Quedan las preguntas que **personalizan el resultado** (objetivo, cuerpo actual y deseado, molestias, nivel, dolores, altura y pesos) y las de compromiso emocional. Antes de cortar se le muestra la lista de pasos que quedan y la de los que se van, y elige él |
| 2026-10-26 | Calistenia Rusa | Flecha azul del antes/después sobre una paleta roja | Cuando la paleta cambia de tema, las **imágenes reusadas con elementos gráficos de color** (flechas, marcos, destacados) se recolorean con Pillow mapeando el matiz y conservando saturación y luminosidad. La foto queda idéntica y no hace falta IA |
| 2026-10-26 | Tai Chi Fit | "Usá su mismo quiz, que es cortito, simple y directo, y donde diga cosas de militar lo adaptás a Tai Chi" | Cuando el quiz modelado tiene un **tema** (militar, espacial, etc.) se cambia el tema entero —vocabulario, rangos, paleta e íconos— pero **no** la cantidad de pasos, su orden ni su lógica. Las preguntas que dependen del producto (ej. "cuántas flexiones hacés") se reemplazan por el test equivalente de la disciplina nueva (ej. equilibrio en un pie), nunca se borran |
| 2026-10-24 | Protocolo Chía 28D | "No es landing, es quiz, este es el link del quiz, tmb lo tenemos que armar" | El quiz del VSL se copia igual (5 pasos, pantalla de análisis, VSL arriba y CTA con retraso) y solo se pasa a español neutro y al precio nuevo. `SEGUNDOS_OFERTA` se calcula con el segundo exacto en que **nuestro** VSL dice el precio, no con el número del original |
| 2026-10-22 | Landing Herrero de Finde | "Me encantó la landing… los primeros textos, que estén alineados al centro" | En landings, los textos del hero (eyebrow, titular, promesa y bajada) van centrados aunque el original los alinee a la izquierda |
| 2026-10-18 | Pan Sin Picos | "Las imágenes son muy malas, me dan ganas de irme del quiz, se ve muy low ticket" (pan en SVG y emojis) | §4: fotos profesionales con IA y un mismo estilo en todo el quiz; nada de ilustraciones ni emojis como imagen principal |
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
| 2026-10-25 | Protocolo Chía 28D | "Poneme el vsl en el quiz, y quiero que el botón de cta aparezca a los 16 minutos, el video tiene que arrancar de una" | §7b: player propio con autoplay con sonido y botón por tiempo visto del video |
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

## 2026-10-27 · Entregar el quiz para ImpulTienda

- El entregable es **un solo `.txt` autocontenido** que se pega en el `custom_html`: `OUTPUTS/scripts-vsl/inline_quiz.py <quiz.html> <salida.txt>` mete cada imagen de `CONFIG.IMG` como data URI.
- **Pasar todo a webp con tope de 1000 px de ancho.** Sin eso, un `mockup.png` de 1,1 MB se vuelve 1,5 MB en base64 y el archivo entero pasa de 2,4 MB. Con la conversión quedan 858 KB sin pérdida visible.
- **El embed de un VSL va dentro de `<template id="vsl-template">` y solo el `<iframe>`**, sin el `<div>` envoltorio que dan Panda o VTurb: el marco del quiz ya resuelve el 9:16.
- **Si el pedido es "que el botón aparezca a los X minutos", el disparador es el reloj**, no el `timeupdate` del reproductor: con el tiempo del video, el que adelanta se saltea la espera. El reloj arranca cuando se monta el player, o sea cuando entran a la última slide.
- Antes de entregar, probar con una copia de `SEGUNDOS_OFERTA` chiquito y verificar que la oferta aparece sola.

## 2026-10-27 · La marca del logo tiene que significar algo

Santiago, sobre la estrella del encabezado de Calistenia Rusa: *"no me gusta la estrella, hay dos opciones, o ponés algo más relacionado a la calistenia, o nada"*. Reglas:
- **Una estrella genérica no es un logo**: no dice nada de la oferta. O la marca es del tema, o va solo el texto.
- A **30 px** casi nada se lee. De cuatro intentos (dominada, brazo flexionado, bandera humana, anillas) solo sobrevivieron las **anillas de gimnasia**: dos círculos colgando de una barra, trazo 2.3 sobre un SVG de 19 px. El brazo flexionado quedó como mancha y la bandera humana se lee como una bandera común.
- Antes de elegir, **renderizar los candidatos al tamaño real** (30 px) en una página aparte con Chrome headless y mirarlos. A 60 px todos parecen buenos y después no se entiende ninguno.
- **Terminó eligiendo el texto solo.** Le mostré las anillas ya puestas y respondió: *"no, sacale el logo, dejá solo lo de calistenia rusa coach santi"*. Es la segunda vez en la misma tarea que prefiere quitar antes que agregar (ya había sacado dos fotos de pasos y la del encabezado). Regla: **cuando duda entre una marca y nada, la respuesta es nada** — y conviene ofrecer esa opción primero en vez de presentar un ícono nuevo.

## 2026-10-27 · Un botón en flex no centra el texto que se parte en dos líneas

Santiago: *"el botón de cta del final está alineado a la izquierda"*. Era el CTA de abajo del VSL, el que aparece con la oferta: en pantalla de teléfono "Obtener mi plan personalizado ahora" se parte en dos renglones y **el segundo quedaba pegado a la izquierda**.

La causa: `.btn` es `display:flex` con `justify-content:center`. Eso centra la **caja** del texto dentro del botón, pero adentro de esa caja el texto sigue alineado según `text-align`, que hereda `start`. Con una sola línea no se nota; con dos, sí. El CTA del cierre no mostraba el problema porque está dentro de `.prueba`, que ya tiene `text-align:center`.

**Regla: todo `.btn` lleva `text-align:center` además del `justify-content:center`.** Y al revisar un quiz, mirar los botones **en ancho de teléfono**, que es donde las etiquetas largas se parten.

**Cómo revisar en ancho real sin salir del navegador:** Chrome headless con `--window-size=390,...` **no aplica el viewport** (maqueta ancho y recorta, y parece que hubiera desborde cuando no lo hay). Lo que sí funciona es cargar la página en un **`<iframe>` de 390 px** dentro de una pestaña ya abierta: ahí el viewport es real, corren las media queries y se puede medir con `getBoundingClientRect()` sobre `contentDocument`.

## 2026-11-04 · Los CTA del último paso: uno solo los engancha a todos

Santiago, sobre DanceGo: *"todos los botones de cta de la ultima slide, tienen que redirigir a este checkout"*. Reglas fijas para la slide de la oferta:

- **Un único lugar con la URL: `CONFIG.LINK_CHECKOUT`.** Nunca un `href` hardcodeado botón por botón: con tres o cuatro CTAs en la misma slide, el día que cambia el checkout uno queda viejo y manda tráfico pagado a la nada.
- **Un solo `ligarCTAs()` que barre toda la sección**, con selector ancho: `#oferta a.btn, #oferta button.btn, #oferta .js-cta`. Así entran también las chapas que no son `<a>` (la de "HOY: GRATIS", por ejemplo), que se enganchan con `cursor:pointer` + `location.href`.
- **Llamarlo también en el arranque**, no solo al renderizar la oferta: así los `href` ya están puestos desde que carga la página y el botón sirve aunque el paso de la oferta nunca se monte o algo falle antes.
- **Tiene que ser idempotente**: marcar cada elemento con `dataset.cta` y saltearlo si ya estaba. Si no, al llamarlo dos veces (arranque + oferta, o la oferta que se destapa con `SEGUNDOS_OFERTA`) se suman dos listeners y el pixel dispara **dos `AddToCart` por clic**, que infla la métrica y ensucia la optimización.
- Los `<a>` del checkout llevan `rel="noopener"`.
- **Verificar en el navegador, no leyendo el código**: saltar al último paso y listar `#oferta a, #oferta button, #oferta .js-cta` con su `href`. Si algún CTA sale con `href="#"`, no se enganchó. Probar también con `?utm_source=...` en la URL y confirmar que el `href` final arrastra los UTM.
