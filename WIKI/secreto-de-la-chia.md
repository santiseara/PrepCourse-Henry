# El Secreto de la Chía (AR) · O Segredo da Chia (BR)

> Oferta propia de Santiago: protocolo casero de **28 días con chía** para mujeres de más de 40. Corre en Argentina en `chauinflamacion.com/pages/chia` (tienda Shopify, checkout en ImpulTienda) a **$24.900**. El 9/11 se clonó el quiz entero al **portugués de Brasil** como **O Segredo da Chia**, a **R$ 67**, y el 10/11 se empaquetó la **versión argentina autocontenida** para pegar en ImpulTienda. (fuente: HTML del quiz en vivo bajado con curl el 2026-11-09)

## Ideas clave
- **Es un quiz sin VSL**: 28 pasos y la oferta aparece sola al final, sin video de por medio. El checkout está en los dos CTA de la última pantalla (`data-checkout`), los dos leen `QUIZ_CONFIG.checkout`.
- **Está montado como `custom_liquid` dentro de una página de Shopify**, no en ImpulTienda: se baja con `curl -sL <url de la página>` y el bloque viaja en texto plano (`<script>` con `QUIZ_CONFIG`, `<style>` y el motor). Ojo: el comentario de apertura aparece **repetido 4 veces** por cómo lo renderiza Liquid; se corta desde el primer `<script>`.
- **Mide con Microsoft Clarity**: un evento por pantalla (`quiz_p01_portada` … `quiz_p28_oferta`), una etiqueta `quiz_ultimo_paso` y dos eventos de clic de compra. Eso se mantuvo igual en la versión brasileña para poder comparar embudos.
- **Prueba social falsa pero contenida**: contador de "personas haciendo el test" que oscila entre 24 y 63, y la cinta diagonal "SOLO HOY · APP GRATIS" que solo se ve en la portada.
- Los testimonios están **vacíos** en el CONFIG, así que el paso 26 se salta solo. Si se cargan testimonios reales, aparece sin tocar nada más.

## La versión de Brasil (2026-11-09)
- **Clon 1:1**: mismos 28 pasos, mismo orden, mismos componentes, misma paleta naranja y las **mismas 10 imágenes** — ninguna tiene texto quemado, así que se reusan sin tocarlas.
- Marca: **O Segredo da Chia**. Precio **R$ 67**, tachado **R$ 147** (decisión de Santiago del 9/11).
- Localización, no traducción: *panza* → **barriga**, *cola* → **bumbum**, *muslos* → **coxas**, *talle grande* → **plus size**, *plata* → **dinheiro**, *súper* → **mercado**, *te devolvemos cada peso* → **devolvemos cada centavo**, fecha con `toLocaleDateString("pt-BR")`.
- **Checkout: `https://o-segredo-da-chia.impultienda.ar/checkout`** (lo pasó Santiago el 9/11, verificado 200 con `curl -sIL`). Vive en `QUIZ_CONFIG.checkout`, el único lugar del archivo donde está la URL; los dos botones de compra la leen de ahí.
- Entregables: `~/Desktop/o-segredo-da-chia/` (`landing/` con el `.txt` para pegar, el `.html` y el `PRUEBA.html` con las fotos embebidas; `imagenes/` con las 10 fotos). Copia en `OUTPUTS/2026-11-09-quiz-o-segredo-da-chia-br.html`.
- Verificado en el navegador a 390 px: los 28 pasos, **cero desborde**, cero errores de JS, los dos CTA leyendo el CONFIG.

## La versión argentina autocontenida (2026-11-10)
Pedido de Santiago: *"necesito que hagamos exactamente el mismo quiz pero en español argentino"*. **El quiz argentino ya existía y es el original**, y ya estaba **entero en voseo** (los únicos `puedes` del HTML en vivo son strings del tema de Shopify, no del quiz). Así que no hubo traducción: lo que faltaba era el **mismo paquete que se armó para Brasil**, pero argentino.

