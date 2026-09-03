---
title: "Quantum Speedups for Sampling and Non-convex Optimization with Stochastic Oracles"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2504.03626"
summary: "arXiv:2504.03626v2 Announce Type: replace Abstract: We present quantum speedups for sampling from distributions of the form pipropto e^{-f} on R^d. We consider two stochastic oracle models: a stochast"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2504.03626v2 Announce Type: replace Abstract: We present quantum speedups for sampling from distributions of the form pipropto e^{-f} on R^d. We consider two stochastic oracle models: a stochastic gradient oracle, where f=frac{1}{n}sum_{i=1}^n f_i and component gradients {nabla f_i}_{i in [n]} are available, and a stochastic evaluation oracle, where only noisy values of f are available. Our framework accelerates classical stochastic Langevin Monte Carlo (LMC) and Hamiltonian Monte Carlo (HMC) algorithms by replacing stochastic gradient estimators with variance-controlled quantum mean estimation and gradient estimation subroutines. Unlike quantum walk based approaches, our algorithms do not require reversibility or exact gradients, and they preserve the structure of the underlying Markov chain. In the finite-sum setting, quantum mean estimation combined with classical variance-reduction techniques improves the stochastic gradient-query complexity for the approximate sampling task. In the stochastic zeroth-order setting, we develop gradient estimators robust to noisy function evaluations, yielding improved evaluation complexity for LMC and HMC. These results apply to strongly log-concave and/or non-log-concave distributions satisfying a log-Sobolev inequality, with convergence guarantees in Wasserstein distance and Kullback--Leibler divergence. We also show that faster sampling methods lead to quantum speedups for optimization, including for non-smooth and approximately convex objectives.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2504.03626) | 2026-09-03
