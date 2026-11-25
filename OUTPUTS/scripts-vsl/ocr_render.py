# -*- coding: utf-8 -*-
"""OCR de un render: lista CADA texto por separado (split por ||) y saca solo los mios.
No se filtra por LINEA: una linea mezcla mi subtitulo con el cartel ajeno y lo esconde."""
import os, re, sys, subprocess, glob, collections
SP, VID, GUION = sys.argv[1], sys.argv[2], sys.argv[3]
D = '/Users/santiagoseara/PrepCourse-Henry/OUTPUTS/scripts-vsl'
FF = os.path.expanduser('~/bin/ffmpeg')
tmp = SP + '/_ocr_' + os.path.basename(VID).split('.')[0]; os.system('rm -rf ' + tmp); os.makedirs(tmp)
subprocess.run([FF,'-v','error','-y','-i',VID,'-vf','fps=2,scale=900:-2','-q:v','3',tmp+'/f_%03d.jpg'],check=True)
mios = set(re.sub(r'[^a-z0-9]',' ', open(GUION).read().lower()).split())
mios |= set('instant access tap the button ready to cut categories sheet dollars weekend market plywood '
            'profit calculator day plan first sale svg dxf cdr pdf calibration lightburn settings christmas '
            'playbook bonus collections clock ornament sales machine paid off a at one'.split())
fs = sorted(glob.glob(tmp+'/f_*.jpg'))
o = subprocess.run([D+'/scanbin'], input='\n'.join(fs)+'\n', capture_output=True, text=True).stdout
ajeno = collections.Counter()
for ln in o.strip().split('\n'):
    p = ln.split('\t')
    if len(p) < 3: continue
    seg = int(os.path.basename(p[0])[2:5]) / 2.0
    for t in p[2].split('||'):
        t = t.strip()
        if len(t) < 3: continue
        pal = [w for w in re.sub(r'[^a-z0-9]',' ', t.lower()).split() if len(w) > 1]
        if pal and all(w in mios for w in pal): continue
        ajeno['%s @ %.1fs' % (t[:48], seg)] += 1
for k in ajeno: print(k)
