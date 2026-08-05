---
title: "PACE-QAOA: Physics-Constrained Quantum Optimization for Qubit-Efficient Power System Islanding"
date: "2026-08-05"
updated: "2026-08-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.02789"
summary: "arXiv:2608.02789v1 Announce Type: new Abstract: Controlled islanding partitions a stressed power network to limit disrupted power transfer while preserving operational integrity in every island. This "
last_verified: "2026-08-05"
review_by: "2026-11-03"
stale: false
---

arXiv:2608.02789v1 Announce Type: new Abstract: Controlled islanding partitions a stressed power network to limit disrupted power transfer while preserving operational integrity in every island. This NP-hard partitioning problem becomes increasingly demanding as networks grow, motivating quantum optimization as a complementary approach. However, limited qubit capacity restricts the scale at which conventional QAOA can address islanding. This paper develops a qubit-efficient hybrid quantum formulation that overcomes this barrier. A physics-informed compact encoding captures essential islanding decisions while exploiting grid structure, with formal guarantees preserving the feasible solution space and optimization objective. A qubit-efficient Lagrangian strategy combines quantum optimization with classical refinement to enforce operational constraints. Complexity analysis shows that for fixed island counts on sparse graphs, the formulation reduces phase-separator and per-layer gate complexity from quadratic to linear scaling. Evaluations on eight IEEE systems (9 to 89 buses) across multiple quantum backends produce feasible, high-quality solutions under practical circuit and sampling budgets. Factorial ablation attributes resource and runtime gains to the complementary effects of compact encoding and qubit-efficient Lagrangian constraint handling. Noise analysis demonstrates stable solution quality under device noise, and landscape diagnostics reveal smoother, more consistently scaled QAOA cost surfaces. These results provide a transferable pathway for scaling constrained quantum optimization toward larger real-world applications on near-term hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.02789) | 2026-08-05
