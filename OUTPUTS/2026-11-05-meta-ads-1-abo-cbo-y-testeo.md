# Meta Ads 1 — ABO, CBO y las dos formas de testear (guía de clase)

> Claude Doc: https://claude.ai/artifact/TZ8mp6qzBtL4b19HLu214R
> Primer video del módulo de Meta Ads de la mentoría. Fuente: la formación de Santiago Bilbao volcada en WIKI/estructuras-cbo, WIKI/testeo-de-creativos, WIKI/setup-de-campanas, WIKI/metodo-v3.

Al terminar este módulo hay que poder decir tres cosas sin dudar: **qué diferencia hay entre una ABO y una CBO**, **cuáles son las dos formas de testear** y **con cuánta plata se arranca**.

## ABO y CBO: dónde va el presupuesto

- **ABO** (*Adset Budget Optimization*): el presupuesto va **en cada conjunto**. Vos decidís cuánto gasta cada anuncio.
- **CBO** (*Campaign Budget Optimization*): el presupuesto va **en la campaña** y **Meta lo reparte solo**.

| | ABO | CBO |
| --- | --- | --- |
| El presupuesto va en | El conjunto | La campaña |
| Quién decide cuánto gasta cada anuncio | **Vos** | **Meta** |
| Cómo se lee | Conjunto por conjunto | **A nivel campaña, siempre** |
| Un conjunto que no gasta | Es un problema tuyo | **No es un problema: Meta eligió** |
| Para qué sirve mejor | Testear | Escalar |

**La notación** campañas-conjuntos-anuncios: 1-1-1 · 1-1-5 · 1-3-1 · 1-8-1 (la Pocket, módulo 3).

⚠️ **El ajuste que convierte la ABO en CBO sin que te enteres:** "compartir hasta un 20% del presupuesto con otros conjuntos". Siempre apagada.

## Forma 1 — ABO 1-1-1

Una campaña, un conjunto, un anuncio. 5 creativos = 5 conjuntos. Da igual armarlo como 5 campañas 1-1-1 o 1 campaña con 5 conjuntos: solo cambia el orden.

**Cuánto por conjunto: entre 5 y 10 USD**

| Ticket del front | Presupuesto por conjunto |
| --- | --- |
| 15 a 19 USD | 5 USD |
| 20 USD | 7 USD |
| Tickets altos (inglés) | ~15 USD |

Bilbao usa 7, 8 o 10: *"esto es criterio propio, lo importante es que desarrolles tu propio criterio"*.

**El setup**

| Nivel | Ajuste | Valor |
| --- | --- | --- |
| Campaña | Objetivo | Ventas |
| Campaña | Presupuesto de campaña | **Desactivado** (esto la hace ABO) |
| Campaña | Nombre | `Testeo ads [fecha] [producto]` |
| Conjunto | Nombre | `[fecha] - [número]` |
| Conjunto | Conversión | Sitio web |
| Conjunto | Optimización | Maximizar el número de conversiones |
| Conjunto | Evento | Comprar (normal que no figure activo la primera vez) |
| Conjunto | Programación | Día siguiente a las 00:00 del mercado |
| Conjunto | Fecha de fin | Ninguna |
| Conjunto | Público | El país, abierto. Género solo si el producto lo pide |
| Anuncio | Formato | Subida manual, un video o imagen |
| Anuncio | Título | Producto + "4.9 de 5" |
| Anuncio | Botón | Más información |
| Anuncio | Descripción | Vacía |

**Limpieza del anuncio:** destildar multi-anunciante, apagar todas las mejoras con IA (0 de 2), quitar los comentarios.

**Duplicar:** armás el primero → duplicás ×4 en la misma campaña → renombrás → guardar como borrador → cambiás el video de cada uno → publicar. Solo cambia el número del nombre y el creativo.

**Por qué 00:00 del mercado:** si largás a la tarde, Meta gasta el presupuesto del día en pocas horas.

## Forma 2 — la CBO de testeo (post-Andrómeda)

*"Me vi afectado por la nueva actualización de Meta, Andrómeda, que nos pide más creativos, más variación, más ángulos y conceptos creativos."* El objetivo pasa a ser darle de comer a Meta todo el día.

