"""Render six editable Markdown slide sections to a readable PDF with model figures."""
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
R=Path(__file__).resolve().parent.parent
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
pdfmetrics.registerFont(TTFont('DejaVu',FONT))
S=R/'meetings/01_introduction/slides.md'
if not S.exists():
 S.write_text('''# Alpha research introduction

## 1. Materials from atoms
- Solids and liquids can contain the same kinds of atoms.
- Arrangement and motion help us describe their behaviour.
- Prediction: what changes when we add energy?

## 2. Rules make motion
- Positions determine forces; forces change motion.
- Particles attract at moderate separation and repel at short separation.
- A model is a useful simplification with assumptions.

## 3. A movie becomes evidence
- Record settings, temperature, energy and neighbours.
- Keep the comparison fair: fixed particle count and box.
- Energy per particle is not a direct measure of structural order.

## 4. Connection to our research
- How does atomic arrangement connect to material behaviour?
- How much can knowing one region tell us about another?
- Machine learning is one possible tool to investigate these relationships.

## 5. Many observations matter
- One configuration is one observation.
- Fluctuations and preparation history matter.
- Mutual information describes a distribution, not one snapshot.

## 6. Your first experiment
- Predict, observe, record, repeat and explain.
- Today: one guided demonstration and your first saved notebook.
- At home: compare three energy preparations and share your evidence.

Sources: Schroeder (2015), doi:10.1119/1.4901185; Olah, Visual Information Theory.
Model diagrams are illustrations; no physical phase boundary is claimed.
''')
sections=re.split(r'^## ',S.read_text(),flags=re.M)[1:]
c=canvas.Canvas(str(S.with_suffix('.pdf')),pagesize=(960,540))
for idx,section in enumerate(sections):
 lines=section.splitlines();title=lines[0];bullets=[x[2:] for x in lines[1:] if x.startswith('- ')]
 c.setFillColor(HexColor('#f6f3eb'));c.rect(0,0,960,540,fill=1,stroke=0)
 c.setFillColor(HexColor('#182f38'));c.setFont('DejaVu',13);c.drawString(50,495,'ALPHA  /  MOLECULAR SIMULATION')
 c.setFont('DejaVu',30);c.drawString(50,430,title)
 c.setFont('DejaVu',21)
 for j,line in enumerate(bullets):
  words=line.split();wrapped=[];current=''
  for word in words:
   proposed=(current+' '+word).strip()
   if pdfmetrics.stringWidth(proposed,'DejaVu',21)>825:wrapped.append(current);current=word
   else:current=proposed
  wrapped.append(current)
  for k,text in enumerate(wrapped):c.drawString(62,350-j*72-k*27,('• ' if k==0 else '  ')+text)
 if idx==0:
  for label,xpos,name in [('Low energy',65,'low'),('High energy',260,'high')]:
   path=R/f'meetings/01_introduction/fallback/{name}.png'
   if path.exists():c.drawImage(str(path),xpos,55,140,140)
   c.setFillColor(HexColor('#53666a'));c.setFont('DejaVu',10);c.drawString(xpos,43,label)
  c.drawString(550,90,'Actual short model observations')
  c.drawString(550,74,'No equilibrium phase assignment')
 elif idx in (1,2,4):
  fig,ax=plt.subplots(figsize=(4.2,1.55));fig.patch.set_facecolor('#f6f3eb');ax.set_facecolor('#f6f3eb')
  if idx==1:
   rr=np.linspace(.96,3,200);u=4*(rr**-12-rr**-6)
   ax.plot(rr,u,color='#096e68');ax.axhline(0,color='gray',lw=.5)
   ax.set(xlabel='Separation / sigma',ylabel='Pair energy / epsilon',ylim=(-1.2,2))
  elif idx==2:
   data=np.genfromtxt(R/'data/examples/window_averages.csv',delimiter=',',names=True,dtype=None,encoding='utf8')
   ax.scatter(data['T_reduced'],data['U_per_particle'],color='#096e68')
   ax.set(xlabel='Measured k_B T / epsilon',ylabel='Potential energy / (N epsilon)')
  else:
   data=np.genfromtxt(R/'data/examples/browser_high.csv',delimiter=',',names=True)
   ax.plot(data['time'],data['T'],color='#096e68')
   ax.set(xlabel='Reduced time',ylabel='Instantaneous k_B T / epsilon')
  ax.tick_params(labelsize=7);ax.xaxis.label.set_size(8);ax.yaxis.label.set_size(8)
  fig.tight_layout(pad=.6);buf=io.BytesIO();fig.savefig(buf,format='png',dpi=180);plt.close(fig);buf.seek(0)
  c.drawImage(ImageReader(buf),65,48,390,144)
  c.setFillColor(HexColor('#53666a'));c.setFont('DejaVu',12)
  caption={1:'The model specifies interactions.',2:'Each point needs its preparation and window.',4:'Measured fluctuations in a short example.'}[idx]
  c.drawString(490,112,caption)
 elif idx==3:
  c.setFont('DejaVu',14)
  for j in range(2):
   c.setFillColor(HexColor('#096e68' if j==0 else '#b65a28'))
   for k in range(6):c.circle(100+j*270+(k%3)*35,90+(k//3)*35,8,fill=1,stroke=0)
  c.setFillColor(HexColor('#53666a'));c.drawString(220,110,'Predict?')
  c.drawString(520,110,'Illustration: many paired observations needed')
 elif idx==5:
  c.setFillColor(HexColor('#096e68'));c.setFont('DejaVu',20)
  c.drawString(70,110,'Predict  →  Observe  →  Record  →  Explain  →  Share')
 c.setFillColor(HexColor('#53666a'));c.setFont('DejaVu',10)
 c.drawString(50,30,'Schroeder (2015), doi:10.1119/1.4901185 · Olah, Visual Information Theory')
 c.drawRightString(910,30,f'{idx+1} / 6');c.showPage()
c.save();print('Built slides.pdf')
