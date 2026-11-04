# Surfing Scale Automatic Bid Launch Expert

> Skill para instalar en tu segundo cerebro. Surfea el presupuesto de tus CBO con el método V3 de Launch Expert: sube +30 % cuando el ROAS lo banca, le tira de la oreja −30 % cuando flaquea, decide en los horarios en que tu oferta vende y, antes de mover un dólar, te pide el OK por WhatsApp o Telegram. Vos respondés **SI** o **NO** desde el celular.

---

## 0. Instrucciones para la IA

Esto es una skill completa. Si sos la IA del alumno y te pegaron este texto, seguí estos pasos al pie de la letra.

**Cuándo se activa:** cuando el alumno diga "instalá Surfing Scale", "surfeá mis CBO", "escalado automático de CBO", "Surfing Scale Automatic Bid", o pegue este manual.

**Paso 1 · Guardar la skill.** Creá la carpeta `~/.claude/skills/surfing-scale/` y guardá este manual entero como `SKILL.md`, con este encabezado arriba de todo:

```
---
name: surfing-scale
description: Surfing Scale Automatic Bid Launch Expert. Surfea el presupuesto de las CBO con el método V3 (+30 % / tirón −30 %) usando las ventas de Impultienda, con horarios por oferta, modos agresivo y tranquilo, y confirmación SI/NO por WhatsApp o Telegram. Usar cuando el alumno diga "surfing scale", "surfear la CBO", "escalar CBO automático" o pegue este manual.
---
```

**Paso 2 · Crear la carpeta de trabajo.** `~/surfing-scale/` (fuera de cualquier carpeta que se sincronice con GitHub o con la nube: ahí va a vivir el archivo `.env` con las claves). Escribí ahí, tal cual, cada archivo de la sección 14. Copiá `config.ejemplo.json` como `config.json`. Corré `python3 -c "import ast,glob;[ast.parse(open(f).read()) for f in glob.glob('*.py')]"` para confirmar que se copiaron bien.

**Paso 3 · Pedir los datos, de a uno.** No le tires una lista de diez preguntas. Pedí en este orden y explicá cómo conseguir cada cosa con la sección 8:
1. Qué ofertas quiere surfear, el país de cada una y el **precio del front** en dólares.
2. El token de Meta. Que lo pegue **directo en el archivo `.env`** (abrilo vos con `open -e ~/surfing-scale/.env` en Mac); vos no lo repetís nunca en el chat. Si sus cuentas están en dos perfiles de Meta distintos, va un token por perfil (sección 8).
3. Cómo quiere los avisos y las confirmaciones: WhatsApp, Telegram o los dos (sección 11).
4. Si arranca en modo **agresivo** o **tranquilo** (sección 4). Si duda: agresivo para CBO chicas que ya venden, tranquilo para todo lo demás.

**Paso 4 · Encontrar las campañas.** Por cada oferta corré `python3 buscar.py "<pedazo del nombre de sus campañas>"`. Mostrale la lista en una tabla corta. Solo se surfean campañas **CBO** en cuentas en **dólares**: las que salen con `NO` quedan afuera y le explicás por qué. Las que no son la oferta (otra oferta con nombre parecido) también quedan afuera. Con su OK:
`python3 buscar.py "<filtro>" --guardar --oferta "<nombre de la oferta>" --ticket <front>`.
Si alguna campaña no es CBO común (Cost Cap o Bid Cap con puja manual), sacala del config: esas se manejan con Pujas Search Scale.

**Paso 5 · Receptor de ventas de Impultienda.** Es obligatorio: el ROAS sale **solo** de Impultienda. Seguí la sección 9 y la 10 (servidor). Al terminar, el instalador imprime la URL del webhook: el alumno la pega en Impultienda (Configuraciones → Webhooks). Hasta que no entre la primera venta real, el Surfing Scale no mueve nada y avisa.

**Paso 6 · Avisos.** Cargá los datos de WhatsApp y/o Telegram en `.env` (sección 11) y corré `python3 comun.py --probar-avisos`. Tiene que llegarle un mensaje. Pedile que responda "hola" y verificá que lo leés con `python3 -c "from comun import respuestas;print(respuestas(0)[-3:])"`. Si no llega o no se lee, arreglalo antes de seguir: sin eso no puede confirmar.

**Paso 7 · Servidor.** Tiene que correr las 24 h con la compu apagada. Sección 10 (DigitalOcean, US$6/mes). El instalador programa el Surfing Scale cada 10 minutos y corre un simulacro.

**Paso 8 · Primera prueba real.** Cuando ya haya ventas de hoy y de ayer en el receptor (al día siguiente de conectar el webhook), pedí **confirmación explícita** y corré en el servidor `python3 surfing.py --ahora`. Le llega el parte con las propuestas numeradas. Que responda **SI n** o **NO n** en el chat. Verificá en el log que se aplicó y que le llegó el "✅ aplicado".

**Reglas para vos, IA:**
- El modo por defecto es **con confirmación**. Nunca lo pases a automático sin que el alumno lo pida con esas palabras. Si quiere que nunca se pueda pasar a automático, poné `"permitir_auto": false`.
- Nunca corras `surfing.py` sin `--simulacro` sin el sí del alumno.
- Nunca escribas tokens en el chat, en `config.json`, en el SKILL.md ni en carpetas que se sincronizan. Solo en `.env`.
- Un solo Surfing Scale por operación: si corre en el servidor, en la Mac solo se usa `--simulacro`.
- Los cambios se hacen en la copia local y se suben al servidor con `scp`. El estado vivo (`estado/`, `ventas/`) está en el servidor.
- No uses Utmify para el ROAS de este sistema, aunque el alumno lo tenga: llega 20 minutos tarde (sección 6).
- Antes de tocar una regla, mostrá qué cambia y por qué, y probá en simulacro antes de subir.

---

## 1. Qué hace y qué esperar

El Surfing Scale hace por vos el trabajo de todos los días con la CBO: mirar cómo viene cada campaña, decidir si sube, si se queda quieta o si le tirás de la oreja, y mover el presupuesto sin pasarte nunca de 30 %.

Lo que hace:
- **Mira el ROAS real.** Ventas de Impultienda al instante contra el gasto de Meta, campaña por campaña.
- **Decide en los horarios de tu oferta.** Analiza a qué hora vende cada oferta y decide cuando ya hay ventas frescas para juzgar. Una oferta de otro país tiene otros horarios.
- **Te propone y vos confirmás.** Te manda el parte por WhatsApp o Telegram con cada propuesta numerada. Respondés **SI 3** o **NO 3**. Si no respondés, no hace nada.
- **Verifica y te confirma.** Después de cambiar la CBO la relee en Meta y te manda "✅ aplicado" con el presupuesto que quedó de verdad.

Qué esperar: esto es para **CBO de ofertas que ya venden**. No arregla una oferta que no convierte: si el ROAS no llega a 2 nunca, el Surfing Scale la va a dejar quieta o le va a tirar de la oreja, que es lo que tiene que pasar. Juzgá el sistema a la semana, no al día.

---

## 2. El método: cómo surfeamos la CBO

Son las reglas de la clase de manejo de la CBO V3, escritas para que una máquina las siga sin dudar.

- **Nunca más de 30 % por movimiento.** Ni para arriba ni para abajo. Un salto más grande saca a la campaña del aprendizaje.
- **Se sube con ROAS 2 o más, estable.** Se mira hoy **y ayer**. Un día bueno solo no alcanza.
- **Ayer bajo + hoy mejor = quieta.** Puede ser una racha: se espera a que se confirme.
- **Si flaquea, tirón de oreja −30 %.** Día negativo: −30 % hasta que vuelve al equilibrio.
- **Una mañana floja no es un día malo.** Si ayer cerró bien, solo se le tira de la oreja si hoy viene muy mal. Las mañanas suelen arrancar flojas y se recuperan en el pico.
- **Sin gasto suficiente no se juzga.** Hasta que la campaña no gastó 2 tickets (3 en tranquilo) en el día, no se toca.
- **Arriba de US$700 se mueve una vez por día.** Con CBO grandes, mover varias veces en el día desordena la entrega.
- **Ticket = precio del front.** Es la medida para el gasto mínimo y para el piso del presupuesto.

---

## 3. Cómo decide, paso a paso

En cada horario de la oferta, para cada campaña:

| Pregunta | Si la respuesta es sí |
|---|---|
| ¿Gastó menos de 2 tickets hoy (3 en tranquilo)? | 🟰 **Quieta**: todavía no hay datos para juzgar. |
| ¿ROAS de hoy menor a 1 (0,9 en tranquilo)? | Si ayer bancó (ROAS ≥ 1,5) y hoy no bajó de 0,7: 🟰 **quieta**. Si no: 👂 **tirón −30 %** (sin bajar del piso). |
| ¿ROAS de hoy 2 o más, con 2+ ventas (3+ en tranquilo)? | Si ayer también bancó (1,5 en agresivo, 2 en tranquilo): 🏄 **surfeo +30 %** (sin pasar el techo). Si ayer fue bajo: 🟰 **quieta**. |
| ¿Nada de lo anterior? | 🟰 **Quieta**: está entre 1 y 2, se mantiene. |

