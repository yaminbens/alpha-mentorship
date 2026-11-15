# Browser simulation guide
Use [Schroeder's Interactive Molecular Dynamics](https://physics.weber.edu/schroeder/md/).
The demonstration and homework use 64 particles in a square of side 12, with gravity
off, no added bonds, no anchored particles and no fixed-temperature particles.
Lengths and times use reduced model units; temperatures are not automatically kelvin.

## Load a reproducible starting state
1. Download **ordered_initial.txt** from the course page or use the file in
   `meetings/01_introduction/presets/`.
2. Pause the simulator. Open **Data**, paste the file's complete text into the data
   box and click **Input state**. Keep a copy of the file you loaded.
3. Check N=64, box side=12, gravity=0 and time step=0.005. The file specifies all
   particle positions and velocities. It is a seeded triangular starting arrangement.
4. Set **Steps per frame** to 200 and press **Step** five times. This advances 1000
   steps, or 5 reduced time units. This preparation is used before every comparison.

## Guided demonstration
Predict what adding energy will change. From the prepared state, use **Faster** to
increase speeds. The rehearsed high condition uses 24 clicks while paused. Keep
particle count and box fixed. Press Step five times, then observe the motion and
arrangement. Show the low/high recorded screenshots if live access fails. A disordered
snapshot is not a demonstrated equilibrium liquid phase.

## Three conditions at home
Reload the same initial state and perform the 1000-step preparation each time.
Use 0, 8 and 24 Faster clicks for low, middle and high energy preparations. The speed
multipliers are respectively 1, about 2.144 and about 9.850; they are not temperatures.
After the intervention, take another 1000 steps as a recorded settling interval.
This is a classroom protocol, not a proof of equilibration.

## Record a measurement window
Press **Reset stats** after settling; this resets the displayed time/statistics,
not the particle state. Open Data, choose **System totals** and **More detail**.
Clear old data. Set Steps per frame to 25. Repeat **Step**, then **Write data**, 40
 times. This records a 5-unit window in increments of 0.125. Copy the tab-separated
data into a text file and save it outside the simulator.

The detailed export includes N, KE and PE. Average KE/N for temperature in this 2D
unanchored model, and PE/N for potential energy per particle across the recorded
rows. The displayed T column can be a running average; do not treat that column as
an independent instantaneous sample. Notebook 02 includes a helper for the detailed
export. Save screenshots and record settings, preparation and the measurement window.

Repeat the middle condition from the same saved state. Exact replay checks the
procedure; it is not an independent-seed uncertainty estimate. A broader study needs
independent preparations and sampling diagnostics. Preserve unexpected outcomes.

## Source and fallback
The simulator's page documents its physics and controls. The course contains an
attributed recording, screenshots, starting states and measured example data from
an automated browser rehearsal. Use them as labelled examples if access fails.
