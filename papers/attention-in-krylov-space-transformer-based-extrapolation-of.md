---
title: "Attention in Krylov Space: Transformer-Based Extrapolation of Lanczos Coefficients"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.07937"
summary: "arXiv:2601.07937v2 Announce Type: replace Abstract: The Universal Operator Growth Hypothesis formulates time evolution of operators through Lanczos coefficients. In practice, however, numerical instab"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

arXiv:2601.07937v2 Announce Type: replace Abstract: The Universal Operator Growth Hypothesis formulates time evolution of operators through Lanczos coefficients. In practice, however, numerical instability and memory cost limit the number of coefficients that can be exactly computed. In response to these challenges, the standard approach relies on fitting early coefficients to asymptotic forms, but such procedures can miss subleading, history-dependent structures in the coefficients that subsequently affect reconstructed observables. In this work, we treat the Lanczos coefficients as a causal time sequence and introduce a transformer-based model to autoregressively predict future Lanczos coefficients from short prefixes. For classical and quantum chaotic systems, our model outperforms asymptotic fits in both coefficient extrapolation and physical observable reconstruction, and achieves an order-of-magnitude reduction in error. The model also accurately extrapolates coefficients in integrable regimes, where no universal asymptotic fit exists. Remarkably, our model transfers across system sizes: it can be trained on smaller systems and then be used to extrapolate coefficients on a larger system without retraining. By probing the learned attention patterns and performing targeted attention ablations, we identify portions of the coefficient history that are most influential for accurate forecasts. Our results demonstrate that modern sequence models can serve as practical surrogates for probing operator dynamics deep in Krylov space, where brute-force Lanczos iteration can be computationally prohibitive.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.07937) | 2026-08-03