- Se bajó el quiz en vivo con `curl -sL` y se cortó el bloque desde el primer `<script>` hasta el `</script>` del motor: **39,2 KB**, igual que el brasileño. Diff contra el de Brasil: **139 líneas**, y todas son idioma, marca, precio, checkout y la variable `Bs` del artículo portugués. Mismo motor, mismos 28 pasos (`TOTAL=29`), mismas 10 imágenes.
- Entregables en `~/Desktop/el-secreto-de-la-chia/`: `landing/` (`.txt` para pegar en el `custom_html`, el `.html` y el `PRUEBA.html` de 1 MB con las fotos embebidas) e `imagenes/` con las 10 fotos renombradas en castellano. Copia en `OUTPUTS/2026-11-10-quiz-el-secreto-de-la-chia-ar.html`.
- **Checkout propio: `https://el-secreto-de-la-chia.impultienda.ar/checkout`** (lo pasó Santiago el 10/11, verificado 200 con `curl -sIL`). Vive en **un solo lugar** (`QUIZ_CONFIG.checkout`) y los dos CTA del último paso (`QUIERO EMPEZAR 🥰` y `¡QUIERO EMPEZAR AHORA! 🔥`) lo leen de ahí: comprobado en el navegador. Precio **$24.900**, tachado **$38.999**.
- 🐞 **Bug del motor, en las dos versiones (AR y BR), encontrado el 10/11:** en las pantallas de carga (`analisis_carga` y `armando_rutina`) el `setInterval` de la barra se limpia solo dentro del `setTimeout` final, y esos pasos llevan la flechita de volver. Si la persona toca `‹` antes de que terminen, el intervalo tira un error cada 100 ms (82 medidos) y a los 8,5 s el `setTimeout` la **arrastra igual a la oferta**. Se arregla con un `clearInterval` al salir del paso. **No se tocó**: el pedido era el checkout.
- Verificado por código en un iframe de 390 px servido con `http.server`: los 28 pasos hasta la oferta, **cero desborde**, **cero imágenes rotas**, **cero errores de JS**, todos los `.btn` centrados y los dos CTA (`QUIERO EMPEZAR 🥰` y `¡QUIERO EMPEZAR AHORA! 🔥`) saliendo del CONFIG.
- 🪤 **Los errores de JS que aparecen al recorrer el quiz dos veces en el mismo iframe son del recorrido, no del quiz.** La primera pasada deja el estado a mitad de camino y la segunda clickea pasos que ya no existen (`Cannot read properties of null (reading 'style')`). Se recarga el iframe con `?x=Date.now()` antes de cada verificación.

## Detalles / notas
- Paleta: `--pri:#FF7A00` sobre fondo `#FFF5EB`, tipografía Poppins. El verde (`--g:#2FA866`) solo significa "bien" (botones de avance y precio).
- Imágenes servidas desde el `storage` de Supabase de la tienda argentina. La versión BR apunta a esas mismas URLs: funcionan igual, pero si Santiago quiere independizarla, las 10 fotos ya están en la carpeta listas para subir.
- Datos de la portada marcados como ejemplo en el propio CONFIG (`-12kg`, `+12.847 mujeres`): **no están respaldados**, los dejó así él.

## Preguntas abiertas
- Los CTA van **directo** al checkout, sin arrastrar los UTM de la URL — igual que el quiz argentino. ¿Se agrega el pase de UTM o se deja como está el original?
- ¿La versión BR lleva cuotas (`ou 12x de R$ 6,70`)? El campo `cuotas` está vacío, igual que en el original argentino.
- ¿Se suben las 10 imágenes a la tienda de Brasil o se dejan apuntando al Supabase argentino?
- ⚠️ **Falta el checkout de la versión argentina nueva** ("después te lo paso", 10/11). Hasta que llegue, el `.txt` entregado apunta al checkout que ya corre.

## Relacionado
[[quizzes-reglas-de-armado]] · [[protocolo-chia-28d]] · [[internacionalizacion]] · [[quiz-funnel]] · [[secreto-de-la-insulina]]

## Fuentes
- `https://www.chauinflamacion.com/pages/chia` (HTML del quiz en vivo, 2026-11-09)
- `OUTPUTS/2026-11-09-quiz-o-segredo-da-chia-br.html`
- `OUTPUTS/2026-11-10-quiz-el-secreto-de-la-chia-ar.html`
