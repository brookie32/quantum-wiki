---
title: "Learning the Kohn-Sham map with neural operators for quasi-linear scaling density functional theory"
date: "2026-08-26"
updated: "2026-08-26"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.23895"
summary: "arXiv:2608.23895v1 Announce Type: new Abstract: Kohn--Sham density functional theory (DFT) underpins electronic-structure simulations, but repeated orbital diagonalizations lead to cubic scaling, rest"
last_verified: "2026-08-26"
review_by: "2026-11-24"
stale: false
---

arXiv:2608.23895v1 Announce Type: new Abstract: Kohn--Sham density functional theory (DFT) underpins electronic-structure simulations, but repeated orbital diagonalizations lead to cubic scaling, restricting quantum calculations to modest scales only. Eliminating these auxiliary orbitals while retaining Kohn--Sham accuracy is the central goal of orbital-free DFT, but both analytical and machine-learning methods have so far fallen short. Prior learning approaches either try to learn the variational kinetic-energy functionals, which are ill-conditioned, or directly predict the ground state, which extrapolate poorly to larger systems. Instead, we identify the Kohn--Sham map as the right learning target for orbital-free DFT. It maps a Kohn--Sham potential directly to the corresponding density and noninteracting kinetic energy, quantities otherwise obtained through an orbital diagonalization. Focusing on the density component in this work, a domain-invariant SE(3)-equivariant Fourier neural operator learns to predict it from the potential as input on real-space grids, enabling stable quasi-linear scaling SCFs. Trained jointly on 8,504 molecules and solids, a single model generalizes to out-of-distribution organic molecules, insulators, and metals. For the first time, the same method converges SCFs across these systems without explicitly constructing Kohn--Sham orbitals, while reproducing densities, electronic spectra, and structural observables at Kohn--Sham DFT accuracy. Linear-scaling SCFs additionally allow converging magnesium dislocation densities containing up to 82,500 valence electrons on a single GPU.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.23895) | 2026-08-26