Ejemplo de un parte:

```
📊 13:00 · modo AGRESIVO · con confirmación

Mi Oferta · CP2
· CBO US$220 · gasto hoy US$100 · 8 ventas · ROAS 2,28
· 🏄 SURFEO +30 %: US$220 → US$286 (ROAS hoy 2,28 (8 ventas) y ayer 1,71)
  👉 Respondé SI 1 o NO 1 (vence en 90 min)

Mi Oferta · CP1
· CBO US$200 · gasto hoy US$73 · 3 ventas · ROAS 0,96
· 🟰 quieta: ROAS hoy 0,96 flojo, pero ayer bancó (1,84): espera
```

---

## 4. Los dos modos

| | Agresivo | Tranquilo |
|---|---|---|
| Cuándo decide | 3 veces por día: cuando la oferta juntó el 25 %, el 50 % y el 75 % de sus ventas del día (mínimo 3 h entre una y otra) | 1 vez por día: cuando la oferta juntó el 60 % de sus ventas |
| Gasto mínimo de hoy para juzgar | 2 tickets | 3 tickets |
| Surfeo +30 % | ROAS hoy ≥ 2 con 2+ ventas **y** ayer ≥ 1,5 | ROAS hoy ≥ 2 con 3+ ventas **y** ayer ≥ 2 |
| Tirón −30 % | ROAS hoy < 1 | ROAS hoy < 0,9 |
| Si ayer bancó, solo tira si hoy < | 0,7 | 0,6 |
| Para qué sirve | CBO chicas (menos de US$700) que ya venden: buscar el techo rápido | Campañas grandes, ofertas nuevas o cuando querés ir seguro |

**Desde US$700 de CBO, cualquier campaña pasa a una vez por día** (el horario del modo tranquilo), sea cual sea el modo.

El modo se cambia desde el celular (`surf agresivo` / `surf tranquilo`) o en `config.json`. También se puede fijar por campaña con `"modo": "tranquilo"` en su bloque.

Todos los números están en `config.json` → `modos`. Vienen calibrados con campañas reales; no los toques hasta tener una semana de datos.

---

## 5. Horarios por oferta

Cada oferta vende a otra hora: una oferta en Argentina puede tener el pico a la mañana y otra en México al mediodía. Por eso los horarios **no son fijos**:

1. Una vez por día, el Surfing Scale toma las compras por hora de los últimos 14 días de las campañas de cada oferta (pixel de Meta, pasado a tu huso horario).
2. Calcula a qué hora la oferta ya juntó el 25 %, el 50 % y el 75 % de sus ventas del día (agresivo) y el 60 % (tranquilo).
3. Si los horarios cambian, te avisa:

```
🕐 Horarios de Mi Oferta (según 288 ventas de los últimos 14 días, pico 09–12 h):
· agresivo: 10:00, 13:00, 18:00
· tranquilo / 1 vez al día: 15:00
```

Por qué así: cada análisis llega con una tanda de ventas nuevas para juzgar, y el de tranquilo cae cuando ya pasó la mayor parte del día pero todavía queda 40 % de las ventas para aprovechar la suba.

Las campañas se agrupan por el campo `oferta` del config. Si una oferta tiene pocas ventas (menos de 40 en 14 días), usa los horarios de respaldo del modo. Si querés que el análisis use también otras campañas de la misma oferta que no surfeás, agregalas en `"analizar_tambien": ["<ID>", ...]`.

Las compras del pixel se usan **solo para saber cuándo se mueve la oferta**. Las decisiones de subir o bajar son siempre con las ventas de Impultienda.

---

## 6. Por qué solo Impultienda (y no Utmify)

Utmify recibe cada venta recién cuando el cliente termina o abandona el post-compra, unos 20 minutos después. Si decidís con Utmify, una campaña que está vendiendo parece peor de lo que está justo en el momento de decidir. El webhook de Impultienda avisa la venta aprobada en el momento.

Dos detalles que ya están resueltos en el receptor del kit:
- **El día es el de la orden.** Impultienda reenvía en tanda, una vez por día, aprobaciones tardías de órdenes de días anteriores (pagos que se aprueban horas después). Si se contaran el día que llega el aviso, inflarían el ROAS de "hoy" justo al mediodía. El receptor las cuenta en el día de la orden.
- **Los upsells suman a la campaña que trajo la compra.** El upsell post-compra hereda la campaña de su orden padre y suma plata, pero no cuenta como venta nueva. Los reembolsos y contracargos restan.

Para que el receptor sepa de qué campaña vino cada venta, tus anuncios tienen que llevar `utm_id={{campaign.id}}` (o el formato de Utmify `utm_campaign={{campaign.name}}|{{campaign.id}}`) en los parámetros de URL.

---

## 7. Confirmación por WhatsApp o Telegram

**Con confirmación** (el modo por defecto):
- En cada horario te llega el parte. Cada cambio propuesto lleva un número.
- Respondés **SI 1** para aplicarlo o **NO 1** para descartarlo. **SI** solo, sin número, aprueba todas las propuestas abiertas.
- Las respuestas se leen cada 10 minutos: la confirmación puede tardar hasta 10 minutos en aplicarse.
- Cada propuesta **vence a los 90 minutos** sin aplicarse (la situación ya cambió).
- Antes de aplicar, revisa que nadie haya movido la CBO a mano. Si la movieron, no la aplica y te avisa.
- Después de aplicar, relee la campaña en Meta y te manda:

```
✅ SURFEO +30 % aplicado #1
Mi Oferta · CP2
· CBO US$220 → US$286 (verificado en Meta)
· campaña activa ✅
```

**Automático:** aplica solo y te manda la misma confirmación. Para usarlo escribí `surf auto`. Si no querés que exista esa posibilidad, poné `"permitir_auto": false` en el config: ahí `surf auto` queda bloqueado y siempre te pide el SI.

### Comandos

Se escriben en el mismo chat donde te llegan los avisos:

| Escribí | Qué hace |
|---|---|
| `SI 3` / `NO 3` | Aplica o descarta la propuesta 3 |
| `SI` | Aplica todas las propuestas abiertas |
| `surf agresivo` / `surf tranquilo` | Cambia el modo |
| `surf confirmar` / `surf auto` | Pide confirmación o aplica solo |
| `surf pausa` / `surf seguir` | Frena todo o lo reanuda |
| `surf estado` | Te manda el parte de todas las campañas ahora |

---

## 8. Lo que necesitás

| Qué | Para qué | Cómo conseguirlo |
|---|---|---|
| **Impultienda con webhooks** | Las ventas al instante (obligatorio) | Configuraciones → Webhooks. Sección 9. |
| **Token de Meta** | Leer y mover las CBO | Business Manager → Configuración del negocio → Usuarios del sistema → Agregar (admin) → Asignar activos (las cuentas publicitarias, con control total) → Generar token con permisos `ads_management`, `ads_read`, `business_management`. Ese token no vence. |
| **Cuentas en dólares** | Que el ROAS cierre con las ventas en dólares | Las cuentas en otra moneda quedan afuera (avisa). |
| **WhatsApp (Whapi) o Telegram** | Avisos y confirmaciones | Sección 11. |
| **Servidor** | Que corra 24 h con tu compu apagada | DigitalOcean, US$6/mes. Sección 10. |
| **Python 3.9 o más** | Correr los scripts en tu compu | En Mac ya viene. Probá `python3 --version`. |

Todas las claves van en el archivo `~/surfing-scale/.env`, una por línea:

```
SURF_META_TOKEN=EAAB...
SURF_WEBHOOK_CLAVE=una-clave-larga-inventada
SURF_WHAPI_TOKEN=...
SURF_WHATSAPP_DESTINO=5491112345678
SURF_TELEGRAM_TOKEN=...
SURF_TELEGRAM_CHAT=...
```

Las que no uses, no las pongas.

**Cuentas en otro perfil de Meta:** agregá otra línea, por ejemplo `SURF_META_TOKEN_2=EAAB...`, buscá esas campañas con `python3 buscar.py "<filtro>" --token SURF_META_TOKEN_2` y al guardarlas cada una queda con `"token": "SURF_META_TOKEN_2"`.

---

## 9. Receptor de ventas de Impultienda

1. En `.env` agregá `SURF_WEBHOOK_CLAVE=` con una clave larga inventada (letras y números, sin espacios).
2. El instalador del servidor (sección 10) deja el receptor andando con HTTPS gratis (Caddy y una dirección `sslip.io`) y te imprime la URL:
   `https://<tu-ip-con-guiones>.sslip.io/venta?k=<tu clave>`
