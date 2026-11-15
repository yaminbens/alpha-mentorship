# Model and units
The classroom browser uses a 2D Lennard-Jones pair model with soft container walls.
Keep gravity off, no artificial bonds, no anchored particles and no fixed-temperature
particles for the energy-intervention exercise. Particle number N and box side L
remain fixed; number density is N/L². The force cutoff is 3 model diameters.
Record any different setting rather than silently combining it with this protocol.

The later Python example uses pinned Grazioli code in 2D with periodic boundaries,
N=16 and L=8. It is a separate teaching example, not matched browser data. Initial
velocities are random with a fixed seed; total momentum is removed. Dynamics have
no thermostat. The small time step is 0.002; record sampling interval and total time.

Lengths use sigma, energy epsilon, mass m; reduced time is sqrt(m sigma²/epsilon).
Temperature is k_B T/epsilon. Potential energy per particle is U/(N epsilon).
The pair cutoff is unshifted: small energy discontinuities at the cutoff are a model/
numerical limitation. The upstream pressure routine is not used for student conclusions.
Temperature is recomputed from sampled velocities using 2K/(dN), rather than trusting
an initial input or an intermediate integration readout.

Report preparation, discarded interval and observation window. Longer observation
and independent repeats are needed for a scientific study; the tiny examples only
teach operation and analysis. Never infer a bulk melting point from these examples.
