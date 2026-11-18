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
 cfg=json.loads((ROOT/'site/config.json').read_text())
 url=f"https://colab.research.google.com/github/{cfg['repository']}/blob/{cfg['branch']}/notebooks/{name}"
 heading='# '+title+'\n\n[Open in Colab / פתיחה בקולאב]('+url+')\n\nGitHub shows a preview. To run or edit this notebook, open it in Colab and choose **File → Save a copy in Drive**.\n\nב־GitHub מוצגת תצוגה מקדימה. להרצה ולעריכה לחצו על הקישור ושמרו עותק אישי ב־Drive.'
 n=nbf.v4.new_notebook(cells=[md(heading),md(SAVE)]+cells+[md('## Reflection and revision\nWhat did you learn? What remains uncertain? What changed after feedback?\n\n**Your answer:** …')])
 for i,cell in enumerate(n.cells): cell['id']=f'cell-{i:03d}'
 n.metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3'},'colab':{'name':name,'provenance':[]}}
 folder=ROOT/'archive/browser_track/notebooks' if name.startswith(('00_', '10_', '11_')) else ROOT/'notebooks'
 p=folder/name;p.parent.mkdir(parents=True,exist_ok=True);nbf.write(n,p)
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
 md('Double-click this text cell. Replace the dots with a sentence.\n\n**My prediction:** If I change `scale` from 1 to 2, I think … because … .'),
 code('import numpy as np\nimport matplotlib.pyplot as plt\ntime = np.array([0,1,2,3,4])\nexample_values = scale * np.array([1.0,1.4,1.2,1.6,1.5])\nplt.plot(time, example_values, "o-")\nplt.xlabel("Example time (arbitrary units)"); plt.ylabel("Example quantity (arbitrary units)")\nplt.title("Invented data for learning to plot — not simulation results"); plt.show()'),
 md('Change `scale`, rerun its cell and rerun the plot. Explain both axes and what changed.\n\n**My observation:** The horizontal axis shows … . The vertical axis shows … . After changing scale, … . This agrees/disagrees with my prediction because … .\n\nNow save and reopen your personal copy. Show the mentor your practice sharing link.')])
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
COURSE='https://yaminbens.github.io/alpha-mentorship/'
exploration=(ROOT/'assignments/01_first_experiment/exploration_template.md').read_text()
report=(ROOT/'assignments/01_first_experiment/report_template.md').read_text()
notebook('10_home_explore.ipynb','Task 1 — Watch what changes',[
 md('**At home: 20–30 minutes.** Save your own copy as `YOUR-CODE_task-1`. This notebook records your work; the simulation runs in a separate browser tab. No Python code is needed here.\n\nFollow the [numbered Task 1 instructions]('+COURSE+'task-1.html). Use the same original starting file for each of two conditions: 0 and 24 Faster clicks. Write your prediction first, then fill in the worksheet below. Double-click a text cell to edit it. You may answer in English or Hebrew.'),
 md(exploration),
 md('## Reading notes\nFor each assigned reading, choose two guiding questions from the [reading page]('+COURSE+'readings.html). Copy these prompts for each reading.\n\nReading title: …\n\nFirst question and my answer: …\n\nSecond question and my answer: …\n\nOne claim: …\n\nSupporting figure or explanation: …\n\nOne limitation: …\n\nOne word or question to discuss: …')])
