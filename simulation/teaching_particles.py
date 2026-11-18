"""Small independent-particle teaching models; not an interacting molecular fluid.

Box length = 1 model-length unit, time in model-time units, mass = 1.
Mixing: free motion, elastic walls, a central wall with a configurable opening.
Bouncing: constant downward acceleration, restitution at horizontal walls.
Vertical impacts are resolved at their event times. A rebound below 0.001
model-speed units at the floor is treated as contact to resolve inelastic collapse.
"""
import json
import uuid
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import HTML, display


def reflect_coordinate(x, v, dt):
    """Elastic motion on [0, 1], including multiple crossings in one step."""
    unfolded = np.asarray(x) + np.asarray(v) * dt
    phase = unfolded % 2.0
    position = np.where(phase <= 1, phase, 2 - phase)
    velocity = np.where(phase < 1, v, -np.asarray(v))
    # Exactly at a wall, choose the outgoing velocity.
    velocity = np.where(position == 0, np.abs(velocity), velocity)
    velocity = np.where(position == 1, -np.abs(velocity), velocity)
    return position, velocity


def vertical_step(y, v, dt, gravity, restitution):
    remaining = float(dt)
    while remaining > 1e-12:
        if gravity > 0 and y <= 1e-12 and 0 <= v < 0.001:
            return 0.0, 0.0
        candidates = []
        for wall in (0.0, 1.0):
            if gravity == 0:
                roots = [(wall-y)/v] if v != 0 else []
            else:
                discriminant = v*v + 2*gravity*(y-wall)
                roots = [] if discriminant < 0 else [(v-np.sqrt(discriminant))/gravity, (v+np.sqrt(discriminant))/gravity]
            for t in roots:
                incoming = v-gravity*t
                if t > 1e-12 and t <= remaining+1e-12 and ((wall == 0 and incoming < 0) or (wall == 1 and incoming > 0)):
                    candidates.append((t,wall))
        # An initial condition already on a wall may point outwards.
        if y <= 1e-12 and v < 0:
            v = -restitution*v
            continue
        if y >= 1-1e-12 and v > 0:
            v = -restitution*v
            continue
        if not candidates:
            return y+v*remaining-0.5*gravity*remaining**2, v-gravity*remaining
        t,wall = min(candidates)
        y = wall
        v = -restitution*(v-gravity*t)
        remaining = max(0.0, remaining-t)
    return y,v


