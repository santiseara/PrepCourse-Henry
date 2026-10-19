# Infinity 3D (mesas infinitas, oferta en inglés)

> Planos para fabricar y vender mesas con efecto infinito (espejo + tira LED + vidrio con film espejado). Santiago la tiene en español (página "Infinity 3D" en Meta, ~26 ads activos) y el 2026-10-19 arrancó la versión para EE.UU. con landing propia. (fuente: pedido de Santiago del 2026-10-19)

## Ideas clave
- **Landing EN:** https://infinity-mirror-tables.impultienda.ar/ . Precio $27 (tachado $81, -67%), pago único, garantía de 30 días.
- **Producto:** guía maestra + 26 planos acotados de 11 modelos, en melamina/terciado de 3/4″ o caño cuadrado (20×20 o 30×30 mm).
- **5 bonus:** Materials & Cost Calculator, Error-Free LED Setup, Messages for Glass Shops, Photos & Posts That Sell y 20 Infinity Effect Designs.
- **Cuentas de la landing:** mesa ratona LED de 39″×24″, materiales $165, publicada a $495 (diferencia de $330 por 8 horas de taller).
- **Público:** herreros, carpinteros y principiantes con herramientas. Sirve para venderlas, para la casa o para regalar.
- **Sus ads en español (Ads Library, page id `1381827265007768`):** voz en off de hombre de 30 a 53 s, con cortes cada ~2 s. Hay 6 ganchos sobre el mismo cuerpo:
  1. **La cuenta:** 8 horas de taller, publicada a $300.000 en Mercado Libre, hacé la cuenta.
  2. **"Cansado de placares / portones que no dejan plata"**, por oficio (carpintero o herrero).
  3. **"Imaginá no preguntarte nunca más qué fabricar para vender".**
  4. **El mecanismo:** parece un pozo sin fondo y tiene 12 cm.
  5. **3 errores:** los puntitos del LED, el reflejo fantasma y las burbujas.
  6. **"El tutorial que nadie te da":** las medidas en milímetros.
  El cuerpo fijo dice: "26 planos de 11 modelos… Paso 1, elegís el modelo. Paso 2, pedís los cortes. Paso 3, armás, prendés la tira y sacás las fotos con la guía… No hace falta ser diseñador… Tocá el botón".
- **Su edición:** el hook va en una caja blanca arriba ("¿Cuánto cobrarías por esta mesa? 👀"), con etiquetas naranjas ("✓ 8 HORAS DE TALLER", "✕ TE COMEN LA SEMANA") y una tarjeta oscura con borde naranja para el precio de Mercado Libre. La tarjeta del plano muestra las medidas. Subtítulos condensados en blanco con la palabra activa en naranja, renders de IA y mockup del sistema, y placa final "INFINITY 3D · 26 planos + 5 bonus · Tocá Más información 👇".

## Cómo se arma un video (2026-10-19)
1. **B-roll:** 7 TikToks que pasó Santiago, bajados con `yt-dlp` (en loop, porque falla). Más las fotos de la landing (`curl` + regex de los `.webp` de supabase): mockups, renders y tapas de bonus como planos fijos con zoom. Las fotos cuadradas de 440 px van centradas sobre la misma foto desenfocada.
2. **Voz:** Google AI Studio, **Gemini 3.1 Flash TTS Preview**, voz **Orus** (Firm, Lower middle pitch). Audio profile: *"American man around 40, a hands-on craftsman narrating a punchy DIY ad on TikTok. Confident, direct, energetic and conversational, brisk pace…"*.
   - Se generan en tanda por JS: `_setTA(2, texto)` (insertText en el 3.er textarea), click en Run y `_grab` espera el `data:` del `<audio>` y lo manda por POST a `recv2.py` (127.0.0.1:8767).
   - Salen de unos 40 s por cada 115–140 palabras.
3. **Edición:** `OUTPUTS/scripts-vsl/edit_infinity.py plan.json salida.mp4` (velocidad 1.12, cortes de 1,8 a 3 s, `usage.json` compartido). Los planes salen de `~/Desktop/mesas-resina/work/plans/gen.py`, que trae los tramos útiles de cada TikTok, los anchors y las placas (hook, chip, price, plan, end).
   - Las placas se componen en **una sola pista .mov con alfa**. Varios PNG superpuestos con `enable` congelaban el video o no aparecían.
   - DIN Condensed no tiene ✓ ni ″: los íconos van con Arial Unicode y las pulgadas con `"`.
   - Las fotos fijas **nunca se espejan** (los mockups y las tapas tienen texto). Ojo con los anchors por palabra: si la palabra se repite antes ("three" en "these three mistakes"), hay que usar `occ` 1.

## Activos
- Videos: `~/Desktop/mesas-resina/IN-V1..V6.mp4` (~33–40 s). Guiones en inglés y español: `OUTPUTS/2026-10-19-guiones-infinity-3d-en.md`.
- Carpeta de trabajo: `~/Desktop/mesas-resina/work/` (`tiktoks/`, `ads/` con sus 23 ads y `transcripts.txt`, `landing/`, `vo/`, `plans/`).
- **TikToks y tramos a cuidar:** `@jorgevalenzuelam/7683664277789592850` (film y tira LED) trae texto en español en 12–15 s ("pieza 1: 50x76cm") y en 64–68 s (medidas en cm): excluidos. Ese mismo TikTok y `@street_art888/7447541641076018478` muestran caras en muchos tramos.

## Preguntas abiertas
- ¿Hay ganador en español para priorizar el ángulo? (por cantidad de copias: la cuenta de 8 horas y el de oficio).
- ¿El nombre "Infinity 3D" se mantiene en inglés en los ads? Por ahora sí, porque la landing lo usa.

## Relacionado
[[bachas-de-concreto]] · [[guiones-y-anuncios]] · [[vsl-reglas-de-armado]] · [[internacionalizacion]]

## Fuentes
- Biblioteca de anuncios de Meta, página "Infinity 3D" (consultada el 2026-10-19)
- Landing https://infinity-mirror-tables.impultienda.ar/
- 7 TikToks que pasó Santiago
