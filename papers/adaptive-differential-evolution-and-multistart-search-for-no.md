---
title: "Adaptive Differential Evolution and Multistart Search for Noisy QAOA Optimization"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.23180"
summary: "arXiv:2609.23180v1 Announce Type: new Abstract: We benchmark classical optimization of a fixed low-depth Quantum Approximate Optimization Algorithm (QAOA) ansatz across four cost-Hamiltonian families "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.23180v1 Announce Type: new Abstract: We benchmark classical optimization of a fixed low-depth Quantum Approximate Optimization Algorithm (QAOA) ansatz across four cost-Hamiltonian families at N=12, p=3, and D=6. Ten optimizers are compared over 25 independent runs under common ceilings of 10,000 and 30,000 function evaluations (FEs), first with exact statevector objectives and then with two additive observation-noise levels. Exact objectives favor multistart BFGS and multistart CMA-ES. Under noisy feedback, adaptive population methods become more competitive, but the ranking depends on whether performance is measured by the best exact point visited or by the point selected from noisy observations. A targeted extension over all three pre-screened instances per family confirms this regime change while showing that named adaptive-DE winners are instance dependent: jSO-lite leads low-noise oracle search, iL-SHADE high-noise oracle search, and L-SRTDE high-noise selected solutions in the equal-instance summaries. Bootstrap analysis quantifies a non-negligible high-noise search--selection gap, and a retrospective fixed-budget verification proxy shows that reserving a small measurement budget for final re-evaluation improves selected quality across all ten methods at 30,000 FEs. A supplementary structure-aware study further shows that QAOA cross-depth restriction and continuous basin refinement are more useful in these conditions than standalone Monte Carlo tree-search selection. Overall, optimizer choice depends jointly on landscape structure, observation noise, and final-point identification.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.23180) | 2026-09-22
