"""Build six research slides, three activity slides and three scientific appendices.

Saved teaching data and labelled schematics only: this builder runs no simulation.
The HTML embeds its figures and licensed Hebrew font for offline presentation.
"""
from pathlib import Path
import base64,html,io,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import markdown
from playwright.sync_api import sync_playwright
from presentation_figures import configuration,neighbours,force_pair,FIRST,LATER

R=Path(__file__).resolve().parent.parent
M=R/'meetings/01_introduction'
COURSE='https://yaminbens.github.io/alpha-mentorship/'

def uri(data,mime):return 'data:'+mime+';base64,'+base64.b64encode(data).decode()
font_uri=uri((R/'vendor/fonts/NotoSansHebrew.ttf').read_bytes(),'font/ttf')
font_css='@font-face{font-family:NotoHebrew;src:url("'+font_uri+'");font-weight:100 900;font-display:block}'

def chart(kind):
    fig,ax=plt.subplots(figsize=(8.2,3.8));color='#146d75'
    if kind=='potential':
        r=np.linspace(.96,3,250);ax.plot(r,4*(r**-12-r**-6),color=color,lw=3)
        ax.axhline(0,color='#9aa7b2',lw=1)
        ax.set(xlabel='Separation r / sigma',ylabel='Pair energy U / epsilon',ylim=(-1.2,2))
    elif kind=='energy':
        d=np.genfromtxt(R/'data/examples/window_averages.csv',delimiter=',',names=True,dtype=None,encoding='utf8')
        for name,tx,uy in zip(d['condition'],d['T_reduced'],d['U_per_particle']):
            repeat=name=='middle_repeat'
            ax.scatter(tx,uy,s=160 if repeat else 80,marker='x' if repeat else 'o',color='#a65d36' if repeat else color,label='middle repeat' if repeat else name)
        ax.set(xlabel='Mean k_B T / epsilon',ylabel='Mean U / (N epsilon)');ax.legend(frameon=False,fontsize=12)
    else:
        d=np.genfromtxt(R/'data/examples/browser_high.csv',delimiter=',',names=True)
        ax.plot(d['time'],d['T'],color=color,lw=2.5)
        ax.set(xlabel='Time / reduced unit',ylabel='Instantaneous k_B T / epsilon')
    ax.spines[['top','right']].set_visible(False);ax.tick_params(labelsize=13)
    ax.xaxis.label.set_size(14);ax.yaxis.label.set_size(14);ax.grid(axis='y',alpha=.16)
    fig.tight_layout(pad=1);b=io.BytesIO();fig.savefig(b,format='svg');plt.close(fig)
    return '<img class="chart" src="'+uri(b.getvalue(),'image/svg+xml')+'" alt="'+{'potential':'אנרגיית זוג לפי נוסחת המודל','energy':'ממוצעי הטמפרטורה והאנרגיה בהדגמה','fluctuations':'תנודות בטמפרטורה לאורך חלון תצפית'}[kind]+'">'

low=configuration(M/'presets/low_observed.txt');high=configuration(M/'presets/high_observed.txt')

def panel(title,visual,caption=''):
    return '<figure><figcaption>'+title+'</figcaption>'+visual+('<p class="figure-note">'+caption+'</p>' if caption else '')+'</figure>'

def link(path,text):return '<a href="'+COURSE+path+'">'+text+'</a>'

