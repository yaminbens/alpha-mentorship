"""Build a Hebrew, self-contained presentation and printable mentor guide.

Figures reuse recorded classroom data; no new simulation is performed.
Requires Playwright/Chromium in addition to the course's plotting/Markdown tools.
"""
from pathlib import Path
import base64, html, io, json, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import markdown
from playwright.sync_api import sync_playwright

R=Path(__file__).resolve().parent.parent
M=R/'meetings/01_introduction'
TEAL='#087f83'; INK='#172f39'; GOLD='#edaf59'; PAPER='#faf7ef'

def uri(data, mime='image/png'):
    return 'data:'+mime+';base64,'+base64.b64encode(data).decode()

def photo(name):
    return uri((M/'fallback'/f'{name}.png').read_bytes())

def chart(kind):
    fig,ax=plt.subplots(figsize=(7,3.8),facecolor=PAPER)
    ax.set_facecolor(PAPER)
    if kind=='potential':
        r=np.linspace(.96,3,250); u=4*(r**-12-r**-6)
        ax.plot(r,u,color=TEAL,lw=4);ax.axhline(0,color='#aaa',lw=1)
        ax.set(xlabel='Separation / sigma',ylabel='Pair energy / epsilon',ylim=(-1.2,2))
    elif kind=='energy':
        d=np.genfromtxt(R/'data/examples/window_averages.csv',delimiter=',',names=True,dtype=None,encoding='utf8')
        ax.scatter(d['T_reduced'],d['U_per_particle'],s=140,color=TEAL,edgecolor=INK)
        ax.set(xlabel='Measured k_B T / epsilon',ylabel='Potential energy / (N epsilon)')
    else:
        d=np.genfromtxt(R/'data/examples/browser_high.csv',delimiter=',',names=True)
        ax.plot(d['time'],d['T'],lw=3,color=TEAL)
        ax.scatter(d['time'][0],d['T'][0],s=160,color=GOLD,zorder=3)
        ax.set(xlabel='Time / reduced unit',ylabel='Instantaneous k_B T / epsilon')
    ax.spines[['top','right']].set_visible(False)
    ax.tick_params(labelsize=13);ax.xaxis.label.set_size(14);ax.yaxis.label.set_size(14)
    ax.grid(alpha=.15);fig.tight_layout(pad=1.4)
    b=io.BytesIO();fig.savefig(b,format='png',dpi=160);plt.close(fig)
    return uri(b.getvalue())

def atoms():
    dots=[]
    for j in range(5):
        for i in range(6):
            x=45+55*i+(j%2)*12;y=40+53*j
            dots.append(f'<circle cx="{x}" cy="{y}" r="{12+(i+j)%4}" fill="{TEAL if i<3 else GOLD}"/>')
    return '<svg viewBox="0 0 390 300" role="img" aria-label="איור של חלקיקים בשני צבעים">'+''.join(dots)+'</svg>'

def image(src,alt):return f'<img src="{src}" alt="{alt}">'

