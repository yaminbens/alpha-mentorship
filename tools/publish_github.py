"""Create an empty course repository, push the local history and enable Pages.

Requires an authenticated GitHub CLI and explicit owner/repository arguments.
Does not overwrite an existing remote repository or expose access tokens.
"""
import argparse,subprocess,json
from pathlib import Path
R=Path(__file__).resolve().parent.parent
p=argparse.ArgumentParser();p.add_argument('--owner',required=True);p.add_argument('--name',default='alpha-mentorship');p.add_argument('--gh',default='gh');a=p.parse_args()
def run(args,**kw):return subprocess.run(args,cwd=R,text=True,check=True,**kw)
repo=a.owner+'/'+a.name
run([a.gh,'auth','status'])
# Refuse to replace unrelated history. Resume only with our already-configured remote.
view=subprocess.run([a.gh,'repo','view',repo,'--json','nameWithOwner'],cwd=R,text=True,capture_output=True)
remote=subprocess.run(['git','remote','get-url','origin'],cwd=R,text=True,capture_output=True)
expected='git@github.com:'+repo+'.git'
if view.returncode==0:
 if remote.returncode!=0 or remote.stdout.strip()!=expected:
  raise SystemExit('Repository exists without a matching local origin. Inspect ownership/history before reuse.')
else:
 run([a.gh,'repo','create',repo,'--public','--description','Alpha molecular simulation mentorship: student book, Colab notebooks and mentor guides'])
 run(['git','remote','add','origin',expected])
cfgpath=R/'site/config.json';cfg=json.loads(cfgpath.read_text());cfg['repository']=repo;cfgpath.write_text(json.dumps(cfg,indent=2)+'\n')
run(['python','tools/build_site.py'])
run(['git','add','site/config.json'])
changed=subprocess.run(['git','diff','--cached','--quiet'],cwd=R).returncode
if changed:run(['git','commit','-m','Configure course repository and Colab launch links'])
run(['git','push','-u','origin','main'])
status=subprocess.run([a.gh,'api','repos/'+repo+'/pages'],cwd=R,text=True,capture_output=True)
if status.returncode!=0:run([a.gh,'api','--method','POST','repos/'+repo+'/pages','-f','build_type=workflow'])
else:run([a.gh,'api','--method','PUT','repos/'+repo+'/pages','-f','build_type=workflow'])
run([a.gh,'workflow','run','pages.yml','--repo',repo])
print('Source pushed. Inspect GitHub Actions deployment and verify the published site before claiming it is live.')
