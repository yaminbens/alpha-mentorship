"""Build an explicitly selected student book for project-path GitHub Pages hosting."""
from pathlib import Path
import json,re,shutil,html
import markdown
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'dist'
PAGES=[('index','מתחילים כאן'),('task-0','פתיחה · סביבת העבודה'),('task-1','1 · פתיחת מחיצה'),('task-2','2 · חוק הקפיצה'),('task-3','3 · כותבים סימולציה'),('browser','הדגמת המנחה'),('readings','מקורות וקריאה'),('submit','שמירה ושיתוף'),('next','המשך וקריאה')]
DOWNLOADS=['assignments/reflection_he.md','assignments/01_first_experiment/exploration_template.md','assignments/01_first_experiment/results_template.csv','assignments/01_first_experiment/report_template.md','project/proposal_template.md','meetings/01_introduction/student_worksheet_he.md','assignments/01_first_experiment/task_he.md','readings/glossary_en_he.md','readings/questions_he.md']
def site_target(target):
 # Source Markdown uses real repository paths so it is also readable on GitHub.
 path,separator,fragment=target.partition('#')
 mapping={f'{slug}.md':f'{slug}.html' for slug,_ in PAGES}
 mapping.update({'../../'+p:'downloads/'+Path(p).name for p in DOWNLOADS})
 mapping.update({'../../meetings/01_introduction/slides.pdf':'presentation/slides.pdf'})
 for source,destination in [('../assets/','assets/'),('../../data/examples/','downloads/examples/'),('../../meetings/01_introduction/presets/','presets/'),('../../meetings/01_introduction/fallback/','fallback/')]:
  if path.startswith(source):return destination+path[len(source):]+separator+fragment
 return mapping.get(path,path)+separator+fragment

def main():
 cfg=json.loads((ROOT/'site/config.json').read_text())
 if OUT.exists():shutil.rmtree(OUT)
 OUT.mkdir();shutil.copytree(ROOT/'site/assets',OUT/'assets')
 downloads=OUT/'downloads';downloads.mkdir()
 presentation=OUT/'presentation';presentation.mkdir()
 for name in ['slides.html','slides.pdf']:
  shutil.copy2(ROOT/'meetings/01_introduction'/name,presentation/name)
 for p in (ROOT/'notebooks').glob('*.ipynb'):shutil.copy2(p,downloads/p.name)
 for p in DOWNLOADS:
  shutil.copy2(ROOT/p,downloads/Path(p).name)
 shutil.copytree(ROOT/'data/examples',downloads/'examples')
 for folder in ['presets','fallback']:
  p=ROOT/'meetings/01_introduction'/folder
  if p.exists():shutil.copytree(p,OUT/folder)
 def launch(m):
  name=m.group(1);repo=cfg['repository'];branch=cfg['branch']
  if not (downloads/name).exists():raise ValueError('Missing notebook '+name)
  button=(f'<a class="button" href="https://colab.research.google.com/github/{html.escape(repo)}/blob/{html.escape(branch)}/notebooks/{name}">פתיחה ב־Colab</a>' if repo else '<a class="button" href="https://colab.research.google.com/">Open Colab</a><small>Download this notebook, then use File → Upload notebook.</small>')
  return f'<div class="launch">{button}<a download href="downloads/{name}">הורדת המחברת</a></div>'
 for idx,(slug,label) in enumerate(PAGES):
  text=(ROOT/f'site/pages/{slug}.md').read_text()
  text=re.sub(r'\[(?:Open in Colab|פתיחה ב־Colab)\]\(https://colab\.research\.google\.com/[^\n]+\)\n\[(?:Download notebook|הורדת המחברת)\]\(\.\./\.\./notebooks/([^\)]+)\)',launch,text)
  contact=''
  if cfg.get('mentor_email'):contact+='Mentor review account: **'+html.escape(cfg['mentor_email'])+'**.\n\n'
  if cfg.get('submission_channel'):contact+='Submission channel: '+html.escape(cfg['submission_channel'])
  text=text.replace('{{contact}}',contact)
  body=markdown.markdown(text,extensions=['tables','fenced_code','md_in_html'])
  body=re.sub(r'((?:href|src)=")([^"]+)(")',lambda m:m[1]+site_target(m[2])+m[3],body)
  nav=''.join(f'<a href="{s}.html"'+(' aria-current="page"' if s==slug else '')+f'>{html.escape(l)}</a>' for s,l in PAGES)
  prev=(f'<a href="{PAGES[idx-1][0]}.html">← {PAGES[idx-1][1]}</a>' if idx else '<span></span>')
  nxt=(f'<a href="{PAGES[idx+1][0]}.html">{PAGES[idx+1][1]} →</a>' if idx+1<len(PAGES) else '<a href="index.html">חזרה להתחלה</a>')
  page=f'''<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="A guided introduction to molecular simulation, Colab and independent research for Alpha students."><title>{html.escape(label)} · Alpha</title><link rel="stylesheet" href="assets/style.css"></head><body><a class="skip" href="#main">דילוג לתוכן</a><header><a href="index.html">אלפא / מעבדה חישובית</a><span class="eyebrow">משנים קוד · רואים תנועה · בודקים</span></header><div class="layout"><nav aria-label="פרקי העבודה"><div class="nav-label">מסלול התלמידים</div>{nav}</nav><main id="main">{body}<div class="pager">{prev}{nxt}</div></main></div><footer>אלפא · שמרו תשובות בעותק האישי של המחברת ב־Colab. האתר אינו אוסף הגשות.<br>תעדו את תנאי הריצה, הקוד ששיניתם והקבצים ששמרתם.</footer></body></html>'''
  (OUT/f'{slug}.html').write_text(page)
 (OUT/'.nojekyll').touch();print('Built',len(PAGES),'student pages in',OUT)
if __name__=='__main__':main()
