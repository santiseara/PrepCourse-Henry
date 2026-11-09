# El Secreto de la Chía (AR) · O Segredo da Chia (BR)

> Oferta propia de Santiago: protocolo casero de **28 días con chía** para mujeres de más de 40. Corre en Argentina en `chauinflamacion.com/pages/chia` (tienda Shopify, checkout en ImpulTienda) a **$24.900**. El 9/11 se clonó el quiz entero al **portugués de Brasil** como **O Segredo da Chia**, a **R$ 67**. (fuente: HTML del quiz en vivo bajado con curl el 2026-11-09)

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
- **Checkout pendiente**: quedó `https://COMPLETAR.impultienda.ar/checkout/chia` en `QUIZ_CONFIG.checkout`, que es el único lugar del archivo donde vive la URL.
- Entregables: `~/Desktop/o-segredo-da-chia/` (`landing/` con el `.txt` para pegar, el `.html` y el `PRUEBA.html` con las fotos embebidas; `imagenes/` con las 10 fotos). Copia en `OUTPUTS/2026-11-09-quiz-o-segredo-da-chia-br.html`.
- Verificado en el navegador a 390 px: los 28 pasos, **cero desborde**, cero errores de JS, los dos CTA leyendo el CONFIG.

## Detalles / notas
- Paleta: `--pri:#FF7A00` sobre fondo `#FFF5EB`, tipografía Poppins. El verde (`--g:#2FA866`) solo significa "bien" (botones de avance y precio).
- Imágenes servidas desde el `storage` de Supabase de la tienda argentina. La versión BR apunta a esas mismas URLs: funcionan igual, pero si Santiago quiere independizarla, las 10 fotos ya están en la carpeta listas para subir.
- Datos de la portada marcados como ejemplo en el propio CONFIG (`-12kg`, `+12.847 mujeres`): **no están respaldados**, los dejó así él.

## Preguntas abiertas
- ¿Cuál es el subdominio de ImpulTienda de la tienda brasileña? Sin eso los CTA no van a ningún lado.
- ¿La versión BR lleva cuotas (`ou 12x de R$ 6,70`)? El campo `cuotas` está vacío, igual que en el original argentino.
- ¿Se suben las 10 imágenes a la tienda de Brasil o se dejan apuntando al Supabase argentino?

## Relacionado
[[quizzes-reglas-de-armado]] · [[protocolo-chia-28d]] · [[internacionalizacion]] · [[quiz-funnel]] · [[secreto-de-la-insulina]]

## Fuentes
- `https://www.chauinflamacion.com/pages/chia` (HTML del quiz en vivo, 2026-11-09)
- `OUTPUTS/2026-11-09-quiz-o-segredo-da-chia-br.html`
