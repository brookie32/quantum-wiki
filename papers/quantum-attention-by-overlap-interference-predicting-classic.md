---
title: "Quantum Attention by Overlap Interference: Predicting Classical and Many-Body Quantum Sequences"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.06699"
summary: "arXiv:2602.06699v2 Announce Type: replace Abstract: We propose a variational quantum implementation of self-attention (QSA)-the core operation in transformers and large language models-which predicts "
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2602.06699v2 Announce Type: replace Abstract: We propose a variational quantum implementation of self-attention (QSA)-the core operation in transformers and large language models-which predicts future elements of a sequence by forming overlap-weighted combinations of past data. At variance with previous approaches, our QSA realizes the required nonlinearity through interference of state overlaps and a degree-k polynomial kernel, and estimates a loss based on Renyi-1/2 entropic functionals via two observables' expectation values, avoiding the decoding of amplitude-encoded predictions into classical probabilities. QSA also accommodates a constrained, trainable data-embedding tying state overlaps to data-level similarities. Its dominant end-to-end training complexity scales as Oleft(mu^{-1}k^2Tdright), versus Oleft(T d^{k+1}right) of the fairest classical comparison, with mu a training signal; we show numerically that this allows a complexity advantage in the regime where sequence length T dominates the embedding size d. In simulations, our QSA-based quantum transformer learns sequence prediction on classical data and on many-body transverse-field Ising trajectories-establishing trainable attention as a practical primitive for quantum dynamical modeling.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.06699) | 2026-09-25
