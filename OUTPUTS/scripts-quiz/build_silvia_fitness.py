"""Quiz de Silvia Fitness · Adiós Panza (2026-11-16).

Clon del quiz "Chau Panza" de Belu Fitness (belufitnesschaupanza.impultienda.ar), regla del 14/11:
SU HTML, SU CSS y SU motor; cambian la marca, la experta, las imágenes con su marca y la configuración.
- Las fotos de Belu y las capturas/antes-después de SUS clientas (con marca de agua @belu_fitness) NO se reusan.
  Los mensajes de alumnas se rearman como burbujas HTML y los antes/después quedan en slots (BA_IMGS) para las
  fotos generadas.
- Cada reemplazo tiene que aparecer: si uno no matchea, el script falla.

Uso: python3 build_silvia_fitness.py
"""
import base64, os, re, sys

D = os.path.expanduser("~/Desktop/silvia-fitness")
SRC = f"{D}/referencia/quiz-original-src.html"
IMG = f"{D}/imagenes"

def datauri(p):
    return "data:image/webp;base64," + base64.b64encode(open(p, "rb").read()).decode()

t = open(SRC, encoding="utf-8").read()
CDN = "https://aekpgsbqjzqntlbucbts.supabase.co/storage/v1/object/public/store-resources/48569e59-6064-4e53-8384-cc48bd4fdafe/"
U = lambda n: CDN + n

AVATAR = datauri(f"{IMG}/q-avatar.webp")
HERO = datauri(f"{IMG}/q-hero.webp")
BA = [f"{IMG}/q-ba-{k}.webp" for k in (1, 2)]
BA_JS = ",".join('"%s"' % (datauri(p) if os.path.exists(p) else "") for p in BA)

def rep(old, new, count=None):
    global t
    n = t.count(old)
    if n == 0:
        sys.exit(f"NO MATCHEA: {old[:90]!r}")
    if count is not None and n != count:
        sys.exit(f"Esperaba {count} y hay {n}: {old[:90]!r}")
    t = t.replace(old, new)

# ---------- cabecera y config ----------
rep("<title>Quiz Chau Panza</title>", "<title>Quiz Adiós Panza · Silvia Fitness</title>", 1)
rep("Look único de marca (rosa + ciruela de Belu)", "Look único de marca (rosa + ciruela)", 1)
rep(f'<img class="avatar" alt="Belu" src="{U("1791246260253_imagen-1.webp")}">',
    f'<img class="avatar" alt="Silvia" src="{AVATAR}">', 1)
rep("<b>BELU FITNESS</b><small>CHAU PANZA</small>", "<b>SILVIA FITNESS</b><small>ADIÓS PANZA</small>", 1)
rep('const CHECKOUT_URL = "https://belufitnesschaupanza.impultienda.ar/checkout"; // link de pago (Tiendanube / Mercado Pago). Vacío = baja hasta el precio.',
    'const CHECKOUT_URL = ""; // link del checkout de TU tienda (ej. https://xxxx.impultienda.ar/checkout). Vacío = baja hasta el precio.', 1)
rep('const ALUMNAS = "+29.000";',
    '''const ALUMNAS = "+29.000"; // ⚠️ poné el número real de alumnas
const EXPERIENCIA = "más de 12 años entrenando mujeres"; // ⚠️ la experiencia de Silvia
const BA_IMGS = [%s]; // antes/después (q-ba-1.webp, q-ba-2.webp). Vacío = no se muestra.
function baFig(k,cap){ return BA_IMGS[k]?`<figure class="bafig"><img src="${BA_IMGS[k]}" alt="Antes y después de una alumna de Adiós Panza"><span class="tag l">ANTES</span><span class="tag r">DESPUÉS</span>${cap?`<figcaption>${cap}</figcaption>`:""}</figure>`:""; }
/* ==== Mensajes de alumnas (casos ilustrativos) ==== */
const CHATS = [
  ["Flor","Silvi!! Terminé la semana 4 y me probé el jean que tenía guardado desde el verano pasado. ME ENTRA 😭 bajé 5 kilos sin pasar hambre","9:42"],
  ["Meli","Lo que más me sirvió es la grilla. Antes picoteaba todo el día y ahora sé qué como en cada comida. La panza baja ya no está así de inflada 🙌","13:15"],
  ["Romi","Arranqué en nivel inicial porque no entrenaba hace años. Hoy hice la rutina en intermedio y no lo puedo creer 💪","19:08"],
  ["Caro","Soy mamá de dos y trabajo todo el día. 30 minutos en el living mientras duermen la siesta y ya bajé 4 kilos. Gracias Silvi ❤️","21:30"],
  ["Pau","Tengo 44 y pensé que mi cuerpo ya no respondía. Me siento súper desinflamada y con un montón de energía, voy por más!","8:51"],
  ["Lu","La regla de no faltar dos veces seguidas me salvó. Siempre abandonaba a la semana y esta vez llegué al final 🔥","17:22"]
];
function chat(k){ const [n,m,h]=CHATS[k]; return `<div class="chat"><b>~ ${n}</b><p>${m}</p><small>${h} ✓✓</small></div>`; }''' % BA_JS, 1)

