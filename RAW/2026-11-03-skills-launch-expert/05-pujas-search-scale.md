# Pujas Search Scale · Launch Expert

> Skill para instalar en tu segundo cerebro. Le decís tu oferta y tu IA te detecta los horarios que venden, te arma las campañas Cost Cap y Bid Cap con tus ganadores, te conecta los avisos por Telegram o WhatsApp y deja corriendo un bot que mueve las pujas cada media hora, todos los días.

---

## 0. Instrucciones para la IA

Esto es una skill completa. Si sos la IA del alumno y te pegaron este texto, seguí estos pasos al pie de la letra.

**Cuándo se activa:** cuando el alumno diga "instalá Pujas Search Scale", "armá las pujas para mi oferta", "Cost Cap / Bid Cap con el bot", "bot de pujas", o pegue este manual.

**Paso 1 · Guardar la skill.** Creá la carpeta `~/.claude/skills/pujas-search-scale/` y guardá este manual entero como `SKILL.md`, con este encabezado arriba de todo:

```
---
name: pujas-search-scale
description: Bot de pujas Launch Expert. Detecta horarios y picos de venta de una oferta, arma Cost Cap y Bid Cap con los winners en cuentas aisladas, conecta avisos por Telegram/WhatsApp y deja corriendo el bot de pujas en escalera cada 30 min. Usar cuando el alumno diga "pujas", "cost cap", "bid cap", "bot de pujas" o "Pujas Search Scale".
---
```

**Paso 2 · Crear la carpeta de trabajo.** `~/pujas-search-scale/` (fuera de cualquier carpeta que se sincronice con GitHub o con la nube: ahí va a vivir el archivo `.env` con las claves). Escribí ahí, tal cual, cada archivo de la sección 12. Copiá `config.ejemplo.json` como `config.json`. Corré `python3 -c "import ast,glob;[ast.parse(open(f).read()) for f in glob.glob('*.py')]"` para confirmar que se copiaron bien.

**Paso 3 · Pedir los datos, de a uno.** No le tires una lista de diez preguntas. Pedí en este orden y explicá cómo conseguir cada cosa con la sección 5:
1. El nombre de la oferta, el país, el precio del front y el ticket promedio con upsells (en dólares).
2. El token de Meta. Que lo pegue **directo en el archivo `.env`** (abrilo vos con `open -e ~/pujas-search-scale/.env` en Mac); vos no lo repetís nunca en el chat.
3. Si usa Utmify: el token del MCP y el ID del dashboard. Si no usa Utmify, el bot trabaja con el pixel.
4. Cómo quiere los avisos: Telegram, WhatsApp o los dos (sección 7).

**Paso 4 · Encontrar la oferta en Meta.** Listá sus cuentas con `me/adaccounts?fields=name,account_status,currency&limit=200` y buscá en cuáles corre la oferta (campañas activas cuyo nombre la contenga). Completá en `config.json` → `oferta`: `nombre`, `pais`, `filtro_campanas` (un pedazo del nombre de las campañas, sin emojis), `front`, `ticket`, `cuentas` (donde corre) y, si hay Utmify, `utmify_dashboard` y `productos_utmify` (el nombre exacto del producto front como figura en Utmify).

**Paso 5 · Horarios y picos.** Corré `python3 analizar.py`. Mostrale al alumno el mapa de 24 h, los picos y las horas que pierden, en una tabla corta. Explicale qué significa la hora de arranque de la escalera y la del reinicio. Con su OK, `python3 analizar.py --guardar`.

**Paso 6 · Ganadores.** Corré `python3 winners.py`. Mostrale los 8 ganadores con ROAS, gasto, ventas y CPA. Si un ganador tiene menos de 2 CPA de gasto o pocas ventas, no entra. Si quiere sacar alguno, editá `winners.json`.

**Paso 7 · Elegir las cuentas aisladas.** Necesitás **dos cuentas donde la oferta NO esté corriendo**: una para la Cost Cap y otra para la Bid Cap. Proponé las candidatas (activas, con medio de pago, sin campañas de esta oferta) y que el alumno elija. Cargá `config.json` → `lanzar` así:

```json
"lanzar": [
  {"tipo": "costcap", "cuenta": "<ID cuenta A>", "pixel": "<ID pixel de la oferta>", "presupuesto": 5000},
  {"tipo": "bidcap",  "cuenta": "<ID cuenta B>", "pixel": "<ID pixel de la oferta>", "presupuesto": 5000}
]
```

Pujas por defecto: Cost Cap = **CPA real de los ganadores** (sale de `winners.py`; si la fuente fue el pixel, confirmalo con Utmify, porque el pixel suele contar de más). Bid Cap = **front × 1,3**. Si el alumno quiere otra puja, va en `"puja"`. Si tiene un conjunto con la segmentación que le funciona, pasalo en `"targeting_desde"`; si no, se usa el país, 18-65, Advantage+ audiencia.

**Paso 8 · Crear en pausa.** `python3 crear.py --revisar` y mostrá lo que va a crear. Después `python3 crear.py` (crea todo **en pausa**, no gasta un peso). Pasale los nombres de las campañas para que las mire en el Administrador de anuncios.

**Paso 9 · Avisos.** Cargá los datos de Telegram y/o WhatsApp en `.env` (sección 7) y corré `python3 comun.py --probar-avisos`. Tiene que llegarle un mensaje. Si no llega, arreglalo antes de seguir.

**Paso 10 · Servidor.** El bot tiene que correr las 24 h, con la compu apagada. Seguí la sección 6 (DigitalOcean, US$6/mes). Si el alumno no quiere servidor, sección 6.4 (en su Mac, que tiene que quedar prendida).

**Paso 11 · Prender.** Pedí **confirmación explícita** ("¿prendo las dos campañas con US$5.000 de presupuesto y el bot?"). Con el sí: `python3 crear.py --prender` (en la copia local), subí `config.json` al servidor y corré ahí `python3 pujas.py --simulacro`. Mostrale el resultado. Desde ahí el bot corre solo a los :00 y :30.

**Reglas para vos, IA:**
- Nunca prendas campañas ni corras `pujas.py` sin `--simulacro` sin el sí del alumno.
- Nunca escribas tokens en el chat, en `config.json`, en el SKILL.md ni en carpetas que se sincronizan. Solo en `.env`.
- Un solo bot por operación: si corre en el servidor, en la Mac solo se usa `--simulacro`.
- Los cambios se hacen en la copia local y se suben al servidor con `scp`. El estado vivo (carpetas `estado/` y `ventas/`) está en el servidor.
- Montos en la moneda de la cuenta publicitaria (dólares). Si una cuenta está en otra moneda, avisá y pasá las pujas a esa moneda.
- Antes de tocar una regla del bot, mostrá qué cambia y por qué. Probá siempre en simulacro antes de subir.

---

## 1. Qué hace y qué esperar

Pujas Search Scale es la forma en la que escalamos ofertas validadas con **puja manual**: en lugar de dejar que Meta gaste lo que quiera, le decimos cuánto estamos dispuestos a pagar por venta, y un bot va moviendo ese número cada media hora según lo que pasa en la cuenta.

Lo que hace por vos:
- **Te detecta los horarios que venden.** Cruza el gasto por hora de Meta con las ventas por hora de Utmify y te marca los picos y las horas que queman plata.
- **Te arma las campañas.** Cost Cap y Bid Cap, cada una en su cuenta aislada, con tus ganadores clonados por post.
- **Mueve las pujas solo.** Busca el precio al que la campaña gasta, lo valida con ventas reales, abre la canilla cuando vende bien y frena cuando pierde.
- **Te avisa todo.** Cada cambio en el momento y un parte con todas las campañas a cada hora en punto, por Telegram o WhatsApp.

Qué esperar: esto es para **ofertas ya validadas** (que venden estable en CBO). No arregla una oferta que no convierte. Los primeros dos días el bot está aprendiendo los precios de tu oferta: no juzgues el sistema antes de 3 días.

---

## 2. La estructura de campañas

| | Cost Cap | Bid Cap |
|---|---|---|
| Qué le decís a Meta | "Quiero que el CPA **promedio** no pase de X" | "No pagues más de X **en cada subasta**" |
| Cómo se comporta | Gasta parejo, cerca del cap | Gasta rápido si el bid es alto; el CPA real puede pasar el bid |
| Puja de arranque | CPA real de tus ganadores (últimos 7 días) | Front × 1,3 |
| Tope del bot | 70 % del ticket o el CPA objetivo, el menor | Front × 1,8 |

La estructura es siempre la misma:
- **1 campaña CBO, 1 conjunto, tus 8 ganadores.** Nada de varios conjuntos ni de anuncios que no ganaron.
- **Presupuesto inflado: US$5.000/día.** El presupuesto no es el límite: el límite es la puja. Si Meta no encuentra ventas al precio que pusiste, no gasta.
- **Cada una en una cuenta aislada.** En la cuenta de la Cost Cap y en la de la Bid Cap la oferta no puede estar corriendo en otra campaña: dos campañas de la misma oferta en la misma cuenta compiten entre sí en la subasta. Una campaña por oferta y por mercado en cada cuenta.
- **Ganadores clonados por post.** Se usa el mismo post del anuncio ganador (`object_story_id`), así arranca con los likes y comentarios que ya juntó.
- **Sin mejoras creativas automáticas** de Advantage+: el ganador sale tal cual se validó.

---

## 3. Cómo trabaja el bot

El bot corre a los :00 y :30 de cada hora. Un día normal de cada campaña:

| Momento | Qué hace |
|---|---|
| **Reinicio** (02:00 por defecto) | Vuelve la puja y el presupuesto al original y reactiva lo que había frenado. Va después de los picos de la noche. |
| **Hasta la hora de ventas** | No toca nada: de madrugada no hay tráfico para medir precio. |
| **Hora de ventas** (30 min antes del primer pico) | Arranca la escalera. Si ayer validó un precio, arranca ahí. |
| **Escalera** | Si en la media hora gastó menos de la mitad de la puja, sube un escalón (7 % del ticket). |
| **Gasta** | El precio queda **en prueba** y la puja queda quieta. |
| **Gastó 2 CPA desde ahí** | Si vendió con ROAS 1,2 o más: **precio validado** y recién ahí abre la canilla. Si no: baja un escalón y ese precio queda como **techo del día**. |
| **Precio validado** | Ajustes de medio escalón. Boost de +20 % si el ROAS del día pasa 2,5 con 3 ventas o más (máximo uno por hora). Baja medio escalón si gasta 3 pujas sin vender o si el CPA se dispara con ROAS bajo. |
| **Freno de mano** | Si en el día pierde 3 CPA o más con ROAS menor a 0,8, **pausa el conjunto** hasta el reinicio. |
| **08:00** | Te manda el resumen: cómo cerró ayer cada campaña y a qué precio arrancó hoy. |
| **Cada hora en punto** | Parte con todas las campañas: puja, fase, gasto, ventas y ROAS. |

