---
title: "Trainability-Oriented Hybrid Quantum Regression via Geometric Preconditioning and Curriculum Optimization"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.11942"
summary: "arXiv:2601.11942v4 Announce Type: replace-cross Abstract: Quantum neural networks (QNNs) have attracted growing interest for scientific machine learning, yet in regression settings they often suffer f"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

arXiv:2601.11942v4 Announce Type: replace-cross Abstract: Quantum neural networks (QNNs) have attracted growing interest for scientific machine learning, yet in regression settings they often suffer from limited trainability under noisy gradients and ill-conditioned optimization. We propose a hybrid quantum--classical regression framework designed to mitigate these bottlenecks. Our model prepends a lightweight classical embedding that acts as a learnable geometric preconditioner, reshaping the input representation to better condition a downstream variational quantum circuit. Building on this architecture, we introduce a curriculum optimization protocol that progressively increases circuit depth and transitions from SPSA-based stochastic exploration to Adam-based gradient fine-tuning. We evaluate the approach on PDE-informed regression benchmarks and standard regression datasets under a fixed training budget in a simulator setting. Empirically, the proposed framework consistently improves over pure QNN baselines and yields more stable convergence in data-limited regimes. We further observe reduced structured errors that are visually correlated with oscillatory components on several scientific benchmarks, suggesting that geometric preconditioning combined with curriculum training is a practical approach for stabilizing quantum regression.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.11942) | 2026-09-14
