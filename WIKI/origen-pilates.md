# Origen Pilates

> Oferta propia AR de pilates asiático, clon mejorado de **Sana Pilates**, la ballena del nicho en Argentina: reto de 28 días de "pilates asiático" para mujeres +40, con quiz. Mercado Argentina, en pesos. ⚠️ **Es la misma oferta que [[pilates-hormonal]]**, que ya está armada desde el 12/10: no hay que construirla, hay que relanzarla. (fuente: relevamiento del 2026-11-09, `OUTPUTS/2026-11-09-analisis-pilates-asiatico-sana-pilates.md`)


## ✅ Decisiones tomadas (2026-11-09)
| | |
|---|---|
| **Nombre** | **Origen Pilates** (eligió la opción 3 dada vuelta). El mecanismo "Pilates Asiático" se mantiene en el copy |
| **Precio** | **$7.999 ARS**, igual que Sana Pilates |
| **Carpeta** | `~/Desktop/origen-pilates/` con `imagenes/`, `landing/` y `anuncios/` |
| **Tanda 1** | **5 videos con avatar IA + 2 de voz en off** (Santiago pidió 7; el tope habitual son 6) |
| **Herramienta de video** | **Veo 3.1** por [[apimart]] — créditos pagados por Santiago el 9/11 en la cuenta de Juan |

### La receta de video que quedó validada (9/11)
- Modelo **`veo3.1-fast`**, `duration: 8`, `aspect_ratio: "9:16"`, `generation_type: "frame"` con una imagen de referencia. **US$0,14 por toma de 8 s.**
- **Las imágenes salen de `gemini-nano-banana-2.1-ext` en el mismo ApiMart: US$0,014 cada una.** Un retrato por personaje, y para una escena con dos personas se genera una **imagen de escena** pasando los dos retratos como `image_urls`.
- 🆕 **La subida de imágenes va por `POST /v1/uploads/images` de ApiMart** (multipart, campo `file`, devuelve `url` en la raíz). No hace falta catbox ni ningún host de terceros. `image_urls` **sólo acepta http/https o `asset://`**: un data URI en base64 lo rechaza con 400.
- **Un clip de 8 s entra 23 a 25 palabras.** Medido: 23 palabras ocuparon de 0,11 a 7,35 s. Por eso un video de 6 tomas son **~130 palabras y ~48 s**.
- **El prompt que da buen lipsync y manos correctas** fija, en este orden: la acción y el encuadre · la línea entre comillas · "Only this woman speaks" · "These are the ONLY words spoken in the whole video, exactly as written, in this order" · qué hace después de la última palabra · "Argentinian Rioplatense Spanish with a Buenos Aires accent" + "accurate lip sync perfectly matched to every word" + "anatomically correct hands with five separate fingers" · "Keep her exact face, hair, clothes and the exact room from the reference image" · cámara estática · "Audio: only these exact spoken words and quiet room ambience" · "No subtitles, no captions, no text, no logos and no watermark".
- Salida real: **720×1280, 24 fps**, audio AAC 48 kHz. El clip de prueba salió con **manos correctas, cara estable y sin texto quemado**.

## ⚠️ No es una oferta nueva
Los **tres bonos de Sana Pilates coinciden palabra por palabra** con los de [[pilates-hormonal]] (Protocolo Anti-flacidez · Revelación lumbar cervical · Drenaje Linfático Express), igual que el reto de 28 días, el avatar de mujeres +40 en menopausia, el mecanismo de los músculos profundos del abdomen, la app, el planner y la garantía de 30 días. Pilates Hormonal ya era este clon. Lo que falta definir es **nombre, precio y la tanda de ads**.

## El ganador: Sana Pilates
| Campo | Valor |
|---|---|
| Página | `982998884899600` · **~92 anuncios activos en AR** |
| Antigüedad | El más viejo en circulación desde el **26/8/2026** — 75 días. Ballena |
| Copy | **Un solo primary text para los 92 anuncios.** No testean copy, testean video |
| CTA del link | "Obtener mi plan personalizado de Pilates Asiatico" |
| Quiz | **InLead** (`inlead.digital`) en `sanaspilates.com`, con cloaker (403 a curl) |
| Checkout | **Shopify** (`sanapilates.myshopify.com`), Mercado Pago, 3 cuotas |
| Precio | **$7.999 ARS**, ancla $39.000, 70 % OFF, 3 cuotas de $2.666 |
| Bonos | Anti-flacidez $18.000 · Revelación lumbar cervical $25.000 · Drenaje Linfático Express $15.000 |
| Garantía | 30 días |
| VSL | **No tiene.** Del quiz pasa directo a una página de oferta de texto con contador de 5:00 |

