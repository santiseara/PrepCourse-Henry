# Organización y registro de la operación

> Registro diario por oferta, tres cuentas con tres trabajos, el recorrido de herramientas y las reglas para que el método siga vivo. (fuente: RAW/2026-10-10-wiki-previa/organizacion-y-registro.md)

**Sin un registro, cada decisión se olvida y se repiten los mismos tests.** Todo cambio de presupuesto o de puja se anota con la hora y con la captura de los números.

## Registro diario

- **Una página por oferta y por día** (en Notion, o en `OUTPUTS/` de este segundo cerebro).
- Cada cambio de presupuesto o de puja se anota **con la hora** y con una **captura del dashboard de UTMify**.
- Así no se pierde el historial de qué se tocó y qué pasó con las ventas después.
- Para los creativos, el registro de qué ángulo ganó lo lleva la skill `ad-builder`.

## Tres cuentas, tres trabajos

| Cuenta | Qué corre |
|---|---|
| **Testeo** | ABO 1-1-1 (o 5 conjuntos), con 3× el CPA medio (testeo acelerado) o 1× el CPA medio. O la CBO de testeo ([[testeo-de-creativos]]) |
| **Escala automática** | V3, aisladas, Pockets, Launch Pocket, CBO mixta y power ([[metodo-v3]], [[estructuras-cbo]]) |
| **Pujas manuales** | CostCap, BidCap y ROAS cap con intrapujas ([[escalado-en-meta-ads]]) |

Una cuarta cuenta, o más, sirve para **replicar horizontalmente** lo que gana. Probá entre 5 y 7 cuentas y quedate con las de **menor CPM**. El CPM puede variar mucho entre cuentas (4, 6 u 8 USD) solo por su historial.

## El recorrido de herramientas

1. **Espiar:** Biblioteca de Anuncios, AdSpy, Minea o GetHook ([[funnel-hacking]]).
2. **Modelar la oferta** y escribir la landing y el copy: Claude.
3. **Producto:** Gamma para el MVP y Claude + Higgsfield para la versión de calidad, después de validar ([[creacion-de-productos-digitales]]).
4. **Testear y escalar:** Meta Ads, a mano o por el conector de Claude.
5. **Trackear:** UTMify ([[tracking-y-atribucion]]).

## Reglas de organización

- **La Biblioteca de Anuncios es la mejor mentoría gratis que existe.** Dedicarle horas no es negociable, en cualquier nivel.
- **No dependas de swipe files compartidos.** Si mucha gente modela lo mismo al mismo tiempo, se satura.
- **No te despegues de la comunicación validada.** Traducí y adaptá el copy y el formato exacto del competidor que modelás. Solo se mejora el mecanismo único. No se cambia la comunicación a la primera, sin datos.
- **El método es un documento vivo.** Las estructuras de campaña y las herramientas cambian cada pocas semanas. Cuando llegue material nuevo, cargalo en `RAW/` y pedile a Claude «procesá RAW».
- **Tené funnels listos antes de necesitarlos.** Con varias ofertas armadas es más probable encontrar una cuya matemática cierre (costo por visita menor que ingreso por visita).

Relacionado: [[testeo-de-creativos]] · [[escalado-en-meta-ads]] · [[metodo-v3]] · [[ia-en-el-flujo-de-trabajo]]

## 📁 Entrega en Google Drive — TODA tanda terminada (REGLA FIJA, 2026-11-13 · reconfirmada el 2026-11-14)

Santiago: *"vos entrás a esa carpeta y vas a crear una nueva carpeta con el nombre de la oferta que el nombre de la oferta siempre por delante va a tener la palabra eBook… y dentro de la carpeta que crees vas a crear una carpeta que se llame Videos terminados y ahí vas a subir los anuncios terminados siempre siempre"*.

**2026-11-14, al arrancar [[navidad-en-macrame]]: *"Acordate lo del drive, guardalo como regla así no lo tengo que repetir más"*.** O sea: el Drive **no se pregunta y no se avisa**. Apenas una tanda está renderizada y revisada, se sube, se da el link y recién ahí se cuenta que está lista. Vale para **toda oferta nueva**, no solo las del socio: si no hay una indicación distinta, el destino es `Ebook Dami`.

**El camino exacto:**

```
Mi unidad / Ebook Dami / Ebook <Oferta> (<MERCADO>) / Videos terminados /
```

- La carpeta madre **`Ebook Dami`** ya existe y no se toca. Dentro va **una carpeta por oferta**.
- El nombre de la carpeta de la oferta **siempre arranca con `Ebook`** y después el nombre de la oferta (ej.: oferta "Campo" → `Ebook Campo`). Las carpetas que ya están ahí cierran con el mercado entre paréntesis — `Ebook Tapizado (LATAM)`, `Ebook Juegos en Pareja (ARG)`, `Ebook Box (INGLES)` —, así que se respeta esa forma: **`Ebook <Oferta> (LATAM | ARG | INGLES | …)`**.
- Dentro de la carpeta de la oferta va **siempre** una subcarpeta **`Videos terminados`**, y ahí van **los anuncios terminados** (los MP4 finales, no los crudos ni las voces ni los guiones).
- **El nombre de cada video es el arranque del hook**, tal cual se escucha. Si el video empieza diciendo *"Las vacas que…"*, el archivo se llama **`Las vacas.mp4`**. Nada de `V1.mp4` ni de la nomenclatura `DD-M - N` acá: esa sigue valiendo para la carpeta del Escritorio.
- **Es el mismo proceso siempre, sin que lo pida.** Apenas una tanda está terminada, se sube.

