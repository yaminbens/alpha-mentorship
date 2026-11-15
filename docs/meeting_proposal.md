# Introductory meeting proposal

Prepared for Yamin's Alpha mentorship, 2026-11-15. The meeting should take place
before the December 6–7 Hanukkah seminar; its exact date is to be coordinated.

## Purpose

The 60-minute meeting centres on the question: **How can we tell whether a
collection of atoms behaves like a solid or a liquid?** Students connect a short
research presentation with one mentor-led simulation and an introduction to Colab.
They perform the full simulation experiment independently at home.

By the end, students should be able to explain what a molecular simulation does,
distinguish an observation from a measurement and open, edit, save and share their
own notebook. Each student leaves with homework instructions and a follow-up
discussion date. No prior programming is assumed. Students need a laptop,
internet access and a Google account that can use Colab. Check access beforehand.

The initial research direction is: **How do atomic arrangement and motion change
as we add energy to a simple model material, and which measurements help us
distinguish solid-like from liquid-like behaviour?** Refine this direction after
learning about the students' backgrounds and interests.

## Agenda

| Time | Activity | Intended outcome |
|---|---|---|
| 0–8 minutes | Introductions and initial readings | Learn backgrounds, interests and questions |
| 8–18 minutes | Short research presentation | Connect atomic motion, measurements and the mentor's research |
| 18–30 minutes | One mentor-led simulation | Predict, observe and discuss the effect of adding energy |
| 30–50 minutes | Guided Colab introduction | Open a personal copy, run a cell, edit text, plot example data, save and share |
| 50–60 minutes | Homework site and submission walkthrough | Find the first tasks, check saved work and explain how to submit |

## Research presentation

Use the following six visual prompts within ten minutes. Keep explanations short;
the readings and later meetings develop the concepts further.

1. **Why do materials behave differently?** Show solid and liquid configurations.
   Ask what changes and what stays the same; invite predictions first.
2. **How do we simulate atoms?** Explain how positions determine forces, forces
   change motion and motion changes positions. Introduce a simplified model with
   attraction at moderate separation and strong repulsion at short separation.
3. **From a movie to a measurement.** Introduce temperature, energy, neighbour
   distances and changes in neighbours. Ask what would convince someone who cannot
   see the animation.
4. **Where the mentor's research enters.** Explain the investigation of atomic
   arrangements and statistical relationships in materials. Introduce “How much
   does knowing one region tell us about another?” and machine learning as one
   tool being investigated for measuring such relationships.
5. **Why many observations matter.** Show several configurations under the same
   conditions. Fluctuations are part of the system. Mutual information describes
   a distribution of observations and cannot be determined from one snapshot.
6. **The students' question.** Present the comparison and invite a measurement
   and a prediction. Keep predictions separate from measured results.

## Classroom simulation

