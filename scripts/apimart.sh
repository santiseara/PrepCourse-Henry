#!/usr/bin/env bash
# apimart.sh — cliente de APIMart para el segundo cerebro
# La clave vive en ~/.config/apimart/env (chmod 600) y nunca se imprime.
set -euo pipefail

CONF="$HOME/.config/apimart/env"
BASE="https://api.apimart.ai/v1"
[ -f "$CONF" ] || { echo "No encuentro $CONF. Copiá la clave desde https://apimart.ai/es/keys"; exit 1; }
set -a; . "$CONF"; set +a
AUTH="Authorization: Bearer $APIMART_API_KEY"
JSON="Content-Type: application/json"

api_post() { curl -sS -X POST "$BASE/$1" -H "$AUTH" -H "$JSON" -d "$2"; }
api_get()  { curl -sS "$BASE/$1" -H "$AUTH"; }

saldo() {
  local r; r=$(api_get "models" || true)
  if echo "$r" | grep -q '"data"' && ! echo "$r" | grep -q 'insufficient balance'; then
    echo "$r" | python3 -I -c 'import json,sys;d=json.load(sys.stdin);print("Saldo OK -",len(d.get("data",[])),"modelos disponibles")'
  else
    echo "$r" | sed -n 's/.*current: \([0-9.]*\) USD.*/Saldo actual: \1 USD — cargá créditos en https:\/\/apimart.ai\/es\/pricing/p'
    if echo "$r" | grep -qi 'invalid\|unauthorized'; then echo "La clave no es válida: revisá https://apimart.ai/es/keys"; fi
  fi
}

# manda un body JSON crudo a /videos/generations y devuelve el task_id
video() {
  local body="$1" r tid
  r=$(api_post "videos/generations" "$body")
  tid=$(echo "$r" | python3 -I -c '
import json,sys
d=json.load(sys.stdin)
def dig(o):
    if isinstance(o,dict):
        if "task_id" in o: return o["task_id"]
        for v in o.values():
            x=dig(v)
            if x: return x
    if isinstance(o,list):
        for v in o:
            x=dig(v)
            if x: return x
    return None
t=dig(d)
print(t if t else "ERROR "+json.dumps(d)[:400])')
  echo "$tid"
}

tarea() { api_get "tasks/$1"; }

# espera a que termine y, si se pasa salida, baja el mp4 con reanudación
esperar() {
  local tid="$1" out="${2:-}" r st url
  for i in $(seq 1 120); do
    r=$(tarea "$tid")
    st=$(echo "$r" | python3 -I -c 'import json,sys;d=json.load(sys.stdin);print(json.dumps(d))' | grep -o '"status"[: ]*"[a-z_]*"' | head -1 | cut -d'"' -f4)
    case "$st" in
      completed|succeeded|success)
        url=$(echo "$r" | python3 -I -c '
import json,sys,re
s=sys.stdin.read()
m=re.findall(r"https?://[^\"\\\\ ]+\.(?:mp4|mov|webm)[^\"\\\\ ]*",s)
print(m[0] if m else "")')
        echo "LISTO $url"
        [ -n "$out" ] && [ -n "$url" ] && curl -L -C - -o "$out" "$url" && echo "guardado en $out"
        return 0;;
      failed|error) echo "FALLO: $r"; return 1;;
      *) sleep 10;;
    esac
  done
  echo "Timeout esperando $tid (seguí con: apimart tarea $tid)"; return 1
}

# avatar que habla, voz fija: apimart avatar <foto_url> <voz_url> "<texto>" [seg] [salida.mp4]
avatar() {
  local foto="$1" voz="$2" texto="$3" dur="${4:-5}" out="${5:-}"
  local body; body=$(python3 -I -c '
import json,sys
foto,voz,texto,dur=sys.argv[1:5]
img={"url":foto,"role":"reference_image"}
if voz and voz!="-": img["reference_voice"]=voz
print(json.dumps({"model":"wan2.7-r2v","prompt":texto,"image_with_roles":[img],
 "duration":int(dur),"resolution":"720P","size":"9:16"}))' "$foto" "$voz" "$texto" "$dur")
  local tid; tid=$(video "$body"); echo "task_id: $tid"
  case "$tid" in ERROR*) return 1;; esac
  esperar "$tid" "$out"
}

# b-roll barato: apimart broll "<prompt>" [seg] [salida.mp4]
broll() {
  local prompt="$1" dur="${2:-6}" out="${3:-}"
  local body; body=$(python3 -I -c '
import json,sys
print(json.dumps({"model":"grok-imagine-video","prompt":sys.argv[1],
 "duration":int(sys.argv[2]),"resolution":"720P","size":"9:16"}))' "$prompt" "$dur")
  local tid; tid=$(video "$body"); echo "task_id: $tid"
  case "$tid" in ERROR*) return 1;; esac
  esperar "$tid" "$out"
}

case "${1:-ayuda}" in
  saldo)   saldo;;
  video)   shift; [ "${1:-}" = "-" ] && video "$(cat)" || video "$(cat "$1")";;
  tarea)   shift; tarea "$1";;
  esperar) shift; esperar "$@";;
  avatar)  shift; avatar "$@";;
  broll)   shift; broll "$@";;
  *) cat <<'H'
apimart saldo                                   ver créditos
apimart avatar <foto> <voz|-> "<texto>" [seg] [out.mp4]   wan2.7-r2v, voz fija
apimart broll "<prompt>" [seg] [out.mp4]        grok-imagine-video (el más barato)
apimart video body.json | apimart video -       body crudo a /v1/videos/generations
apimart tarea <task_id>                         estado de la tarea
apimart esperar <task_id> [out.mp4]             espera y baja con curl -C -
H
;;
esac