Los números de cada regla están en `config.json` → `reglas`. Vienen calibrados con campañas reales; no los toques hasta tener una semana de datos.

---

## 4. Lo que aprendimos (y ya está corregido en el bot)

- **Gastar no es vender.** La primera versión daba un precio por bueno apenas la campaña gastaba. Una campaña "encontró precio", se destapó y quemó en 3 horas a ROAS 0,75. Ahora el precio se valida con ventas reales después de 2 CPA de gasto.
- **Una venta en un CPA es ruido.** Con 1 CPA de prueba, el bot le puso techo a una campaña ganadora por debajo del precio que el día anterior le había dado ROAS 1,87. Por eso la prueba es de 2 CPA y el techo nunca baja del precio que ganó ayer.
- **Bajar el presupuesto no frena.** Meta gasta por encima del presupuesto diario cuando se lo bajás en el día: una campaña con tope de US$675 llegó a US$751. El freno ahora pausa el conjunto.
- **Bid Cap a 1,5 × el front salió caro.** Gastó rápido a un CPA mayor que el front, y en una oferta quemó 10 CPA con una sola venta. El método dice front × 1,3 y el tope del bot es front × 1,8.
- **Utmify llega 20 minutos tarde.** Recibe la venta cuando el cliente termina o abandona el post-compra. Una campaña recién prendida parece negativa aunque esté vendiendo. Por eso el bot toma el mayor entre Utmify y tu webhook de ventas (sección 8).
- **No cortes la noche.** El bot analiza y sube todo el día. El reinicio va después del último pico de la noche, no a las 00:00 en medio del pico.
- **Cada mañana no hay que bajar a la ganadora.** Las campañas creadas por este kit arrancan el día en el precio validado ayer, sin bajar escalones.

---

## 5. Lo que necesitás

| Qué | Para qué | Cómo conseguirlo |
|---|---|---|
| **Token de Meta** | Leer y mover campañas | Business Manager → Configuración del negocio → Usuarios del sistema → Agregar (admin) → Asignar activos (las cuentas publicitarias, con control total) → Generar token con permisos `ads_management`, `ads_read`, `business_management`. Ese token no vence. |
| **IDs de cuentas y pixel** | Saber dónde corre la oferta y dónde lanzar | Los busca tu IA con el token. |
| **Utmify** (recomendado) | Ventas reales por campaña y por hora | Utmify → Integraciones → MCP (IA). Copiá el link: el token es lo que va después de `token=`. El ID del dashboard está en la dirección del dashboard: `app.utmify.com.br/dashboards/<ID>`. Utmify deja **una sola** integración MCP por cuenta. |
| **Telegram o WhatsApp** | Recibir los avisos | Sección 7. |
| **Servidor** (recomendado) | Que el bot corra 24 h con tu compu apagada | DigitalOcean, US$6/mes. Sección 6. |
| **Python 3.9 o más** | Correr los scripts en tu compu | En Mac ya viene. Probá `python3 --version`. |

Todas las claves van en el archivo `~/pujas-search-scale/.env`, una por línea:

```
PUJAS_META_TOKEN=EAAB...
PUJAS_UTMIFY_TOKEN=...
PUJAS_TELEGRAM_TOKEN=...
PUJAS_TELEGRAM_CHAT=...
PUJAS_WHAPI_TOKEN=...
PUJAS_WHATSAPP_DESTINO=5491112345678
PUJAS_WEBHOOK_CLAVE=una-clave-larga-inventada
```

Las que no uses, no las pongas.

---

## 6. Instalación en el servidor

### 6.1 Crear el servidor
1. Entrá a DigitalOcean → Create → Droplets.
2. Ubuntu 24.04, plan Basic, Regular, **US$6/mes**. Región: Nueva York.
3. Autenticación: **SSH Key**. Tu IA te genera una con `ssh-keygen -t ed25519 -f ~/.ssh/pujas -N ""` y te pasa el contenido de `~/.ssh/pujas.pub` para pegar ahí.
4. Create. Anotá la IP.

### 6.2 Subir el bot
Tu IA corre, desde tu compu:

```
ssh -i ~/.ssh/pujas root@<IP> "mkdir -p /opt/pujas"
scp -i ~/.ssh/pujas ~/pujas-search-scale/*.py ~/pujas-search-scale/*.json ~/pujas-search-scale/.env ~/pujas-search-scale/instalar_servidor.sh root@<IP>:/opt/pujas/
ssh -i ~/.ssh/pujas root@<IP> "bash /opt/pujas/instalar_servidor.sh"
```

El instalador deja el bot programado a los :00 y :30 y corre un simulacro. Si en `.env` está `PUJAS_WEBHOOK_CLAVE`, también instala el receptor de ventas y te imprime la URL para tu plataforma (sección 8).

### 6.3 Cambios después
Siempre en la copia local y después `scp` del archivo al servidor. Para mirar lo que hizo el bot:

```
ssh -i ~/.ssh/pujas root@<IP> "tail -50 /opt/pujas/log/$(date +%F).log"
```

### 6.4 Sin servidor (en tu Mac)
Funciona igual, pero la Mac tiene que quedar prendida y sin suspenderse. Tu IA agrega con `crontab -e`:

```
0,30 * * * * cd ~/pujas-search-scale && /usr/bin/python3 pujas.py >> log/cron.out 2>&1
```

---

## 7. Avisos por Telegram y WhatsApp

### Telegram (gratis, 3 minutos)
1. En Telegram buscá **@BotFather** → `/newbot` → ponele nombre. Te da un token: va en `PUJAS_TELEGRAM_TOKEN`.
2. Mandale cualquier mensaje a tu bot nuevo.
3. Tu IA abre `https://api.telegram.org/bot<TOKEN>/getUpdates` y saca el número de `chat.id`: va en `PUJAS_TELEGRAM_CHAT`.

### WhatsApp (Whapi)
1. Creá una cuenta en **whapi.cloud** y un canal.
2. Escaneá el QR con un **número secundario** (el que va a mandar los avisos; no uses tu número personal).
3. Copiá el token del canal: va en `PUJAS_WHAPI_TOKEN`.
4. En `PUJAS_WHATSAPP_DESTINO` va tu número personal con código de país, sin `+` ni espacios (Argentina: `549` + área + número).

Probá con `python3 comun.py --probar-avisos`. Te llegan:
- 💧 cuando una campaña empieza a gastar y su precio queda en prueba.
- ✅ cuando un precio se valida con ventas.
- Cada suba y baja de puja con su motivo.
- 🛑 cuando el freno pausa una campaña.
- ⏳ si los anuncios siguen en revisión.
- 📊 el parte de cada hora y ☀️ el resumen de las 08:00.

---

## 8. Ventas al instante (opcional, recomendado)

Utmify recibe cada venta recién cuando el cliente termina o abandona el post-compra, unos 20 minutos después. El receptor del kit toma el webhook de tu plataforma en el momento y el bot usa el mayor entre las dos fuentes.

1. En `.env` agregá `PUJAS_WEBHOOK_CLAVE=` con una clave larga inventada.
2. Corré de nuevo `instalar_servidor.sh`: instala el receptor con HTTPS (Caddy y una dirección `sslip.io` gratis) y te imprime la URL.
3. Pegá esa URL en tu plataforma como webhook del evento **venta aprobada**. En Impultienda: Configuraciones → Webhooks (eventos `order.approved`, `order.refunded`, `order.chargeback`).

El receptor lee el ID de campaña de las UTMs (`utm_id` o el formato `nombre|id` de Utmify), suma los upsells a la campaña de la compra original y pasa todo a dólares con la cotización del día. Para que funcione, tus anuncios tienen que llevar las UTMs del kit (las campañas que crea `crear.py` ya las llevan).

---

## 9. Operación diaria

- **Mirá el parte, no el Administrador de anuncios.** El bot ya está mirando cada 30 minutos.
- **No toques la puja a mano** de una campaña que maneja el bot. Si querés moverla, decile a tu IA y que lo haga en el estado del bot.
- **Para pausar el bot entero:** creá un archivo llamado `FRENADO` en la carpeta del bot (en el servidor). Para reanudar, borralo. El bot también se frena solo si el token deja de andar, y te avisa.
- **Para sacar una campaña del bot:** pausala en Meta (el bot no toca lo que está pausado a mano) o poné `"activo": false` en su bloque de `config.json`.
- **Renovaciones:** cuando tengas ganadores nuevos, corré `winners.py` y agregalos como anuncios nuevos al mismo conjunto. No hace falta campaña nueva.
- **Juzgá a los 3 días**, no a las 3 horas. Si después de 3 días una de las dos campañas pierde, pausala y quedate con la que gana.

---

## 10. Problemas comunes

| Síntoma | Causa | Qué hacer |
|---|---|---|
| "Meta error 190" y el bot frenado | El token venció o lo revocaron | Generá otro token de usuario del sistema, ponelo en `.env` del servidor y borrá el archivo `FRENADO`. |
| La campaña no gasta nada | La puja está baja para tu mercado | Es normal la primera hora: la escalera sube sola. Si llega al tope y sigue sin gastar, te avisa con 🛑. |
| "los anuncios siguen en revisión" | Meta todavía no aprobó | El bot espera. Si en 24 h no se aprueban, revisá si fueron rechazados. |
| Utmify no responde | Caída de Utmify o token mal copiado | Con el webhook instalado el bot sigue igual. Sin webhook, no sube pujas hasta que vuelva. |
| No llegan los avisos | Token o número mal cargado | `python3 comun.py --probar-avisos` te dice cuál falló. |
| WhatsApp da 403 | El canal de Whapi se desconectó | Volvé a escanear el QR en whapi.cloud. |
| La puja se mueve sola sin aviso | Corren dos bots a la vez | Dejá uno solo: el del servidor. |

---

## 11. Control final

