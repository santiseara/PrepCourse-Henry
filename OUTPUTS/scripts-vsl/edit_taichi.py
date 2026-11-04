#!/usr/bin/env python3
"""Editor del VSL de Tai Chi Fit. Render por segmentos en paralelo (regla 4f)."""
import json, os, re, subprocess, sys, unicodedata
from concurrent.futures import ThreadPoolExecutor

W   = os.path.expanduser("~/Desktop/tai-chi-fit/vsl/work")
TMP = os.environ.get("VSL_TMP", "/tmp") + "/taichi_tmp"
FF  = os.path.expanduser("~/bin/ffmpeg")
BASE, CLIPS, GFX = W+"/base.mp4", W+"/clips", W+"/gfx"
NUCLEOS = int(os.environ.get("NUCLEOS", "6"))
FONT = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
os.makedirs(TMP, exist_ok=True)

def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^\w]", "", s)

WORDS = json.load(open(W+"/words.json"))

def _corregir_con_guion():
    """Reemplaza lo que oyo Whisper por las palabras del guion (difflib), como el editor de la wiki."""
    import difflib
    gui = []
    for b in ["b1","b2a","b2b","b3"]:
        f = W + "/vo/" + b + ".txt"
        if os.path.exists(f): gui += open(f, encoding="utf-8").read().split()
    if not gui: return
    a = [norm(w["w"]) for w in WORDS]
    b = [norm(g) for g in gui]
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal" or (op == "replace" and (i2-i1) == (j2-j1)):
            for k in range(i2-i1):
                WORDS[i1+k]["w"] = gui[j1+k]
        elif op == "replace" and "".join(a[i1:i2]) == "".join(b[j1:j2]):
            # Whisper pego o partio palabras ("corro yo" -> "corroyo"): el texto es el mismo
            WORDS[i1]["w"] = " ".join(gui[j1:j2])
            for k in range(i1+1, i2):
                WORDS[k]["w"] = ""
_corregir_con_guion()
TOKS  = [norm(w["w"]) for w in WORDS]

def ancla(frase):
    o = [norm(x) for x in frase.split() if norm(x)]; n = len(o)
    hits = [i for i in range(len(TOKS)-n+1) if TOKS[i:i+n] == o]
    if not hits: raise SystemExit("ANCLA NO ENCONTRADA: " + frase)
    if len(hits) > 1: print("  aviso: ancla repetida x%d -> %s" % (len(hits), frase))
    return WORDS[hits[0]]["t0"]

# ---------- plan ----------
BROLLS = [
    ("c03", 4.0,  4.5), ("c01", "pararse en un pie", 4.0), ("c08", "un manuscrito", 4.0),
    ("c04", "yo lo llamo tu raiz", 4.0), ("c07", "un cuerpo que vive en alerta", 4.0),
    ("c03", "cansada de empezar el lunes", 4.0), ("c04", "una dieta nunca te va a devolver", 4.0),
    ("c01", "y el gimnasio tampoco", 4.0), ("c08", "la primera se llama raiz", 4.5),
    ("c07", "la segunda se llama fluir", 4.5), ("c03", "la tercera se llama grulla", 4.5),
    ("c04", "por dia en tu casa descalza", 4.0), ("c01", "se llama tai chi fit", 4.0),
    ("c08", "y tenes dos caminos", 4.0),
]
PLACAS = [
    ("bono1", "la guia de respiracion", 3.6), ("bono2", "alivio oriental", 3.6),
    ("bono3", "el te termogenico", 3.6), ("bono4", "el nivel maestra", 3.6),
    ("bono5", "tu hoja de ruta", 3.6), ("total", "los cinco juntos son", 4.0),
    ("precio", "pero hoy en esta pagina", 5.0), ("garantia", "y el riesgo lo", 4.2),
    ("cta", "te esta esperando", 4.5),
]
USO = {}   # tramo distinto cada vez que se repite un clip
def tramo(c, dur):
    i = USO.get(c, 0); USO[c] = i + 1
    d = float(subprocess.run([FF.replace("ffmpeg","ffprobe")] if False else
        [FF, "-i", CLIPS+"/"+c+".mp4"], capture_output=True, text=True).stderr.split("Duration: ")[1].split(",")[0].split(":")[-1])
    return 1.5 + i * (dur + 2.0)