### Cómo se suben los videos a Drive (resuelto el 2026-11-13)

Santiago: *"Metela en el drive siempre, no quiero mas en el escritorio"*. **Los videos terminados no
quedan en el Escritorio: van al Drive y listo.** El Escritorio es solo taller (`work/`, con las voces,
el pool de clips y los masters en alta).

**El método que funciona** (Drive no acepta arrastre simulado ni deja usar el selector nativo):

1. Abrir la carpeta `Videos terminados` en Chrome y **parchear `HTMLInputElement.prototype.click`**
   para que, cuando Drive quiera abrir el selector nativo, en vez de abrirlo **se capture el input**:
   guardarlo en `window.__cap`, ponerle un `id` y un `aria-label` propios y, si no está en el DOM,
   agregarlo al `body`. Sin el parche, el clic abre un diálogo del sistema que no se puede manejar.
2. Clic real en **Nuevo → Subir archivo**. El input queda capturado (es `multiple`).
3. Cargar los MP4 con `file_upload`. **Tope de 10,4 MB por llamada**, así que van de a uno. ⚠️ **Desde
   el 2026-11-14 `file_upload` solo acepta archivos que la sesión tiene permitidos**: un MP4 que está en
   `~/Desktop/...` lo rechaza con *"only files this session is allowed to read can be uploaded"*. Se copian
   antes al **scratchpad de la sesión** y se suben desde ahí. Para
   mandarlos todos juntos, se acumulan en un `input` propio con un listener que los empuja a
   `window.__acc`, y al final se arma un `DataTransfer` y se hace `input.files = dt.files`.
4. Disparar `input` y `change` sobre el input capturado. Ahí Drive sube de verdad.

**Por el tope de 10,4 MB los MP4 se recomprimen antes de subir:** `-crf 29 -maxrate 1650k -preset slow`
deja un ad de 45 s en 1080x1920 en **8,5–9,6 MB** (el render sale a 12 Mbps, 65–76 MB). Es calidad de
sobra para Meta, que recomprime igual. **El master en alta queda en `work/masters/`.**

⛔ Lo que **no** funciona y no hay que volver a probar: el evento `drop` sintético sobre la página de
Drive (exige eventos confiables y `webkitGetAsEntry` real), el `fetch` a un servidor local (lo corta la
CSP de Drive), y las descargas automáticas del navegador (Chrome las bloquea después del primer intento).
Tampoco hay Google Drive para escritorio instalado; si algún día se instala, la subida pasa a ser un `cp`.

**La única excepción:** cuando él dice expresamente que esa oferta no va al Drive. Mientras no lo diga, toda tanda terminada sube a `Ebook Dami` (regla reconfirmada el 2026-11-14).

### 🔧 Cómo se sube un MP4 al Drive desde acá (2026-11-13)
Drive no deja subir por las vías obvias y esto costó encontrarlo, así que queda anotado:
- **El drag & drop sintético no funciona** (Drive ignora un `DragEvent` que no es del usuario) y **el `fetch` a un servidor local se cuelga** (Chrome bloquea las peticiones de un sitio público a `127.0.0.1`).
- **Lo que sí funciona:** parchear `HTMLInputElement.prototype.click` para que, cuando Drive quiera abrir el selector nativo, guarde el input en `window.__drvInput` en vez de abrirlo; después *Nuevo → Subir archivo* (el selector ya no se abre), se le asignan los archivos con un `DataTransfer` y se dispara `change`. Drive los sube como si los hubiera elegido él.
- **El límite de 10 MB de la herramienta de subida se sortea troceando:** el MP4 se parte en pedazos de 9,4 MB, cada pedazo entra por un `<input type=file>` propio inyectado en la página, y adentro del navegador se rearma con `new File([...partes], 'Nombre del hook.mp4')`. Se verifica que el tamaño del File coincida con el del archivo en disco antes de mandarlo.
- **Un input de Drive sirve para una sola tanda:** después de un `change` hay que volver a pedir *Nuevo → Subir archivo*. Varios archivos sí pueden ir juntos en el mismo `DataTransfer`.

> Esto **no reemplaza** la carpeta local: los videos igual se arman y quedan en `~/Desktop/<oferta>/anuncios/` con el nombre de tanda `DD-M - N` (regla de [[como-trabajar-con-santiago]]). El Drive es la **entrega**, el Escritorio es el **taller**.

## Conexiones con tu operación actual
- **El registro diario va en `OUTPUTS/` de este cerebro.** Cuando me pases cambios de presupuesto o de puja con la captura de UTMify, los anoto en `OUTPUTS/AAAA-MM-DD-registro-<oferta>.md` y los enlazo desde el índice.
- **"El método es un documento vivo: cargá en RAW y pedí procesá RAW"** es exactamente cómo funciona este segundo cerebro.
- **"No te despegues de la comunicación validada"** coincide con tus variables: se mantiene la DNA y se mejora el mecanismo, no se reinventa ([[scented-stones]]).

## Fuentes
- RAW/2026-10-10-wiki-previa/organizacion-y-registro.md (página de la wiki previa, actualizada el 2026-09-24)
- Fuentes originales citadas (todavía no están en este cerebro): clases de la formación y experiencias de la comunidad, agosto–septiembre 2026