- **Están solos en la categoría:** un barrido de "pilates asiático / reto 28 días" en AR da 28 resultados y los 28 son suyos.
- **Perdieron un dominio con los ads corriendo:** los anuncios de agosto a octubre apuntan a `sanapilates.com`, que hoy es un **dominio parkeado de GoDaddy**. Los de noviembre ya van a `sanaspilates.com`.

## El quiz (17 pasos)
Portada = 1ª pregunta (edad: 39-45 / 46-50 / 51-60 / 60+) · puente "No estás sola, +1.2 millones" · objetivo principal · puente "solo 10 minutos" · objetivo adicional (multi) · áreas que preocupan (multi con fotos) · punto de partida (con fotos) · cuerpo de tus sueños (5 con fotos) · hace cuánto estuviste en tu mejor forma · puente educativo del mecanismo · qué tan cómoda al ejercitar · altura (slider) · peso actual (slider) · peso objetivo (slider) · qué es lo más importante (multi) · síntomas de menopausia (multi) · **carga de 15 s con testimonios firmados por ciudad argentina** · plan recomendado · oferta.

### Lo que hace bien
- La portada ya es la pregunta: el primer toque es una respuesta, sin botón "Empezar" (igual que Calistenia Militar en [[tai-chi-fit]]).
- **La pantalla de carga con testimonios firmados** (Mariela G. de CABA, Graciela R. de Córdoba) convierte 15 segundos muertos en prueba social local. Es lo mejor del quiz.
- Las fotos de cuerpo en tres pasos seguidos: elegir es mirarse, no leer.
- Los sliders cierran con una nota de IMC y le dan aire de diagnóstico.

### Lo que hay que mejorar al clonarlo
1. **El idioma baila**: conviven "para vos", "Consigue", "Puedes elegir", "para **usted**", "Si sientes", "Para ti: GRATIS". Es un quiz traducido del portugués y argentinizado a medias. El nuestro va en **voseo cerrado**.
2. **Faltan tildes por todos lados** ("dias", "asiatico", "¿Cual", "interes", "Revelacion"). En salud para mujeres de 50 eso baja la credibilidad.
3. **Los sliders arrancan en 180 cm y 70 kg**, valores de hombre promedio. Van en 160 cm y 72 kg.
4. **El peso objetivo no calcula nada**: falta la **previsión con fecha** (lo que sí hace [[dancego]]).
5. **El resultado no es personalizado**: después de 16 preguntas el plan es el mismo para todas y la oferta no repite una sola respuesta.
6. **No hay VSL** — el hueco más grande del embudo y justo donde tenemos pipeline ([[vsl-reglas-de-armado]]).
7. El contador de 5:00 y "quedan 7 lugares" se contradicen con "congelás tu precio para siempre".
8. Paleta violeta de plantilla de InLead (`#8b5cf6` sobre `#fafaf9`) y logo con fondo recortado a mano.
9. El paso "hace cuánto estuviste en tu mejor forma" no personaliza nada (es el mismo que sacamos de [[dancego]]).

## Las 6 familias de ads
| Familia | Largo | Qué es | Cómo está hecho |
|---|---|---|---|
| **A · Mosaico de píldoras** | 25 s a 1:15 | 3 a 5 micro-clips de 5-10 s, cada uno con otra mujer y otra frase | UGC real |
| **B · Entrevista en la calle** | 25 s a 1:00 | "¿Cuántos años tenés?" / "Che, ¿vos entrenás?" | Real, cámara en mano |
| **C · Historia de vida** | 1:55 | El ex marido en la cola del súper con la novia nueva | Testimonio + b-roll |
| **D · Mini-novela actuada** | 4:03 | El marido que se va a la fiesta sin ella; la hija la levanta | Actuado, personas reales |
| **E · VSL-ad educativo** | 2:46 a 4:03 | "El truco de las asiáticas"; el error del gimnasio; los músculos que se apagan | **Avatar IA** en cocina + clips reales + anatomía 3D |
| **F · Celebridades argentinas** | 1:47 | Clips de TV: "no tengo metabolismo, tengo disciplina" | **Avatar IA** + clips de TV |
| **G · Diario Día 1 → Día 28** | 1:15 a 3:58 | "Me llamo Marta, tengo 63 y hoy empiezo" → "este es el día 59" · "Día 1: me sentí ridícula sola en mi habitación… Día 28: fui a la playa sin esconderme" | Antes/después en el mismo plano |
| **H · Sketch de humor** | 2:08 | El vecino y "una mano con la pileta" · "tres meses en la cinta y estás igual" · "Ma, ¿ya te acostumbraste a tener panza?" | Actuado, humor argentino |

