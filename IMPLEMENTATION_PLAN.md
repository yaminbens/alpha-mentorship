# Implementation plan

Updated: 2026-11-15. This is the deliverable inventory for the Alpha mentorship
repository. Deliverables are implemented, backed up on GitHub and published through GitHub Pages.
Remaining unchecked items require actual student/mentor accounts, official program
details or a human classroom check. See STATUS.md and
validation/ for evidence; local notebook execution is distinct from live Colab.

## Current scope

The first meeting is 60 minutes: introductions (8), research presentation (10),
one mentor-led browser demonstration (12), Colab practice (20) and homework/site
walkthrough (10). Students perform the simulation comparison at home. A GitHub
Pages book provides instructions; personal Colab copies provide durable work and
mentor review. The website itself is not a student submission database.

See [the site and submission design](docs/student_site_and_submissions.md) and
[the demonstration guide](meetings/01_introduction/demonstration.md).

## 1. Repository foundation

- [x] Initialize an independent local Git repository on branch `main`.
- [x] Add a README with purpose, audience, entry points and current state.
- [x] Preserve the meeting proposal in `docs/meeting_proposal.md`.
- [x] Add this staged implementation checklist.
- [x] Ignore generated output, notebook checkpoints and local submissions.
- [x] Add `AGENTS.md` with durable teaching and scientific-writing conventions:
  define terms, preserve uncertainty, distinguish hypotheses from observations,
  use relative paths and keep the teaching environment independent of GNN.
- [x] Add `STATUS.md` with deliverable readiness and unresolved classroom issues.
- [x] Add `CONTRIBUTING.md` explaining edits, checks and notebook conventions.
- [x] Record licensing for original material and attribution requirements for
  adapted third-party code or figures. Preserve upstream license notices.
- [x] Prepare and review the complete initial local commit.
- [x] Create the GitHub remote, push the history and verify Pages deployment:
  https://github.com/yaminbens/alpha-mentorship.
- [x] Configure repository-specific student downloads and Colab links.
  Live Google account save/share checks remain separate below.

## 2. First meeting package

- [x] `meetings/01_introduction/agenda.md`: the 60-minute agenda, equipment,
  learning outcomes and expected student outputs.
- [x] `meetings/01_introduction/slides.md`: ten Hebrew slides, including six brief research slides for a ten-minute talk, following
  the saved proposal, with simple figures and citations.
- [x] `meetings/01_introduction/slides.pdf`: a presentation export checked for
  readable figures, equations and text. Record how to rebuild it.
- [x] `meetings/01_introduction/speaker_notes.md`: what to say, questions to ask,
  suggested transitions, likely misconceptions and approximate timing per slide.
- [x] `meetings/01_introduction/student_worksheet.md`: a demonstration prediction,
  observation prompt, Colab save/share checklist and an exit question. The full
  measurement table belongs to homework.
- [x] `meetings/01_introduction/student_worksheet_he.md`: Hebrew classroom version,
  retaining English names for software controls and scientific resources.
- [x] `meetings/01_introduction/demonstration.md`: write the 12-minute mentor-led
  demonstration sequence, prompts and scientific limitations.
- [x] Rehearse the demonstration and add the exact initial state, settings, heating
  increments and observed outcomes; the written guide is not a completed rehearsal.
- [x] `meetings/01_introduction/presets/`: reproducible initial states and metadata
  for ordered, disordered and ambiguous examples, chosen through rehearsal.
- [x] `meetings/01_introduction/fallback/`: clearly labelled example screenshots,
  a short recorded demonstration and small data files for connection problems.
- [x] `meetings/01_introduction/closing_checklist.md`: confirm each student can
  state their task, find the resources and explain when the next discussion occurs.

## 3. Mentor guidance

- [x] `mentor/facilitation_guide.md`: a practical before/during/after meeting guide,
  including demonstration rehearsal, prompts and handling unexpected outcomes.
- [x] `mentor/background_assessment.md`: brief questions about physics, algebra,
  graphs, coding and English reading; use responses to adjust the activity.
- [x] `mentor/scientific_background.md`: concise explanations of the particle
  model, reduced units, energy, temperature, equilibration, structural order,
  motion and the limits of a small two-dimensional system.
- [x] `mentor/discussion_and_answers.md`: indicative answers to reading and
  activity questions, alternative reasonable answers and misconceptions.
- [x] `mentor/feedback_rubric.md`: assess fair comparisons, reproducibility,
  graphs, reasoning and limitations; do not reward only an expected result.
