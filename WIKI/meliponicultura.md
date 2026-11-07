# Meliponicultura

> Oferta nueva para **LATAM**: la guía completa de crianza de **abejas sin aguijón**. Se modela sobre **Meliponicultura Essencial** (Brasil), una flota faceless de 14 creativos que corre desde el **17 de agosto de 2026** con el mismo guion. En español no hay un solo infoproducto compitiendo. (fuente: pedido de Santiago del 2026-11-07 + Biblioteca de Anuncios)

## Ideas clave
- **El original es brasileño y vende un cuadernillo** (*ABELHAS SEM FERRÃO · Guia de Criação* / *Guia Prático 2026 · Do Quintal ao Mercado*) desde la página faceless **Meliponicultura Essencial** → `saberessencial.com/meliponicultura`.
- Detrás está **Carlos Almeida (Yraptã)**, que además corre su propio ecosistema de cursos con marca personal (12 ads, Black Friday de acceso vitalicio). La flota que modelamos es la cara sin marca del mismo producto.
- **No es una ballena de volumen, es un operador que no cambia lo que funciona:** 8 de sus 14 creativos llevan casi 3 meses al aire y renueva de a uno o dos por mes.
- **La ventana en español está abierta entera:** `abejas sin aguijón` da ~26 ads en toda la Biblioteca y **ninguno es un infoproducto** (son meliponarios vendiendo miel, cajas y enjambres). `curso meliponicultura` da 12 resultados, todos en portugués del mismo autor.
- ⚠️ **Hoy su landing es un lead de libro físico con envío gratis** (nombre + WhatsApp), aunque los ads digan "garantiza tu acceso". La nuestra sale digital; falta armarla.

## 🧬 La DNA de sus 14 ads

El cuerpo es **idéntico palabra por palabra en 11 de los 14**; lo único que cambia es el hook.

1. **Hook = un error de manejo concreto, nunca plata** (13 de 14).
2. Puente: *"y ese es apenas uno de los errores silenciosos que pueden comprometer toda tu crianza"*.
3. Presentación fija: *"Este es el guía completo de meliponicultura, del cero al avanzado"*.
4. Los 6 bullets de siempre: especie ideal · primera colmena · cuidado de las colonias · división de enjambres · cosecha sin perjudicar a las abejas · **y hasta cómo vender y lucrar con la producción**.
5. **El diferenciador:** *"no entrega un montón de información suelta, el contenido sigue una secuencia clara"*. El enemigo declarado es YouTube y los grupos de Facebook, no otro curso.
6. **El entregable estrella: el calendario de manejo mes a mes** (verano agua y ventilación · invierno alimentación de refuerzo · primavera multiplicar cajas).
7. Reaseguro del principiante: *"empieza del absoluto cero, con foto, paso a paso, sin término difícil"*.
8. CTA blando: *"Link aquí abajo"* · *"Tocá Saber más"*.

### Las familias de hook que tiene corriendo
| Familia | Hook | Desde |
|---|---|---|
| Error del agua | "Ofrecé el agua de esta forma o podés perder parte de la colonia" | 16 ago |
| Error del alimento | "El error de no ponerle limón al jarabe" | 17 ago |
| La época equivocada | "Podés estar haciendo el manejo correcto, pero en la época equivocada" | 18 oct |
| La floración | "Si no sabés cuándo da la florada en tu región, deberías dejar de criar abejas" | 2 nov |
| La caja trampa | "El secreto no está en la isca, está en dónde la colgás" | 31 oct y 2 nov |
| Las especies | "Empezá por estas: jataí, mandaçaia y borá" | 16 ago |
| El miedo a no poder | "Más todavía si tenés miedo de no dar la talla" | 17 ago |
| La renta del patio | "Una de las formas más inteligentes de generar ingresos en casa" | 17 ago |
| Lo simple que es | "Mucha gente cree que es complicado" | 17 ago |

**Las dos familias que estrenó en noviembre son floración y caja trampa**: son las que hoy le rinden.