- **1 CBO con 3 conjuntos = 3 conceptos distintos** (el tercero suele ser venta directa: últimos cupos, garantía, últimas 24 h).
- Variaciones en **contenido flexible** dentro de cada anuncio.
- **35 USD por CBO** + una copia a 30. **4 campañas por día** (2 + 2 copias).
- **Nunca mezclar imagen y video** en la misma CBO ni en el mismo anuncio.
- Se puede repetir un ángulo que funciona, pero **cambiando el formato**. Meta penaliza la variación cosmética.
- Decisión: programás 00:00, entrás al mediodía siguiente. La que no vendió se corta; si el costo sube, tirón de oreja (−30%) antes de matarla.

| | ABO 1-1-1 | CBO de testeo |
| --- | --- | --- |
| Estructura | Un anuncio por conjunto | 3 conjuntos = 3 conceptos |
| Presupuesto | 5 a 10 USD por anuncio | 35 USD por campaña |
| Por día | Una tanda | 4 campañas |
| Para quién | **El que arranca** | El que ya tiene volumen creativo |

Bilbao **no derogó la ABO 1-1-1**. Adoptó la CBO y le fue mejor, pero necesita máquina de creativos atrás.

## El CPA medio

> **CPA medio = ticket ÷ 2.** Ticket 20 → CPA medio 10.

| Modo | Presupuesto por conjunto | Para qué |
| --- | --- | --- |
| Tranquilo | 1× el CPA medio | Testeo continuo |
| Normal | 2× | — |
| **Acelerado** | **3×** | **Validar en 24 a 48 horas** |

**Regla de corte:** todo conjunto que llega al CPA medio sin una venta se apaga. Y al revés: no se decide nada antes de llegar a ese número.

| Lo que pasó | Qué hacés |
| --- | --- |
| Vendió por debajo del break-even | Dejarlo correr |
| Vendió una vez, CPA justo en el límite | 1 o 2 USD más de margen; si vende, el CPA se parte al medio |
| No vendió, sin carritos ni inicios de pago | Cortar (acá se puede cortar antes del tope) |

**Creativo ganador = 5 conversiones a buen CPA** (10+ para Pocket o Cost Cap).

## Cómo queda armada la cuenta

**Solo dos campañas fijas: pre-testeo y testeo.** No se crean campañas nuevas cada día: se suman conjuntos.

**Pre-testeo** (solo para ofertas ya estables): 30 anuncios/día (20 imágenes + 10 videos) a 1,50–2 USD (~1/6 del ticket), se dan de baja todos a las 21 h, pasan los que vendieron o tienen CPC bajo el promedio de la cuenta. La cuenta: 25 de 30 no funcionan; dejarlos correr al break-even cuesta 375–400 USD, filtrarlos cuesta 50.

⚠️ **El que lanza de cero va directo al testeo con ABO 1-1-1.**

| | Cantidad de creativos |
| --- | --- |
| Lo que saca Bilbao | 10 por día |
| El mínimo que recomienda | 5 cada 2 días |

Principio de fondo: **se escala por volumen creativo, no afinando la segmentación.** El targeting vive en el creativo. Sobre segmentación: *"acá no hay ninguna regla, todo funciona"*.

## Los errores que se repiten

1. Dejar activado "compartir hasta un 20% del presupuesto".
2. Juzgar una CBO conjunto por conjunto.
3. Mezclar imagen y video.
4. Decidir antes del CPA medio.
5. **Duplicar el mismo creativo en muchos conjuntos.** La cola de duplicados se comía entre el 25% y el 75% del gasto con ROAS 0,23–0,99 (el núcleo daba 1,10–1,69). En una oferta, 42 de 46 campañas duplicadas no hicieron una sola venta.
6. Dejar Advantage+ prendido con filtro duro de género.
7. Lanzar a la tarde.

## Tarea

- [ ] Calcular el CPA medio y el presupuesto por conjunto en los tres modos
- [ ] Armar una ABO de testeo con 5 conjuntos y 5 creativos, con todo el setup
- [ ] Programarla a las 00:00 del mercado
- [ ] Escribir la regla de corte con el número puesto

**Criterio de aprobación:** explicar ABO vs CBO sin mirar el documento, y decir de memoria cuánto gasta cada conjunto y a qué número se apaga.
