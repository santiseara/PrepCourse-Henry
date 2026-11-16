#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arma el quiz "Reseteo del Nervio Vago 28" para LATAM (español neutro).

Clona el documento del original (https://nervio-vago.impultienda.ar/): su motor
(engine v2 block-based), su CSS (q-home), su tema y sus 36 pasos. Lo unico que
cambia son los textos (voseo argentino -> neutro LATAM), las imagenes con
marcador argentino (el mate) y el bloque de configuracion.

Salida:
  <out>/nervio-vago-quiz.txt   -> para pegar en el custom_html de ImpulTienda
  <out>/PRUEBA.html            -> el mismo HTML para abrir en Chrome
  <out>/spec-latam.json        -> el spec solo, por si el builder lo importa

Uso: python3 build_nervio_vago_latam.py <carpeta-trabajo> <carpeta-salida>
"""
import base64
import json
import mimetypes
import os
import re
import sys

# ---------------------------------------------------------------------------
# 1. Reemplazos de texto: voseo argentino -> espanol neutro LATAM.
#    Cada par TIENE que matchear al menos una vez o el script falla.
# ---------------------------------------------------------------------------
TEXTOS = {
    # --- portada y genero -------------------------------------------------
    "Elegí tu edad para personalizar tu plan":
        "Elige tu edad para personalizar tu plan",
    "Al elegir tu edad aceptás los términos y la política de privacidad.":
        "Al elegir tu edad aceptas los términos y la política de privacidad.",
    "¿Con qué te *identificás*?":
        "¿Con qué te *identificas*?",

    # --- prueba social ----------------------------------------------------
    "argentinas ya hicieron este test":
        "mujeres de Latinoamérica ya hicieron este test",
    "Y la mayoría se sorprendió con el resultado. Contestá con sinceridad: no hay respuestas buenas ni malas.":
        "Y la mayoría se sorprendió con el resultado. Responde con sinceridad: no hay respuestas buenas ni malas.",

    # --- sintomas ---------------------------------------------------------
    "¿Cada cuánto te sentís *estresada o ansiosa*?":
        "¿Cada cuánto te sientes *estresada o ansiosa*?",
    "¿Te levantás *cansada* aunque hayas dormido?":
        "¿Te levantas *cansada* aunque hayas dormido?",
    "¿Te pasa de tener la *cabeza nublada* o no poder concentrarte?":
        "¿Te pasa que tienes la *cabeza nublada* o no puedes concentrarte?",
    "¿Sentís el *cuello, la mandíbula o los hombros* duros?":
        "¿Sientes el *cuello, la mandíbula o los hombros* duros?",

    # --- placa del nervio vago -------------------------------------------
    "El cansancio, la ansiedad, la niebla mental y las contracturas no vienen sueltos. Son señales de tu nervio vago, el cable que une tu cerebro con el corazón, los pulmones y la panza. Cuando se traba, tu cuerpo se queda en *modo alerta* todo el día.":
        "El cansancio, la ansiedad, la niebla mental y las contracturas no vienen sueltos. Son señales de tu nervio vago, el cable que une tu cerebro con el corazón, los pulmones y el estómago. Cuando se traba, tu cuerpo se queda en *modo alerta* todo el día.",

    # --- frases de identificacion ----------------------------------------
    "¿Cuánto te identificás con esta frase?":
        "¿Cuánto te identificas con esta frase?",
    "“Cómo me siento me está *frenando* en el laburo y en mis planes”":
        "“Cómo me siento me está *frenando* en el trabajo y en mis planes”",
    "¿Te saltás con los demás *y después te arrepentís*?":
        "¿Les contestas mal a los demás *y después te arrepientes*?",
    "¿Sentís que te estás *perdiendo la vida* por cómo te sentís?":
        "¿Sientes que te estás *perdiendo la vida* por cómo te sientes?",

    # --- placa de modo alerta --------------------------------------------
    "Con el nervio vago trabado, el cuerpo cree que está en peligro todo el tiempo: el cortisol no baja, dormís mal, digerís mal y la energía se te va en sostener la alarma. Por eso ni las vacaciones te recargan.":
        "Con el nervio vago trabado, el cuerpo cree que está en peligro todo el tiempo: el cortisol no baja, duermes mal, digieres mal y la energía se te va en sostener la alarma. Por eso ni las vacaciones te recargan.",

    # --- antiguedad y cafeina --------------------------------------------
    "¿Hace cuánto *te sentís así*?":
        "¿Hace cuánto *te sientes así*?",
    "¿Cuánto *mate o café* tomás por día?":
        "¿Cuánto *café o té* tomas por día?",
    "Mate todo el día": "Café todo el día",
    "2 cafés o más": "2 tazas o más",
    "Uno por día": "Una por día",

    # --- sueno y cuerpo ---------------------------------------------------
    "Elegí todas las que te pasen": "Elige todas las que te pasen",
    "Me despierto a la madrugada": "Me despierto de madrugada",
    "Panza hinchada": "Barriga hinchada",
    "Caída de pelo": "Caída del cabello",

    # --- estresores -------------------------------------------------------
    "El laburo": "El trabajo",
    "La plata": "El dinero",
    "Los chicos y la casa": "Los niños y la casa",

    # --- objetivos --------------------------------------------------------
    "¿Qué querés *mejorar primero*?": "¿Qué quieres *mejorar primero*?",
    "Elegí todas las que quieras": "Elige todas las que quieras",
    "¿Para qué *lo querés*?": "¿Para qué *lo quieres*?",
    "Rendir mejor en el laburo": "Rendir mejor en el trabajo",
    "¿Cuánto tiempo le podés dar *por día*?": "¿Cuánto tiempo le puedes dar *por día*?",

    # --- placa de la calma ------------------------------------------------
    "“Con un plan claro no necesitás fuerza de voluntad: solo seguir el paso del día.”":
        "“Con un plan claro no necesitas fuerza de voluntad: solo seguir el paso del día.”",

    # --- compromiso y lead ------------------------------------------------
    "¿Te comprometés a darle *28 días a tu cuerpo*?":
        "¿Te comprometes a darle *28 días a tu cuerpo*?",
    "Sí, arranco hoy": "Sí, empiezo hoy",
    "Sí, arranco mañana": "Sí, empiezo mañana",
    "Último paso: ¿a dónde te mandamos *tu resultado*?":
        "Último paso: ¿a dónde te enviamos *tu resultado*?",
    "Dejanos tu nombre y tu mail para ver tu diagnóstico y tu plan.":
        "Déjanos tu nombre y tu correo para ver tu diagnóstico y tu plan.",

    # --- testimonio de la carga ------------------------------------------
    "“Lo hice en la cocina, con el mate”. Pensé que era una pavada y a la semana ya dormía mejor. Cortito y fácil de seguir.":
        "“Lo hice en la cocina, con mi café”. Pensé que era una tontería y a la semana ya dormía mejor. Cortito y fácil de seguir.",
    "Silvina, 47": "Silvana, 47",

    # --- resultados -------------------------------------------------------
    "Todavía no estás en modo supervivencia, pero las señales ya aparecen: cansancio, tensión y un sueño que no siempre te recarga. Con 5 a 15 minutos por día lo podés revertir rápido.":
        "Todavía no estás en modo supervivencia, pero las señales ya aparecen: cansancio, tensión y un sueño que no siempre te recarga. Con 5 a 15 minutos por día lo puedes revertir rápido.",
    "Tus respuestas muestran un sistema nervioso que no logra apagar la alarma: dormís pero no descansás, la cabeza no para y el cuerpo vive tenso. La buena noticia es que el nervio vago se entrena.":
        "Tus respuestas muestran un sistema nervioso que no logra apagar la alarma: duermes pero no descansas, la cabeza no para y el cuerpo vive tenso. La buena noticia es que el nervio vago se entrena.",

    # --- bonos ------------------------------------------------------------
    "Qué sumar y qué bajar (incluido el mate y el café).":
        "Qué sumar y qué bajar (incluidos el café y el azúcar).",

    # --- checklist de la oferta ------------------------------------------
    "Te levantás con energía de verdad": "Te levantas con energía de verdad",
    "Chau niebla mental y olvidos": "Adiós a la niebla mental y los olvidos",
    "Dormís de corrido y te despertás descansada":
        "Duermes de corrido y te despiertas descansada",
    "Dejás de saltar con los tuyos por cualquier cosa":
        "Dejas de contestarles mal a los tuyos por cualquier cosa",

    # --- testimonios de la oferta ----------------------------------------
    "“Mi marido me dijo: volviste”. Dos médicos me dijeron que lo mío era estrés. Vivía cansada, con la cabeza en una nube y saltando con los chicos por todo. A la tercera semana dormí de corrido por primera vez en meses.":
        "“Mi esposo me dijo: volviste”. Dos médicos me dijeron que lo mío era estrés. Vivía cansada, con la cabeza en una nube y contestándoles mal a mis hijos por todo. A la tercera semana dormí de corrido por primera vez en meses.",
    "Carolina G., 44 · Rosario": "Carolina G., 44 · Guadalajara",
    "“Se me fue el nudo en el pecho”. Pensé que era la edad o que estaba quemada del laburo. Los ejercicios son cortitos, los hago a la mañana con el mate. En dos semanas se me aflojó el cuello y la presión en el pecho bajó un montón.":
        "“Se me fue el nudo en el pecho”. Pensé que era la edad o que estaba quemada del trabajo. Los ejercicios son cortitos, los hago en la mañana con mi café. En dos semanas se me aflojó el cuello y la presión en el pecho bajó muchísimo.",
    "Laura M., 38 · CABA": "Laura M., 38 · Bogotá",
    "Mónica R., 56 · Córdoba": "Mónica R., 56 · Lima",

    # --- FAQ y garantia ---------------------------------------------------
    "No. Pagás una sola vez y el plan es tuyo para siempre. Sin cargos automáticos.":
        "No. Pagas una sola vez y el plan es tuyo para siempre. Sin cargos automáticos.",
    "Apenas pagás te llega todo por mail para descargar: el plan de 28 días y los 3 bonos.":
        "Apenas pagas te llega todo por correo para descargar: el plan de 28 días y los 3 bonos.",
    "Apenas pagás te llega por mail el acceso a tu app, con el plan de 28 días y los 3 bonos.":
        "Apenas pagas te llega por correo el acceso a tu app, con el plan de 28 días y los 3 bonos.",
    "🛡️ Garantía de 7 días: si sentís que no es para vos, te devolvemos el 100%. Sin vueltas.":
        "🛡️ Garantía de 7 días: si sientes que no es para ti, te devolvemos el 100%. Sin vueltas.",

    # --- carril B (quiz corto + VSL) -------------------------------------
    "Elegí la que más te identifique": "Elige la que más te identifique",
    "¿Cada cuánto sentís el cuerpo *en modo alerta*?":
        "¿Cada cuánto sientes el cuerpo *en modo alerta*?",
    "Acelerada, tensa o saltando por cualquier cosa":
        "Acelerada, tensa o reaccionando por cualquier cosa",
}

# Precios: viven en un solo lugar. El original corre dos (A/B del competidor);
# en LATAM va uno solo.
PRECIOS = {
    "Hoy *$14.999* en vez de $39.999 · pago único, sin suscripción":
        "Hoy *{PRECIO}* en vez de {PRECIO_ANTES} · pago único, sin suscripción",
    "Hoy *$19.990* en vez de $39.999 · pago único, sin suscripción":
        "Hoy *{PRECIO}* en vez de {PRECIO_ANTES} · pago único, sin suscripción",
}

# Emojis: el original repite ☕ en dos opciones del mismo paso cuando se saca
# el mate. Un emoji por opcion (regla del 2026-11-04).
ICONOS = {"🧉": "☕", "☕": None}  # se resuelve por paso, ver fix_iconos()

# Bloques HTML del original que NO se copian: su analitica y su A/B de precio.
BLOQUES_FUERA = {"bsm9m4qd", "bab_pref", "bab_r1", "bab_r2", "bab_r3"}

# ---------------------------------------------------------------------------
# Parche al motor: la barra de progreso.
#
# El motor supone que las pantallas con `outcome` son "variantes de un mismo
# resultado" y las cuenta como UNA sola. En este quiz el `outcome` es el
# mecanismo del A/B, asi que lo llevan las 35 pantallas menos la portada:
#   gated = 35  ->  total = 36 - 34 = 2  ->  pct = 100 % desde el paso 1.
# La barra nacia llena y no se movia nunca.
#
# El reemplazo cuenta solo las pantallas de PREGUNTA del carril en el que esta
# la persona (las que llevan `showProgress`, filtradas por su banda de puntaje
# con el mismo `gateMatches` del motor). Son 25 en el carril largo, asi que la
# barra avanza de a 4 % por pregunta y llega a 100 % en la ultima.
PROGRESO_VIEJO = """  function progressBar(screen) {
    if (screen.showProgress === false) return ''
    // Score-gated screens are alternatives of one result slot: count them as 1.
    var gated = 0
    for (var k = 0; k < steps.length; k++) if (steps[k] && steps[k].outcome) gated++
    var total = steps.length - (gated > 1 ? gated - 1 : 0)
    var pos = 0
    for (var m = 0; m <= state.i && m < steps.length; m++) if (!steps[m].outcome) pos++
    if (screen.outcome) pos++
    var pct = Math.min(100, Math.round(((pos - 1) / Math.max(1, total - 1)) * 100))
    return '<div class="quiz-progress"><div class="quiz-progress-bar" style="width:' + pct + '%"></div></div>'
  }"""

PROGRESO_NUEVO = """  function progressBar(screen) {
    if (screen.showProgress === false) return ''
    // Solo las pantallas de pregunta del carril en el que esta la persona.
    // (El conteo original colapsaba las 35 pantallas con `outcome` en una sola
    //  y dejaba la barra en 100 % desde la primera pregunta.)
    var total = 0, pos = 0
    for (var k = 0; k < steps.length; k++) {
      var s = steps[k]
      if (!s || s.showProgress === false) continue
      if (!gateMatches(s)) continue
      total++
      if (k <= state.i) pos++
    }
    var pct = total > 0 ? Math.min(100, Math.round((pos / total) * 100)) : 100
    return '<div class="quiz-progress"><div class="quiz-progress-bar" style="width:' + pct + '%"></div></div>'
  }"""

CAMPOS_TEXTO = {
    "text", "label", "title", "body", "authorName", "question", "metricLabel",
    "startLabel", "endLabel", "placeholder",
}

usados = {}


def traducir(valor):
    if valor in TEXTOS:
        usados[valor] = usados.get(valor, 0) + 1
        return TEXTOS[valor]
    return valor


def walk(nodo):
    """Aplica los reemplazos a todo campo de texto visible del spec."""
    if isinstance(nodo, dict):
        if nodo.get("type") == "html":
            return
        for k, v in list(nodo.items()):
            if isinstance(v, str) and k in CAMPOS_TEXTO:
                nodo[k] = traducir(v)
            else:
                walk(v)
    elif isinstance(nodo, list):
        for x in nodo:
            walk(x)


def fix_iconos(spec):
    """Ningun paso repite emoji (el mate se fue y dejaba dos ☕)."""
    nuevos = {"Café todo el día": "☕", "2 tazas o más": "🍵", "Una por día": "🥛"}
    tocados = 0
    for step in spec["steps"]:
        for b in step.get("blocks", []):
            for o in b.get("options", []) or []:
                if o.get("label") in nuevos:
                    o["icon"] = nuevos[o["label"]]
                    tocados += 1
    assert tocados == 3, f"esperaba 3 iconos de cafeina, toque {tocados}"


def fix_precios(spec, precio, precio_antes):
    n = 0
    for step in spec["steps"]:
        for b in step.get("blocks", []):
            t = b.get("text")
            if isinstance(t, str) and t in PRECIOS:
                b["text"] = (PRECIOS[t]
                             .replace("{PRECIO}", precio)
                             .replace("{PRECIO_ANTES}", precio_antes))
                n += 1
    assert n == 4, f"esperaba 4 lineas de precio, encontre {n}"


def data_uri(path):
    mime = mimetypes.guess_type(path)[0] or "image/webp"
    with open(path, "rb") as fh:
        return "data:%s;base64,%s" % (mime, base64.b64encode(fh.read()).decode())


# ---------------------------------------------------------------------------
# 2. Bloques HTML propios (reemplazan los del competidor)
# ---------------------------------------------------------------------------
AB_ASIG = """<style>
.quiz-block[data-block-options]~.quiz-block[data-block-options]{display:none}
html[data-abvsl=B] .quiz-block[data-block-options]:has(~.quiz-block[data-block-options]){display:none}
html[data-abvsl=B] .quiz-block[data-block-options]~.quiz-block[data-block-options]{display:block}
.nvb-sub{display:none;text-align:center;font-size:.98rem;color:#4B4560;margin:-4px 0 6px}html[data-abvsl=B] .nvb-sub{display:block}
.nvb-sub b{color:#6E4FD0}
</style><p class="nvb-sub">Responde <b>5 preguntas</b> y <span class="nvb-exp"></span> te explica tu resultado en un video corto.</p>
<script>(function(){var C=(window.CONFIG_QUIZ||{});
try{document.querySelector('.nvb-sub .nvb-exp').textContent=C.VSL_EXPERTA||'nuestra especialista'}catch(e){}
// El carril B (quiz corto + VSL) solo se reparte si hay video cargado.
try{if(!C.AB_VSL||!C.VSL_MP4){document.documentElement.setAttribute('data-abvsl','A');return}
var k='nv_ab_vsl',v=localStorage.getItem(k);if(v!=='A'&&v!=='B'){v=Math.random()<0.5?'A':'B';localStorage.setItem(k,v)}
document.documentElement.setAttribute('data-abvsl',v)}catch(e){document.documentElement.setAttribute('data-abvsl','A')}})()</script>"""

VSL_BLOQUE = """<div class="vab"></div><style>
.vab h2{font-weight:800;font-size:1.5rem;line-height:1.2;color:#1F1A33;text-align:center;margin:2px 0 6px}.vab h2 b{color:#4E9A78}
.vab p.vsub{text-align:center;color:#4B4560;margin:0 0 10px;font-size:1rem}
.vslw{margin:6px 0 4px}.vslbox{position:relative;width:100%;max-width:380px;margin:0 auto;aspect-ratio:9/16;border-radius:14px;overflow:hidden;background:#000;box-shadow:0 10px 28px rgba(0,0,0,.22)}
.vslbox video{display:block;width:100%;height:100%;object-fit:cover;background:#000}
.vslprog{position:absolute;left:0;right:0;bottom:0;height:5px;background:rgba(255,255,255,.28);pointer-events:none}.vslprog i{display:block;height:100%;width:0;background:#6E4FD0;transition:width .3s linear}
.vslsnd{position:absolute;inset:0;width:100%;border:0;background:rgba(0,0,0,.12);cursor:pointer;display:flex;align-items:flex-start;justify-content:center;padding-top:9%;font-family:inherit}
.vslsnd b{display:inline-flex;align-items:center;gap:9px;background:#6E4FD0;color:#fff;font-size:16px;font-weight:800;padding:14px 20px;border-radius:999px;box-shadow:0 10px 26px rgba(0,0,0,.4)}
.vslsnd[hidden]{display:none}.vslpau{position:absolute;inset:0;display:none;align-items:center;justify-content:center;pointer-events:none}
.vslpau span{width:78px;height:78px;border-radius:50%;background:rgba(0,0,0,.55);color:#fff;display:grid;place-items:center;font-size:32px;padding-left:5px}
.vslbox.pausa .vslpau{display:flex}.vslnota{text-align:center;color:#6B6480;font-size:.9rem;margin:10px 0 0}
.vslmsc{display:none;text-align:center;color:#C2410C;font-weight:800;margin:12px 0 0}
body:not(.vsl-ok) .quiz-html:has(.vab)~*{display:none!important}body.vsl-ok .vslmsc{display:block}body.vsl-ok .vslnota{display:none}
</style><script>(function(){
var C=(window.CONFIG_QUIZ||{});
var w=document.querySelector('.vab');if(!w||w.__ok)return;w.__ok=1;
// Sin video cargado no se esconde la oferta: se muestra entera.
if(!C.VSL_MP4){document.body.classList.add('vsl-ok');w.style.display='none';return}
var EXP=C.VSL_EXPERTA||'nuestra especialista';
w.innerHTML='<h2>\\u2705 Tu plan est\\u00e1 <b>listo</b></h2><p class="vsub">Lo que tus respuestas dicen de tu cuerpo, explicado por '+EXP+'.</p>'+
'<div class="vslw"><div class="vslbox"><video playsinline webkit-playsinline muted autoplay preload="auto" disablepictureinpicture controlslist="nodownload noplaybackrate nofullscreen" poster="'+(C.VSL_POSTER||'')+'" src="'+C.VSL_MP4+'"></video>'+
'<div class="vslpau"><span>\\u25b6</span></div><div class="vslprog"><i></i></div><button class="vslsnd" type="button"><b>\\ud83d\\udd0a Toca para activar el sonido</b></button></div>'+
'<p class="vslnota">\\ud83d\\udd12 Sigue mirando el video para desbloquear tu plan</p><p class="vslmsc">\\u26a0\\ufe0f Lugares que quedan a este precio: <b class="vsln">7</b></p></div>';
var V=w.querySelector('video'),box=w.querySelector('.vslbox'),snd=w.querySelector('.vslsnd'),pb=w.querySelector('.vslprog i');
var UNLOCK=C.VSL_UNLOCK||216.6,DUR=C.VSL_DURACION||263.9,on=false,KEY='nv_vsl_ok';
function reveal(){if(on)return;on=true;document.body.classList.add('vsl-ok');try{sessionStorage.setItem(KEY,'1')}catch(e){}
var n=w.querySelector('.vsln');setTimeout(function(){n.textContent='6'},8000);setTimeout(function(){n.textContent='5'},19000)}
try{if(sessionStorage.getItem(KEY)==='1')reveal()}catch(e){}
setTimeout(reveal,(UNLOCK+25)*1000);V.addEventListener('error',reveal);
V.addEventListener('timeupdate',function(){var d=V.duration||DUR,x=Math.min(V.currentTime/d,1);pb.style.width=(100*(1-Math.pow(1-x,2.2)))+'%';if(V.currentTime>=UNLOCK)reveal()});
V.addEventListener('ended',function(){pb.style.width='100%';reveal()});
V.addEventListener('pause',function(){if(snd.hidden&&!V.ended)box.classList.add('pausa')});V.addEventListener('play',function(){box.classList.remove('pausa')});
var p=V.play();if(p&&p.catch)p.catch(function(){});
snd.addEventListener('click',function(){V.muted=false;if(V.currentTime<15)V.currentTime=0;V.play();snd.hidden=true});
V.addEventListener('click',function(){if(V.paused)V.play();else V.pause()});
})()</script>"""


def main():
    trabajo, salida = sys.argv[1], sys.argv[2]
    os.makedirs(salida, exist_ok=True)

    D = json.load(open(os.path.join(trabajo, "quiz-data.json"), encoding="utf-8"))
    spec = D["spec"]

    # --- textos ---------------------------------------------------------
    walk(spec)
    faltan = [k for k in TEXTOS if k not in usados]
    if faltan:
        for f in faltan:
            print("NO MATCHEO:", repr(f))
        raise SystemExit("ABORTADO: %d reemplazos no encontraron su texto" % len(faltan))

    fix_iconos(spec)

    PRECIO = "US$ 9,99"
    PRECIO_ANTES = "US$ 29,99"
    fix_precios(spec, PRECIO, PRECIO_ANTES)

    # --- bloques html ---------------------------------------------------
    fuera = 0
    for step in spec["steps"]:
        keep = []
        for b in step.get("blocks", []):
            if b.get("id") in BLOQUES_FUERA:
                fuera += 1
                continue
            if b.get("id") == "nvb_asig":
                b["text"] = AB_ASIG
            elif b.get("id") == "nvr_vsl":
                b["text"] = VSL_BLOQUE
            keep.append(b)
        step["blocks"] = keep
    assert fuera == len(BLOQUES_FUERA), f"esperaba sacar {len(BLOQUES_FUERA)} bloques, saque {fuera}"

    # --- checkout: uno solo, del CONFIG ---------------------------------
    quitados = 0
    for step in spec["steps"]:
        o = step.get("outcome")
        if isinstance(o, dict) and o.pop("target", None) is not None:
            quitados += 1
    assert quitados == 4, f"esperaba 4 targets del competidor, encontre {quitados}"

    # --- imagenes: data URI ---------------------------------------------
    fin = os.path.join(trabajo, "final")
    mapa = {}
    for nombre in sorted(os.listdir(fin)):
        mapa[nombre.replace(".webp", "")] = data_uri(os.path.join(fin, nombre))

    bruto = json.dumps(spec, ensure_ascii=False)
    reemplazadas = 0
    for clave, uri in mapa.items():
        patron = re.compile(r'"https://[^"]*?' + re.escape(clave.split("-", 1)[-1]
                            if clave != "logo" else "logo") + r'[^"]*?"')
        bruto, n = patron.subn(json.dumps(uri, ensure_ascii=False), bruto)
        reemplazadas += n
    spec = json.loads(bruto)

    sueltas = re.findall(r'https://[^"]*?\.(?:webp|png|jpe?g)', json.dumps(spec, ensure_ascii=False))
    assert not sueltas, f"quedaron URLs del competidor: {sueltas[:3]}"

    theme = dict(D["theme"])
    theme["logoUrl"] = mapa["logo"]

    salida_data = {
        "quizId": "",
        "slug": "reseteo-nervio-vago-28-latam",
        "spec": spec,
        "theme": theme,
        "checkoutBase": "__CHECKOUT__",
        "supabaseUrl": "",
        "supabaseKey": "",
        "preview": False,
        "edit": False,
    }

    json.dump(spec, open(os.path.join(salida, "spec-latam.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    css = open(os.path.join(trabajo, "css-q-home.C17Cvys6.css"), encoding="utf-8").read()
    runtime = open(os.path.join(trabajo, "script3.js"), encoding="utf-8").read()

    assert runtime.count(PROGRESO_VIEJO) == 1, "no encontre el progressBar del motor"
    runtime = runtime.replace(PROGRESO_VIEJO, PROGRESO_NUEVO)

    datos = json.dumps(salida_data, ensure_ascii=False).replace("</script>", "<\\/script>")

    frag = PLANTILLA.replace("@@CSS@@", css)
    frag = frag.replace("@@DATOS@@", datos)
    frag = frag.replace("@@RUNTIME@@", runtime)
    frag = frag.replace("@@PRECIO@@", PRECIO).replace("@@PRECIO_ANTES@@", PRECIO_ANTES)

    with open(os.path.join(salida, "nervio-vago-quiz.txt"), "w", encoding="utf-8") as fh:
        fh.write(frag)
    with open(os.path.join(salida, "PRUEBA.html"), "w", encoding="utf-8") as fh:
        fh.write('<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">'
                 '<meta name="viewport" content="width=device-width,initial-scale=1">'
                 "<title>Reseteo del Nervio Vago 28 — LATAM</title></head><body "
                 'style="margin:0">' + frag + "</body></html>")

    kb = os.path.getsize(os.path.join(salida, "nervio-vago-quiz.txt")) / 1024
    print("OK  %d textos al neutro · %d imagenes embebidas · %d bloques del competidor fuera"
          % (len(usados), reemplazadas, fuera))
    print("    %s  (%.0f KB)" % (os.path.join(salida, "nervio-vago-quiz.txt"), kb))


PLANTILLA = """<!-- ===================================================================
     RESETEO DEL NERVIO VAGO 28 — quiz LATAM (espanol neutro)
     Pegar entero en el custom_html de la tienda de ImpulTienda.

     >>> CONFIGURACION: lo unico que se toca esta aca abajo. <<<
     ==================================================================== -->
<script>
window.CONFIG_QUIZ = {
  // Checkout. Unico lugar donde vive la URL: los 4 CTAs de la ultima slide la
  // leen de aca y le enganchan los UTMs y los click id de la URL.
  CHECKOUT: "https://resetnervio-vago.impultienda.ar/checkout",

  // Pixel de Meta. Vacio = no dispara nada.
  PIXEL_ID: "",

  // Carril B (quiz corto de 5 preguntas + VSL). Queda APAGADO hasta que haya
  // VSL propio: con AB_VSL en true y un VSL_MP4 cargado, el trafico se reparte
  // 50/50 entre el quiz largo y el quiz corto con video.
  AB_VSL: false,
  VSL_MP4: "",
  VSL_POSTER: "",
  VSL_EXPERTA: "nuestra especialista",
  VSL_UNLOCK: 216.6,     // segundo del video en que aparece la oferta
  VSL_DURACION: 263.9
};
</script>
<!-- ================= fin de la configuracion ========================= -->

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" media="print" onload="this.media='all'"
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap">
<noscript><link rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap"></noscript>

<style>
@@CSS@@
.quiz-wrap img{max-width:100%;height:auto}
.quiz-btn{text-align:center}
/* La metrica es DESREGULACION: mas alto = peor. El gradiente del motor viene
   rojo->verde (sirve para metricas donde mas es mejor) y dejaba el verde sobre
   "Alto", o sea pintaba de "bien" el riesgo. Se invierte: verde en Bajo,
   rojo en Alto. */
.quiz-gauge{background:linear-gradient(90deg,#10b981,#f59e0b 50%,#ef4444)!important}
</style>

<main class="quiz-wrap" style="--quiz-accent:#6E4FD0;--quiz-bg:#F7F5FB">
  <div id="quiz-root" class="quiz-root"></div>
</main>

<script id="quiz-data" type="application/json">@@DATOS@@</script>

<script>
/* Pixel de Meta (el motor dispara InitiateCheckout al tocar un CTA). */
(function(){var id=(window.CONFIG_QUIZ||{}).PIXEL_ID;if(!id)return;
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init',id);fbq('track','PageView')})();

/* Checkout del CONFIG + UTMs de la URL en la sesion (lo que lee el motor). */
(function(){try{
  var el=document.getElementById('quiz-data');var D=JSON.parse(el.textContent);
  D.checkoutBase=(window.CONFIG_QUIZ||{}).CHECKOUT||'/checkout';

  var q=new URLSearchParams(location.search),u={};
  ['utm_source','utm_medium','utm_campaign','utm_content','utm_term','utm_adset','utm_id',
   'fbclid','gclid','ttclid','msclkid','twclid','xcod','sck'].forEach(function(k){
     if(q.get(k))u[k]=q.get(k)});
  try{var p=JSON.parse(sessionStorage.getItem('impultienda_utm')||'{}');
      for(var k in p)if(!(k in u))u[k]=p[k];
      sessionStorage.setItem('impultienda_utm',JSON.stringify(u))}catch(e){}

  /* Las fotos van una sola vez de data URI a Blob URL: un blob se cachea y se
     decodifica una vez sola, un data URI se vuelve a decodificar en cada paso.
     Si la tienda bloqueara blob: por CSP, el listener de error devuelve la
     imagen a su data URI y el quiz no se queda sin fotos. */
  window.IMGRAW={};window.__pre=[];
  var txt=JSON.stringify(D),vistas={},i=0;
  txt=txt.replace(/data:image\\/[a-z+]+;base64,[A-Za-z0-9+\\/=]+/g,function(uri){
    if(vistas[uri])return vistas[uri];
    try{
      var c=uri.split(',')[1],m=uri.slice(5,uri.indexOf(';')),bin=atob(c),
          arr=new Uint8Array(bin.length);
      for(var j=0;j<bin.length;j++)arr[j]=bin.charCodeAt(j);
      var b=URL.createObjectURL(new Blob([arr],{type:m}));
      window.IMGRAW[b]=uri;vistas[uri]=b;i++;return b;
    }catch(e){return uri}
  });
  window.__preTotal=i;
  el.textContent=txt;

  Object.keys(window.IMGRAW).forEach(function(b){
    var im=new Image();im.src=b;window.__pre.push(im);
    if(im.decode)im.decode().catch(function(){});
  });
  document.addEventListener('error',function(ev){
    var t=ev.target;
    if(t&&t.tagName==='IMG'&&t.src.indexOf('blob:')===0&&window.IMGRAW[t.src])
      t.src=window.IMGRAW[t.src];
  },true);
}catch(e){}})();
</script>

<script>@@RUNTIME@@</script>
"""


if __name__ == "__main__":
    main()
