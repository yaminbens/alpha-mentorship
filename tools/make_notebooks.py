"""Generate portable teaching notebooks. No GNN or GitHub authentication required."""
from pathlib import Path
import hashlib,json
import nbformat as nbf
ROOT=Path(__file__).resolve().parent.parent
SHA='9f3f932bb3ffdf47bc0de23378aba196bdc9452b'
VENDOR=ROOT/'vendor/lennard_jones_fluid_lab'
def md(s): return nbf.v4.new_markdown_cell(s)
def code(s): return nbf.v4.new_code_cell(s)
SAVE='''## Save and submit / שמירה והגשה
1. **File → Save a copy in Drive** before editing. Rename with your student code and task.
2. Write answers in text cells. Save outputs. Runtime files are temporary: download data/images separately.
3. Save, close and reopen your copy. Verify that your answer and plot remain.
4. Share with the mentor account given in class, normally as **Commenter**. Send the link through the agreed private channel.
5. Keep a dated `.ipynb` download if you need a fixed submission snapshot.

שמרו עותק אישי, פתחו אותו מחדש ובדקו שהתשובות נשמרו. שיתוף מחברת אינו שיתוף אוטומטי של קובצי סביבת ההרצה.
'''
def notebook(name,title,cells):
 n=nbf.v4.new_notebook(cells=[md('# '+title),md(SAVE)]+cells+[md('## Reflection and revision\nWhat did you learn? What remains uncertain? What changed after feedback?\n\n**Your answer:** …')])
 for i,cell in enumerate(n.cells): cell['id']=f'cell-{i:03d}'
 n.metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3'},'colab':{'name':name,'provenance':[]}}
 p=ROOT/'notebooks'/name;p.parent.mkdir(exist_ok=True);nbf.write(n,p)
BOOT='''# Fetch three MIT-licensed teaching modules and their license from a pinned commit.
# The content hashes verify the exact source used by this course.
import urllib.request, hashlib, sys, tempfile
from pathlib import Path
MODULES = '''+repr({f:hashlib.sha256((VENDOR/f).read_bytes()).hexdigest() for f in ['mathTools.py','classes.py','dynamics.py','LICENSE']})+'''
module_dir = Path(tempfile.gettempdir()) / "alpha_lj_pinned"
module_dir.mkdir(exist_ok=True)
for filename, expected in MODULES.items():
    path = module_dir / filename
    if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        content = urllib.request.urlopen("https://raw.githubusercontent.com/ggrazioli/LennardJonesFluidLab/'''+SHA+'''/" + filename).read()
        if hashlib.sha256(content).hexdigest() != expected:
            raise ValueError("Source integrity mismatch: " + filename)
        path.write_bytes(content)
sys.path.insert(0, str(module_dir))
import numpy as np
import matplotlib.pyplot as plt
from classes import Ensemble
from dynamics import takeOneStep
'''
RUN='''# Small CPU teaching example, not a melting experiment.
np.random.seed(42)
system = Ensemble(nMol=16, sideLen=8.0, dim=2, temperature=0.3, periodic=True)
system.UpdateAccelerationLJ()  # initialize forces before the first integration step
positions, values = [], []
dt = 0.002
for step in range(201):
    if step % 5 == 0:
        positions.append(np.array([m.r.copy() for m in system.moList]))
        kinetic = system.getKE()
        values.append([step*dt, 2*kinetic/(system.dim*system.nMol), system.getPE()/system.nMol,
                       (kinetic+system.getPE())/system.nMol])
    if step < 200:
        takeOneStep(system, dt=dt)
positions = np.asarray(positions)
values = np.asarray(values)
print("Samples:", len(values), "simulation time:", values[-1,0], "reduced time units")
print("Energy per-particle range:", np.ptp(values[:,3]), "epsilon")
plt.plot(values[:,0], values[:,1]); plt.xlabel("Time / reduced unit"); plt.ylabel("k_B T / epsilon"); plt.show()
'''
notebook('00_getting_started.ipynb','Task 0 — Your first saved notebook',[
 md('**In class: 20 minutes.** A notebook combines explanation, code and outputs. Run cells from top to bottom. No simulation is run here.\n\n**Prediction:** what will happen to the plotted values if you double `scale`?'),
 code('message = "My first saved notebook"\nprint(message)\nscale = 1.0'),
 md('Double-click this text cell. Replace the dots with a sentence.\n\n**My prediction:** …'),
 code('import numpy as np\nimport matplotlib.pyplot as plt\ntime = np.array([0,1,2,3,4])\nexample_values = scale * np.array([1.0,1.4,1.2,1.6,1.5])\nplt.plot(time, example_values, "o-")\nplt.xlabel("Example time (arbitrary units)"); plt.ylabel("Example quantity (arbitrary units)")\nplt.title("Invented data for learning to plot — not simulation results"); plt.show()'),
 md('Change `scale`, rerun its cell and rerun the plot. Explain both axes and what changed.\n\n**My observation:** …\n\nNow save and reopen your personal copy. Show the mentor your practice sharing link.')])
