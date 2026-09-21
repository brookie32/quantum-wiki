---
title: "Structure-Aware Variance Reduction for Unbiased Randomized Hamiltonian Simulation"
date: "2026-09-21"
updated: "2026-09-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.23544"
summary: "arXiv:2606.23544v2 Announce Type: replace Abstract: Randomized Hamiltonian simulation methods are often governed by a trade-off between systematic bias and sampling overhead. We study how classical va"
last_verified: "2026-09-21"
review_by: "2026-12-20"
stale: false
---

arXiv:2606.23544v2 Announce Type: replace Abstract: Randomized Hamiltonian simulation methods are often governed by a trade-off between systematic bias and sampling overhead. We study how classical variance-reduction techniques can be applied to such methods without changing their mean channel, and therefore without introducing additional bias. As a motivating unbiased estimator, we formulate continuous time-evolution probabilistic angle interpolation (continuous TE-PAI), a quasiprobabilistic random-circuit protocol whose remaining Monte Carlo error is purely statistical. Continuous TE-PAI removes Trotter discretization error with finite-depth random circuits, whereas deterministic Trotterization does so only in the infinite-depth limit. Further, in tensor-network simulations, we demonstrate that discretization error can cause an unphysical exponential growth in the bond dimension required for Trotterized simulations, whereas comparable-depth continuous TE-PAI circuits avoid this growth. We then show that the variance of randomized product-formula-based estimators admits a canonical decomposition into a classical counting component and a quantum ordering component such that the dominant simulation overhead results from the non-commutative parts of the Hamiltonian dynamics. Motivated by this decomposition, we achieve an approx70% error-reduction using the counting-component for small systems whereas our tensor-network simulations of n=30 spin-chain dynamics use coarser statistics tailored to the observable and estimator attaining a negligible bias and a reduction of approx 80% leading to approx91% and approx96% sampling-cost reductions, respectively.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.23544) | 2026-09-21