3. Pegala en Impultienda → Configuraciones → Webhooks, con los eventos **order.approved**, **order.refunded** y **order.chargeback**. Es un webhook por cuenta de Impultienda: cubre todas tus tiendas.
4. Probá abriendo la URL sin `/venta` en el navegador: tiene que decir "receptor del Surfing Scale funcionando".
5. Con la primera venta real aparece `ventas/AAAA-MM-DD.json` en el servidor, con las ventas por campaña.

El receptor convierte a dólares las ventas en otra moneda con la cotización del día. Las ventas de prueba de Impultienda no se cuentan.

---

## 10. Instalación en el servidor

### 10.1 Crear el servidor
1. Entrá a DigitalOcean → Create → Droplets.
2. Ubuntu 24.04, plan Basic, Regular, **US$6/mes**. Región: Nueva York.
3. Autenticación: **SSH Key**. Tu IA te genera una con `ssh-keygen -t ed25519 -f ~/.ssh/surfing -N ""` y te pasa el contenido de `~/.ssh/surfing.pub` para pegar ahí.
4. Create. Anotá la IP.

Si ya tenés el servidor de Pujas Search Scale, usá el mismo: el Surfing Scale vive en otra carpeta (`/opt/surfing`) y no se pisan.

### 10.2 Subir e instalar
Tu IA corre, desde tu compu:

```
ssh -i ~/.ssh/surfing root@<IP> "mkdir -p /opt/surfing"
scp -i ~/.ssh/surfing ~/surfing-scale/*.py ~/surfing-scale/*.json ~/surfing-scale/.env ~/surfing-scale/instalar_servidor.sh root@<IP>:/opt/surfing/
ssh -i ~/.ssh/surfing root@<IP> "bash /opt/surfing/instalar_servidor.sh"
```

El instalador:
- Instala el receptor de ventas y te imprime la URL del webhook.
- Programa el Surfing Scale cada 10 minutos.
- Corre un simulacro (no cambia nada ni manda avisos).

### 10.3 Cambios después
Siempre en la copia local y después `scp` del archivo al servidor. Para mirar lo que hizo:

```
ssh -i ~/.ssh/surfing root@<IP> "tail -50 /opt/surfing/log/$(date +%F).log"
```

---

## 11. Avisos y confirmaciones: WhatsApp o Telegram

### WhatsApp (Whapi)
1. Creá una cuenta en **whapi.cloud** y un canal.
2. Escaneá el QR con un **número secundario** (el que va a mandar los avisos; no uses tu número personal).
3. Copiá el token del canal: va en `SURF_WHAPI_TOKEN`.
4. En `SURF_WHATSAPP_DESTINO` va tu número personal con código de país, sin `+` ni espacios (Argentina: `549` + área + número).
5. Respondés en el chat con ese número secundario. El Surfing Scale lee lo que le escribís.

### Telegram (gratis)
1. En Telegram buscá **@BotFather** → `/newbot` → ponele nombre. Te da un token: va en `SURF_TELEGRAM_TOKEN`.
2. Mandale cualquier mensaje a tu bot nuevo.
3. Tu IA abre `https://api.telegram.org/bot<TOKEN>/getUpdates` y saca el número de `chat.id`: va en `SURF_TELEGRAM_CHAT`.
4. Respondés en ese chat.

Probá con `python3 comun.py --probar-avisos`. Te llegan:
- 🕐 los horarios de cada oferta cuando cambian.
- 📊 el parte en cada horario, solo con las campañas que tocaba analizar.
- 🏄 / 👂 cada propuesta con su número.
- ✅ cada cambio aplicado, verificado en Meta.
- ⌛ las propuestas que vencieron sin respuesta.
- ⚠️ campañas que no puede leer, que no son CBO o que están en otra moneda.
- 🛑 si se frena por un problema con el token.

---

## 12. Operación diaria

- **Mirá el parte, no el Administrador de anuncios.** Respondé SI o NO desde el celular.
- **Si movés una CBO a mano, avisale:** el Surfing Scale lee el presupuesto actual en cada análisis, así que sigue desde donde la dejaste. Si había una propuesta abierta sobre esa campaña, no la aplica.
- **Para frenarlo un rato:** `surf pausa`. Para seguir: `surf seguir`.
- **Para sacar una campaña:** pausala en Meta (no toca lo que está pausado) o poné `"activa": false` en su bloque de `config.json`.
- **Campañas nuevas de la oferta:** corré `buscar.py` con `--guardar` y subí el `config.json` al servidor.
- **Techo y piso:** `presupuesto_max` frena las subas en ese monto; `presupuesto_piso` frena los tirones (por defecto, 2 tickets).
- **Juzgá a la semana.** Mirá el `estado/historial.json`: cada cambio con su motivo.

---

## 13. Problemas comunes

| Síntoma | Causa | Qué hacer |
|---|---|---|
| "No hay ventas de Impultienda" | El webhook no está cargado o no entró ninguna venta | Revisá la URL en Impultienda → Webhooks y que el receptor responda (sección 9). |
| Todo queda "quieta" con ROAS 0 | Las ventas no traen el ID de campaña | Agregá `utm_id={{campaign.id}}` a los parámetros de URL de los anuncios. |
| "la cuenta está en ARS / BRL..." | La cuenta publicitaria no está en dólares | Esa campaña queda afuera: el ROAS no cerraría. |
| "no tiene presupuesto de campaña" | Es ABO, no CBO | El Surfing Scale solo maneja CBO. |
| "no la puedo leer en Meta (#10)" | El token no tiene esa cuenta | Asigná la cuenta al usuario del sistema o agregá el token del otro perfil (sección 8). |
| "Meta error 190" y frenado | El token venció o lo revocaron | Generá otro, ponelo en `.env` del servidor y borrá el archivo `FRENADO`. |
| Respondo SI y no pasa nada | Se lee cada 10 min, o respondiste en otro chat | Esperá 10 min. Respondé en el chat donde llegó el parte. Si pasaron 90 min, venció. |
| "La propuesta ya no está abierta (venció)" | Respondiste después de 90 min | Esperá el próximo horario: vuelve a proponer si sigue correspondiendo. |
| WhatsApp da 403 | El canal de Whapi se desconectó | Volvé a escanear el QR en whapi.cloud. |
| Llegan dos partes iguales | Corren dos Surfing Scale a la vez | Dejá uno solo: el del servidor. |

---

## 14. Control final

1. La skill está guardada en `~/.claude/skills/surfing-scale/SKILL.md`.
2. Los archivos del kit están en `~/surfing-scale/` y pasan el chequeo de sintaxis.
3. El `.env` tiene el token de Meta y la clave del webhook, y no está en ninguna carpeta que se sincronice.
4. `buscar.py` cargó las CBO de cada oferta, todas en dólares, con el precio del front como ticket.
5. El servidor está instalado y el simulacro corrió sin errores.
6. El webhook está cargado en Impultienda y ya entró la primera venta en `ventas/`.
7. Llegó el mensaje de prueba y el Surfing Scale lee tus respuestas.
8. Llegó el aviso 🕐 con los horarios de cada oferta.
9. Hiciste la primera prueba con `--ahora`, respondiste SI y llegó el ✅ verificado en Meta.
10. El modo (agresivo o tranquilo) y la confirmación quedaron como querés.

---

## 15. Archivos del kit

Tu IA los copia tal cual en `~/surfing-scale/`. No hace falta que los leas.

### comun.py