- [x] `mentor/project_scoping.md`: how to narrow a question, select a measurement,
  match scope to student skills and distinguish the core project from extensions.
- [x] `mentor/troubleshooting.md`: browser controls, missing data, Colab access,
  notebook execution order, numerical failures and fallback materials.
- [x] `mentor/program_requirements.md`: record official proposal requirements,
  responsibilities, deadlines and source/date; mark missing details as unknown.
- [x] `mentor/communication_templates_he.md`: meeting invitation, reading
  instructions, first-task message, feedback and follow-up reminders.
- [x] `mentor/meeting_log_template.md`: reusable agenda, decisions, questions and
  next actions. Store completed personal student assessments outside this repo.

## 4. Reading and terminology

- [x] `readings/reading_guide.md`: required and optional readings, assigned
  sections, intended order, estimated workload and learning purpose.
- [x] `readings/questions.md`: guiding questions for Schroeder, Olah, Levitt and
  the selected notebook background; separate initial and later reading.
- [x] `readings/questions_he.md`: Hebrew version of the student prompts.
- [x] `readings/glossary_en_he.md`: model, force, energy, temperature, phase,
  density, configuration, trajectory, probability, entropy, mutual information,
  control variable and uncertainty; include units and examples where helpful.
- [x] `readings/references.bib`: bibliographic details and stable source links.
- [x] `readings/source_register.md`: access date, upstream version/commit,
  license, adaptation notes and assets reused. Link articles instead of copying
  full copyrighted texts into the repository.

## 5. Simulation and Colab materials

- [x] `simulation/browser_guide.md`: student instructions with labelled controls,
  data export/import examples and the distinction between energy adjustment and
  temperature control.
- [x] `simulation/model_and_units.md`: dimensionality, particle interactions,
  boundary conditions, fixed quantities, units and preparation procedure.
- [x] `notebooks/00_getting_started.ipynb`: running cells, editing one parameter,
  reading a plot, saving a personal copy, reopening it and sharing for review.
  This notebook is required for the first meeting, not a later optional stage.
- [x] `notebooks/01_first_simulation.ipynb`: a short adaptation of the external
  teaching resource with attribution, selected completed setup cells and explicit
  student exercises. Keep dependencies small and CPU compatible.
- [x] `notebooks/02_analyse_browser_data.ipynb`: load exported homework data,
  inspect units/columns, make the first plot and preserve raw observations.
- [x] `notebooks/03_measure_structure_and_motion.ipynb`: implement the selected
  measure, initially neighbour distances or neighbour persistence. Define the
  neighbour rule, time lag, boundary treatment and averaging explicitly.
- [x] `simulation/configs/`: small documented configurations recording model,
  particle count, box size, integration step, preparation and sampling settings.
- [x] `data/examples/`: small reusable datasets with source, settings, units,
  preparation/measurement windows and clear generated-versus-observed labels.
- [x] `data/README.md`: schemas, provenance and where student outputs should go.
- [x] Record dependency versions and instructions that work outside GNN.
- [x] Compare the browser and notebook models before connecting their results:
  document differences in dimension, walls/periodicity and ensemble. Do not treat
  different implementations as the same experiment without checking these choices.
- [x] Keep example results available so analysis lessons can proceed even when a
  student cannot launch Colab. All notebooks have local fresh-kernel execution records; live Colab is pending.

## 6. First assignment

- [x] `assignments/01_first_experiment/task.md`: the three-energy-level comparison,
  prediction, fixed settings, repeat, submission format and estimated workload.
- [x] `assignments/01_first_experiment/task_he.md`: Hebrew student version.
- [x] `assignments/01_first_experiment/report_template.md`: question, hypothesis,
  method, settings, observations, figure, conclusion and limitations.
- [x] `assignments/01_first_experiment/results_template.csv`: condition identifier,
  measured temperature, potential energy per particle, units, observation window,
  preparation history and notes; provide a data dictionary.
- [x] `assignments/01_first_experiment/example_report.md`: a labelled worked
  example using traceable demonstration data, not invented experimental results.
- [x] `assignments/01_first_experiment/review_checklist.md`: readable axes/units,
  controlled comparison, repeatability and claims supported by observations.

## 7. Follow-up meetings and research proposal

- [x] `meetings/02_results_and_question/agenda.md`: student presentations, review
  of differences and selection of a quantitative measurement.
- [x] `meetings/03_analysis/agenda.md`: extend the first-meeting Colab skills with
  an analysis exercise matched to student readiness.
- [x] `project/question_options.md`: a small set of feasible questions with their
  observables, controls, prerequisites, likely difficulties and minimum outputs.
