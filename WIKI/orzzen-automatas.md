# Orzzen — Tu Primer Autómata de Madera (→ Your First Wooden Automaton)

> Oferta de autómatas de madera que corre en ImpulTienda en español (AR$ 19.976, 60% off) y que se clona al **mercado inglés**. Análisis del 2026-11-05 sobre `orzzen.impultienda.ar` en la Biblioteca de Anuncios. (fuente: Biblioteca de Anuncios de Meta + landing `orzzen.impultienda.ar`)

## Ideas clave
- **32 anuncios activos**, el más viejo del **13 oct. 2026** → 23 días corriendo. Escala sostenida, no un arranque.
- **Nicho vacío de verdad**: autómatas de madera (wooden automata / kinetic sculpture) no tiene nadie vendiéndolo como infoproducto en inglés. El material de TikTok existe y es hipnótico (el producto se filma solo).
- **Avatar doble**: el que ya trabaja la madera y nunca se animó a la mecánica, y el principiante total que vio un autómata y preguntó "¿cómo se hace eso?".
- El producto es **el mecanismo, no la madera**: manivelas, levas y conectores. Eso es lo que todos los hooks prometen entender.
- **Prueba social dura: +1.400 compradores, 4.9 ★**, y la repite en 6 de los ads.
- **Promesa de tiempo: primera pieza terminada en 5 a 7 días**, 1 a 2 horas por día.

## Las 7 familias de guion (transcriptas de 14 videos)
1. **"Podés construir esto aunque…"** — la madre. Desde el 13/10, con **6 variantes vivas** que cambian solo la objeción del hook (no distingue una mecha de un tornillo · nunca cortó una tabla · no sabe dibujar una línea recta · solo tiene los fines de semana · sus manos solo escriben en un teclado). Cuerpo idéntico: *no es motivación → no lleva motor ni electrónica → la guía te lleva de la mano → +1.400 personas → esta semana tenés tu primera pieza → CTA*.
2. **Diálogo de dos voces** (0:41, el más largo) — pregunta/respuesta que liquida las objeciones una por una: cómo se mueve, planos, herramientas, qué mecanismo usar.
3. **Antimoderno** (0:20) — *"no tiene pantalla, ni batería, ni algoritmo"*. Hacer algo real en un mundo falso.
4. **"¿Hace cuánto que no terminás algo?"** (0:34) — el único emocional puro: todo lo que hacés en el día no se termina nunca; esto empieza y termina.
5. **Demostración / misterio** (0:23) — *"Eso parece imposible de fabricar. Hasta que ves esto."* Explica el mecanismo en dos pasos.
6. **Artesano / oportunidad** (0:21) — *"La mayoría ve un adorno. Un artesano ve algo muy diferente."* Único que roza el bizop; la landing lo respalda con el Bono 4.
7. **Estacional de Navidad** (0:25, impresiones bajas) — el pesebre que se mueve. Buen ángulo, poco gasto.

## Lo que incluye el producto (para alinear los ads)
Guía completa · Curso en video de 18 lecciones (2 h 15) · Planos, plantillas y medidas · Proyectos paso a paso · Videoteca premium · Biblioteca de +20 mecanismos · Cuaderno de diseño · **App simuladora de mecanismos** · Guía para vender tus autómatas. Garantía de 30 días, acceso de por vida.
Proyectos que promete: raya manta, pájaro con alas, músico, caballo al galope, escenas cotidianas, figura propia.

## Tanda 1 producida (5/11) — 6 videos de voz en off
- **Voz:** Orus (hombre, acento americano) por API. El guion 2 es el único a **dos voces** (Orus + Sulafat), generado con `tts_gemini_multi.py` y `multiSpeakerVoiceConfig`; el guion para TTS lleva los prefijos `Speaker1:`/`Speaker2:` y el guion que lee el editor va limpio (`V2_tts.txt` vs `V2.txt`).
- **Modelo de TTS:** `gemini-2.5-flash-preview-tts` para 4 de las 6; dio 429 en el guion 4 y en el diálogo, y las dos salieron con `gemini-3.1-flash-tts-preview` sin leer el Style en voz alta.
- **Pool:** 19 clips de TikTok del tag `#woodenautomata` (la página de hashtag **sí carga** en el navegador: `tiktok.com/tag/<tag>`, no hizo falta entrar por perfil). Makers reales, nunca tiendas de dropshipping.
- **Duraciones:** 25 a 38 s. Scripts: `gen_automata_plans.py` + `edit_automata.py`.