1. La skill está guardada en `~/.claude/skills/pujas-search-scale/SKILL.md`.
2. Los archivos del kit están en `~/pujas-search-scale/` y pasan el chequeo de sintaxis.
3. El `.env` tiene el token de Meta y no está en ninguna carpeta que se sincronice.
4. `analizar.py` mostró los picos y la hora de arranque quedó guardada.
5. `winners.py` encontró al menos 5 ganadores con 2 CPA de gasto o más.
6. La Cost Cap y la Bid Cap están en dos cuentas donde la oferta no corría.
7. Llegó el mensaje de prueba por Telegram o WhatsApp.
8. El bot está programado en el servidor y el simulacro corrió sin errores.
9. El alumno confirmó y las campañas están prendidas.
10. Pasada la primera hora en punto, llegó el primer parte 📊.

---

## 12. Archivos del kit

Tu IA los copia tal cual en `~/pujas-search-scale/`. No hace falta que los leas.

### comun.py

```python
"""Pujas Search Scale · Launch Expert — funciones compartidas (Meta, Utmify, avisos, secretos).
Los secretos se leen de las variables de entorno o del archivo .env de esta carpeta (nunca del config.json)."""
import json, os, sys, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

AQUI = os.path.dirname(os.path.abspath(__file__))
G = "https://graph.facebook.com/v21.0"
UA = "pujas-search-scale/1.0"   # Utmify y Whapi responden 403 sin un User-Agent propio
UTMIFY_URL = "https://mcp.utmify.com.br/mcp/"
# Códigos de Meta que NO se reintentan: permisos/token (10, 190, 200-299) y límites (4, 17, 32, 613, 80000-80014)
FRENAR = {4, 10, 17, 32, 190, 613} | set(range(200, 300)) | set(range(80000, 80015))
# UTMs con el formato que lee Utmify (nombre|id) + utm_id = ID de campaña (lo usa el receptor de ventas)
URL_TAGS = ("utm_source=FB&utm_campaign={{campaign.name}}|{{campaign.id}}&utm_medium={{adset.name}}|{{adset.id}}"
            "&utm_content={{ad.name}}|{{ad.id}}&utm_term={{placement}}&utm_id={{campaign.id}}")
# Sin "mejoras creativas" de Advantage+: el winner sale tal cual se validó
FEATURES = ["text_optimizations", "image_touchups", "video_auto_crop", "image_brightness_and_contrast", "enhance_cta",
            "image_templates", "media_type_automation", "adapt_to_placement", "profile_card", "site_extensions"]
DOF = {"creative_features_spec": {f: {"enroll_status": "OPT_OUT"} for f in FEATURES}}
ATTR = [{"event_type": "CLICK_THROUGH", "window_days": 7}, {"event_type": "VIEW_THROUGH", "window_days": 1}]


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


def offset(dia, zona):
    """'-03:00' para un día en un huso (para los rangos de fecha de Utmify)."""
    o = datetime.strptime(dia, "%Y-%m-%d").replace(hour=12, tzinfo=zona).strftime("%z")
    return f"{o[:3]}:{o[3:]}"


def hm(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)


# ---------- Meta Graph API ----------
def graph(path, data=None):
    tok = secreto("PUJAS_META_TOKEN")
    url = f"{G}/{path}"
    if data is None:
        req = urllib.request.Request(f"{url}{'&' if '?' in url else '?'}access_token={tok}")
    else:
        body = {k: (json.dumps(v) if isinstance(v, (dict, list)) else v) for k, v in data.items()}
        body["access_token"] = tok
        req = urllib.request.Request(url, data=urllib.parse.urlencode(body).encode())
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


def graph_todo(path, tope=5000):
    """GET paginado: junta todas las páginas de 'data'."""
    out, url = [], path
    while url and len(out) < tope:
        r = graph(url)
        out += r.get("data", [])
        nxt = r.get("paging", {}).get("next")
        if nxt:  # la URL siguiente trae el token: se lo saco y graph() lo vuelve a poner
            u = urllib.parse.urlsplit(nxt)
            q = [(k, v) for k, v in urllib.parse.parse_qsl(u.query) if k != "access_token"]
            url = u.path.split("/", 2)[2] + "?" + urllib.parse.urlencode(q)
        else:
            url = None
    return out


def accion(lista, tipo="offsite_conversion.fb_pixel_purchase"):
    for a in lista or []:
        if a.get("action_type") == tipo:
            return float(a["value"])
    return 0.0


# ---------- Utmify (su MCP por HTTP, JSON-RPC) ----------
def utmify(tool, args):
    """Llama una herramienta del MCP de Utmify. Devuelve el JSON del resultado o lanza RuntimeError."""
    tok = secreto("PUJAS_UTMIFY_TOKEN")
    base = f"{UTMIFY_URL}?token={tok}&resources=gs,gm,gg,gk,gt,gtb,gu,gwe,ga,gp,gwa,gr,gtf,gpc,gcs"
    hdr = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream", "User-Agent": UA}

    def post(body, sid=None):
        h = dict(hdr, **({"Mcp-Session-Id": sid} if sid else {}))
        resp = urllib.request.urlopen(urllib.request.Request(base, data=json.dumps(body).encode(), headers=h), timeout=120)
        raw = resp.read().decode()
        sid = resp.headers.get("Mcp-Session-Id") or sid
        if raw.lstrip().startswith("{"):
            return json.loads(raw), sid
        datos = [l[5:].strip() for l in raw.splitlines() if l.startswith("data:")]
        return (json.loads(datos[-1]) if datos else {}), sid

    _, sid = post({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
        "protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "pujas", "version": "1"}}})
    post({"jsonrpc": "2.0", "method": "notifications/initialized"}, sid)
    r, _ = post({"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": tool, "arguments": args}}, sid)
    if "result" not in r:
        raise RuntimeError(str(r)[:300])
    texto = r["result"]["content"][0]["text"]
    if r["result"].get("isError"):
        raise RuntimeError(texto[:300])
    return json.loads(texto)


# ---------- Avisos: Telegram y/o WhatsApp (Whapi) ----------
def avisar_externo(texto):
    """Manda el texto a Telegram y a WhatsApp si están configurados. Devuelve la lista de errores."""
    errores = []
    tg_tok, tg_chat = secreto("PUJAS_TELEGRAM_TOKEN", False), secreto("PUJAS_TELEGRAM_CHAT", False)
    if tg_tok and tg_chat:
        try:
            data = urllib.parse.urlencode({"chat_id": tg_chat, "text": texto[:4000]}).encode()
            urllib.request.urlopen(f"https://api.telegram.org/bot{tg_tok}/sendMessage", data=data, timeout=20)
        except Exception as e:
            errores.append(f"Telegram: {e}")
    wa_tok, wa_to = secreto("PUJAS_WHAPI_TOKEN", False), secreto("PUJAS_WHATSAPP_DESTINO", False)
    if wa_tok and wa_to:
        try:
            req = urllib.request.Request("https://gate.whapi.cloud/messages/text", method="POST",
                                         data=json.dumps({"to": wa_to, "body": f"🚀 Pujas\n{texto}"}).encode(),
                                         headers={"Authorization": f"Bearer {wa_tok}", "Content-Type": "application/json", "User-Agent": UA})
            urllib.request.urlopen(req, timeout=20)
        except Exception as e:
            errores.append(f"WhatsApp: {e}")
    return errores


if __name__ == "__main__" and "--probar-avisos" in sys.argv:
    errs = avisar_externo("✅ Pujas Search Scale conectado. Desde ahora te aviso cada cambio de puja y te mando el parte de cada hora.")
    print("Errores:", errs or "ninguno")
```

### pujas.py

