# 100 Paper Squishies

> Oferta de Santiago: ebook de **100 diseños imprimibles de squishies de papel** para chicos, a **US$ 16,99** con 3 bonos. Se modela a **Hora de Papel**, un anunciante argentino que lanzó el mismo producto el 15 de octubre y en 12 días ya corre 94 anuncios activos en español, italiano y alemán. (fuente: pedido de Santiago del 2026-10-27)

## La oferta propia
- Landing: `https://100-paper-squishies.impultienda.ar/` — "100 Paper Squishies. 100 designs, so there's always an activity ready whenever they feel like making something".
- **US$ 16,99** (tachado US$ 19,99, "you save $3"), pago único, entrega instantánea por email. **Está en inglés**, no en español: el mercado es anglo, el competidor todavía no lo toca.
- Contenido: 100 diseños A4 listos para imprimir, en blanco para pintar, con líneas de corte, doblado y pegado marcadas; sets de varias piezas; mini guía de materiales y armado.
- **3 bonos:** Seasonal Pack (Navidad, Halloween, cumpleaños) · Gift Tags & Display Boxes (etiquetas y cajitas imprimibles) · The Squishy Pro Guide (que queden más blandos, duren más y cómo arreglar uno roto).
- Diseños que nombra la tapa: butter, dumpling, sandwich, capibara, frutilla, pizza. Materiales: hojas, marcadores, cinta, tijera y algodón.
- La landing trae solo **5 imágenes** (tapa + 4 fotos de producto): copiadas en `~/Desktop/100-paper-squishies/imagenes/`. Alcanzan para los stills de los ads.

## El competidor: Hora de Papel (page id 1114598271746718)
- **94 anuncios activos** relevados el 27/10, todos del mismo producto (no es multi-oferta). Arrancó el **15 de octubre**: 2 ads ese día, 4 el 16, 4 el 17 y después tandas de 14 a 21 por día el 22, 24, 25 y 27. **Está escalando fuerte y rápido.**
- Corre **español rioplatense, italiano y alemán**. Tiendas: `horadepapel.impultienda.ar` y `horadepapel.myshopify.com`. Precio en AR: $15.990.
- **Videos de 9 a 25 segundos** (mediana 18). Esto es lo más distinto de todo lo que veníamos haciendo: son ads cortísimos, no de 45 s ni de 1:30.
- **Un solo texto principal por idioma**, con la primera línea cambiando según el ángulo. Lo que varía es el video, no el copy.
- **Tres formatos de video:**
  1. **Voz en off + montaje de clips reales** de manos pintando, recortando y rellenando squishies, subtítulo de una línea en caja blanca y **placa final con la tapa del ebook** + "Tocá en 'Ver más'". Es el formato mayoritario y el que replicamos.
  2. **UGC de mamá a cámara** en la cocina (solo el hook hablado) y después el montaje.
  3. **Animación 2D** del squishy de papel hablando en primera persona, fondo amarillo pastel.

### DNA del cuerpo (idéntica en los 94)
hook de una línea → el pivote ("mejor le imprimo cien") → qué es ("un libro digital con cien squishies de papel para imprimir en casa") → cómo, en cadena de verbos ("elige uno, lo pinta, lo recorta, lo rellena con algodón y a apretar") → variedad ("butter, dumpling, sánguche, capibara y muchos más") → entrega y CTA ("te llega el PDF al instante, lo imprimís las veces que quieras. Tocá en 'Ver más'").

### Las familias de hook, por volumen
1. ⭐ **El precio del kiosco** (~18 ads, relanzada el 27/10): "$5.000 un squishy y a los dos días, roto", "4 squishies rotos este mes: $20.000 tirados", "Un squishy de kiosco: $5.000. Esto: 100".
2. ⭐ **El squishy habla en primera persona**: "Hola, mamá. En el kiosco salgo $5.000 y a los dos días estoy roto".
3. **La pedida**: "Mamá, ¿me comprás uno?", "Otra vez en la caja del súper", "Mi mamá no me compra squishies".
4. **El recreo**: "Volvió del cole con 3 squishies que no hizo él", "A scuola se li scambiano tutti", "La maestra los secuestró… eran de papel".
5. **El regalo**: "Le regalé esto en vez de otro juguete", "¿Qué le regalás si ya tiene de todo?", "Cumples del mes".
6. **Humor y POV**: "Las 5 etapas de la mamá en la era squishy", "POV: tu hija vende squishies como si fuera contrabando", "POV: encontrás la reserva secreta", "Último momento en El Diario del Recreo".
7. **Sin pantallas** y **prueba social** ("más de mil familias") son las dos colas menores.

