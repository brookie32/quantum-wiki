---
title: "Active learning and explicit electrostatics enable accurate modeling of electrolytes"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2510.03479"
summary: "arXiv:2510.03479v4 Announce Type: replace Abstract: Machine learning interatomic potentials (MLIPs) combine near-ab initio accuracy with the computational efficiency of classical force fields, making "
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2510.03479v4 Announce Type: replace Abstract: Machine learning interatomic potentials (MLIPs) combine near-ab initio accuracy with the computational efficiency of classical force fields, making them promising tools for modeling molecular liquids and electrolytes. Their predictive accuracy depends strongly on the diversity of the training set, while the explicit treatment of electrostatics is increasingly recognized as an important factor in improving their performance. In this work, we assess the impact of incorporating explicit electrostatics and environment-dependence of atomic charges by comparing short-ranged Moment Tensor Potentials (MTPs) with electrostatics-augmented MTPs, including fixed-charge and environment-dependent charge models. To this end, we employ D-optimality-based active learning (AL) to train short-ranged MTPs and extend the AL procedure, previously unavailable for long-range electrostatics-augmented MTPs, to these models, enabling largely automated generation of diverse training sets for pure ethylene carbonate (EC) and ethyl methyl carbonate (EMC), their mixtures, and LiPF6 solutions. For EC, EMC, and their mixtures, electrostatics-augmented MTPs achieve accuracy comparable to or better than that of their short-ranged counterparts while requiring fewer machine-learned parameters. For LiPF6 solutions, however, a notable improvement in accuracy is achieved only with environment-dependent charges, which also enhance stability in large-scale molecular dynamics simulations, unlike the fixed-charge model. The resulting short-ranged MTPs and environment-dependent-charge models reproduce experimental densities with mean absolute deviations of 0.2-6% and ionic conductivities with deviations of 11-15%, while capturing the experimentally observed temperature dependence of conductivity.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2510.03479) | 2026-11-09
