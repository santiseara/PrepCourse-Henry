# Solar Installer Pro (oferta en inglés)

> **Solar Installer Pro — the 20-day system to install, size and sell solar.** Curso digital de instalación solar para el mercado inglés, a US$ 47 (ancla $197, valor total $461). Clon de **De Cero a Instalador Solar Profesional™**, de la página **Mundo en Digital**, que corre en Argentina desde el 24 de agosto. (fuente: pedido de Santiago del 2026-10-29 + Biblioteca de Anuncios + landing propia)

## La oferta
- Landing: `https://solar-installer-pro.impultienda.ar/` — US$ 47, pago único, acceso de por vida, **garantía de 7 días**, descarga inmediata (PDF + dashboard online).
- Autor de la landing: **Gabriel Fernández**. Prueba social: **+3.200 alumnos**, 4.8/5.
- **6 módulos:** 01 el negocio desde el día uno (registro, cuentas con proveedores, precio mayorista) · 02 instalación paso a paso (on-grid y off-grid) · 03 dimensionamiento y cálculos · 04 venta y contratos · 05 conseguir clientes por Facebook e Instagram sin pagar ads · 06 ingreso recurrente con contratos de mantenimiento.
- **5 bonos + 1 fast-action:** Pre-Quote Checklist ($57) · Supplier Playbook ($47) · Closing Kit ($57: plantilla de cotización, contrato de instalación, contrato de mantenimiento y el script de mensaje) · Permits & Liability Checklist ($37) · The 20-Day Plan ($37) · Low-Budget Tool Kit ($29).
- **Promesas fuertes de la landing** (las que el competidor no usa): *"The global solar market grows 30% a year — installers are the bottleneck"*, *"Solar isn't hard. Finding out how to do it properly is"*, *"The courses are built for engineers"*, *"The demand is already there. The installers are not"*, *"Twenty days from now you can be quoting your first system"*, *"a trade that pays you twice"*.
- Paleta de la landing: azul noche **#0A1A2F**, ámbar **#F5A623**, verde **#26A65B**.
- Imágenes de las tarjetas de bonos y del producto: `~/Desktop/solar-installer-pro/imagenes/img00…img09`.

## El ganador que modelamos (Mundo en Digital, page id 314381038431811)
- **4 anuncios activos.** El más viejo (`1005192582550063`) en circulación desde el **24 de agosto de 2026 = 66 días**. Los otros tres del 22 de septiembre. Landing: `educacionyenlinea.online`, "+ de 1399 DESCARGAS".
- **2 textos principales**, los dos sin una sola cifra de ingreso: *"¿Has intentado aprender sobre energía solar y terminaste más confundido que al principio? Paneles. Baterías. Inversores. Cálculos. Diagramas."* y *"Aprender sobre energía solar no tiene por qué ser complicado."* Cierran con ✔ de entregables y "Haz clic en Más Información".
- **2 cuerpos de video** (voz en off femenina sobre b-roll de instalaciones, 0:54 y 1:13):
  - **A (1:13) · los cálculos.** "Una de las partes que más confunde a quienes comienzan son los cálculos" → las tres preguntas (cuántos paneles, qué batería, qué inversor) → información desordenada → **pero el sector crece** → el problema son los cursos extensos y demasiado técnicos → "existe una forma más estructurada" → los 6 módulos por nombre → 5 bonos, acceso de por vida, celular/tablet/computadora → +3.200 personas → CTA suave.
  - **B (0:54) · por dónde empezar.** "¿Te interesa el mundo de la energía solar pero no sabés por dónde empezar?" → videos, cursos y tutoriales y cuanto más buscás más confuso → "¿cuál es el primer paso?" → mucha teoría y poca práctica → la guía → avanzás a tu ritmo → +3.200 alumnos → "descubre si esta guía puede ayudarte".

### Lo que esto dice
**Vende claridad, no plata.** Cero montos, cero plazos de ganancia, cero "cambiá tu vida". Es exactamente el patrón anti-bloqueo de [[profesional-digital]], y acá lo sostiene **66 días de circulación**. La oportunidad se nombra como **mercado que crece**, no como ingreso prometido. Nuestros guiones agregan la promesa fuerte en la primera línea (regla del 29/10) sin tocar ninguna de esas tres líneas rojas.