## Tanda 1 (2026-10-27): 6 videos
- Guiones en **inglés y español con voseo**, los dos completos: `OUTPUTS/2026-10-27-guiones-100-paper-squishies.md` (copia en `anuncios/guiones-tanda1.md`). Una familia ganadora distinta por video: 1) el precio del kiosco, 2) el squishy que habla, 3) la pedida en la caja, 4) el canje en el recreo, 5) el cumple de ocho nenes, 6) las cinco etapas de la mamá.
- **Videos en inglés** (la landing lo está), 9:16, de **15 a 24 s**: `~/Desktop/100-paper-squishies/anuncios/SQ-V1…SQ-V6`.
- **Voz:** AI Studio, Gemini 3.1 Flash TTS Preview, voz **Sulafat**, Pace Natural, Audio Profile de mamá estadounidense de 35 grabando un voiceover de TikTok. Salen de 19 a 31 s en crudo; el plan las lleva a `speed 1.30` con `silence [0.26, 0.12]`.
- **Edición** (`OUTPUTS/scripts-vsl/edit_squishies.py`, copia de `edit_365.py`): rojo #EA203A de la tapa en el hook, los chips y el botón; subtítulo de 2 palabras con la palabra activa en amarillo; cortes de 1,6 a 2,5 s; tapa del ebook y fotos de producto como stills; placa final "100 PAPER SQUISHIES · 100 DESIGNS · 3 BONUSES · Tap Learn more".
- **B-roll de TikTok:** 150 videos del tag `#papersquishy` resueltos con tikwm, 42 bajados y **21 usados**. Cero stock, cero créditos. Material en `anuncios/work/tiktoks/`.
- **Texto principal:** uno solo para los seis, como hace el competidor (está al final del archivo de guiones).

## Cómo se sacaron las visuales (sirve para la próxima oferta)
- La búsqueda de TikTok sigue tirando "Hubo un problema", pero **la página de tag sí carga**: `tiktok.com/tag/papersquishy` da ~230 links con scroll. De ahí salen los IDs.
- **A tikwm le alcanza el ID**: `https://www.tikwm.com/api/?hd=1&url=https://www.tiktok.com/@x/video/<ID>` funciona con cualquier handle. El endpoint de búsqueda (`/api/feed/search`) está detrás de Cloudflare y no sirve.
- **TikTok bloquea el POST a 127.0.0.1** (CSP), así que los links se sacan por chunks desde `javascript_tool` (la respuesta se corta cerca de los 1.000 caracteres). AI Studio sí deja el POST al receptor local.
- **Revisar los clips con hoja de contactos no alcanza con 6 cuadros.** En esta tanda se colaron, y hubo que rehacer el render tres veces: un cartel coreano que aparecía recién al minuto, un "DIY Crunchy Squishy" que volvía a los 22 s, y marcas de agua de conejito y calabaza que el `zoom` 1.16 no llegaba a recortar. Reglas nuevas abajo.

## Reglas anti-bloqueo de este nicho
- El precio que se nombra es **el del squishy del kiosco** (lo que gasta hoy), nunca el del ebook. Eso respeta la regla de "sin precio" y encima es el ángulo ganador.
- Sin atributos negativos sobre el chico ni promesas de conducta. El dolor va en primera persona ("le compré tres este mes, los tres rotos").
- CTA "Tap Learn more" / "Tocá en Ver más" + entrega instantánea.

## Preguntas abiertas
- ¿Se corre también en español e italiano, como el competidor, o solo en inglés? Los guiones ya están en las dos versiones.
- ¿Hay upsell después del pago? Los 3 bonos ya están adentro del producto, así que el OTO habría que armarlo.
- El competidor tiene 10 anuncios de imagen (carrusel, "top 3 para empezar", "comprar vs. imprimir", prueba social). Todavía no hicimos natives para esta oferta.

## Relacionado
[[365-actividades-imprimibles]] · [[funnel-hacking]] · [[guiones-y-anuncios]] · [[caza-de-ofertas]] · [[ugc-y-video-generativo]] · [[vsl-reglas-de-armado]]

## Fuentes
- Landing propia y biblioteca de anuncios de Hora de Papel (relevadas el 2026-10-27)
