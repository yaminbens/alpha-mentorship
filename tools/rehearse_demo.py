"""Rehearse the external educational browser model; preserve actual observations."""
from pathlib import Path
import json,math,csv,hashlib
import numpy as np
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parent.parent
P=R/'meetings/01_introduction/presets';P.mkdir(parents=True,exist_ok=True)
F=R/'meetings/01_introduction/fallback';F.mkdir(exist_ok=True)
D=R/'data/examples';D.mkdir(parents=True,exist_ok=True)
rng=np.random.default_rng(31)
xy=np.array([[1.5+1.12*i+0.56*(j%2),2+1.12*math.sqrt(3)/2*j] for j in range(8) for i in range(8)])
v=rng.normal(size=(64,2));v-=v.mean(axis=0);v*=math.sqrt(.05/(np.sum(v*v)/128))
state='MD state data\nN = 64\nSize = 12\nGravity = 0\ndt = 0.005\nSteps per frame = 25\nx\ty\tvx\tvy\n'+'\n'.join('\t'.join(f'{z:.6f}' for z in [*a,*b]) for a,b in zip(xy,v))+'\n'
(P/'ordered_initial.txt').write_text(state)
records=[]; frames=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(args=['--no-sandbox'])
 page=b.new_page(ignore_https_errors=True,viewport={'width':1050,'height':1000})
 page.on('dialog',lambda d:d.dismiss())
 page.goto('https://physics.weber.edu/schroeder/md/',wait_until='domcontentloaded')
 source_hash=hashlib.sha256(page.content().encode()).hexdigest()
 for name,clicks in [('low',0),('middle',8),('middle_repeat',8),('high',24)]:
  page.evaluate('(s)=>{running=false;dataArea.value=s;inputState();for(let i=0;i<1000;i++)doStep();computeStats();}',state)
  # Identical initial preparation, then documented speed-control intervention.
  page.evaluate('(n)=>{for(let i=0;i<n;i++)speedFactor(1.1);for(let i=0;i<1000;i++)doStep();reset();}',clicks)
  samples=page.evaluate('''()=>{let out=[];for(let j=0;j<40;j++){for(let i=0;i<25;i++)doStep();computeStats();out.push({time:time,T:kineticE/N,U:potentialE/N,E:(kineticE+potentialE)/N});}paintCanvas();showStats();return out;}''')
  snapshot=page.evaluate('()=>({xy:x.slice(0,N).map((a,i)=>[a,y[i]]),T:kineticE/N,U:potentialE/N,dt:Number(dtSlider.value),N,boxWidth,fixedCount,bondCount,fixedT:fixedTList.length})')
  vals=np.array([[x['T'],x['U'],x['E']] for x in samples])
  record={'condition':name,'faster_clicks':clicks,'velocity_factor':1.1**clicks,'N':64,'L':12,'settle_steps':1000,'window_steps':1000,'dt':snapshot['dt'],'T_mean':float(vals[:,0].mean()),'U_per_particle_mean':float(vals[:,1].mean()),'E_range':float(np.ptp(vals[:,2])),'flags':[]}
  if not np.isfinite(vals).all():record['flags'].append('NONFINITE')
  records.append(record)
  with (D/f'browser_{name}.csv').open('w') as f:
   writer=csv.DictWriter(f,fieldnames=['time','T','U','E'],lineterminator='\n');writer.writeheader();writer.writerows(samples)
  page.evaluate('showState()');(P/f'{name}_observed.txt').write_text(page.locator('#dataArea').input_value())
  page.locator('canvas').first.screenshot(path=str(F/f'{name}.png'))
  frames.append(snapshot['xy'])
 # Actual browser animation captured from the high-energy state, accelerated playback is labelled.
 from PIL import Image,ImageDraw
 import io
 images=[]
 for i in range(30):
  page.evaluate('for(let i=0;i<50;i++)doStep();paintCanvas();computeStats();showStats();')
  im=Image.open(io.BytesIO(page.locator('canvas').first.screenshot())).convert('RGB')
  draw=ImageDraw.Draw(im);draw.rectangle((0,0,im.width,25),fill='white');draw.text((8,6),'Schroeder browser model | accelerated recording',fill='black');images.append(im)
 images[0].save(F/'demonstration.gif',save_all=True,append_images=images[1:],duration=100,loop=0)
 b.close()
meta={'source':'https://physics.weber.edu/schroeder/md/','page_sha256_at_rehearsal':source_hash,'date':'2026-11-15','preparation':'64 triangular positions, seeded velocities at initial kinetic T=0.05; 1000 steps before energy intervention','units':'sigma=epsilon=m=k_B=1','records':records,'interpretation':'Short teaching observations; no equilibrium phase assignment. middle_repeat is a deterministic replay, not an independent seed.','recording':'30 browser canvas frames, 50 simulation steps between frames, played at 10 frames/s. Recording begins after high condition.'}
(P/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n');(D/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(records,indent=2))