AVERAGE = r'''import io
import numpy as np
import pandas as pd

# Paste ONE complete System totals / More detail table between these triple quotes.
# Keep the column headings and tabs. Save each original file separately.
browser_tsv = """
"""

def average_browser_run(text):
    raw = pd.read_csv(io.StringIO(text.strip()), sep="\t")
    raw.columns = raw.columns.str.strip()
    required = ["t", "N", "KE", "PE"]
    missing = [key for key in required if key not in raw.columns]
    if missing:
        raise ValueError("Missing columns: " + ", ".join(missing) +
                         ". Choose System totals and More detail; copy the header too.")
    values = raw[required].apply(pd.to_numeric, errors="raise")
    if values.empty or not np.isfinite(values.to_numpy()).all():
        raise ValueError("The table has empty or non-numeric measurements. Check the raw file.")
    if (values.N <= 0).any():
        raise ValueError("Particle count N must be positive. Check the export.")
    flags = []
    if len(values) != 40:
        flags.append("Expected 40 readings; found " + str(len(values)))
    if not (values.N == 64).all():
        flags.append("Particle count differs from the planned N=64")
    if len(values) != 40 or not np.allclose(values.t, np.arange(1,41)*0.125, atol=0.001):
        flags.append("Times differ from the planned 0.125, 0.250, ..., 5.000 window")
    return {"readings": len(values), "T_reduced": float((values.KE/values.N).mean()),
            "U_per_particle": float((values.PE/values.N).mean()), "flags": flags}

if not browser_tsv.strip():
    print("Paste one run's raw table above, then run this cell again. No averages yet.")
else:
    try:
        result = average_browser_run(browser_tsv)
        print("Readings:", result["readings"])
        print("T_reduced =", result["T_reduced"])
        print("U_per_particle =", result["U_per_particle"])
        for flag in result["flags"]:
            print("FLAGGED:", flag, "— keep the data and explain the difference in your method.")
        print("Copy these two averages into the matching results row below.")
    except (ValueError, pd.errors.ParserError) as error:
        print("Could not calculate averages:", error)
        print("Keep your original file and ask your mentor if you need help.")
'''
RESULTS = '''import pandas as pd
import matplotlib.pyplot as plt
# Replace only None with YOUR measured averages. Use a decimal point, not a comma.
# Each line describes one run. Keep the labels and punctuation.
rows = [
    {"condition": "low",           "repeat": 1, "T_reduced": None, "U_per_particle": None},
    {"condition": "middle",        "repeat": 1, "T_reduced": None, "U_per_particle": None},
    {"condition": "high",          "repeat": 1, "T_reduced": None, "U_per_particle": None},
    {"condition": "middle-repeat", "repeat": 2, "T_reduced": None, "U_per_particle": None},
]
table = pd.DataFrame(rows)
print(table.to_string(index=False))
'''
PLOT = '''if table[["T_reduced", "U_per_particle"]].isna().any().any():
    print("Enter your four pairs of averages above, then rerun My results and this cell.")
    print("No result plotted yet. Missing data should remain blank.")
else:
    for column in ["T_reduced", "U_per_particle"]:
        table[column] = pd.to_numeric(table[column], errors="raise")
    if not np.isfinite(table[["T_reduced", "U_per_particle"]].to_numpy()).all():
        print("A value is not finite. Check the raw data and record the problem; no graph saved.")
    else:
        fig, ax = plt.subplots()
        for index, row in table.iterrows():
            ax.scatter(row.T_reduced, row.U_per_particle, marker="x" if index==3 else "o")
            ax.annotate(row["condition"], (row.T_reduced, row.U_per_particle),
                        xytext=(5, -14 if index==3 else 6), textcoords="offset points")
        ax.set_xlabel("Measured k_B T / epsilon (reduced temperature)")
        ax.set_ylabel("U / (N epsilon) (potential energy per particle)")
        ax.set_title("My four recorded runs; the repeat may overlap the middle point")
        fig.tight_layout()
        fig.savefig("my_energy_plot.png", dpi=160, bbox_inches="tight")
        plt.show()
        table.to_csv("my_observations.csv", index=False)
        print("Created my_energy_plot.png and my_observations.csv. Download both.")
'''
notebook('11_home_compare.ipynb','Task 2 — Measure and compare',[
 md('**At home: allow 60–90 minutes; split into two sessions if useful.** Save your own copy as `YOUR-CODE_task-2`. Follow the [numbered Task 2 instructions]('+COURSE+'task-2.html) in another tab. Run four fresh preparations: 0, 8, 24 and 8 Faster clicks. Keep N=64, box side=12, gravity=0 and time step=0.005. Each run has 1000 preparation steps, 1000 settling steps and 40 readings separated by 25 steps. This notebook does the arithmetic; you collect the data.\n\nDouble-click text cells to replace `…`. In the results code, replace only `None` with your measured numbers. You may answer in English or Hebrew.'),
 md(report.split('## C.')[0]),
 md('## C. Calculate one run’s averages\nPaste the complete tab-separated export, including headings, into the empty triple quotes in the next cell. Run it once per file. Copy the two averages into the matching row of **My results** before replacing the pasted text with the next file. Keep all four raw files separately; this cell holds only the most recently pasted file.\n\nKE is kinetic energy, PE is potential energy, N is particle count. For this 2D model the helper averages KE/N and PE/N over your readings. It does not use the displayed running-average T column. Units are the model’s own reduced units, not kelvin or joules.'),
 code(AVERAGE),
 md('## My results\nEach row below is one run. Replace its two `None` entries with the two averages printed above. Leave unmeasured entries as `None`; the empty template should not produce results. After filling all four rows, run this cell. Example of the syntax only: replace `None` with a number using a decimal point. Do not copy demonstration values as your own observations.'),
 code(RESULTS),
 md('## D. Make my graph\nRun the next cell after **My results**. The repeat can lie exactly on the middle point. This is possible when replaying the same original state. If a warning appears, keep it with your notes.'),
 code(PLOT),
 md('## Save the graph and results file\nIn Colab, click the folder icon in the left sidebar. Refresh the file list if needed. Open the three-dot menu beside `my_energy_plot.png`, choose **Download**, and do the same for `my_observations.csv`. Store both in your shared work folder. These files exist only after a complete table has been plotted. Runtime files disappear when the session is removed.\n\nMy four raw data files and screenshots are saved here: …\n\nMotion and arrangement in low: …\n\nMotion and arrangement in middle: …\n\nMotion and arrangement in high: …\n\nThe middle repeat agrees/differs in these ways: …\n\nAs measured temperature increases, potential energy per particle … .\n\nThis graph does not directly measure arrangement. An additional measurement could be … .'),
 md('## E.'+report.split('## E.',1)[1]),
 md('## Interpretation reminder\nA same-state replay checks the procedure; it is not an estimate of uncertainty across independent preparations. A short observation and an energy plot do not establish an equilibrium melting temperature. Keep unexpected results. If using provided data, name its source explicitly.')])
print('Preserved five optional notebooks and three archived browser-track notebooks')