- [x] `project/research_plan.md`: the selected question, hypothesis, experimental
  comparison, measurement, repeat strategy, uncertainty and interpretation limits.
- [x] `project/proposal_template.md`: one-page draft covering motivation,
  question, hypothesis, methods, expected figures, limitations and references.
- [x] `project/proposal_checklist.md`: distinguish an introductory research outline
  from the official submission requirements, which must be obtained from Alpha.
- [x] `project/timeline.md`: tasks before the December 6–7 seminar, follow-up
  milestones and summer work. Meeting dates remain provisional until coordinated.
- [x] `project/lab_notebook_template.md`: predictions, changes, observations,
  explanations and next actions for every session.

## 8. Optional later extensions

These are not prerequisites for the first meeting or first research proposal.

- [x] A small probability/MI notebook with a known-answer discrete example and
  an independence control before applying any estimator to particle data.
- [x] A study of whether local arrangement predicts subsequent motion, with the
  random variables, sampling distribution and comparison law stated explicitly.
- [x] A simple classifier compared with an interpretable measurement, if it serves
  the selected question. Separate training and evaluation by independent runs.
- [x] A student poster or short final report template.

Neural MI estimation and the production GNN pipeline are not requirements for
this introductory project. Only the tiny classroom examples and demonstration rehearsal have been run. New
scientific campaigns retain their own scope and authorization.

## 9. Verification and release readiness

- [x] Check relative links and ensure all advertised files exist.
- [x] Check that the slides and handouts agree on controls, units and tasks.
- [x] Run all eight notebooks from a fresh local CPU environment; record execution
  details in validation/notebook_execution.json.
- [ ] Run the notebooks in live Colab using actual student/mentor accounts.
- [x] Rehearse the browser activity from the supplied initial states; document
  actual observations and ambiguous cases rather than promise a phase outcome.
- [x] Check data import, particle identity, neighbour calculation and plots on
  simple known-answer fixtures when those features are implemented.
- [x] Distinguish steady-looking averages from demonstrated equilibration, short
  trajectories from phase-boundary evidence and classroom estimates from validated
  physical results. Display applicable numerical/physical flags with results.
- [x] Check Hebrew layout, figure labels, equation rendering and PDF exports.
- [x] Confirm a student can open the instructions and complete the core exercise
  without access to GNN files, a lab server or a GPU.
- [x] Review content before sharing: answer keys are accessible if tracked in a
  student-shared repository; personal records and real student submissions remain
  outside its tracked history. `.gitignore` alone is not access control.

## 10. GitHub Pages and student submissions

- [x] Specify the student site, saving and mentor-review workflow in
  `docs/student_site_and_submissions.md`.
- [x] Add book-style `site/` pages: start, first notebook, atomic-motion exploration,
  controlled comparison, readings, and saving/submission instructions.
- [x] Add a local preview/build command and recorded site dependencies.
- [x] Create matching task notebooks with answer cells, observation tables, plot
  outputs and a clear distinction between example data and student observations.
- [x] Add notebook downloads and Open in Colab buttons using the configured remote.
- [x] Add GitHub Actions deployment restricted to the student site build artifact.
- [x] Configure the GitHub remote and Pages destination; verify the project-site
  base path at https://yaminbens.github.io/alpha-mentorship/.
- [x] Add `mentor/review_workflow.md`: practice submission, access checks, feedback
  and revision process; keep completed review records outside public source history.
- [ ] Blank private-review tracker and storage guidance are implemented. Identify the
  actual mentor Google account and link-submission channel before class.
- [ ] Perform the human account-access check: save/reopen, separate file persistence,
  reviewer access, comments and revision using actual student/mentor accounts.
  Notebook downloads and the local executable path have already been checked.
- [x] Check that the site contains no private student records or answer keys, and
  that no browser-local save is labelled as a submission to the mentor.

## Delivery order

1. **First meeting ready:** 60-minute agenda, short presentation, rehearsed guided
   demo, introductory Colab notebook, save/share practice and mentor guide.
2. **Homework ready:** student website, first two simulation tasks, reading prompts,
   notebook/report templates and a verified mentor-review workflow.
3. **Proposal ready:** follow-up discussion, chosen measurement, research outline,
   program requirements and timeline.
4. **Further analysis ready:** simulation notebook adaptations, quantitative
   measurements, reproducible datasets and checks.
5. **Extensions:** only after the core student question and measurements are sound.

Each stage should be useful on its own. Track actual completion in this checklist;
do not mark a notebook classroom-ready merely because its source has been written.