### 🧬 El hallazgo: no escriben guiones, permutan píldoras
Tienen un **banco de unas 15 píldoras de 5 a 10 segundos** y arman videos pegándolas en órdenes distintos, siempre con el **mismo bloque de oferta al final**: *"Arrancó la promoción de Sana Pilates y va a estar disponible solo hasta este viernes. Durante estos días podés conseguir todo el programa por solo 7.999 pesos."* El video de 4 minutos es la novela + seis píldoras encadenadas. **Por eso tienen 92 anuncios con un solo copy: el creativo es combinatoria, no escritura.**

Frases que se repiten palabra por palabra entre videos distintos: *"Esto es lo que hacen mis alumnos todos los días, 5 minutos desde casa"* · *"6 kilos menos en 28 días… no hay gym, no hay dietas raras, todo acá en mi living y en mi mat"* · *"¿Cuántos años tenés? Mirá, estoy vieja, 62 años"* · *"¿Cómo se siente tener 53?"*.

### Dos datos que importan
- **La familia G ya es el formato Día 01 / Día 49** que quedó fijado en [[estilo-de-video-ia]] el 4/11 a partir del ad brasileño: la ballena argentina ya lo corre y es uno de sus videos más entregados.
- **Usan estacionalidad y nosotros no:** *"si querés que la grasa del vientre desaparezca antes del verano"*. Estamos en noviembre: el pre-verano argentino es una ventana que se cierra sola y no hay que inventarle escasez. Va en la tanda.

### Lo que NO se copia
Sus claims son durísimos y son exactamente los que bloquearon cuentas en [[profesional-digital]]: *"bajé 12 kilos"*, *"del talle XL al M"*, *"en 7 días adelgazás"*, *"mirá esta panza"*. **Nuestra tanda va sin kilos, sin plazos de resultado y sin segunda persona sobre el cuerpo de quien mira** ([[pilates-hormonal]], [[problemas-de-cuentas-meta]]). Y el ad de celebridades **nombra personas reales** (Valeria, Pampita, Araceli, Andrea) con clips de TV: el ángulo sirve, los nombres y los clips no.

## El nicho en Brasil (2026-11-09)
- **"21 Day Challenge" — 241 ads activos: NO es modelo.** Es **BetterMe** (`betterme-fitness-coaching.com`), app global por suscripción que corre varios idiomas y nichos a la vez. Se descarta por el filtro de [[caza-de-ofertas]].
- **"Calistenia Japonesa 28 Dias"** (`1317407098122729`): **50 ads activos, todos del 4 al 8 de noviembre.** Arrancó hace cinco días. Mismo molde (método oriental + 28 días + quiz) y **anuncios 100 % mini-novela 3D estilo Pixar con IA**: el marido que apaga la luz · el del avión que pide cambiarse de asiento · el probador de vestidos. Cierre con chapita roja **"Toca na tela!!!"**. Ver [[mini-novela]] y [[estilo-de-video-ia]].
- **"Camila Oliveira"** (`1521598694360583`): 14 ads arrancados el 9/11, con el **ángulo de la vergüenza** que falta en Argentina: *"Treine escondida. Apareça pronta."* · *"Deixa eles falarem. Faz o teste."* · *"O problema nunca foi o seu número."*
- **Lectura:** en Brasil el nicho ya pasó del UGC a la novela 3D con IA, y el gancho se corrió del cuerpo a **la mirada de los otros**. En Argentina, Sana Pilates sigue en UGC real + escalera de kilos. Hay un mercado de diferencia para aprovechar.

## Plan de ads (tanda de lanzamiento: 6 videos, 3 carriles)
No es "IA o voz en off": son dos carriles distintos, y **el que no podemos copiar es el que ellos corren mejor** (familias A y B, UGC real con caras filmadas).
1. **Mini-novela 3D con IA ×2** — lo que escala en Brasil y lo que Sana Pilates **no tiene**. Escenas de mirada ajena, no de kilos.
2. **Avatar IA a cámara, 90 s ×2** — la familia E con cuerpo propio, siguiendo las 8 reglas de [[estilo-de-video-ia]].
3. **Voz en off sobre clips de TikTok ×2** — el carril barato: `speed 1.30`, cortes de 1,9-2,9 s. Tags a medir: `#pilatesencasa`, `#pilatesparede`, `#pilatesmujeres40` y en portugués `#pilatesemcasa`.