Use [Schroeder's Interactive Molecular Dynamics](https://physics.weber.edu/schroeder/md/).
It accompanies the initial reading and runs in a browser. Its two-dimensional
particle model provides controls for particle number, box size and energy, and
supports numerical data export.

Use one demonstration, **What changes when we add energy?**, with the mentor
controlling the simulation on the projector. Students predict and comment; the
three-condition experiment and measurements belong to homework. The
[mentor demonstration guide](../meetings/01_introduction/demonstration.md) gives
the 12-minute sequence and questions.

Show a prepared ordered state, ask whether its atoms are moving, then add energy
without changing particle count or box size. Discuss the observed changes in
motion and arrangement and identify one quantity to measure at home. Do not
promise that melting will occur within the demonstration window.

## Colab introduction

Use a short introductory notebook with example data, not a second simulation.
During the 20-minute guided activity each student should:

1. Open the notebook from the course site and save a personal copy in Drive.
2. Rename it using an agreed student code and assignment identifier.
3. Run a simple code cell, edit a text answer and display a supplied example plot.
4. Change one value, rerun the relevant cell and explain what changed.
5. Save, close and reopen the notebook to check that their answer persists.
6. Share it with the mentor's designated Google account and copy the review link.

Explain that notebook text and saved outputs can persist, while runtime variables
and temporary files do not provide durable storage. Store observations in notebook
cells and download any data files that must be retained. Use the
[site and submission plan](student_site_and_submissions.md) for the full workflow.

## Independent simulation at home

Students carry out the following sequence using the homework instructions:

1. Start from a prepared ordered configuration. Ask whether atoms move, retain
   their neighbours and might change their behaviour when energy is added.
2. Keep particle number, box size and interaction settings fixed. Add energy in
   stages using the speed controls. After each change, allow a settling period
   and observe for the same duration.
3. Record three conditions. Save a screenshot and record measured temperature,
   energy, arrangement and motion. Use the simulator's units and record the
   observation window.
4. Remove energy and examine whether the initial arrangement returns. Discuss
   preparation history and waiting time.
5. Identify the evidence for solid-like or liquid-like behaviour, ambiguous
   observations and measurements that might resolve them.

Measure temperature after adding energy; it is not automatically held fixed.
A short classroom trajectory cannot establish an equilibrium melting temperature.
Use the [simulation instructions](https://physics.weber.edu/schroeder/md/) for the
controls, units, data recording and reset procedure. A settling period is part of
the classroom protocol, not proof that equilibrium has been reached.

For later simulation coding, use a selected subset of
[Grazioli's Lennard-Jones Fluid Lab](https://github.com/ggrazioli/LennardJonesFluidLab)
and its [Colab notebook](https://colab.research.google.com/github/ggrazioli/LennardJonesFluidLab/blob/main/LennardJonesFluidLab_Colab_public.ipynb).
Begin with loading the code, running a small simulation and inspecting a plot.
The full lab targets undergraduate physical chemistry and includes incomplete
student exercises; prepare a shortened adaptation. It conserves total energy
rather than maintaining prescribed temperature. Check dimensionality and boundary
conditions before comparing its results with those of the browser model.

## Reading and guiding questions

### Before the meeting

[Daniel Schroeder, Interactive Molecular Dynamics](https://arxiv.org/html/1502.06169v1):
read the introduction, Section II and Figure 1, then Exercise 1 in Section VI.
Focus on explanations and figures; implementation details can wait.

- What rules govern the particles?
- What makes this a simplified model?
- How could arrangement and motion distinguish a solid from a liquid?

### After the meeting

[Christopher Olah, Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information/):
read “Visualizing Probability Distributions,” “Entropy and Multiple Variables”
and “Mutual Information.” Focus on intuition; derivations are optional.

- Give an example where knowing one quantity helps predict another.
- What would independence mean?
- Why is one observation insufficient to measure the relationship?

### Optional Hebrew introduction

[Michael Levitt, סימולציות מחשב בשירות הביולוגיה](https://kids.frontiersin.org/he/articles/10.3389/frym.2020.603629-he)
offers an accessible introduction for students who find the English readings hard.

- What can a simulation help us learn?
- Why do scientists simplify models?
- How could we check whether a model is useful?

### Before the later simulation coding session

Read the background and initial setup in the
[Lennard-Jones Fluid Lab](https://github.com/ggrazioli/LennardJonesFluidLab).

- What are inputs and outputs of the simulation?
- Which quantities are controlled?
- What makes two runs a fair comparison?

For each reading, identify one claim, its explanation or supporting evidence,
and one limitation or unanswered question. Bring short answers and one unresolved
question to the discussion.

## First task

Allow approximately one week, with an expected workload of 60–90 minutes.

**At fixed particle number and box size, explore three energy levels. Describe
changes in atomic arrangement and motion, and propose a measurement that would
make the comparison more objective.** Provide a starting configuration and agree
on the procedure during the meeting.

Students submit:

- Their question and prediction, written before the comparison.
- Starting conditions and a record of changed and fixed quantities.
- A table of measured temperature, potential energy per particle, observation
  window and qualitative observations for all three conditions.
- One screenshot per condition and one plot of potential energy per particle
  against measured temperature, with units on both axes.
- A repeat of one condition from the same starting preparation, noting differences.
- A conclusion of about 150 words: observations, agreement or disagreement with
  the prediction, and the next question.

The energy plot introduces quantitative analysis; it is not by itself a measure
of structural order. Possible structural or dynamical measurements include
neighbour distances, local arrangement and persistence of neighbours. Select and
implement one with the mentor at the next stage.

Assess whether the comparison is understandable and reproducible and whether
the conclusion follows from the evidence. Unexpected observations are useful
material for discussion.

## Next steps

| Stage | Work | Deliverable |
|---|---|---|
| Before the meeting | Send reading; confirm access; prepare starting states | Student predictions and questions |
| Within one week afterwards | Complete the first task | Report, table and plot |
| Follow-up before December 6 | Discuss findings and select a measurement | A narrower question and agreed comparison |
| Before the seminar | Draft a research outline | Background, question, hypothesis, method, controls, expected figures and limitations |
| Subsequent sessions | Extend the introductory Colab skills; automate analysis; examine repeatability | Reproducible notebook and preliminary results |

A possible refined question is: **At fixed density, how does the persistence of
neighbouring atoms change with measured temperature in a two-dimensional model
material?** Define the neighbour rule, time interval and sampling procedure when
developing it. A later information-theory extension could ask whether local
arrangement helps predict subsequent motion, after the basic measurements are
understood.

Before the first meeting, rehearse the simulation states and retain example
outputs for discussion. The browser demonstration has been rehearsed and the notebooks executed locally;
authenticated live Colab saving/sharing still requires an account-access check. Official proposal requirements should be obtained from the program
coordinators before treating the one-page outline as a submission template.
