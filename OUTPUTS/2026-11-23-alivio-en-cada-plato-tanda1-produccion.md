Alivio en Cada Plato — tanda 1 producida (LATAM, 23/11/2026)

Clon de הקלה בכל צלחת (hakala-bechol-tzalachat.impultienda.ar). 6 ads de voz en off, 9:16.

QUE COPIA CADA VIDEO
23/11 - 1  La vecina del cuarto piso con el jean ajustado (reaccion de un tercero, su familia mas corrida: 4+2+2 ads)
23/11 - 2  El medico del chequeo anual y el caos de informacion de internet
23/11 - 3  La jefa en el pasillo: energia y cabeza clara, no peso
23/11 - 4  "Como si me hubieran dado un aumento": lo que dejo de gastar en comer afuera
23/11 - 5  El grupo de WhatsApp donde ella era el chiste de las dietas
23/11 - 6  La angustia del domingo a la noche y la semana resuelta en dos horas

VOZ
Sulafat por API. Style: mujer latinoamericana de ~45 grabandose con el celular en la cocina,
acento neutro con seseo, nunca castellano ni rioplatense, ritmo normal de conversacion.
V1 a V4 con gemini-2.5-flash-preview-tts; la cuota del dia se agoto a mitad y V5 y V6 salieron
con gemini-3.1-flash-tts-preview. Las seis verificadas con Whisper: arrancan por la primera
palabra del guion, ningun bloque de estilo leido en voz alta.
Acento verificado con Gemini sobre los dos modelos: "neutro latinoamericano, Colombia andina"
y "neutro latinoamericano, Mexico centro". Ninguno castellano ni rioplatense.
En el plan: speed 1.20, silence [0.26, 0.12].

EDICION (clonada de la suya)
Caja de hook ROJA chica arriba, texto blanco en mayuscula, hasta la palabra que cierra el hook.
Subtitulos de 4 palabras, Montserrat ExtraBold blanco con borde negro, capy 1400, con la palabra
que suena en color: UN color por creativo, rotando magenta (V1, V4), celeste (V2, V5) y lima (V3, V6).
Cortes de 1,8 a 2,5 s. Cama musical unica para la tanda (music_activa, 104 BPM) a -11 dB.
Un solo insert del producto, anclado a la palabra "Alivio": la tapa dibujada por codigo y compuesta
sobre un cuadro real del pool (mesa de madera con un bowl de chia), con sombra y una pizca de rotacion.
Chip rojo "DESCUENTO POR TIEMPO LIMITADO" en 3 de los 6 (V2, V4, V6), como ellos.
Sin placa de cierre y sin boton: termina en el b-roll.

EL CHIP VA SIN EL NUMERO
Ellos ponen "50 % de descuento" porque su landing tiene el precio tachado. Nosotros todavia no
tenemos landing ni precio, asi que el chip dice solo "descuento por tiempo limitado", igual que la voz.
Cuando haya precio y ancla se le pone el numero.

EL POOL: 192 CLIPS BAJADOS, 39 ENTREGADOS
Tags: #mealprep, #healthybreakfast, #glutenfreerecipes, #sugarfreedessert, #traybake.
192 bajados con tikwm en 5 procesos, ninguno truncado (verificado con ffprobe).
Filtro denso a 1 cuadro por segundo (texto con OCR de Vision + caras + bandas negras): 72 con
ventana limpia de 4,5 s o mas.
Pase a ojo sobre hoja de contactos: 56 (afuera harina cruda y masa, pan de molde, una cocina
comercial, caras y torsos identificables, una marca legible y una torta con galletas de azucar).
Hoja de contactos del RENDER: 54 (afuera un frasco con etiqueta VIS KRUIDEN en primer plano y un
cartel impreso de reposteria).
Conteo de caras sobre el CLIP ENTERO: 41 (afuera 11 clips donde el creador aparece a camara en
algun momento, aunque la ventana muestreada estuviera limpia).
OCR de la VENTANA a 1080 px y 2 cuadros/s, la escala a la que la ve el editor: 39 clips, con 16
ventanas recortadas. Ahi aparecieron el paquete KIRKLAND, la salsa Pomarola justo en el CTA del V3
y tres carteles del creador en ingles que el escaneo a 640 px no habia leido. El texto del utensilio
(PYREX, la balanza, los ml de la jarra) se queda: el ganador tambien lo muestra.
39 clips de 39 creadores distintos: no se repite autor en toda la tanda.

LO QUE SE APRENDIO (ya esta en la WIKI)
1. Una ventana limpia no garantiza un clip limpio. El filtro mira la ventana; el creador aparece
   a camara en otro tramo y el editor puede caer justo ahi. En un nicho de recetas hay que contar
   las caras sobre el CLIP ENTERO antes de armar el pool, no solo sobre la ventana.
2. El OCR lee en el render lo que no lee en el clip. El editor amplia (zoom 1.0 a 1.14 + crop), asi
   que un cartel chico que el OCR del pool no marca a 640 px aparece legible en el video armado.
   La hoja del render sigue siendo la ultima palabra.
3. Buscar el clip culpable por su contenido, no deducirlo de un plan. Deducirlo de los indices de un
   plan que se regenero con otro usage.json hace vetar clips inocentes y deja vivo al culpable.
   Costo: dos re-renders completos de la tanda.
4. El glob de zsh que no matchea aborta el comando ENTERO. `rm -f usage.json out/V*.mp4 out/_x* render.log`
   murio en `out/_x*` y no borro ni el usage ni el log: el render siguiente arranco sucio.
   En limpiezas va `find ... -delete`, nunca un glob.

ARCHIVOS NUEVOS EN OUTPUTS/scripts-vsl/
  edit_alivio.py        el editor (caja de hook roja y chip rojo sobre edit_helados.py)
  gen_alivio_plans.py   los planes de los 6
  gfx_alivio.py         la tapa dibujada y compuesta sobre un cuadro real
  ventanas_alivio.py    el filtro denso del pool (texto + caras + bandas, 1 cuadro/s)
  autores_alivio.py     el autor de cada clip, para no repetir creador en cortes contiguos

REVISION FINAL DEL RENDER (OCR a 1080 px, un cuadro por segundo de los 6 videos)
  Cero caras en los seis.
  Un solo defecto: V1, segundo 20, el clip trae "yogurt bowl" en ingles, chico y tenue, centrado.
  Se entrega asi y queda a decision de Santiago rehacer ese video.

ENTREGA
  ~/Desktop/alivio-en-cada-plato/anuncios/   los 6 mp4 y los guiones
  ~/Desktop/alivio-en-cada-plato/imagenes/   la tapa
  Drive: Ebook Dami / Ebook Alivio en Cada Plato (LATAM) / Videos terminados

PENDIENTE
  Landing propia y precio para LATAM (los guiones se escribieron contra el ganador, no contra una
  pagina nuestra: hay que releerlos cuando la pagina exista).
  Decidir quiz o venta directa. El ganador va directo a checkout.
  El numero del chip de descuento.