### La edición: copiada de la de ellos (v2, 5/11)
Santiago, al revisar la tanda 1: *"¿Copiaste tal cual los guiones como te dije? ¿Y la edición?"* La primera versión salió con **nuestro** formato (caja de hook, subtítulos de 2 palabras en ámbar, placa final oscura). Comparado contra sus ads, el montaje de Orzzen es otro:
- **Sin caja de hook y sin placa final.** Arranca en el b-roll y cierra con **la tapa del ebook más un botón ámbar** ("QUIERO EMPEZAR" → *I WANT TO START*).
- **Subtítulos de 3 palabras**, Montserrat con contorno, y **un color distinto por creativo**: amarillo, celeste, verde, ámbar, rosa, naranja.
- **Muestran el producto todo el tiempo**: la tapa, las páginas internas (planos de un proyecto, "Biblioteca de Mecanismos", "Comparativa de los 12 Mecanismos", "Las 6 Fases del Proceso") y **la app simuladora funcionando**, con medidas en mm. Era la diferencia más grande con lo nuestro: nosotros no mostrábamos nada.
- El ad del diálogo lo montan como **podcast**, con dos personas y micrófonos en banda inferior. Eso no se replicó.

Los 5 inserts se dibujan por código en `gfx_automata.py` (tapa, hoja de planos con cut list, biblioteca de mecanismos, las 6 fases, pantalla de la app) y entran **anclados a la palabra que los nombra**. Cuestan cero y no hace falta que el producto exista.

Dos cosas que el editor obligó a resolver:
- **Los inserts necesitan margen.** El zoom de las fotos fijas va de 1.0 a 1.14 más un golpe de 1.16 en cada corte: un gráfico de 1080×1920 justo pierde la cabecera y el pie. Se entregan sobre un lienzo **1.20×** con el sobrante desenfocado. Con 1.41× entraban enteros pero quedaban ilegibles en el teléfono.
- **El cierre se fuerza, no se ancla.** Anclar la tapa a la palabra del CTA no alcanza: en los videos largos entran planos después y el botón queda sobre un clip cualquiera. Se agregó `last` al plan, que fija el clip del último plano.

### La descripción del ad (5/11)
Un **solo copy para los 6 videos**, igual que hace Orzzen con sus 32 ads (ellos testean creativo, no copy). Molde de oferta directa en inglés: golpe en la primera línea (*"It's wood. No motor, no battery, no electronics"*), bullets de mecanismo, entregables con nombre (app simuladora, +20 mecanismos, 18 lecciones, los proyectos), prueba social +1.400 y 4.9★, garantía de 30 días y acceso de por vida, un solo pago **sin precio**, CTA *Tap Learn More* con la promesa de tiempo (5 a 7 días, 1 a 2 h por día). Las dos versiones completas en `OUTPUTS/2026-11-05-descripcion-ads-wooden-automaton.md`.

### Lo que se cayó del pool y por qué
- Caras hablando a cámara (`craftsmm`) y marcas de agua **centradas** (`CRAFTSMM`): el zoom no las saca.
- Texto quemado que vuelve a aparecer más tarde en el clip: el de los camarones dice *"link in bio"* a los 8 s, mucho después del bloque de subtítulos del principio. **Se cayó entero.**
- Subtítulos que duran más de lo que mostraba la hoja de 1,5 s: *"Turn the crank → chickens dance!"* llega hasta 4,0 s y el texto en español del pájaro hasta 3,5 s, con un *"Gracias por ver"* a los 13,0 s. Los dos extremos de la ventana hay que verificarlos, no solo el principio.
- Etsy y cualquier "link in bio".

## Detalles / notas
- La landing ya escribe los hooks: *"Ves un autómata increíble y piensas ¿cómo se hace eso?"*, *"Buscaste tutoriales y todo lo que encontraste era confuso, incompleto o en otro idioma"*, *"Si puedes seguir instrucciones, puedes construirlo"*, *"Hay miles de proyectos de madera. Solo uno hace que la gente pare y pregunte ¿cómo funciona?"*.
- El argumento *"todo lo que encontraste estaba en otro idioma"* **se da vuelta en inglés**: ahí el material bueno sí está en inglés, así que el dolor pasa a ser "confuso e incompleto".
- Los videos del competidor son **voz en off sobre clips de autómatas**, 17 a 41 s. Mismo formato que usamos nosotros: los clips se consiguen en TikTok.

## Preguntas abiertas
- Nombre y precio definitivos en inglés (propuesto: *Your First Wooden Automaton*).
- Landing propia en inglés: ¿se clona la de Orzzen o se arma nueva?

## Relacionado
[[guiones-y-anuncios]] · [[internacionalizacion]] · [[infinity-3d]] · [[herrero-de-finde]] · [[perles-merveilles-3d]]

## Fuentes
- Biblioteca de Anuncios de Meta, búsqueda `orzzen.impultienda.ar` (5 nov. 2026, 32 ads activos, 14 videos transcriptos)
- Landing `orzzen.impultienda.ar`
- OUTPUTS/2026-11-05-guiones-orzzen-automatas-ingles.md
- OUTPUTS/2026-11-05-descripcion-ads-wooden-automaton.md
- OUTPUTS/scripts-vsl/gen_automata_plans.py · OUTPUTS/scripts-vsl/edit_automata.py · OUTPUTS/scripts-vsl/tts_gemini_multi.py
