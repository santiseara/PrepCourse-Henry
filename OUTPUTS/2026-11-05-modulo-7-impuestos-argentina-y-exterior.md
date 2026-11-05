# Módulo 7 — Impuestos: vender en Argentina y vender afuera

> Guía de clase de la mentoría. Claude Doc: https://claude.ai/artifact/2y1AdsWcAioGyRfuakKkeB
> Fecha: 2026-11-05

## El punto del módulo

Lo impositivo no hace vender un peso más, pero mal armado te frena el negocio: te traba el cobro, te come margen sin que lo veas o te deja expuesto cuando ya facturás en serio. Este módulo te da el mapa de los dos escenarios y nada más.

**Las tres reglas madre**

1. **Primero vendé, después estructurá.** Ninguna estructura sirve si no hay oferta validada. El alta de monotributo se hace en un día; la LLC recién tiene sentido cuando ya hay facturación afuera.
2. **Un camino por mercado.** Argentina = monotributo y factura local. Afuera = plataforma que cobra por vos (Whop) y, cuando hay volumen, LLC + Stripe. No se mezclan.
3. **El costo impositivo entra en el cálculo de la oferta.** Si vendés en Argentina, Ingresos Brutos y la cuota salen del margen de cada venta. Si no lo contás antes, el ROAS que creés que tenés no es el que tenés.

**Qué no es este módulo:** no es asesoramiento contable. Es el mapa para que entiendas qué te están cobrando y qué estás firmando. La implementación se cierra con un contador, y los montos se verifican en ARCA el día que te das de alta porque se actualizan cada seis meses.

# PARTE 1 — VENDER EN ARGENTINA

## El mapa en un cuadro

De toda la lista de impuestos que existen en Argentina, vendiendo infoproductos te tocan **dos** si sos monotributista y **cuatro** si sos responsable inscripto. El resto no entra.

| Impuesto | ¿Te toca? | El dato clave |
| --- | --- | --- |
| **Monotributo** (cuota mensual) | Sí, si estás en el régimen | Cuota fija única que reemplaza IVA, Ganancias y jubilación |
| **Ingresos Brutos** (provincial) | **Sí, siempre** | Es el que de verdad pagás por vender. Monotributista: cuota fija. Responsable inscripto: porcentaje sobre lo facturado |
| **IVA** (21%) | No, si lo que vendés es un libro digital | Exento por ley, cualquiera sea el soporte. Un curso o una membresía no es un libro: eso sí paga IVA cuando sos responsable inscripto |
| **Ganancias** | Monotributo: no. Responsable inscripto: sí | Escala progresiva sobre la ganancia (ingresos menos gastos), no sobre la facturación |
| **Aportes jubilatorios y obra social** | Sí | Monotributo: van dentro de la cuota. Responsable inscripto: autónomos, se paga aparte |
| **Impuesto al débito y crédito** (al cheque) | Monotributista: no | Los monotributistas están exentos sobre su cuenta declarada. Responsable inscripto: sí, 0,6% por lado |

**Lo que hay que retener:** el monotributo no es un impuesto, es un régimen que te junta tres cosas en una cuota. Y el impuesto invisible del negocio es Ingresos Brutos, porque se paga sobre la venta aunque pierdas plata.

## Monotributo: por dónde se arranca

Arrancás monotributista. Siempre. Es el alta más simple que existe, la hacés online en el día y te deja facturar legalmente desde la primera venta.

**El alta, en orden**

1. CUIT y Clave Fiscal nivel 3 en ARCA (ex AFIP).
2. Declarás domicilio fiscal y constituís domicilio electrónico.
3. Elegís **código de actividad**. De acá sale tu alícuota de Ingresos Brutos, así que no es un trámite menor.
4. Elegís **categoría** por facturación anual estimada. Si arrancás de cero, categoría A.
5. Elegís obra social (o la pagás sin usarla, pero igual va en la cuota).

**Las categorías, con los valores vigentes desde agosto de 2026**

Los topes son de **facturación anual acumulada de los últimos 12 meses**, no por año calendario.

