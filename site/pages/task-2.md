# Task 2 · Measure and compare
**At home · allow 60–90 minutes, which you can split into two sessions · after Task 1**

**Goal:** collect numbers for three energy conditions, make one graph, and explain
what it shows. You will also replay one condition to check your procedure.
You do not need to write simulation code.

{{notebook:11_home_compare.ipynb}}

## 1. Save your worksheet and write a prediction
Save a copy as `YOUR-CODE_task-2`. Fill in the prediction and method sections before
collecting results. Keep your prediction even if the results surprise you.

> When I add more energy, I predict … . I will check this by measuring … .

Use a fresh copy of [ordered_initial.txt](presets/ordered_initial.txt) for every run.
Keep N = 64, box side = 12, gravity = 0, time step = 0.005, and the original model
settings. Do not add bonds, anchor particles, or fix their temperature.

## 2. Complete these four runs
| Run name | Faster clicks, while paused | Raw-data filename |
|---|---|---|
| low | 0 | `low.tsv` |
| middle | 8 | `middle.tsv` |
| high | 24 | `high.tsv` |
| middle-repeat | 8 | `middle-repeat.tsv` |

The names describe how we prepare the system. They are not temperature values.
A `.tsv` file is a plain text table whose columns are separated by tabs.

**For each row, start again at step 1 below:**

1. Pause. Load the complete original state using **Data → All atoms → Input state**.
2. Set **Steps per frame = 200**, then click **Step** five times. This is preparation.
3. Click **Faster** the number of times in the table, keeping the simulator paused.
4. Click **Step** five times more. This is the settling interval: time we allow before
   measuring. It does not prove that the system has reached equilibrium.
5. Click **Reset stats**. Open **Data**, choose **System totals** and **More detail**,
   set **Auto interval** to its off setting, and clear the old text in the data box. Do not reload or reset the particle state.
6. Set **Steps per frame = 25**. Click **Step**, then **Write data**. Do this pair of
   clicks **40 times**. Keep a tally to avoid losing count.
7. Copy the complete table, including column headings, into a plain text file with
   the filename above. Preserve tabs. Save it in Drive or on your laptop.
8. Save a screenshot and write one sentence each about motion and arrangement.
   Record anything unexpected, including a missed click or a different setting.

Each run has 1000 preparation steps, 1000 settling steps and 1000 measured steps.
The measurement window lasts 5 model time units, with 40 readings at 0.125-unit
intervals. See [the control guide](browser.html) if a control is unfamiliar.

## 3. Turn each data file into two averages
In your Task 2 notebook, find **Calculate one run's averages**. For each run:

1. Replace the empty text between the triple quotes with the entire exported table.
2. Run that cell. It reports the row count, average temperature and average potential
   energy per particle. If the row count differs from 40, check your file and note why.
3. Copy the two averages into the matching row of **My results**. Replace only `None`
   with your measured number. Then process the next file.

**Temperature** here measures particle motion. **Potential energy per particle**
describes interactions, divided by the number of particles. The notebook averages
KE/N and PE/N from your data. It uses the model's own units, not kelvin or joules.
The simulator's displayed T column may be a running average; do not copy it as an
instantaneous measurement. Keep all four raw files, not just the averages.

## 4. Make and read your graph
Run **My results**, then **Make my graph**. Until all four rows are filled, the notebook
will ask for data and leave the graph blank.

The horizontal axis is measured temperature; the vertical axis is potential energy
per particle. Each point represents one run. Answer:

- As measured temperature increases, what happens to potential energy per particle?
- Do the middle and middle-repeat points agree? If they overlap, both may be present.
- Does this graph measure arrangement directly? What would you measure to study that?

Download the CSV and graph created by the notebook. Save them outside the temporary
Colab runtime. The notebook has explicit download instructions.

## 5. Write a short conclusion
Aim for about 150 words; five or six clear sentences are enough. Use these starters:

> I changed … and kept … fixed. I observed … . My evidence is … .
> This agrees/disagrees with my prediction because … .
> I am still unsure about … . Next I would measure … .

Reloading the same starting state can give identical results. This checks that you
followed the same procedure; it does not tell us the uncertainty across independent
starting states. A short run and an energy graph do not establish a melting temperature.
Keep unexpected results and explain them rather than changing values to fit a prediction.

## Finished when
- Your notebook has a prediction, method, four completed result rows, one labelled graph,
  and a short conclusion.
- You saved four raw data files and screenshots, plus the graph and results CSV.
- You reopened the notebook and checked that your mentor can access its supporting files.
- You sent the link using [Save & submit](submit.html).

[Fill-in report template](downloads/report_template.md) ·
[Blank results CSV](downloads/results_template.csv) ·
[Hebrew instructions](downloads/task_he.md)

**Stuck?** Save what you have. Write the step number, what you expected, and what happened;
include the error message if there is one. Send that with your notebook. Missing data
should remain blank. If you use demonstration data, label its source and do not present
it as your own experiment.

<div lang="he" dir="rtl" class="hebrew">בצעו ארבע הרצות: 0, 8, 24 ושוב 8 לחיצות Faster. בכל פעם טענו מחדש את אותו קובץ התחלה. שמרו 40 שורות נתונים, חשבו ממוצעים במחברת ומלאו את הטבלה. הגישו גרף, הסבר קצר וקובצי נתונים.</div>
