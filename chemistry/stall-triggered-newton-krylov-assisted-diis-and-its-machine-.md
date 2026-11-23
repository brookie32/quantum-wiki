---
title: "Stall-Triggered Newton-Krylov-Assisted DIIS and Its Machine-Learning-Accelerated Variant for CCSD Convergence"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.27705"
summary: "arXiv:2611.27705v1 Announce Type: new Abstract: The iterative solution of the non-linear amplitude equations of coupled-cluster singles doubles (CCSD) theory can encounter convergence instabilities, a"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2611.27705v1 Announce Type: new Abstract: The iterative solution of the non-linear amplitude equations of coupled-cluster singles doubles (CCSD) theory can encounter convergence instabilities, asymptotic convergence or outright divergence. Direct Inversion in the Iterative Subspace (DIIS) is a widely used extrapolation technique but can also exhibit slow or oscillatory convergence in challenging regimes. In this work, we introduce a robust hybrid solver: Stall-Triggered Newton-Krylov Assisted DIIS ({}{st}NK-DIIS) alongside its machine-learning accelerated variant {}{st}NK^{ML}-DIIS which leverages the robust convergence of Newton-Krylov (NK) while avoiding the high computational cost of Krylov iterations. In our methods, DIIS remains the default accelerator and a matrix-free NK procedure is activated when sustained stagnation or divergence is detected with each NK step verified using the non-linear residual before acceptance. To alleviate the cost of Krylov iterations the {}{st}NK^{ML}-DIIS uses a gated recurrent unit (GRU) to predict a scalar logarithmic step-size ratio along the approximately computed Newton direction. When the ML-predicted step fails residual-based verification, the method falls back to a grid-based NK line search. Using CCSD as the underlying electronic-structure theory, we evaluate these methods against conventional DIIS and pure NK for stretched molecules exhibiting convergence difficulties in terms of residual convergence, iteration counts, and wall-time performance. These protocols may be generalizable to other non-linear equation solvers as well, as the ML model learns the convergence pattern of the variables and does not require system-specific knowledge such as atom identities or molecular orbital properties. This allows transferability across atom-type, bonding character and basis-sets.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.27705) | 2026-11-23