| Cat. | Tope de facturación anual | Cuota mensual (servicios) |
| --- | --- | --- |
| A | $12.009.410 | $49.527 |
| B | $17.595.182 | $56.379 |
| C | $24.670.494 | $66.020 |
| D | $30.628.651 | $84.614 |
| E | $36.028.231 | $119.811 |
| F | $45.151.659 | $150.784 |
| G | $53.995.798 | $230.612 |
| H | $81.924.660 | $522.706 |
| I | $91.699.761 | $963.747 |
| J | $105.012.519 | $1.167.299 |
| **K** | **$126.610.830** | $1.614.446 |

Valores de la tabla ARCA vigente desde agosto de 2026 (fuente: iprofesional). Se actualizan cada seis meses: la próxima corrección es en enero de 2027, así que el día que lo uses, chequealo en ARCA.

**Los tres números que importan**

- **$126.610.830 al año** es el techo de la categoría K. Pasado eso, se termina el monotributo y pasás a responsable inscripto.
- **Recategorización cada 6 meses** (enero y julio): mirás los últimos 12 meses facturados y te acomodás a la categoría que corresponde. Es obligatorio, y si no lo hacés te recategorizan de oficio.
- **Se controla por lo facturado, no por lo que te queda.** Si vendés $50 millones y ponés $35 millones en Meta, tu categoría sale de los $50 millones. Este es el error que revienta a todo el mundo que escala ads: la categoría sube por el volumen bruto, no por la ganancia.

**Lo que te deja el monotributo:** facturás, cobrás por Mercado Pago y plataformas sin problemas, y pagás una cuota fija que ya trae IVA, Ganancias y jubilación adentro. Para un negocio que arranca es imbatible.

## Cómo facturar en la práctica

La app oficial de ARCA funciona, pero es incómoda: se cuelga, te saca la sesión y para facturar diez ventas perdés media hora. **Usá Facturitas**: se conecta a tu CUIT, emite el mismo comprobante fiscal y hacés una factura en diez segundos desde el teléfono.

| Qué | Monotributista | Responsable inscripto |
| --- | --- | --- |
| Tipo de comprobante | **Factura C** | Factura B a consumidor final, A a empresas |
| IVA discriminado | No lleva | Sí, 21% (salvo exento) |
| A quién le facturás | Consumidor final | Según el comprador |

**Las reglas de la operación**

- **Facturás la venta, no el cobro.** La plata entra por Mercado Pago, Impultienda o la plataforma que uses; eso no es la factura. La factura la emitís vos igual.
- **Consumidor final:** ponés el monto, concepto "productos digitales" y listo. No necesitás los datos del comprador si la venta es chica.
- **No hace falta una factura por cada checkout.** Si vendés cien unidades de $15.000 por día, se puede trabajar con comprobantes por lote. Esto te lo arma el contador una vez y después es rutina.
- **El código de actividad define tu Ingresos Brutos.** Elegí el que describe lo que vendés de verdad (edición de libros, enseñanza no formal, servicios digitales). Poner un código que no corresponde es el camino corto a una inspección provincial.
- **Guardá todo:** facturas emitidas, liquidaciones de la plataforma de cobro, gastos de Meta Ads, herramientas. El día que pasás a responsable inscripto, los gastos te bajan Ganancias; si no los tenés documentados, no existen.

## IVA: el libro no paga, el curso sí

Acá está el dato fino que casi nadie chequea y que **te cambia el 21% del precio** el día que sos responsable inscripto.

**Lo que dice la ley**

- El art. 7 inc. a) de la Ley de IVA exime a los **libros**, y desde la reforma de 2018 la exención alcanza al libro "cualquiera sea su soporte o el medio utilizado para su difusión". El formato digital entra.
- El Dictamen 70/2010 (DAT) confirmó que la exención vale **incluso si el libro se descarga o se lee desde un sitio web**, con dos condiciones: que la modalidad reemplace la venta del libro tradicional, y que no tenga funciones que desvirtúen su naturaleza de libro.
- El mismo dictamen aclara qué se cae de la exención: **ejercicios interactivos y aplicativos de software**. En cambio el buscador interno y la posibilidad de imprimir no te sacan del beneficio.

