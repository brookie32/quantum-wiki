---
title: "Training Energy-Based Models with Non-MCMC Samplers and Efficient Temperature Estimation"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.02323"
summary: "arXiv:2512.02323v2 Announce Type: replace-cross Abstract: Efficient sampling from Boltzmann distributions over discrete variables is a fundamental operation in a wide range of applications. While fast"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2512.02323v2 Announce Type: replace-cross Abstract: Efficient sampling from Boltzmann distributions over discrete variables is a fundamental operation in a wide range of applications. While fast non-MCMC samplers have recently emerged as promising alternatives to conventional MCMC methods, their practical use for probabilistic learning remains hindered by the difficulty of estimating the effective temperature of the generated samples. In this work, we begin by introducing Langevin simulated bifurcation (LSB), a Boltzmann sampler that enables fast and parallel sampling with accuracy comparable to sequential MCMC methods. To address the challenge of unknown effective temperature, we propose conditional expectation matching (CEM), an efficient estimation method applicable to energy-based models (EBMs) with exploitable conditional independence structures. Building on these components, we further develop a learning framework, termed sampler adaptive learning (SAL), which adaptively adjusts the model temperature to match that of the distribution induced by fast non-MCMC sampling. We demonstrate the effectiveness of LSB, CEM, and SAL on semi-restricted Boltzmann machines (SRBMs), a class of EBMs that are difficult to train using conventional approaches. LSB achieves orders-of-magnitude acceleration over Gibbs sampling while maintaining comparable or higher accuracy, and CEM enables accurate temperature estimation of the resulting distribution with negligible computational overhead. As a consequence, SAL enables efficient training of SRBMs and outperforms conventional Boltzmann machine learning methods on synthetic spin-glass datasets. In addition, the trained models achieve strong performance across multiple tasks. These results establish LSB as a fast and accurate Boltzmann sampler and provide key insights that enable practical applications of fast non-MCMC sampling methods via efficient temperature estimation with CEM.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.02323) | 2026-09-16