```python
"""Surfing Scale Automatic Bid Launch Expert — funciones compartidas (Meta, avisos, respuestas, secretos).
Los secretos se leen de las variables de entorno o del archivo .env de esta carpeta (nunca del config.json)."""
import json, os, sys, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

AQUI = os.path.dirname(os.path.abspath(__file__))
G = "https://graph.facebook.com/v21.0"
UA = "surfing-scale/1.0"   # Whapi responde 403 sin un User-Agent propio
NOMBRE = "🏄 Surfing Scale Automatic Bid Launch Expert"
# Códigos de Meta que NO se reintentan: permisos/token (10, 190, 200-299) y límites (4, 17, 32, 613, 80000-80014)
FRENAR = {4, 10, 17, 32, 190, 613} | set(range(200, 300)) | set(range(80000, 80015))


class Frenar(Exception):
    """Error que no se arregla reintentando (token vencido, permisos, límites de Meta)."""


def cargar_env():
    p = os.path.join(AQUI, ".env")
    if not os.path.exists(p):
        return
    for linea in open(p):
        linea = linea.strip()
        if linea and not linea.startswith("#") and "=" in linea:
            k, v = linea.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


cargar_env()


def secreto(nombre, obligatorio=True):
    v = (os.environ.get(nombre) or "").strip()
    if not v and obligatorio:
        raise Frenar(f"Falta {nombre} en el archivo .env")
    return v or None


def cfg():
    return json.load(open(os.path.join(AQUI, "config.json")))


def tz():
    return ZoneInfo(cfg().get("huso", "America/Argentina/Buenos_Aires"))


def hm(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)


# ---------- Meta Graph API ----------
def graph(path, data=None, token="SURF_META_TOKEN"):
    """token = nombre de la variable del .env (cada campaña puede usar otro perfil de Meta)."""
    tok = secreto(token)
    url = f"{G}/{path}"
    if data is None:
        req = urllib.request.Request(f"{url}{'&' if '?' in url else '?'}access_token={tok}")
    else:
        req = urllib.request.Request(url, data=urllib.parse.urlencode(dict(data, access_token=tok)).encode())
    for intento in range(3):
        try:
            r = json.load(urllib.request.urlopen(req, timeout=90))
            break
        except urllib.error.HTTPError as e:
            r = json.loads(e.read() or b"{}")
            break
        except Exception:
            if intento == 2:
                raise
            time.sleep(5)
    if "error" in r:
        err = r["error"]
        code, sub = err.get("code"), err.get("error_subcode")
        msg = f"Meta error {code}/{sub}: {err.get('error_user_msg') or err.get('message')}"
        if code in FRENAR or sub in FRENAR or err.get("type") == "OAuthException":
            raise Frenar(msg)
        raise RuntimeError(msg)
    return r


def compras_pixel(acciones):
    for a in acciones or []:
        if a.get("action_type") in ("offsite_conversion.fb_pixel_purchase", "purchase"):
            return float(a["value"])
    return 0.0


# ---------- Avisos: WhatsApp (Whapi) y/o Telegram ----------
def whapi(path, data=None):
    tok = secreto("SURF_WHAPI_TOKEN", False)
    if not tok:
        return None
    req = urllib.request.Request(f"https://gate.whapi.cloud/{path}", method="POST" if data else "GET",
                                 data=json.dumps(data).encode() if data else None,
                                 headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json", "User-Agent": UA})
    return json.loads(urllib.request.urlopen(req, timeout=20).read().decode() or "{}")


def avisar_externo(texto):
    """Manda el texto a WhatsApp y a Telegram si están configurados. Devuelve la lista de errores."""
    errores = []
    destino = secreto("SURF_WHATSAPP_DESTINO", False)
    if destino and secreto("SURF_WHAPI_TOKEN", False):
        try:
            whapi("messages/text", {"to": destino, "body": f"{NOMBRE}\n{texto}"})
        except Exception as e:
            errores.append(f"WhatsApp: {e}")
    tg_tok, tg_chat = secreto("SURF_TELEGRAM_TOKEN", False), secreto("SURF_TELEGRAM_CHAT", False)
    if tg_tok and tg_chat:
        try:
            data = urllib.parse.urlencode({"chat_id": tg_chat, "text": f"{NOMBRE}\n{texto}"[:4000]}).encode()
            urllib.request.urlopen(f"https://api.telegram.org/bot{tg_tok}/sendMessage", data=data, timeout=20)
        except Exception as e:
            errores.append(f"Telegram: {e}")
    return errores


def respuestas(desde_ts):
    """Lo que el dueño escribió (SI 3, NO 3, surf ...) por WhatsApp o Telegram después de desde_ts (epoch).
    Devuelve [(ts, texto)] del más viejo al más nuevo."""
    out = []
    destino = secreto("SURF_WHATSAPP_DESTINO", False)
    if destino and secreto("SURF_WHAPI_TOKEN", False):
        try:
            r = whapi(f"messages/list/{destino}@s.whatsapp.net?count=50") or {}
            for m in r.get("messages", []):
                if not m.get("from_me") and m.get("type") == "text" and m.get("timestamp", 0) > desde_ts:
                    out.append((m["timestamp"], (m.get("text") or {}).get("body", "").strip()))
        except Exception as e:
            print(f"No pude leer WhatsApp: {e}")
    tg_tok, tg_chat = secreto("SURF_TELEGRAM_TOKEN", False), secreto("SURF_TELEGRAM_CHAT", False)
    if tg_tok and tg_chat:
        try:
            r = json.load(urllib.request.urlopen(f"https://api.telegram.org/bot{tg_tok}/getUpdates?limit=100", timeout=20))
            for u in r.get("result", []):
                m = u.get("message") or {}
                if str((m.get("chat") or {}).get("id")) == str(tg_chat) and m.get("date", 0) > desde_ts and m.get("text"):
                    out.append((m["date"], m["text"].strip()))
        except Exception as e:
            print(f"No pude leer Telegram: {e}")
    return sorted(out)


if __name__ == "__main__" and "--probar-avisos" in sys.argv:
    errs = avisar_externo("✅ Conectado. Te voy a mandar el parte de cada horario y, antes de mover una CBO, te pido el SI.")
    print("Errores:", errs or "ninguno")
```

### surfing.py

