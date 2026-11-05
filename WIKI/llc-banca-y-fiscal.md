# LLC, banca y estructura fiscal

> LLC en EE.UU. para Stripe y Shopify Payments, ITIN, bancos (Mercury, Relay), diversificar fondos, cripto para pagar Meta e impuestos. (fuente: RAW/2026-10-10-wiki-previa/llc-banca-y-fiscal.md)

**Para vender en serio desde fuera de Estados Unidos, la estructura habitual es una LLC en Estados Unidos.** Habilita Stripe y Shopify Payments, y da menos pagos rechazados que operar como persona física.

## La LLC

- **Mantenimiento anual:** tasa estatal + agente registrado + declaración de impuestos. Referencia: **~350–400 USD por año** en total.
- Muchas gestorías cobran un margen alto sobre el costo real del trámite estatal. Compará antes de contratar.
- Cargar la **dirección de facturación de la LLC** en la "Información del negocio" del Business Manager ayuda a subir el límite de gasto de Meta ([[problemas-de-cuentas-meta]]).

## ITIN

Hace falta para algunos productos bancarios de Estados Unidos si no sos residente. La espera típica es de **3 a 6 meses**. Arrancá el trámite antes de necesitarlo.

## Bancos

- **Mercury** y **Relay** son los bancos digitales más usados para cuentas de LLC. Tienen tarjetas de débito virtuales y físicas sin comisión.
- La tarjeta de crédito se habilita después de mantener un saldo de **~15.000 USD**.

## Regla de oro: diversificar

**Nunca tengas el 100% de la plata en un solo procesador o banco.** Cualquiera te puede congelar los fondos sin aviso. Repartí entre Stripe, Whop, Mercury y cripto ([[procesadores-de-pago]]).

## Cripto para pagar Meta Ads

- **USDT** (redes TRC20 o Solana) para mover fondos con menos comisión que las apps de cambio.
- Hay **tarjetas cripto con 1,5–3% de cashback** que se usan específicamente para pagar Meta Ads.

## Impuestos

- **Llevá la contabilidad al día desde el principio.** Es parte de construir un negocio de largo plazo.
- Nota para Argentina: hoy, la plata que pasa por plataformas extranjeras puede quedar fuera del régimen local de información automática. Los acuerdos internacionales de intercambio (CARF, CRS, DAC8) van a cerrar ese hueco en **2–3 años**. Tratalo como algo temporal. Esto no es asesoramiento fiscal: consultalo con un contador.


## Lo que hay que PRESENTAR en EE.UU. aunque no pagues nada (verificado 2026-11-05)

**No pagar no es lo mismo que no presentar, y ahí está la multa de 25.000 USD.**

- **Income tax:** un no residente paga impuesto federal solo si está *engaged in a US trade or business* y tiene renta efectivamente conectada (**ECI**). Eso se configura con presencia real: oficina, empleados, un agente dependiente en EE.UU. o trabajar estando allá. Vendiendo un PDF o un curso desde Argentina, **en general no hay ECI ni impuesto federal**. Lo rompe un producto físico con stock o depósito en EE.UU.
- **Form 5472 + Form 1120 pro forma:** obligatorio para toda LLC de un miembro extranjero, **aunque no haya facturado un dólar**. Lo dispara cualquier operación reportable, hasta un aporte de 1 USD. Vence el **15 de abril** (15 de octubre con Form 7004). **No se puede presentar online**: correo o fax.
- **Multa: 25.000 USD** por formulario y por año, más 25.000 cada 30 días si no se responde la notificación del IRS, sin tope. **La prescripción no empieza a correr hasta que se presenta.** Es la trampa de la LLC abierta "por si acaso" y dejada dormida.
- **BOI (beneficiario final):** las LLC formadas en EE.UU. quedaron **exentas** por la regla interina de FinCEN del **26 de marzo de 2025**. Solo siguen presentando las entidades extranjeras registradas en un estado.
- **Costo estatal de referencia:** Wyoming ~60 USD de annual report, New Mexico sin annual report, Delaware 300 USD de franchise tax, California 800 USD mínimo.

### Sales tax y VAT: un test aparte

- **Sales tax es por estado y no tiene nada que ver con el income tax.** Funciona por *economic nexus*: pasado el umbral del estado (referencia habitual **100.000 USD o 200 transacciones**, varía) hay que registrarse y cobrar. **Muchos estados sí gravan los productos digitales**, y las ventas no gravadas igual cuentan para el umbral.
- **Reino Unido y la UE:** el IVA de servicios digitales a consumidores **se debe desde la primera venta**; para un vendedor de fuera no hay umbral mínimo.
- Con Stripe esto lo configurás vos (Stripe Tax). Con Whop lo puede hacer la plataforma, ver abajo.

### Los tres modos de impuestos de Whop (de sus términos de vendedor)

Whop es *merchant of record* **solo** a efectos de las reglas de las redes de tarjetas y la liquidación del pago; para impuestos, defensa del consumidor y licencias de contenido **el vendedor es el usuario**.

| Modo | Quién cobra | Quién declara | Costo |
|---|---|---|---|
| Whop cobra y declara | Whop | Whop | **2 % por transacción**; solo 18 estados de EE.UU., Reino Unido y países de la UE |
| Whop calcula, vos declarás | Whop | Vos | 2 % por transacción |
| Vos te ocupás (default) | Nadie | Vos | Sin costo extra |

Otras cláusulas que conviene tener presentes: **tasa de disputas por debajo del 1 %** en 90 días rodantes o te cierran la cuenta ([[disputas-y-reembolsos]]), reservas de **hasta el 100 % de los fondos** y **1,5 % mensual** de interés sobre saldo negativo.

### Y el lado argentino

**Argentina grava a sus residentes fiscales por renta mundial**, y la LLC transparente no saca al dueño del medio: justamente porque no paga impuesto propio, la renta se le atribuye a él. Vender al exterior **no lleva IVA argentino** (exportación de servicios), pero facturado **sí cuenta para el tope del monotributo** ([[impuestos-en-argentina]]).

El costo real de no declarar no es el consumo diario: es el **origen de fondos** el día de una compra grande. Y el hueco se cierra con CARF, CRS y DAC8 en 2–3 años. Esto no es asesoramiento fiscal.

(fuente: OUTPUTS/2026-11-05-modulo-7-impuestos-argentina-y-exterior.md · https://www.taxesforexpats.com/articles/foreign-business/foreign-owned-single-member-llc.html · https://whop.com/seller-terms/ · https://www.numeral.com/blog/sales-tax-on-digital-goods)

Relacionado: [[procesadores-de-pago]] · [[impuestos-en-argentina]] · [[disputas-y-reembolsos]] · [[shopify-y-checkout]]

## Conexiones con tu operación actual
- **[[scented-stones]] cobra en USD a Tier 1.** No sé si lo hacés con LLC + Stripe, con Impultienda o con Hotmart. Queda como pregunta abierta en [[perfil-y-negocio]].
- **Regla de diversificar:** con un solo winner, que te congelen fondos en un procesador es un riesgo directo. Conviene repartir.
- La nota fiscal para Argentina no es asesoramiento: consultalo con un contador.

## Fuentes
- RAW/2026-10-10-wiki-previa/llc-banca-y-fiscal.md (página de la wiki previa, actualizada el 2026-09-24)
- Fuentes originales citadas (todavía no están en este cerebro): clases de la formación y experiencias de la comunidad, agosto–septiembre 2026
