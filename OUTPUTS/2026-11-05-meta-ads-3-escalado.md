# Meta Ads 3 — Campañas de escalado: Cost Cap, Bid Cap y Pocket (guía de clase)

> Claude Doc: https://claude.ai/artifact/MokxS6UHE3HtrbbVaehM3G
> Tercer video del módulo de Meta Ads. Fuente: WIKI/escalado-en-meta-ads, WIKI/estructuras-cbo, WIKI/metodo-v3 (+ la skill manejo-cbo).

Arranca donde termina el anterior: la oferta ya está validada y hay anuncios ganadores. Estas estructuras no descubren nada, **exprimen lo que ya funciona**.

## Antes de tocar una estructura

**Condición de entrada:** anuncios con **5+ compras a buen CPA** (10+ para Pocket y Cost Cap).

**Los dos vectores, en orden:**
1. **Diversificación creativa** — el motor. *"Yo he escalado a 1.000, 2.000 dólares al día solamente con nuevos creativos. Ni siquiera con campañas raras."*
2. **Escala vertical** — el multiplicador.

> *"Una estructura de campaña no te va a salvar el negocio. No va a volcar un funnel negativo en uno positivo."*
> *"Cuando tenés un funnel cuya matemática da, solo es gastar más dinero en anuncios. No importa la estructura de campaña — importa muy poco."*

**Regla transversal:** no se toleran campañas con costo por resultado arriba del CPA break-even.

| Si querés… | La palanca es |
| --- | --- |
| Escalar **esta** oferta a 5 o 6 cifras por día | **Más anuncios para esta oferta** |
| Cubrir la caducidad de las ofertas | Más ofertas |

## Escala vertical: el surfeo

**Condición:** 7 a 10 compras en unos 3 días a buen CPA.

| Situación | Movimiento |
| --- | --- |
| CBO debajo de 500 USD/día | **+30% cada 3 o 4 horas** |
| CBO arriba de 500 USD/día | **+30% una vez por día** |
| ROAS por debajo de 2 | Una sola subida por día |

**Nunca más de 30% por vez.** Progresión desde 10: 10 → 12,5 → 16 → 20 → 26…

**La tabla de ayer y hoy**

| Ayer | Hoy | Qué hacés |
| --- | --- | --- |
| Bueno (2+) | Bien | +30% |
| Bajo | Mejor | Quieta |
| Bajo | Mal | −30% (tirón de oreja) |
| Los dos muy buenos (2,5–4) | — | Surfeo agresivo, volver en 3–4 h |

- **Nunca surfear con 1 venta:** 3 a 5 ventas con ROAS 2,5+.
- Si subís hoy y mañana no vende, **no vuelvas a subir**: quieta.
- **Si el CPA sube, bajá el bid**, no el presupuesto. Si deja de gastar, subí el bid y esperá una hora.
- Duplicar presupuesto **hasta que suba el CPM** (señal de saturación).
- **Reseteo nocturno**, o un escalón arriba si el día cerró muy bien.

**El techo de la cuenta:** si a 2.000 USD/día rinde y a 2.600 el ROAS se cae, el techo está cerca de 2.000. No se fuerza: **se abren otras cuentas**. Y **una campaña por cuenta publicitaria**.

## Puja automática y puja manual

**Automática ("volumen más alto"):** libertad total a Meta. Es la normal, para testear y para escalar. ("Valor más alto" es para cuando ya hay backend.)

| Manual | Qué le decís a Meta |
| --- | --- |
| **Cost Cap** | No gastes si no conseguís ventas a este CPA |
| **Objetivo de ROAS** | No gastes si no alcanzás este ROAS |
| **Bid Cap** | No pujes por encima de esto |

En las tres, si Meta no puede cumplir, **no entra a la subasta**.

> ⚠️ **Regla de reparto:** para meter más presupuesto necesitás una parte de la cuenta en manual y otra en automática. **Todo en manual no se puede**; todo en automático sí.

Un mismo ganador puede estar en varias estructuras a la vez (V3, aislada, Cost Cap, Bid Cap). No se pisan.

## Cost Cap — para reventar los días que ya vienen bien

Campaña **ABO** con objetivo de costo por resultado.

| | Valor |
| --- | --- |
| Conjuntos | **7**, todos con el mismo ganador |
| Presupuesto | 15 a 25 USD por conjunto |
| Bids | Escalonados 4, 5, 6, 7, 8, 9, 10 — el del medio ≈ **ticket ÷ 2** |

Con oferta súper validada: presupuesto **20–30 tickets** y **Cost Cap inicial = front ÷ 2 + 30%**, siempre en **cuentas nuevas**.

**Operativa:** revisar **4 veces al día** · activar a medianoche · primer vistazo 9–10 h · los que no arrancaron, cortar · los que vendieron a buen costo, duplicar presupuesto (50 → 100 → 200) · si se dispara el costo, cortar · si quema sin ventas, **−1 USD y esperar 2 h**; si no gasta, **+1 USD y esperar 2 h** · **reseteo total a la noche**.

**Es normal que casi ningún conjunto arranque:** de 49 conjuntos arrancó uno, con una compra a 3 USD. Si no arranca en dos días, subir los bids.

⚠️ **No sirve para consistencia:** es para reventar días que ya vienen bien.

**Truco:** si un conjunto validó (3 compras a 3 USD), duplicar presupuesto **y** subir el bid a la vez; el presupuesto "se patina en minutos".

**Diversificar:** 4 Cost Cap a la vez, cada una con 5 anuncios distintos en formatos y ángulos distintos.