```python
"""Surfing Scale Automatic Bid Launch Expert — surfea el presupuesto de las CBO con el método V3 de Launch Expert.
+30 % cuando el ROAS de hoy y de ayer lo banca, tirón de oreja −30 % cuando flaquea, nunca más de 30 % por movimiento.
El ROAS sale SIEMPRE de las ventas de Impultienda (receptor.py), nunca de Utmify. Decide en los horarios de cada oferta,
que salen de sus ventas por hora. Corre cada 10 min por cron.
Uso:  python3 surfing.py                          -> corrida real
      python3 surfing.py --simulacro              -> lee todo, no cambia nada, no manda avisos
      python3 surfing.py --simulacro --ahora      -> simula un análisis de todas las campañas ya mismo
      python3 surfing.py --ahora                  -> análisis real ya mismo (con confirmación, nada se aplica sin tu SI)
"""
import json, os, re, sys, time, urllib.parse
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from comun import AQUI, Frenar, avisar_externo, cfg, compras_pixel, graph, hm, respuestas, tz

CFG = cfg()
TZ = tz()
FRENO = os.path.join(AQUI, "FRENADO")
SIM = "--simulacro" in sys.argv
YA = "--ahora" in sys.argv


def ahora():
    if "--hora" in sys.argv:
        h, m = sys.argv[sys.argv.index("--hora") + 1].split(":")
        return datetime.now(TZ).replace(hour=int(h), minute=int(m), second=0, microsecond=0)
    return datetime.now(TZ)


def usd(v):
    return f"US${v:,.0f}".replace(",", ".")


def r2(v):
    return f"{v:.2f}".replace(".", ",")


# ---------- Log y avisos ----------
MENSAJES = []


def log(t):
    linea = f"{datetime.now(TZ):%Y-%m-%d %H:%M:%S} {'[SIM] ' if SIM else ''}{t}"
    print(linea, flush=True)
    os.makedirs(os.path.join(AQUI, "log"), exist_ok=True)
    with open(os.path.join(AQUI, "log", f"{datetime.now(TZ):%Y-%m-%d}.log"), "a") as f:
        f.write(linea + "\n")


def avisar(texto):
    MENSAJES.append(texto)
    log(f"AVISO: {texto}")
    if not SIM:
        for e in avisar_externo(texto):
            log(f"  {e}")


# ---------- Estado ----------
def ruta(nombre):
    os.makedirs(os.path.join(AQUI, "estado"), exist_ok=True)
    return os.path.join(AQUI, "estado", f"{'simulacro-' if SIM else ''}{nombre}.json")


def leer(nombre, defecto):
    for p in (ruta(nombre), os.path.join(AQUI, "estado", f"{nombre}.json")):
        if os.path.exists(p):
            return json.load(open(p))
    return defecto


def escribir(nombre, datos):
    json.dump(datos, open(ruta(nombre), "w"), indent=1, ensure_ascii=False)


def ajustes():
    """Lo que el dueño cambió por WhatsApp/Telegram (modo, confirmación, pausa) pisa al config.json."""
    a = leer("ajustes", {})
    conf = a.get("confirmacion", CFG["confirmacion"]) if CFG.get("permitir_auto", True) else "confirmar"
    return {"modo": a.get("modo", CFG["modo"]), "confirmacion": conf, "pausado": a.get("pausado", False), "_raw": a}


# ---------- Datos: gasto de Meta, ventas SOLO de Impultienda ----------
def tok_de(c):
    return c.get("token") or "SURF_META_TOKEN"


def gasto(c, dia):
    ins = graph(f"{c['campana']}/insights?fields=spend&time_range=" + urllib.parse.quote(json.dumps({"since": dia, "until": dia})),
                token=tok_de(c)).get("data", [])
    return float(ins[0]["spend"]) if ins else 0.0


def ventas_impultienda(dia):
    """{campana_id: (ventas, usd)} del día, de lo que guardó receptor.py. None si el receptor no está andando."""
    p = os.path.join(AQUI, "ventas", f"{dia}.json")
    if not os.path.exists(os.path.join(AQUI, "ventas", "ordenes.json")):
        return None   # el receptor nunca recibió nada: no está instalado o Impultienda no tiene el webhook
    d = json.load(open(p)) if os.path.exists(p) else {"campanas": {}}
    return {k: (v["ventas"], v["usd"]) for k, v in d["campanas"].items()}


# ---------- Horarios por oferta ----------
def curva_oferta(oferta, t):
    """Compras del pixel por hora (en tu huso) de las campañas de la oferta, últimos N días.
    Sirve solo para saber CUÁNDO se mueve la oferta; las decisiones de ROAS son con Impultienda."""
    H = CFG["horarios"]
    rango = urllib.parse.quote(json.dumps({"since": (t - timedelta(days=H["dias_analisis"])).strftime("%Y-%m-%d"),
                                           "until": (t - timedelta(days=1)).strftime("%Y-%m-%d")}))
    compras, vistas = [0.0] * 24, set()
    for c in CFG["campanas"]:
        if c.get("oferta") != oferta:
            continue
        for cid in [c["campana"]] + c.get("analizar_tambien", []):
            if cid in vistas:
                continue
            vistas.add(cid)
            acc = graph(f"{cid}?fields=account_id", token=tok_de(c))["account_id"]
            zona = ZoneInfo(graph(f"act_{acc}?fields=timezone_name", token=tok_de(c))["timezone_name"])
            dif = round((datetime.now(TZ).utcoffset() - datetime.now(zona).utcoffset()).total_seconds() / 3600)
            filas = graph(f"{cid}/insights?fields=actions&breakdowns=hourly_stats_aggregated_by_advertiser_time_zone"
                          f"&time_range={rango}&limit=100", token=tok_de(c)).get("data", [])
            for f in filas:
                h = int(f["hourly_stats_aggregated_by_advertiser_time_zone"][:2])
                compras[(h + dif) % 24] += compras_pixel(f.get("actions"))
    return compras


def cortes_a_horarios(compras, cortes, separacion_h):
    """La hora en que la oferta ya juntó cada % de sus ventas del día (ej. 25/50/75 %): cada análisis llega con ventas frescas.
    Si un horario cae a menos de separacion_h del anterior, se corre hasta respetar la separación."""
    total, out, acum = sum(compras), [], 0.0
    for h in range(24):
        acum += compras[h]
        while len(out) < len(cortes) and acum >= cortes[len(out)] * total:
            m = (h + 1) * 60
            if out:
                m = max(m, hm(out[-1]) + separacion_h * 60)
            out.append(f"{min(m, 23 * 60) // 60:02d}:00")
    return sorted(set(out))


def horarios_oferta(oferta, t):
    """Calcula una vez por día los horarios de la oferta. Con pocas ventas usa los de respaldo del config."""
    H = CFG["horarios"]
    guardado = leer("horarios", {})
    g = guardado.get(oferta)
    if g and g.get("dia") == t.strftime("%Y-%m-%d"):
        return g
    try:
        compras = curva_oferta(oferta, t)
    except Frenar:
        raise
    except Exception as e:
        log(f"{oferta}: no pude analizar los horarios ({e}); uso los de respaldo")
        compras = [0.0] * 24
    total = sum(compras)
    g = {"dia": t.strftime("%Y-%m-%d"), "compras": [round(x) for x in compras], "total": round(total)}
    if total >= H["compras_minimas"]:
        g.update(fuente="ventas", agresivo=cortes_a_horarios(compras, H["cortes_agresivo"], H["separacion_min_h"]),
                 tranquilo=cortes_a_horarios(compras, H["cortes_tranquilo"], 0))
    else:
        g.update(fuente="respaldo", agresivo=CFG["modos"]["agresivo"]["horarios"], tranquilo=CFG["modos"]["tranquilo"]["horarios"])
    pico = max(range(24), key=lambda h: sum(compras[(h + i) % 24] for i in range(3))) if total else None
    g["pico"] = f"{pico:02d}–{(pico + 3) % 24:02d} h" if pico is not None else "-"
    guardado[oferta] = g
    escribir("horarios", guardado)
    av = leer("horarios_avisados", {})
    if (av.get(oferta) or {}) != {"agresivo": g["agresivo"], "tranquilo": g["tranquilo"]}:
        av[oferta] = {"agresivo": g["agresivo"], "tranquilo": g["tranquilo"]}
        escribir("horarios_avisados", av)
        fuente = (f"según {g['total']} ventas de los últimos {H['dias_analisis']} días, pico {g['pico']}" if g["fuente"] == "ventas"
                  else f"pocas ventas para analizar ({g['total']}), uso los de respaldo")
        avisar(f"🕐 Horarios de {oferta} ({fuente}):\n· agresivo: {', '.join(g['agresivo'])}\n· tranquilo / 1 vez al día: {', '.join(g['tranquilo'])}")
    return g


def horarios_de(modo, presupuesto, hor):
    """Bajo el umbral (US$700): los horarios del modo. Desde el umbral: una vez al día (el de tranquilo)."""
    if presupuesto >= CFG["umbral_diario_usd"]:
        return hor["tranquilo"], f"1 vez al día (CBO ≥ {usd(CFG['umbral_diario_usd'])})"
    return hor[modo], modo


def toca(t, horarios, hechos):
    minuto = t.hour * 60 + t.minute
    for h in horarios:
        if hm(h) <= minuto < hm(h) + 60 and h not in hechos:
            return h
    return None


# ---------- Decisión (método V3) ----------
def decidir(c, modo, presupuesto, d):
    """(accion, nuevo_presupuesto, motivo). accion: 'subir' | 'tiron' | 'quieta'."""
    M = CFG["modos"][modo]
    ticket = c["ticket"]
    g, v, f = d["gasto_hoy"], d["ventas_hoy"], d["usd_hoy"]
    roas = f / g if g else None
    roas_ayer = d["usd_ayer"] / d["gasto_ayer"] if d["gasto_ayer"] else None
    piso, techo = c.get("presupuesto_piso", 0), c.get("presupuesto_max") or 1e12
    if g < M["gasto_min_tickets"] * ticket:
        return "quieta", presupuesto, f"gastó {usd(g)} hoy, todavía no llega a {M['gasto_min_tickets']} tickets ({usd(M['gasto_min_tickets'] * ticket)}) para juzgar"
    # tirón de oreja: hoy flaquea. Si ayer bancó, una mañana floja no alcanza: solo tira si hoy viene muy mal
    if roas < M["roas_tiron"]:
        if roas_ayer is not None and roas_ayer >= M["roas_subir_ayer"] and roas >= M["roas_tiron_con_ayer_bueno"]:
            return "quieta", presupuesto, f"ROAS hoy {r2(roas)} flojo, pero ayer bancó ({r2(roas_ayer)}): espera"
        nuevo = max(piso, round(presupuesto * (1 - M["tiron_pct"]), 2))
        if nuevo >= presupuesto:
            return "quieta", presupuesto, f"ROAS hoy {r2(roas)} pero ya está en el piso ({usd(piso)})"
        return "tiron", nuevo, f"ROAS hoy {r2(roas)} < {r2(M['roas_tiron'])} con {usd(g)} gastados"
    # surfeo: hoy y ayer tienen que bancarlo
    if roas >= M["roas_subir_hoy"]:
        if v < M["ventas_min_subir"]:
            return "quieta", presupuesto, f"ROAS hoy {r2(roas)} pero con solo {v} ventas (pide {M['ventas_min_subir']})"
        if roas_ayer is None or d["gasto_ayer"] < M["gasto_min_tickets"] * ticket:
            return "quieta", presupuesto, f"ROAS hoy {r2(roas)}, pero ayer no tiene gasto suficiente para ver si es estable"
        if roas_ayer < M["roas_subir_ayer"]:
            return "quieta", presupuesto, f"ROAS hoy {r2(roas)} pero ayer {r2(roas_ayer)} (< {r2(M['roas_subir_ayer'])}): ayer bajo + hoy mejor = quieta"
        nuevo = min(techo, round(presupuesto * (1 + M["subida_pct"]), 2))
        if nuevo <= presupuesto:
            return "quieta", presupuesto, f"ROAS hoy {r2(roas)} / ayer {r2(roas_ayer)}, pero ya está en el techo ({usd(techo)})"
        return "subir", nuevo, f"ROAS hoy {r2(roas)} ({v} ventas) y ayer {r2(roas_ayer)}"
    ra = f" · ayer {r2(roas_ayer)}" if roas_ayer is not None else ""
    return "quieta", presupuesto, f"ROAS hoy {r2(roas)}{ra}: entre {r2(M['roas_tiron'])} y {r2(M['roas_subir_hoy'])}, se mantiene"


def cambiar_presupuesto(c, de, a, accion, ref=""):
    """Cambia el daily_budget de la CBO, relee en Meta y manda la confirmación con lo que Meta muestra."""
    if SIM:
        return True
    graph(c["campana"], {"daily_budget": round(a * 100)}, token=tok_de(c))
    x = {}
    for _ in range(10):  # justo después del cambio Meta muestra IN_PROCESS unos segundos: es normal
        time.sleep(3)
        x = graph(f"{c['campana']}?fields=daily_budget,effective_status", token=tok_de(c))
        if abs(int(x.get("daily_budget") or 0) - round(a * 100)) <= 1 and x.get("effective_status") != "IN_PROCESS":
            break
    actual, estado = int(x.get("daily_budget") or 0) / 100, x.get("effective_status")
    if abs(actual - a) > 0.01:
        avisar(f"⚠️ {c['nombre']}: pedí pasar la CBO de {usd(de)} a {usd(a)} y Meta muestra {usd(actual)}. Revisala.")
        return False
    verbo = "SURFEO +30 % aplicado" if accion == "subir" else "TIRÓN −30 % aplicado"
    est = ("activa ✅" if estado == "ACTIVE" else
           "procesando el cambio (normal, en unos minutos queda activa)" if estado == "IN_PROCESS" else f"'{estado}' ⚠️ revisala")
    avisar(f"✅ {verbo}{' ' + ref if ref else ''}\n{c['nombre']}\n· CBO {usd(de)} → {usd(actual)} (verificado en Meta)\n· campaña {est}")
    return True


def registrar(t, c, de, a, accion, motivo):
    h = leer("historial", [])
    h.append({"t": t.isoformat(), "campana": c["campana"], "nombre": c["nombre"], "accion": accion, "de": de, "a": a, "motivo": motivo})
    escribir("historial", h[-500:])


def campana_por_id(cid):
    return next((c for c in CFG["campanas"] if c["campana"] == cid), None)


# ---------- Confirmaciones y comandos (WhatsApp / Telegram) ----------
def procesar_respuestas(t, aj):
    marca = leer("ultimo_mensaje", {"ts": int(t.timestamp()) - 3600})
    prop = leer("propuestas", {"siguiente": 1, "abiertas": {}, "resueltas": {}})
    raw = dict(aj["_raw"])
    for ts, txt in respuestas(marca["ts"]):
        marca["ts"] = max(marca["ts"], ts)
        low = txt.lower().replace("í", "i").strip(" .!")
        m = re.fullmatch(r"(si|no)\s*#?\s*(\d+)?", low)
        if m:
            ids = [m.group(2)] if m.group(2) else sorted(prop["abiertas"], key=int)   # "SI" solo = todas las abiertas
            if not ids:
                avisar("No hay propuestas abiertas para confirmar.")
            for pid in ids:
                p = prop["abiertas"].pop(pid, None)
                if not p:
                    if not prop.get("resueltas", {}).get(pid):
                        avisar(f"La propuesta #{pid} ya no está abierta (venció).")
                    continue
                c = campana_por_id(p["campana"])
                if m.group(1) == "no" or not c:
                    prop.setdefault("resueltas", {})[pid] = "rechazada"
                    avisar(f"❌ #{pid} {p['nombre']}: no la aplico. Queda en {usd(p['de'])}.")
                    continue
                actual = int(graph(f"{c['campana']}?fields=daily_budget", token=tok_de(c)).get("daily_budget") or 0) / 100
                if abs(actual - p["de"]) > 0.01:
                    avisar(f"⚠️ #{pid} {p['nombre']}: la CBO ya no está en {usd(p['de'])} (ahora {usd(actual)}): alguien la movió. No la aplico.")
                    continue
                if cambiar_presupuesto(c, p["de"], p["a"], p["accion"], f"#{pid}"):
                    registrar(t, c, p["de"], p["a"], p["accion"], p["motivo"] + f" · confirmada #{pid}")
                    prop.setdefault("resueltas", {})[pid] = "aplicada"
            continue
        m = re.fullmatch(r"surf\s+(agresivo|tranquilo|auto|confirmar|pausa|seguir|estado)", low)
        if not m:
            continue
        cmd = m.group(1)
        if cmd in ("agresivo", "tranquilo"):
            raw["modo"] = cmd
            avisar(f"Modo {cmd.upper()} activado.")
        elif cmd == "auto" and not CFG.get("permitir_auto", True):
            avisar("🔒 El modo automático está bloqueado en esta instalación: todo cambio te lo pido con SI / NO.")
        elif cmd in ("auto", "confirmar"):
            raw["confirmacion"] = cmd
            avisar("Desde ahora aplico los cambios solo y te aviso." if cmd == "auto" else "Desde ahora te pido confirmación antes de cada cambio.")
        elif cmd == "pausa":
            raw["pausado"] = True
            avisar("⏸ En pausa: no propongo ni muevo nada hasta que escribas 'surf seguir'.")
        elif cmd == "seguir":
            raw["pausado"] = False
            avisar("▶️ Sigo surfeando.")
        elif cmd == "estado":
            raw["pedir_estado"] = True
    for pid, p in list(prop["abiertas"].items()):
        if t.timestamp() - p["ts"] > CFG["confirmacion_vence_min"] * 60:
            prop["abiertas"].pop(pid)
            avisar(f"⌛ #{pid} {p['nombre']}: venció sin respuesta, no la aplico.")
    if not SIM:
        escribir("ultimo_mensaje", marca)
    escribir("propuestas", prop)
    escribir("ajustes", raw)
    return prop


# ---------- Corrida ----------
def main():
    if os.path.exists(FRENO) and not SIM:
        print(f"FRENADO: {open(FRENO).read()}  (borrá el archivo FRENADO para reanudar)")
        return
    t = ahora()
    dia, ayer = t.strftime("%Y-%m-%d"), (t - timedelta(days=1)).strftime("%Y-%m-%d")
    st = leer(dia, {"dia": dia, "campanas": {}})
    try:
        prop = procesar_respuestas(t, ajustes())
        aj = ajustes()
        if aj["pausado"]:
            log("En pausa ('surf seguir' para reanudar).")
            return
        activas = [c for c in CFG["campanas"] if c.get("activa", True)]
        pendientes, info = [], {}
        for c in activas:
            s = st["campanas"].setdefault(c["campana"], {"nombre": c["nombre"], "evaluados": [], "decisiones": []})
            try:  # un permiso caído en una campaña no frena a las demás
                x = graph(f"{c['campana']}?fields=name,daily_budget,effective_status,account_id", token=tok_de(c))
                moneda = graph(f"act_{x['account_id']}?fields=currency", token=tok_de(c)).get("currency")
            except Frenar as e:
                if not s.get("aviso_permiso"):
                    avisar(f"⚠️ {c['nombre']}: no la puedo leer en Meta ({e}). La salteo hoy.")
                    s["aviso_permiso"] = True
                continue
            if not x.get("daily_budget"):
                if not s.get("aviso_abo"):
                    avisar(f"⚠️ {c['nombre']}: no tiene presupuesto de campaña (¿es ABO?). La salteo.")
                    s["aviso_abo"] = True
                continue
            if moneda != "USD":
                if not s.get("aviso_moneda"):
                    avisar(f"⚠️ {c['nombre']}: la cuenta está en {moneda}, no en dólares; el ROAS no cerraría con Impultienda. La salteo.")
                    s["aviso_moneda"] = True
                continue
            modo = c.get("modo") or aj["modo"]
            presupuesto = int(x["daily_budget"]) / 100
            horarios, cadencia = horarios_de(modo, presupuesto, horarios_oferta(c["oferta"], t))
            h = toca(t, horarios, s["evaluados"])
            if YA:
                if h:
                    s["evaluados"].append(h)
                h = f"{t:%H:%M} (a pedido)"
            info[c["campana"]] = (modo, presupuesto, f"{cadencia}: {', '.join(horarios)}")
            if h and x.get("effective_status") in ("ACTIVE", "IN_PROCESS"):
                pendientes.append((c, h))
            elif h:
                s["evaluados"].append(h)
                log(f"{c['nombre']}: está '{x.get('effective_status')}', no la toco.")
        if not pendientes and not aj["_raw"].get("pedir_estado"):
            return
        v_hoy, v_ayer = ventas_impultienda(dia), ventas_impultienda(ayer)
        if v_hoy is None:
            if not st.get("aviso_impultienda"):
                avisar("⚠️ No hay ventas de Impultienda: el receptor no recibió nada todavía. Sin ventas reales no muevo ninguna CBO.")
                st["aviso_impultienda"] = True
            return
        st["aviso_impultienda"] = False
        lineas = [f"📊 {t:%H:%M} · modo {aj['modo'].upper()} · {'automático' if aj['confirmacion'] == 'auto' else 'con confirmación'}"]
        for c in activas:
            if c["campana"] not in info:
                continue
            h = next((h for cc, h in pendientes if cc is c), None)
            if not h and not aj["_raw"].get("pedir_estado"):
                continue   # el parte trae solo las campañas que tocaba analizar ahora
            modo, presupuesto, cadencia = info[c["campana"]]
            d = {"gasto_hoy": gasto(c, dia), "gasto_ayer": gasto(c, ayer),
                 "ventas_hoy": v_hoy.get(c["campana"], (0, 0.0))[0], "usd_hoy": v_hoy.get(c["campana"], (0, 0.0))[1],
                 "ventas_ayer": (v_ayer or {}).get(c["campana"], (0, 0.0))[0], "usd_ayer": (v_ayer or {}).get(c["campana"], (0, 0.0))[1]}
            roas = d["usd_hoy"] / d["gasto_hoy"] if d["gasto_hoy"] else 0
            base = f"\n{c['nombre']}\n· CBO {usd(presupuesto)} · gasto hoy {usd(d['gasto_hoy'])} · {d['ventas_hoy']} ventas · ROAS {r2(roas)}"
            if not h:
                lineas.append(base + f"\n· próximo análisis: {cadencia}")
                continue
            s = st["campanas"][c["campana"]]
            accion, nuevo, motivo = decidir(c, modo, presupuesto, d)
            s["evaluados"].append(h)
            s["decisiones"].append({"h": h, "accion": accion, "de": presupuesto, "a": nuevo, "motivo": motivo, "datos": d})
            log(f"{c['nombre']} [{h} · {cadencia}]: {accion} {presupuesto} → {nuevo} · {motivo} · {d}")
            if accion == "quieta":
                lineas.append(base + f"\n· 🟰 quieta: {motivo}")
                continue
            flecha = "🏄 SURFEO +" if accion == "subir" else "👂 TIRÓN −"
            pct = round(abs(nuevo / presupuesto - 1) * 100)
            if aj["confirmacion"] == "auto":
                if cambiar_presupuesto(c, presupuesto, nuevo, accion):
                    registrar(t, c, presupuesto, nuevo, accion, motivo)
                    lineas.append(base + f"\n· {flecha}{pct} %: {usd(presupuesto)} → {usd(nuevo)} ({motivo}) ✅ aplicado")
            else:
                pid = str(prop["siguiente"]); prop["siguiente"] += 1
                prop["abiertas"][pid] = {"campana": c["campana"], "nombre": c["nombre"], "accion": accion, "de": presupuesto,
                                         "a": nuevo, "motivo": motivo, "ts": int(t.timestamp())}
                lineas.append(base + f"\n· {flecha}{pct} %: {usd(presupuesto)} → {usd(nuevo)} ({motivo})"
                                     f"\n  👉 Respondé *SI {pid}* o *NO {pid}* (vence en {CFG['confirmacion_vence_min']} min)")
        if len(lineas) > 1:
            avisar("\n".join(lineas))
        escribir("propuestas", prop)
        raw = leer("ajustes", {}); raw.pop("pedir_estado", None); escribir("ajustes", raw)
    except Frenar as e:
        avisar(f"🛑 FRENADO: {e}. No reintento. Para reanudar borrá {FRENO}.")
        if not SIM:
            open(FRENO, "w").write(f"{datetime.now(TZ):%Y-%m-%d %H:%M} {e}")
    except Exception as e:
        avisar(f"⚠️ Error en esta corrida, salteo hasta la próxima: {e}")
    finally:
        escribir(dia, st)
    if SIM:
        print("\n===== MENSAJES QUE MANDARÍA =====")
        print("\n---\n".join(MENSAJES) or "(ninguno)")


if __name__ == "__main__":
    main()
```