**Cómo se traduce a nuestras ofertas**

| Lo que vendés | ¿Lleva IVA siendo responsable inscripto? |
| --- | --- |
| Ebook, PDF, guía, recetario, libro de patrones | **No**, exento |
| Pack de imágenes o imprimibles | Zona gris: discutilo con el contador |
| Curso en video, clases, membresía, comunidad | **Sí**, 21% |
| Software, app, herramienta interactiva | **Sí**, 21% |
| Servicio o consultoría | **Sí**, 21% |

**Las dos consecuencias prácticas**

1. **Como monotributista esto no te cambia nada hoy**, porque la cuota ya reemplaza el IVA. Importa el día que cruzás a responsable inscripto: si tu producto es un libro digital, seguís sin IVA y tu margen no se mueve. Si es un curso, de golpe el 21% del precio no es tuyo.
2. **Esto se decide cuando armás la oferta, no después.** Un entregable construido como libro digital es, además de más rápido de producir, estructuralmente más barato de facturar en Argentina.

> **Ojo con el antecedente:** en octubre de 2024 el Gobierno eliminó la exención de IVA para diarios, revistas y suscripciones digitales. Los libros quedaron afuera de ese recorte, pero muestra que la exención no es intocable: antes de armar el precio de una oferta grande, confirmá el texto vigente.

## Ingresos Brutos: el que sí se paga siempre

Es un impuesto **provincial**, no nacional, y es el único que se paga por el solo hecho de vender: se calcula sobre la facturación, no sobre la ganancia. Si vendés a pérdida, igual lo pagás.

**Siendo monotributista**

| Jurisdicción | Cómo lo pagás |
| --- | --- |
| **CABA** | Desde enero de 2026 entró el **Monotributo Unificado**: el IIBB del régimen simplificado se paga junto con la cuota nacional, en un solo pago. A los que ya estaban en IIBB Simplificado los incorporaron de oficio |
| **Provincia de Buenos Aires** | ARBA tiene su propio régimen simplificado, con cuota fija por categoría. La adhesión es **optativa** |
| **Resto de las provincias** | Casi todas tienen régimen simplificado propio, algunas unificado con ARCA. Se verifica en la agencia de rentas de tu provincia |

Orden de magnitud en CABA, vigente desde enero de 2026: **$22.485 por mes en categoría A** y **$237.015 en K**, encima de la cuota nacional. Se actualiza, así que el número del día se chequea en AGIP.

**Siendo responsable inscripto (o fuera del simplificado)**

- Pagás un **porcentaje sobre lo facturado** cada mes. La alícuota sale de tu código de actividad y de tu tramo de facturación, no del canal por el que vendiste.
- Referencia CABA 2026: **3% hasta el umbral de ingresos y 5% por encima** (Ley Impositiva 2026). En Provincia de Buenos Aires el general ronda el 5% con alícuotas reducidas por tramo.
- **Ese 3–5% sale directo del margen de cada venta.** Entra en el cálculo del ticket igual que la comisión de la pasarela.

**Convenio Multilateral:** aparece cuando tu actividad tiene sustento territorial en más de una provincia. Con un negocio digital operado desde un solo domicilio fiscal, en la práctica tributás donde estás. Es una de las primeras cosas a confirmar con el contador, porque las agencias provinciales son las que más rápido te detectan por las retenciones de las pasarelas de pago.

## Cuándo pasás a responsable inscripto

Pasás cuando cruzás el tope de la categoría K ($126,6 millones al año) o cuando te conviene antes. **Responsable inscripto no tiene límite de facturación**, y eso es lo que te deja escalar sin techo.

| | Monotributista | Responsable inscripto |
| --- | --- | --- |
| Techo de facturación | $126,6 millones/año | **Sin techo** |
| Qué pagás | Una cuota fija | IVA mensual + Ganancias anual + autónomos |
| Base de cálculo | Tu categoría | IVA sobre ventas, Ganancias sobre **la ganancia** |
| Gastos | No se deducen | **Se deducen todos** (Meta Ads, herramientas, honorarios) |
| Crédito fiscal de IVA | No existe | Recuperás el IVA de lo que comprás |
| Contador | Opcional | Obligatorio, todos los meses |