notebook('01_first_simulation.ipynb','Later activity — Run a small particle simulation',[
 md('Adapted teaching workflow using [Gianmarc Grazioli’s MIT-licensed code](https://github.com/ggrazioli/LennardJonesFluidLab), pinned at `'+SHA+'`. The course keeps the upstream license in `vendor/`.\n\nThis 2D periodic example differs from the browser model’s soft walls. It has no thermostat. Initial temperature is a preparation parameter; measured temperature can change. The upstream pressure calculation is not used.'),
 md('**Predict first:** will measured temperature remain exactly equal to its initial value? Why?'),code(BOOT),code(RUN),
 code('import json\nnp.savez("alpha_trajectory.npz", positions=positions, values=values, L=system.sideLen, dt=dt, sample_every=5)\nnp.savetxt("alpha_observations.csv", values, delimiter=",", header="time,T_reduced,U_per_particle,E_per_particle", comments="")\nprint("Created alpha_trajectory.npz and alpha_observations.csv — download these before the runtime ends.")'),
 md('**Questions:** what did the input control? What did we measure? Why is this short run insufficient to establish a phase or convergence?\n\n**Answers:** …')])
notebook('02_analyse_browser_data.ipynb','Analyse your recorded observations',[
 md('Paste your window-averaged observations into the CSV text below. The initial table is an **invented format example**, not evidence from a simulation. Replace it and set `using_example=False` only after entering your own measured data. Keep raw browser exports separately.'),
 code('import io\nimport pandas as pd\nimport matplotlib.pyplot as plt\nusing_example = True\ncsv_text = """condition,repeat,T_reduced,U_per_particle\nlow,1,0.1,-2.2\nmiddle,1,0.3,-1.8\nhigh,1,0.6,-1.2\nmiddle,2,0.32,-1.75\n"""\ntable = pd.read_csv(io.StringIO(csv_text))\nrequired = ["T_reduced", "U_per_particle"]\nfor column in required:\n    table[column] = pd.to_numeric(table[column], errors="raise")\nprint("INVENTED FORMAT EXAMPLE" if using_example else "STUDENT OBSERVATIONS — verify source and units")\nprint(table.to_string(index=False))'),
 code('plt.scatter(table.T_reduced, table.U_per_particle)\nfor _,row in table.iterrows():\n    plt.annotate(str(row["condition"])+" / "+str(row["repeat"]), (row.T_reduced,row.U_per_particle))\nplt.xlabel("Measured k_B T / epsilon"); plt.ylabel("Potential energy / (N epsilon)")\nplt.title("Invented example" if using_example else "My observations"); plt.show()\ntable.to_csv("recorded_observations.csv",index=False)'),
 code('browser_tsv = """"""\n# Paste the full detailed System totals export inside the triple quotes above.\nif browser_tsv.strip():\n    raw = pd.read_csv(io.StringIO(browser_tsv), sep="\\t")\n    raw.columns = raw.columns.str.strip()\n    for key in ["N","KE","PE"]:\n        raw[key] = pd.to_numeric(raw[key], errors="raise")\n    print("Window mean reduced T:", (raw.KE/raw.N).mean())\n    print("Window mean U/N:", (raw.PE/raw.N).mean())\nelse:\n    print("Optional: paste your detailed browser export to average KE/N and PE/N.")'),
 md('Record N, L, preparation, settling time, observation windows and source filenames here. Adjacent time samples are correlated; one repeat does not establish an uncertainty interval. Energy alone does not measure structural order.\n\n**Method and interpretation:** …')])
