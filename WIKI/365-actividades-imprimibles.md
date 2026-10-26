# 365 Actividades Imprimibles

> Oferta de Santiago: kit sin pantallas de **+390 recursos imprimibles** para chicos de 4 a 12 (robótica con cartón, experimentos y desafíos de concentración), a **US$ 15,99** con 6 bonos. Se modela a **Croba / CrobaVault**, que corre el mismo producto en inglés desde agosto. (fuente: pedido de Santiago del 2026-10-26)

## La oferta propia
- Landing: `https://365-actividades-imprimibles.impultienda.ar/` — "Convierte el tiempo de pantalla de tus hijos en aprendizaje real".
- **US$ 15,99** (tachado US$ 60, "73% de descuento"), pago único, descarga inmediata, **garantía de 7 días**, "4.9/5 · +3.400 familias".
- Contenido: **+40 proyectos de robótica con cartón** (vehículos, poleas, brazos robóticos que funcionan), **+100 experimentos científicos** con cosas de la cocina, **+100 desafíos de concentración y sensoriales**, y **6 bonos** (guía sensorial, entrenamiento de la atención, caligrafía, plantillas de aprendizaje inicial).
- Bloque de dolor de la landing: pérdida de concentración, pereza mental y berrinches al apagar la pantalla. Bloque de solución: tolerar la frustración, curiosidad STEM, orgullo.
- La landing trae **40 imágenes** (tapas de cada categoría y fotos de chicos armando) que sirven de stills para los ads: copiadas en `~/Desktop/365-actividades-imprimibles/imagenes/`.

## El competidor: Croba (page id 550882744784458)
- **33 anuncios activos** en la página, pero es un vendedor multi-oferta: 15 del kit de chicos, 5 de un manual de relojería, 4 de pájaros de madera, 9 de inciensos.
- **Los 15 del kit corren desde el 6 de agosto** (casi 3 meses) con tandas nuevas el 15, 22 y 23 de octubre: es el ganador a modelar.
- **Un solo texto principal en los 15** ("Are you looking for a way to help children spend less time in front of screens?" + lista con emojis de lo que incluye + "Click on Learn More"). **El que varía es el video, no el copy.**
- Landing del competidor: `crobavault.shop`, título "Screen-Free Kit for Kids". Ellos dicen 20 proyectos de robótica, 28 manualidades y 30+ videos; nosotros tenemos más recursos.
- **Formato de sus videos:** 27 a 54 s (mediana 41 s), voz en off en inglés sobre **montaje rápido de clips de manualidades** (robots de cartón, autos con gomita, juguetes de papel), subtítulos de 1 a 3 palabras con la palabra clave resaltada en una caja de color, y **la tapa del producto insertada 2 o 3 veces**. Marca de agua propia arriba al centro.
- Material: `~/Desktop/365-actividades-imprimibles/anuncios/work/` (`rows.json`, `videos/`, `transcripts.json`, `kids_ids.json`).

## Las 15 familias de hook del competidor
1. "Si tu hijo alguna vez desarmó un juguete para ver qué tenía adentro" (6 ago, la más vieja).
2. "Día de lluvia, sin planes y sin dónde ir" (29 sept).
3. "Para vos parece una actividad simple, para tu hijo es un invento brillante" (7 ago).
4. "Para que arme robots toda la tarde no necesitás ser ingeniero" (13 ago).
5. "Si gastás en juguetes que lo entretienen dos días…" (6 ago).
6. "Dos horas. Eso duró mi hijo lejos del teléfono la primera tarde" (15 oct).
7. "Mi hijo pasaba horas frente a las pantallas hasta que encontré…" (5 sept).
8. "Hoy lo más fácil es darle una pantalla para que se quede quieto" (12 sept).
9. "¿Se aferra al teléfono porque es caprichoso? Tal vez no encontró nada mejor" (13 ago).
10. "Si puede pasar una hora mirando videos, puede pasar una hora construyendo algo" (15 oct).
11. "Con una caja de cartón, unas tapitas y un poco de imaginación" (9 sept, el más corto: 27 s).
12. "Horas y horas frente a una pantalla. Ese era mi hijo cada tarde" → "mirá, lo hice yo solo" (12 ago).
13. "Pero yo no sé nada de robótica. Perfecto, yo tampoco" (22 oct, el más nuevo).
14. "¿Sabías que tu hijo puede pasar de mirar una pantalla a construir su propio robot?" (23 oct).
15. "Sin prohibiciones, sin peleas, sin cinco minutos más. Le di otra cosa que hacer" (23 oct).