```python
"""Pujas Search Scale · Launch Expert — el bot de pujas en escalera para campañas Cost Cap y Bid Cap.
Corre cada 30 minutos (cron). Reglas en config.json.
Uso:  python3 pujas.py                          -> corrida real
      python3 pujas.py --simulacro              -> lee todo, no cambia nada, no manda avisos
      python3 pujas.py --simulacro --hora 09:30 -> simula la corrida de esa hora con los datos de hoy
Cómo trabaja (cada conjunto, todos los días):
  02:00 reinicio      -> puja y presupuesto vuelven al original (y reactiva lo que frenó)
  hasta hora_ventas   -> no toca nada (de madrugada no hay tráfico para medir precio)
  hora_ventas         -> arranca la escalera: si no gasta, sube un escalón cada media hora
  gasta               -> el precio queda EN PRUEBA (puja quieta)
  gastó 2 CPA         -> si vendió con ROAS >= 1,2: precio VALIDADO (recién ahí abre la canilla: +½ escalón y boost)
                         si no: baja un escalón y ese precio queda de techo hasta el reinicio
  pierde 3 CPA en el día con ROAS < 0,8 -> FRENO: pausa el conjunto hasta el reinicio
"""
import json, os, sys, time
from datetime import datetime, timedelta

from comun import AQUI, Frenar, accion, avisar_externo, cfg, graph, hm, offset, secreto, tz, utmify

CFG = cfg()
TZ = tz()
FRENO = os.path.join(AQUI, "FRENADO")
SIM = "--simulacro" in sys.argv
MENSAJES = []


def ahora():
    if "--hora" in sys.argv:
        h, m = sys.argv[sys.argv.index("--hora") + 1].split(":")
        return datetime.now(TZ).replace(hour=int(h), minute=int(m), second=0, microsecond=0)
    return datetime.now(TZ)


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
            log(f"  aviso falló: {e}")


# ---------- Ventas: Utmify, webhook propio y, si no hay nada, el pixel ----------
def utmify_ventas(conjuntos, dia):
    """{adset_id: (aprobadas, facturado_usd)} de HOY según Utmify, o None. Utmify recibe la venta ~20 min tarde."""
    if not CFG.get("utmify_dashboard") or not secreto("PUJAS_UTMIFY_TOKEN", False):
        return None
    try:
        o = offset(dia, TZ)
        r = utmify("get_meta_ad_objects", {"dashboardId": CFG["utmify_dashboard"], "level": "adset",
                                           "adsetIds": [c["conjunto"] for c in conjuntos],
                                           "dateRange": {"from": f"{dia}T00:00:00{o}", "to": f"{dia}T23:59:59{o}"}})
        return {x["id"]: (x["approvedOrdersCount"], x["revenue"] / 100) for x in r["results"]}
    except Exception as e:
        log(f"Utmify no respondió: {e}")
        return None


def webhook_ventas(conjuntos, dia):
    """{adset_id: (ventas, usd)} de HOY según el receptor de webhooks (ventas al instante), o None si no está instalado."""
    p = os.path.join(AQUI, "ventas", f"{dia}.json")
    if not secreto("PUJAS_WEBHOOK_CLAVE", False):
        return None
    if not os.path.exists(p):
        # sin ninguna venta recibida hoy no sé si el webhook anda: no lo uso (si no, leería 0 y frenaría campañas sanas)
        return None
    try:
        camp = json.load(open(p)).get("campanas", {})
        return {c["conjunto"]: (camp.get(c["campana"], {}).get("ventas", 0), camp.get(c["campana"], {}).get("usd", 0.0)) for c in conjuntos}
    except Exception as e:
        log(f"No pude leer las ventas del webhook: {e}")
        return None


def juntar(*fuentes):
    """Por conjunto, el mayor entre las fuentes (Utmify llega tarde; un webhook puede perder alguna)."""
    fuentes = [f for f in fuentes if f is not None]
    if not fuentes:
        return None
    ids = set().union(*[f.keys() for f in fuentes])
    return {i: (max(f.get(i, (0, 0.0))[0] for f in fuentes), max(f.get(i, (0, 0.0))[1] for f in fuentes)) for i in ids}


def frenados(nuevo=None):
    """Conjuntos que pausó el freno de mano (sobreviven al cambio de día, hasta el reinicio)."""
    p = os.path.join(AQUI, "estado", "frenados.json")
    if nuevo is None:
        return json.load(open(p)) if os.path.exists(p) else {}
    if not SIM:
        json.dump(nuevo, open(p, "w"), indent=1, ensure_ascii=False)


# ---------- Estado por día ----------
def ruta_estado(dia):
    os.makedirs(os.path.join(AQUI, "estado"), exist_ok=True)
    return os.path.join(AQUI, "estado", f"{'simulacro-' if SIM else ''}{dia}.json")


def cargar(dia):
    p = ruta_estado(dia)
    if os.path.exists(p):
        return json.load(open(p))
    real = os.path.join(AQUI, "estado", f"{dia}.json")
    if SIM and os.path.exists(real):
        return json.load(open(real))
    return {"dia": dia, "conjuntos": {}, "resumen_enviado": False}


def guardar(st):
    json.dump(st, open(ruta_estado(st["dia"]), "w"), indent=1, ensure_ascii=False)


# ---------- Cambios con verificación ----------
def aplicar(c, s, campo, valor_cent, motivo):
    """Cambia la puja (bid_amount del conjunto) o el presupuesto (daily_budget de la campaña) y verifica que siga activo."""
    obj = c["conjunto"] if campo == "bid_amount" else c["campana"]
    ant = s["puja_cent"] if campo == "bid_amount" else s["presupuesto_cent"]
    etiqueta = "puja" if campo == "bid_amount" else "presupuesto"
    s["cambios"].append({"hora": ahora().strftime("%H:%M"), "campo": etiqueta, "de": ant / 100, "a": valor_cent / 100, "motivo": motivo})
    if campo == "bid_amount":
        s["puja_cent"] = valor_cent
    else:
        s["presupuesto_cent"] = valor_cent
    avisar(f"{'[SIMULACRO] ' if SIM else ''}{c['nombre']}: {etiqueta} US${ant/100:.2f} → US${valor_cent/100:.2f} ({motivo})")
    if SIM:
        return
    graph(obj, {campo: valor_cent})
    x = {}
    for _ in range(12):
        time.sleep(5)
        x = graph(f"{c['conjunto']}?fields=status,effective_status,bid_amount")
        if x["effective_status"] == "ACTIVE":
            return
        if x["status"] == "PAUSED":
            graph(c["conjunto"], {"status": "ACTIVE"})
            avisar(f"⚠️ {c['nombre']}: el conjunto quedó PAUSADO después del cambio de {etiqueta}. Lo reactivé.")
    avisar(f"⚠️ {c['nombre']}: después del cambio de {etiqueta} el conjunto sigue en '{x.get('effective_status')}'. Revisalo.")


# ---------- Lógica ----------
def evaluar(c, s, d, ventas_ok, t):
    R = CFG["reglas"]
    reinicio = CFG.get("hora_reinicio", "02:00")
    ticket = c["ticket"] * (1 - c.get("comision_pct", 0))
    paso = round(ticket * R["escalon_pct"] * (0.5 if c.get("mercado_chico") else 1) * 100)
    medio = max(1, paso // 2)
    minimo = round(ticket * R["puja_min_pct"] * 100)
    maximo = min(round(ticket * R["puja_max_pct"] * 100), round(c["cpa_objetivo"] * 100))
    if c.get("puja_max"):  # tope propio (las Bid Cap arrancan por encima del 70 % del ticket)
        maximo = round(c["puja_max"] * 100)
    if s.get("techo"):  # precio que ya perdió plata hoy: no se vuelve a pagar hasta el reinicio
        maximo = min(maximo, round(s["techo"] * 100))
    original = round(c["puja_original"] * 100)
    clamp = lambda v: max(minimo, min(maximo, v))
    minuto = t.hour * 60 + t.minute
    puede_subir = minuto < hm(CFG.get("hora_sin_subas", "23:59")) and ventas_ok
    puja = s["puja_cent"]
    escalones_abajo = c.get("escalones_abajo", R["arranque_escalones_abajo"])

    # gasto de la última media hora (diferencia con la corrida anterior)
    g30 = None
    if s["corridas"]:
        prev = s["corridas"][-1]
        dt = (t - datetime.fromisoformat(prev["t"])).total_seconds() / 60
        if 20 <= dt <= 45:
            g30 = d["gasto"] - prev["gasto"]
    s["corridas"].append({"t": t.isoformat(), "gasto": d["gasto"], "compras_meta": d["compras_meta"],
                          "aprobadas": d["aprobadas"], "facturado": d["facturado"], "puja": puja / 100, "g30": g30})
    esperado = puja * R["gasto_esperado_30min_x_puja"] / 100
    roas = d["facturado"] / d["gasto"] if d["gasto"] else None
    compras = d["aprobadas"] if d["aprobadas"] is not None else d["compras_meta"]
    cpa = d["gasto"] / compras if compras else None

    # Reinicio (después de los picos de la noche): todo vuelve al original
    ini = hm(reinicio)
    if ini <= minuto < ini + 60:
        if puja != original:
            aplicar(c, s, "bid_amount", original, f"{reinicio}: vuelve a la puja original")
        if s["presupuesto_cent"] != round(c["presupuesto_original"] * 100):
            aplicar(c, s, "daily_budget", round(c["presupuesto_original"] * 100), f"{reinicio}: vuelve al presupuesto original")
        return

    # Madrugada: hasta la hora de ventas no se toca
    if s["fase"] == "sin_iniciar" and minuto < hm(c["hora_ventas"]):
        return

    # Freno de mano: si en el día pierde mucho, PAUSA el conjunto hasta el reinicio
    # (bajar el presupuesto no alcanza: Meta gasta por encima del diario cuando se lo bajás en el día)
    perdida = d["gasto"] - d["facturado"]
    if (ventas_ok and d["aprobadas"] is not None and roas is not None and roas < R["freno_roas_menor_a"]
            and perdida >= R["freno_perdida_x_cpa_obj"] * c["cpa_objetivo"]):
        s["freno"] = t.strftime("%H:%M")
        avisar(f"{'[SIMULACRO] ' if SIM else ''}🛑 FRENO {c['nombre']}: pierde US${perdida:.0f} en el día (ROAS {roas:.2f}). "
               f"Pauso el conjunto; lo reactivo a las {reinicio} con la puja y el presupuesto originales.")
        if not SIM:
            graph(c["conjunto"], {"status": "PAUSED"})
            fr = frenados(); fr[c["conjunto"]] = {"nombre": c["nombre"], "desde": t.isoformat()}; frenados(fr)
        return

    # Hora de ventas: arranca la escalera
    if s["fase"] == "sin_iniciar":
        ayer = s.get("precio_ayer")
        base_txt = f"precio validado ayer US${ayer:.2f}" if ayer else "puja original"
        inicio = (round(ayer * 100) if ayer else original) - escalones_abajo * paso
        inicio = clamp(max(inicio, round(ticket * R["arranque_pct"] * 100)))
        s["fase"] = "escalera"
        s["puja_arranque"] = inicio / 100
        s["inicio_escalera"] = t.isoformat()
        s["escalones"] = [{"hora": t.strftime("%H:%M"), "puja": inicio / 100, "g30": None}]
        if inicio != puja:
            aplicar(c, s, "bid_amount", inicio, f"{c['hora_ventas']}: arranca la escalera ({escalones_abajo} escalones debajo del {base_txt})")
        return

    # Escalera: buscando un precio que gaste
    if s["fase"] == "escalera":
        if g30 is None:
            log(f"{c['nombre']}: sin gasto de media hora comparable todavía")
        elif g30 >= esperado:
            # gastar no alcanza: el precio queda en prueba y se valida recién si además vende
            prev = s["corridas"][-2] if len(s["corridas"]) > 1 else {}
            s["fase"] = "probando"
            s["prueba"] = {"puja": puja / 100, "hora": t.strftime("%H:%M"), "g30": round(g30, 2), "gasto": d["gasto"] - g30,
                           "compras": prev.get("aprobadas") if prev.get("aprobadas") is not None else (compras or 0),
                           "facturado": prev.get("facturado") or 0.0}
            avisar(f"💧 {c['nombre']}: gasta a US${puja/100:.2f} ({t:%H:%M}, US${g30:.2f} en la media hora). Lo dejo quieto y lo valido "
                   f"si vende con ROAS ≥ {R['valida_roas_min']} en los próximos {R['prueba_gasto_x_cpa_obj']} CPA de gasto.")
        elif puede_subir:
            if puja < maximo:
                nueva = clamp(puja + paso)
                s["escalones"].append({"hora": t.strftime("%H:%M"), "puja": nueva / 100, "g30": round(g30, 2)})
                aplicar(c, s, "bid_amount", nueva, f"escalón: gastó US${g30:.2f} < US${esperado:.2f} esperado")
            elif not s.get("aviso_tope"):
                s["aviso_tope"] = True
                avisar(f"🛑 {c['nombre']}: llegó al tope (US${maximo/100:.2f}) y sigue sin gastar.")
        ini_e = datetime.fromisoformat(s.get("inicio_escalera") or t.isoformat())
        if s["fase"] == "escalera" and (t - ini_e).total_seconds() >= 7200 and not s.get("aviso_franja"):
            s["aviso_franja"] = True
            avisar(f"🚨 {c['nombre']}: lleva 2 h de escalera y no encontró precio (puja US${s['puja_cent']/100:.2f}).")
        if not ventas_ok and not s.get("aviso_ventas"):
            s["aviso_ventas"] = True
            avisar("⚠️ No tengo datos de ventas (Utmify, webhook ni pixel): no subo pujas hasta que vuelvan.")
        presupuesto(c, s, d, roas, compras, cpa)
        return

    # Prueba: el precio gasta; se valida solo si vende. Si no vende, baja y ese precio es el techo del día
    if s["fase"] == "probando":
        pr = s["prueba"]
        gd = d["gasto"] - pr["gasto"]
        cd = (compras or 0) - pr["compras"]
        rd = (d["facturado"] - pr["facturado"]) / gd if gd else None
        if not ventas_ok:
            log(f"{c['nombre']}: en prueba a US${puja/100:.2f}, sin datos de ventas; espero")
        elif gd >= R["prueba_gasto_x_cpa_obj"] * c["cpa_objetivo"]:
            if cd > 0 and rd is not None and rd >= R["valida_roas_min"]:
                s["fase"] = "encontrado"
                s["precio_encontrado"] = {"puja": puja / 100, "hora": t.strftime("%H:%M"), "roas_prueba": round(rd, 2)}
                s["base_hallazgo"] = {"gasto": d["gasto"], "compras": compras or 0}
                s["frenadas"] = 0
                avisar(f"✅ {c['nombre']}: precio VALIDADO a US${puja/100:.2f}: gastó US${gd:.2f} y vendió {cd} (ROAS {rd:.2f}). Desde acá puede abrir la canilla.")
            else:
                # nunca por debajo del precio que ganó ayer
                s["techo"] = max((puja - medio) / 100, s.get("precio_ayer") or 0)
                maximo = min(maximo, round(s["techo"] * 100))
                nueva = clamp(puja - paso)
                s.setdefault("precios_descartados", []).append(dict(pr, roas=round(rd or 0, 2), ventas=cd))
                s["fase"] = "escalera"; s["aviso_tope"] = False
                s["escalones"].append({"hora": t.strftime("%H:%M"), "puja": nueva / 100, "g30": round(g30 or 0, 2)})
                aplicar(c, s, "bid_amount", nueva, f"−1 escalón: a US${puja/100:.2f} gastó US${gd:.2f} y vendió {cd} "
                        f"(ROAS {rd or 0:.2f}); techo del día US${s['techo']:.2f}")
        presupuesto(c, s, d, roas, compras, cpa)
        return

    # Precio validado: solo medios escalones, boost si vende muy bien
    base = s["base_hallazgo"]
    gasto_desde = d["gasto"] - base["gasto"]
    compras_desde = (compras or 0) - base["compras"]
    suficiente = d["gasto"] >= R["gasto_suficiente_x_cpa_obj"] * c["cpa_objetivo"]
    hecho = False
    # 1) bajas
    if compras_desde == 0 and gasto_desde >= R["baja_sin_compras_x_puja"] * puja / 100:
        aplicar(c, s, "bid_amount", clamp(puja - medio), f"−½ escalón: 0 compras con US${gasto_desde:.2f} gastados")
        s["base_hallazgo"] = {"gasto": d["gasto"], "compras": compras or 0}
        hecho = True
    elif ventas_ok and suficiente and cpa and roas is not None and cpa > R["baja_cpa_x_puja"] * puja / 100 and roas < R["valida_roas_min"]:
        s["techo"] = max(min(s.get("techo") or 1e9, (puja - medio) / 100), s.get("precio_ayer") or 0)
        aplicar(c, s, "bid_amount", clamp(puja - medio), f"−½ escalón: CPA US${cpa:.2f} y ROAS {roas:.2f} (techo US${s['techo']:.2f})")
        hecho = True
    # 2) freno del boost
    elif ventas_ok and s.get("boosts") and roas is not None and roas < R["boost_freno_roas_menor_a"] and puja > original:
        nueva = max(original, round(puja * (1 - R["boost_freno_pct"])))
        aplicar(c, s, "bid_amount", nueva, f"−15 %: ROAS {roas:.2f} bajo {R['boost_freno_roas_menor_a']}")
        hecho = True
    # 3) boost: abre la canilla
    elif (puede_subir and roas is not None and roas >= R["boost_roas_min"] and (compras or 0) >= R["boost_compras_min"]
          and d["gasto"] < R["boost_gasto_max_pct_presupuesto"] * s["presupuesto_cent"] / 100
          and (not s.get("ultimo_boost") or (t - datetime.fromisoformat(s["ultimo_boost"])).total_seconds() >= 3600)):
        nueva = clamp(round(puja * (1 + R["boost_pct"])))
        if nueva > puja:
            s["ultimo_boost"] = t.isoformat(); s["boosts"] = s.get("boosts", 0) + 1
            aplicar(c, s, "bid_amount", nueva, f"+20 %: ROAS {roas:.2f} con {compras} compras")
            hecho = True
    # 4) se apagó: dos medias horas gastando menos de 1/4 de lo esperado -> vuelve a la escalera (+1 escalón)
    if not hecho and g30 is not None:
        s["apagadas"] = s.get("apagadas", 0) + 1 if g30 < esperado * 0.25 else 0
        if s["apagadas"] >= 2 and puede_subir and puja < maximo:
            s.setdefault("precios_descartados", []).append(s.pop("precio_encontrado", {}))
            s["fase"] = "escalera"; s["apagadas"] = 0; s["aviso_tope"] = False
            nueva = clamp(puja + paso)
            s["escalones"].append({"hora": t.strftime("%H:%M"), "puja": nueva / 100, "g30": round(g30, 2)})
            aplicar(c, s, "bid_amount", nueva, f"se apagó a US${puja/100:.2f} (US${g30:.2f} en la media hora): vuelve a la escalera")
            hecho = True
    # 5) se frena dos medias horas seguidas sin empeorar -> +½ escalón
    if not hecho and g30 is not None:
        s["frenadas"] = s.get("frenadas", 0) + 1 if g30 < esperado else 0
        sin_empeorar = cpa is None or cpa <= c["cpa_objetivo"]
        if s["frenadas"] >= 2 and puede_subir and sin_empeorar and puja < maximo:
            aplicar(c, s, "bid_amount", clamp(puja + medio), "+½ escalón: se frenó dos medias horas sin empeorar")
            s["frenadas"] = 0
    presupuesto(c, s, d, roas, compras, cpa)


def presupuesto(c, s, d, roas, compras, cpa):
    """Recorte suave del presupuesto si el día viene mal (el corte duro es el freno de mano)."""
    R = CFG["reglas"]
    if roas is None or d["gasto"] < R["gasto_suficiente_x_cpa_obj"] * c["cpa_objetivo"] or d["aprobadas"] is None:
        return
    if (compras or 0) >= 3 and cpa and cpa <= c["cpa_objetivo"]:
        return
    orig, piso = c["presupuesto_original"] * 100, c.get("presupuesto_piso", 300) * 100
    if roas < R["presupuesto_recorte_50_roas_menor_a"]:
        nuevo, nivel = max(piso, round(orig * 0.5)), 50
    elif roas < R["presupuesto_recorte_30_roas_menor_a"]:
        nuevo, nivel = max(piso, round(orig * 0.7)), 30
    else:
        return
    if nuevo < s["presupuesto_cent"]:
        aplicar(c, s, "daily_budget", int(nuevo), f"−{nivel} %: ROAS del día {roas:.2f} con US${d['gasto']:.0f} gastados")


def resumen(dia, ayer):
    """Resumen de la mañana: cómo cerró ayer cada conjunto y a qué precio arrancó hoy."""
    def leer(x):
        p = os.path.join(AQUI, "estado", f"{x}.json")
        return json.load(open(p))["conjuntos"] if os.path.exists(p) else {}
    hoy, prev = leer(dia), leer(ayer)
    lineas = [f"☀️ Resumen {dia}"]
    for nombre in sorted(hoy.keys() | prev.keys()):
        s = hoy.get(nombre, {})
        up = (prev.get(nombre, {}).get("corridas") or [{}])[-1]
        pe = prev.get(nombre, {}).get("precio_encontrado")
        lineas.append(f"\n{nombre}\n· hoy arrancó en US${(s.get('puja_cent') or 0)/100:.2f}"
                      f"\n· precio validado ayer: {'US$%.2f' % pe['puja'] if pe else 'ninguno'}")
        if up.get("gasto"):
            lineas.append(f"· ayer cerró: gasto US${up['gasto']:.0f} · {up.get('aprobadas') or 0} ventas"
                          f" · ROAS {(up.get('facturado') or 0) / up['gasto']:.2f}")
    return "\n".join(lineas)


def main():
    if os.path.exists(FRENO) and not SIM:
        print(f"FRENADO: {open(FRENO).read()}  (borrá el archivo FRENADO para reanudar)")
        return
    t = ahora()
    dia = t.strftime("%Y-%m-%d")
    ayer = (t - timedelta(days=1)).strftime("%Y-%m-%d")
    st = cargar(dia)
    reinicio = CFG.get("hora_reinicio", "02:00")
    try:
        conjuntos = [c for c in CFG["conjuntos"] if c.get("activo", True)]
        if not st.get("resumen_enviado") and t.hour * 60 + t.minute >= hm(CFG.get("hora_resumen", "08:00")):
            avisar(resumen(dia, ayer))
            st["resumen_enviado"] = True
        v_utm = utmify_ventas(conjuntos, dia)
        v_web = webhook_ventas(conjuntos, dia)
        estado_ayer = {}
        p_ayer = os.path.join(AQUI, "estado", f"{ayer}.json")
        if os.path.exists(p_ayer):
            estado_ayer = json.load(open(p_ayer))["conjuntos"]
        datos = {}
        for c in conjuntos:
            x = graph(f"{c['conjunto']}?fields=bid_amount,status,effective_status,campaign{{daily_budget}}")
            ins = graph(f"{c['conjunto']}/insights?fields=spend,actions,action_values&date_preset=today").get("data", [])
            i0 = ins[0] if ins else {}
            datos[c["conjunto"]] = (x, float(i0.get("spend", 0)), int(accion(i0.get("actions"))),
                                    accion(i0.get("action_values")))
        # sin Utmify ni webhook, el pixel hace de fuente de ventas (compras y valor de compra de Meta)
        v_pix = {k: (v[2], v[3]) for k, v in datos.items()} if v_utm is None and v_web is None else None
        ventas = juntar(v_utm, v_web, v_pix)
        ventas_ok = ventas is not None
        parte = [f"📊 Estado {t:%H:%M}"]
        fr = frenados()
        for c in conjuntos:
            x, gasto, compras_px, _ = datos[c["conjunto"]]
            aprob, fact = ventas.get(c["conjunto"], (0, 0.0)) if ventas_ok else (None, 0.0)
            d = {"gasto": gasto, "compras_meta": compras_px, "aprobadas": aprob, "facturado": fact}
            s = st["conjuntos"].setdefault(c["nombre"], {
                "puja_original": c["puja_original"], "fase": "sin_iniciar", "cambios": [], "corridas": [],
                "precio_ayer": (estado_ayer.get(c["nombre"], {}).get("precio_encontrado") or {}).get("puja")})
            if not (SIM and "puja_cent" in s):  # en simulacro se encadena la puja simulada
                s["puja_cent"] = int(x.get("bid_amount") or round(c["puja_original"] * 100))
                s["presupuesto_cent"] = int(x.get("campaign", {}).get("daily_budget") or round(c["presupuesto_original"] * 100))
            reactivado = False
            if c["conjunto"] in fr:
                if hm(reinicio) <= t.hour * 60 + t.minute < hm(reinicio) + 60:
                    avisar(f"{'[SIMULACRO] ' if SIM else ''}▶️ {c['nombre']}: reinicio, reactivo el conjunto que había frenado.")
                    if not SIM:
                        graph(c["conjunto"], {"status": "ACTIVE"})
                        fr.pop(c["conjunto"]); frenados(fr)
                    x["effective_status"] = x["status"] = "ACTIVE"; reactivado = True
                else:
                    log(f"{c['nombre']}: frenado desde las {fr[c['conjunto']]['desde'][11:16]}; vuelve a las {reinicio}")
                    parte.append(f"\n{c['nombre']}\n· 🛑 frenado hasta las {reinicio} · gasto hoy US${gasto:.2f}")
                    continue
            if x["effective_status"] != "ACTIVE" and x["status"] == "PAUSED":
                log(f"{c['nombre']}: el conjunto está pausado a mano; no lo toco.")
                continue
            ads = graph(f"{c['conjunto']}/ads?fields=effective_status&limit=100").get("data", [])
            if not reactivado and not any(a.get("effective_status") == "ACTIVE" for a in ads):
                log(f"{c['nombre']}: ningún anuncio aprobado todavía; no toco la puja.")
                if not s.get("aviso_revision"):
                    avisar(f"⏳ {c['nombre']}: los anuncios siguen en revisión de Meta; la escalera arranca cuando se aprueben.")
                    s["aviso_revision"] = True
                continue
            log(f"{c['nombre']}: fase {s['fase']} · puja US${s['puja_cent']/100:.2f} · gasto hoy US${gasto:.2f} · ventas {aprob} "
                f"(US${fact:.2f}) [Utmify {(v_utm or {}).get(c['conjunto'])} · webhook {(v_web or {}).get(c['conjunto'])} · pixel {compras_px}]")
            evaluar(c, s, d, ventas_ok, t)
            parte.append(f"\n{c['nombre']}\n· puja US${s['puja_cent']/100:.2f} ({s['fase']}) · gasto hoy US${gasto:.2f}"
                         f"\n· {aprob} ventas US${fact:.2f} · ROAS {fact / gasto if gasto else 0:.2f}")
            guardar(st)
        # parte de cada hora en punto con todos los conjuntos (los cambios se avisan al momento)
        if t.minute < 15 and len(parte) > 1:
            avisar("\n".join(parte))
    except Frenar as e:
        avisar(f"🛑 Pujas FRENADO: {e}. No reintento. Arreglalo y borrá el archivo FRENADO para reanudar.")
        if not SIM:
            open(FRENO, "w").write(f"{datetime.now(TZ):%Y-%m-%d %H:%M} {e}")
    except Exception as e:
        avisar(f"⚠️ Pujas: error en esta corrida, salteo hasta la próxima: {e}")
    finally:
        guardar(st)
    if SIM:
        print("\n===== MENSAJES QUE MANDARÍA =====")
        print("\n---\n".join(MENSAJES) or "(ninguno)")


if __name__ == "__main__":
    main()
```