**El punto que casi nadie ve**

En este negocio, entre el 50% y el 70% de la facturación se va en Meta Ads. Como monotributista en K, pagás $1,6 millones por mes **sin poder descontar un peso de eso**. Como responsable inscripto, Ganancias se calcula sobre lo que te queda después de los ads, y el IVA de la factura de Meta te vuelve como crédito fiscal.

Conclusión: con mucho gasto publicitario, cruzar a responsable inscripto puede salir **más barato** que quedarse arriba del monotributo, no más caro. Es un cálculo que se hace con el contador con tus números reales, no una regla fija.

**Lo que se suma a la rutina**

- Declaración mensual de IVA y Libro de IVA Digital.
- Ganancias anual con escala progresiva que llega al **35%** sobre la ganancia neta, con anticipos a cuenta durante el año.
- Aportes de autónomos mensuales.
- Retenciones y percepciones que te van a aplicar clientes y plataformas.
- Honorarios de contador todos los meses.

**El paso siguiente** es pasar de persona física a sociedad (SRL o SAS). Tiene sentido cuando hay socios, cuando querés separar tu patrimonio del del negocio o cuando el volumen justifica la estructura. No es un tema del arranque.

## Las retenciones de las plataformas de cobro

Cuando cobrás por Mercado Pago o una billetera, te descuentan plata antes de que te llegue. **No es un impuesto nuevo: es un adelanto de Ingresos Brutos.** El problema no es la retención, es no computarla: ahí sí pagás dos veces.

| Qué te descuentan | Qué es | ¿Le aplica al monotributista? |
| --- | --- | --- |
| **SIRTAC** | Retención de IIBB sobre cobros con tarjeta | **Sí.** La alícuota sale del padrón de tu provincia; el 3% es una referencia común |
| **SIRCUPA** | Retención de IIBB sobre acreditaciones en cuentas de pago y billeteras | **Sí.** Provincia de Buenos Aires adhirió en septiembre de 2025 |
| **IVA y Ganancias** | Las viejas retenciones de la RG 4622 | **Ya no.** La RG 5554/2024 derogó esos regímenes para pagos desde el 1/9/2024 |
| **Percepción de IVA** (RG 5319) | La aplican marketplaces tipo Mercado Libre | 0% mientras estés dentro de los parámetros del monotributo; 7% si los excedés |

**Cómo no pagarlo dos veces**

- Las retenciones de IIBB se computan como **pago a cuenta** en tu declaración provincial. El contador las carga todos los meses con el certificado de la plataforma.
- **Si te retienen en una jurisdicción donde no estás inscripto, esa plata no tiene contra qué imputarse.** Es la pérdida silenciosa más típica del que vende online a todo el país.
- Si te queda saldo a favor permanente, se pide **reducción de alícuota** en la provincia. Y las últimas 12 declaraciones se pueden revisar para recuperar saldos no computados.

**La regla operativa:** medí el margen con **el neto que te liquidan**, no con el precio de venta. Entre comisión de la pasarela y retenciones, entre el precio del checkout y lo que entra a tu cuenta hay varios puntos de diferencia.

## Checklist y los errores que se repiten

**Lo que hay que tener armado antes de la primera campaña**

- [ ] CUIT con Clave Fiscal nivel 3
- [ ] Alta de monotributo con el código de actividad que corresponde
- [ ] Alta o adhesión a Ingresos Brutos de tu provincia
- [ ] Facturitas instalada y conectada al CUIT
- [ ] Cuenta bancaria y cuenta de pagos **declaradas en ARCA**
- [ ] Carpeta mensual de comprobantes de gastos (Meta, herramientas, dominios)
- [ ] Recordatorio de recategorización en enero y julio
- [ ] Contador que entienda cobros digitales, no uno de kiosco

**Los seis errores que se repiten**

