# Worked example — measured browser rehearsal
This is mentor-prepared teaching data, not a student submission or validated phase study.
Question: how do measured temperature and potential energy change after the documented
speed interventions? Prediction: increasing kinetic energy will raise measured temperature,
while the configuration and potential energy may also change.

Model: 64 unbonded particles, box side 12, gravity zero, soft walls and dt=0.005.
Starting state: ordered_initial.txt. Run 1000 steps, apply 0/8/24 Faster clicks, run
1000 settling steps, reset statistics and record 40 samples every 25 steps. The
measurement window spans 5 reduced time units. Files: data/examples/browser_*.csv.

| Preparation | Faster clicks | Mean reduced T | Mean U/N |
|---|---|---|---|
| low | 0 | 0.026422 | -2.680812 |
| middle | 8 | 0.071206 | -2.631925 |
| middle_repeat | 8 | 0.071206 | -2.631925 |
| high | 24 | 0.991434 | -1.143934 |

In this short observation, the higher-energy preparation has higher measured temperature
and less negative potential energy per particle. The high-energy snapshot is visibly
less ordered than the low-energy snapshot. These observations motivate a quantitative
neighbour measurement; the energy table alone does not classify a phase. The repeated
middle preparation exactly replays the same saved initial state, so its agreement checks
reproducibility rather than independent-run robustness. Finite size, short duration and
preparation history limit interpretation. No equilibrium melting temperature is inferred.
A next step would define neighbour persistence and compare it at a fixed lag across
independent preparations. The plotted conditions should retain their settings and units.