stages=[
    '<div class="pair configurations">'+panel('הכנה באנרגיה נמוכה',low,'ללא תוספת מהירות')+panel('הכנה באנרגיה גבוהה',high,'לאחר 24 לחיצות Faster')+'</div><p class="takeaway">שני מצבים של אותו מודל: <bdi>N = 64</bdi>, קופסה באורך <bdi>L = 12</bdi> ביחידות המודל.</p>',
    '<div class="pair forces">'+panel('מרחק קצר: דחייה',force_pair(True))+panel('מרחק בינוני: משיכה',force_pair(False))+'</div><div class="calculation"><span>מיקומים</span><i>←</i><span>כוחות</span><i>←</i><span>שינוי בתנועה</span><i>←</i><span>מיקומים חדשים</span></div><p class="takeaway">המודל כאן דו־ממדי; תכונותיו נקבעות גם על ידי האינטראקציות והגבולות.</p>',
    '<div class="pair neighbours">'+panel('זמן ראשון',neighbours(FIRST),'שכני החלקיק המסומן: <bdi>1, 2, 3, 4</bdi>')+panel('זמן מאוחר יותר',neighbours(LATER),'שכני אותו חלקיק: <bdi>1, 2, 5, 6</bdi>')+'</div><p class="takeaway"><strong>2 מתוך 4 שכנים נשמרו.</strong> כאן ״שכנים״ הם ארבעת החלקיקים הקרובים ביותר.</p>',
    '<div class="protocol"><div class="common">אותו מצב התחלתי שמור · <bdi>N = 64</bdi> · <bdi>L = 12</bdi></div><div class="branches"><div><span>הכנה נמוכה</span><b>0</b><small>לחיצות Faster</small></div><div><span>הכנה בינונית</span><b>8</b><small>לחיצות Faster</small></div><div><span>הכנה גבוהה</span><b>24</b><small>לחיצות Faster</small></div></div><div class="common bottom">אותו זמן הכנה, אותו זמן המתנה ואותו חלון מדידה</div></div><p class="takeaway">חוזרים על ההכנה הבינונית מאותו מצב כדי לבדוק את הליך הביצוע.</p>',
    '<div class="research"><div class="region-figure">'+configuration(M/'presets/low_observed.txt',regions=True)+'<div class="region-labels" dir="ltr"><span>אזור א׳</span><span>אזור ב׳</span></div></div><div class="research-text"><p><b>מה מתעדים?</b>תיאור של המבנה בכל אחד מהאזורים, באותה תצפית.</p><p><b>מה בודקים?</b>האם הכרת אזור אחד מסייעת לתאר את האחר, לאורך אוסף תצפיות?</p><p class="research-tool">למידת מכונה היא כלי אפשרי לחקירת הקשר.</p></div></div>',
    '<div class="research-question"><div class="question-rule"></div><p class="project-question">איך משתנים התנועה והשכנים<br>כאשר מוסיפים אנרגיה?</p></div><dl class="project-scope"><div><dt>משנים</dt><dd>את הכנת האנרגיה, במספר חלקיקים ובקופסה קבועים.</dd></div><div><dt>בשלב הראשון</dt><dd>מתארים תנועה וסידור; משווים טמפרטורה ואנרגיה.</dd></div><div><dt>בהמשך</dt><dd>מגדירים מדד לשינוי בשכנים ואת פרק הזמן להשוואה.</dd></div></dl>',
    '<div class="demo-stage"><div class="demo-procedure"><p><b>לפני ההפעלה</b>רושמים תחזית על התנועה ועל הסידור.</p><p><b>במהלך ההדגמה</b>משווים הכנה נמוכה וגבוהה מאותו מצב שמור.</p><p><b>לאחר ההתבוננות</b>מפרידים בין מה שנראה לבין ההסבר שמציעים.</p><a href="https://physics.weber.edu/schroeder/md/">פתיחת ההדמיה ↗</a></div>'+panel('מצב מההדגמה המתועדת',high)+'</div>',
    '<ol class="colab-steps"><li><b>יצירת עותק אישי</b><span><bdi>File → Save a copy in Drive</bdi> ושינוי שם המחברת.</span></li><li><b>תחזית והרצה</b><span>כותבים מה צפוי לקרות, מריצים ומציגים את הגרף.</span></li><li><b>שינוי פרמטר אחד</b><span>משנים <bdi>scale = 1</bdi> ל־<bdi>scale = 2</bdi> ומריצים שוב.</span></li><li><b>בדיקת שמירה וגישה</b><span>שומרים, פותחים מחדש ומשתפים עם חשבון המנחה.</span></li></ol><p class="activity-link">'+link('task-0.html','פתיחת Task 0 ↗')+'</p>',
    '<table class="homework"><thead><tr><th>שלב</th><th>התוצר</th><th>זמן מתוכנן</th></tr></thead><tbody><tr><td>'+link('task-1.html','משימה 1: תצפית')+'</td><td>תחזית, שני צילומים, תיאור ושאלה להמשך.</td><td>20–30 דקות</td></tr><tr><td>'+link('task-2.html','משימה 2: השוואה')+'</td><td>ארבע הרצות, נתוני מקור, גרף ומסקנה קצרה.</td><td>60–90 דקות</td></tr></tbody></table><div class="submission"><b>להגשה</b><p>קישור למחברת האישית, עם הרשאה למנחה, וקובצי נתונים ותמונות שנשמרו בנפרד.</p>'+link('submit.html','הוראות שמירה והגשה ↗')+'</div>',
    '<div class="appendix-plot">'+chart('potential')+'<div class="equation" dir="ltr">U(r) = 4ε [(σ/r)¹² − (σ/r)⁶]</div><p class="figure-note">r — מרחק; σ — סולם אורך; ε — סולם אנרגיה. זהו גרף אנרגיה, לא גרף כוח.</p></div>',
    '<div class="appendix-plot">'+chart('energy')+'<p class="figure-note">כל ממוצע: 40 קריאות לאורך 5 יחידות זמן, לאחר הכנה והמתנה. החזרה חופפת לנקודה הבינונית.</p></div>',
    '<div class="appendix-plot">'+chart('fluctuations')+'<p class="figure-note">40 קריאות מההכנה באנרגיה גבוהה. חלון קצר אינו מוכיח התכנסות או שיווי משקל.</p></div>'
]
provenance=[
 'תצפיות שמורות מהדגמת Schroeder; אותו קנה מידה. אין קביעה של פאזה בשיווי משקל.',
 'סכמה של אינטראקציה זוגית. נוסחת לנארד־ג׳ונס והגדרות היחידות מופיעות בנספח.',
 'דוגמה סינתטית להמחשת המדידה; אינה תוצאה של ההדמיה.',
 'Faster משנה מהירויות ואינו קובע טמפרטורה. חזרה זהה אינה אומדן לשונות בין הכנות עצמאיות.',
 'חלוקה סכמטית של תצורה שמורה. מוצגת שאלה מחקרית; לא נמדד כאן קשר בין האזורים.',
 'כיוון ראשוני לפרויקט. מדידת השכנים תוגדר בהמשך; אינה דרישה למשימת הבית הראשונה.',
 'הדגמה אחת בהובלת המנחה. מספר חלקיקים וקופסה קבועים; אין צורך לבצע את הניסוי המלא בכיתה.',
 'נתוני התרגול מומצאים. קובצי סביבת ההרצה זמניים ויש לשמור אותם בנפרד.',
 'מועדי ההגשה וערוץ שליחת הקישורים יימסרו במפגש. האתר אינו שומר תשובות.',
 'Schroeder (2015), doi:10.1119/1.4901185. מודל דו־ממדי עם קירות רכים.',
 'נתוני הדגמה בלבד: N=64, L=12, dt=0.005; 1000 צעדי הכנה ו־1000 צעדי המתנה לכל תנאי.',
 'מדידות מתועדות מההדגמה. מידע הדדי מתייחס להתפלגות של תצפיות; הוא אינו מחושב במצגת.'
]
sections=re.split(r'^## ',(M/'slides.md').read_text(),flags=re.M)[1:]
assert len(sections)==len(stages)==12
slides=[]
for i,section in enumerate(sections):
    lines=section.splitlines();title=re.sub(r'^\d+\. ','',lines[0]);lead=next(x[2:] for x in lines if x.startswith('- '))
    group='מבוא למחקר' if i<6 else 'פעילות במפגש' if i<9 else 'נספח מדעי'
    slides.append(f'<section class="slide s{i+1}" aria-label="שקף {i+1}: {html.escape(title)}"><header><span>אלפא · תנועה, מבנה ותכונות החומר</span><span>{group}</span></header><h1>{html.escape(title)}</h1><p class="lead">{html.escape(lead)}</p><div class="stage">{stages[i]}</div><footer><p>{html.escape(provenance[i])}</p><span><bdi>{i+1:02d} / 12</bdi></span></footer></section>')
