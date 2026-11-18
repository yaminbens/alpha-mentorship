from pathlib import Path
import re,json,importlib.util
import numpy as np
import nbformat
R=Path(__file__).resolve().parent.parent

def test_agenda_totals_sixty():
 s=(R/'docs/meeting_proposal.md').read_text()
 intervals=[tuple(map(int,m)) for m in re.findall(r'^\| (\d+)–(\d+) minutes',s,re.M)]
 assert intervals[0][0]==0 and intervals[-1][1]==60
 assert sum(b-a for a,b in intervals)==60
 assert all(a[1]==b[0] for a,b in zip(intervals,intervals[1:]))

def test_neighbours_known_controls():
 n=nbformat.read(R/'notebooks/03_measure_structure_and_motion.ipynb',as_version=4)
 scope={};exec(n.cells[3].source,scope)
 f=scope['persistence'];rng=np.random.default_rng(12);x=rng.uniform(0,10,(15,2))
 assert f(x,x+5,3)==1
 assert f(x,(x+10)%10,3,box=10)==1
 assert 0<=f(x,rng.uniform(0,10,x.shape),3)<=1

def test_information_known_laws():
 n=nbformat.read(R/'notebooks/04_information_controls.ipynb',as_version=4)
 scope={};exec(n.cells[3].source,scope)
 assert abs(scope['mi']([[1,1],[1,1]]))<1e-12
 assert abs(scope['mi']([[1,0],[0,1]])-1)<1e-12

def test_empty_homework_not_fabricated():
 n=nbformat.read(R/'notebooks/11_home_compare.ipynb',as_version=4)
 scope={}
 for c in n.cells:
  if c.cell_type=='code':exec(c.source,scope)
 assert scope['table'].T_reduced.isna().all()

def test_site_has_no_private_material():
 assert (R/'dist/index.html').exists()
 assert not (R/'dist/mentor').exists()
 assert not any(p.name in ('review_tracker_template.csv','discussion_and_answers.md') for p in (R/'dist').rglob('*'))
 for p in (R/'dist').glob('*.html'):
  text=p.read_text();assert '<main id="main">' in text
  for target in re.findall(r'(?:href|src)="([^"]+)"',text):
   if '://' in target or target.startswith(('#','mailto:','data:')):continue
   assert (p.parent/target.split('#')[0]).exists(),(p,target)

def test_upstream_hash_manifest():
 manifest=json.loads((R/'vendor/source_manifest.json').read_text())
 import hashlib
 for name,sha in manifest['sha256'].items():
  assert hashlib.sha256((R/'vendor/lennard_jones_fluid_lab'/name).read_bytes()).hexdigest()==sha

def test_source_pages_links_work_on_github():
 for p in (R/'site/pages').glob('*.md'):
  source=p.read_text()
  assert '{{notebook:' not in source
  targets=re.findall(r'\]\(([^)]+)\)|(?:src|href)="([^"]+)"',source)
  for markdown_target,html_target in targets:
   target=markdown_target or html_target
   if '://' in target or target.startswith(('#','mailto:','data:')):continue
   assert (p.parent/target.split('#')[0]).exists(),(p,target)

def test_notebook_launches_in_source_and_site():
 cfg=json.loads((R/'site/config.json').read_text())
 for p in (R/'notebooks').glob('*.ipynb'):
  n=nbformat.read(p,as_version=4);nbformat.validate(n)
  url=f"https://colab.research.google.com/github/{cfg['repository']}/blob/{cfg['branch']}/notebooks/{p.name}"
  assert url in n.cells[0].source
  pages=[s for s in (R/'site/pages').glob('*.md') if f'../../notebooks/{p.name}' in s.read_text()]
  assert pages,p.name
  for source in pages:
   built=(R/'dist'/f'{source.stem}.html').read_text()
   assert f'class="button" href="{url}"' in built
   assert f'download href="downloads/{p.name}"' in built
  assert (R/'dist/downloads'/p.name).read_bytes()==p.read_bytes()
