# Task 1 · Watch what changes
**At home · about 20–30 minutes · after Task 0**

**Question:** what happens to the motion and arrangement of atoms when we add energy?
Today you will describe what you see. The numerical measurements come in Task 2.

[Open in Colab](https://colab.research.google.com/github/yaminbens/alpha-mentorship/blob/main/notebooks/10_home_explore.ipynb)
[Download notebook](../../notebooks/10_home_explore.ipynb)

## 1. Get ready
Save your own copy as `YOUR-CODE_task-1`. It already contains a worksheet: replace
`…` with your answers. You may answer in English or Hebrew. Short sentences are fine.
Open [the simulator](https://physics.weber.edu/schroeder/md/) in a second tab and keep
[the control guide](browser.md) available.

## 2. Write a prediction before running
Complete both sentences in the notebook:

> I think the particles will move … when energy is added, because … .
> I think their arrangement will … because … .

A prediction can turn out to be wrong. Keep it so you can compare it with your observation.

## 3. Observe the low-energy condition
1. Open [ordered_initial.txt](../../meetings/01_introduction/presets/ordered_initial.txt) and copy all its text.
2. Pause the simulator. Open **Data**, choose **All atoms**, paste that text into its data box, and click **Input state**.
3. Check **N = 64**, box side **12**, gravity **0**, and time step **0.005**.
   N means number of particles; the box side is a length in the model's own units.
4. Set **Steps per frame = 200**. Click **Step** five times to prepare the system,
   then five more times to let it evolve. Do not click **Faster** yet.
5. Save a screenshot as `task1_low.png`. Describe the arrangement. Watch a few more
   steps to describe the motion: do particles mainly move around nearby positions,
   or do their neighbours change? If you cannot tell, write that.

## 4. Compare with added energy
Reload the **same original file**. This starts a fresh comparison; do not continue
from your previous observation.

1. Set Steps per frame to **200** and click **Step** five times.
2. While paused, click **Faster** **24 times**. Count the clicks.
3. Click **Step** five more times. Save `task1_high.png`.
4. Watch a few more steps. Describe the motion and arrangement again.

Keep N, box size, gravity and other model settings unchanged. Faster increases speeds;
it does not set a fixed temperature. Task 1 is an exploration: use fresh runs for Task 2.

## 5. Fill in your worksheet
| Prompt | What to write |
|---|---|
| What stayed the same? | Particle count, box size, starting file and model settings |
| What did I change? | Number of Faster clicks: 0 compared with 24 |
| What did I see? | One sentence about motion and one about arrangement for each condition |
| What supports my description? | Your two screenshots and notes from watching motion |
| What is still unclear? | One question, such as how to count changes of neighbours |

Describe observations before interpreting them. “Particles changed neighbours” is
an observation. “This is a liquid” is an interpretation that needs more evidence.
A still image cannot show speed, and a short run cannot establish a phase.

## Finished when
Your saved notebook contains your original prediction, settings, two observations,
two screenshots or accessible image links, and one question for the mentor.
Save the images separately in Drive and share them too. Follow [Save & submit](submit.md).

[Download the fill-in worksheet](../../assignments/01_first_experiment/exploration_template.md).
If Colab is unavailable, copy this worksheet into a document and use the same prompts.

**If the simulator will not load:** use the [recorded demonstration](browser.md),
label your work “provided demonstration, not my run”, and write what you can and
cannot observe. Send the access problem to your mentor.

<div lang="he" dir="rtl" class="hebrew">כתבו תחזית, השוו בין 0 ל־24 לחיצות Faster מאותו קובץ התחלה, ושמרו שני צילומים. תארו בנפרד תנועה וסידור. אין צורך במספרים או בגרף במשימה הזאת.</div>