## Bid Cap — la que aguanta las escalas más agresivas

CBO con **límite de puja** y **entrega acelerada**.

| | Valor |
| --- | --- |
| Presupuesto | Mínimo 100 USD; Bilbao arranca en **500** |
| Conjuntos | Uno por cada ganador |
| Bid inicial | **front × 1,3** (el material viejo usaba el precio del front) |
| Si no gasta | +50 centavos cada hora |
| Dónde | Cuenta nueva, aislada |

*"Si no te vende es porque tus anuncios son una mierda, o tu oferta no pega, o tenés mal redactado el landing page."*

## La intrapuja

Después de que una Cost Cap o Bid Cap encuentra su puja. Con ticket 20 y bid central 10:

1. El conjunto con bid 10 vende → surfear presupuesto.
2. **Duplicarlo 9 veces** → bids 10,1 … 10,9.
3. Si gana el 10,6 → **10,6 ×9** → 10,61 … 10,69 (la intrapuja de la intrapuja).

Para Bid Cap, igual pero arrancando en el precio del front y bajando de uno en uno.

⭐ **El atajo:** validada la puja ganadora (ej. 10,70), todos los winners nuevos van **directo a 10,70**. El test de puja se hace **una vez por oferta**, no por creativo.

## Pocket — el mismo ganador en muchas audiencias

Son **CBO**: Meta redirige la plata hacia los conjuntos que rinden.

| | CBO Pocket | Launch Pocket |
| --- | --- | --- |
| Forma | **1-8-1** | **1-10-N** |
| Qué va adentro | El mismo ganador en 8 conjuntos | 3 a 6 ganadores distintos, duplicados |
| Presupuesto | **75% del front** | **3 a 5× el front** |
| Cuándo | Tenés **un** ganador | Tenés varios |

Launch Pocket en concreto: front 10 USD → 30–50/día; front 20 → 60–100/día.

**Cómo se opera:** dejarla 48–72 h al presupuesto inicial · **cada 48 h apagar los conjuntos caros o sin gasto** · **si a las 24 h no vendió, apagar** y pasar a otro creativo · escala conservadora: cada 24 h, si el ROAS supera **1,8**, subir.

> ⚠️ **Se analiza SIEMPRE a nivel campaña**, nunca conjunto por conjunto.

## Las otras estructuras

| Estructura | Forma | Qué va adentro | Presupuesto |
| --- | --- | --- | --- |
| **Aislada** (ABO y CBO, se lanzan las dos) | 1-3-1 | El mismo ganador en 3 conjuntos | 3× el CPA medio |
| **CBO de ganadores** | 5 CBO idénticas | 3–5 conjuntos, un ganador distinto cada uno | 30/40/50/60/70 USD |
| **Mixta** | 1-4-N | 4 o 5 ganadores duplicados | Según el ticket |
| **Power** | 1-8-N | 7 u 8 ganadores duplicados | Según el ticket |
| **Winners** | 1-1-N | Los 6–10 mejores por ROAS de 7 días, clonados por post ID | ~250 USD/día, otra cuenta |
| **Micropresupuesto** | 1-10/20-1 | El mismo ganador en 10–20 conjuntos | 2,77 USD cada uno |

**El día 2 de un ganador:** con 3–5 ventas el primer o segundo día va a tres lugares a la vez: ABO aislada, CBO aislada y Cost Cap de 7 conjuntos.

> Cuidado con los ROAS altos de muestra chica: ROAS 5 con 24 USD de gasto no es un ganador, es ruido.

## La rutina de la semana

| Días | Qué se hace |
| --- | --- |
| Lunes a jueves | **Testear** — mínimo 10 creativos por día |
| Viernes a domingo | **Escalar** con Cost Cap, Bid Cap y Pocket |

Se sube el estándar por escalones: piso de 500/día → escalado el finde → 600 → la semana siguiente 700–800.

*"Yo dupliqué por 10 y al menos 5 o 6 no me han vendido."* **La mayoría de las dúplicas no vende.** Corte de una dúplica: ~4 USD sin vender.

**Error típico:** cuando un anuncio se cae, **no dupliques ese** — duplicá el original.

**La conversión se rompe al duplicar y es normal:** *"no te asustes, lo importante es que siempre mires el CPA"*.

## Tres cosas que no se olvidan

1. **Programar siempre a las 00:00.** Si programás a las 19:00, le das 6 horas para gastar 100 dólares y te lo quema.
2. **Reglas automáticas de corte** en Meta: a un alumno se le dispararon 150 USD en dos horas. Pero con corte sano (2× el ticket), no a 8 USD.
3. **Encontrar la franja horaria de la oferta:** una oferta sin momentum responde al surfeo solo hasta cierta hora; pasada esa franja el ROAS cae.

## Tarea

- [ ] Listar los anuncios con 5+ compras a buen CPA
- [ ] Calcular CPA medio (ticket ÷ 2), Cost Cap inicial (front ÷ 2 + 30%) y Bid Cap inicial (front × 1,3)
- [ ] Armar una aislada con el mejor ganador a 3× el CPA medio
- [ ] Armar una Cost Cap de 7 conjuntos con bids escalonados, en cuenta aparte
- [ ] Dejar una regla automática de corte a 2× el ticket
- [ ] Anotar el ROAS por franja horaria durante 3 días

**Criterio de aprobación:** decir sin mirar el documento cuánto sube cada surfeo y cada cuánto, el bid inicial de Cost Cap y de Bid Cap, y qué se hace cuando una campaña manual no gasta nada.
