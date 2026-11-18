import os, sys, json, subprocess
from faster_whisper import WhisperModel
W = int(sys.argv[1]); NW = int(sys.argv[2])
D = os.path.expanduser('~/Desktop/dieta-3-fases/work/ref')
VID, TR = os.path.join(D,'videos'), os.path.join(D,'trans')
os.makedirs(TR, exist_ok=True)
m = WhisperModel('small', device='cpu', compute_type='int8', cpu_threads=2)
fs = [f for f in sorted(os.listdir(VID)) if f.endswith('.mp4')]
for i, f in enumerate(fs):
    if i % NW != W: continue
    out = os.path.join(TR, f[:-4] + '.json')
    if os.path.exists(out): continue
    wav = f'/tmp/_t{W}.wav'
    subprocess.run(['ffmpeg','-y','-v','error','-i',os.path.join(VID,f),'-ar','16000','-ac','1',wav], check=True)
    segs, info = m.transcribe(wav, language='pt', vad_filter=True)
    data = [{'ini': round(s.start,2), 'fin': round(s.end,2), 'txt': s.text.strip()} for s in segs]
    json.dump(data, open(out,'w'), ensure_ascii=False, indent=1)
    print(f, len(data), flush=True)
print('LISTO', W)