**Se copia de su edición:** el bloque de oferta fijo al final con **fecha y no con precio**, los subtítulos karaoke, la placa de marca de cierre, y la lógica de banco de píldoras para renovar barato.


## Tanda 1 de ads y quiz (2026-11-09)

### Los 7 videos · `~/Desktop/origen-pilates/anuncios/`
| # | Formato | Largo | Escenas |
|---|---|---|---|
| 9-11 - 1 | avatar IA | 34,6 s | pizarrón "ABDOMEN PROFUNDO" · profe en su living · clase en terraza · presentadora |
| 9-11 - 2 | avatar IA | 34,5 s | día 1 (hija filmando, la madre atrás) · día 28 · abuela con la nieta · presentadora |
| 9-11 - 3 | avatar IA | 41,9 s | Ana en su casa (3 tomas) · clase en terraza · abuela con la nieta · presentadora |
| 9-11 - 4 | avatar IA | 34,9 s | pizarrón (la rodilla) · estudio · clase en terraza · presentadora |
| 9-11 - 5 | avatar IA | 35,6 s | balcón porteño · abuela con la nieta · presentadora (3 escenas) |
| 9-11 - 6 | voz en off | 36,1 s | b-roll de TikTok, 8 familias visuales |
| 9-11 - 7 | voz en off | 34,0 s | b-roll de TikTok, mismo pool con otro seed |

Guiones en `OUTPUTS/2026-11-09-guiones-origen-pilates-tanda-1.md`. **Costo total de ApiMart: US$4,90.**

### 🧬 La estructura que se calcó (del despiece de sus videos cortos)
Su ad de 53 s son **4 escenas + placa**; el de 75 s, **7 escenas + placa**. Cada escena es otra mujer en otro lugar, y **el bloque de oferta lo dice siempre la misma presentadora del living**, al final de todos los anuncios. Reglas que salen de ahí y que ahora son el molde de esta oferta:
- **Máximo 4 escenas por video** (regla de Santiago del 9/11). Una escena puede tener 2 o 3 tomas.
- **Cada video arma con escenas distintas**: algunos de antes/después, otros con las que ellos usan (pizarrón, testimonio al espejo, clase grupal, entrevista en la calle, dos generaciones).
- **Caja roja de hook** sobre los primeros 6 s, blanca en itálica, como su "5 EJERCICIOS / Y SE VAN A ARREPENTIR / DE CRITICAR".
- **Una sola toma de cierre reusada en los 5 videos**: la presentadora con el bloque de oferta, con fecha y sin precio.
- Repertorio de escenas: pizarrón casero · profe en su living · testimonio con nombre y ciudad · clase grupal en terraza · entrevista en la vereda · abuela con la nieta · presentadora · placa de marca.

### ⚠️ El filtro de contenido de Veo
Rechaza (`content_policy_violation`, y **no cobra**) las referencias con **ropa ceñida o de color piel** y las escenas de **una mujer sola en un dormitorio** o de **un hombre fuera de cuadro abordando a una mujer en la calle**. Se cayeron el testimonio al espejo (3 tomas) y la entrevista en la vereda (2). Con ropa holgada y en otro ambiente pasan: la presentadora salió recién al rehacerla con remera blanca y jogging. **Regla: las imágenes de referencia van siempre con ropa holgada y cubierta.**

### Ajuste del 9/11 (pedido de Santiago, sin regenerar nada)
*"metele 1.2 de velocidad, cortame los silencios y poneme una música activa que se escuche bien."* Se re-montó desde las tomas ya generadas:
- **`speed 1.2`** en video y audio juntos (el lipsync se mantiene), silencios de más de 0,26 s recortados a 0,12 s a −38 dB.
- **Cama `bed_activo`** (la misma que DanceGo, Quesos y Nail Designer, md5 idéntico): medida en **85 % de graves, pulso 0,64 y 135 onsets/min**. Va a −12 dB con `sidechaincompress`, así que baja sola cuando alguien habla.
- **Niveles normalizados**: los cinco a pico −1,3 dB (antes iban de −5,8 a −11,4 y algunos se oían flojos). Media entre −18 y −23 dB, el rango de los de Sana Pilates.
- Los subtítulos se **re-alinean contra el audio ya acelerado**, no se estiran.

