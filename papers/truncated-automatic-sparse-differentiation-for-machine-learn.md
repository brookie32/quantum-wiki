---
title: "Truncated automatic sparse differentiation for machine learning interatomic potentials"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.20510"
summary: "arXiv:2609.20510v1 Announce Type: new Abstract: Machine learning interatomic potentials (MLIPs) learn the mapping from atomic positions to potential energy. The forces, the negative gradient of this e"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2609.20510v1 Announce Type: new Abstract: Machine learning interatomic potentials (MLIPs) learn the mapping from atomic positions to potential energy. The forces, the negative gradient of this energy, drive molecular dynamics and are readily obtained using automatic differentiation. Higher-order derivatives, most notably the Hessian, describe collective motion and allow the direct prediction of experimental observables, but are considered computationally inaccessible for large systems. We suggest a solution: in physical systems, interactions decay with distance, and most MLIPs build on this locality through message passing up to a finite receptive field. This implies both sparsity of higher-order derivatives and their decay with distance. This structure can be exploited using automatic sparse differentiation (ASD). We explain how to compute the sparsity pattern for MLIP derivatives and demonstrate that, for multiple foundation MLIPs, ASD computes full Hessians of large porous materials exactly, but with modest speedups at best. The larger gains come from truncated ASD: discarding small, but nonzero, Hessian entries between distant atoms yields order-of-magnitude speedups with negligible impact on predicted observables.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.20510) | 2026-09-18
