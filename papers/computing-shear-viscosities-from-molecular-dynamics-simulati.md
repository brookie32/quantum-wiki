---
title: "Computing Shear Viscosities from Molecular Dynamics Simulation: Comparing the OrthoBoXY Approach with the Green-Kubo Method"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.05845"
summary: "arXiv:2608.05845v1 Announce Type: cross Abstract: We calculated shear viscosities of 15 neat molecular liquids from equilibrium molecular dynamics (MD) simulations using the OrthoBoXY approach and com"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.05845v1 Announce Type: cross Abstract: We calculated shear viscosities of 15 neat molecular liquids from equilibrium molecular dynamics (MD) simulations using the OrthoBoXY approach and compare them to viscosities calculated via the Green-Kubo method. Data from both methods agree very well. Here, we show how to avoid pitfalls while computing the OrthoBoXY-data to obtain optimal results. From simulations of multiple system sizes, we could verify that the viscosity of molecular liquids is not influenced by finite size effects down to systems as small as 250 molecules. Moreover, we demonstrate that also the standard error of the viscosity is nearly independent of the system size. This is shown to be a consequence of a compensation effect of an increasing accuracy of the self-diffusion coefficients with increasing systems-size and the system-size dependent weighting according to the OrthoBoXY-equation. As a consequence, we suggest that it is preferable to run simulations of smaller systems with longer simulation times rather than larger systems with shorter simulation runs. In addition, we discuss a refinement of the recently introduced "recipe" for OrthoBoXY simulations block-lengths au_block. Based on data from simulations with varying run-lengths, we suggest the following modification: for highly viscous systems, the value of au_block might safely be scaled by a factor of 1/8, significantly reducing the computational resources needed. For less viscous systems, the value of au_block might safely be scaled by a factor of 1/4. For systems with high fluidity, the value of au_block should not be scaled down in order to achieve reliable results. When using a smaller system size of 250 molecules, these refinements are leading up to a 24-fold reduction in computational cost compared to the previous recommended set-up without sacrificing numerical accuracy.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.05845) | 2026-08-07
