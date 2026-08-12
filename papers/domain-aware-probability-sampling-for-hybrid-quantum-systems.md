---
title: "Domain-Aware Probability Sampling for Hybrid Quantum Systems using Bayesian Optimization"
date: "2026-08-12"
updated: "2026-08-12"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2510.00145"
summary: "arXiv:2510.00145v5 Announce Type: replace Abstract: We study the problem of probability distribution matching and sampling on near-term quantum computers, aiming to construct parameterized circuits th"
last_verified: "2026-08-12"
review_by: "2026-11-10"
stale: false
---

arXiv:2510.00145v5 Announce Type: replace Abstract: We study the problem of probability distribution matching and sampling on near-term quantum computers, aiming to construct parameterized circuits that generate samples from a target distribution while minimizing resource overhead. This task arises naturally in hybrid quantum-classical workflows, where measurement-driven objectives replace full state reconstruction, and is central to applications in generative modeling and variational inference. However, it remains challenging due to hardware noise, limited circuit depth, and a high-dimensional, non-convex parameter space. We propose CircuitTree, a surrogate-guided optimization framework based on Bayesian Optimization with tree-based models for scalable, domain-aware distribution matching. Our approach introduces a structured, layerwise decomposition aligned with the variational circuit architecture, enabling distributed and sample-efficient optimization within hybrid loops with theoretical convergence guarantees. Across representative distribution-matching tasks, CircuitTree achieves up to 2-3x lower total variation distance while using 40-60% fewer gates than prior approaches. These results demonstrate its effectiveness as a practical building block for end-to-end hybrid quantum sampling.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2510.00145) | 2026-08-12
