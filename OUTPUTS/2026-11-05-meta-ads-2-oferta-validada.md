# Meta Ads 2 — Cómo saber si la oferta está validada (guía de clase)

> Claude Doc: https://claude.ai/artifact/TRb1YibGiWkMCCWg7pVo8A
> Segundo video del módulo de Meta Ads. Fuente: WIKI/metricas-y-kpis, WIKI/validacion-de-oferta, WIKI/lectura-de-resultados.

La pregunta del módulo es una sola: **¿entra más plata de la que sale?**

## Todo el negocio son dos números

> **Costo por visita contra revenue por visita.** La diferencia es la ganancia por visita.

```
Costo por visita   = lo que gastaste  ÷ visitantes
Revenue por visita = lo que facturaste ÷ visitantes
```

100 USD y 200 visitas → 0,50 de costo por visita. Si facturan 200 USD → 1 USD de revenue por visita → **ROAS 2**.

El revenue por visita se sube de dos formas nada más: **mejor conversión** o **mejor AOV**.

**Meta cobra por impresión: gana el que menos impresiones necesita para una conversión.** Funciona igual en venta directa, VSL o quiz.

| Familia | Qué mide | Se arregla con |
| --- | --- | --- |
| De anuncio | El costo por visita | Mejores creativos |
| De conversión | El revenue por visita | Mejor funnel y oferta |

## El CPA break-even

Lo que entra **neto en la cuenta** por cada venta, descontadas comisiones y conversión de moneda. Ejemplo: vendés a 19.000 pesos, te entran 17.000, dólar a 1.200 → **14,16 USD**.

⚠️ **Con upsells el break-even no es el precio del front.** Agregar en Meta la columna **valor de conversión de compras promedio**: si el front son 17 pero el valor real es 25, juzgar contra 17 apaga conjuntos que ganan plata.

## Los números de la validación

| Parámetro | Valor |
| --- | --- |
| Presupuesto máximo para validar | **100 USD** |
| Plazo | 1 semana |
| Test inicial típico | 6 creativos (3 foto + 3 video) a 5,50–6,50 USD |

> **Si con 100 USD no hay una sola venta, se cambia de oferta.**

**El error de dar "un poco más de chance":** un equipo mataba las ofertas a 200–250 USD en vez de a 100–150 → **600–700 USD de pérdida y ni una oferta en profit**. *"Tirar más rápido y desapegarse más rápido. Si estás 600 abajo, con una oferta buena a las 9 de la mañana ya lo recuperaste."* El costo de alargar una oferta muerta es el tiempo que no estuviste testeando la siguiente.

**Pero: 20 anuncios antes de abandonar la oferta.** Si los 5 primeros no van, 5 más al día siguiente. El presupuesto acota el gasto; los 20 anuncios acotan la conclusión.

> *"Cuando lanzás una oferta nueva no estás gastando dinero: estás comprando datos."*

## Qué se mira, y en qué orden

**1. Costo por visita, en las primeras horas.** Asumís comprate del 2%. Ticket 15 → 100 visitas = 2 compras = 30 USD. Si el costo por visita es 0,30 estás en break-even exacto. Si es 1 USD, necesitarías 7% de conversión: descartar.

**2. Costo por compra contra lo que entra neto.** Oferta validada = creativos con costo por compra menor a lo que ingresa en la cuenta bancaria.

**3. La señal inequívoca:** *"entra más dinero a tu cuenta del que sale"*, normalmente el primer o segundo día.

## Oferta validada ≠ creativo validado

| | Qué significa | Qué habilita |
| --- | --- | --- |
| **Oferta validada** | Convierte y el CPA cierra | Backend y escala |
| **Creativo validado** | Ese anuncio tiene 5+ conversiones a buen CPA | Estructuras de escala (10+ para Pocket o Cost Cap) |

Hay un caso de validación relámpago (3 ventas en 2 horas → directo a Cost Cap) que Bilbao marca como excepción: *"capaz que era un vicio"*. Lo normal es esperar las 5 conversiones.

## Los KPIs

**De anuncio**

| Métrica | Referencia |
| --- | --- |
| CPC | LatAm 0,10–0,50 USD · EE.UU. hasta 1 USD |
| CTR | 1,5–2% mínimo, ideal 2,5%+ |
| Hook rate (3 s ÷ impresiones) | Estándar 30%; **Bilbao exige >50%** |
| Retention (thruplays ÷ impresiones) | Estándar 5%; **él exige >10%** |
| CPM | Sin número fijo |
| Frecuencia | No debe dispararse al escalar en frío |

