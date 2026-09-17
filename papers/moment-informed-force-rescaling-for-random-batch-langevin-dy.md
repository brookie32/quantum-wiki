---
title: "Moment-informed force rescaling for random-batch Langevin dynamics"
date: "2026-09-17"
updated: "2026-09-17"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.18389"
summary: "arXiv:2609.18389v1 Announce Type: cross Abstract: Random-batch methods accelerate molecular dynamics by replacing full interaction sums with stochastic force estimators. In Langevin simulations, howev"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

arXiv:2609.18389v1 Announce Type: cross Abstract: Random-batch methods accelerate molecular dynamics by replacing full interaction sums with stochastic force estimators. In Langevin simulations, however, random-batch force errors can cause artificial heating and distort equilibrium and dynamical observables, especially for small batch sizes or under weak thermostat coupling. Moreover, the magnitude of these errors can vary across particles. We introduce moment-informed force rescaling for random-batch list (Mi-RBL) and random-batch Ewald (Mi-RBE) methods. A lagged average of each particle's sampled-force intensity sets an isotropic gain before the current batch is sampled, changing the random-batch force magnitude without changing its direction. The formal finite-time analysis quantifies the bias--variance tradeoff, and an estimate of the steady-state kinetic-temperature error predicts the scaling of the kinetic error with time step and thermostat friction. In the coexistence, binary-mixture, and electrolyte tests, Mi-RBL and Mi-RBE reduce kinetic errors and more closely reproduce the mean-square displacement, radial distribution function, and charge density profiles of the reference solutions. Mi-RBE also reduces the growth rate of the kinetic error with the time step by more than half and retains the predicted dependence on thermostat friction. The tested rescaling strength decreases with increasing batch size, and the particlewise update retains O(N) complexity for fixed batch size.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.18389) | 2026-09-17