### analizar.py

```python
"""Pujas Search Scale · Launch Expert — detecta los horarios de mejor rendimiento y los picos de venta de la oferta.
Cruza el gasto por hora de Meta (campañas de la oferta) con las ventas por hora de Utmify (o, si no hay, el pixel).
Uso:  python3 analizar.py              -> imprime el mapa de 24 h, los picos y los horarios recomendados
      python3 analizar.py --dias 21    -> cambia la ventana (por defecto 14 días)
      python3 analizar.py --guardar    -> además escribe hora_ventas, hora_reinicio y los picos en config.json
"""
import json, os, sys, urllib.parse
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from comun import AQUI, accion, cfg, graph_todo, graph, offset, secreto, tz, utmify

C = cfg()
TZ = tz()
O = C["oferta"]
DIAS = int(sys.argv[sys.argv.index("--dias") + 1]) if "--dias" in sys.argv else 14
hasta = datetime.now(TZ).date() - timedelta(days=1)          # días completos, sin el de hoy
desde = hasta - timedelta(days=DIAS - 1)

gasto = [0.0] * 24; compras_px = [0.0] * 24; valor_px = [0.0] * 24
for act in O["cuentas"]:
    act = str(act).replace("act_", "")
    zona = ZoneInfo(graph(f"act_{act}?fields=timezone_name")["timezone_name"])
    # Meta reporta la hora en el huso de la cuenta: la paso al huso del config
    corr = round((datetime.now(TZ).utcoffset() - datetime.now(zona).utcoffset()).total_seconds() / 3600)
    # el filtro por nombre se hace acá: el "filtering" de Meta falla con emojis (banderas) en el nombre
    q = urllib.parse.urlencode({
        "level": "campaign", "fields": "campaign_name,spend,actions,action_values", "limit": 500,
        "breakdowns": "hourly_stats_aggregated_by_advertiser_time_zone",
        "time_range": json.dumps({"since": str(desde), "until": str(hasta)})})
    filas = [f for f in graph_todo(f"act_{act}/insights?{q}", tope=50000)
             if O["filtro_campanas"].lower() in f.get("campaign_name", "").lower()]
    for f in filas:
        h = (int(f["hourly_stats_aggregated_by_advertiser_time_zone"][:2]) + corr) % 24
        gasto[h] += float(f.get("spend", 0))
        compras_px[h] += accion(f.get("actions"))
        valor_px[h] += accion(f.get("action_values"))

ventas = None; fact = None; fuente = "pixel de Meta"
if C.get("utmify_dashboard") and O.get("productos_utmify") and secreto("PUJAS_UTMIFY_TOKEN", False):
    try:
        r = utmify("get_dashboard_summary", {"dashboardId": C["utmify_dashboard"], "productNames": O["productos_utmify"],
                                             "dateRange": {"from": f"{desde}T00:00:00{offset(str(desde), TZ)}",
                                                           "to": f"{hasta}T23:59:59{offset(str(hasta), TZ)}"}})
        ventas = [0.0] * 24
        for x in r["ordersCount"]["byHour"]:
            ventas[x["hour"]] = x["count"]
        acum = {x["hour"]: x["cents"] / 100 for x in r["hourlyCumulative"]["revenueByHourNetCumulative"]}
        fact = [acum.get(h, 0) - (acum.get(h - 1, 0) if h else 0) for h in range(24)]
        fuente = "Utmify"
    except Exception as e:
        print(f"(Utmify no respondió, uso el pixel: {e})")
if ventas is None:
    ventas, fact = compras_px, valor_px

total_v, total_g = sum(ventas), sum(gasto)
if total_v < 20:
    print(f"Ojo: solo {total_v:.0f} ventas en {DIAS} días; los picos todavía son ruido. Probá con --dias 30.")
media = total_v / 24 if total_v else 0
es_pico = [ventas[h] >= 1.3 * media and ventas[h] > 0 for h in range(24)]

# ventanas de horas pico seguidas (la noche puede cruzar la medianoche)
ventanas, vistas = [], set()
for h in range(24):
    if es_pico[h] and not es_pico[(h - 1) % 24] and h not in vistas:
        v = [h]
        while es_pico[(v[-1] + 1) % 24] and len(v) < 24:
            v.append((v[-1] + 1) % 24)
        vistas.update(v); ventanas.append(v)
if not ventanas and any(es_pico):
    ventanas = [[h for h in range(24) if es_pico[h]]]
ventanas.sort(key=lambda v: -sum(ventas[h] for h in v))

print(f"\nOferta: {O['nombre']} · {desde} → {hasta} ({DIAS} días) · ventas por hora: {fuente} · gasto: Meta\n")
print(" hora  ventas  % día   gasto US$   ROAS   ")
for h in range(24):
    roas = fact[h] / gasto[h] if gasto[h] else 0
    barra = "█" * round(30 * ventas[h] / max(ventas)) if max(ventas) else ""
    marca = "  ← pico" if es_pico[h] else ("  ← pierde" if gasto[h] > 0 and roas < 0.8 * (sum(fact) / total_g if total_g else 0) else "")
    print(f" {h:02d}h  {ventas[h]:6.0f}  {100*ventas[h]/total_v if total_v else 0:4.1f}%  {gasto[h]:9.0f}  {roas:5.2f}  {barra}{marca}")

def rango_txt(v):
    return f"{v[0]:02d}–{(v[-1] + 1) % 24:02d} h"

picos = [{"franja": rango_txt(v), "desde": v[0], "hasta": (v[-1] + 1) % 24,
          "ventas_pct": round(100 * sum(ventas[h] for h in v) / total_v, 1) if total_v else 0} for v in ventanas[:3]]
# la escalera arranca 30 min antes del primer pico del día (entre las 5 y las 14 h)
manana = [v for v in ventanas if 5 <= v[0] <= 14]
primero = min(manana or ventanas or [[9]], key=lambda v: v[0])[0]
hora_ventas = f"{(primero - 1) % 24:02d}:30"
# el reinicio va 1 h después del último pico de la noche (entre la 01 y las 05 h); si no hay pico de noche, 02:00
noche = [v for v in ventanas if v[-1] >= 19 or v[-1] <= 3]
ultimo = max([(v[-1] if v[-1] > 3 else v[-1] + 24) for v in noche], default=24)
reinicio_h = min(max((ultimo + 2) % 24, 1), 5) if noche else 2
hora_reinicio = f"{reinicio_h:02d}:00"

print("\nPicos de venta:")
for p in picos:
    print(f"  · {p['franja']}: {p['ventas_pct']}% de las ventas")
flojas = [h for h in range(24) if gasto[h] > 0.02 * total_g and fact[h] / gasto[h] < 0.8 * (sum(fact) / total_g if total_g else 0)]
if flojas:
    print("Horas que gastan y no venden (ROAS < 80 % del promedio): " + ", ".join(f"{h:02d}h" for h in flojas))
print(f"\nRecomendado: arrancar la escalera a las {hora_ventas} · reinicio a las {hora_reinicio}")

json.dump({"oferta": O["nombre"], "desde": str(desde), "hasta": str(hasta), "fuente": fuente, "ventas_por_hora": ventas,
           "gasto_por_hora": gasto, "facturado_por_hora": fact, "picos": picos, "horas_flojas": flojas,
           "hora_ventas": hora_ventas, "hora_reinicio": hora_reinicio},
          open(os.path.join(AQUI, "analisis.json"), "w"), indent=1, ensure_ascii=False)
if "--guardar" in sys.argv:
    C["oferta"].update(picos=picos, hora_ventas=hora_ventas)
    # el reinicio es uno solo para todo el bot: queda el más tardío entre las ofertas cargadas
    C["hora_reinicio"] = max(C.get("hora_reinicio", "02:00"), hora_reinicio) if C["conjuntos"] else hora_reinicio
    for c in C["conjuntos"]:
        if c.get("oferta") == O["nombre"]:
            c["hora_ventas"] = hora_ventas
    json.dump(C, open(os.path.join(AQUI, "config.json"), "w"), indent=2, ensure_ascii=False)
    print("Guardado en config.json.")
```

