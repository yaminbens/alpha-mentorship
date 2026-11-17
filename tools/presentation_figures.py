"""Vector teaching figures from saved coordinates or explicitly synthetic diagrams."""
import html
import numpy as np

INK='#203246'; TEAL='#146d75'; COPPER='#a65d36'; GRAY='#c0c9d1'

def svg(body,w=480,h=350,label=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(label)}">{body}</svg>'

def state(path):
    lines=path.read_text().splitlines()
    start=next(i for i,s in enumerate(lines) if s.split()[:4]==['x','y','vx','vy'])+1
    return np.array([[float(v) for v in s.split()[:4]] for s in lines[start:start+64]])

def configuration(path,regions=False):
    data=state(path);body=''
    x0,y0,side=80,10,320
    if regions:
        body+=f'<rect x="80" y="10" width="160" height="320" fill="#edf5f5"/><rect x="240" y="10" width="160" height="320" fill="#f8f1ed"/>'
        body+='<path d="M240 10V330" stroke="#8495a4" stroke-dasharray="5 6"/>'
    body+=f'<rect x="{x0}" y="{y0}" width="{side}" height="{side}" fill="none" stroke="{GRAY}" stroke-width="1.5"/>'
    for x,y,*_ in data:
        color=(TEAL if x<6 else COPPER) if regions else '#50657a'
        body+=f'<circle cx="{x0+x*side/12:.3f}" cy="{y0+(12-y)*side/12:.3f}" r="6.1" fill="{color}"/>'
    return svg(body,label='קואורדינטות חלקיקים שמורות מההדגמה; אותו קנה מידה בשתי ההכנות')

FIRST=np.array([[0,0],[1,0],[0,1],[-1,0],[0,-1],[2,1.6],[-2,-1.6]])
LATER=np.array([[0,0],[1.15,.45],[0,1.15],[-2.1,.5],[0,-2.2],[.75,-1],[-1.2,0]])

def neighbour_ids(points):
    return list(np.argsort(np.linalg.norm(points[1:]-points[0],axis=1))[:4]+1)

def neighbours(points):
    selected=neighbour_ids(points);body='';cx,cy,scale=240,170,65
    for j in selected:
        x,y=points[j];body+=f'<path d="M{cx} {cy}L{cx+x*scale} {cy-y*scale}" stroke="{TEAL}" stroke-width="2"/>'
    for j,(x,y) in enumerate(points):
        px,py=cx+x*scale,cy-y*scale
        fill=COPPER if j==0 else TEAL if j in selected else 'white'
        color='white' if j==0 or j in selected else '#637589'
        body+=f'<circle cx="{px}" cy="{py}" r="19" fill="{fill}" stroke="{GRAY if fill=="white" else fill}" stroke-width="2"/>'
        body+=f'<text x="{px}" y="{py+7}" text-anchor="middle" font-family="NotoHebrew,sans-serif" font-size="21" font-weight="600" fill="{color}">{"i" if j==0 else j}</text>'
    return svg(body,label='דוגמה סינתטית: חלקיק מסומן וארבעת שכניו הקרובים')

def force_pair(repulsive):
    # Distances are schematic, not sampled trajectories.
    a,b=(190,290) if repulsive else (135,345)
    body=f'<defs><marker id="arrow-{int(repulsive)}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{TEAL}"/></marker></defs>'
    for x in [a,b]:body+=f'<circle cx="{x}" cy="105" r="25" fill="{INK}"/>'
    direction=-1 if repulsive else 1
    for x,d in [(a,direction),(b,-direction)]:
        start=x+d*32;end=x+d*98
        body+=f'<path d="M{start} 105H{end}" stroke="{TEAL}" stroke-width="4" marker-end="url(#arrow-{int(repulsive)})"/>'
    return svg(body,h=200,label='דחייה במרחק קצר' if repulsive else 'משיכה במרחק בינוני')