### receptor.py

```python
"""Surfing Scale Automatic Bid Launch Expert — receptor de ventas de Impultienda (OBLIGATORIO).
El ROAS del Surfing Scale sale SOLO de acá, nunca de Utmify: Utmify recibe la venta recién cuando el cliente termina o
abandona el post-compra (~20 min) y la campaña parece peor de lo que está. Este receptor toma el webhook de Impultienda
(evento order.approved) en el momento y lo guarda por campaña en ventas/AAAA-MM-DD.json, por la FECHA DE LA ORDEN.
Corre en el servidor como servicio (systemd) detrás de Caddy, que le pone HTTPS gratis.
URL para pegar en Impultienda:  https://<IP-con-guiones>.sslip.io/venta?k=<SURF_WEBHOOK_CLAVE>
"""
import json, os, re, threading, urllib.request
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from comun import AQUI, secreto, tz

CLAVE = secreto("SURF_WEBHOOK_CLAVE")
TZ = tz()
DIR = os.path.join(AQUI, "ventas")
os.makedirs(DIR, exist_ok=True)
LOCK = threading.Lock()
_tasas = {"dia": None, "rates": {}}


def a_usd(monto, moneda):
    """Convierte a dólares con la cotización del día (open.er-api.com, sin clave). Si falla, deja el monto como está."""
    moneda = (moneda or "USD").upper()
    if moneda == "USD":
        return monto
    hoy = datetime.now(TZ).strftime("%Y-%m-%d")
    if _tasas["dia"] != hoy:
        try:
            r = json.load(urllib.request.urlopen(urllib.request.Request(
                "https://open.er-api.com/v6/latest/USD", headers={"User-Agent": "surfing-scale/1.0"}), timeout=20))
            _tasas.update(dia=hoy, rates=r["rates"])
        except Exception:
            pass
    tasa = _tasas["rates"].get(moneda)
    return monto / tasa if tasa else monto


def leer(p, vacio):
    return json.load(open(p)) if os.path.exists(p) else vacio


def escribir(p, datos):
    tmp = p + ".tmp"
    json.dump(datos, open(tmp, "w"), indent=1, ensure_ascii=False)
    os.replace(tmp, p)


def registrar(p):
    """Guarda una venta (o resta un reembolso) en la campaña que la trajo. Devuelve lo que hizo."""
    evento = p.get("event") or p.get("type") or ""
    if evento not in ("order.approved", "order.refunded", "order.chargeback"):
        return f"ignorado: {evento}"
    d = p.get("data") or {}
    if d.get("test") or p.get("test") or str(d.get("order_id", "")).upper().startswith("TEST"):
        return "prueba: no se cuenta"
    oid = str(d.get("order_id") or p.get("id") or "")
    tr = d.get("tracking") or {}
    camp = str(tr.get("utm_id") or "").strip()
    if not re.fullmatch(r"\d{6,}", camp):
        m = re.search(r"\|\s*(\d{6,})\s*$", str(tr.get("utm_campaign") or ""))   # formato Utmify: nombre|id
        camp = m.group(1) if m else ""
    with LOCK:
        idx = leer(os.path.join(DIR, "ordenes.json"), {})
        clave = f"{oid}:{evento}"
        if clave in idx.get("_vistos", []):
            return "duplicado"
        # el upsell post-compra hereda la campaña de su orden padre
        if not camp and d.get("is_post_purchase") and d.get("parent_order_id"):
            camp = idx.get(str(d["parent_order_id"]), "")
        if oid and camp:
            idx[oid] = camp
        idx.setdefault("_vistos", []).append(clave)
        idx["_vistos"] = idx["_vistos"][-5000:]
        escribir(os.path.join(DIR, "ordenes.json"), idx)
        # Día = fecha de la ORDEN, no la del aviso: Impultienda reenvía en tanda aprobaciones tardías de días anteriores
        # (pagos que se aprueban horas después) y, si se cuentan el día que llega el aviso, inflan el ROAS de "hoy".
        cuando = datetime.now(TZ)
        for f in (d.get("order_created_at"), d.get("created_at"), p.get("created_at")):
            if f:
                try:
                    cuando = datetime.fromisoformat(str(f).replace("Z", "+00:00"))
                    cuando = (cuando if cuando.tzinfo else cuando.replace(tzinfo=TZ)).astimezone(TZ)
                    break
                except ValueError:
                    continue
        archivo = os.path.join(DIR, f"{cuando:%Y-%m-%d}.json")
        dia = leer(archivo, {"campanas": {}, "sin_campana": {"ventas": 0, "usd": 0.0}})
        fila = dia["campanas"].setdefault(camp, {"ventas": 0, "usd": 0.0}) if camp else dia["sin_campana"]
        signo = 1 if evento == "order.approved" else -1
        fila["usd"] = round(fila["usd"] + signo * a_usd(float(d.get("total") or 0), d.get("currency")), 2)
        if not d.get("is_post_purchase"):     # el upsell suma plata pero no cuenta como venta nueva
            fila["ventas"] += signo
        escribir(archivo, dia)
    return f"ok {evento} campaña {camp or 'sin campaña'}"


class H(BaseHTTPRequestHandler):
    def _resp(self, code, txt):
        self.send_response(code); self.send_header("Content-Type", "application/json"); self.end_headers()
        self.wfile.write(json.dumps({"ok": code == 200, "msg": txt}).encode())

    def do_POST(self):
        u = urlparse(self.path)
        if u.path != "/venta" or parse_qs(u.query).get("k", [""])[0] != CLAVE:
            return self._resp(403, "clave")
        try:
            p = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
            self._resp(200, registrar(p))
        except Exception as e:
            self._resp(500, str(e)[:200])   # la plataforma reintenta

    def do_GET(self):
        self._resp(200, "receptor del Surfing Scale funcionando")

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8787), H).serve_forever()
```