### winners.py

```python
"""Pujas Search Scale · Launch Expert — busca los anuncios ganadores de la oferta para meterlos en la Cost Cap / Bid Cap.
Ranking por ROAS de los últimos 7 días (Utmify si está; si no, el pixel), con gasto mínimo de 2 CPA para que no sea suerte.
De cada ganador guarda el post (object_story_id): se clona por post y conserva los likes y comentarios.
Uso:  python3 winners.py              -> top 8
      python3 winners.py --top 10 --dias 7
"""
import json, os, sys, urllib.parse
from datetime import datetime, timedelta

from comun import AQUI, accion, cfg, graph, graph_todo, offset, secreto, tz, utmify

C = cfg(); TZ = tz(); O = C["oferta"]
TOP = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 8
DIAS = int(sys.argv[sys.argv.index("--dias") + 1]) if "--dias" in sys.argv else 7
hasta = datetime.now(TZ).date()
desde = hasta - timedelta(days=DIAS - 1)
cpa_obj = O["ticket"] / 1.1
min_gasto = 2 * cpa_obj

anuncios = {}
for act in O["cuentas"]:
    act = str(act).replace("act_", "")
    q = urllib.parse.urlencode({
        "level": "ad", "fields": "ad_id,ad_name,campaign_id,campaign_name,spend,actions,action_values", "limit": 500,
        "time_range": json.dumps({"since": str(desde), "until": str(hasta)})})
    # el filtro por nombre se hace acá: el "filtering" de Meta falla con emojis (banderas) en el nombre
    for f in graph_todo(f"act_{act}/insights?{q}", tope=50000):
        if O["filtro_campanas"].lower() not in f.get("campaign_name", "").lower():
            continue
        anuncios[f["ad_id"]] = {"act": act, "nombre": f["ad_name"].strip(), "campana": f["campaign_id"], "gasto": float(f.get("spend", 0)),
                                "ventas": accion(f.get("actions")), "facturado": accion(f.get("action_values"))}

fuente = "pixel"
if C.get("utmify_dashboard") and secreto("PUJAS_UTMIFY_TOKEN", False) and anuncios:
    try:
        campanas = sorted({a["campana"] for a in anuncios.values()})
        r = utmify("get_meta_ad_objects", {"dashboardId": C["utmify_dashboard"], "level": "ad", "campaignIds": campanas,
                                           "dateRange": {"from": f"{desde}T00:00:00{offset(str(desde), TZ)}",
                                                         "to": f"{hasta}T23:59:59{offset(str(hasta), TZ)}"}})
        for x in r["results"]:
            if x["id"] in anuncios:
                anuncios[x["id"]].update(ventas=x["approvedOrdersCount"], facturado=x["revenue"] / 100)
        fuente = "Utmify"
    except Exception as e:
        print(f"(Utmify no respondió, uso el pixel: {e})")

# el mismo creativo suele estar en varias cuentas con el mismo nombre: sumo por nombre
por_nombre = {}
for ad_id, a in anuncios.items():
    p = por_nombre.setdefault(a["nombre"], {"nombre": a["nombre"], "gasto": 0, "ventas": 0, "facturado": 0, "ads": []})
    p["gasto"] += a["gasto"]; p["ventas"] += a["ventas"]; p["facturado"] += a["facturado"]
    p["ads"].append((a["gasto"], ad_id))
candidatos = [p for p in por_nombre.values() if p["gasto"] >= min_gasto and p["ventas"] >= 2]
for p in candidatos:
    p["roas"] = p["facturado"] / p["gasto"]
candidatos.sort(key=lambda p: -p["roas"])

ganadores = []
for p in candidatos:
    if len(ganadores) >= TOP:
        break
    ad_id = max(p["ads"])[1]   # el post del anuncio que más gastó (el que más prueba social juntó)
    cr = graph(f"{ad_id}?fields=effective_status,creative{{effective_object_story_id,object_story_spec}}").get("creative", {})
    post = cr.get("effective_object_story_id")
    if not post:
        print(f"  · {p['nombre']}: no tiene post clonable (anuncio de catálogo o dinámico); lo salteo")
        continue
    ganadores.append({"nombre": p["nombre"], "post": post, "roas": round(p["roas"], 2), "gasto": round(p["gasto"], 2),
                      "ventas": p["ventas"], "cpa": round(p["gasto"] / p["ventas"], 2)})

print(f"\nGanadores de {O['nombre']} · {desde} → {hasta} · ROAS por {fuente} · gasto mínimo US${min_gasto:.0f} (2 CPA)\n")
for i, g in enumerate(ganadores, 1):
    print(f" {i}. {g['nombre'][:48]:48}  ROAS {g['roas']:.2f}  gasto US${g['gasto']:.0f}  {g['ventas']:.0f} ventas  CPA US${g['cpa']:.2f}")
if ganadores:
    gt = sum(g["gasto"] for g in ganadores); vt = sum(g["ventas"] for g in ganadores)
    print(f"\nCPA real de los ganadores: US${gt / vt:.2f}  (es la referencia para el cap de la Cost Cap)")
json.dump({"desde": str(desde), "hasta": str(hasta), "fuente": fuente, "cpa_ganadores": round(gt / vt, 2) if ganadores else None,
           "ganadores": ganadores}, open(os.path.join(AQUI, "winners.json"), "w"), indent=1, ensure_ascii=False)
```