def construir():
    b = []
    for c, a, dur in BROLLS:
        t0 = a if isinstance(a, float) else ancla(a)
        b.append({"tipo": "broll", "clip": c, "t0": round(t0, 2), "t1": round(t0+dur, 2), "ss": tramo(c, dur)})
    for g, a, dur in PLACAS:
        t0 = ancla(a) if isinstance(a, str) else a
        b.append({"tipo": "placa", "gfx": g, "t0": round(t0, 2), "t1": round(t0+dur, 2)})
    b.sort(key=lambda x: x["t0"])
    for i in range(len(b)-1):
        if b[i]["t1"] > b[i+1]["t0"]:
            b[i]["t1"] = round(b[i+1]["t0"] - 0.15, 2)
    return [x for x in b if x["t1"] - x["t0"] > 0.8]

# ---------- subtitulos ----------
CLAVE = {"raiz","raíz","fluir","grulla","equilibrio","firme","suelta","liviana","gratis","garantia",
         "garantía","maestra","veintiocho","28","hoy","nunca","dieta","gimnasio","error","tres","cuerpo"}
def ass(plan, dur):
    cab = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\n\n"
     "[V4+ Styles]\nFormat: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,"
     "Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,"
     "MarginL,MarginR,MarginV,Encoding\n"
     "Style: N,Arial Black,86,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,7,3,2,40,40,430,1\n"
     "Style: A,Arial Black,86,&H0000D7FF,&H0000D7FF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,7,3,2,40,40,430,1\n\n"
     "[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n")
    def t(x):
        h=int(x//3600); m=int(x%3600//60); s=x%60
        return "%d:%02d:%05.2f" % (h, m, s)
    ev=[]; i=0
    while i < len(WORDS):
        grupo = WORDS[i:i+2]
        txt = " ".join(g["w"] for g in grupo).upper().strip()
        if not txt: i += 2; continue
        est = "A" if any(norm(g["w"]) in {norm(k) for k in CLAVE} for g in grupo) else "N"
        t0, t1 = grupo[0]["t0"], grupo[-1]["t1"]
        if t1 - t0 > 2.2: t1 = t0 + 2.2
        ev.append("Dialogue: 0,%s,%s,%s,,0,0,0,,%s" % (t(t0), t(max(t1, t0+0.25)), est, txt))
        i += 2
    open(TMP+"/subs.ass","w").write(cab + "\n".join(ev) + "\n")

def subs_recorte(a, b, out):
    src = open(TMP+"/subs.ass").read().split("[Events]")
    cab, ev = src[0] + "[Events]" + src[1].split("\n")[0], src[1].split("\n")[1:]
    def seg(x):
        p=x.split(":"); return int(p[0])*3600+int(p[1])*60+float(p[2])
    def t(x):
        h=int(x//3600); m=int(x%3600//60); s=x%60; return "%d:%02d:%05.2f"%(h,m,s)
    keep=[]
    for l in ev:
        if not l.startswith("Dialogue"): continue
        f=l.split(",",4); s0,s1=seg(f[1]),seg(f[2])
        if s1 < a or s0 > b: continue
        keep.append("%s,%s,%s,%s,%s" % (f[0], t(max(s0,a)-a), t(min(s1,b)-a), f[3], f[4]))
    open(out,"w").write(cab+"\n"+"\n".join(keep)+"\n")

# ---------- render ----------
def duracion(f):
    o = subprocess.run([FF,"-i",f], capture_output=True, text=True).stderr
    d = o.split("Duration: ")[1].split(",")[0]
    h,m,s = d.split(":"); return int(h)*3600+int(m)*60+float(s)

def render(args):
    idx, a, b, item = args
    out = "%s/s%03d.mp4" % (TMP, idx)
    if os.path.exists(out) and os.environ.get("REUSAR"): return out
    sub = "%s/s%03d.ass" % (TMP, idx); subs_recorte(a, b, sub)
    dur = b - a
    if item and item["tipo"] == "broll":
        cl = CLIPS + "/" + item["clip"] + ".mp4"
        ss = min(item["ss"], max(0.5, duracion(cl) - dur - 0.5))
        cmd = [FF,"-y","-ss",str(a),"-t",str(dur),"-i",BASE,"-ss",str(ss),"-t",str(dur),"-stream_loop","-1","-i",cl,
               "-filter_complex",
               "[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,"
               "fade=t=in:st=0:d=0.25,fade=t=out:st=%.2f:d=0.25[v];[v]ass=%s[o]" % (dur-0.25, sub),
               "-map","[o]","-an"]
    elif item and item["tipo"] == "placa":
        g = GFX + "/" + item["gfx"] + ".png"
        y = 1180 if item["gfx"] not in ("garantia",) else 980
        cmd = [FF,"-y","-ss",str(a),"-t",str(dur),"-i",BASE,"-loop","1","-t",str(dur),"-i",g,
               "-filter_complex",
               "[1:v]format=rgba,fade=t=in:st=0:d=0.3:alpha=1,fade=t=out:st=%.2f:d=0.3:alpha=1[g];"
               "[0:v][g]overlay=(W-w)/2:%d:shortest=1[v];[v]ass=%s[o]" % (dur-0.3, y, sub),
               "-map","[o]","-an"]
    else:
        cmd = [FF,"-y","-ss",str(a),"-t",str(dur),"-i",BASE,"-vf","ass="+sub,"-an"]
    cmd += ["-c:v","libx264","-crf","20","-preset","veryfast","-pix_fmt","yuv420p","-r","30",out]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out

def main():
    dur = duracion(BASE)
    plan = construir()
    json.dump(plan, open(W+"/plan.json","w"), indent=1, ensure_ascii=False)
    print("plan: %d eventos (%d b-rolls, %d placas)" % (len(plan),
          sum(1 for x in plan if x["tipo"]=="broll"), sum(1 for x in plan if x["tipo"]=="placa")))
    ass(plan, dur)
    cortes = [0.0]
    for x in plan: cortes += [x["t0"], x["t1"]]
    cortes.append(dur); cortes = sorted(set(round(c,2) for c in cortes if 0 <= c <= dur))
    tareas = []
    for i in range(len(cortes)-1):
        a, b = cortes[i], cortes[i+1]
        if b - a < 0.12: continue
        it = next((x for x in plan if x["t0"] <= a + 0.01 and x["t1"] >= b - 0.01), None)
        tareas.append((len(tareas), a, b, it))
    print("segmentos:", len(tareas))
    with ThreadPoolExecutor(max_workers=NUCLEOS) as ex:
        outs = list(ex.map(render, tareas))
    outs = [o for o in outs if os.path.exists(o) and os.path.getsize(o) > 1000]
    print("renderizados:", len(outs), "de", len(tareas))
    lst = TMP+"/lista.txt"
    open(lst,"w").write("\n".join("file '%s'" % o for o in outs))
    mudo = TMP+"/mudo.mp4"
    subprocess.run([FF,"-y","-f","concat","-safe","0","-i",lst,"-c","copy",mudo],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # audio: voz + cama -8 dB relativa
    sal = os.path.expanduser("~/Desktop/tai-chi-fit/vsl/Tai-Chi-Fit-VSL.mp4")
    subprocess.run([FF,"-y","-i",mudo,"-i",BASE,"-stream_loop","-1","-i",W+"/music_bed.wav",
        "-filter_complex",
        "[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,loudnorm=I=-15:TP=-1.5,asplit=2[voz1][voz2];"
        "[2:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,loudnorm=I=-23,volume=-8dB[mus];"
        "[mus][voz2]sidechaincompress=threshold=0.05:ratio=6:attack=20:release=400[duck];"
        "[voz1][duck]amix=inputs=2:duration=first:dropout_transition=0,alimiter=limit=0.95[a]",
        "-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-shortest",sal],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("SALIDA:", sal, round(duracion(sal),1), "s" if os.path.exists(sal) else "FALLO")

if __name__ == "__main__":
    main()