# ---------- textos con la experta ----------
rep("Belu lo ve todos los días con sus ${ALUMNAS} alumnas.", "Silvia lo ve todos los días con sus ${ALUMNAS} alumnas.", 1)
rep("Belu armó una salida específica para cada uno.", "Silvia armó una salida específica para cada uno.", 1)
rep("¿Estás lista para decirle chau a la panza en <em>4 semanas</em>?", "¿Estás lista para decirle adiós a la panza en <em>4 semanas</em>?", 1)
rep("ya hicieron Chau Panza desde su casa", "ya hicieron Adiós Panza desde su casa", 1)
rep("mujeres con su plan Chau Panza", "mujeres con su plan Adiós Panza", 1)
rep("✓ Videos demostrativos grabados por Belu de cada ejercicio.", "✓ Videos demostrativos grabados por Silvia de cada ejercicio.", 1)
rep('[28,95,"Chau panza"]', '[28,95,"Adiós panza"]', 1)

# ---------- prueba social (paso 9) ----------
rep(f'<div class="mt"><figure class="bafig"><img loading="lazy" src="{U("1791246315006_imagen-3.webp")}" alt="Antes y después de una alumna de Chau Panza"><span class="tag l">ANTES</span><span class="tag r">DESPUÉS</span><figcaption>El cambio de Cami, mi alumna, en 4 semanas</figcaption></figure></div>',
    '${BA_IMGS[0]?`<div class="mt">${baFig(0,"El cambio de Flor, mi alumna, en 4 semanas")}</div>`:""}', 1)
m = re.search(r'<div class="stack"><img loading="lazy" class="wa" src="[^"]*imagen-5\.webp"[^>]*><img loading="lazy" class="wa" src="[^"]*imagen-6\.webp"[^>]*></div>', t)
assert m, "stack de la prueba"
t = t.replace(m.group(0), '<div class="stack">${chat(0)}${chat(1)}</div><p class="note">Casos ilustrativos. Los resultados varían de persona a persona.</p>', 1)

# ---------- plan (autoridad) ----------
rep(f'<img loading="lazy" class="hero-img" alt="Belu, creadora de Chau Panza" src="{U("1791246295669_imagen-2.webp")}">',
    f'<img class="hero-img" alt="Silvia, creadora de Adiós Panza" src="{HERO}">', 1)
rep('<p class="auth"><b>Belu</b>: <b>más de 20 años de experiencia</b>, <b>más de 1.200.000 seguidoras</b> entre Instagram y TikTok y <b>${ALUMNAS} alumnas</b> que ya bajaron la panza desde su casa.</p>',
    '<p class="auth"><b>Silvia</b>: <b>${EXPERIENCIA}</b> y <b>${ALUMNAS} alumnas</b> que ya bajaron la panza desde su casa.</p>', 1)

# ---------- venta ----------
rep("<b>Chau Panza en 4 semanas</b> es el mismo método que Belu usa con sus alumnas:",
    "<b>Adiós Panza en 4 semanas</b> es el mismo método que Silvia usa con sus alumnas:", 1)