### buscar.py

```python
"""Surfing Scale Automatic Bid Launch Expert — busca las CBO activas de una oferta en todas tus cuentas.
Uso:  python3 buscar.py "Mi Oferta"                         -> lista lo que encuentra (no cambia nada)
      python3 buscar.py "Mi Oferta" --guardar --oferta "🇦🇷 Mi Oferta" --ticket 15 [--piso 30] [--token SURF_META_TOKEN_2]
                                                             -> las agrega a config.json (sin duplicar)
Muestra moneda, presupuesto, gasto de hoy y si es CBO. Solo se pueden surfear CBO en cuentas en dólares."""
import json, os, sys

from comun import AQUI, graph


def arg(nombre, defecto=None):
    return sys.argv[sys.argv.index(nombre) + 1] if nombre in sys.argv else defecto


def main():
    if len(sys.argv) < 2 or sys.argv[1].startswith("--"):
        print(__doc__)
        return
    filtro, token = sys.argv[1].lower(), arg("--token", "SURF_META_TOKEN")
    cuentas = graph("me/adaccounts?fields=name,account_status,currency&limit=200", token=token).get("data", [])
    halladas = []
    for a in cuentas:
        if a.get("account_status") != 1:
            continue
        camps = graph(f"{a['id']}/campaigns?fields=name,daily_budget,effective_status&effective_status=[\"ACTIVE\"]&limit=200",
                      token=token).get("data", [])
        for c in camps:
            if filtro not in c["name"].lower():
                continue
            ins = graph(f"{c['id']}/insights?fields=spend&date_preset=today", token=token).get("data", [])
            halladas.append({"nombre": c["name"], "campana": c["id"], "cuenta": a["name"], "moneda": a.get("currency"),
                             "cbo": bool(c.get("daily_budget")), "presupuesto": int(c.get("daily_budget") or 0) / 100,
                             "gasto_hoy": float(ins[0]["spend"]) if ins else 0.0})
    for h in halladas:
        ok = "OK " if h["cbo"] and h["moneda"] == "USD" else "NO "
        motivo = "" if ok == "OK " else ("(no es CBO)" if not h["cbo"] else f"(cuenta en {h['moneda']})")
        print(f"{ok}{h['nombre'][:45]:45} | {h['campana']} | {h['cuenta'][:22]:22} | CBO US${h['presupuesto']:.0f} | hoy US${h['gasto_hoy']:.0f} {motivo}")
    if "--guardar" not in sys.argv:
        print(f"\n{len(halladas)} campañas. Para agregarlas: --guardar --oferta \"<nombre de la oferta>\" --ticket <precio del front>")
        return
    p = os.path.join(AQUI, "config.json")
    cfg = json.load(open(p))
    ya = {c["campana"] for c in cfg["campanas"]}
    nuevas = 0
    for h in halladas:
        if not h["cbo"] or h["moneda"] != "USD" or h["campana"] in ya:
            continue
        fila = {"nombre": h["nombre"], "oferta": arg("--oferta", sys.argv[1]), "campana": h["campana"],
                "ticket": float(arg("--ticket", 0)), "presupuesto_piso": float(arg("--piso", 2 * float(arg("--ticket", 0)))),
                "presupuesto_max": None, "activa": True}
        if token != "SURF_META_TOKEN":
            fila["token"] = token
        cfg["campanas"].append(fila)
        nuevas += 1
    json.dump(cfg, open(p, "w"), indent=2, ensure_ascii=False)
    print(f"\nAgregadas {nuevas} campañas a config.json.")


if __name__ == "__main__":
    main()
```

