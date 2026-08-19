---
title: "SPSA Hyperparameter Tuning for Variational Quantum Natural Language Inference"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.16939"
summary: "arXiv:2608.16939v1 Announce Type: new Abstract: Training variational quantum models requires choosing between parameter-shift gradients, which are exact but cost O(P) forward evaluations, and simultan"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.16939v1 Announce Type: new Abstract: Training variational quantum models requires choosing between parameter-shift gradients, which are exact but cost O(P) forward evaluations, and simultaneous perturbation stochastic approximation (SPSA), which uses only two samples but produces high-variance estimates that can degrade optimisation on small supervised tasks. Whether the cheap gradient is usable depends on the variance that results from different choices of the SPSA perturbation scale, learning rate, and gain-decay schedule. We varied those quantities across a broad grid on a 6-qubit, 60-parameter QNLI classifier and compared the best configurations to parameter-shift AdamW and BuresQNG. AdamW-style SPSA with c_0=0.01, eta=0.10, gamma=0.10 reached 55% pm 11% test accuracy, improving over the default configuration (49% pm 6%) but remaining 16-19 percentage points below the parameter-shift baselines because the two-sample SPSA gradient estimate has too much variance for reliable optimisation of 60 parameters in 40 epochs. Classical-gain SPSA and Bures-preconditioned SPSA performed worse, at 51% and 46% respectively. Bures-preconditioning a noisy two-sample SPSA gradient amplifies perturbation noise.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.16939) | 2026-08-19