### crear.py

```python
"""Pujas Search Scale · Launch Expert — arma las campañas Cost Cap y Bid Cap con la estructura que funciona:
1 campaña CBO · 1 conjunto · los winners clonados por post · cada una en una cuenta AISLADA (donde la oferta no corre).
Lee config.json -> "lanzar" y winners.json. Es idempotente: si se corta, se vuelve a correr y sigue donde quedó.
Uso:  python3 crear.py --revisar   -> solo chequea cuentas, pixel y winners (no crea nada)
      python3 crear.py             -> crea todo EN PAUSA (no gasta)
      python3 crear.py --prender   -> prende las campañas creadas y las suma al bot
"""
import json, os, sys, time
from datetime import datetime

from comun import AQUI, ATTR, DOF, URL_TAGS, cfg, graph, tz

C = cfg(); O = C["oferta"]
P_EST = os.path.join(AQUI, "estado", "crear.json")
os.makedirs(os.path.dirname(P_EST), exist_ok=True)
est = json.load(open(P_EST)) if os.path.exists(P_EST) else {}


def guardar_est():
    tmp = P_EST + ".tmp"
    json.dump(est, open(tmp, "w"), indent=1, ensure_ascii=False)
    os.replace(tmp, P_EST)


def guardar_cfg():
    tmp = os.path.join(AQUI, "config.json.tmp")
    json.dump(C, open(tmp, "w"), indent=2, ensure_ascii=False)
    os.replace(tmp, os.path.join(AQUI, "config.json"))


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


if "--prender" in sys.argv:
    for k, e in est.items():
        if "campana" not in e:
            continue
        ads = graph(f"{e['conjunto']}/ads?fields=effective_status&limit=50").get("data", [])
        graph(e["campana"], {"status": "ACTIVE"})
        log(k, "PRENDIDA", e["campana"], f"({sum(a['effective_status'] in ('ACTIVE', 'PENDING_REVIEW', 'IN_PROCESS') for a in ads)} anuncios)")
        for c in C["conjuntos"]:
            if c["conjunto"] == e["conjunto"]:
                c["activo"] = True
    guardar_cfg()
    log("Listo: el bot las toma en la próxima corrida (:00 o :30).")
    sys.exit()

W = json.load(open(os.path.join(AQUI, "winners.json")))
if not W["ganadores"]:
    sys.exit("winners.json no tiene ganadores: corré winners.py primero.")
front, ticket = O["front"], O["ticket"]
cpa_obj = round(ticket / 1.1, 2)
fecha = datetime.now(tz()).strftime("%d-%m")

for L in C["lanzar"]:
    tipo = L["tipo"].lower().replace(" ", "")
    act = str(L["cuenta"]).replace("act_", "")
    k = f"{tipo}-{act}"
    e = est.setdefault(k, {"ads": {}})
    puja = L.get("puja") or (W["cpa_ganadores"] if tipo == "costcap" else round(front * 1.3, 2))
    nombre = f"{O['nombre']} · {'CostCap' if tipo == 'costcap' else 'BidCap'} W {fecha}"

    if "campana" not in e:
        a = graph(f"act_{act}?fields=name,account_status,disable_reason,currency,funding_source_details,business")
        if a.get("account_status") != 1:
            log(k, f"SALTEO: la cuenta {a.get('name')} no está activa (estado {a.get('account_status')}, motivo {a.get('disable_reason')})"); continue
        if not a.get("funding_source_details"):
            log(k, f"SALTEO: la cuenta {a.get('name')} no tiene medio de pago"); continue
        if a.get("currency") != "USD":
            log(k, f"OJO: la cuenta está en {a.get('currency')}; las pujas del config van en esa moneda")
        # cuenta AISLADA: la oferta no puede estar corriendo ahí (dos campañas de la misma oferta se pisan en la subasta)
        activas = graph(f"act_{act}/campaigns?fields=name&limit=200&effective_status=['ACTIVE']").get("data", [])
        pisa = [x["name"] for x in activas if O["filtro_campanas"].lower() in x["name"].lower()]
        if pisa and "--forzar" not in sys.argv:
            log(k, f"SALTEO: en {a.get('name')} ya corre la oferta ({pisa[0]}). Elegí una cuenta donde no corra."); continue
        # el pixel tiene que estar asignado a la cuenta
        px = graph(f"act_{act}/adspixels?fields=id,name&limit=100").get("data", [])
        if not any(p["id"] == str(L["pixel"]) for p in px) and "--revisar" in sys.argv:
            log(k, "el pixel no está asignado a la cuenta: al crear intento asignarlo")
        elif not any(p["id"] == str(L["pixel"]) for p in px):
            biz = L.get("business") or (a.get("business") or {}).get("id")
            r = graph(f"{L['pixel']}/shared_accounts", {"account_id": act, "business": biz}) if biz else {}
            if not r.get("success"):
                log(k, "SALTEO: el pixel no está asignado a la cuenta y no pude asignarlo. Asignalo en Configuración del negocio → Orígenes de datos."); continue
            log(k, "pixel asignado a la cuenta")
        if "--revisar" in sys.argv:
            log(k, f"OK para crear en {a.get('name')}: '{nombre}', puja US${puja:.2f}, {len(W['ganadores'])} winners")
            est.pop(k, None); continue
        c = graph(f"act_{act}/campaigns", {"name": nombre, "objective": "OUTCOME_SALES", "buying_type": "AUCTION",
                  "daily_budget": int(L.get("presupuesto", 5000) * 100), "special_ad_categories": [], "status": "PAUSED",
                  "bid_strategy": "COST_CAP" if tipo == "costcap" else "LOWEST_COST_WITH_BID_CAP"})
        e.update(campana=c["id"], nombre=nombre, cuenta=act, puja=puja); guardar_est()
        log(k, "campaña", c["id"], nombre)

    if "conjunto" not in e:
        if L.get("targeting_desde"):
            tgt = graph(f"{L['targeting_desde']}?fields=targeting")["targeting"]
        else:
            tgt = {"geo_locations": {"countries": [O["pais"]], "location_types": ["home", "recent"]},
                   "age_min": 18, "age_max": 65, "targeting_automation": {"advantage_audience": 1}}
        s = graph(f"act_{act}/adsets", {"name": f"Winners · {'Cost Cap' if tipo == 'costcap' else 'Bid Cap'} {fecha}",
                  "campaign_id": e["campana"], "targeting": tgt, "optimization_goal": "OFFSITE_CONVERSIONS",
                  "billing_event": "IMPRESSIONS", "bid_amount": int(round(puja * 100)), "attribution_spec": ATTR,
                  "promoted_object": {"pixel_id": str(L["pixel"]), "custom_event_type": "PURCHASE"}, "status": "ACTIVE"})
        e["conjunto"] = s["id"]; guardar_est()
        log(k, "conjunto", s["id"], f"puja US${puja:.2f}")

    for g in W["ganadores"]:
        if g["nombre"] in e["ads"]:
            continue
        try:
            ad = graph(f"act_{act}/ads", {"name": g["nombre"], "adset_id": e["conjunto"], "status": "ACTIVE",
                       "creative": {"object_story_id": g["post"], "url_tags": URL_TAGS, "degrees_of_freedom_spec": DOF}})
            e["ads"][g["nombre"]] = ad["id"]; guardar_est()
            log(k, "anuncio", g["nombre"], ad["id"])
        except RuntimeError as err:
            log(k, "NO SE PUDO", g["nombre"], err)
        time.sleep(5)   # ritmo humano: Meta penaliza las ráfagas

    if not any(c["conjunto"] == e["conjunto"] for c in C["conjuntos"]):
        C["conjuntos"].append({
            "nombre": f"{O['nombre']} · {'CostCap' if tipo == 'costcap' else 'BidCap'} · {act[-4:]}", "oferta": O["nombre"],
            "tipo": tipo, "cuenta": act, "campana": e["campana"], "conjunto": e["conjunto"],
            "ticket": ticket, "cpa_objetivo": cpa_obj, "puja_original": puja,
            "puja_max": round(front * 1.8, 2) if tipo == "bidcap" else None, "escalones_abajo": 0,
            "presupuesto_original": L.get("presupuesto", 5000), "presupuesto_piso": 300,
            "hora_ventas": O.get("hora_ventas", "08:30"), "activo": False})
        guardar_cfg()

if "--revisar" not in sys.argv:
    log("Creado EN PAUSA. Revisá en el Administrador de anuncios y corré:  python3 crear.py --prender")
```

