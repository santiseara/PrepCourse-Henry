#!/bin/zsh
# Voces de la tanda 1 de Ingles con Mapas Mentales (Sulafat, rioplatense).
set -e
W=~/Desktop/ingles-mapas-mentales/anuncios/work
export $(cat ~/.config/herrero/gemini.env | xargs)
export TTS_VOICE=Sulafat
for n in 1 2 3 4 5 6; do
  if [ -s "$W/voz/V$n.wav" ]; then echo "V$n ya esta"; continue; fi
  for intento in 1 2 3; do
    if python3 /Users/santiagoseara/PrepCourse-Henry/OUTPUTS/scripts-vsl/tts_gemini.py \
        "$W/voz/V$n.txt" "$W/voz/V$n.wav" "$W/voz/estilo.txt"; then break; fi
    echo "V$n fallo (intento $intento), espero 20 s"; sleep 20
  done
done
echo FIN
