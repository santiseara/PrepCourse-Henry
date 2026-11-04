# Calendarios 2027 (mercado inglés)

> Modelado de **Hecho en Casa / Calendarios 2027** (Argentina): 50 diseños imprimibles de calendarios de escritorio que, al apilar los doce meses, arman **un ramo de flores parado en un florero**, más una app que pone el precio y anota los pedidos. Se lleva al **mercado de habla inglesa** (arbitraje de sofisticación: la oferta ya corre fuerte en AR).

## Ideas clave

- **El producto es un imprimible, no un objeto.** Se descarga una vez y se reimprime "por lo que sale una hoja": esa es la frase de margen que repiten todos los ads del original (*casi todo es ganancia*).
- **El ángulo es bizop, no manualidades.** La promesa no es "hacé flores de papel", es **plata extra desde casa sin stock y sin envíos**: feria, escuela, bazar de la iglesia, pedidos por WhatsApp.
- **La app es el diferencial de la oferta** ("no te llevás solo los imprimibles, te llevás el negocio armado"): pantallas de Precios, Pedidos y Guía.
- **Estacionalidad:** el original empuja Navidad ("las fiestas no esperan"). El V6 de nuestra tanda es el guion largo de Navidad.

## El original (12 ads transcriptos)

- Material en `~/Desktop/calendarios-2027-en/work/`: los 12 videos (`original-es/`), `urls.tsv` y `transcripciones.json` (duración + texto de cada uno, ordenados por impresiones).
- **Qué usa de visual el original:** renders del propio producto (los calendarios-florero), impresora de casa, tijera, mockups de la app en español, mockups de WhatsApp y **dos UGC hablando a cámara** (una señora de canas y una chica joven). Subtítulos de 2–3 palabras en caja blanca.
- **Lo que nosotros no tenemos:** las imágenes del producto. Hasta que existan los 50 diseños propios, el visual sale 100 % de TikTok.

## La tanda 1 de ads (2026-11-04)

Seis videos de voz en off, en `~/Desktop/calendarios-2027-en/anuncios/`:

| Ad | Duración | Ángulo | Hook en pantalla |
|----|----------|--------|------------------|
| CAL-V1 | 0:30 | feria artesanal, se agotó el primer día | SOLD OUT ON DAY ONE AT THE CRAFT FAIR |
| CAL-V2 | 0:29 | las mamás de la escuela | THE SCHOOL MUMS TOOK EVERY ONE |
| CAL-V3 | 0:23 | oferta directa (50 diseños + la app) | 50 DESIGNS + THE APP THAT PRICES THEM |
| CAL-V4 | 0:28 | 61 años y un desastre con la computadora | 61, HOPELESS WITH COMPUTERS, STILL SELLING |
| CAL-V5 | 0:26 | lo que vendí este fin de semana | WHAT I SOLD THIS WEEKEND |
| CAL-V6 | 0:57 | historia larga de Navidad | THESE CALENDARS PAID FOR CHRISTMAS DINNER |

- **Guiones (inglés + español con voseo):** `OUTPUTS/2026-11-04-guiones-calendarios-2027-ingles.md`.
- **Voz:** Sulafat en Google AI Studio, `style_en.txt` de mujer norteamericana de unos cuarenta, a **speed 1.30** (ver [[ugc-y-video-generativo]]).
- **Montaje:** `OUTPUTS/scripts-vsl/edit_cal.py` + `gen_cal_plans.py`. Paleta propia: **ámbar #EFA93C** en la caja de hook, el botón y la palabra que suena; **verde hoja #15694A** en los chips; crema #FBF7F0 en la placa final.
- **Placa final (provisoria):** `2027 CALENDAR PACK · 50 PRINTABLE DESIGNS · PRICING APP`. **Falta que Santiago confirme el nombre, el precio y el checkout.**

## El pool de TikTok (lo que sirvió y lo que no)

- **Dos intentos fallidos antes de acertar.** Primero se barrió el tag `printablecalendar`: la mitad es **impresión 3D** (calendarios perpetuos en PLA, relojes flip) más chicos bailando. Después se buscó por las *escenas del guion* (`popupcard`, `paperflowers`, `craftfair`, `epsonecotank`) y salieron 23 clips lindos de flores de papel, tijera y feria **en los que no se veía un solo calendario**. Santiago lo cortó en seco: *"no hay un puto calendario"*. Los dos pools se tiraron enteros.
- **Lo que sí funciona:** `deskcalendar`, `diycalendar`, `papercalendar` y `handmadecalendar`. De 166 candidatos bajaron 147 y **quedaron 17 ventanas de 15 clips** (`anuncios/work/tiktoks3/`).
- **Los hallazgos:** `7679474945889455380` es un calendario de papel con forma de **florero con un ramo**, en caballete, con **2027** impreso — es el producto. `7585091358939942166` son tulipanes de papel parados sobre la base de un calendario. `7466996351692295431` son calendarios chicos de escritorio con flores que se abren. Esos tres son la espina dorsal de los seis ads.
- **Hay material 2027 en TikTok** (`7682732880446934292`, `7688575999272963336`, `7685253422047825172`, `7674237279988174100`): conviene buscarlo antes que conformarse con 2026, porque un año viejo quemado en el producto mata el ad.
- **tikwm rate-limitea:** en paralelo de a 5 fallan 7 de cada 10. De a uno con `sleep 1.6` anda. Y si corre una segunda tanda mientras se renderiza, **pisa un .mp4 a medio bajar y el render muere** con `AttributeError: 'NoneType' ... Duration`.

## Preguntas abiertas

- Nombre comercial, precio y checkout en inglés (la placa final está con un nombre provisorio).
- Los 50 diseños propios: sin ellos no hay producto ni imágenes de producto para la landing.
- La app de precios/pedidos: ¿se replica o se reemplaza por otro bonus?
- Landing y quiz: todavía no existen.

## Relacionado

[[guiones-y-anuncios]] · [[ugc-y-video-generativo]] · [[estilo-de-video-ia]] · [[internacionalizacion]] · [[caza-de-ofertas]] · [[drawing-world]] · [[365-actividades-imprimibles]]

## Fuentes

- RAW/ — (la oferta entró por la Biblioteca de Anuncios, sin archivo en RAW)
- ~/Desktop/calendarios-2027-en/work/transcripciones.json
- OUTPUTS/2026-11-04-guiones-calendarios-2027-ingles.md