## 🎬 La edición (clonada)
- **POV de manos, cero cara hablando a cámara** en los 14 videos.
- **El cuadernillo en pantalla casi la mitad del tiempo**, siempre abierto en **la página que nombra la voz**.
- B-roll real de meliponario para la otra mitad: cajas trampa colgadas, la piquera, abejas en flores, la jeringa del alimento, los potes de miel.
- Subtítulos quemados de 2 a 4 palabras, **en mayúscula**, blancos con borde, **la palabra activa en verde lima o amarillo** (un color por creativo), **sin caja**.
- Placas mínimas: cartel `LOCAL ERRADO` con ícono rojo y etiqueta de especie con línea apuntadora.
- Cierre: placa roja manuscrita *"Clique em SAIBA MAIS"* con flecha.

## Tanda 1 (2026-11-07) — 6 videos
Guiones en **español neutro con tuteo** ([[internacionalizacion]]), uno por familia ganadora, con estructura, bajada de producto y cierre propios (regla del 22/10: no se repite una frase entre guiones aunque el original sí repita). `OUTPUTS/2026-11-07-guiones-meliponicultura-latam.md`.

1. **El agua, bien ofrecida** — el error silencioso que te come media colonia.
2. **La época equivocada** — acertar la técnica y errar el mes sigue siendo un error → el calendario.
3. **La caja trampa en el lugar correcto** — un enjambre gratis en vez de comprarlo.
4. **Con cuál especie arrancar** — angelita y melipona, y el primer paso de una secuencia.
5. **Cuándo florece tu región** — la floración manda sobre dividir, cosechar y alimentar.
6. **La renta del patio** — la miel rara que se paga más (el único de plata, como en el original).

- **Voz Orus** por API (`gemini-2.5-flash-preview-tts` para V1, V2 y V4; **429 de cuota** → `gemini-3.1-flash-tts-preview` para V3, V5 y V6), acento latino neutro dirigido desde el Style, `speed 1.30`, verificada con Whisper.
- **Visual 100 % TikTok:** 58 clips bajados de `#meliponicultura` con tikwm, **24 entraron al pool** tras la hoja de contactos a 1,5 s y el control de marcas de agua en la mitad inferior. Se cayeron los de texto quemado en portugués, los de cara a cámara, los de bandas negras y un meme de baile que el tag arrastra.
- **Los inserts del cuadernillo se dibujan por código** (`OUTPUTS/scripts-vsl/gfx_meliponi.py`): tapa, calendario de manejo, floraciones, especies, caja trampa, el agua y cosecha y venta. **No hace falta que el producto exista para lanzar la tanda.**
- Scripts: `gen_meliponi_plans.py` + `edit_meliponi.py` (copia del de arreglos con los subtítulos derechos, sin caja, y el botón rojo de ellos).
- Entrega en `~/Desktop/meliponicultura/anuncios/` como `7-11 - 1` a `7-11 - 6`.
- Descripción para ads: `OUTPUTS/2026-11-07-descripcion-ads-meliponicultura.md`.

## Preguntas abiertas
- **¿La landing?** Hoy no existe la nuestra. La del original es un lead de libro físico con cierre por WhatsApp; la nuestra sería digital por Impultienda.
- **¿Nombre del producto y precio?** Los guiones no nombran la marca (el original tampoco), así que no bloquea el testeo.
- **¿Qué países?** México, Colombia, Perú, Ecuador y Bolivia tienen tradición de abejas nativas; Argentina y Chile son mercado más chico para el nicho.
- ¿Sumamos el formato de 1:10 que ellos estrenaron en noviembre, o nos quedamos en 40–60 s?

## Relacionado
[[guiones-y-anuncios]] · [[caza-de-ofertas]] · [[internacionalizacion]] · [[funnel-hacking]] · [[dancego]]

## Fuentes
- Biblioteca de Anuncios de Meta, 2026-11-07: `saberessencial.com/meliponicultura` (17 resultados, 14 creativos bajados y transcriptos con faster-whisper), `Meliponicultura Essencial`, `curso meliponicultura`, `abejas sin aguijón`.
- `OUTPUTS/2026-11-07-analisis-meliponicultura-essencial.md`
- `https://saberessencial.com/meliponicultura/` (leída el 7/11)
