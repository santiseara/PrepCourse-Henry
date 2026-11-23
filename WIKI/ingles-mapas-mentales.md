# Inglés con Mapas Mentales (Argentina)

> Clon argentino de **Fluente com Legenda** (`mapa.fluentecomlegenda.com`), un low ticket brasileño que vende
> +300 mapas mentales imprimibles de inglés (A1→C2) más 5 bonus. Cazada y modelada el 2026-11-22.

## La oferta original
- **Producto:** +300 mapas mentales de inglés en PDF, imprimibles, divididos por los niveles oficiales
  (A1 Fundação 50 · A2 Construção 55 · B1 Independente 55 · B2 Natural 55 · C1 Avançado 50 · C2 Domínio 45).
  Cada mapa trae: significado, estructura, ejemplos, dato rápido, error común y **mini ejercicio**.
- **5 bonus:** 82 ebooks + audiolibros · 500 frases más usadas con pronunciación y traducción ·
  "Rota da Fluência" (plan diario de estudio con checklist) · 100 phrasal verbs · 150 expresiones y modismos.
- **Precio:** R$ 37,90 pago único (de R$ 382), garantía 7 días, entrega por mail + área de miembros.
- **Prueba social:** +11.450 alumnos, testimonios de alumnos y de una profesora de inglés.

## Por qué es un winner
- **~230 anuncios activos** en la Biblioteca el 22/11, **131 creativos distintos**, y los de arriba corren con
  **13-14 anuncios usando el mismo contenido** (o sea: el mismo video replicado en 14 conjuntos).
- En circulación desde fines de septiembre: más de 7 semanas corriendo.
- Low ticket, infoproducto puro, sin marca personal fuerte. Pasa todos los filtros de [[filtros-caza-de-ofertas]].

## La DNA de sus guiones
Formato único, repetido en los 24 creativos que bajamos: **POV de manos sobre el material**, cero cara (salvo
2 o 3 con presentadora), impresora escupiendo hojas o mano pasando páginas de un anillado.

Estructura fija:
1. **Hook de 1 frase** — siempre sobre el DESORDEN o la CONFUSIÓN de estudiar inglés, nunca sobre el precio.
2. **Un solo mapa mental leído en voz alta** — se nombra lo que se ve: la regla, los ejemplos, el error común,
   el mini ejercicio. Esto ocupa la mitad del video.
3. **"Y este es uno solo de los más de 300"** + nivel A1 a C2.
4. **"Viene en PDF, lo imprimís o lo ves en el celu"**.
5. **"Y encima te llevás 5 bonus"** (se muestran).
6. **CTA:** "Clicá en Saber más y conseguí los tuyos" (+ garantía de 7 días en algunos).

Los 13 hooks distintos que usan: arrepentimiento ("ojalá lo hubiera descubierto antes") · recién impreso
("mirá lo que acabo de imprimir") · objeción ("no sé nada de inglés, ¿puedo?") · no encontrás lo que estudiaste ·
apuntes desparramados · anotar no alcanza · confusión puntual (was/were, have/has, much/many) · impreso vs pantalla ·
"sin confusión, directo al punto" · "no sabía que se podía ordenar así" · autoridad (profesora de inglés) ·
olvido al día siguiente · "cómo nadie me mostró esto antes".

## ⛔ El problema de este clon: el material está en portugués
Medido sobre **24 de sus creativos de más impresiones (~1.300 segundos, 1 cuadro por segundo con OCR de Vision)**:
- Los mapas son un producto **brasileño**: los títulos van bilingües (`WAS E WERE / Was and Were`,
  `HAVE E HAS`, `MUCH E MANY`, `Prepositions of Place`) pero **todo el cuerpo está en portugués**
  (*Perguntas e negativas*, *Respostas curtas*, *Mini exercício*, *Erro comum*, *Nível A2*, *Você trabalha?*).
- Filtrando caras, subtítulos quemados, stickers de comentario, la página del logo, el área de miembros
  (tapas que dicen *Inglês Nível A1*) y todo cuadro con un delator portugués legible, quedan
  **~85 segundos usables de 1.300**.
- **Conclusión: no existen "videos donde muestra el material en inglés".** Lo que sí hay son planos donde el
  título grande es inglés y el portugués queda chico. La tanda del 22/11 se armó con esos 85 segundos.
- **La solución real para la próxima tanda:** rehacer los mapas en español (HTML + captura, o Nano Banana por
  navegador) y filmar/componer planos propios. Mientras el producto argentino no exista, el ad muestra el
  material de otro idioma.

## ⛔ Tanda 1 v1: el producto dibujado se cayó (2026-11-22)

La primera versión de la tanda se armó con **las páginas del producto dibujadas por código en español**
(`gfx_ingles.py`), porque el material de ellos está en portugués. Santiago la rechazó en una línea:
*"Horribles las visuales, usá las originales"*. **El visual de un clon sale del creativo del ganador**
(regla nueva en [[guiones-y-anuncios]]). Las páginas dibujadas quedan como base del **producto argentino**
—son 15 hojas con la DNA de las suyas— pero no como visual de los ads.

