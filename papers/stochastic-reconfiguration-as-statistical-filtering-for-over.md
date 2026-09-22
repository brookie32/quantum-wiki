---
title: "Stochastic Reconfiguration as Statistical Filtering for Overparameterized Neural Quantum States"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.23334"
summary: "arXiv:2609.23334v1 Announce Type: new Abstract: Stochastic reconfiguration (SR) is the standard optimizer for neural quantum states (NQS), but modern NQS often have far more parameters than Monte Carl"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.23334v1 Announce Type: new Abstract: Stochastic reconfiguration (SR) is the standard optimizer for neural quantum states (NQS), but modern NQS often have far more parameters than Monte Carlo samples. We show that in this regime the diagonal shift is more than a numerical stabilizer. It acts as a statistical filter for finite-sample generalization. At a fixed wave function, SR is ridge regression from tangent features to the centered local energy. Its residual is the expressivity gap, the part of imaginary-time evolution outside the current tangent space. This gap is orthogonal to the tangent space in population, but finite batches make it act as noise that SR can overfit. The shift therefore balances shrinkage of useful update directions against variance from fitting sampled residuals. Exact diagnostics on a 4imes4 Heisenberg graph separate two effects of overparameterization. Larger tangent spaces help when they reduce the expressivity gap, but they can hurt when they overfit a fixed gap. In a 100-site transverse-field Ising family trained with a foundation NQS, validation risk is U-shaped in the shift while variance decreases, matching the noisy-ridge model. This view leads to multi-shift SR (MS-SR), which averages independent ridge solves at data-adaptive shifts to form a richer, lower-variance spectral filter. Checkpoint-local experiments show that MS-SR lowers validation risk and update variance relative to the fixed-shift SR baseline. We further compare MS-SR and SR in paired online training continuations, with independent endpoint energy evaluations and a separate update-cost benchmark.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.23334) | 2026-09-22