1. **Creer que la categoría se calcula sobre la ganancia.** Se calcula sobre lo facturado bruto. Es el error que te excluye del régimen escalando ads.
2. **No facturar porque "cobro por plataforma".** La plataforma te liquida plata; no emite tu factura. Y lo que entra por ahí queda registrado.
3. **No declarar la cuenta por donde entra la plata.** Te deja afuera de la exención del impuesto al cheque y te llena de retenciones.
4. **Elegir el código de actividad por descarte.** De ese código sale tu alícuota de Ingresos Brutos para siempre.
5. **No recategorizarse.** Te recategorizan de oficio, con multa, y en el peor caso te excluyen del régimen.
6. **Mezclar la plata del negocio con la personal.** Sin separación no sabés tu margen real y la contabilidad se vuelve imposible de reconstruir.

# PARTE 2 — VENDER AFUERA (EN INGLÉS)

## Los dos caminos para cobrar afuera

Para vender en inglés hay dos caminos y **no son etapas obligatorias: son dos niveles**. Se arranca por el primero.

| | **Whop, sin LLC** | **LLC + Stripe** |
| --- | --- | --- |
| Qué necesitás | Verificación individual, con tu documento | LLC constituida, EIN, banco y dirección en EE.UU. |
| Tiempo hasta cobrar | Horas | 1 a 3 semanas (la LLC en días, el banco después) |
| Costo de apertura | $0 | **400–500 USD** |
| Costo anual | $0 | **350–400 USD** (tasa estatal + agente registrado + declaración) |
| Pagos rechazados | Más que Stripe | **Menos**: es el estándar del mercado |
| Disputas | Más resistente a los contracargos | Casi nunca se ganan |
| Liquidación | 3 a 7 días, o al instante con su tarjeta pagando ~2% | 2 a 7 días hábiles |
| Cómo sacás la plata | **USDT** (TRC20 o Solana) a exchange o P2P | Cuenta en Mercury o Relay |
| Riesgo principal | Más rechazos en el checkout | **Bloqueos y reservas** ante picos de volumen |
| Para qué etapa | Validar y escalar sin estructura | Cuando el volumen ya justifica la estructura |

**La decisión, en una línea:** Whop para empezar y para cualquiera que no quiera estructura. LLC + Stripe cuando los puntos de conversión extra del checkout valen más que el riesgo de que te congelen la cuenta.

## Whop sin LLC: el camino cómodo

Whop te deja cobrar en dólares sin empresa, sin EIN y sin banco afuera. La verificación es **individual**, con tu documento. Es el camino por el que arranca cualquiera.

**Cómo funciona en la práctica**

- Cobra en múltiples monedas de forma automática.
- Liquidación en **3 a 7 días**. Con la tarjeta propia de Whop usás el saldo no liquidado al instante pagando **~2% extra**.
- Los retiros salen casi siempre en **USDT** (TRC20 o Solana, menos comisión) hacia un exchange o P2P.
- En los OTO, si un pago falla, el reintento va a los **10 a 15 minutos**: antes o después sube el bloqueo.

**Lo que dice el contrato y conviene saber antes**

