#!/bin/bash
# Recorta el avatar de HeyGen contra su fondo (pantalla verde) con Vision de macOS.
# Deja <carpeta>/avatar/<V>_key.mov: ProRes 4444 con alfa, 720x1280.
# Uso: avatar_recortar.sh <carpeta_de_trabajo> V05 V09 ...
# Despues: python3 avatar_ubicar.py <carpeta> <V>   (escribe escala y posicion en el plan)
set -e
D="$1"; shift
SEG=${SEG:-/tmp/segbin}
[ -x "$SEG" ] || swiftc -O -o "$SEG" "$(dirname "$0")/recorte_persona.swift"
cd "$D"
for V in "$@"; do
  rm -rf key/$V; mkdir -p key/$V/f key/$V/m
  ffmpeg -nostdin -v error -y -i avatar/${V}_avatar.mp4 -vf scale=720:1280 -start_number 1 key/$V/f/%05d.png
  echo "cuadros $V: $(ls key/$V/f | wc -l)"
  "$SEG" key/$V/f key/$V/m | tail -1
  # tmix de 3 cuadros contra el parpadeo del borde, gblur + lut para apretar la silueta
  ffmpeg -nostdin -v error -y -framerate 25 -i key/$V/f/%05d.png -framerate 25 -i key/$V/m/%05d.png \
    -filter_complex "[1:v]format=gray,tmix=frames=3,gblur=sigma=0.8,lut=y='clip((val-30)*1.35,0,255)'[a];[0:v][a]alphamerge,format=yuva444p10le[v]" \
    -map "[v]" -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le avatar/${V}_key.mov
  rm -f key/$V/f/*.png
  echo "LISTO $V"
done
