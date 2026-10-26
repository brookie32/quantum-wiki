---
title: "Contrastive Regularization of Machine Learning Potentials"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2606.31660"
summary: "arXiv:2606.31660v2 Announce Type: replace Abstract: Machine learning models are increasingly trained as regressors and then deployed as generators, from language models to learned simulators. In this "
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2606.31660v2 Announce Type: replace Abstract: Machine learning models are increasingly trained as regressors and then deployed as generators, from language models to learned simulators. In this setting, accuracy on held-out data says little about the distribution a model produces when it is sampled. We study this problem where the correct distribution is fixed by first principles, in machine learning interatomic potentials (MLIPs) trained by minimizing the mean squared error (MSE) on density functional theory (DFT) energies and forces, then used to run molecular simulations. The MSE never constrains the Boltzmann distribution that the potential defines, so an MLIP can match held-out DFT data and still drift, when sampled, into spurious minima that corrupt its thermodynamics. Building on the variational principle of statistical physics, we introduce Contrastive Regularized MSE (CRMSE), a post-training step in which the potential acts as its own energy-based model and learns to reproduce the distribution it generates, without any new DFT data. On molecules from the MD17 benchmark, CRMSE restores physical sampling and recovers DFT free-energy profiles, while keeping energy and force errors within chemical accuracy. Our results suggest that a model meant to be sampled must be trained on the distribution it produces, not only for pointwise accuracy.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2606.31660) | 2026-10-26