visuals=[
    '<div class="atom-hero">'+atoms()+'<p>לשאול · להתבונן · לבדוק</p></div>',
    '<div class="photos"><figure>'+image(photo('low'),'מצב מהדגמת המודל באנרגיה נמוכה')+'<figcaption>לפני הוספת אנרגיה</figcaption></figure><figure>'+image(photo('high'),'מצב מהדגמת המודל לאחר הוספת אנרגיה')+'<figcaption>אחרי הוספת אנרגיה</figcaption></figure></div><p class="caption">הצבע מציין מהירות, לא סוג אטום. תצפיות קצרות מהמודל — לא קביעת פאזה בשיווי משקל</p>',
    image(chart('potential'),'גרף אנרגיית הזוג כתלות במרחק, לפי מודל לנארד־ג׳ונס')+'<div class="formula" dir="ltr">U(r) = 4ε [(σ/r)¹² − (σ/r)⁶]</div><p class="caption">r — מרחק; σ — סולם אורך; ε — סולם אנרגיה. משוואת המודל, לא נתון נמדד.</p>',
    image(chart('energy'),'ממוצעי אנרגיה וטמפרטורה מההדגמה הקצרה')+'<p class="caption">כל נקודה: ממוצע של 40 קריאות לאורך 5 יחידות זמן של המודל. החזרה עשויה לחפוף לנקודה המקורית.</p>',
    '<div class="regions"><div><b>אזור א׳</b><span>מה אנחנו רואים כאן?</span></div><div><b>אזור ב׳</b><span>מה זה עוזר לנו לדעת שם?</span></div></div>'+atoms()+'<p class="caption">איור בלבד. בודקים קשר בעזרת תצפיות רבות שנאספו בתנאים מוגדרים.</p>',
    image(chart('fluctuations'),'טמפרטורה רגעית לאורך חלון תצפית קצר בהדגמה')+'<p class="caption">סדרת תצפיות אמיתית מתוך ההדגמה. נקודה בודדת אינה כל הסיפור.</p>',
    '<div class="steps"><div><b>01</b>תחזית<span>מה אני מצפה שיקרה?</span></div><div><b>02</b>תצפית<span>מה קרה בפועל?</span></div><div><b>03</b>הסבר<span>מה הנתונים תומכים בו?</span></div></div>',
    '<div class="demo">'+image(photo('high'),'תצפית מההדגמה, לקראת מעבר להדמיה החיה')+'<div class="badge">מנחשים לפני שמפעילים</div></div>',
    '<div class="notebook"><div class="notebook-bar">המחברת האישית שלי</div><p>התחזית שלי: אם אכפיל את המספר, אז…</p><pre dir="ltr"><span>▶</span> scale = 1.0\n<span>▶</span> scale = 2.0</pre><div class="mini-bars"><i></i><i></i><i></i><i></i><i></i></div><p class="caption">איור של תרגול המחברת — הנתונים בתרגיל מומצאים</p></div>',
    '<div class="homework"><div><small>קודם מתבוננים</small><b>משימה 1</b><span>20–30 דקות · שני צילומים ושאלה</span></div><div><small>אחר כך מודדים</small><b>משימה 2</b><span>60–90 דקות · אפשר בשני חלקים</span></div></div><a class="site-link" href="https://yaminbens.github.io/alpha-mentorship/" dir="ltr">yaminbens.github.io/alpha-mentorship</a>'
]
phases=['היכרות · 0–8','מחקר · 8–9:30','מחקר · 9:30–11','מחקר · 11–13','מחקר · 13–15','מחקר · 15–16:30','מחקר · 16:30–18','הדגמה · 18–30','Colab · 30–50','המשך הדרך · 50–60']
sections=re.split(r'^## ',(M/'slides.md').read_text(),flags=re.M)[1:]
assert len(sections)==10
slides=[]
for idx,section in enumerate(sections):
    lines=section.splitlines();title=re.sub(r'^\d+\. ','',lines[0]);items=[x[2:] for x in lines if x.startswith('- ')]
    prompt=next(x[2:] for x in lines if x.startswith('> '))
    source=('Schroeder (2015) · doi:10.1119/1.4901185' if idx in (1,2,3,5,7) else 'Olah · Visual Information Theory' if idx==4 else 'אלפא · מתחילים לחקור')
    slides.append(f'''<section class="slide slide-{idx+1}" aria-label="שקף {idx+1}: {html.escape(title)}">
    <header><span>אלפא / מאטומים לשאלה מחקרית</span><span>{phases[idx]}</span></header>
    <h1>{html.escape(title)}</h1><div class="body"><div class="words"><ul>{''.join('<li>'+html.escape(x)+'</li>' for x in items)}</ul></div><div class="visual">{visuals[idx]}</div></div>
    <div class="question"><span>שאלה אליכם</span>{html.escape(prompt)}</div>
    <footer><span>{source}</span><span>{idx+1:02d} / 10</span></footer></section>''')
