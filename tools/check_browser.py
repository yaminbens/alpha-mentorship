"""Check the built book at a GitHub-style project path and capture previews."""
from pathlib import Path
import threading,http.server,functools,json
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parent.parent
# Serve the repository parent so /alpha-mentorship/dist/ exercises nested relative URLs.
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
handler=functools.partial(Quiet,directory=str(R.parent))
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),handler)
threading.Thread(target=server.serve_forever,daemon=True).start()
base=f'http://127.0.0.1:{server.server_port}/alpha-mentorship/dist/'
out=R/'validation';out.mkdir(exist_ok=True);records=[];errors=[]
try:
 with sync_playwright() as pw:
  browser=pw.chromium.launch(args=['--no-sandbox'])
  for width in (1280,390):
   page=browser.new_page(viewport={'width':width,'height':900})
   page.on('pageerror',lambda e:errors.append(str(e)))
   for slug in ['index','task-0','task-1','task-2','task-3','browser','readings','submit']:
    response=page.goto(base+slug+'.html',wait_until='networkidle')
    assert response.status==200
    assert page.locator('h1').count()==1,(slug,page.locator('h1').count())
    assert page.locator('nav a[aria-current="page"]').count()==1
    overflow=page.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1')
    assert not overflow,(slug,width)
    broken=page.locator('img').evaluate_all('(es)=>es.filter(e=>!e.complete || e.naturalWidth===0).map(e=>e.src)')
    assert not broken,broken
    if slug in ('index','task-0','readings','submit'):page.screenshot(path=str(out/f'{slug}_{width}.png'),full_page=True)
    records.append({'page':slug,'width':width,'status':'passed'})
   # Actual downloadable notebook endpoint, plus local-link transport.
   response=page.request.get(base+'downloads/00_getting_started.ipynb')
   assert response.status==200 and response.json()['nbformat']==4
   page.close()
  browser.close()
 assert not errors,errors
 (out/'browser_checks.json').write_text(json.dumps(records,indent=2)+'\n')
 print(str(len(records))+' page/viewport checks and notebook download passed')
finally:server.shutdown()
