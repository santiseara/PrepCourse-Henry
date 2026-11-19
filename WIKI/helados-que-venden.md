# Helados que Venden

> Oferta nueva para **LATAM** (español neutro): recetario de **helado en vasito con base italiana**
> —sin leche condensada y sin crema de leche, sin máquina— para hacer en casa y vender.
> Clon de **Camila Torres - Desarrollo Personal** (`heladosquevenden.impultienda.ar`), que
> **solo tira en Argentina**. Pedido de Santiago el 19/11/2026: *"esta solo tira en arg, así que
> agarremos todo lo validado y pasémoslo a latam, acento neutro, 6 ads"*.

## El ganador que se clona

- **48 anuncios activos** el 19/11/2026. El más viejo es del **9/11**: diez días y ya renovando
  (hay creativos estrenados el 18/11 y el 19/11, con 13 h de actividad). Está escalando, no testeando.
- **Un solo texto principal en los 48.** Lo único que rota es el video. (Mismo patrón que
  [[pisos-epoxi]] y [[postres-en-vaso]].)
- Destino: **quiz de 2 preguntas** en ImpulTienda → *"Responde 2 preguntas y arma tu plan"*.
  Mercado Pago, acceso inmediato, 30 días de garantía.
- Producto: **Combo 5x1** — Recetario Maestro + Postres Helados de las Fiestas + Palitos y Helados
  de Agua + Helados Saludables + Kit Vendé desde tu Casa, **+ 5 bonos** (entre ellos la Planilla
  de Costos y Precios). +100 recetas.

## El mecanismo (lo que hay que conservar)

**La base italiana**: leche, azúcar y leche en polvo en una olla. **No lleva leche condensada ni
crema de leche** — que es con lo que hace helado casero todo el mundo. Dos promesas en una:
**queda más cremosa** y **cuesta menos**. De una sola base salen +100 sabores.
La frase bisagra: *"pensé que iba a perder calidad y pasó exactamente lo contrario"*.

## La DNA de sus videos (12 bajados y transcriptos el 19/11)

- 9:16, **27 a 40 s**, voz en off de mujer + cama musical. **100 % b-roll de producción, sin una sola cara.**
- **5 cuerpos fijos** con el hook rotando:
  - **A** (6 de 12, el ganador): *pasé meses haciéndolo con leche condensada y crema… hasta que conocí la base italiana… pensé que iba a perder calidad y pasó lo contrario… la mejor semana de ventas.*
  - **B**: *descubrí sin querer un ingrediente que da cremosidad y baja el costo… quien lo prueba cree que está hecho con los ingredientes más caros.*
  - **C**: *cómo empezar a vender: base económica, por encargo, a domicilio o por redes; empezás de a poco y aumentás la producción.*
  - **D**: *el día de producción: una sola base, en pocas horas 50 sabores, se hace en la licuadora, no hay que dejarla descansar.*
  - **E**: *no tenés plata para invertir en un negocio grande → ingreso extra.*
- Hooks: los vasitos que parecen de heladería · leche, azúcar, leche en polvo y una olla ·
  si te cuento qué lo hace tan cremoso no me vas a creer · casi no subo este video ·
  mi freezer está lleno y cada pote tiene dueño · ¿no tenés plata para invertir?
- **CTA fijo**: *"solo tenés que tocar el botón de más información"*.

## Su firma de montaje

- **Placa blanca arriba** los primeros 3-5 s, dos renglones en mayúscula: el primero **negro**,
  el segundo **rojo** (*"PARECEN / DE HELADERÍA"*, *"UNA SOLA BASE / +100 SABORES"*,
  *"UNA OLLA / Y UN FREEZER"*). La tienen **la mitad** de los ads, no todos.
- **Subtítulos**: mayúscula, sans bold **recta (no itálica)**, blancos con borde negro,
  **2-3 palabras en un renglón**, tercio inferior (~75 % de la altura), con la palabra que suena
  en **color de texto, sin caja**. El color **rota entre turquesa, verde lima y amarillo**.
- **Flecha roja hacia abajo** sobre el b-roll cuando llega el CTA.
- **Sin** fichas de paso, **sin** placa final y **sin** botón.
- Primer plano casi siempre un **héroe de producto**: la grilla de vasitos de colores, el
  congelador lleno, o cuatro bases cayendo en pantalla partida.

## Lo nuestro (tanda 1, 19/11/2026)

- 6 guiones en `OUTPUTS/2026-11-19-guiones-helados-que-venden-LATAM-tanda1.md` (uno por cuerpo,
  el A y el C duplicados con hooks distintos).