### ⚠️ Cazar b-roll de pilates en TikTok: 191 clips para 8 limpios
Santiago rechazó la primera versión de los dos ads de voz en off: *"son muy malos, clips horribles, muy poco variado, todo repetitivo"*. Tenía razón: el pool era de 6 clips para dos videos y se compartían.

**Medición de los cinco tags**, 191 clips bajados en total:

| Tag | Bajados | Limpios |
|---|---|---|
| `#pilatesencasa` | 70 | 6 |
| `#pilatesmenopausia` + `#pilatesmujeres40` | 75 | 0 |
| `#wallpilates` + `#pilatesathome` | 47 | 6 |

**El nicho de pilates está tomado por creadoras que queman el título de la rutina en pantalla** ("Elbow Sliders 10 reps", "WALL PILATES WORKOUT", "Bridge Lifts 30 reps"), en todos los idiomas. `#pilatesemcasa` en portugués **se solapa casi entero** con el tag en español, así que la regla del 8/11 ("buscar el mismo producto en otro idioma") **no aplica acá**: el solapamiento de TikTok la anula.

Lo que sí sirvió:
- **Los tags de pilates en la pared y en inglés** (`#wallpilates`, `#pilatesathome`) rinden parecido al español, pero traen **planos de piso de cuerpo entero** donde no se lee la cara ni la edad, que es justo lo que necesita una oferta para mujeres de más de 40 (en TikTok de pilates casi todas las creadoras tienen 20).
- **Bajar con tres pases y reintentos.** tikwm entrega de a poco: en un pase da 12 de 75, en tres da 47 de 49. Hay que dejarlo correr y volver.
- **Pool final: 8 clips limpios en 8 familias visuales**, con la franja limpia anotada (`desde`/`hasta`) para saltear los segundos con cartel.

### El quiz · `~/Desktop/origen-pilates/landing/`
- **Sin VSL** (pedido del 9/11): se sacaron el player de Panda, el `<template id="vsl-template">` y el JS que lo cargaba. **`SEGUNDOS_OFERTA: 0`** → la oferta se ve apenas se llega al paso 19. Copia en `OUTPUTS/2026-11-09-quiz-origen-pilates.html`, original en `quiz.html.bak`.
- **Precio $9.990**, 3 cuotas sin interés de **$3.330** (ancla coherente $33.300 con el 70 % OFF).
- **Las 29 imágenes se rehicieron de cero** (las del quiz de [[pilates-hormonal]] no existían en disco) y quedaron en `landing/img/`, con el mapa `IMAGENES` apuntando ahí:
  - **17 por código, a costo cero** (`OUTPUTS/scripts-vsl/` no; el script quedó en el scratchpad): logo de loto de 8 pétalos con "ORIGEN PILATES / Método Asiático" en PNG transparente, las 5 siluetas de zonas con el círculo del acento, las 3 de punto de partida y las 5 de cuerpo deseado con anchos bien diferenciados, el mockup de la app (reto día 11 de 28), la placa del Pase VIP y el sello de pago seguro.
  - **12 fotos con `gemini-nano-banana-2.1-ext`** (US$0,014 c/u): mujeres argentinas de 45 a 65 en departamentos porteños reales, ropa holgada.

