# Cápsulas Encantadas (AR)

> Clon argentino del quiz **Tea Charm Studio** (mercado de habla inglesa, 27 USD): cápsulas de té y café sin azúcar que se derriten en la taza, para vender como regalos y souvenirs. Precio **$12.990** ARS. (fuente: quiz en vivo `emilycarter.digitallearninghub.lat`)

## ⚠️ Pendientes
- 🔴 **Checkout:** Santiago dijo *"el link de checkout te lo paso desp"*. El quiz sale con **`/checkout` relativo**, así que apunta al checkout de la tienda donde se pegue el HTML. Cuando pase la URL completa, va en una sola línea: `CONFIG.checkoutUrl`.
- 🔴 **Nombre de marca y de la mentora:** los puse yo. Marca **Cápsulas Encantadas**, mentora **Emilia Castro** (mismas iniciales que Emily Carter, por si alguna imagen las usa), método **Moldeá y Derretí**. Si quiere otros, se cambian en el HTML (la marca aparece ~12 veces) y hay que rehacer la tapa del mockup con `mockup.py`.
- 🟡 **Mail de soporte:** quedó el de la oferta en inglés (`digitallearninghub.support@gmail.com`), que es el que funciona. Se cambia en `CONFIG.correoSoporte`.
- 🟡 **UTMify:** el quiz original traía el script cifrado de UTMify de la tienda en inglés. **No lo copié** (apunta a la configuración de esa tienda). Si quiere rastreo, va el script de la cuenta argentina.

## La oferta
- **Producto:** método + 25 recetas de cápsulas de té y café, 12 formas, colores naturales, lista de compras, plan de ventas, certificado.
- **4 regalos:** Packaging para regalar · Guía de duración y conservación · Precios claros · Kit de los primeros 10 pedidos.
- **Precio:** $12.990 (antes $46.990, −72 %), hasta 3 cuotas sin interés de $4.330.
- **Garantía:** 30 días (en inglés eran 7 días en el sello del mockup; se rehízo a 30 para que no choque con el texto).

## Números del quiz (todos consistentes entre sí)
| Dato | Valor |
|---|---|
| Precio por cápsula | $2.500 |
| Pedido de 40 souvenirs | $100.000 |
| Ingredientes de ese pedido | $12.000 |
| 2–3 pedidos por semana | $1.000.000+ por mes |
| Meses fuertes de la mentora | $2.000.000+ |
| Insumos para arrancar | $8.000–12.000 + $7.000–10.000 = $20.000 o menos |
| Regalo que parece caro (bonus 1) | $35.000 |

La reseña de Brenda cierra con los mismos números: iba a cobrar $800 por cápsula y vende cajas de 12 a $30.000 (= $2.500 c/u).

## Estructura (8 pasos, igual al original)
1. Portada + promesa + 4 chapitas de beneficio · 2. ¿Cuánto tiempo tenés? · 3. ¿Cuál es tu mayor desafío? · 4. ¿Es fácil? · 5. ¿Es barato? · 6. Alumnas (3 chats + 3 fotos) · 7. Carga de 5 s · 8. Resultado y oferta.
El plan personal del paso 8 sale de las respuestas 2 y 3 (3 × 3 combinaciones).

## Qué se cambió de las imágenes (ninguna se generó con IA, costo cero)
- **Hero:** se usó la foto de la cocina (la original tenía el logo *Tea Charm Studio* quemado arriba).
- **Bio del final:** recorte de la foto del logo, del lado derecho, donde no hay texto.
- **Caja corazón:** recorte de la pieza de diseño que tenía todo el texto en inglés; las 4 chapitas (*fácil de hacer, alto valor percibido, perfectas para regalar, baja inversión*) se rehicieron **en HTML**.
- **Chats de alumnas:** las 3 capturas de Instagram en inglés se rehicieron **en HTML** (tarjeta con cabecera, foto y burbujas). Se ven nítidas y las fotos salen del mismo CONFIG, así no pesan doble.
- **Nombres de las alumnas** (Jessica/Aoife/Hannah → Jesi/Aylén/Flor): se repintó la chapita con Pillow y se re-tipeó con Arial Rounded Bold.
- **Mockup:** las 5 tapas, el sello y la tarjetita *Thank you* se borraron interpolando el fondo y se re-tipearon con **Playfair Display** (serif) y **Great Vibes** (script). Script: `OUTPUTS/scripts-quiz/mockup-capsulas.py`.

## Entrega
- `~/Desktop/capsulas-encantadas/landing/capsulas-encantadas-quiz.txt` — autocontenido, 1,4 MB, para pegar en el `custom_html` de ImpulTienda.
- `~/Desktop/capsulas-encantadas/landing/PRUEBA.html` · `quiz.html` (con las imágenes sueltas) · `~/Desktop/capsulas-encantadas/imagenes/` (21 archivos).
- Copia en `OUTPUTS/2026-11-11-quiz-capsulas-encantadas.html`.

## Verificado en el navegador (iframe de 390 px)
Los 8 pasos, sin imágenes rotas, sin desborde horizontal, sin errores de JS; los 4 CTA con el mismo link y arrastrando las UTMs; precio, tachado y cuotas iguales en todos lados; las 24 imágenes del `.txt` cargan.

## Relacionado
[[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[internacionalizacion]] · [[modelo-low-ticket]]

## Fuentes
- Quiz en vivo `emilycarter.digitallearninghub.lat` (ImpulTienda, `custom_html`), bajado el 2026-11-11.
