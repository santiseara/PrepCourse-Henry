"""Inserta un bloque de video (con su propio audio) adentro de otro, en un segundo exacto.
Uso: python3 insertar_bloque.py base.mp4 bloque.mp4 segundo salida.mp4
Reencodea todo a 1080x1920 @30 / aac 48k estéreo para que el pegado no tenga saltos."""
import subprocess, sys, os, tempfile
FF = os.path.expanduser('~/bin/ffmpeg')
base, bloque, seg, out = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4]
tmp = tempfile.mkdtemp(prefix='ins_')
VF = 'scale=1080:1920:flags=lanczos,fps=30,setsar=1'
ENC = ['-c:v','libx264','-crf',os.environ.get('CRF','18'),'-preset',os.environ.get('PRESET','veryfast'),'-pix_fmt','yuv420p',
       '-c:a','aac','-b:a','192k','-ar','48000','-ac','2']
a, b, c = f'{tmp}/a.mp4', f'{tmp}/b.mp4', f'{tmp}/c.mp4'
subprocess.run([FF,'-y','-v','error','-i',base,'-t',f'{seg:.3f}','-vf',VF]+ENC+[a], check=True)
subprocess.run([FF,'-y','-v','error','-i',bloque,'-vf',VF]+ENC+[b], check=True)
subprocess.run([FF,'-y','-v','error','-ss',f'{seg:.3f}','-i',base,'-vf',VF]+ENC+[c], check=True)
lst = f'{tmp}/lista.txt'
open(lst,'w').write(f"file '{a}'\nfile '{b}'\nfile '{c}'\n")
subprocess.run([FF,'-y','-v','error','-f','concat','-safe','0','-i',lst,'-c','copy',out], check=True)
dur = subprocess.run([FF,'-i',out], capture_output=True, text=True).stderr
print('listo:', out, [l for l in dur.splitlines() if 'Duration' in l][0].strip())