De los términos de vendedor de Whop (https://whop.com/seller-terms/):

- Whop actúa como *merchant of record* **solo** a efectos de las reglas de las redes de tarjetas y de la liquidación del pago. Para todo lo demás —impuestos, defensa del consumidor, licencias de contenido— **el vendedor sos vos**.
- Hay **tres modos de impuestos**, y el que elegís define quién se come el problema:

| Modo | Quién cobra | Quién declara | Costo |
| --- | --- | --- | --- |
| **Whop cobra y declara** | Whop | Whop | **2% por transacción**. Solo en 18 estados de EE.UU., Reino Unido y países de la UE |
| **Whop calcula, vos declarás** | Whop | **Vos** | 2% por transacción |
| **Vos te ocupás** | Nadie | Vos | Sin costo extra |

- **Tasa de disputas por debajo del 1%** en 90 días rodantes. Pasado eso te cierran la cuenta.
- Pueden retener **hasta el 100% de los fondos** como reserva, e **1,5% mensual** de interés si quedás en saldo negativo.

**El techo de este camino:** más pagos rechazados que Stripe, y toda tu facturación colgada de una sola plataforma. Por eso, aunque funcione, no se deja el 100% de la plata adentro.

## La LLC: qué es y qué cuesta

Una LLC de un solo miembro extranjero es, para el fisco estadounidense, una *disregarded entity*: **fiscalmente transparente, no paga impuesto propio**. No es un escudo fiscal, es una herramienta para cobrar.

**Para qué la abrís, en concreto**

1. Habilita **Stripe** y **Shopify Payments**, que es lo que baja los pagos rechazados.
2. Te da una dirección de facturación de empresa para cargar en el Business Manager, lo que ayuda a subir el límite de gasto de Meta.
3. Te separa del cobro: la cuenta está a nombre de la empresa, no tuyo.

**Los costos reales**

| Concepto | Referencia |
| --- | --- |
| Apertura | **400–500 USD** |
| Mantenimiento anual | **350–400 USD** (tasa estatal + agente registrado + declaración) |
| Estado barato | Wyoming (~60 USD de annual report), New Mexico (sin annual report) |
| Estado caro | Delaware (300 USD de franchise tax), California (800 USD mínimo) |

Muchas gestorías cobran un margen alto sobre el costo real del trámite estatal. Compará dos o tres antes de contratar.

**EIN, ITIN y banco**

- **EIN**: es el CUIT de la empresa. Lo necesitás para el banco y para declarar, y **se obtiene sin tener SSN**.
- **ITIN**: no hace falta para abrir la LLC ni para el EIN. Sí para algunos productos bancarios. La espera típica es de **3 a 6 meses**.
- **Banco**: Mercury y Relay son los dos más usados para LLC. Tarjetas de débito virtuales y físicas sin comisión. La tarjeta de crédito recién se habilita manteniendo un saldo de **~15.000 USD**.
- **BOI (registro de beneficiario final)**: las LLC formadas en EE.UU. quedaron **exentas** por la regla interina de FinCEN del 26 de marzo de 2025. Solo siguen presentando las entidades extranjeras registradas en un estado.

## Stripe: mejor conversión, más riesgo

Stripe es el estándar del mercado y por eso **acepta más pagos que cualquier alternativa**. Ese es todo el argumento a favor, y es un argumento fuerte: en low ticket, unos puntos de rechazo son plata directa.

**Lo que pagás por eso**

- **Mira con lupa las cuentas nuevas**, sobre todo ante subas bruscas de volumen. Se escala gradual, no de 100 a 1.000 USD por día de un día para el otro.
- Puede retener fondos en **reserva** o bloquear la cuenta mientras revisa.
- **Las disputas casi nunca se ganan.** El contracargo se previene en el checkout —descriptor claro, entrega inmediata, soporte visible— no se pelea después.
- Liquida en **2 a 7 días hábiles** según la antigüedad y la salud de la cuenta.

**Lo que ayuda a sobrevivir la revisión**

- Publicar página de empresa, términos y política de reembolso antes de mandar tráfico.
- Si hay muchos rechazos, probar **3D Secure**.
- **A diferencia de Whop, el impuesto no lo cobra nadie por vos**: lo configurás con Stripe Tax y te registrás donde corresponda.

## Impuestos en Estados Unidos: la verdad completa

Vendiendo un producto digital desde Argentina, **lo normal es no pagar impuesto a las ganancias en Estados Unidos**. Pero *no pagar* no es lo mismo que *no presentar*, y esa confusión es la que termina en una multa de 25.000 dólares.

**1. Por qué no se paga income tax**

- La LLC de un miembro es transparente: no paga impuesto propio. El que tributaría sos vos, como no residente.
- Un no residente paga impuesto federal **solo si está "engaged in a US trade or business" y tiene renta efectivamente conectada (ECI)**. Eso se configura con presencia real: oficina, empleados o un agente dependiente en EE.UU., o trabajar estando allá.
- Vendiendo un PDF o un curso desde Argentina, sin oficina, sin empleados y sin pisar el país, **en general no hay ECI y no hay impuesto federal**.
- **Qué lo rompe:** un producto físico con depósito o stock en EE.UU., empleados o agentes allá, o viajar a trabajar. Cuando en el ambiente se dice "solo se paga con producto físico o servicios", esto es lo que hay detrás: el físico necesita logística en el país, y la logística crea presencia.

**2. Lo que hay que presentar aunque no pagues nada**

| Qué | Cuándo | Si no lo hacés |
| --- | --- | --- |
| **Form 5472 + Form 1120 pro forma** | 15 de abril; 15 de octubre con extensión (Form 7004). Lo dispara cualquier operación reportable, **hasta un aporte de 1 USD** | **25.000 USD** por formulario y por año, más 25.000 cada 30 días si no respondés la notificación del IRS, sin tope. Y la prescripción no empieza a correr hasta que presentás |
| **Annual report / franchise tax del estado** | Anual, según el estado | La LLC pierde su buena situación y se disuelve |
| **Form 1040-NR** | Solo si tenés ECI | — |

**El 5472 no se puede presentar online**: va por correo o fax. Y la obligación existe **aunque la LLC no haya facturado un dólar**. Esta es la trampa que se come el que abre una LLC "por si acaso" y la deja dormida.

**3. Sales tax: el que sí puede aparecer**

- Es un test **completamente distinto** al del income tax, y es **por estado**.
- Funciona por *economic nexus*: superás un umbral de ventas en un estado —la referencia habitual es **100.000 USD o 200 transacciones**, pero cambia en cada estado— y a partir de ahí tenés que registrarte y cobrar el impuesto.
- **Muchos estados sí gravan los productos digitales.** Y ojo: las ventas no gravadas igual cuentan para el umbral.
- **Cómo se resuelve:** en Whop, con el modo "cobra y declara" (2% por transacción). En Stripe, configurando Stripe Tax y registrándote vos.
- En la práctica no es un problema del día 1: se vuelve real cuando concentrás volumen en un mismo estado.

**4. VAT de Reino Unido y Europa**

Si vendés a consumidores de Reino Unido o la Unión Europea, el IVA de servicios digitales **se debe desde la primera venta**: para un vendedor de fuera no hay umbral mínimo. Es exactamente la razón por la que el modo "Whop cobra y declara" cubre Reino Unido y la UE junto con los 18 estados.

## Y vos, que vivís en Argentina

Esta es la parte que no aparece en los videos de LLC, y es la que hay que decir: **Argentina grava a sus residentes fiscales por renta mundial.** La plata que ganás afuera, en la ley, también tributa acá.

- **La LLC transparente no te saca del medio.** Justamente porque no paga impuesto propio, la renta se le atribuye al dueño: vos, residente argentino.
- **Vender al exterior no lleva IVA argentino.** Es exportación de servicios: el producto se utiliza afuera. Pero si lo facturás, **sí cuenta para el tope del monotributo**.
- **Lo que hace la mayoría** es dejar la plata afuera, en la plataforma, en el banco de la LLC o en cripto, y no hacerla entrar. Es una decisión de riesgo, no una zona gris comprobada.
- **El costo de esa decisión es el origen de fondos.** El día que querés comprar algo grande en Argentina —un auto, un departamento— te piden de dónde salió la plata. Lo que nunca declarás no tiene origen.
- **El hueco se está cerrando.** Los acuerdos internacionales de intercambio —**CARF** para cripto, **CRS**, **DAC8**— lo van a cerrar en los próximos **2 a 3 años**. Tratá el escenario de hoy como temporal, no como la regla.
- **La salida ordenada existe y es más barata de lo que la gente cree:** facturar la venta al exterior como exportación de servicios desde el monotributo. No pagás IVA, te queda todo con origen y dormís tranquilo. Lo único que tenés que mirar es el tope de categoría.

> Esto no es asesoramiento fiscal y las reglas cambian todos los años. Se cierra con un contador que entienda LLC y cripto, no con el contador del barrio.

## Cómo llega la plata y cómo no te la congelan

**La regla de oro: nunca tengas el 100% de la plata en un solo procesador ni en un solo banco.** Cualquiera te puede congelar los fondos sin aviso y sin explicación. Se reparte entre Stripe, Whop, el banco de la LLC y cripto.

- **USDT** (TRC20 o Solana) para mover fondos con menos comisión que las apps de cambio.
- Hay **tarjetas cripto con 1,5–3% de cashback** que se usan específicamente para pagar Meta Ads. Con el gasto publicitario de este negocio, ese cashback es margen directo.
- Cargá la **dirección de facturación de la LLC** en la información del negocio del Business Manager: ayuda a subir el límite de gasto de Meta.
- **Plata del negocio separada de la personal.**
- **Guardá el rastro de todo lo que movés.** El origen se prueba con comprobantes, no con memoria.

# CIERRE

## Qué hacer en cada etapa

| Etapa | En Argentina | Afuera |
| --- | --- | --- |
| **Todavía validando** | Monotributo categoría A, Facturitas, alta en IIBB de tu provincia | Whop, sin estructura. No abras nada |
| **Primeras ventas sostenidas** (100–300 USD de ganancia por día) | Recategorizarte, carpeta de gastos mensual, contador que entienda cobros digitales | Whop, y empezá a repartir los retiros entre más de un destino |
| **~10.000 USD por mes** | Proyectar el cruce a responsable inscripto: compará la cuota K contra IVA + Ganancias con tus gastos reales | LLC + Stripe + Mercury. Y el **calendario del Form 5472** anotado el día uno |
| **Escalando en serio** | Responsable inscripto o sociedad, contador todos los meses | Registro de sales tax donde cruces el umbral, y VAT si vendés a Reino Unido o la UE |

**El error de etapa más caro** es abrir la LLC antes de tener una oferta validada: pagás 400–500 USD de apertura, 350–400 por año y te cargás una obligación anual con multa de 25.000 USD, todo para facturar cero.

## Tarea del módulo

- [ ] Dar el alta de monotributo, o verificar en qué categoría estás y si te corresponde recategorizarte
- [ ] Instalar Facturitas y emitir una factura de prueba
- [ ] Confirmar cómo pagás Ingresos Brutos en tu provincia
- [ ] **Calcular tu costo impositivo por venta:** cuota mensual ÷ ventas del mes, más la alícuota de IIBB
- [ ] Elegir el camino de afuera (Whop o LLC + Stripe) y escribir en una línea por qué
- [ ] Si ya tenés LLC: verificar que el Form 5472 del último ejercicio esté presentado

**Criterio de aprobación:** poder responder sin mirar el documento cuánto te cuesta en impuestos una venta de un ticket tuyo en Argentina, y por qué elegías el camino que elegías para vender afuera.

## Fuentes consultadas

- Tabla de monotributo ARCA vigente desde agosto de 2026 — https://www.iprofesional.com/impuestos/461293-monotributo-asi-quedan-las-escalas-topes-e-importes-a-pagar-desde-agosto-2026
- Dictamen 70/2010 (DAT), exención de IVA de libros en formato no tradicional — https://www.mrconsultores.com.ar/archivos/Dictamenes/IVA/28-%20Exencion_de_libros_en_formato_no_tradicional.doc
- Eliminación de exenciones de IVA a suscripciones digitales (octubre 2024) — https://www.lanacion.com.ar/politica/el-gobierno-elimina-las-exenciones-al-iva-para-la-venta-de-diarios-revistas-y-suscripciones-nid21102024/
- Monotributo Unificado CABA 2026 — https://eleconomista.com.ar/economia/monotributo-unificado-caba-2026-como-adherirse-cuanto-paga-mes-n91713
- Ley Impositiva 2026 de CABA — https://siap.blogdelcontador.com.ar/novedades/caba-modifica-la-ley-impositiva-2026-con-nuevos-parametros-para-ingresos-brutos/
- Retenciones y percepciones en e-commerce 2026 — https://contablix.ar/blog/retenciones-percepciones-ecommerce-argentina-2026
- Términos de vendedor de Whop — https://whop.com/seller-terms/
- LLC de un solo miembro de propiedad extranjera (ECI, Form 5472) — https://www.taxesforexpats.com/articles/foreign-business/foreign-owned-single-member-llc.html
- Sales tax de productos digitales por estado — https://www.numeral.com/blog/sales-tax-on-digital-goods
