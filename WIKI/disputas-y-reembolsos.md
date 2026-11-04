# Disputas, contracargos y reembolsos

> Cómo mantener los contracargos por debajo de ~1%: términos y condiciones claros, reembolsar o pelear con Claude Code, y pasar la revisión de Stripe. (fuente: RAW/2026-10-10-wiki-previa/disputas-y-reembolsos.md)

**Un contracargo te cuesta mucho más que un reembolso.** Por eso hay dos posturas, y las dos necesitan la misma base: una página pública de términos con una garantía clara.

## El límite que no hay que pasar

**~0,9–1% de contracargos.** Por encima de eso, Hotmart, PayPal y los procesadores empiezan a restringir productos o cuentas.

## La base: términos y condiciones

- Publicá **Términos y Condiciones** con una ventana de garantía clara (por ejemplo, **7 días**), y hacé que se acepten en el checkout.
- Ponele **causas concretas** a la garantía. Por ejemplo: "solo hay devolución si se consumió menos del 5% del contenido" o "si hubo un error técnico documentado que impidió usarlo y soporte no respondió".
- Esa página sirve para dos cosas: filtrar a quién reembolsar y tener un argumento para defender cada disputa. Sin ella, no hay con qué defenderse.
- También ayuda a pasar la revisión de Stripe ([[procesadores-de-pago]]).

## Postura 1: reembolsar sin pelear

- Ante cualquier reclamo, se devuelve la plata antes de que se convierta en contracargo.
- Pelear disputas de Stripe **rara vez se gana**, incluso con pruebas sólidas (hay mucho "fraude amistoso"), y cada disputa cobra un fee.
- Si no las vas a pelear, **desactivá la respuesta automática de Stripe**.

## Postura 2: pelearlas con Claude Code

1. Abrí **Claude Code desde la carpeta del segundo cerebro**, para que tenga todo el contexto del negocio.
2. Conectá Stripe y MercadoPago. Lo mejor es por **MCP, CLI o API**. Si la plataforma no tiene ninguno, usá **Claude en Chrome** con una pestaña real. Alcanza con pasarle los links de la documentación y decirle "quiero conectar mi Stripe y mi MercadoPago": te guía paso a paso.
3. Pasale el link de tu página de términos.
4. Pedile que revise las disputas abiertas y responda cada una con las pruebas y los términos.
5. **Automatizalo:** pedile una rutina que cada **12 horas** busque disputas nuevas y responda las que tengas a favor.

## Evitar la disputa antes de que pase

- **Entrega automática redundante:** dos métodos de entrega a la vez, así nadie dice que no le llegó ([[shopify-y-checkout]]).
- **Seguimiento de pagos fallidos** automatizado con Claude conectado a Stripe o MercadoPago. Guardá la prueba de entrega de cada venta.

## Pasar la revisión de Stripe

- Cuando Stripe bloquea una cuenta, **casi nunca es por fraude**: falta una landing pública clara sobre el negocio.
- Lo que ayuda a que la aprueben: descripción del negocio, precios claros, contacto de soporte y una **política de reembolso y cancelación visible y coherente con lo declarado en Stripe**.
- **Términos y Condiciones** que funcionaron: Titular · Aceptación · Producto y entrega · Precio y pago · Garantía y reembolsos (ventana de **7 días**) · Propiedad intelectual · Resultados · Privacidad · Contacto y soporte. Van en el pie de página y enlazados desde la landing que se declara en Stripe.
- Hotmart reembolsa casi sin cuestionar. Hay que contarlo en el cálculo de margen.

Relacionado: [[procesadores-de-pago]] · [[llc-banca-y-fiscal]] · [[email-y-automatizaciones]]

## Conexiones con tu operación actual
- Tu **garantía estándar de 7 días** ([[perfil-y-negocio]]) ya coincide con la ventana recomendada. Falta ponerle causas concretas en los términos.
- **Esta carpeta es el "segundo cerebro" que menciona la Postura 2.** Para pelear disputas desde acá hay que conectar Stripe o MercadoPago. En esta sesión en la nube no están conectados.
- Hotmart reembolsa casi sin preguntar: contalo en el margen de las ofertas que cobres por Hotmart.

## La skill `disputas` (3/11/2026)

Desde el 3/11 está instalada la skill **`disputas`** de Launch Expert ([[skills-launch-expert]]), que es la versión armada de lo que acá estaba como "pelearlas con Claude Code". Viene con scripts propios (`estado.py`, `whop_responder.py`, `whop_contracargos.py`, JS para el panel y tools en Swift para los PDF) y contesta en una sola pasada los reclamos y contracargos de **Whop / Impul Pay** y de **Mercado Pago** de una tienda de Impultienda.

**De dónde saca la prueba:** del panel de Impultienda, que corre sobre Supabase (`sb.impultienda.ar/rest/v1/`), consultado desde la pestaña con la sesión iniciada. Tablas `orders`, `email_events` (accepted / delivered / opened / failed), `download_logs` y `order_items`.

**Sus reglas duras:**
- Solo hechos verificables: nada de descargas, llamadas o contactos inventados.
- **Si el mail de entrega falló** (casilla llena, rebote, casilla inexistente), **no se declara la entrega**: primero se reenvía o se pide otro mail, y se dice la verdad.
- Las descargas con user-agent `node`, `bot`, `python` o `curl` son de servidor y **no se le atribuyen al comprador**.
- El `recommended_action` de la API de Whop **es publicidad y se ignora**.
- **Nunca** se toca "Devolver el dinero", `accept` ni `refund` sin orden explícita.
- Si la landing ofrece garantía, dentro del plazo no se escribe "no reembolsable": se responde con hechos del producto y se ofrece ayuda.
- Los upsells son órdenes hijas (`parent_order_id`), cada una con su pago y su hora: es el argumento contra "no autoricé" y "me cobran de más".
- La base guarda **UTC**; al comprador se le escribe en su hora local (AR = UTC−3).
- **El chat de MP rechaza el PDF**: el informe de actividad de la orden se sube como JPG.
- Si MP pide verificar el inicio de sesión, **lo hace Santiago**: la skill no ingresa contraseñas ni códigos.

**Falta para usarla:** cargar `~/.claude/skills/disputas/.env` con las claves de Whop y de Mercado Pago, y completar su **sección 8** con las carpetas de entrega reales y la política de reembolsos de cada oferta.

## Fuentes
- RAW/2026-10-10-wiki-previa/disputas-y-reembolsos.md (página de la wiki previa, actualizada el 2026-09-24)
- Fuentes originales citadas (todavía no están en este cerebro): clases de la formación y experiencias de la comunidad, agosto–septiembre 2026
