# Pack Tesoro del Soldador (oferta LATAM)

> Clon para LATAM de **Welder's Treasure Pack** (`welders-treasure.online`, página de Meta "Daniel Brooks"): biblioteca digital de **más de 4.000 planos de herrería** listos para construir y vender, con medidas, listas de corte, costo y precio sugerido, más 4 bonos. Ellos corren en 🇺🇸 🇫🇷 🇩🇪 🇮🇹 y **cero en español**, así que LATAM está libre. (fuente: pedido de Santiago del 2026-11-27)

## Ideas clave
- **Pedido de Santiago:** *"Quiero que hagamos exactamente lo que a ellos les está funcionando. No nos inventemos guiones, no nos cambiemos cosas. Pongamos exactamente las mismas palabras que utilizan ellos en todo."* Tanda de **10 anuncios de testeo**, español **neutro** (no voseo), copiando su edición y agregando **una musiquita baja**.
- **Nombre del producto en español: "Pack Tesoro del Soldador"** (lo fijó Santiago el 27/11).

## Su biblioteca de anuncios (medida el 2026-11-27)
- **493 anuncios activos**, **163 videos únicos** (los 162 que se pudieron bajar están transcriptos).
- Idiomas por URL de destino: **fr 170 · en-us 115 · de 102 · it 96 · en-37-1p 9**. Ninguno en español.
- Fechas de arranque de los videos: 9 el 7/10, 18 el 16/10, 5 entre el 29 y el 30/10 y **110 entre el 19 y el 26/11**.
- 330 de los 493 anuncios son **estáticos**; 163 llevan video.

### ⭐ La señal más fuerte: los 9 guiones madre
Los **9 videos en inglés del 7 de octubre** son los mismos **9 que tradujeron al francés y al alemán el 16 de octubre**. Es lo único que tradujeron tres veces y siguen activos siete semanas después. Esos nueve son la DNA validada:
1. "Cuando un cliente te pregunta qué modelos tenés, no podés improvisar."
2. "Estaba buscando unos modelos de portón y me encontré con un pack entero."
3. "Desde que tengo el pack nunca más me quedé sin ideas de qué construir y vender."
4. "Mientras perdés tiempo sacando cada medida a mano, otros ya están cortando y soldando." ← uno de los 3 que mandó Santiago
5. "Dejame mostrarte algo que todo soldador debería tener." ← **avatar**, uno de los 3 que mandó
6. "Buscar planos de herrería en internet parece fácil, hasta que…" ← uno de los 3 que mandó
7. "Saber soldar no siempre es el problema; el problema es saber qué ofrecer."
8. "¿Todavía perdés horas sacando medidas y dibujando planos desde cero?"
9. "Si soldás o trabajás el metal, mirá esto."

La ola del 19 al 26/11 (unos 110 videos) es **un solo ángulo repetido**: *el cliente te pide algo que no tenés y perdés el trabajo* (pérgola, quincho, carport, mesa industrial, escalera, baranda, fogonero). El más repetido ahí —2 copias en inglés más versión en francés— es **"imaginate que un cliente te pregunta si hacés pérgolas y, en vez de decirle que lo vas a averiguar, le abrís el plano con las medidas ahí mismo"**, que entró como guion 10.

## Su oferta (landing `welders-treasure.online/en-us/`)
- **Kit Básico US$ 9** (3.000+ planos) y **Kit Profesional US$ 30 → US$ 17 hoy** (4.000+ planos, 300 de portones y rejas, remolques, carrocería, 600 de muebles industriales, 500 de estructuras y galpones, 50 de parrillas, 100 de equipamiento de gimnasio).
- **4 bonos:** guía para presentar muebles de caño, guía completa de precios de muebles industriales, los 10 errores del soldador principiante, tipos de acero y sus usos.
- Garantía de 7 días, pago único, acceso inmediato por mail, contador de oferta.
- Cada plano trae: medidas exactas, lista de materiales, diagrama de corte, perfil y espesor, orden de armado, costo de producción, precio sugerido y ganancia estimada.
- 🔎 Existe un espejo en `tesoro-del-herrero.vercel.app` (en inglés, sin ruta /es): el nombre en español ya se lo reservaron, pero **todavía no tiran en el idioma**.

## Su edición (medida sobre los 162 videos)
- 23 a 42 s, 9:16, **voz en off de hombre grave: F0 105-136 Hz** (la nuestra quedó en 122-141).
- 100 % b-roll del oficio. Cortes de 1 a 2 s.
- **Subtítulos** de 2-3 palabras, mayúscula, blancos con borde negro, la palabra que suena en **amarillo**, sin caja, centrados a **0,78 del alto** (en los de avatar, a 0,69).
- **Fichas de plano**: grabación de pantalla del PDF sobre fondo gris oscuro, con barra naranja "WELDER'S TREASURE PACK | PROJECT 06", título, vistas frontal/lateral/superior, "CUT LIST & MATERIALS", "BUILD STEPS" numerados en naranja y "FINISH".
- **Mockup** del pack con resplandor, una o dos veces, y al final otra vez con el CTA.
- Formato con cara: **el avatar va recortado abajo a la derecha**, filmado contra pantalla verde y keyeado — sin recuadro y sin fondo propio. Medido con Vision sobre sus cuadros: en 720x1280 la silueta va de x 408 a 719 (pegada al borde derecho) y de y 840 a 1279 (pegada al piso). No es un talking head.
- Cierran con grabación de pantalla de la landing.

