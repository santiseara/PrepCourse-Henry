# Claude + Lovable + base de datos de eventos (2026-11-11)

> Pregunta de Santiago: "¿Puedo conectar Claude con Lovable? ¿Y armar una base de datos para que cada cosa que suceda en el sitio me lo notifique?". Respuesta: sí, son dos cosas separadas.

## 1. Claude ↔ Lovable: hay MCP oficial

Se agrega con un comando:

    claude mcp add --transport http lovable "https://mcp.lovable.dev"

- Alternativa: `/plugin install lovable@claude-plugins-official` (mismo servidor + slash commands).
- **Auth:** solo OAuth, se abre el navegador en la primera llamada. No hay API key.
- Disponible en todos los planes (en Enterprise, un admin tiene que habilitar clientes MCP de terceros).

**Qué puedo hacer desde acá una vez conectado:**
- Proyectos: `list_projects`, `get_project`, `create_project`, `deploy_project`, `remix_project`.
- Hablarle al agente de Lovable: `send_message`, `get_message`, `list_messages` (o sea, le pido cambios al sitio desde acá).
- Leer el código: `list_files`, `read_file`, `get_diff`, `list_edits`.
- **Base de datos: `query_database`** → SQL directo contra la base del proyecto, con permisos completos (lectura, escritura y cambios de schema).
- Analytics del proyecto publicado, conectores, subida de archivos.

**Créditos:** `create_project` y `send_message` gastan créditos de Lovable. El resto es gratis.
**Límite:** si el proyecto usa un Supabase propio (no Lovable Cloud), la base se maneja desde Supabase, no por el MCP.

## 2. "Que cada cosa que pase me lo notifique"

Son dos pasos distintos: **guardar** el evento y **avisar**.

1. **Guardar:** Lovable Cloud es Supabase (Postgres) por detrás. Se crea una tabla `eventos`
   (`fecha`, `tipo`, `paso`, `oferta`, `valor`, `utm_source`, `utm_campaign`, `session_id`) y el front
   escribe una fila en cada cosa que importa: entró, paso 3 del quiz, click al checkout, compra.
   Esa tabla **ya es la base de datos**: la puedo consultar desde acá con `query_database`.
2. **Avisar:** **Database Webhooks** de Supabase (trigger de Postgres + `pg_net`). En cada INSERT
   manda un POST HTTP a la URL que le pongas. Se configura en el dashboard (Database → Webhooks)
   o por SQL (`create trigger ... supabase_functions.http_request`), así que **si no tengo dashboard
   a mano lo puedo crear con `query_database`**.
   - ⚠️ No tiene reintentos: si el endpoint falla, el aviso se pierde. Para algo crítico (ventas),
     conviene guardar igual en la tabla y mandar el aviso aparte.
   - 🔐 Va con un header de secreto (`Authorization: Bearer …`) y se verifica del otro lado.
3. **Destino del aviso:** un **bot de Telegram** es lo más simple (una URL, sin servidor propio),
   igual que los bots de pujas y de surfing. Si querés verlo como planilla, el webhook puede
   apuntar a un Apps Script de Google Sheets.

## ⚠️ El punto a resolver primero
En el cerebro, los sitios de Lovable son de **competidores** (`scentedstone.lovable.app`,
`monja-roxo.lovable.app`, DanceGo, Bordado Chinês). Las landings propias están en **ImpulTienda** y
**Shopify**. Si lo que querés registrar son las ventas reales, el evento no nace en Lovable:
nace en ImpulTienda / Whop / Mercado Pago, y eso se engancha por su propio webhook, no por este camino.

## Fuentes
- https://docs.lovable.dev/integrations/lovable-mcp-server
- https://supabase.com/docs/guides/database/webhooks
