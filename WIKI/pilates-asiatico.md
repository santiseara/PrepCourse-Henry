# Pilates Asiático (oferta nueva AR)

> Clon de **Sana Pilates**, la ballena del nicho en Argentina: reto de 28 días de "pilates asiático" para mujeres +40, con quiz. Mercado Argentina, en pesos. ⚠️ **Es la misma oferta que [[pilates-hormonal]]**, que ya está armada desde el 12/10: no hay que construirla, hay que relanzarla. (fuente: relevamiento del 2026-11-09, `OUTPUTS/2026-11-09-analisis-pilates-asiatico-sana-pilates.md`)

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