m = re.search(r'<div class="shots mt" tabindex="0" aria-label="Capturas de mensajes de alumnas, deslizá para ver más">.*?imagen-10\.webp"[^>]*></div>', t, re.S)
assert m and "imagen-10.webp" in m.group(0), "carrusel de capturas"
t = t.replace(m.group(0), '<div class="shots mt" tabindex="0" aria-label="Mensajes de alumnas, deslizá para ver más">${chat(2)}${chat(3)}${chat(4)}</div>', 1)
rep('<p class="sub" style="margin-top:4px">Capturas reales del grupo y de mensajes a Belu.</p>',
    '<p class="sub" style="margin-top:4px">Casos ilustrativos. Los resultados varían de persona a persona.</p>', 1)
m = re.search(r'<div class="stack"><img loading="lazy" class="wa" src="[^"]*imagen-6\.webp".*?imagen-12\.webp"[^>]*></div>', t, re.S)
assert m, "stack de mensajes de la venta"
t = t.replace(m.group(0), '<div class="stack">${chat(5)}${chat(0)}${chat(1)}</div>', 1)

APP = '''<div class="appmock"><div class="am-top"><span class="am-badge">SILVIA FITNESS</span><span class="am-k">ADIÓS PANZA · 4 SEMANAS</span></div>
      <p class="am-h"><span>NO ES UN PDF.</span><br><span>ES TU APP.</span></p>
      <p class="am-p">Entrás desde el celular y tenés todo adentro: <b>el plan de 4 semanas, las comidas y los bonus.</b></p>
      <div class="am-chips"><span>✓ Acceso inmediato vía mail</span><span>✓ Es tuya para siempre</span></div>
      <div class="am-phone"><div class="am-scr"><small>SILVIA FITNESS · ADIÓS PANZA</small><h4>Adiós panza</h4><p>Entrenamiento + alimentación + mentalidad.</p>
        <div class="am-row"><i>💪</i><div><small>ENTRENAMIENTO</small><b>Rutinas con video</b></div><em>›</em></div>
        <div class="am-row"><i>🥗</i><div><small>ALIMENTACIÓN</small><b>Dos semanas repetibles</b></div><em>›</em></div>
        <div class="am-row"><i>🎁</i><div><small>BONUS</small><b>Material complementario</b></div><em>›</em></div>
        <div class="am-row"><i>🧠</i><div><small>MENTALIDAD</small><b>De abandonar a crear el hábito</b></div><em>›</em></div>
      </div></div></div>'''
rep(f'<img loading="lazy" class="appimg" src="{U("1791245447952_imagen-1.webp")}" alt="No es un PDF, es tu app: el plan de 4 semanas, las comidas y los bonus en el celular">', APP, 1)

m = re.search(r'<div class="sec"><h2>Resultados <span class="script">reales</span></h2>.*?</div>\s*</div>', t, re.S)
assert m and "imagen-4.webp" in m.group(0), "bloque resultados reales"
t = t.replace(m.group(0), '''${BA_IMGS.some(Boolean)?`<div class="sec"><h2>Resultados <span class="script">reales</span></h2>
      <p class="sub" style="margin-top:4px">Todas entrenando en casa, sin gimnasio.</p>
      <div class="stack">${baFig(0)}${baFig(1)}</div><p class="note">Casos ilustrativos. Los resultados varían de persona a persona.</p>
    </div>`:""}''', 1)
rep('<p class="foot">Belu Fitness · Chau Panza en 4 Semanas</p>', '<p class="foot">Silvia Fitness · Adiós Panza en 4 Semanas</p>', 1)

