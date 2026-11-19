# Capillas de la Virgen — capillas marianas para imprimir (LATAM)

> Clon en **español neutro para LATAM** de **The Our Lady Chapel Kit** (`ourladychapels.impultienda.ar`, US$ 27), de **Mariana Williams Creations** — la misma página que corre [[slime-shop-kit]]. Producto: **120 capillas de papel de la Virgen** en 12 advocaciones, que se imprimen en casa, se recortan, se doblan y quedan paradas. (fuente: su biblioteca de anuncios y su landing, 18/11/2026)

## La oferta de ellos
- **120 diseños** en **12 advocaciones** (Guadalupe, Gracia/Milagrosa, Inmaculada, Fátima, Lourdes, Inmaculado Corazón, Desatanudos, Perpetuo Socorro, Carmen, Dolores, Rosario, Buen Socorro), 10 diseños por advocación, cada uno en **3 tamaños** (Premium de página entera, Standard ~20x13 cm y Mini ~13x9 cm, 4 por hoja).
- **Estilos:** clásico, ícono, acuarela, dulce, vitral, vintage, floral, luz de vela, moderno y barroco.
- **5 bonos** (valor declarado US$ 64): separadores y tarjetitas, cajas de rosario y porta-caramelos, portavelas y canasta, **calendario mariano 2027** y la **guía de impresión y venta con licencia de reventa** de las piezas armadas.
- **Precio:** US$ 54 → **US$ 27**, descarga inmediata, garantía de 7 días.
- **Avatar:** mujer católica que quiere un rincón de oración en casa, que regala en comuniones, bautismos y novenas, catequista o voluntaria de parroquia, y la que quiere armar y vender recuerdos.

## Lo que hacen ellos (sus 6 creativos de más impresiones, del 31/10 al 16/11)
- **24 a 31 segundos**, 9:16, voz en off de mujer cálida y cama musical.
- **Todo el visual es render de IA de su propio producto**: la capilla de papel sobre la mesa, la impresora, las manos que recortan, el altarcito con velas y rosario. Luz dorada de casa. **No usan TikTok.**
- **Caja de hook blanca** redondeada arriba, texto azul marino en mayúscula, se va con la primera frase.
- **Fichas de paso azules** arriba: `1. PRINT` · `2. CUT & FOLD` · `3. PRAY & GIVE`.
- **Subtítulos de 3 palabras** abajo, blancos con la palabra que suena en **dorado**.
- **Placa de cierre** blanca: *CLICK "LEARN MORE" AND DOWNLOAD IT TODAY*.
- **Un solo texto de anuncio** para los ~35 activos.

## Sus 6 ángulos (los que calcamos)
| # | Ángulo | Hook |
|---|---|---|
| 1 | Los tres pasos ⭐ | "Así se arma una capillita de la Virgen en tres pasos" |
| 2 | De una hoja a una capilla | "De una simple hoja de papel a una capilla preciosa" |
| 3 | POV familiar (testimonio) | "Esta fue nuestra tarde de domingo" |
| 4 | Catequesis | "Si das catequesis, a tus niños les va a encantar" |
| 5 | Recuerdo de primera comunión | "¿Buscas un recuerdo que de verdad signifique algo?" |
| 6 | Antes y después | "Arriba, una hoja de papel. Abajo, la misma hoja diez minutos después" |

## Lo nuestro (tanda 1, 2026-11-18)
Los 6 guiones en **neutro, sin voseo y sin cifra en moneda** (`OUTPUTS/2026-11-18-guiones-capillas-virgen-tanda1.md`), con las cajas de hook, las fichas de paso (`1. IMPRIME · 2. RECORTA Y DOBLA · 3. REZA O REGALA`), la placa de cierre y la descripción única.

**Montaje:** `OUTPUTS/scripts-vsl/gen_capillas_plans.py` + `edit_capillas.py` (clon de su firma: cajita blanca, fichas azules, subtítulo con la palabra en dorado). Voces Gemini TTS con **Sulafat**, velocidad 1.20. Cama musical propia (`music_calma.py`, 64 BPM).

## El pool de TikTok (la decisión importante)
Santiago pidió **las mismas visuales, pero sacadas de TikTok** para no tener que difuminar nada. Se bajaron **183 clips** de 12 búsquedas y 3 tags; quedaron **27**. Lo que hay y lo que no:
- **Sí hay:** nichos y capillas de papel y cartón (el nicho de Guadalupe, el arco dorado, la iglesita kraft que se recorta), impresoras imprimiendo, manos que cortan y doblan papel, tarjetas de primera comunión, altarcitos con velas y rosario, la reja de la Basílica con velas.
- **No hay:** la capilla de papel **armada y parada** de ellos, que es un render de IA. El pool real cubre el proceso y el entorno; el producto terminado aparece en pocos planos.
- **Las búsquedas que rindieron** fueron las del objeto bien dicho: `nicho de papel virgen manualidad`, `iglesia de papel cartulina maqueta`, `paper shrine virgin mary`, `recuerdos de primera comunión de papel`. Las devocionales (`virgendeguadalupe`, `altarcito`) traen **texto quemado en el 80 % de los casos**: son posts de oración con la frase encima.

## Preguntas abiertas
- Falta la **landing en español** y el producto (los 120 PDFs). El precio sugerido para LATAM sería menor que los US$ 27 de ellos.
- ¿Se generan 6-8 tomas del producto con Veo (como en [[tarot-2-dias]]) para tener la capilla terminada en cuadro?
- Backend: los 4 OTOs todavía no están; el molde es [[scented-stones]].

## Relacionado
[[slime-shop-kit]] · [[guiones-y-anuncios]] · [[estilo-de-video-ia]] · [[internacionalizacion]] · [[tarot-2-dias]]

## Fuentes
- `OUTPUTS/2026-11-18-guiones-capillas-virgen-tanda1.md`
- Biblioteca de anuncios de Mariana Williams Creations y `ourladychapels.impultienda.ar` (18/11/2026)
- `~/Desktop/capillas-papel/anuncios/work/` (sus 15 creativos, el pool y `vent_capillas.py`)
