---
title: "Quantum Speedups for Log-Concave Sampling from Local Structure"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.20253"
summary: "arXiv:2609.20253v1 Announce Type: new Abstract: For a convex function f olon R^d o R, the problem of sampling from a distribution proportional to e^{-f(x)} is called log-concave sampling. In many prac"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2609.20253v1 Announce Type: new Abstract: For a convex function f olon R^d o R, the problem of sampling from a distribution proportional to e^{-f(x)} is called log-concave sampling. In many practical scenarios, the function f(x) turns out to admit a local decomposition f(x) = sum_{a=1}^R psi_a(x_{S_a}). In this paper, we consider log-concave sampling using local queries, i.e., evaluation and gradient queries to each clause psi_a(dot), which can be computationally much cheaper than the queries to f(x) itself. We show that if each coordinate appears in only a small number of clauses, there is a quantum algorithm for strongly log-concave sampling using widetilde{O}(sqrt{kappa}d) local queries, where kappa is the condition number. This improves the prior best classical result widetilde{O}(kappa d) due to Ascolani, Lavenant, and Zanella (Ann. Probab. 2026) and the quantum result widetilde{O}(sqrt{kappa} d^2) implied by Childs et al. (NeurIPS 2022). Our quantum sampler applies to a broad class of locally structured models from statistical computing and machine learning, with representative examples including Gaussian Markov random fields, finite-element latent Gaussian models, and sparse generalized linear models. These results demonstrate that local structure is not merely an implementation detail, but a quantum algorithmic resource for high-dimensional sampling.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.20253) | 2026-09-18
