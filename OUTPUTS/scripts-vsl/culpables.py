import os, re, subprocess, sys, json, collections
W=sys.argv[1]; FF=os.path.expanduser('~/bin/ffmpeg')
MIOS=('MÁS INFORMACIÓN','ACTIVIDADES AB','NATURALISTAS','Toca en','Más información','NATÜRALISTAS')
culp=collections.defaultdict(set)
for n in range(1,7):
    log=open(f'{W}/render.log').read()
    m=re.search(r'planos: (.+)\nOK V%d\.mp4'%n, log)
    if not m: print('sin planos V%d'%n); continue
    orden=[x.split(':')[0] for x in m.group(1).split()]
    # duraciones de los s??.mp4
    tmp=f'{W}/V{n}.mp4_tmp'
    lim=[]; t=0
    for i,k in enumerate(orden):
        p=f'{tmp}/s{i:02d}.mp4'
        if not os.path.exists(p): break
        r=subprocess.run([FF,'-i',p],capture_output=True,text=True).stderr
        mm=re.search(r'Duration: (\d+):(\d+):([\d.]+)',r)
        d=int(mm.group(1))*3600+int(mm.group(2))*60+float(mm.group(3))
        lim.append((t,t+d,k)); t+=d
    # ocr
    out=subprocess.run(['python3','/Users/santiagoseara/PrepCourse-Henry/OUTPUTS/scripts-vsl/ocr_render.py',W,f'{W}/V{n}.mp4',f'{W}/guiones/V{n}.txt'],capture_output=True,text=True).stdout
    for ln in out.strip().split('\n'):
        mm=re.match(r'(.+) @ ([\d.]+)s$', ln.strip())
        if not mm: continue
        txt, ts = mm.group(1).strip(), float(mm.group(2))
        if any(x.lower() in txt.lower() for x in MIOS): continue
        if len(txt)<4: continue
        for a,b,k in lim:
            if a<=ts<b: culp[k].add(txt[:40]); break
for k in sorted(culp, key=lambda x:-len(culp[x])):
    print(k, len(culp[k]), '|', ' // '.join(sorted(culp[k])[:4]))
