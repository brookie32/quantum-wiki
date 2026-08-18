---
title: "A Machine-Learning Framework for Efficient Ring-Polymer Instanton Rate Calculations"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2602.16962"
summary: "arXiv:2602.16962v3 Announce Type: replace Abstract: We develop an efficient machine-learning framework for ring-polymer instanton rate calculations that combines Gaussian process regression (GPR)-enha"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2602.16962v3 Announce Type: replace Abstract: We develop an efficient machine-learning framework for ring-polymer instanton rate calculations that combines Gaussian process regression (GPR)-enhanced line integral string optimization with scalable surrogate modeling of the fluctuation prefactor. By exploiting uncertainty estimates from the surrogate modeling, we show that the number of force evaluations required to converge an instanton path becomes effectively independent of the number of beads used to discretize the pathway. To improve the efficiency of GPR model training, we introduce a strategy combining a physics-informed kernel prior, Hessian-free hyperparameter optimization, and GPU-accelerated Blackbox Matrix-Matrix Multiplication (BBMM), reducing model-training costs by more than an order of magnitude. For rate calculations, we develop adaptive regression, selective Hessian training, and cubic-spline interpolation strategies that substantially reduce the number of explicit Hessian evaluations while maintaining accurate tunneling rates. We apply and compare both cubic spline interpolation and GPR methods to approximate the instanton rate for representative proton transfer systems such as malonaldehyde, Z-3-aminopropenal, and 7,9-dinitro-10-hydroxybenzo[h]quinoline (dinitro-HBQ). Both approaches perform well for the smaller systems, whereas the dinitro-HBQ results expose limitations of the GPR model and demonstrate the greater robustness of the cubic spline interpolation method. These developments provide a practical workflow for reducing the computational cost of instanton rate calculations in complex molecular systems.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2602.16962) | 2026-08-18
