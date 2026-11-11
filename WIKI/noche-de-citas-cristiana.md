# Noche de Citas Cristiana (Date Night)

> Oferta nueva para **Argentina**, clonada de **Date Night Cristão** (`dateparacasais.com.br`, R$ 19,90), la página **Ana Cristina** de la Biblioteca de Anuncios: **+100 encuentros listos** para que un matrimonio tenga una noche de a dos adentro de casa, cada uno con desafío, juego, dinámica, conversación, oración y devocional. (fuente: Biblioteca de Anuncios + los 12 videos del competidor, 2026-11-10)

## Ficha
| Campo | Valor |
|---|---|
| Mercado | 🇦🇷 Argentina, **voseo** |
| Producto | +100 encuentros para matrimonios: juego de cartas, cartas de preguntas, devocionales, oraciones guiadas, desafíos de conexión, bingo, verdad o desafío, tribunal bíblico, los 4 temperamentos |
| Avatar | Matrimonio cristiano de años, que llega a la noche cansado, con el celular en la mano y sin tema de conversación |
| Precio | **a definir** (el original: R$ 19,90, una sola vez, acceso inmediato por celular y 30 días de garantía) |
| Formato de ads | **Sin voz en off y sin subtítulos**: música + carteles fijos, 15 s |

## 🐋 El ganador: Ana Cristina / Date Night Cristão (leído el 2026-11-10)
- **16 ads activos**, el más viejo del **12 de agosto de 2026** → casi 3 meses corriendo. Todos video, **15,4 s exactos**, 9:16.
- De los 12 que bajé, **6 son creativos distintos**: dos de ellos están subidos 4 veces cada uno (mismo video, distinto anuncio).
- **Ninguno tiene locución.** Se transcribieron los 12 con faster-whisper: audio vacío. Toda la venta la hacen **dos carteles de texto y la música**.
- Landing `dateparacasais.com.br`, "⭐ + 72.442 Avaliações 5/5", acceso inmediato y garantía de 30 días.

### La estructura, idéntica en los 6
1. **0 a ~6,5 s — el hook.** Un solo cartel fijo, blanco con borde negro, centrado arriba, 2 a 3 líneas con emoji, sobre **4 planos de celular**: la Biblia abierta con las hojas impresas al lado, el marido escribiendo en la mesa, ella en un café, las manos tomadas, la cama a oscuras.
2. **~6,5 a ~12,5 s — qué es.** Segundo cartel fijo sobre **las hojas del producto**: o a pantalla completa (la página del juego de cartas, el devocional, las oraciones) o apiladas en la mesa mientras una mano las pasa.
3. **~12,5 a 15,4 s — el cierre.** **Caja blanca con texto negro** (`CLIQUE NO LINK ABAIXO`, `Link dos Encontros está aqui em baixo 👇`) sobre una pareja feliz bailando o abrazada.

### Las 6 familias de cartel (lo que clonamos)
| # | Familia | Cartel 1 del original |
|---|---|---|
| 1 | **Volvió el tema de conversación** | "Depois de anos casados, isso trouxe assunto de volta pra nossa noite ❤️" |
| 2 | **Comparación de precio + inmediatez** | "Menos que um jantar fora, e recebemos o acesso na hora." |
| 3 | **El dolor en mayúscula** | "CASADOS HÁ ANOS E SEM ASSUNTO.." |
| 4 | **Costó menos que una pizza** | "Nossa melhor sexta custou menos que uma pizza 🍕🥰" |
| 5 | **La oración que nunca arranca** | "«Hoje a gente ora junto», chegava a noite e ninguém começava 😔" |
| 6 | **El precio puesto adelante** | "R$ 19,90, uma vez só. A gente orou junto na mesma noite que comprou." |

El **segundo cartel** rota entre: "+100 encontros prontos pra fazer a dois: oração, devocional, quiz bíblico, jogos e cultos 🙏", "Acesso na hora pelo celular, e 30 dias de garantia 🙏❤️" y "Até que achamos os date nights, agora a oração já vem escrita pra gente fazer 🙏❤️".

## 🔎 Competencia (leída el 2026-11-10)
- **En portugués el nicho está caliente:** `"encontros prontos"` da **~100 ads activos** con al menos 8 anunciantes (Ana Cristina, Rafaela Dantas, Geize Lima Terapeuta, Semear a Fé, Prime Dicas, CestodaCatequista, Ana Alves, Ano Pastoral dos Casais).
- **En español no lo corre nadie.** `"juegos para parejas"` da ~29 ads y son **mazos físicos** (toyco.com.ar, Mister Brewer, En Palabras, Kermés, Mazo 365); `"cartas para parejas"` en AR, 7 ads, lo mismo. `"parejas cristianas"` y `"devocional en pareja"`, cero. Es el arbitraje de [[caza-de-ofertas]]: ballena en Brasil, mercado destino vacío. Y los mazos físicos argentinos prueban que la demanda de "cartas de preguntas para la pareja" ya existe acá.

