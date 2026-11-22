#!/bin/zsh
# V3, V4 y V6 pasan a voz de hombre (Orus). V1, V2 y V5 quedan con Sulafat.
set -e
W=~/Desktop/ingles-mapas-mentales/anuncios/work
export $(cat ~/.config/herrero/gemini.env | xargs)
export TTS_VOICE=Orus
for n in 3 4 6; do
  mv -f "$W/voz/V$n.wav" "$W/voz/V${n}_mujer.wav" 2>/dev/null || true
  for intento in 1 2 3; do
    if python3 /Users/santiagoseara/PrepCourse-Henry/OUTPUTS/scripts-vsl/tts_gemini.py \
        "$W/voz/V$n.txt" "$W/voz/V$n.wav" "$W/voz/estilo_hombre.txt"; then break; fi
    echo "V$n fallo (intento $intento)"; sleep 20
  done
done
echo FIN
