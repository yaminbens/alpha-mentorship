# Alpha molecular simulation mentorship

An introductory teaching package for high-school students: a one-hour meeting,
a guided simulation, Colab practice and three independent coding activities.
Students should already know variables, conditions and loops.

**[Student website — Hebrew](https://yaminbens.github.io/alpha-mentorship/)**

Send students the website link above. It provides the course chapters, activity
instructions, guided reading and Colab buttons in Hebrew. This repository contains
the English project documentation, source code and teaching assets. Student-facing
notebooks and materials are in Hebrew; optional scientific extensions are in English.

## First meeting

8 minutes introductions, 10 minutes research, 12 minutes mentor-led simulation,
20 minutes Colab and 10 minutes next steps. Students need a laptop, browser,
internet and a Google account that can use Colab. No local installation or student
GitHub account is needed. The full activities take place independently over later sessions.

## Activities and notebooks

| Activity | Main idea | Notebook |
|---|---|---|
| [Task 0](https://yaminbens.github.io/alpha-mentorship/task-0.html) | Edit a variable, run code and save a personal notebook | [Colab](https://colab.research.google.com/github/yaminbens/alpha-mentorship/blob/main/notebooks/00_getting_started.ipynb) |
| [Task 1](https://yaminbens.github.io/alpha-mentorship/task-1.html) | Open a partition, observe mixing, count particles and plot | [Colab](https://colab.research.google.com/github/yaminbens/alpha-mentorship/blob/main/notebooks/10_home_explore.ipynb) |
| [Task 2](https://yaminbens.github.io/alpha-mentorship/task-2.html) | Change restitution, compare bouncing trajectories and calculate means | [Colab](https://colab.research.google.com/github/yaminbens/alpha-mentorship/blob/main/notebooks/11_home_compare.ipynb) |
| [Task 3](https://yaminbens.github.io/alpha-mentorship/task-3.html) | Complete motion and wall functions, a time loop and checks | [Colab](https://colab.research.google.com/github/yaminbens/alpha-mentorship/blob/main/notebooks/12_build_simulation.ipynb) |

An optional [combined Hebrew workbook](https://colab.research.google.com/github/yaminbens/alpha-mentorship/blob/main/notebooks/student_workbook_he.ipynb)
contains all four stages. Each activity also has its own page and notebook.

## Saving and feedback

Students save a personal Colab copy with **File → Save a copy in Drive**, then
share it with the designated mentor account through the agreed private channel.
Animations, plots, data and run settings must be downloaded and shared separately.
The website does not store student answers. Do not publish student records here.

Reflection invites students to describe what interested them, what felt easy or
difficult, and what they would like to explore next. Partial work is welcome;
there is no required report or grade. Code checks help debug the simulation.

If a Colab link fails, download the notebook from its website page, open
[Colab](https://colab.research.google.com/), choose **File → Upload notebook** and
save a personal Drive copy.

## Mentor resources

- [Coding track and feedback guide](mentor/hebrew_coding_track.md)
- [Reference implementation](mentor/coding_reference.py) — public, for consultation after an independent attempt
- [60-minute agenda](meetings/01_introduction/agenda.md)
- [Detailed Hebrew facilitator plan](meetings/01_introduction/facilitator_plan_he.md)
- [Hebrew presentation](https://yaminbens.github.io/alpha-mentorship/presentation/slides.html), [PDF](meetings/01_introduction/slides.pdf) and [guided demonstration](meetings/01_introduction/demonstration.md)
- [Review workflow](mentor/review_workflow.md) and [troubleshooting](mentor/troubleshooting.md)
- [Scientific extension notebooks](notebooks/) and [original browser track archive](archive/browser_track/README.md)
- [Project status](STATUS.md) and [implementation inventory](IMPLEMENTATION_PLAN.md)

The new coding models contain no forces between particles. Mixing does not
demonstrate melting, and particles near the floor are not evidence of a solid.
The presentation and browser demonstration introduce a separate interacting
molecular model; keep its observations distinct from the coding activities.

## Development and publication

This repository is independent of GNN and requires no GPU. The engine in
[simulation/teaching_particles.py](simulation/teaching_particles.py) is embedded
in the student notebooks so they can run independently.

```sh
python -m pip install -r requirements.txt
python tools/make_notebooks.py
python tools/build_site.py
python -m pytest tests -q
python tools/check_notebooks.py
python -m http.server 8000 --directory dist
```

[Site configuration](site/config.json) sets the repository and optional sharing
contacts. A push to `main` builds and publishes GitHub Pages. Source Markdown
links resolve on GitHub; the builder converts them into website URLs.
Keep repository documentation in English and the student website in Hebrew,
preserving its chapter navigation. See [contribution guidance](CONTRIBUTING.md),
[license](LICENSE) and [external sources](THIRD_PARTY.md).
