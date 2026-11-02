---
title: "Query-Efficient Quantum Multi-Objective Optimization for Materials Configuration Search via Bayesian Weight Selection"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41788"
summary: "arXiv:2610.41788v1 Announce Type: cross Abstract: Materials design is a multi-objective problem, and recent advances in quantum optimization make it possible to bring quantum solvers to bear on such p"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41788v1 Announce Type: cross Abstract: Materials design is a multi-objective problem, and recent advances in quantum optimization make it possible to bring quantum solvers to bear on such problems. The realistic near-term win, though, is not raw quantum advantage but making an expensive, noisy quantum solver usable by spending its calls wisely. Quantum Approximate Multi-Objective Optimization (QAMOO) traces a Pareto front by solving a family of scalarized Ising problems, one per objective-weight vector, with QAOA --- but chooses those weights non-adaptively, sampling them at random, blind to what it has already found. We recast weight selection as multi-objective Bayesian optimization: our method, BW-QAMOO (Bayes-Weighted QAMOO), picks each next weight by expected hypervolume improvement (EHVI) under a Gaussian-process (GP) surrogate over the weight-to-objective map. On a frustrated alloy-configuration benchmark across min{3,4} objectives and nin{10,11,12} sites, BW-QAMOO reaches the same Pareto hypervolume as QAMOO's random sampling with a median 33% fewer scalarized solves across the 90/95% targets and 60--74% fewer than a uniform-grid baseline), on a genuine (simulated) QAOA solver; a paired Wilcoxon test confirms the saving is significant, and the advantage grows with the objective count m as the weight simplex expands and blind sampling wastes more of the budget. This is a query-efficiency result, and we close with the open challenges on the path to real alloy data and hardware.



## Related
- [[m-qam-mimo-maximum-likelihood-detection-with-qaoa-ml-rate-of|M-QAM MIMO Maximum-Likelihood Detection with QAOA: ML-Rate Offline Angle Design and Correlated Infinite-Size Spin-Glass Models]]
- [[empirical-quantum-advantage-in-constrained-optimization-from|Empirical Quantum Advantage in Constrained Optimization from Encoded Unitary Designs]]
- [[rate-optimal-quantum-discrete-simulation-optimization|Rate-Optimal Quantum Discrete Simulation Optimization]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41788) | 2026-11-02
