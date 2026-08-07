---
title: "Next Generation of Ultra-Coarse-Graining: Self-Consistent Inference of Critical Internal States"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.05388"
summary: "arXiv:2608.05388v1 Announce Type: new Abstract: Bottom-up coarse-graining expands the length and time scales accessible to molecular dynamics (MD) simulations, but information loss can hinder accurate"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.05388v1 Announce Type: new Abstract: Bottom-up coarse-graining expands the length and time scales accessible to molecular dynamics (MD) simulations, but information loss can hinder accurate representation of multistate phenomena in complex biomolecular dynamics. Ultra-Coarse-Graining (UCG) projects discrete "quantum-like" extended degrees of freedom, or "internal states," onto coarse-grained (CG) molecules, extending CG model expressiveness. The rapid-local-equilibrium (RLE) approximation in UCG depends on user-defined collective variables (CVs, e.g., local density) and neglects correlations between internal states within and between CG molecules. We present Self-Consistent UCG (SC-UCG), which uses the underlying UCG interactions directly to assign internal states without designing CVs in the CG ensemble. During simulation, internal state probabilities are determined self-consistently through graph message passing. We enhance the RLE Hamiltonian with the Bethe approximation and AI-based inference to represent explicit correlations between UCG beads. For force-field training, we develop Multilayer Internal State Consistency (MISC), a machine-learning method derived from relative entropy minimization that avoids iterative sampling of intermediate force fields. We apply SC-UCG to a tetramer exhibiting a second-order symmetry-breaking phase transition from a supercritical racemic fluid to subcritical D-rich and L-rich fluids. SC-UCG captures collective switching of internal states in the subcritical region and recapitulates the phase transition across temperatures, despite being trained on a single-temperature dataset.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.05388) | 2026-08-07
