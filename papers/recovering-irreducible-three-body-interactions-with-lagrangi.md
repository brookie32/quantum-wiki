---
title: "Recovering Irreducible Three-Body Interactions with Lagrangian Neural Networks"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-atom-ph]
url: "https://arxiv.org/abs/2610.13292"
summary: "arXiv:2610.13292v1 Announce Type: cross Abstract: Lagrangian Neural Networks (LNNs) learn mechanical systems from trajectory data by parameterizing a scalar Lagrangian and deriving the dynamics throug"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2610.13292v1 Announce Type: cross Abstract: Lagrangian Neural Networks (LNNs) learn mechanical systems from trajectory data by parameterizing a scalar Lagrangian and deriving the dynamics through the Euler-Lagrange equations, biasing the model toward motion that respects the variational structure of mechanics. The interactions studied so far have been pairwise-additive, leaving open whether LNNs can recover an irreducible many-body interaction from motion alone. We address this using the Axilrod-Teller triple-dipole interaction, the leading three-body dispersion term, whose dependence on the collective geometry of three particles cannot be represented by any sum of pairwise terms. We prescribe the kinetic energy exactly and learn only the potential, as a function of interparticle distances and angles. Combined with a signal-aware sampling strategy that concentrates training data where the three-body signal is strongest while preserving broad coverage of configuration space, this recovers the interaction from accelerations alone. The learned potential reproduces the radial scaling, angular dependence, and characteristic sign reversal of the Axilrod-Teller interaction, and generates stable trajectories. Embedding it within a pairwise Lennard-Jones potential lets us examine its observability: the three-body term is recovered once its dynamical signature exceeds the residual modeling error, which it does cleanly at amplified coupling but not at the coupling of a real noble gas, bracketing the transition between the two. Finally, symbolic regression on the trained potential, with no assumed functional form, returns the Axilrod-Teller expression with angular numerator, radial law, and coupling constant intact. An LNN with domain-specific structure can thus recover an irreducible three-body interaction from trajectories as a closed-form law, pointing toward learning interaction laws whose structure is not known a priori.

**Source:** [arXiv physics.atom-ph](https://arxiv.org/abs/2610.13292) | 2026-10-12