css='''
*{box-sizing:border-box}html,body{margin:0;background:#e7eaed;color:#203246;font-family:NotoHebrew,Arial,sans-serif}
.slide{width:1280px;height:720px;padding:30px 62px 24px;background:#fff;position:relative;display:none;transform-origin:top left;overflow:hidden}.slide.active{display:block}
header{display:flex;justify-content:space-between;font-size:16px;letter-spacing:.2px;color:#607184;border-bottom:1px solid #d9e0e6;padding-bottom:13px}
h1{font-size:43px;font-weight:650;line-height:1.3;margin:24px 0 10px;letter-spacing:-.4px}.lead{font-size:24px;line-height:1.45;font-weight:400;margin:0;color:#405469}.stage{height:438px;margin-top:18px}
footer{position:absolute;bottom:23px;left:62px;right:62px;display:flex;align-items:start;justify-content:space-between;gap:24px;color:#596c7d;font-size:16px;line-height:1.4;border-top:1px solid #d9e0e6;padding-top:11px}footer p{margin:0;max-width:1030px}footer>span{white-space:nowrap}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:64px;direction:rtl}figure{margin:0;text-align:center}figcaption{font-size:24px;font-weight:600;margin-bottom:5px}.pair svg{width:100%;height:310px}.figure-note{font-size:18px;color:#566b7c;line-height:1.5;margin:5px 0}.takeaway{font-size:23px;text-align:center;line-height:1.5;margin:10px 0 0}.takeaway strong{color:#146d75;font-weight:600}
.forces{padding-top:24px}.forces svg{height:200px}.calculation{display:flex;justify-content:center;gap:30px;align-items:center;font-size:27px;padding:16px 0;border-top:1px solid #d9e0e6;border-bottom:1px solid #d9e0e6;margin:12px 0 22px}.calculation i{font-style:normal;color:#146d75}
.neighbours svg{height:290px}.neighbours .figure-note{font-size:22px}.s3 .takeaway{margin-top:20px}
.protocol{margin:15px 35px 0}.common{text-align:center;background:#f5f7f9;border-top:1px solid #d9e0e6;border-bottom:1px solid #d9e0e6;padding:16px;font-size:24px}.branches{display:grid;grid-template-columns:repeat(3,1fr);gap:0;text-align:center;padding:24px 0}.branches>div+div{border-right:1px solid #d9e0e6}.branches span{font-size:22px;display:block}.branches b{font-size:54px;line-height:1.35;font-weight:500;color:#146d75;display:block}.branches small{font-size:18px;display:block}.s4 .takeaway{font-size:22px;margin-top:22px}
.research{display:grid;grid-template-columns:52% 45%;gap:3%;align-items:center;padding-top:12px}.region-figure svg{height:345px;width:100%}.region-labels{display:flex;justify-content:center;gap:120px;font-size:22px;margin-top:-4px}.region-labels>span:first-child{color:#146d75}.region-labels>span+span{color:#a65d36}.research-text p{font-size:23px;line-height:1.55;margin:0 0 20px}.research-text b{display:block;font-weight:650;margin-bottom:4px}.research-text .research-tool{font-size:21px;color:#566b7c;border-top:1px solid #d9e0e6;padding-top:18px}
.research-question{display:flex;gap:24px;align-items:stretch;padding:10px 0 20px}.question-rule{width:4px;background:#146d75}.project-question{font-size:38px;line-height:1.4;margin:0;font-weight:500}.project-scope{margin:10px 0 0}.project-scope>div{display:grid;grid-template-columns:180px 1fr;border-top:1px solid #d9e0e6;padding:16px 0;gap:24px;font-size:23px}.project-scope dt{font-weight:600;color:#146d75}.project-scope dd{margin:0}
.demo-stage{display:grid;grid-template-columns:47% 50%;gap:3%;align-items:center}.demo-stage svg{height:320px;width:100%}.demo-procedure p{font-size:24px;line-height:1.5;margin:0 0 20px}.demo-procedure b{display:block;font-weight:650;font-size:21px;color:#146d75;margin-bottom:5px}a{color:#146d75;text-underline-offset:5px}.demo-procedure a{font-size:22px}
.colab-steps{counter-reset:steps;list-style:none;padding:0;margin:5px 0 0}.colab-steps li{position:relative;padding:15px 60px 15px 0;border-bottom:1px solid #d9e0e6;display:grid;grid-template-columns:240px 1fr;font-size:23px;gap:18px;line-height:1.5}.colab-steps li:before{counter-increment:steps;content:counter(steps,decimal-leading-zero);position:absolute;right:0;top:15px;color:#146d75;font-size:24px}.colab-steps b{font-weight:600}.activity-link{font-size:24px;margin-top:22px}
.homework{border-collapse:collapse;width:100%;font-size:23px;line-height:1.55;margin-top:12px}.homework td,.homework th{padding:20px 14px;text-align:right;border-bottom:1px solid #d9e0e6}.homework th{font-size:18px;color:#607184;font-weight:500}.homework td:last-child{white-space:nowrap}.submission{padding-top:28px;font-size:23px;line-height:1.5}.submission b{color:#146d75}.submission p{margin:8px 0 15px}
.appendix-plot{text-align:center}.chart{height:340px;max-width:100%}.equation{font-size:26px;margin:0 0 8px}.appendix-plot .figure-note{font-size:20px}.s10 .chart{height:310px}
.controls{position:fixed;bottom:8px;left:18px;display:flex;gap:8px;z-index:10;direction:rtl}.controls button,.controls select{font:15px NotoHebrew,Arial,sans-serif;padding:7px 12px;border:1px solid #aebac4;color:#203246;background:white;cursor:pointer;border-radius:2px}.controls :focus-visible{outline:3px solid #146d75}
@page{size:1280px 720px;margin:0}@media print{html,body{background:white}.slide,.slide.active{display:block!important;transform:none!important;break-after:page}.slide:last-child{break-after:auto}.controls{display:none}}
'''
js='''let current=0;const slides=[...document.querySelectorAll('.slide')];
function fit(){const scale=Math.min(innerWidth/1280,Math.max(1,innerHeight-48)/720);slides.forEach(s=>s.style.transform=`scale(${scale})`);}
function show(n){current=Math.max(0,Math.min(slides.length-1,n));slides.forEach((s,i)=>{s.classList.toggle('active',i===current);s.setAttribute('aria-hidden',i!==current)});location.hash=String(current+1);fit();}
document.querySelector('#next').onclick=()=>show(current+1);document.querySelector('#prev').onclick=()=>show(current-1);
document.querySelector('#section').onchange=e=>{show(Number(e.target.value));e.target.blur()};
document.querySelector('#full').onclick=()=>{if(document.fullscreenElement)document.exitFullscreen();else document.documentElement.requestFullscreen?.();};
document.addEventListener('keydown',e=>{if(e.target.tagName==='SELECT')return;if(['ArrowLeft','ArrowRight','ArrowDown','ArrowUp',' '].includes(e.key)&&!(e.key===' '&&e.target.tagName==='BUTTON')){e.preventDefault();show(current+(['ArrowLeft','ArrowDown',' '].includes(e.key)?1:-1));}});
addEventListener('resize',fit);let start=Number(location.hash.slice(1));show(Number.isFinite(start)&&start>0?start-1:0);
'''
document='<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>אלפא — תנועה, מבנה ותכונות החומר</title><style>'+font_css+css+'</style></head><body>'+''.join(slides)+'<div class="controls"><button id="prev">הקודם →</button><button id="next">← הבא</button><select id="section" aria-label="בחירת חלק במצגת"><option value="0">מבוא למחקר</option><option value="6">פעילויות</option><option value="9">נספח מדעי</option></select><button id="full">מסך מלא</button></div><script>'+js+'</script></body></html>'
(M/'slides.html').write_text(document)
guide=markdown.markdown((M/'facilitator_plan_he.md').read_text(),extensions=['tables'])
guide_css='''body{font-family:"NotoHebrew",Arial,sans-serif;direction:rtl;color:#172f39;max-width:1050px;margin:35px auto;line-height:1.75;font-size:17px;padding:0 30px}h1{font-size:32px}h2{font-size:22px;color:#087f83;break-after:avoid;margin-top:30px}table{border-collapse:collapse;width:100%;font-size:14px}td,th{border:1px solid #d3ded9;padding:9px;text-align:right}th{background:#e8efe9}tr{break-inside:avoid}a{overflow-wrap:anywhere;color:#087f83}li{margin-bottom:7px}@page{size:A4;margin:17mm}@media print{body{font-size:11pt;line-height:1.5;margin:0;padding:0}h1{font-size:22pt}h2{font-size:16pt;margin-top:18px}table{font-size:9pt}}'''
(M/'facilitator_plan_he.html').write_text('<!doctype html><html lang="he" dir="rtl"><meta charset="utf-8"><title>סדר המפגש — אלפא</title><style>'+guide_css+'</style><body>'+guide+'</body></html>')
# The guide shares the embedded font and remains an independent printable document.
p=M/'facilitator_plan_he.html';p.write_text(p.read_text().replace('<style>','<style>'+font_css,1))
with sync_playwright() as pw:
    b=pw.chromium.launch(args=['--no-sandbox']);page=b.new_page(viewport={'width':1280,'height':768})
    page.goto((M/'slides.html').as_uri());page.evaluate('document.fonts.ready')
    page.pdf(path=str(M/'slides.pdf'),print_background=True,prefer_css_page_size=True)
    page.goto((M/'facilitator_plan_he.html').as_uri());page.evaluate('document.fonts.ready')
    page.pdf(path=str(M/'facilitator_plan_he.pdf'),print_background=True,prefer_css_page_size=True)
    b.close()
print('Built 12 slides: 6 research, 3 activity, 3 appendix; embedded Hebrew font; guide HTML/PDF.')
