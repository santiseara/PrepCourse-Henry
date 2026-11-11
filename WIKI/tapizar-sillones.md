# Tapizar sillones

> Oferta nueva para **Argentina** (voseo): aprender a tapizar un sillón desde cero, **sin coser**, con martillo y engrampadora. Modelada de **Caprichos de Mar** (`aprendeatapizarsillones.impultienda.ar`), 19 ads activos en AR desde el 30 de octubre. Tanda 1 de 6 videos del 11/11. (fuente: Biblioteca de Anuncios, page id 462185917253124)

## El competidor
- **Caprichos de Mar**, dos hermanas (Mar y Vero) con **más de 10 años de taller** de tapicería y restauración en Argentina. Es **marca personal**: se clonan los anuncios, no la marca.
- **19 ads activos**, el más viejo del 30 de octubre. Corren **dos cosas en paralelo**: el curso (`aprendeatapizarsillones.impultienda.ar`) y el **servicio** de retapizado por WhatsApp. Los ads del servicio no se modelan.
- **Precio: AR$39.990** en ImpulTienda, pago único, acceso inmediato. Valor tachado AR$75.950.
- **Lo que entrega:** curso en video (un sillón de 2 cuerpos de punta a punta) · **Bono 1** confección de almohadones (60 páginas con fotos) · **Bono 2** la tela perfecta y la medida exacta · **Bono 3** de tapizar a emprender, con planilla de presupuesto · **grupo de WhatsApp de soporte** · garantía de 7 días · +1.500 alumnos.
- **El mecanismo que repiten en todos lados:** *"sin coser, solo con martillo y engrampadora"*.

### Las 6 familias ganadoras (14 videos bajados y transcriptos el 11/11)
| # | Familia | Frase eje |
|---|---|---|
| 1 | **El sillón que iba a la basura** (la más replicada) | *"¿Viste este sillón viejo y destruido? La mayoría lo tiraría, pero si estás buscando un ingreso extra es valiosísimo"* |
| 2 | **Sin taller ni máquinas** | *"No necesitás taller ni máquinas caras para empezar a tapizar"* |
| 3 | **El gato rompió el sillón** | *"¿Estás pensando en tirar ese sillón que tu gatito rompió? No lo hagas"* |
| 4 | **Proyectos ambiciosos con miedo** | *"Te encantan los proyectos ambiciosos, son tu cable a tierra, pero tenés miedo de no terminarlos"* |
| 5 | **Testimonio de alumna** | *"Compré el curso y le renové el tapizado a este sillón que era de mis abuelos"* |
| 6 | **Te quedaste sin trabajo** | *"Un oficio como la tapicería es hiperrentable: con pocos trabajos al mes ya tenés para vivir cómodo"* |

### La lista de objeciones de su landing (oro para los guiones)
Miedo a que el sillón quede **desarmado por meses** · no saber **cuánta tela** comprar · creer que hay que **saber coser** o tener máquina · *"no voy a poder, hace falta fuerza, es cosa de hombres"* · **a quién preguntar** si te trabás · no tener lugar ni tiempo.

### Su edición
B-roll de sillones **antes/después** y panorámicas lentas del sillón terminado; **banda blanca con texto negro arriba** durante el hook (*"APRENDÉ A TAPIZAR SILLONES DESDE CERO A TU RITMO Y EN VIDEO!"*); **subtítulos chicos blancos, sin caja**, abajo al centro, de 3 a 5 palabras; pantallas partidas para el antes/después; **sin placa de cierre**. CTA fijo: *"Hacé clic abajo y entrá al hermoso mundo de la tapicería"*.

