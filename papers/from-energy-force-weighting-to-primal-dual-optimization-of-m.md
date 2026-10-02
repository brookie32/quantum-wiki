---
title: "From Energy-Force Weighting to Primal-Dual Optimization of Machine-Learned Interatomic Potentials"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.00876"
summary: "arXiv:2610.00876v1 Announce Type: cross Abstract: Machine-learned interatomic potentials are commonly fitted by weighted-sum scalarization, which combines energy and force errors in a single loss. A n"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.00876v1 Announce Type: cross Abstract: Machine-learned interatomic potentials are commonly fitted by weighted-sum scalarization, which combines energy and force errors in a single loss. A nominal weight, however, identifies a potential only relative to the complete fitting protocol. We therefore treat energy--force balancing as a protocol-dependent problem of physical model selection. For fixed-basis atomic cluster expansion models of molten LiCl, liquid H_2O, and Si, the resulting scalarization paths contain dominated states at extreme weights. Their nondominated subsets depend on the solver, and the out-of-distribution Si path is nonmonotone. We replace direct weight selection by minimizing the regularized energy objective subject to an upper bound on the normalized force loss. Projected dual ascent adjusts the Lagrange multiplier from the force-constraint residual. A frozen-multiplier limited-memory quasi-Newton refinement then returns the final model. Across the three systems, the constrained procedure reaches the solver-matched low-error region and gives measured speedups of 6.7--8.9 over completed scalarization scans under the stated timing convention. Physical-property calculations show that first-shell geometry is comparatively insensitive to the selected balance, whereas transport and solid-state observables vary more strongly. These results identify the fitted model--protocol pair as the relevant object of energy--force model selection and support force-constrained fitting as an explicit selection rule.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.00876) | 2026-10-02