NEIGH='''def neighbours(frame, k=4, box=None):
    frame = np.asarray(frame, dtype=float)
    if frame.ndim != 2 or not 1 <= k < len(frame):
        raise ValueError("Need positions (particles, dimensions) and 1 <= k < N")
    delta = frame[:, None, :] - frame[None, :, :]
    if box is not None:
        delta -= box * np.round(delta / box)
    distance2 = np.sum(delta**2, axis=-1)
    np.fill_diagonal(distance2, np.inf)
    return np.argsort(distance2, axis=1, kind="stable")[:, :k]

def persistence(first, later, k=4, box=None):
    a,b = neighbours(first,k,box), neighbours(later,k,box)
    return np.mean([len(set(x)&set(y))/k for x,y in zip(a,b)])
'''
notebook('03_measure_structure_and_motion.ipynb','Measure how neighbours persist',[
 md('Choose the same particle identities at two times. For each particle define its k nearest neighbours; persistence is the retained fraction averaged over particles. Exact distance ties use index order. Periodic distances require the same box in both frames. This is a dynamical measure that depends on the time lag.'),
 code('import numpy as np\nimport matplotlib.pyplot as plt\n'+NEIGH),
 code('rng=np.random.default_rng(7)\nfirst=rng.uniform(0,10,(20,2))\ntranslated=first+np.array([2,3])\nprint("Translation control:",persistence(first,translated,k=4))\nassert persistence(first,translated,k=4)==1.0\nlater=first+rng.normal(0,1,first.shape)\nprint("Synthetic displaced configuration:",persistence(first,later,k=4))'),
 md('The control above is synthetic. For actual data, upload the NPZ generated by notebook 01. This next cell skips cleanly if the file is absent; a skipped cell is not a physical result.'),
 code('from pathlib import Path\np=Path("alpha_trajectory.npz")\nif p.exists():\n    data=np.load(p)\n    trajectory=data["positions"]\n    box=float(data["L"])\n    lag_time=float(data["dt"])*int(data["sample_every"])\n    retained=[persistence(trajectory[0],frame,k=4,box=box) for frame in trajectory]\n    plt.plot(np.arange(len(retained))*lag_time,retained)\n    plt.xlabel("Lag / reduced time");plt.ylabel("Retained neighbour fraction");plt.ylim(0,1.05);plt.show()\nelse:\n    print("Upload alpha_trajectory.npz to analyse a trajectory; only synthetic controls ran.")'),
 md('**Questions:** why does translation preserve neighbours? Why does changing lag or k change the question? What additional runs would support a temperature comparison?\n\n**Answers:** …')])
notebook('04_information_controls.ipynb','Optional — Information from repeated trials',[
 md('Population: repeated fair binary trials. X is a fair bit and Y is either an independent fair bit or a copy of X. The joint law has respectively four equally likely pairs or two diagonal pairs. The product law draws X and Y independently from their marginals. Exact MI is respectively 0 or 1 bit. We estimate from many pairs, never from one outcome.'),
 code('import numpy as np\ndef mi(table):\n    p=np.asarray(table,dtype=float);p=p/p.sum()\n    q=p.sum(axis=1,keepdims=True)*p.sum(axis=0,keepdims=True)\n    mask=p>0\n    return float(np.sum(p[mask]*np.log2(p[mask]/q[mask])))\nassert abs(mi([[1,1],[1,1]]))<1e-12\nassert abs(mi([[1,0],[0,1]])-1)<1e-12\nrng=np.random.default_rng(12)\nx=rng.integers(0,2,1000); independent=rng.integers(0,2,1000)\ncounts=np.zeros((2,2),int);np.add.at(counts,(x,independent),1)\nprint("Finite-sample independent estimate:",mi(counts),"bits; exact population value: 0")'),
 md('Why need not the finite estimate be exactly zero? What changes if we use fewer trials? This exercise is not a measurement of thermodynamic entropy.')])