### ✅ Quiz cerrado y entregado (9/11, segunda vuelta)
Santiago pidió *"el txt del quiz"* y *"una descripcion para los ads"*. Antes de generar el .txt se cerraron los tres pendientes del quiz:
- **Checkout propio y verificado:** `https://origen-pilates.impultienda.ar/checkout` devuelve **200**. Los 4 CTAs del paso 19 (2 botones + los 2 cuadros de precio) pasan por `comprar()` → `CONFIG.LINK_CHECKOUT` + UTMs. Ninguno muerto.
- **Voseo cerrado:** se sacaron las 20 formas de tuteo que quedaban del original traducido (*comenzaron como tú · Elija · Puedes elegir · te sientes · Arrastre · para usted · tienes · te llevas · congelas · aseguras · Para ti · Si sientes · Consigue*) y se repusieron las tildes que faltaban (*dias · asiatico · Cual · interes · energia · Revelacion · guia · gluteos · pelvico · Explicacion · Como · segun*).
- **Claims de kilos afuera:** se cayó *"Silvia, de 75 a 71 kg en 28 dias"* (ahora *"Silvia, 54 años · reto de 28 días completo"*) y *"Consegui resultados visibles en 28 DIAS"* pasó a *"Empezá hoy tu reto de 28 DÍAS"*. Sin plazo de resultado y sin cifra de peso.
- **Testimonios argentinos, no italianos:** las cuatro reseñas venían con nombres del clon (Francesca Rossi, Laura Bianchi, Martina Conti, Silvia Romano). Ahora van con nombre + ciudad: Marcela F. (Rosario), Alejandra P. (Mendoza), Verónica S. (La Plata), Silvia R. (Mar del Plata). 👉 **Regla: un clon trae los nombres propios del mercado de origen y no saltan leyendo el HTML, saltan recorriendo el quiz.**
- **Sliders a valores del avatar:** 160 cm / 72 kg actual / 65 kg objetivo (venían en 180 cm y 70 kg, valores de hombre promedio).

**Entregables:** `landing/origen-pilates-quiz.txt` (**1,24 MB**, 29 imágenes embebidas, listo para pegar en ImpulTienda), `landing/origen-pilates-PRUEBA.html` y copia en `OUTPUTS/2026-11-09-quiz-origen-pilates.html` (+ el fuente con rutas `img/` en `-fuente.html`).

**Probado los 19 pasos** en un iframe de 390 px: 29 imágenes sin romper, cero overflow horizontal (`scrollWidth` 390), la carga de 15 s pasa sola al paso 18 y la oferta se ve al entrar al 19 (`SEGUNDOS_OFERTA: 0`).

### La descripción de los ads (una sola para la tanda)
`anuncios/descripcion-ads.txt` y `OUTPUTS/2026-11-09-descripcion-ads-origen-pilates.md`. **177 palabras**, el formato corto del 6/11. Igual que Sana Pilates, que corre **un solo primary text para sus 92 anuncios**: el creativo es la variable, no el copy.
- Abre por el mecanismo (*el ejercicio equivocado · los músculos profundos del abdomen que se apagan*), 3 bullets, una línea de entregables, una de bonos, una de garantía y CTA al test gratis.
- **Sin precio** (el precio lo dice el paso 19), **sin kilos, sin plazo de resultado y sin segunda persona sobre el cuerpo de quien mira**: se habla de *"el cuerpo"*, nunca de *"tu panza"*.
- Cierra con la **estacionalidad** que ellos usan y nosotros no: *"Falta un mes para el verano"*.

### Pendientes
- Las dos escenas que rechazó el filtro (espejo y entrevista) quedan para la tanda 2.
- **El peso objetivo sigue sin calcular nada**: falta la previsión con fecha que sí hace [[dancego]].
- **El resultado no es personalizado**: después de 16 preguntas el plan es el mismo para todas.
- Falta el **VSL** (hueco #6 del embudo).

## Decisiones abiertas
- **Nombre.** Propuestas: **Kaizen Pilates** (recomendada), Pilates Hana, Pilates Origen. El mecanismo "Pilates Asiático" se mantiene en el copy. Evitar "sana", "zen" y "wellness".
- **Precio.** Ellos están a $7.999 hace 75 días: el mercado está calibrado ahí. [[pilates-hormonal]] estaba fijado en $14.990, **87 % más caro que el único otro jugador**. Recomendación: **$7.999, ancla $39.000, 3 cuotas**.
- Checkout (ImpulTienda) a confirmar.
- ¿Se reusa el guion de VSL de [[pilates-hormonal]] o se escribe de nuevo contra el mecanismo del abdomen profundo?

## Relacionado
[[pilates-hormonal]] · [[estilo-de-video-ia]] · [[mini-novela]] · [[quizzes-reglas-de-armado]] · [[quiz-funnel]] · [[dancego]] · [[tai-chi-fit]] · [[caza-de-ofertas]]

## Fuentes
- Biblioteca de Anuncios de Meta, página `982998884899600` (Sana Pilates), relevada el 2026-11-09: 22 videos bajados, 12 transcriptos
- Quiz `sanaspilates.com`, recorrido paso por paso el 2026-11-09
- Biblioteca de Anuncios, páginas `420362471161663`, `1317407098122729` y `1521598694360583` (Brasil)
- `OUTPUTS/2026-11-09-analisis-pilates-asiatico-sana-pilates.md`
