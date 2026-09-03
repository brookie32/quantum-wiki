---
title: "RBMD 2.0: Random batch molecular dynamics package for large-scale simulations on multi-GPU architectures"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.02694"
summary: "arXiv:2609.02694v1 Announce Type: cross Abstract: Large-scale molecular dynamics simulations of particle systems on multi-GPU architectures are often constrained by the computational and communication"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.02694v1 Announce Type: cross Abstract: Large-scale molecular dynamics simulations of particle systems on multi-GPU architectures are often constrained by the computational and communication costs of nonbonded force evaluation. We present RBMD 2.0, a major new release of the random batch molecular dynamics package designed for cross-node multi-GPU simulations of large-scale systems. It combines the improved random batch Ewald method with three-dimensional domain decomposition and ghost-particle communication to accelerate multi-GPU nonbonded force evaluation, while the DTK CUDA framework facilitates portability across heterogeneous accelerator architectures. Numerical experiments on multiple benchmark systems demonstrate both the accuracy and efficiency of simulations with RBMD 2.0. For simulations involving up to hundreds of millions of particles across multiple accelerator devices, one achieves speedups ranging from severalfold to approximately two orders of magnitude in nonbonded force evaluation while exhibiting over 97.5% weak-scaling behavior. These results demonstrate the promising nature of RBMD 2.0 as a computational engine for future exascale molecular dynamics simulations.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.02694) | 2026-09-03