notebook('05_prediction_controls.ipynb','Optional — A prediction baseline',[
 md('This is a **synthetic supervised-learning illustration**, not molecular data. Eight independently generated groups stand in for independent runs. The feature is a random number and the label is whether it exceeds zero plus noise. Train and test groups are separated. Compare an interpretable threshold with a nearest-centroid classifier and a constant-label baseline.'),
 code('import numpy as np\nrng=np.random.default_rng(8)\nx=rng.normal(size=(8,80))\ny=(x+0.4*rng.normal(size=x.shape)>0).astype(int)\nxtrain,ytrain=x[:5].ravel(),y[:5].ravel()\nxtest,ytest=x[5:].ravel(),y[5:].ravel()\ncentres=np.array([xtrain[ytrain==c].mean() for c in (0,1)])\npred=np.argmin((xtest[:,None]-centres[None,:])**2,axis=1)\nconstant=np.full_like(ytest,int(ytrain.mean()>=0.5))\nthreshold=(xtest>0).astype(int)\nfor label,p in [("constant",constant),("threshold",threshold),("nearest centroid",pred)]:\n    print(label,"held-out accuracy",np.mean(p==ytest))\nprint("Test positive fraction",ytest.mean())'),
 md('What would leakage look like for nearby frames from the same physical trajectory? Why is accuracy not mutual information, causality or free energy?')])
for name,title,body in [
 ('10_home_explore.ipynb','Task 1 — Explore atomic motion','''Open [Schroeder’s simulation](https://physics.weber.edu/schroeder/md/) and follow the course browser guide. Use the supplied starting state. This notebook records your work; it does not launch the simulation.

## Before observing
My question and prediction: …

## Settings
N: …; L: …; initial-state file: …; model/boundaries: …; energy intervention: …

## Observations
What changed in motion? …
What changed in arrangement? …
What remains uncertain? …
Screenshot or separately shared image link: …

## Next measurement
What would I measure to test my interpretation? …'''),
 ('11_home_compare.ipynb','Task 2 — Make a controlled comparison','''Keep particle number, box and model fixed. Compare three energy preparations and repeat one from the same initial state. Follow the website instructions.

## Prediction
…

## Method
Preparation and interventions: …
Settling interval and observation windows: …
Time step and units: …
Separate raw data and screenshot locations: …

## Conclusion (about 150 words)
Describe observations, disagreement/agreement with the prediction, limitations and the next measurement. Energy alone does not determine structural order.

…''')]:
 cells=[md(body)]
 if name.startswith('11'):
  cells += [code('import pandas as pd\nimport matplotlib.pyplot as plt\n# Replace None only with your measured window averages. No invented defaults.\nrows=[{"condition":c,"repeat":r,"T_reduced":None,"U_per_particle":None}\n      for c,r in [("low",1),("middle",1),("high",1),("middle",2)]]\ntable=pd.DataFrame(rows)\nprint(table.to_string(index=False))'),code('if table[["T_reduced","U_per_particle"]].isna().any().any():\n    print("Enter your measured data above, then rerun both cells. No result plotted yet.")\nelse:\n    table.T_reduced=pd.to_numeric(table.T_reduced)\n    table.U_per_particle=pd.to_numeric(table.U_per_particle)\n    plt.scatter(table.T_reduced,table.U_per_particle)\n    plt.xlabel("Measured k_B T / epsilon");plt.ylabel("Potential energy / (N epsilon)");plt.show()\n    table.to_csv("my_observations.csv",index=False)\n    print("Download my_observations.csv before ending the runtime.")')]
 notebook(name,title,cells)
print('Generated 8 notebooks')
