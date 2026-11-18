# Facilitating the Hebrew coding track

Students already know variables, conditions and loops. They want to write code
and see interesting results. Each activity connects a clear task, a code change,
a visible outcome and a check. Keep documentation brief and use direct,
respectful language.

## Schedule and activities

Keep the first meeting to 60 minutes, including one mentor-led demonstration and
20 minutes of Colab practice. The three full activities are independent work and
may span several sessions.

| Activity | Phenomenon | Programming tools | Possible material to discuss |
|---|---|---|---|
| 1 | Crossing and mixing after opening a partition | Counting with a loop and condition, array selection, plotting | Count, plot and closed/open animations |
| 2 | Sustained bouncing versus decay | Parameter lists, comparison loop, mean and maximum | Plot for several restitution values and final heights |
| 3 | Elastic particle trajectory in a square | Functions, return values, time loop and checks | Student code, eight checks and two animations |

## Facilitation

Begin with a brief visible change and invite students to describe what surprised
them. Help them identify the code that could affect it. Allow time to edit, run
and make mistakes before explaining. When debugging, identify the input, expected
output and actual result. Physical reasoning should help choose a measurement or
explain a result while students actively work with the code.

Design challenges have multiple possible solutions. Activity 1 seeks an opening
that meets a crossing target at a specified time; Activity 2 seeks restitution
that meets a height target. Preserve attempts that miss the target. A short run
with few particles need not produce a smooth graph or monotonic trend.

## Model boundaries

The first two activities use independent particles in a unit-length box. There
are no interparticle forces or collisions. Colour, height and mixing do not
establish temperature or phase.

Activity 1 uses elastic walls and a central partition with an opening. The engine
checks the crossing point at the partition. Activity 2 uses ballistic vertical
motion between impacts and solves impact times from the equation of motion.
After impact, the vertical speed magnitude is multiplied by restitution `e`.
Floor rebound speeds below 0.001 model speed units are treated as continuous
contact to represent the limit of repeated impacts. The notebook explains this
numerical rule.

Activity 3 has no gravity. Student code handles one impact per axis per step,
with `dt=0.02` and velocity components up to 1. The animation uses the trajectory
returned by student code. No hidden solution completes the functions; running an
unfinished template reports missing pieces rather than false success.

The presentation and browser demonstration use a separate Lennard–Jones model
with interparticle forces. Keep their data distinct from the new activities.

## Coding support and reflection

For Activity 1, add `count_right += 1` inside the condition. Use `plt.title` for
the title and `plt.savefig` before `show` to save the plot.

For Activity 2, compute `np.mean(final_y)` and add values to `cases`. Use
`np.max(final_y)` for a maximum. A fixed number that happens to match one run
does not implement a general calculation.

For Activity 3, consult the [reference code](coding_reference.py). It is public
but is not imported into learner notebooks. Invite students to explain their
code and demonstrate a changed input. Help them interpret a failed check rather
than focusing only on a passing result.

At the end, invite students to choose something to show. Discuss what interested
them, what came easily, what was difficult and what they want to explore next.
Partial work and unsuccessful ideas are welcome. There are no grades, mandatory
responses to every prompt or quotas of outputs. The
[Hebrew reflection page](../assignments/reflection_he.md) is included in each notebook.

Code checks provide technical feedback; their pass count is not a student grade.
Debug a small case together and choose the next step around the student's
interests and difficulties.

## Saving and review

The [student website](https://yaminbens.github.io/alpha-mentorship/) is the entry
point. Each activity page opens its own notebook; a combined workbook is also
available. Students save personal Drive copies and share them through a private
channel. Animations and plots must be saved and shared separately. Standalone
HTML animations and PNG images support review when interactive output is not
preserved in the notebook.
