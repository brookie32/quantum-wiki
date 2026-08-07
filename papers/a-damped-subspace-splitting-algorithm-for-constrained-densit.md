---
title: "A Damped Subspace Splitting Algorithm for Constrained Density Functional Theory"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.05682"
summary: "arXiv:2608.05682v1 Announce Type: cross Abstract: Constrained density functional theory (CDFT) provides a powerful framework for describing electronically excited and charge-localized states, which un"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.05682v1 Announce Type: cross Abstract: Constrained density functional theory (CDFT) provides a powerful framework for describing electronically excited and charge-localized states, which underlie a broad range of physical and chemical phenomena. However, the discretized optimization problems arising from CDFT calculations remain challenging, owing to the presence of both the Stiefel manifold constraint and additional nonconvex quadratic constraints. Existing algorithms either fail to enforce the quadratic constraints with high accuracy or face convergence issues due to double-loop iterative structures. In this paper, we first derive a subspace-splitting reformulation that decouples the two groups of constraints, by exploiting the inherent rotation invariance and introducing a nonlinear subspace alignment constraint. Based on this reformulation, we propose a single-loop damped alternating direction method of multipliers, called DASSP. To the best of our knowledge, DASSP is the first algorithm for CDFT calculations with rigorous convergence guarantees. Each iteration of DASSP comprises a spectral minimization step, a projected gradient step, and a damped dual ascent step, all of which admit efficient implementations. Numerical results on synthetic and realistic CDFT problems demonstrate that DASSP attains high feasibility accuracy and exhibits favorable efficiency without compromising robustness. We expect that this work will pave the way toward reliable and efficient large-scale CDFT applications.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.05682) | 2026-08-07