El CPC es la métrica por excelencia: dice si el funnel va a estar en positivo antes de tener ventas. Duplicar el CTR es partir el CPC al medio.

**De conversión**

| Métrica | Referencia |
| --- | --- |
| Comprate (compras ÷ visitas a landing) | 2%+, y 2,5% antes de escalar |
| Visita → inicio de checkout | 10%+ |
| Inicio de checkout → compra | 25–30% |
| AOV ÷ front | 1,5+ (hasta 2–2,5 en digitales) |

⚠️ **Ninguna métrica se juzga sola.** Con CPM regalado se tolera CTR de 0,5%. Se mira el conjunto, buscando el cuello de botella.

## Si no hay ganancia, casi nunca es el anuncio

**1. Que los números sean reales.** Una semana que figuraba con +800 USD daba pérdida con el 8–10% de comisión. Mirar las ventas pendientes (109 pendientes contra 232 aprobadas en una oferta).

**2. ¿Anuncio o landing?** Con CTR de link 4–7% y hook 40–60%, el anuncio está sobre el promedio. La métrica que separa ganadores de perdedores es **cuántos pasan de la landing al pago**:

| Anuncios | ROAS | Inician el pago de cada 100 |
| --- | --- | --- |
| Ganadores | 1,14+ | ~15 |
| Neutros | ~1,0 | ~12,5 |
| Perdedores | 0,69− | ~10 |

El anuncio con mejor retención de una semana vendió cero. Los relevos tenían peor hook (0,45–0,52 vs 0,60) pero casi el doble pasando al pago. Llevar ese paso de 8,8% a 12% dio +83 ventas por semana y el ROAS pasó de 1,04 a 1,42.

**3. Tarjetas rechazadas.** 1 de cada 4 pagos rechazado (23%). Subir la aprobación del 75% al 88% + arreglar la landing llevó el ROAS de 1,05 a 1,53.

**4. Backend.** AOV ÷ front = 1,5 objetivo; las sanas dieron 1,94 y 2,02. El OTO más caro casi no vendía (2,6%) contra el primero al 30%.

**5. La cuenta.** Mismos anuncios, una cuenta perdía por CPM 45% más caro. Un solo creativo con el 79% del gasto semanal es una alarma.

**6. Horario y presupuesto.** De 12 a 20 h se perdía todo (ROAS 0,78 con el 34% del presupuesto); de 20 a 00 h se ganaba (1,36) con el 9%. Y el ROAS baja al subir el gasto: 178 USD/día → 1,30 · 306 → 1,17 · 652 → 0,98 · 1.232 → 0,93.

## Los tres errores de lectura más caros

**1. Mirar el día suelto.** *"Hasta invirtiendo 200 dólares al día hubo un día que no vendí nada… generalmente ves el día malo."* Se analiza en "máximo", o con promedios de 3, 7 y 15 días. La decisión va sobre el CPA acumulado.

**2. Decidir sin comisiones.** ROAS con ventas **aprobadas** y comisiones cargadas: con 8–10%, el equilibrio real está en **ROAS ~1,10**. El ROAS del píxel viene inflado: sirve para ordenar, no como valor.

**3. Reglas automáticas que cortan temprano.** Con CPA real ~20 USD, una regla que cortaba a 8 USD tenía **67% de probabilidad de matar un conjunto sano**: dos de cada tres tests buenos, y casi el 9% del gasto semanal. **Corte sano: ~2 veces el ticket.**

**Diagnóstico de un día malo, en orden:** inicio de checkout ÷ visitas → AOV ÷ front → compras ÷ inicios de checkout. Casi siempre bajó el último: *"no es que tu funnel no funcione: son tus ads, nada más. No toques nada."* La respuesta es más anuncios.

## Cuando ya está validada

1. **Backend** para subir el ROAS antes de escalar fuerte.
2. **Escalar**, y recién después pensar en otra oferta. Una sola oferta hasta 1.000–2.000 USD por día.

Expectativa: **de 6 ofertas validadas, solo 1 escala agresivo.** Validar no es escalar.

## Tarea

- [ ] Calcular el CPA break-even real
- [ ] Cargar comisiones, impuestos y costo de producto en el panel
- [ ] Agregar la columna "valor de conversión de compras promedio"
- [ ] Escribir los dos números de corte: el del conjunto (CPA medio) y el de la oferta (100 USD y 20 anuncios)
- [ ] Revisar la oferta actual con los 6 pasos de diagnóstico

**Criterio de aprobación:** decir sin mirar el documento el CPA break-even, con qué número se considera validada una oferta, y qué se mira primero cuando un día da pérdida.