## 🎬 Producción de la tanda 1 (2026-11-10, 6 videos)
`OUTPUTS/2026-11-10-guiones-date-night-tanda1.md` · videos en `~/Desktop/date-night/anuncios/`.
- **Las páginas del producto se dibujan por código**: `OUTPUTS/scripts-vsl/gfx_datenight.py` (HTML + Chrome headless) saca las 7 hojas en español —cartas de la gratitud, preguntále a tu pareja, devocional, oraciones guiadas, desafíos de conexión, bingo y verdad o desafío— con la paleta de ellos (papel crema, vino, dorado). No hace falta que el producto exista todavía.
- **Editor propio sin voz:** `OUTPUTS/scripts-vsl/edit_datenight.py` + `gen_datenight_plans.py` + `vent_datenight.py`. Monta los planos, les quema los carteles fijos (Poppins SemiBold blanca con borde negro, emoji a color) y la caja blanca del cierre, y le pone la cama `bed_calma` (piano de fieltro, 64 BPM, `music_calma.py`) de punta a punta. Sin locución y sin subtítulos.
- **El pool costó tres tandas de descarga.** 135 clips de los tags del nicho en español (`#parejascristianas`, `#matrimoniocristiano`, `#juegosenpareja`, `#biblia`, `#devocionaldiario`) se tiraron **enteros**: todos traían texto quemado. Los que sirvieron salieron de tags de **objeto**, que no tienen idioma (`#juegodecartas`, `#cardgames`, `#boardgamenight`, `#cozynight`): **11 clips limpios** —7 de manos con cartas sobre una mesa, 3 de parejas jugando y 1 de la casa a la noche con velas— verificados con cuadros cada 1 s entre el segundo 1 y el 10. La regla quedó anotada en [[guiones-y-anuncios]].
- **Los 6 videos:** `10-11 - 1` a `10-11 - 6`, 1080×1920, en `~/Desktop/date-night/anuncios/`.
  - **1 a 3 (clones):** 15,40 s, **sin voz y sin subtítulos**, cama `bed_calma`, dos carteles fijos y caja blanca de CTA.
  - **4 a 6 (orgánicos):** con **voz en off de mujer (Sulafat)** y **cama activa nueva** (`music_activa.py`, 104 BPM, pluck + palmas + bajo, generada para esta oferta porque Santiago pidió *"música activa, no la de siempre"*). Duran **14,87 / 17,47 / 13,93 s**: el largo lo manda la locución ya procesada (`speed 1.30`, pausas recortadas a 0,26/0,12). Con voz quedan **solo dos carteles**, el de apertura estilo TikTok y el del CTA; el del medio lo dice ella. **Y llevan subtítulos** (pedido de Santiago del 10/11: *"agregale subtitulos, que se vean bien"*): **3 palabras**, Montserrat ExtraBold 92 blanca con borde negro de 9, la palabra que suena en **ámbar #F2B33C**, a `capy 1330` para que no choque con los carteles de arriba. Se arman alineando la transcripción con el guion escrito (Whisper con `word_timestamps` + `difflib`) y se queman con `ass=` — este ffmpeg trae **libass**.
  - La locución salió con `gemini-2.5-flash-preview-tts` en la primera y con **`gemini-3.1-flash-tts-preview`** en las otras dos (la 2.5 devolvió **429** a la segunda request del día). Las tres se transcribieron: arrancan por la primera palabra y no leen el Style.
- ⚠️ **La misma pareja aparece en varios ads** (el pool limpio de parejas jugando son 3 clips y dos son del mismo creador). Para la tanda 2 conviene ampliar el pool antes de repetir el formato.

## Preguntas abiertas
- **Precio y checkout**: falta definirlos. El original sale R$ 19,90 una sola vez.
- **La landing no existe todavía** (ni el producto). Los ads se pueden testear igual porque las hojas están dibujadas.
- ¿Entra un quiz adelante, como en [[secreto-de-la-chia]], o va directo a la página de venta?

## Relacionado
[[caza-de-ofertas]] · [[guiones-y-anuncios]] · [[internacionalizacion]] · [[visuales-de-tiktok]]

## Fuentes
- Biblioteca de Anuncios, página 1244301418773018 (Ana Cristina), 2026-11-10
- 12 videos del competidor bajados y transcriptos (audio vacío) + hojas de contactos