## Lo que hicimos
- **Los 6 guiones**, uno por familia, con hook, cuerpo y CTA propios: el sillón de la vereda · no se cose, se clava · el gato te arruinó la tela · el oficio que nadie aprende · el miedo real (que quede desarmado) · el sillón de tu abuela.
- **La edición se clona** (banda blanca arriba + subtítulos chicos blancos sin caja). Lo que agregamos son los **4 insertos dibujados por código** (`gfx_tapizar.py`), que ellos no tienen: los seis pasos, las tres herramientas con la lista de "sin", todo lo que recibís y el celular con el índice. Paleta lino `#F4EFE7` + tinta `#23201C` + verde azulado `#2F6B6A`.
- **Sin cifra en pesos.** Es oferta de un solo país, así que podría llevar una, pero la única candidata era cuánto se cobra un retapizado, que en un ad de ingresos es lo que más mira Meta ([[problemas-de-cuentas-meta]]). Quedó como múltiplo: *"se cobra varias veces lo que sale aprender a hacerlo"*.
- **Voz Sulafat** en rioplatense, `speed 1.30`. La V6 salió con `gemini-2.5-flash-preview-tts` porque el 3.1 se quedó sin cuota a mitad de la tanda.

## Versión LATAM (2026-11-11)
Santiago: *"Necesito los ads de sillón con acento neutro, son para LATAM"*. La tanda se rehízo entera en **español neutro**.

- **No alcanza con sacar el voseo:** también salieron los argentinismos que no se leen igual en México o Colombia — *vereda* → **calle**, *living* → **sala**, *engrampadora* → **engrapadora**, *almohadones* → **cojines**, *prolijo* → **parejo**, *garage* → **garaje**, *dar vuelta* → **voltear**, *apoyabrazos* → **brazos**. Los **insertos** (`gfx_tapizar.py`) y la descripción se rehicieron igual.
- **Voz** Sulafat con Style de mujer latinoamericana (mezcla mexicano-colombiana), verificada con Gemini sobre el primer wav: *"español mexicano, no usa voseo"*.
- 🐞 **La placa de cierre se me quedó en voseo.** Cambié los guiones, la voz y los insertos, pero el `head` de la placa final seguía diciendo **"TOCÁ ABAJO"** y la línea de entregables, *"Almohadones"*. Lo cazó el OCR del render (17 cuadros) y hubo que rehacer los seis. Regla práctica: cuando se cambia el dialecto de una tanda, el texto vive en **cuatro lugares** — el guion, los chips y tags del plan, los insertos de `gfx_*.py` y la **placa de cierre** —, y el OCR del render es el que confirma que no quedó ninguno.
- Guiones en `OUTPUTS/2026-11-11-guiones-tapizar-sillones-latam.md`. Planes: `gen_tapizar_plans_latam.py`. Los videos en voseo quedaron en `work/version-argentina/`.

## El pool de TikTok
- 96 clips de `#tapiceria`, `#tapizado`, `#reformadesofa` y `#restauraciondemuebles`. **Entraron 21.**
- `#restauraciondemuebles` trae sobre todo **pintura de muebles de madera** (chalk paint), y los otros tags pesan fuerte en **tapizado de autos**: nada de eso muestra lo que vendemos.
- Se cayeron por marca de agua `@jessicafernanda.ofc` y `TAPICES FORRY'S`, y **26999 se cayó recién en la hoja del render** (*"Publicada en mi perfil"*): el scan ya decía **34 cuadros con texto de 60** y yo le había recortado la ventana en vez de tirarlo. Es la regla del 11/11 de [[displays-de-papel]], repetida el mismo día.
- Listado completo con cuenta, link y tramo en `OUTPUTS/2026-11-11-visuales-tiktok-tapizar-sillones.md`.

## Preguntas abiertas
- **Falta la landing y el precio nuestro.** Los guiones no nombran marca ni precio.
- ¿Clonamos también su **servicio** de retapizado por WhatsApp, o solo el curso?
- ¿Va la cifra en pesos de lo que se cobra un retapizado? Hoy está como múltiplo en el guion 4.

## Relacionado
[[guiones-y-anuncios]] · [[arreglos-de-ropa]] · [[herrero-de-finde]] · [[problemas-de-cuentas-meta]] · [[displays-de-papel]]

## Fuentes
- Biblioteca de Anuncios, page id 462185917253124 (19 ads activos, leídos el 2026-11-11)
- `aprendeatapizarsillones.impultienda.ar`
- OUTPUTS/2026-11-11-guiones-tapizar-sillones-tanda1.md
