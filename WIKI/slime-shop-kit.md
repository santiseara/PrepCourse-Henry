# Slime Shop Kit — recetas de slime para mamás (mercado inglés)

> Clon en **inglés (US)** de **Mariana Williams Creations**, la página que corre el *Slime Shop Kit*: un kit de **70+ recetas de slime y masas sensoriales** con medidas exactas, listas de materiales y cómo venderlos. Oferta low ticket de **USD 19**. Nuestra tienda: `slimeshopkit.impultienda.ar`. (fuente: su biblioteca de anuncios + sus 17 creativos activos bajados el 18/11/2026)

## La oferta
- **70+ recetas probadas**: butter, cloud, clear, icee, glossy, play dough y cloud dough, con **medidas exactas** y la **lista completa de materiales** (todo de Walmart y Dollar Tree).
- **El ángulo no es el slime: es el negocito.** Barra de slime en un cumpleaños, frasquitos en la puerta del colegio, kits personalizados con el nombre del chico, talleres creativos, souvenirs de fiesta. El kit también enseña **cómo ponerle precio, empaquetar y vender**.
- **Números que repiten**: una tanda sale en ~10 minutos, cada frasco cuesta ~USD 2 de ingredientes, **5 bonos** incluidos, etiquetas imprimibles, descarga digital instantánea, sin experiencia previa.
- **Avatar:** mamá de habla inglesa con hijos chicos (o que trabaja con chicos) que quiere arrancar algo propio desde la mesa de la cocina, sin local, sin stock y sin plata inicial.

## Lo que hacen ellos (medido sobre sus 17 creativos activos, 31/10 al 16/11)
- **9:16, de 21 a 28 segundos.** Voz en off de mujer americana, cálida y rápida, con una cama musical por debajo.
- **100 % b-roll de slime**: manos, bowls, glitter, texturas. **Ni una cara hablando, ni una foto fija, ni una captura.**
- **Caja de hook blanca redondeada arriba**, texto negro bold en mayúscula, dos renglones, y se va cuando termina la primera frase.
- **Subtítulos de 3 palabras abajo**, mayúscula, blancos con borde fino y sombra, y **la palabra que suena en amarillo** (texto de color, no caja de color).
- **Sin placa final, sin chips, sin insertos de producto, sin SFX.** Cierra sobre el b-roll con el último subtítulo.
- **Un solo texto de anuncio** para todos los creativos, con el CTA "Tap Learn More".

## Lo nuestro (tanda 1, 2026-11-18)
Seis guiones en inglés + voseo (`OUTPUTS/2026-11-18-guiones-slime-shop-kit-tanda1.md`), uno por ángulo:

| # | Ángulo | Caja de hook |
|---|---|---|
| 1 | El slime como negocito | SLIME CAN BE YOUR NEXT LITTLE BUSINESS |
| 2 | La mesa de la cocina (el más cercano al de ellos) | THE LITTLE BUSINESS ON YOUR KITCHEN TABLE |
| 3 | Otras mamás ya lo están vendiendo | OTHER MOMS ARE ALREADY SELLING THIS |
| 4 | No necesitás un local | YOU DON'T NEED A STORE TO START |
| 5 | La experiencia, no el producto | KIDS LOVE IT. PARENTS PAY FOR IT. |
| 6 | Proyecto de fiestas (estacional) | A HOLIDAY PROJECT YOU CAN START THIS WEEK |

**Las visuales, con fuente (20/11):** los seis ads usan **38 de las 43 ventanas limpias**, de **28 cuentas de TikTok** distintas, y los 6 comparten el mismo pool (cambia el seed del orden de cortes). La cuenta y el link de cada clip se reconstruyeron desde `V1.json` (clave `cXX` → `src`), `pool_autores.txt` (autor/id) y `usage.json` (qué clips entraron de verdad): `OUTPUTS/2026-11-20-slime-shop-kit-links-visuales.md`. Los 6 masters están en Drive (*Ebook Dami / Ebook Slime Shop Kit (EN) / Videos terminados*), carpeta ya compartida con el socio como editor.

**Montaje:** `OUTPUTS/scripts-vsl/gen_slime_plans.py` (los 6 planes) + `edit_slime.py` (el render), con el pool de clips de TikTok en `~/Desktop/slime-shop-kit/anuncios/work/clips` y las ventanas limpias en `vent_slime.py`. Voces con Gemini TTS (Sulafat), velocidad 1.20.

## Renovaciones del ganador (tanda R, 2026-11-20)

El **01** ("Did you know slime and sensory dough can turn into your next little business?", 18,5 s) es el que mejor anda y ya trae ventas. Tres renovaciones con el **cuerpo y el CTA textuales** y **un formato de hook distinto cada una**, todas del mismo angulo (el negocito desde casa):

| # | Formato del hook | Caja de hook |
|---|---|---|
| R1 | Reaccion de un tercero | ANOTHER MOM ASKED ME WHERE I BOUGHT IT |
| R2 | Cuentas rapidas | TEN MINUTES. TWO DOLLARS. ONE JAR. |
| R3 | Declaracion contraintuitiva | SLIME ISN'T JUST A TOY ANYMORE |

Guiones (EN + voseo) y banco de 6 hooks de reserva: `OUTPUTS/2026-11-20-renovaciones-slime-shop-kit.md`. Montaje: `OUTPUTS/scripts-vsl/gen_slimeR_plans.py` + el mismo `edit_slime.py`. Masters en `~/Desktop/slime-shop-kit/anuncios/R*.mp4` y en el Drive.

