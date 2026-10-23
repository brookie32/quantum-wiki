---
title: "Unconstrained learning of equivariant atomistic properties"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.31183"
summary: "arXiv:2610.31183v1 Announce Type: new Abstract: Machine-learned interatomic potentials based on graph neural networks (GNNs) have made first-principles accuracy routine for the potential energy surfac"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2610.31183v1 Announce Type: new Abstract: Machine-learned interatomic potentials based on graph neural networks (GNNs) have made first-principles accuracy routine for the potential energy surface (PES). Their backbones, often O(3)-equivariant by design, are increasingly used to learn other atomistic properties. Many of these are of high angular order or pseudotensorial character, defined per atom, or expanded on large atom-centered basis sets. Such targets strain equivariant GNNs, whose tensor products grow steeply in cost with angular order and can fail to represent the target if truncated, forcing difficult trade-offs between hyperparameters. Unconstrained models like the Point-Edge Transformer (PET) instead replace explicit O(3) algebra with edge-to-edge attention and learn equivariance from data, so that the same backbone can in principle learn any equivariant property. We demonstrate how to use PET to learn molecular dipoles and polarizabilities, NMR chemical shielding tensors, and auxiliary-basis expansions of the electron density. Increasing the backbone size systematically improves both accuracy and equivariance error, and targeted architectural and training choices reduce the symmetry breaking further. PET matches or improves on the released reference models at lower inference cost and, compared with equivariant models, a smaller memory footprint. The predictions give accurate IR and Raman spectra and isotropic shieldings; the predicted densities accelerate self-consistent field calculations and give one-shot ground-state properties, and pretrained density models transfer to higher levels of theory by fine-tuning on little data. The impact of approximate equivariance is small for most observables, further validating this approach to train fast, accurate, and useful surrogate models for properties beyond the PES.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.31183) | 2026-10-23
