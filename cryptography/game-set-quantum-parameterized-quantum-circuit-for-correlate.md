---
title: "Game, Set, Quantum: Parameterized Quantum Circuit for Correlated Equilibrium in Bayesian Games"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.03109"
summary: "arXiv:2606.03109v2 Announce Type: replace Abstract: Strategic decision-making among many agents under incomplete information is central to economics, security, and multi-agent artificial intelligence "
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

arXiv:2606.03109v2 Announce Type: replace Abstract: Strategic decision-making among many agents under incomplete information is central to economics, security, and multi-agent artificial intelligence (AI). Computing equilibria in such settings is challenging because the joint type-action space grows exponentially with the number of players. In binary-type, binary-action Bayesian games with n players, an explicit representation over type-action profiles requires O(2^{2n}) entries, making direct linear-programming (LP) formulations increasingly costly as n grows. We propose a hybrid quantum-classical framework for approximating Bayes correlated equilibrium (BCE) using a parameterized quantum circuit (PQC). The PQC represents the conditional distribution over joint actions using O(nL) trainable parameters, where L denotes the circuit depth; for the largest trained setting, n=8 and L=2, this corresponds to 48 trainable angles. Each player count is trained independently by maximizing expected social welfare with a penalty on positive aggregated BCE obedience violations. On a strategically coupled Bayesian congestion game with n=2,4,6,8 players, feasible PQC solutions attain higher welfare than MCCFR and DCFR product-strategy baselines while satisfying epsilon_{max}leq10^{-3}, where epsilon_{max} denotes the maximum positive aggregated BCE obedience violation. Across five independent runs per setting, all runs are feasible for n=2,4,6, while four of five are feasible for n=8. PQC welfare remains below the exact LP optimum, with the absolute gap increasing with n, while classical state-vector simulation prevents PQC training beyond eight players. These results demonstrate the use of a compact PQC parameterization for approximate equilibrium computation and quantify its welfare, feasibility, and classical simulation scaling on the studied benchmark.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.03109) | 2026-08-24
