# Course status

## Active course

The student entry point is the [Hebrew GitHub Pages book](https://yaminbens.github.io/alpha-mentorship/).
It retains chapter navigation, a first-hour agenda, activity pages, readings,
saving/sharing instructions and further material. Repository documentation is
in English. Student notebooks and teaching assets intended for Hebrew use remain
in Hebrew.

The active track has a combined workbook and four separate notebooks: Colab
onboarding, partition opening and mixing, bouncing and dissipation, and writing
a particle-in-a-box simulation. It assumes familiarity with variables, conditions
and loops. Instructions use headings and flowing explanations.

Reading is integrated where ideas are applied: a Hebrew explanation, a specified
source passage and a connection to the code. English sources support further
reading. Reflection invites interests, easy and difficult moments, and desired
next steps. Partial work is welcome; no full report or grade is required. Code
checks support debugging.

There are nine website pages and ten active notebooks: five Hebrew notebooks and
five original English scientific extensions. Three original notebooks are retained
under `archive/browser_track` separately from the active course.

## Scientific scope

The new simulations are small, independent CPU examples with no interparticle
forces. They teach motion, boundary conditions and measurement; they do not establish
melting, equilibrium or properties of real materials. The browser demonstration
and further material use an interacting molecular model. Earlier data and the
presentation are preserved separately.

The first meeting remains one hour with a mentor-led demonstration and Colab
practice. Full exercises take place independently over as many sessions as needed.

## Validation

The existing course validation covers:

- 15 automated tests: source/site links, notebook structure, closed-partition
  crossing, elastic motion and energy conservation, dissipation, zero-gravity
  rest and a known impact time.
- The unfinished Activity 3 template reports missing code and does not generate
  a trajectory using a hidden solution. The reference passes; incorrect motion fails.
- Ten notebooks executed locally in fresh Python kernels, plus completed student
  paths for Activities 1–3. Running an empty template does not show that a student
  completed an activity.
- 18 browser checks across nine pages and two viewport widths. Standalone HTML
  animations and PNG plots support review outside Colab.
- Source Markdown links resolve inside GitHub and are converted to HTML links
  during the build, avoiding the former source-folder `task-0.html` error.

Evidence is stored under `validation/`, including `notebook_execution.json`,
`completed_student_paths.json` and `browser_checks.json`. Local tests do not verify
an authenticated student's Google account, Drive saving or sharing permissions.

## Publication and privacy

Source: https://github.com/yaminbens/alpha-mentorship

Website: https://yaminbens.github.io/alpha-mentorship/

The public repository includes mentor guidance and reference code. Reference code
is not imported into student notebooks. No real submissions, student details or
personal feedback belong here. The mentor supplies the sharing account and private
channel; access to shared notebooks and files must be checked using that account.
