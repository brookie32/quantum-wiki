---
title: "Exact periodic electrostatics for latent-charge machine-learning potentials"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.06575"
summary: "arXiv:2611.06575v1 Announce Type: new Abstract: Machine-learning interatomic potentials of the latent Ewald summation (LES) type learn atomic charges from energies and forces and evaluate their electr"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.06575v1 Announce Type: new Abstract: Machine-learning interatomic potentials of the latent Ewald summation (LES) type learn atomic charges from energies and forces and evaluate their electrostatic energy in reciprocal space. I formulate this long-range term as a smeared Epstein-Hurwitz lattice sum and derive its exact periodic structure: a decomposition isolating a net-charge artefact and a local self-energy, an image theorem for cells of any shape, and the forces and virial. Full charge equilibration, LES with induced charges, constrained and unconstrained LES models and fixed-charge force fields follow as successive approximations of one variational problem, whose diagonal-hardness limit is a projection of the latent charges onto fixed total charge, which I call projected latent Ewald summation (pLES). Energies and forces determine the latent charges only up to a gauge, so fragment-level rather than atom-level charge quantization is the consistent target. The latent channel is guaranteed to be a dielectric only if charge is conserved locally; charges that are local functions of the environment and conserved only globally can screen like a conductor. pLES is implemented in the atomic cluster expansion and in LAMMPS, and the exact identities hold to machine precision, also for trained models. For charged NaCl clusters, pLES recovers the total charge that an unconstrained model misses by up to 1.8 e and reduces the test errors of a short-range model from 1.44 to 0.42 meV/atom and from 37 to 13 meV/{AA}. In two water datasets, constrained and unconstrained models learn the same latent charges up to sign and scale. In molecular dynamics of pLES water, fluctuating molecular charges dominate the screening at all accessible wavelengths; a crossover model excludes a conductor and gives a latent dielectric constant between 19 and 71; molecular charges are compensated over about 1 nm, beyond the training cells.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.06575) | 2026-11-05