def mixing_run(opening=1.0, speed=0.3, seed=7):
    if not (0 <= opening <= 1 and 0.05 <= speed <= 1):
        raise ValueError('opening בין 0 ל־1; speed בין 0.05 ל־1')
    rng = np.random.default_rng(seed)
    n,dt,steps = 40,0.02,500
    labels = np.repeat([0,1],n//2)
    pos = rng.uniform(0.08,0.92,(n,2))
    pos[:,0] = rng.uniform(0.08,0.42,n)+0.5*labels
    angle = rng.uniform(0,2*np.pi,n)
    vel = speed*np.column_stack((np.cos(angle),np.sin(angle)))
    frames,times = [pos.copy()],[0.0]
    for step in range(1,steps+1):
        old = pos.copy()
        trial = old+vel*dt
        crossed = (old[:,0]-0.5)*(trial[:,0]-0.5) < 0
        for i in np.flatnonzero(crossed):
            fraction = (0.5-old[i,0])/(trial[i,0]-old[i,0])
            y_cross = old[i,1]+fraction*(trial[i,1]-old[i,1])
            if abs(y_cross-0.5) >= opening/2:
                trial[i,0] = 1-trial[i,0]
                vel[i,0] *= -1
        for axis in (0,1):
            pos[:,axis],vel[:,axis] = reflect_coordinate(trial[:,axis],vel[:,axis],0)
        if step % 5 == 0:
            frames.append(pos.copy());times.append(step*dt)
    positions = np.array(frames)
    fraction = (positions[:,labels==0,0]>0.5).mean(axis=1)
    return dict(positions=positions,time=np.array(times),labels=labels,opening=opening,
                measure=fraction,measure_name='Blue fraction on right',
                settings=dict(model='noninteracting mixing',opening=opening,speed=speed,seed=seed,dt=dt,N=n,duration=steps*dt))


def bounce_run(restitution=1.0, gravity=1.0, seed=7):
    if not (0 <= restitution <= 1 and 0 <= gravity <= 3):
        raise ValueError('restitution בין 0 ל־1; gravity בין 0 ל־3')
    rng=np.random.default_rng(seed)
    n,dt,steps=24,0.02,400
    pos=np.column_stack((rng.uniform(.08,.92,n),rng.uniform(.55,.9,n)))
    vel=np.column_stack((rng.uniform(-.15,.15,n),np.zeros(n)))
    frames,times,energy=[pos.copy()],[0.0],[np.mean(0.5*vel[:,1]**2+gravity*pos[:,1])]
    for step in range(1,steps+1):
        pos[:,0],vel[:,0]=reflect_coordinate(pos[:,0],vel[:,0],dt)
        for i in range(n):
            pos[i,1],vel[i,1]=vertical_step(pos[i,1],vel[i,1],dt,gravity,restitution)
        if step % 5 == 0:
            frames.append(pos.copy());times.append(step*dt)
            energy.append(np.mean(0.5*vel[:,1]**2+gravity*pos[:,1]))
    positions=np.array(frames)
    return dict(positions=positions,time=np.array(times),labels=np.arange(n)%2,opening=None,
                measure=positions[:,:,1].mean(axis=1),measure_name='Mean height',energy=np.array(energy),
                settings=dict(model='independent bouncing particles',restitution=restitution,gravity=gravity,seed=seed,dt=dt,N=n,duration=steps*dt,contact_speed=0.001))


def animation_html(result, title='סימולציית חלקיקים'):
    ident='animation_'+uuid.uuid4().hex
    data=json.dumps(dict(positions=np.asarray(result['positions']).round(5).tolist(),
                        time=np.asarray(result['time']).round(3).tolist(),
                        labels=np.asarray(result['labels']).tolist(),opening=result.get('opening')))
    import html
    return '''<!doctype html><html lang="he" dir="rtl"><meta charset="utf-8">
<div id="'''+ident+'''" style="font:16px system-ui;max-width:560px;background:#f5f8fa;padding:16px;color:#203246">
<strong>'''+html.escape(title)+'''</strong><br>
<canvas width="500" height="500" style="width:100%;max-width:500px;background:white" aria-label="תנועת חלקיקים בקופסה"></canvas>
<div><button type="button" class="play">ניגון / עצירה</button> <button type="button" class="reset">להתחלה</button>
<input class="timeline" type="range" min="0" value="0" aria-label="זמן בסימולציה" style="width:45%"><output></output><br><label><input class="trails" type="checkbox"> הצגת מסלולים</label></div>
<p style="font-size:13px">אפשר לגרור את מחוון הזמן. הצבעים מסמנים קבוצות חלקיקים; הם אינם טמפרטורה.</p></div>
<script>(()=>{const root=document.getElementById("'''+ident+'''"),d='''+data+''';
const canvas=root.querySelector('canvas'),ctx=canvas.getContext('2d'),slider=root.querySelector('.timeline'),out=root.querySelector('output'),trails=root.querySelector('.trails');trails.checked=d.positions[0].length===1;
slider.max=d.positions.length-1;let running=false;
function draw(){const k=Number(slider.value);ctx.clearRect(0,0,500,500);ctx.strokeStyle='#26394b';ctx.lineWidth=2;ctx.strokeRect(15,15,470,470);
if(d.opening!==null&&d.opening<1){ctx.beginPath();ctx.moveTo(250,15);ctx.lineTo(250,250-235*d.opening);ctx.moveTo(250,250+235*d.opening);ctx.lineTo(250,485);ctx.stroke();}
if(trails.checked){d.positions[0].forEach((_,i)=>{ctx.strokeStyle=d.labels[i]===0?'#8fbfc4':'#dcb296';ctx.lineWidth=1;ctx.beginPath();for(let j=0;j<=k;j++){const p=d.positions[j][i];if(j===0)ctx.moveTo(15+470*p[0],485-470*p[1]);else ctx.lineTo(15+470*p[0],485-470*p[1]);}ctx.stroke();});}
d.positions[k].forEach((p,i)=>{ctx.fillStyle=d.labels[i]===0?'#087e8b':'#c56732';ctx.beginPath();ctx.arc(15+470*p[0],485-470*p[1],5,0,Math.PI*2);ctx.fill();});out.textContent='זמן: '+d.time[k];}
root.querySelector('.play').onclick=()=>running=!running;root.querySelector('.reset').onclick=()=>{running=false;slider.value=0;draw();};slider.oninput=()=>{running=false;draw();};trails.onchange=draw;
const timer=setInterval(()=>{if(!root.isConnected){clearInterval(timer);return;}if(running){slider.value=(Number(slider.value)+1)%d.positions.length;draw();}},80);draw();})();</script></html>'''


def show_result(result, stem, title):
    """Display and save an animation, static figure, measurements and conditions."""
    document=animation_html(result,title)
    Path(stem+'.html').write_text(document,encoding='utf-8')
    display(HTML(document))
    fig,axes=plt.subplots(1,3,figsize=(10,3.4))
    colors=np.where(np.array(result['labels'])==0,'#087e8b','#c56732')
    for ax,k in zip(axes,[0,len(result['time'])//2,len(result['time'])-1]):
        xy=result['positions'][k];ax.scatter(xy[:,0],xy[:,1],c=colors,s=18)
        if result.get('opening') is not None:
            gap=result['opening'];ax.plot([.5,.5],[0,.5-gap/2],color='gray');ax.plot([.5,.5],[.5+gap/2,1],color='gray')
        ax.set(xlim=(0,1),ylim=(0,1),xlabel='x / model length',ylabel='y / model length',title=f"t = {result['time'][k]:.1f}");ax.set_aspect('equal')
    fig.tight_layout();fig.savefig(stem+'.png',dpi=130);plt.show();plt.close(fig)
    np.savetxt(stem+'.csv',np.column_stack((result['time'],result['measure'])),delimiter=',',header='time,'+result['measure_name'],comments='')
    Path(stem+'_settings.json').write_text(json.dumps(result['settings'],ensure_ascii=False,indent=2),encoding='utf-8')
    print('נשמרו קבצים בשם',stem,': אנימציה html, תמונה png, נתונים csv ותנאים settings.json. הורידו אותם מתיקיית הקבצים ב־Colab.')
