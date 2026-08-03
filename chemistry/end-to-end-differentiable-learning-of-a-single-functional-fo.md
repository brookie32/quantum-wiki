---
title: "End-to-End Differentiable Learning of a Single Functional for DFT and Linear-Response TDDFT"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2602.05345"
summary: "arXiv:2602.05345v3 Announce Type: replace Abstract: Density functional theory (DFT) and linear-response time-dependent density functional theory (LR-TDDFT) rely on an exchange-correlation (xc) approxi"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

arXiv:2602.05345v3 Announce Type: replace Abstract: Density functional theory (DFT) and linear-response time-dependent density functional theory (LR-TDDFT) rely on an exchange-correlation (xc) approximation that provides not only energy but also its functional derivatives that enter the self-consistent potential and the response kernel. Here, we present an end-to-end differentiable workflow to optimize a single deep-learned energy functional using targets from both Kohn-Sham DFT and adiabatic LR-TDDFT. To enable this training in a computationally efficient and differentiable manner, we developed a JAX-based two-component quantum chemistry package (IQC), in which the learned functional provides a self-consistent potential and linear-response kernel via automatic differentiation. This construction permits gradient-based optimization through both the self-consistent-field (SCF) fixed-point equations and the Casida eigenvalue problem. We learn an exchange-correlation functional on excitation energies and ground-state properties (noncovalent interactions, thermochemistry, bond dissociation, ionization potentials, electron affinities, isomerization energies, and reaction barriers) while incorporating one-electron self-interaction cancelation as penalty terms, and we assess its possible transfer to molecular test cases.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2602.05345) | 2026-08-03