# ---------- CSS nuevo (burbujas y maqueta de la app) ----------
CSS = '''
/* mensajes de alumnas en HTML */
.chat{background:#fff;border:1.5px solid var(--line);border-radius:4px 16px 16px 16px;padding:10px 14px 6px;box-shadow:0 1px 2px rgba(0,0,0,.06);text-align:left}
.chat b{display:block;color:#1f8a5b;font-size:14px}
.chat p{margin:2px 0 0;font-size:15px;line-height:1.45;color:#222}
.chat small{display:block;text-align:right;font-size:11px;color:#8a8a8a}
.shots .chat{flex:0 0 82%;max-width:82%;scroll-snap-align:center}
/* maqueta de la app */
.appmock{background:linear-gradient(160deg,var(--plum),var(--plum-2));border-radius:22px;padding:22px 20px 0;color:#fff;overflow:hidden}
.am-top{display:flex;justify-content:space-between;align-items:center;gap:8px}
.am-badge{background:var(--pink);color:var(--plum);font-weight:800;font-size:10px;letter-spacing:.14em;padding:4px 10px;border-radius:999px}
.am-k{font-size:10px;letter-spacing:.14em;color:var(--pink);font-weight:700}
.am-h{font-family:var(--display);font-size:40px;line-height:1.12;margin:18px 0 0}
.am-h span{background:#111;padding:0 8px}
.am-p{font-size:14px;margin:12px 0 0;color:var(--pink-soft)}
.am-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.am-chips span{border:1px solid rgba(255,255,255,.4);border-radius:999px;font-size:11px;padding:4px 10px}
.am-phone{width:72%;margin:22px auto 0;background:#111;border-radius:30px 30px 0 0;padding:10px 10px 0}
.am-scr{background:var(--pink-soft);border-radius:22px 22px 0 0;padding:16px 14px 18px;color:var(--ink)}
.am-scr>small{font-size:9px;letter-spacing:.14em;color:var(--rasp);font-weight:800}
.am-scr h4{font-family:var(--script);font-style:italic;font-size:24px;margin:4px 0 0;color:var(--plum)}
.am-scr>p{font-size:12px;margin:2px 0 10px;color:var(--muted)}
.am-row{display:flex;align-items:center;gap:10px;background:#fff;border-radius:12px;padding:8px 10px;margin-top:8px}
.am-row i{font-style:normal;font-size:18px}
.am-row div{flex:1}.am-row small{display:block;font-size:9px;letter-spacing:.12em;color:var(--rasp);font-weight:800}
.am-row b{font-size:13px}.am-row em{font-style:normal;color:var(--muted);font-size:18px}
'''
rep("</style>\n</head>", CSS + "</style>\n</head>", 1)

# ---------- precio y checkout (16/11: $16.990, checkout propio) ----------
rep('const CHECKOUT_URL = ""; // link del checkout de TU tienda (ej. https://xxxx.impultienda.ar/checkout). Vacío = baja hasta el precio.',
    'const CHECKOUT_URL = "https://adios-panza.impultienda.ar/checkout"; // link de pago. Vacío = baja hasta el precio.\n'
    '/* checkout + los UTM/fbclid con los que llegó la visita */\n'
    'const CK = ()=> CHECKOUT_URL ? CHECKOUT_URL + (location.search ? (CHECKOUT_URL.includes("?")?"&":"?") + location.search.slice(1) : "") : "";', 1)
rep('a.href=CHECKOUT_URL;', 'a.href=CK();', 1)
rep('<a class="cta" id="buyIn" href="${CHECKOUT_URL}"', '<a class="cta" id="buyIn" href="${CK()}"', 1)
rep('"🔒 Pago seguro · Acceso inmediato", CHECKOUT_URL||null);', '"🔒 Pago seguro · Acceso inmediato", CK()||null);', 1)
rep('De <s>$43.998</s> por solo', 'De <s>$33.980</s> por solo', 1)
rep('<div class="now">$21.999</div>', '<div class="now">$16.990</div>', 1)
rep('Menos de <b>$790 por día</b>', 'Menos de <b>$610 por día</b>', 1)  # 16.990 / 28 = 606,8

# ---------- barrido ----------
t = t.replace(' loading="lazy"', "")
for bad in ("belu", "chau panza", "cami,", "aekpgsbqjzqntlbucbts", "1.200.000", "20 años"):
    if bad in t.lower():
        i = t.lower().index(bad)
        sys.exit(f"QUEDÓ RASTRO {bad!r}: …{t[i-80:i+80]}…")

os.makedirs(f"{D}/landing", exist_ok=True)
open(f"{D}/landing/adios-panza-quiz.txt", "w", encoding="utf-8").write(t)
open(f"{D}/landing/adios-panza-PRUEBA.html", "w", encoding="utf-8").write(t)
print("OK", len(t) // 1024, "KB")
