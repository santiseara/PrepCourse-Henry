# Meta Ads 1 — ABO, CBO y las dos formas de testear (guía de clase)

> Claude Doc: https://claude.ai/artifact/TZ8mp6qzBtL4b19HLu214R
> Google Doc: https://docs.google.com/document/d/1N943ljltNzis4Kpkg930njF4t-imDHm1TQsoIiljTwk/edit
> Primer video del módulo de Meta Ads de la mentoría.

Al terminar este video hay que poder decir tres cosas sin dudar: **qué diferencia hay entre una ABO y una CBO**, **cuáles son las dos formas de testear** y **con cuánta plata se arranca**.

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

Una campaña, un conjunto, un anuncio. 5 creativos = 5 conjuntos. Da igual armarlo como 5 campañas 1-1-1 o 1 campaña con 5 conjuntos: cambia el orden, no el resultado.

**Cuánto por conjunto: entre 5 y 10 USD**

| Ticket del front | Presupuesto por conjunto |
| --- | --- |
| 15 a 19 USD | 5 USD |
| 20 USD | 7 USD |
| Tickets altos (inglés) | unos 15 USD |

Dentro de ese rango es criterio propio: 7, 8 o 10 también sirven. Lo importante es desarrollar el criterio.

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
| Conjunto | Programación | Día siguiente a las 00:00 del mercado, sin fecha de fin |
| Conjunto | Público | El país, abierto. Género solo si el producto lo pide |
| Anuncio | Formato | Subida manual, un video o imagen |
| Anuncio | Texto | Título: producto + "4.9 de 5". Botón: más información. Descripción vacía |

- **Limpieza del anuncio:** destildar multi-anunciante, apagar todas las mejoras con IA (0 de 2), quitar los comentarios.
- **Duplicar:** armás el primero → duplicás ×4 → renombrás → guardás como borrador → cambiás el video de cada uno → publicar. Solo cambia el número del nombre y el creativo.
- **Por qué 00:00 del mercado:** si largás a la tarde, Meta gasta el presupuesto del día en pocas horas.

## Forma 2 — la CBO de testeo

La última actualización de Meta, Andrómeda, pide más creativos, más variación, más ángulos. El objetivo pasa a ser darle de comer a Meta todo el día.

- **1 CBO con 3 conjuntos = 3 conceptos distintos** (el tercero suele ser venta directa: últimos cupos, garantía, últimas 24 h).
- Variaciones en **contenido flexible** dentro de cada anuncio.
- **35 USD por CBO** + una copia a 30. **4 campañas por día** (2 + 2 copias).
- **Nunca mezclar imagen y video** en la misma CBO ni en el mismo anuncio. Un ángulo que funciona se puede repetir, pero **cambiando el formato**: Meta penaliza la variación cosmética.
- Decisión: programás 00:00, entrás al mediodía siguiente. La que no vendió se corta; si el costo sube, tirón de oreja (−30%) antes de matarla.

**Para quién es cada una.** La CBO de testeo necesita máquina de creativos atrás: si no tenés volumen, se queda sin material en dos días. **El que arranca de cero va con ABO 1-1-1.** La ABO no quedó vieja.

## El CPA medio

> **CPA medio = ticket ÷ 2.** Ticket 20 → CPA medio 10.

| Modo | Presupuesto por conjunto | Para qué |
| --- | --- | --- |
| Tranquilo | 1× el CPA medio | Testeo continuo |
| Normal | 2× | — |
| **Acelerado** | **3×** | **Validar en 24 a 48 horas** |

**Regla de corte:** todo conjunto que llega al CPA medio sin una venta se apaga. Y al revés: no se decide nada antes de llegar a ese número.

- Vendió por debajo del break-even → dejarlo correr.
- Vendió una vez y el CPA quedó justo en el límite → 1 o 2 USD más de margen; si vende otra vez, el CPA se parte al medio.
- No vendió y no tiene carritos ni inicios de pago → cortar (acá sí se puede cortar antes del tope).

**Creativo ganador = 5 conversiones a buen CPA** (10+ para Pocket o Cost Cap).

## Cómo queda armada la cuenta

**Solo dos campañas fijas: pre-testeo y testeo.** No se crean campañas nuevas cada día: se suman conjuntos.

El **pre-testeo** es un filtro para ofertas ya estables: 30 anuncios por día a 1,50–2 USD (un sexto del ticket), todos de baja a las 21 h, pasan los que vendieron o tienen CPC debajo del promedio de la cuenta. De 30 creativos, 25 no funcionan: dejarlos correr hasta el break-even cuesta 375–400 USD, filtrarlos cuesta 50.

⚠️ **El que lanza de cero no hace pre-testeo: va directo al testeo con ABO 1-1-1.**

**Volumen creativo:** el ritmo es 10 anuncios nuevos por día; el mínimo, 5 cada 2 días. Porque el principio de fondo es este: **se escala por volumen creativo, no afinando la segmentación.** El targeting vive en el creativo; en público, el país abierto y listo.

## Los errores que se repiten

1. **Duplicar el mismo creativo en muchos conjuntos.** La cola de duplicados se come entre el 25% y el 75% del gasto con ROAS por debajo de 1. En una oferta, 42 de 46 campañas duplicadas no hicieron una sola venta.
2. **Juzgar una CBO conjunto por conjunto** en lugar de leerla a nivel campaña.
3. **Decidir antes del CPA medio**, para bien o para mal.
4. Dejar Advantage+ prendido con filtro duro de género.
5. Lanzar a la tarde, mezclar imagen y video y dejar prendido el 20% compartido.

## Tarea

- [ ] Calcular el CPA medio y el presupuesto por conjunto en los tres modos
- [ ] Armar una ABO de testeo con 5 conjuntos y 5 creativos, con todo el setup
- [ ] Programarla a las 00:00 del mercado
- [ ] Escribir la regla de corte con el número puesto

**Criterio de aprobación:** explicar ABO vs CBO sin mirar el documento, y decir de memoria cuánto gasta cada conjunto y a qué número se apaga.