### receptor.py

```python
"""Pujas Search Scale · Launch Expert — receptor de ventas al instante (opcional, recomendado).
Utmify recibe la venta recién cuando el cliente termina o abandona el post-compra (~20 min): con eso una campaña
recién prendida parece negativa aunque esté vendiendo. Este receptor toma el webhook de tu plataforma
(Impultienda: evento order.approved) en el momento y lo guarda por campaña en ventas/AAAA-MM-DD.json.
Corre en el servidor como servicio (systemd) detrás de Caddy, que le pone HTTPS gratis.
URL para pegar en la plataforma:  https://<IP-con-guiones>.sslip.io/venta?k=<PUJAS_WEBHOOK_CLAVE>
"""
import json, os, re, threading, urllib.request
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from comun import AQUI, secreto, tz

CLAVE = secreto("PUJAS_WEBHOOK_CLAVE")
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
                "https://open.er-api.com/v6/latest/USD", headers={"User-Agent": "pujas-search-scale/1.0"}), timeout=20))
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
        cuando = datetime.fromisoformat(str(p.get("created_at")).replace("Z", "+00:00")).astimezone(TZ) if p.get("created_at") else datetime.now(TZ)
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
        self._resp(200, "receptor de Pujas Search Scale funcionando")

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8787), H).serve_forever()
```

### instalar_servidor.sh

```bash
#!/bin/bash
# Pujas Search Scale · Launch Expert — instala el bot en un servidor Ubuntu 24.04 (DigitalOcean US$6/mes).
# Se corre UNA vez en el servidor, como root, con los archivos ya copiados en /opt/pujas:
#   bash /opt/pujas/instalar_servidor.sh
set -e
cd /opt/pujas
apt-get update -qq
apt-get install -y -qq python3 tzdata > /dev/null
chmod 600 .env
mkdir -p estado log ventas

# El bot corre a los :00 y :30 de cada hora; flock evita que se pisen dos corridas
cat > /etc/cron.d/pujas <<'CRON'
SHELL=/bin/bash
0,30 * * * * root cd /opt/pujas && flock -n /tmp/pujas.lock python3 pujas.py >> log/cron.out 2>&1
CRON
chmod 644 /etc/cron.d/pujas

# Receptor de ventas al instante (solo si en .env hay PUJAS_WEBHOOK_CLAVE)
if grep -q '^PUJAS_WEBHOOK_CLAVE=.' .env; then
  apt-get install -y -qq caddy > /dev/null
  IP=$(curl -s https://api.ipify.org)
  HOST="$(echo "$IP" | tr . -).sslip.io"
  cat > /etc/caddy/Caddyfile <<CADDY
$HOST {
  reverse_proxy 127.0.0.1:8787
}
CADDY
  cat > /etc/systemd/system/pujas-receptor.service <<'UNIT'
[Unit]
Description=Pujas Search Scale - receptor de ventas
After=network.target
[Service]
WorkingDirectory=/opt/pujas
ExecStart=/usr/bin/python3 /opt/pujas/receptor.py
Restart=always
[Install]
WantedBy=multi-user.target
UNIT
  systemctl daemon-reload
  systemctl enable --now pujas-receptor
  systemctl restart caddy
  CLAVE=$(grep '^PUJAS_WEBHOOK_CLAVE=' .env | cut -d= -f2)
  echo "URL del webhook para tu plataforma (evento: venta aprobada):"
  echo "  https://$HOST/venta?k=$CLAVE"
fi

echo "Instalado. Prueba sin tocar nada:"
python3 pujas.py --simulacro | tail -25
```

### config.ejemplo.json

```json
{
  "_nota": "Montos en US$ (la moneda de tus cuentas publicitarias). La IA completa este archivo con analizar.py y crear.py; vos solo confirmás los números.",
  "huso": "America/Argentina/Buenos_Aires",
  "utmify_dashboard": "",
  "hora_resumen": "08:00",
  "hora_reinicio": "02:00",
  "hora_sin_subas": "23:59",
  "oferta": {
    "nombre": "Mi Oferta",
    "pais": "AR",
    "filtro_campanas": "Mi Oferta",
    "productos_utmify": [],
    "front": 15.0,
    "ticket": 24.0,
    "cuentas": []
  },
  "reglas": {
    "escalon_pct": 0.07,
    "arranque_pct": 0.25,
    "arranque_escalones_abajo": 2,
    "puja_min_pct": 0.18,
    "puja_max_pct": 0.7,
    "gasto_esperado_30min_x_puja": 0.5,
    "prueba_gasto_x_cpa_obj": 2,
    "valida_roas_min": 1.2,
    "baja_sin_compras_x_puja": 3,
    "baja_cpa_x_puja": 1.3,
    "gasto_suficiente_x_cpa_obj": 3,
    "boost_roas_min": 2.5,
    "boost_compras_min": 3,
    "boost_gasto_max_pct_presupuesto": 0.3,
    "boost_pct": 0.2,
    "boost_freno_roas_menor_a": 1.6,
    "boost_freno_pct": 0.15,
    "presupuesto_recorte_30_roas_menor_a": 1.2,
    "presupuesto_recorte_50_roas_menor_a": 0.9,
    "freno_roas_menor_a": 0.8,
    "freno_perdida_x_cpa_obj": 3
  },
  "lanzar": [],
  "conjuntos": []
}
```