- Descripción en `OUTPUTS/2026-11-19-descripcion-helados-que-venden-LATAM.md`.
- Voz **Sulafat** a 1.20, cama musical activa a −10 dB.
- Editor `OUTPUTS/scripts-vsl/edit_helados.py` (placa blanca de dos colores + flecha roja)
  y `gen_helados_plans.py`.
- Entregados en Drive: **Ebook Dami → Ebook Helados que Venden (LATAM) → Videos terminados**
  (`https://drive.google.com/drive/folders/1LFl3Zq1hDL1pnhWbEjogCBTIfIKB9MVq`). 28 a 33 s, 15 a 17 planos.
- Pool: **88 clips bajados de TikTok, 22 sobrevivieron** (el ojo tiró 54 y el OCR 10 más). Vive en
  `~/Movies/helados-clips` con un symlink en `work/clips`, fuera del Escritorio (iCloud).
- **Neutro**: pote → vasito, frutilla → fresa, plata → dinero, freezer → congelador,
  delivery → a domicilio, y sin cifras en moneda ni Mercado Pago (cambia por país).

## El quiz (19/11/2026)

**Su mismo documento**: su `<style>`, su markup y su motor, con los textos en neutro.
Se bajó con `curl -sL` de la tienda (el bloque va en texto plano entre el `<body>` y los scripts
de ImpulTienda) y se reescribió con `OUTPUTS/scripts-quiz/build_helados_latam.py`, que **falla si
un par no matchea** (regla del 14/11).

- **8 pantallas**: portada → 2 preguntas (tiempo disponible · qué te frena) → *¿necesito máquina?*
  → *¿lleva leche condensada?* → testimonios y sabores → carga con plan armado → oferta.
- **Precio: US$ 12** (valor total US$ 136,90, ahorro US$ 124,90). Checkout propio:
  `https://helados-que-vendenn.impultienda.ar/checkout` (verificado 200, sin redirecciones).
- **El bono 5 cambió de contenido**: *Vendé Helados en Regla* (carnet de manipulador, bromatología,
  monotributo) **no existe fuera de Argentina** → *Envasado y Entrega* (envases, conservación, entrega).
- **Imágenes**: 40 claves, 34 archivos. Se reusaron las suyas; se rehicieron 7 (portada, beneficios,
  mockup de oferta, tapa de paletas, tapa del kit, tapa del bono 5 y la foto del vasito de fresa) y
  se dibujó un sello de pago neutro para reemplazar el de Mercado Pago / Naranja X / Cabal.
  **Van embebidas en el propio archivo** (pedido de Santiago: *"no tengo el txt con las fotos,
  dejámelo solo"*): comprimidas por rol (portada 720 px q70, mockups 620 px q66, miniaturas 420 px q64)
  el entregable queda en **1,28 MB**, abajo del corte de 1,5 MB de ImpulTienda. No hay que subir nada
  a Recursos. Las 8 imágenes rehechas, en calidad alta, están en `OUTPUTS/scripts-quiz/helados-latam-img/`.
- **Neutro**: pote → vasito, frutilla → fresa, palitos → paletas, pan dulce → panettone,
  sin TACC → sin gluten, freezer → congelador, plata → dinero, Mercado Pago → medios de pago de tu país.
- Entregable: **un solo archivo**, `~/Desktop/helados/landing/helados-que-venden-LATAM-quiz.txt`,
  con todo adentro. Copia en `OUTPUTS/2026-11-19-quiz-helados-que-venden-LATAM.html`. Los scripts:
  `build_helados_latam.py` (los textos), `helados_comprimir_img.py` y `helados_empaquetar.py`.


## Preguntas abiertas

- ¿Se queda el nombre **Helados que Venden** o lleva uno propio para LATAM?
- Falta pegarlo en ImpulTienda y probar el quiz en vivo.
- ✅ Quiz y precio resueltos el 19/11: US$ 12 con checkout propio.
- Backend: se clona de los 4 OTOs de [[scented-stones]] ([[backend-molde-de-piedras]]).

## Relacionado
[[postres-en-vaso]] · [[quesos-latam]] · [[pisos-epoxi]] · [[guiones-y-anuncios]]

## Fuentes
- Biblioteca de anuncios de Meta, búsqueda `heladosquevenden.impultienda.ar` (19/11/2026)
- `heladosquevenden.impultienda.ar`
- `~/Desktop/helados/anuncios/comp/transcripciones.txt`