**Como se cambio la estetica sin bajar un clip nuevo** (lo que pide el checklist del 27/10): la ventana de muestreo va **corrida media ventana** (`OFF 1.3`) y con **tope 8** en vez de 6, se reusa el `usage.json` de la tanda 1 (que penaliza x10 lo ya visto) y el ritmo de corte pasa de `[1.5, 2.0, 2.5]` a `[1.7, 2.2, 2.7]`. Resultado: **los 248 tramos del pool son todos nuevos**, ni uno coincide con la tanda 1.

## Lo que se aprendió armando esta tanda
- **La familia de un plano no siempre es la primera letra de la clave.** Este pool se numeró `c00…c83`, así que la regla de "no repetir fuente" se quedaba sin candidatos y el render moría con `min() arg is an empty sequence`. Ahora cada clip lleva `fam` = el autor de TikTok (53 autores entre 49 clips) y la regla compara por autor. Ver [[estilo-de-video-ia]].
- **El pool hay que pasarlo por OCR antes de montar, siempre.** De 84 ventanas, **35 se cayeron por texto quemado**: tutoriales en castellano y en inglés, marcas de agua que duran el clip entero (`SLIMEOWY`, `DK-ASMR`, `honeycomb asmr`, `SquishPaw`, `lionslimer`), un cartel de Play-Doh, un aviso de tienda ("fake snow particles may stick to hands") y hasta un teléfono de pedidos.
- **El OCR no alcanza: después hay que mirar el pool entero, un cuadro por clip.** Se cayeron **6 más** que el OCR dejó pasar: dos pibes en una cocina sin nada de slime, la cara de una creadora, una **marca de agua china** (`@有一只小猪 抖音视频 禁止搬运`, chiquita y abajo a la izquierda) y tres carteles de tienda que el OCR había mezclado con las etiquetas de los frascos ("Best Sellers Collection", "Pistachio Croissant", "pineapple"). Un séptimo clip se recortó: a los 22 s aparecía una **paleta de sombras**. **Pool final: 43 ventanas de 84.**
- **El OCR se saltea cuadros sin avisar.** Los clips de rango completo (full-range YUV) no escribían el JPG y `scan_carteles.py` los daba por "sin texto". Corregido con `format=yuv420p` + `-pix_fmt yuvj420p`.
- **Las etiquetas de los frascos NO se descartan**: "Orange Creamsicle Fluff", "Teddy Bear Fluff", "Peach Frozen Yogurt" son producto, y ellos también muestran frascos. Lo que se cae es la leyenda del creador y la marca de agua.
- **El TRIPODE DE FILMACION no lo caza ningun OCR, y el defecto es del CREADOR, no del clip (20/11).** En el primer render de las renovaciones aparecio un tripode negro asomando arriba en un plano de `c17`. Mirando el clip entero estaba en **casi todos los cuadros**, y revisando los otros tres clips del mismo autor (**@mushslime**: `c04`, `c08`, `c17`, `c30`) **los cuatro tenian el tripode en cuadro**: graba con el tripode dentro del encuadre. Ninguno habia salido sorteado en la tanda 1, por eso nunca se habia visto. Regla: cuando un clip tiene equipo de filmacion a la vista, **se revisan todos los clips de ese creador**, no solo ese.
- **La nota de un recorte puede estar mal medida, y se paga en el render siguiente (20/11).** `c23` decia *"a los 22 s aparece una paleta de sombras"* y la ventana se habia fijado en 18,0 s. La paleta entra a los **~14 s**: con la ventana corrida salio quemada en el render de R2. Ventana corregida a 13,5 s. Las notas de recorte se verifican mirando el clip, no se heredan.
- **La etiqueta sobre el frasco se queda, salvo que sea el primer plano del ad (20/11).** `c28` abre con *"SLIME BUTTER / EXTRA WHIPPED BUTTERCREAM"* de otra tienda, grande y nitida, y cayo justo en el **primer plano de R3**, abajo de la caja de hook. La regla del 18/11 (etiqueta sobre frasco = se queda) sigue valiendo, pero **el plano de apertura es otra cosa**: ahi una marca ajena legible es lo primero que ve el mercado. Veto de los primeros 14 s de `c28`; el resto del clip se sigue usando. Mismo criterio con el frasco *"MARKET COOLER"* de `c25` (2,5 a 5,5 s).
- **Dos clips del pool estaban corruptos** (ffmpeg colgaba con *Operation timed out* al abrirlos). Se detectan con un barrido de `ffprobe` con timeout y se rebajan con `dl_tikwm.py`.

## Preguntas abiertas
- ¿Cuántos anuncios activos tiene hoy la página y desde cuándo? (los 17 creativos son del 31/10 al 16/11).
- El backend: todavía no están armados los 4 OTOs. El molde es [[scented-stones]] (ver [[embudo-post-compra]] si se arma).
- ¿Conviene una tanda 2 con formato estático (caja de preguntas de IG)? Ellos no lo usan.

## Relacionado
[[estilo-de-video-ia]] · [[guiones-y-anuncios]] · [[internacionalizacion]] · [[ceramic-recipes]] · [[scented-stones]]

## Fuentes
- `OUTPUTS/2026-11-18-guiones-slime-shop-kit-tanda1.md`
- `~/Desktop/slime-shop-kit/anuncios/work/competencia/` (17 creativos de ellos) y `work/vent_slime.py`
- `OUTPUTS/scripts-vsl/gen_slime_plans.py`, `edit_slime.py`, `scan_carteles.py`