css='''
*{box-sizing:border-box} :root{--ink:#172f39;--teal:#087f83;--paper:#faf7ef;--gold:#edaf59}
html,body{margin:0;background:#172f39;color:var(--ink);font-family:"DejaVu Sans",Arial,sans-serif}
.slide{width:1280px;height:720px;background:var(--paper);padding:30px 52px 24px;position:relative;overflow:hidden;display:none;transform-origin:top left}
.slide.active{display:block} header,footer{display:flex;justify-content:space-between;align-items:center;font-size:15px;color:#53696b} header{border-bottom:1px solid #d7dfd8;padding-bottom:15px}
h1{font-size:48px;line-height:1.2;margin:26px 0 18px;font-weight:700;letter-spacing:-1.1px}
.body{display:grid;grid-template-columns:40% 57%;gap:3%;height:405px;align-items:center}.words ul{padding:0 24px 0 0;margin:0}.words li{font-size:27px;line-height:1.55;margin:0 0 20px;padding-right:5px}.words li::marker{color:var(--teal)}
.visual{text-align:center;max-height:405px}.visual>img{width:100%;max-height:340px;object-fit:contain}.caption{font-size:14px;color:#53696b;line-height:1.5;margin:8px 10px}
.question{position:absolute;bottom:66px;left:52px;right:52px;border-right:6px solid var(--gold);padding:15px 22px;background:#e8f0e9;font-size:25px;line-height:1.3;display:flex;gap:20px;align-items:center}.question>span{font-size:14px;color:var(--teal);white-space:nowrap;font-weight:700}
footer{position:absolute;bottom:24px;left:52px;right:52px;font-size:12px}.photos{display:flex;gap:18px}.photos figure{margin:0;flex:1}.photos img{width:100%;height:260px;object-fit:contain;background:#fff;border-radius:18px;padding:10px}.photos figcaption{font-size:20px;margin-top:8px}
.formula{font-size:22px;margin-top:-10px}.atom-hero svg{width:90%;height:300px}.atom-hero p{font-size:27px;color:var(--teal);font-weight:700}
.slide-1 h1{font-size:61px}.slide-1{background:linear-gradient(135deg,#faf7ef 70%,#e6efdf)}
.regions{display:flex;gap:18px}.regions>div{width:50%;padding:14px;background:#e6eeeb;border-radius:18px;border-top:5px solid var(--teal)}.regions>div+div{border-color:var(--gold)}.regions b{font-size:29px;display:block}.regions span{font-size:17px}.slide-5 .visual>svg{height:205px;width:80%}
.steps{display:flex;gap:14px}.steps>div{flex:1;background:#e8efe9;border-radius:22px;padding:24px 12px;font-size:29px;font-weight:700}.steps b{display:block;color:var(--teal);font-size:49px;margin-bottom:20px}.steps span{display:block;font-size:17px;line-height:1.5;margin-top:20px;font-weight:400}
.demo{position:relative}.demo img{height:355px;max-width:100%;border-radius:20px}.badge{position:absolute;bottom:16px;left:35px;background:var(--gold);padding:12px 18px;border-radius:30px;font-size:22px}
.notebook{background:white;border:1px solid #d9e2db;border-radius:22px;overflow:hidden;text-align:right}.notebook-bar{background:#e6eeeb;padding:12px 24px;font-size:20px;font-weight:700}.notebook p{margin:14px 24px;font-size:19px}.notebook pre{background:#f3f5f1;padding:16px 30px;font-size:25px;line-height:1.6;text-align:left;margin:0 20px}.notebook pre span{color:var(--teal)}.mini-bars{height:70px;display:flex;align-items:end;gap:20px;padding:10px 45px}.mini-bars i{display:block;width:50px;background:var(--teal);height:65%}.mini-bars i:nth-child(2n){height:100%;background:var(--gold)}.mini-bars i:nth-child(3){height:80%}.notebook p.caption{font-size:13px}
.homework{display:flex;gap:18px}.homework>div{flex:1;background:#e8efe9;border-radius:22px;padding:27px 12px}.homework small{font-size:18px}.homework b{display:block;font-size:38px;margin:18px 0}.homework span{font-size:18px;line-height:1.6;display:block}.site-link{display:block;margin-top:30px;color:var(--teal);font-size:23px;text-decoration:underline}
.controls{position:fixed;bottom:9px;left:14px;display:flex;gap:8px;z-index:10;direction:rtl}.controls button{font:15px Arial;padding:8px 13px;color:#fff;background:#203e49;border:1px solid #8ba2aa;border-radius:8px;cursor:pointer}.controls button:focus-visible{outline:3px solid var(--gold)}
@page{size:1280px 720px;margin:0}@media print{html,body{background:white} .slide,.slide.active{display:block!important;transform:none!important;break-after:page} .slide:last-child{break-after:auto}.controls{display:none}}
'''
js='''let current=0; const slides=[...document.querySelectorAll('.slide')];
function fit(){let scale=Math.min(innerWidth/1280,(innerHeight-48)/720);slides.forEach(s=>s.style.transform=`scale(${scale})`);}
function show(n){current=Math.max(0,Math.min(slides.length-1,n));slides.forEach((s,i)=>{s.classList.toggle('active',i===current);s.setAttribute('aria-hidden',i!==current)});location.hash=String(current+1);fit();}
document.querySelector('#next').onclick=()=>show(current+1);document.querySelector('#prev').onclick=()=>show(current-1);
document.querySelector('#full').onclick=()=>{if(document.fullscreenElement)document.exitFullscreen();else document.documentElement.requestFullscreen?.();};
document.addEventListener('keydown',e=>{if(['ArrowLeft','ArrowRight','ArrowDown','ArrowUp',' '].includes(e.key)&&e.target.tagName!=='BUTTON'){e.preventDefault();show(current+(['ArrowLeft','ArrowDown',' '].includes(e.key)?1:-1));}});
addEventListener('resize',fit);let start=Number(location.hash.slice(1));show(Number.isFinite(start)&&start>0?start-1:0);
'''
document='<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>אלפא — מאטומים לשאלה מחקרית</title><style>'+css+'</style></head><body>'+''.join(slides)+'<div class="controls"><button id="prev">הקודם →</button><button id="next">← הבא</button><button id="full">מסך מלא</button></div><script>'+js+'</script></body></html>'
(M/'slides.html').write_text(document)
guide=markdown.markdown((M/'facilitator_plan_he.md').read_text(),extensions=['tables'])
guide_css='''body{font-family:"DejaVu Sans",Arial,sans-serif;direction:rtl;color:#172f39;max-width:1050px;margin:35px auto;line-height:1.75;font-size:17px;padding:0 30px}h1{font-size:32px}h2{font-size:22px;color:#087f83;break-after:avoid;margin-top:30px}table{border-collapse:collapse;width:100%;font-size:14px}td,th{border:1px solid #d3ded9;padding:9px;text-align:right}th{background:#e8efe9}tr{break-inside:avoid}a{overflow-wrap:anywhere;color:#087f83}li{margin-bottom:7px}@page{size:A4;margin:17mm}@media print{body{font-size:11pt;line-height:1.6;margin:0;padding:0}h1{font-size:22pt}h2{font-size:16pt}table{font-size:9pt}}'''
(M/'facilitator_plan_he.html').write_text('<!doctype html><html lang="he" dir="rtl"><meta charset="utf-8"><title>סדר המפגש — אלפא</title><style>'+guide_css+'</style><body>'+guide+'</body></html>')
with sync_playwright() as pw:
    b=pw.chromium.launch(args=['--no-sandbox'])
    page=b.new_page(viewport={'width':1280,'height':768})
    page.goto((M/'slides.html').as_uri());page.evaluate('document.fonts.ready')
    page.pdf(path=str(M/'slides.pdf'),print_background=True,prefer_css_page_size=True)
    page.goto((M/'facilitator_plan_he.html').as_uri());page.evaluate('document.fonts.ready')
    page.pdf(path=str(M/'facilitator_plan_he.pdf'),print_background=True,prefer_css_page_size=True)
    b.close()
print('Built 10 Hebrew slides (HTML/PDF) and Hebrew facilitator guide (HTML/PDF).')
