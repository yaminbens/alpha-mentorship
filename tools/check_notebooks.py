"""Execute every notebook in a fresh directory; preserve validation, not student work."""
from pathlib import Path
import json,tempfile,time,os,sys
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
R=Path(__file__).resolve().parent.parent
out=R/'validation';out.mkdir(exist_ok=True)
records=[]
for path in sorted((R/'notebooks').glob('*.ipynb')):
 start=time.monotonic();n=nbformat.read(path,as_version=4)
 with tempfile.TemporaryDirectory(prefix='alpha-notebook-') as d:
  km=KernelManager(kernel_name='python3')
  km.kernel_spec.argv=[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}']
  try:
   NotebookClient(n,timeout=None,km=km,resources={'metadata':{'path':d}}).execute()
  finally:
   if km.has_kernel: km.shutdown_kernel(now=True)
  errors=[o for c in n.cells if c.cell_type=='code' for o in c.outputs if o.output_type=='error']
  if errors:raise RuntimeError(errors)
 records.append({'notebook':path.name,'status':'passed','seconds':round(time.monotonic()-start,2),'execution':'fresh local Python kernel; not live Colab'})
 print(path.name,'passed',flush=True)
(out/'notebook_execution.json').write_text(json.dumps(records,indent=2)+'\n')