## Tanda 1 (2026-10-29): 6 videos
- Guiones (EN + ES con voseo): `OUTPUTS/2026-10-29-guiones-solar-installer-pro.md`, copia en `anuncios/guiones.md`. Ángulos:
  1. no es difícil, es que nadie te lo pone en orden · 2. lo que falta no son los paneles, son los instaladores · 3. te dejan apuntes, esto te deja una cotización · 4. dimensionar es todo el oficio · 5. la otra mitad arranca cuando el cliente dice que sí · 6. del día uno al día veinte.
- **Videos de 32 a 35 s**, 9:16, en `~/Desktop/solar-installer-pro/anuncios/SIP-V1.mp4` … `SIP-V6.mp4`. Nombres para subir: `29/10 - 1` a `29/10 - 6`.
- **Voz:** AI Studio, Gemini 3.1 Flash TTS Preview, voz **Orus** (Firm, Lower middle pitch), Pace **Natural**. Audio Profile: *"American man around 40, a hands-on tradesman narrating a punchy ad on TikTok. Confident, direct, energetic and conversational, brisk pace, no radio-announcer tone."* Scene: un instalador solar de cuarenta y pico grabando el voiceover de un TikTok en una obra. Crudos de 34,8 a 42,7 s; plan a `speed 1.30` con `silence [0.26, 0.12]`.
- **Música:** la cama del propio ganador, separada de la voz con demucs (`work/music/bed_A.wav`, del ad de 66 días), a −11 dB. **Una sola para los seis**, según la regla del 27/10.
- **B-roll de TikTok:** 132 clips bajados con tikwm de los tags `solarinstaller`, `solarinstallation`, `solarpanelinstallation` y `offgridsolar`; **21 limpios y usados** (`anuncios/work/tiktoks/`). Cero stock, cero créditos.
- **Edición:** `OUTPUTS/scripts-vsl/edit_solar.py` (copia de `edit_energia.py`) con la paleta de la landing: caja azul noche del hook, chips ámbar, palabra activa del subtítulo en ámbar y placa final "SOLAR INSTALLER PRO · 6 MODULES · 5 BONUSES · 20-DAY PLAN". Planes: `gen_solar_plans.py`.
- **Texto principal:** uno solo para los seis, en `anuncios/texto-principal.md`.

## Lo que se aprendió acá
- **El nicho solar rinde muchísimo en TikTok**, al revés de cristales y sahumerios ([[energia-vital]]): de ~38 clips revisados quedaron 21 limpios. Hay cuentas de instaladores que publican puro proceso sin hablar a cámara (@cutlerbaysolarsolution, @pv_monteur, @greenleafsolar, @skysolarpro, @unitysolargroup). Lo que se descarta sigue siendo lo mismo: cartel quemado ("SOLAR INSTALLATIONS 5KVA", "AUTOMATIC SOLAR CLEANING SYSTEM"), marca de agua móvil (@volta_solar), cara del creador hablando y los 16:9.
- **tikwm no contesta a `urllib`** (403) ni al endpoint de búsqueda: funciona el endpoint documentado `api/?hd=1&url=` llamado con **curl**. Los links se sacan de `tiktok.com/tag/<tag>` en el Chrome de Santiago y se bajan de la página como un `.txt` con un `<a download>`, porque el `fetch` a un receptor local lo bloquea el permiso de red local.
- **Los videos del competidor se bajan igual**, con un `fetch` + blob + `<a download>` desde la Biblioteca de Anuncios: el `video.src` sale bloqueado si se lo pide por JS.

## Preguntas abiertas
- ¿Hay OTO después del pago? La landing no muestra bumps.
- ¿Se corre también formato native/imagen, o solo video?
- El competidor corre en español para LATAM: ¿se clona también esa versión, o solo inglés?

## Relacionado
[[profesional-digital]] · [[guiones-y-anuncios]] · [[energia-vital]] · [[funnel-hacking]] · [[vsl-reglas-de-armado]] · [[ugc-y-video-generativo]] · [[internacionalizacion]]

## Fuentes
- Biblioteca de Anuncios de Meta, page id 314381038431811 (relevada el 2026-10-29)
- https://solar-installer-pro.impultienda.ar/ (leída el 2026-10-29)