## Lo que hicimos (tanda 1, 2026-11-27)
- **10 guiones** en español neutro: `OUTPUTS/2026-11-27-guiones-tesoro-del-soldador-LATAM.md`. Traducción casi literal de los 9 madre + el de la pérgola.
- **Voz:** Orus por API. ⚠️ Con `gemini-2.5-flash-preview-tts` y el estilo normal salió a **145-153 Hz**, más fina que la de ellos. La que calzó es **`gemini-3.8-flash-tts` con un bloque de estilo que pide voz grave de pecho**: da **121-141 Hz**. Ese modelo **lee el estilo en voz alta**, así que se corta con `voz/cortar.py` (Whisper busca la última aparición de las primeras palabras del guion). Ritmo final 185 ppm.
- **Mockup en español:** `imagenes/mockup-pack-tesoro-del-soldador.png`, hecho **editando el PNG original de ellos** (1254×1254 con transparencia) con `ref/mockup_es.py`: tapa cada texto con el percentil de luminancia de su propia fila y lo redibuja en español. La tabla chica de materiales quedó en inglés a propósito (a tamaño de anuncio mide 1 mm).
- **6 fichas de plano propias** en español y en milímetros (`fichas_es/gen_fichas.py` + `pantalla.py`): portón corredizo, portón de dos hojas, baranda de escalera, remolque de dos ejes, pérgola de acero y mesa industrial pata X. Se entregan como clip de "grabación de pantalla" con fondo gris, sombra, inclinación de 1,1° y desplazamiento lento.
- **B-roll:** 1.050 TikToks de 7 tags (`herreria`, `soldadura`, `portones`, `estructurasmetalicas`, `muebleindustrial`, `trailercasero`, `pergolametalica`), 210 bajados, **39 limpios** después de OCR (Vision), detector de caras (Vision), bandas negras y nitidez.
- **Avatar:** HeyGen **Avatar IV**, 720p vertical, audio subido (no gasta voz). El personaje es **"VRF TECNICO sala de maquinas"**, el único de oficio que quedaba en la cuenta: el avatar "HERRERO" de [[herrero-de-finde]] **ya no está**.
- **Recorte del avatar (27/11, pedido de Santiago):** los dos videos con cara salían con la sala de máquinas del avatar metida en una cajita. Se recortó la persona con **Vision de macOS** (`scripts-vsl/recorte_persona.swift` + `avatar_recortar.sh`), sin volver a generar nada en HeyGen, y se ubicó con `avatar_ubicar.py` en la misma posición que el ganador (alto 660, tope en y=1260, pegado al borde derecho). V05: escala 0,715 en x=566 y=1005. V09: 0,716 en x=565 y=1004.
- **Editor:** `OUTPUTS/scripts-vsl/edit_soldador.py` (copia de `edit_acm.py`) con tipo de overlay `mockup`, capa de **avatar recortado** (bandera `key`) y subtítulo amarillo sin caja.
- **Música:** `atlasaudio-advertising-marketing-617541.mp3` (la de oficio y taller), preparada con `cama_acm.py`, a −11 dB con ducking de 5.

- **Descripción de los ads (27/11):** ellos corren **un solo texto principal y un solo título** en los 493 anuncios, traducido a los 4 idiomas. Se clonó literal al español neutro (`OUTPUTS/2026-11-27-descripcion-ads-tesoro-del-soldador.md`): título *"🔥 Más de 4.000 planos de herrería"* y body *"El pack que todo soldador debería tener en el taller"* + 3 ✅ + CTA. **Se sacó la línea del precio** (`Starting at $9`) porque el precio LATAM no está definido y la tanda sale multipaís; queda una variante con precio para cuando se fije y salga a un solo país.

## Preguntas abiertas
- Falta **landing, producto, bonos y backend**. El producto son 4.000 planos: hay que decidir si se compran, se arman o se clonan.
- Precio en LATAM sin definir (el de ellos es US$ 9 / US$ 17).
- El avatar es un técnico de aire acondicionado, no un soldador. Si Santiago quiere, se hace una foto nueva gratis (ChatGPT o Nano Banana) y se crea el avatar "SOLDADOR".

## Relacionado
[[herrero-de-finde]] · [[puertas-de-acm]] · [[guiones-y-anuncios]] · [[funnel-hacking]]

## Fuentes
- Biblioteca de Anuncios de Meta, búsqueda `welders-treasure.online` (27/11/2026)
- `welders-treasure.online/en-us/`
- Pedido de Santiago del 2026-11-27
