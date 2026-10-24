# Procesadores de pago

> Stripe, Whop, MercadoPago y PayPal: qué gana y qué pierde cada uno en rechazos, disputas y velocidad de cobro, y trucos operativos de cada uno. (fuente: RAW/2026-10-10-wiki-previa/procesadores-de-pago.md)

**Cada procesador tiene un trade-off entre pagos rechazados, disputas y velocidad para cobrar.** Por eso se usan varios a la vez y nunca se concentra la plata en uno solo ([[llc-banca-y-fiscal]]).

| Procesador | Necesita LLC | A favor | En contra |
|---|---|---|---|
| **Stripe** | Sí | El estándar, menos pagos rechazados | Mira con lupa las cuentas nuevas y los picos de volumen. Las disputas casi nunca se ganan |
| **Whop** | No (verificación individual) | Multidivisa automática, más resistente a las disputas | Más pagos rechazados que Stripe en varios casos |
| **MercadoPago** | No | Mercado local | Rechazos sin motivo aparente |
| **PayPal** | No | Suma volumen | Mucha exposición a contracargos |

## Stripe

- Te liquida en **2 a 7 días hábiles**, según la antigüedad y la salud de la cuenta.
- Las cuentas nuevas están más vigiladas, sobre todo ante subas bruscas de volumen. Escalá de forma gradual.
- Si hay muchos pagos rechazados, activar **3D Secure** puede ayudar. No a todos les funcionó.
- Para pasar la revisión, publicá una página de empresa y de términos ([[disputas-y-reembolsos]]).

## Whop

- Tiene una **tarjeta propia** con la que podés usar al instante el saldo que todavía no se liquidó, pagando **~2% extra**. Si no, la liquidación normal tarda de 3 a 7 días.
- Retiros: casi siempre en **USDT** (TRC20 o Solana, menos comisión) hacia un exchange o P2P.
- **Reintento de pagos fallidos en los OTO: esperá 10–15 minutos.** Si reintentás muy rápido o muy tarde, aumentan los bloqueos.

## MercadoPago

Si empieza a rechazar pagos sin motivo, **renová las credenciales de producción** (Public Key y Access Token, o Client ID y Secret) desde MercadoPago Developers. Suele resolverse al instante.

## PayPal

Se recomienda **desactivarlo en Shopify** por el riesgo de contracargos. Hay quien lo deja por el volumen extra, asumiendo ese riesgo.

Relacionado: [[shopify-y-checkout]] · [[disputas-y-reembolsos]] · [[diagnostico-de-checkout]]

## Conexiones con tu operación actual
- **Para cobrar piedras en USD sin LLC**, Whop es una opción: verificación individual y multidivisa automática. A cambio, tiene más rechazos que Stripe ([[llc-banca-y-fiscal]]).
- **Para ofertas en AR con Mercado Pago:** si empieza a rechazar sin motivo, renovar las credenciales de producción.
- Queda abierta la pregunta de cómo cobra hoy [[scented-stones]].

## Fuentes
- RAW/2026-10-10-wiki-previa/procesadores-de-pago.md (página de la wiki previa, actualizada el 2026-09-24)
- Fuentes originales citadas (todavía no están en este cerebro): clases de la formación y experiencias de la comunidad, agosto–septiembre 2026
