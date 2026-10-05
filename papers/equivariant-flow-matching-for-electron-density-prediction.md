---
title: "Equivariant Flow Matching for Electron Density Prediction"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.02651"
summary: "arXiv:2610.02651v1 Announce Type: new Abstract: Machine learning surrogates for density functional theory (DFT) have been increasingly used to reduce the cost of first-principles calculations. In this"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.02651v1 Announce Type: new Abstract: Machine learning surrogates for density functional theory (DFT) have been increasingly used to reduce the cost of first-principles calculations. In this arena, predicting real-space electron densities offers a scalable and transferable initialization for self-consistent field (SCF) procedures. However, current methods face a clear dilemma. That is, grid-based architectures incur a high computational cost, while basis-set methods fail to capture the structural correlations inherent in the coefficient space. Here, we develop OrbFlow, an SE(3)-equivariant generative model that predicts Gaussian-type orbital (GTO) coefficients via flow matching. OrbFlow retains the efficiency of a compact atom-centered basis while replacing pointwise regression with a learned probability path over the full coefficient space. It is trained through a two-phase trajectory curriculum that mitigates discretization drift during numerical integration. OrbFlow achieves state-of-the-art accuracy on QM9, reducing density error by 13.6% relative to the previous best model, and reduces error by 51% to 63% on every molecule of the MD benchmark relative to the strongest prior method sharing its basis. The predicted density also cuts SCF iterations by up to 68% with zero-shot transfer to unseen exchange-correlation functionals and recovers dipole and quadrupole moments to within a few percent of DFT references without any SCF calculation.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.02651) | 2026-10-05