### instalar_servidor.sh

```bash
#!/bin/bash
# Surfing Scale Automatic Bid Launch Expert — instala todo en un servidor Ubuntu 24.04 (DigitalOcean US$6/mes).
# Se corre UNA vez en el servidor, como root, con los archivos ya copiados en /opt/surfing:
#   bash /opt/surfing/instalar_servidor.sh
set -e
cd /opt/surfing
apt-get update -qq
apt-get install -y -qq python3 tzdata curl > /dev/null
chmod 600 .env
mkdir -p estado log ventas

if ! grep -q '^SURF_WEBHOOK_CLAVE=.' .env; then
  echo "Falta SURF_WEBHOOK_CLAVE en .env: sin el receptor de Impultienda el Surfing Scale no tiene ventas. Agregala y volvé a correr esto."
  exit 1
fi

# 1) Receptor de ventas de Impultienda, con HTTPS gratis (Caddy + dirección sslip.io)
apt-get install -y -qq caddy > /dev/null
IP=$(curl -s https://api.ipify.org)
HOST="$(echo "$IP" | tr . -).sslip.io"
cat > /etc/caddy/Caddyfile <<CADDY
$HOST {
  reverse_proxy 127.0.0.1:8787
}
CADDY
cat > /etc/systemd/system/surfing-receptor.service <<'UNIT'
[Unit]
Description=Surfing Scale - receptor de ventas de Impultienda
After=network.target
[Service]
WorkingDirectory=/opt/surfing
ExecStart=/usr/bin/python3 /opt/surfing/receptor.py
Restart=always
[Install]
WantedBy=multi-user.target
UNIT
systemctl daemon-reload
systemctl enable --now surfing-receptor
systemctl restart caddy

# 2) El Surfing Scale corre cada 10 minutos (lee tus SI/NO y decide en los horarios de cada oferta); flock evita que se pisen
cat > /etc/cron.d/surfing <<'CRON'
SHELL=/bin/bash
*/10 * * * * root cd /opt/surfing && flock -n /tmp/surfing.lock python3 surfing.py >> log/cron.out 2>&1
CRON
chmod 644 /etc/cron.d/surfing

CLAVE=$(grep '^SURF_WEBHOOK_CLAVE=' .env | cut -d= -f2)
echo
echo "Instalado."
echo "URL del webhook para Impultienda (Configuraciones → Webhooks, eventos order.approved, order.refunded y order.chargeback):"
echo "  https://$HOST/venta?k=$CLAVE"
echo
echo "Prueba sin tocar nada:"
python3 surfing.py --simulacro --ahora | tail -30
```

### config.ejemplo.json

```json
{
  "_nota": "Montos en US$ (la moneda de tus cuentas publicitarias). 'ticket' = precio del front. Las campañas las agrega buscar.py; vos confirmás los números.",
  "huso": "America/Argentina/Buenos_Aires",
  "modo": "agresivo",
  "confirmacion": "confirmar",
  "permitir_auto": true,
  "confirmacion_vence_min": 90,
  "umbral_diario_usd": 700,
  "horarios": {
    "_nota": "Se calculan por oferta con las compras por hora de los últimos días: agresivo = cuando la oferta juntó 25/50/75 % de sus ventas del día; tranquilo y 1 vez al día = cuando juntó el 60 %. Los 'horarios' de cada modo son el respaldo si hay pocas ventas.",
    "dias_analisis": 14,
    "compras_minimas": 40,
    "cortes_agresivo": [0.25, 0.5, 0.75],
    "cortes_tranquilo": [0.6],
    "separacion_min_h": 3
  },
  "modos": {
    "agresivo": {
      "horarios": ["09:00", "12:00", "15:00", "18:00", "21:00"],
      "subida_pct": 0.30,
      "tiron_pct": 0.30,
      "roas_subir_hoy": 2.0,
      "roas_subir_ayer": 1.5,
      "roas_tiron": 1.0,
      "roas_tiron_con_ayer_bueno": 0.7,
      "gasto_min_tickets": 2,
      "ventas_min_subir": 2
    },
    "tranquilo": {
      "horarios": ["20:00"],
      "subida_pct": 0.30,
      "tiron_pct": 0.30,
      "roas_subir_hoy": 2.0,
      "roas_subir_ayer": 2.0,
      "roas_tiron": 0.9,
      "roas_tiron_con_ayer_bueno": 0.6,
      "gasto_min_tickets": 3,
      "ventas_min_subir": 3
    }
  },
  "campanas": []
}
```