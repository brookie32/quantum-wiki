---
title: "Sample Complexity for Generative Learning of Quantum Measurement Data"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.38028"
summary: "arXiv:2610.38028v2 Announce Type: replace Abstract: Generative learning of a quantum measurement distribution from finite data requires choosing a model capacity that balances representation accuracy "
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.38028v2 Announce Type: replace Abstract: Generative learning of a quantum measurement distribution from finite data requires choosing a model capacity that balances representation accuracy against estimation cost. We develop a bias-variance framework that decomposes the expected population Kullback-Leibler error at model capacity s and sample size N as E(s,N)=B(s)+V(s,N), with representation bias B and a variance term V capturing the mean estimation error. In the well-sampled regime, V(s,N)simeq[NC(s)]^{-1}, and exponential or algebraic laws for B and C yield four scaling templates for the optimal error, from inverse powers of N to inverse powers of ln N. For local autoregressive models, the context radius sets the model capacity, and B is the summed conditional mutual information lost by truncating the context. For a smoothed histogram learner, we derive an exact finite-sample estimation cost that accounts for rarely observed contexts and recovers the parameter-count law in the well-sampled regime. For transverse-field Ising Born distributions, the independently evaluated bias and estimation cost predict both the optimal context radius and the optimal error. In the well-sampled regime, the estimation cost grows exponentially with context radius. Its competition with approximately exponential bias decay in the gapped regimes predicts power-law error decay in N, while algebraic bias decay at criticality predicts asymptotic inverse-power decay in ln N. Bulk-site results are consistent with the corresponding finite-sample predictions. These results connect the structure of quantum measurement distributions to the model capacity justified by finite data.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.38028) | 2026-11-02