## Tanda 1 v2: sus creativos, limpiados (2026-11-22, noche)

- **30 creativos suyos** bajados de la Biblioteca en **720x1280** (`video_hd_url`, los de más impresiones).
- Limpieza en 5 pasos (detalle del método en [[guiones-y-anuncios]]): recorte del watermark con
  `zoom=1.25/ybias=0` sin recomprimir, fuera caras y capturas del área de miembros, fuera **su subtítulo
  quemado** (detectado por el amarillo de su palabra resaltada), fuera los 3 creativos con **sticker de
  comentario** y fuera los tramos con su CTA. De 1.175 s quedaron **714 s**: 85 tramos de 17 creativos.
- **Voces: 3 de mujer (Sulafat) en V1, V2 y V5 y 3 de hombre (Orus) en V3, V4 y V6**, mismos guiones.
  V5 tiene que ser de mujer sí o sí: el guion dice *"yo, como profesora de inglés"*.
- Cada hoja que ELLOS muestran entra **anclada a la palabra que la nombra** en nuestro guion: el OCR de
  sus propios cuadros encuentra `MUCH E MANY`, `WAS E WERE`, `HAVE E HAS`, `500 FRASES`, `ROTA DA
  FLUÊNCIA`, los niveles y los bonus.

## El producto en español se dibuja, no se pide prestado (2026-11-22)

Como el material de ellos está en portugués, **el material que se ve en nuestros ads es el producto
argentino, dibujado por código**: `OUTPUTS/scripts-vsl/gfx_ingles.py` saca **15 páginas** a 2160x3840
(6 mapas, 8 páginas de bonus y la grilla de volumen) y de cada una tres encuadres → **43 planos**.
Misma salida que [[laboratorio-wow]]: si el producto en el idioma destino todavía no existe, el inserto
se dibuja. Detalle de qué muestra cada página en
`OUTPUTS/2026-11-22-ingles-mapas-mentales-tanda1-plan.md`.

- La DNA de sus mapas, respetada hoja por hoja: título bilingüe, badge de nivel, nodo central y ramas con
  **significado, estructura, dato rápido, error común (✗ rojo / ✓ verde) y mini ejercicio**.
- **La hoja termina en y=1500 de 1920 a propósito**: los últimos 420 px quedan de fondo oscuro para que
  el subtítulo quemado del ad no tape ni una línea del material. Es la forma de poder leer la hoja *y*
  tener subtítulos.
- El contenido de cada mapa está escrito contra el guion que lo nombra: si el guion dice "tiene tips, mini
  ejercicio y hasta un mini diálogo", la hoja del aeropuerto tiene esas tres ramas.

## Tanda 1 (2026-11-22)
- 6 guiones en español rioplatense, copiados de sus 6 mejores ángulos:
  `OUTPUTS/2026-11-22-ingles-mapas-mentales-6-guiones.md`.
- Visual: **las 43 páginas del producto en español** (lo que se lee en voz alta) + **14 clips de TikTok**
  de impresora, anillados, post-it y manos escribiendo, como tejido entre página y página.
- Voz: **Sulafat**, estilo rioplatense verificado con Gemini, speed 1.20.
- Corte cada ~2,5 s (más lento que un ad de b-roll puro: la hoja hay que poder leerla), subtítulos de
  3 palabras abajo con la palabra que suena en amarillo, y cada página **anclada a la palabra que la nombra**.
- Descripción: `OUTPUTS/2026-11-22-ingles-mapas-mentales-descripcion.md`.

### Lo que costó el b-roll en este nicho
De **148 clips** bajados de `#mapasmentales`, `#apuntes`, `#impresora`, `#papeleria` y `#estudiaringles`,
el filtro automático de texto quemado dejó pasar **cero**: en este nicho el tema **es** papel escrito, así
que el OCR encuentra texto en casi todos los cuadros y no sabe distinguir el apunte del cartel del creador.
La selección se hizo **a ojo sobre hojas de contactos** (7 hojas de 24 clips con 2 cuadros cada uno, y
después una tira de 6 cuadros por finalista) y quedaron **14**. Ver la regla nueva en [[guiones-y-anuncios]].

## Preguntas abiertas
- ¿Precio en pesos y plataforma de cobro (ImpulTienda)?
- ¿Se rehacen los mapas en español o se compra/arma un equivalente?
- Backend: se clona de los 4 OTOs de [[scented-stones]] (regla de [[backend-molde-de-piedras]]).

## Relacionado
[[guiones-y-anuncios]] · [[caza-de-ofertas]] · [[estilo-de-video-ia]] · [[como-trabajar-con-santiago]]

## Fuentes
- Biblioteca de Anuncios de Meta, búsqueda `mapa.fluentecomlegenda.com` (22/11/2026)
- `mapa.fluentecomlegenda.com` (landing completa)
- 24 creativos bajados en 720x1280 y transcriptos con faster-whisper
