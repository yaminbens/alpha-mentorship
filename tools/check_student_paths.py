"""Exercise incomplete and completed learner paths, keeping solutions out of templates."""
from pathlib import Path
import json, tempfile, sys
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
R=Path(__file__).resolve().parent.parent
records=[]
for name in ['10_home_explore.ipynb','11_home_compare.ipynb','12_build_simulation.ipynb']:
    n=nbformat.read(R/'notebooks'/name,as_version=4)
    for c in n.cells:
        if c.cell_type!='code':continue
        s=c.source
        s=s.replace('pass  # TODO: הגדילו את count_right באחד','count_right += 1')
        s=s.replace('cases = [1.0, 0.7]','cases = [1.0, 0.7, 0.85]')
        s=s.replace('mean_height = None','mean_height = float(np.mean(final_y))')
        s=s.replace('next_position = None','next_position = position + velocity * dt')
        s=s.replace('velocity = None','velocity = -velocity')
        s=s.replace('x = None  # TODO: קראו ל־move עם x, vx ו־dt','x = move(x, vx, dt)')
        s=s.replace('y = None  # TODO: קראו ל־move עם y, vy ו־dt','y = move(y, vy, dt)')
        c.source=s
    with tempfile.TemporaryDirectory(prefix='alpha-student-completed-') as d:
        km=KernelManager(kernel_name='python3');km.kernel_spec.argv=[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}']
        try:NotebookClient(n,timeout=None,km=km,resources={'metadata':{'path':d}}).execute()
        finally:
            if km.has_kernel:km.shutdown_kernel(now=True)
        text='\n'.join(o.get('text','') for c in n.cells if c.cell_type=='code' for o in c.outputs)
        if name.startswith('10_'):assert 'הספירה תואמת לבדיקה' in text
        if name.startswith('11_'):
            table=json.loads((Path(d)/'task2_comparison.json').read_text())
            assert len(table)==3 and all(isinstance(row['mean_height'],float) for row in table)
        if name.startswith('12_'):
            assert 'עברו 8 מתוך 8' in text
            assert (Path(d)/'task3_my_simulation.html').exists()
            (R/'validation/student_animation_preview.html').write_text((Path(d)/'task3_my_simulation.html').read_text())
        records.append({'notebook':name,'completed_learner_path':'passed','artifacts':sorted(p.name for p in Path(d).iterdir())})
        print(name,'completed learner path passed',flush=True)
(R/'validation/completed_student_paths.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