**DNA del cuerpo:** hook (escena u objeción) → nombre completo del kit → qué trae (robótica, ciencia, juegos, manualidades) → materiales de casa (cartón, tapitas, botellas) → "paso a paso, sin conocimiento técnico ni materiales caros" → beneficios (foco, lógica, orgullo) → CTA "Learn More, acceso inmediato por mail y 6 bonos".

## Tanda 1 (2026-10-26): 6 videos
- Guiones: `OUTPUTS/2026-10-26-guiones-365-actividades-imprimibles.md` (copia en `anuncios/guiones-tanda1.md`), español neutro con *tú*, uno por familia ganadora: 1) el inventor que desarma, 2) dos horas sin el celular, 3) yo tampoco sé de robótica, 4) la tarde de lluvia, 5) el juguete que dura dos días, 6) mira, lo hice yo solo.
- **Voz:** AI Studio, Gemini 3.1 Flash TTS Preview, voz **Gacrux**, Pace Natural, Audio Profile de mamá latinoamericana de 38 en neutro.
- **Edición** (`OUTPUTS/scripts-vsl/edit_365.py`): azul #1D4ED8 de la tapa en hook, chips y botón; subtítulo de 2 palabras con la palabra activa en amarillo; cortes de 1,7 a 2,6 s; tapa del producto y tapas de categoría insertadas como stills; placa final "365 ACTIVIDADES IMPRIMIBLES · +390 PROYECTOS · 6 BONOS".
- **B-roll (v2, 2026-10-26):** Santiago pidió sacar las visuales de **TikTok** y no de stock. Se bajaron **44 clips sin marca de agua con tikwm** (`anuncios/work/tiktoks/`) de **@dccraftlab** (máquinas de cartón con motor: escalera mecánica, portón, torre de estacionamiento, poleas, engranajes, cintas) y **@healthy.mum.and.b** (mano robótica de cartón). Se usan **27**; se descartaron los que traen cartel quemado ("Electric power gate" se recorta con `zoom`/`ybias`), los que muestran la cara del creador hablando a cámara y **dos con capturas de TikTok Studio** que se colaron en el primer render. Los **2 clips que Santiago marcó como obligatorios** (portón eléctrico y mano robótica) están anclados en los seis videos. Del stock quedan solo **5 clips de Mixkit** para las caras de chicos, que TikTok no da. Stills: 16 imágenes de la landing. Cero créditos gastados.
- **Voz a 1.30** (antes 1.22), por pedido suyo: "un poquito más de velocidad, así suena mejor".

## Reglas anti-bloqueo de este nicho
- Nada de atributos personales negativos sobre el espectador o el chico ("tu hijo es adicto", "no te presta atención"): el dolor va en primera persona ("en casa la tarde terminaba igual").
- Sin promesas de conducta ni de resultados ("deja la pantalla para siempre"), sin lenguaje médico (atención, conducta, diagnóstico).
- Sin precio en el video; como mucho "sale menos que un juguete".
- CTA "Toca Más información" + descarga inmediata y bonos.

## Preguntas abiertas
- ¿Se corre también en inglés, como el competidor? Los guiones están en neutro; traducirlos es directo.
- ¿Hay upsell después del pago? El competidor no muestra ninguno en el ad.

## Relacionado
[[funnel-hacking]] · [[guiones-y-anuncios]] · [[profesional-digital]] · [[caza-de-ofertas]] · [[ugc-y-video-generativo]]

## Fuentes
- Landing propia y biblioteca de anuncios de Croba (relevadas el 2026-10-26)
