# Guided classroom demonstration

Duration: 12 minutes, within the 60-minute introductory meeting. The mentor runs
one demonstration on the projector. Students predict, observe and discuss.
They conduct the full simulation experiment independently at home.

## Question

**What changes when we add energy to an ordered collection of atoms?**

Use [Schroeder's browser simulation](https://physics.weber.edu/schroeder/md/).
It uses a two-dimensional Lennard-Jones model. The Faster control increases
particle speeds; it does not change animation playback alone. The displayed
temperature follows from kinetic energy in the simulator's reduced units.
See the linked page for the model and control definitions.

## Before the meeting

- Rehearse a small, ordered, unbonded configuration with gravity off. Keep particle
  count and box size fixed during the comparison. Avoid fixed atoms and added bonds
  that would alter the intended model.
- Record and save the initial state, settings and preparation procedure. The recorded
  setup uses N=64, L=12, dt=0.005 and 24 Faster clicks after 1000 preparation steps.
  See ../../simulation/browser_guide.md for the exact controls.
- Confirm that the motion and controls are legible on the projector.
- Retain screenshots or a recording of the rehearsed example for connection
  problems. Label these as recorded observations if used.

## Twelve-minute sequence

| Elapsed time | Mentor action | Student prompt |
|---|---|---|
| 0–2 minutes | Show the ordered state running, then pause | Are the atoms stationary? What makes this look solid-like? |
| 2–4 minutes | Point to particle count, box size and temperature; explain the energy control | If we add energy, what do you predict will change? |
| 4–7 minutes | Resume and use the rehearsed heating increments; hold other settings fixed | What changed in the motion? Are neighbours changing? |
| 7–9 minutes | Observe after the intervention; compare with the initial state | Does faster motion necessarily mean a liquid? What else would you check? |
| 9–12 minutes | Show where numerical data can be read/exported; explain the homework | Which quantities would you keep fixed, record and compare at home? |

Do not rely on observing a phase transition within twelve minutes. If the system
remains ordered, use that observation to distinguish faster vibration from loss
of order. Discuss the actual outcome without calling an ambiguous state liquid.

## Transition to Colab

Explain that the browser produces observations and the notebook holds predictions,
data, plots and explanations. Open the introductory notebook and demonstrate saving
a personal copy. Use labelled example data for this part; students collect their
own three-condition comparison at home.

## Readiness

The external browser model has been rehearsed automatically. Saved initial and final
states, screenshots, a recording and measurement files are included. See presets/metadata.json
for observations and limitations. The mentor should still rehearse the projector and
pace on the actual classroom laptop. No equilibrium phase behaviour is certified.
