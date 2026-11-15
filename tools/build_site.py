"""Build an explicitly selected student book for project-path GitHub Pages hosting."""
from pathlib import Path
import json,re,shutil,html
import markdown
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'dist'
PAGES=[('index','Start here'),('task-0','0 · Your first notebook'),('task-1','1 · Explore motion'),('task-2','2 · Compare conditions'),('browser','Simulation guide'),('readings','Reading & questions'),('submit','Save & submit'),('next','Next steps')]
def main():
 cfg=json.loads((ROOT/'site/config.json').read_text())
 if OUT.exists():shutil.rmtree(OUT)
 OUT.mkdir();shutil.copytree(ROOT/'site/assets',OUT/'assets')
 downloads=OUT/'downloads';downloads.mkdir()
 for p in (ROOT/'notebooks').glob('*.ipynb'):shutil.copy2(p,downloads/p.name)
 for p in ['assignments/01_first_experiment/results_template.csv','assignments/01_first_experiment/report_template.md','project/proposal_template.md','meetings/01_introduction/student_worksheet_he.md','assignments/01_first_experiment/task_he.md','readings/glossary_en_he.md','readings/questions_he.md']:
  shutil.copy2(ROOT/p,downloads/Path(p).name)
 shutil.copytree(ROOT/'data/examples',downloads/'examples')
 for folder in ['presets','fallback']:
  p=ROOT/'meetings/01_introduction'/folder
  if p.exists():shutil.copytree(p,OUT/folder)
 def launch(m):
  name=m.group(1);repo=cfg['repository'];branch=cfg['branch']
  if not (downloads/name).exists():raise ValueError('Missing notebook '+name)
  button=(f'<a class="button" href="https://colab.research.google.com/github/{html.escape(repo)}/blob/{html.escape(branch)}/notebooks/{name}">Open in Colab</a>' if repo else '<a class="button" href="https://colab.research.google.com/">Open Colab</a><small>Download this notebook, then use File → Upload notebook.</small>')
  return f'<div class="launch">{button}<a download href="downloads/{name}">Download notebook</a></div>'
 for idx,(slug,label) in enumerate(PAGES):
  text=(ROOT/f'site/pages/{slug}.md').read_text()
  text=re.sub(r'\{\{notebook:([^}]+)\}\}',launch,text)
  contact=''
  if cfg.get('mentor_email'):contact+='Mentor review account: **'+html.escape(cfg['mentor_email'])+'**.\n\n'
  if cfg.get('submission_channel'):contact+='Submission channel: '+html.escape(cfg['submission_channel'])
  text=text.replace('{{contact}}',contact)
  body=markdown.markdown(text,extensions=['tables','fenced_code','md_in_html'])
  nav=''.join(f'<a href="{s}.html"'+(' aria-current="page"' if s==slug else '')+f'>{html.escape(l)}</a>' for s,l in PAGES)
  prev=(f'<a href="{PAGES[idx-1][0]}.html">← {PAGES[idx-1][1]}</a>' if idx else '<span></span>')
  nxt=(f'<a href="{PAGES[idx+1][0]}.html">{PAGES[idx+1][1]} →</a>' if idx+1<len(PAGES) else '<a href="index.html">Back to start</a>')
  page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="A guided introduction to molecular simulation, Colab and independent research for Alpha students."><title>{html.escape(label)} · Alpha</title><link rel="stylesheet" href="assets/style.css"></head><body><a class="skip" href="#main">Skip to content</a><header><a href="index.html">ALPHA / MOLECULAR SIMULATION</a><span class="eyebrow">Observe · Measure · Explain</span></header><div class="layout"><nav aria-label="Course chapters"><div class="nav-label">Student field guide</div>{nav}</nav><main id="main">{body}<div class="pager">{prev}{nxt}</div></main></div><footer>Alpha mentorship · Save answers in your personal Colab notebook. This site does not collect submissions.<br>Educational models and examples have limits; record your conditions and sources.</footer></body></html>'''
  (OUT/f'{slug}.html').write_text(page)
 (OUT/'.nojekyll').touch();print('Built',len(PAGES),'student pages in',OUT)
if __name__=='__main__':main()
