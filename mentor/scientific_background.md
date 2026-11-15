# Scientific background
A simulation is a model plus a numerical method. Here particles obey classical motion.
Their pair potential is
$$
U(r)=4\epsilon[(\sigma/r)^{12}-(\sigma/r)^6].
$$
Here r is separation, sigma sets length and epsilon sets energy. Repulsion dominates
at small separation; attraction dominates at larger separation. The potential is a
simplification, not a universal model of all materials.

Reduced units set mass, sigma, epsilon and Boltzmann's constant to one. Temperature
is reported as k_B T / epsilon, time as t sqrt(epsilon/m)/sigma, and energy per particle
as E/(N epsilon). Do not label these temperatures kelvin without a physical mapping.
In d dimensions the teaching kinetic-temperature convention is T=2K/(dN), where K
is kinetic energy. Removing centre-of-mass motion can motivate a different degrees-
of-freedom convention; record the convention used rather than silently mixing them.

Adding energy is an intervention. In constant-energy dynamics, measured temperature
can change as kinetic and potential energy exchange. A stationary-looking average
is a diagnostic, not proof of equilibration. A small, short, two-dimensional trajectory
cannot establish a bulk material's equilibrium melting temperature.

Structure concerns arrangement: neighbour distances and local angular patterns.
Motion concerns how positions or neighbours change over time. Fast vibration alone
does not demonstrate a liquid. Energy per particle is not itself an order parameter.
Neighbour persistence is a dynamical measure: for each particle, retain the fraction
of its original k nearest neighbours after a fixed lag, then average over particles.
It depends on k, lag, boundaries, density and the trajectory ensemble.

For mutual information, define the random variables and population first. A classroom
example is paired outcomes X,Y from repeated fair-bit trials. Compare their joint law
P(X,Y) with independent draws P(X)P(Y). Population MI is a property of that law; a
finite count estimate has sampling error. Do not infer MI from one particle picture.
The introductory measurements do not validate thermodynamic entropy or the lab's
neural estimators.
