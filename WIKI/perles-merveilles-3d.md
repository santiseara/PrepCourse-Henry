# Perles Merveilles 3D

> Oferta nueva **en inglés** (US$ 24,65 desde 74): 83 figuras en mostacillas 3D explicadas paso a paso —60 animales en 6 familias + 23 modelos de Halloween y Navidad + el pesebre completo de 12 figuras—. Clon en inglés de una oferta francesa que ya corre con 6 ads. Tanda 1 producida el 30/10: 6 videos de voz en off sobre B-roll de TikTok.

## La oferta
- **Producto:** colección de patrones de mostacillas en 3D. El mecanismo que vende no es "hacer animalitos", es **poder leer el patrón**: filas numeradas, cuentas contadas, el recorrido de los **dos hilos** dibujado y **puntos de control** para comparar la pieza antes de seguir.
- **Precio:** US$ 24,65 (tachado 74) · 83 diseños · 7 bonus · acceso instantáneo · colección en inglés.
- **Estacional:** la edición Halloween–Navidad suma 23 modelos de temporada y el **pesebre de 12 figuras** (niño, María, José, los tres reyes, el pastor, la oveja, el burro, el buey, la estrella y el establo). Es el ángulo más fuerte de acá a diciembre.
- **Avatar:** mujer que ya hace manualidades y se frustra con los esquemas gratis de internet. El dolor no es la falta de ganas, es **el paso que nadie explica**.
- Carpeta: `~/Desktop/perles-merveilles-3d/` (`landing/index.html`, `anuncios/`, `imagenes/`).

## DNA de los ads del original (francés)
Los 6 ads del competidor están en `anuncios/work/ref/` con su transcripción. El patrón:
1. **Dato duro de entrada:** "un elefante son 236 cuentas, por eso nadie empieza por el elefante".
2. **El problema está en el papel, no en tus manos** (desculpabilizar).
3. **Mecanismo:** filas contadas + recorrido de los dos hilos + punto de control.
4. **Catálogo:** 60 animales en 6 familias, del jardín al océano.
5. **Estacional gratis:** Navidad y pesebre dentro de la edición especial.
6. **CTA suave:** "mirá la colección acá abajo".

## Tanda 1 (30/10) — 6 guiones y 6 videos
Guiones en `OUTPUTS/2026-10-30-guiones-perles-merveilles-v1-v6.md` (inglés y español con voseo) y copia en `anuncios/guiones/`.

| # | Ángulo | Archivo |
|---|---|---|
| V1 | Empezás por el caracol (76 cuentas), no por el elefante (236) | `PM-V1-start-with-the-snail.mp4` |
| V2 | El problema estaba en el papel, no en tus manos | `PM-V2-it-was-on-the-paper.mp4` |
| V3 | Si un libro te da 83 figuras, ¿por qué seguís comprando adornos? | `PM-V3-why-are-you-still-buying.mp4` |
| V4 | El patrón gratis siempre saltea un paso | `PM-V4-the-step-nobody-explains.mp4` |
| V5 | Lo que hacés con tus manos no se vende en ningún local | `PM-V5-not-sold-in-any-shop.mp4` |
| V6 | Un pesebre que vuelve cada diciembre por veinte años | `PM-V6-the-nativity-that-comes-back.mp4` |

## Producción (pipeline, 30/10)
- **Voz:** Google AI Studio, **Gemini 3.1 Flash TTS Preview**, voz **Sulafat**, Pace **Natural**. Audio Profile: mujer estadounidense de 40 y pico que hace mostacillas en la mesa de la cocina, hablándole a otras, sin tono de locutora. Crudos de 43 a 55 s, los 6 con MD5 distinto, en `anuncios/work/vo/`. En la edición van a `speed 1.30` con `silence [0.26, 0.12]`.
- **Visual: 100% clips de TikTok** (regla del 29/10), ni una foto fija ni captura. 28 clips bajados a `work/tiktoks/`, revisados con hoja de contactos de 12 cuadros cada uno.
- **Editor:** `OUTPUTS/scripts-vsl/edit_perles.py` (copia de `edit_atlas.py` con la paleta navideña: rojo #BE1E2D, dorado #E7BE6E y verde pino #123428; subtítulos de 3 palabras con la activa en dorado; placa final PERLES MERVEILLES 3D). Planes en `anuncios/work/plans/gen.py`.

## Dos trampas de esta tanda (anotar antes de la próxima)
- 🆕 **El pool se come la tanda si no se topea por clip.** Los 14 clips de una misma creadora (mármol + boles + uñas plateadas) son largos y aportaban el 80% de los recortes: el primer V1 salió con 13 planos que parecían el mismo. Dos arreglos en el pipeline: **tope de 8 recortes por clip** repartidos a lo largo del clip, y **familias visuales** (`fam` en el plan) para que el editor penalice repetir creadora, no repetir archivo.
- 🆕 **La marca de agua no se ve en la hoja de contactos chica.** El clip `7669715654102027552` entró al pool como limpio y en el render se leía "handsofjulia" en el medio del cuadro. Regla: además de la hoja de contactos, mirar **un cuadro grande de la mitad inferior de cada clip** antes de armar el pool.

## Preguntas abiertas
- ¿Qué países y presupuesto para el testeo? Por defecto, lo de [[testeo-de-creativos]]: US/CA/AU/UK/NZ, ABO US$ 10 por conjunto.
- Falta la **descripción de ads** y las **natives** de esta oferta.
- El ángulo Halloween ya pasó; en enero hay que reemplazar los 4 guiones navideños (V3 a V6) por ángulos de todo el año.

## Relacionado
[[guiones-y-anuncios]] · [[como-trabajar-con-santiago]] · [[atlas-de-cortes]] · [[vsl-reglas-de-armado]]

## Fuentes
- ~/Desktop/perles-merveilles-3d/landing/index.html
- ~/Desktop/perles-merveilles-3d/anuncios/work/ref/ (6 ads del original en francés, con transcripción)
- OUTPUTS/2026-10-30-guiones-perles-merveilles-v1-v6.md
