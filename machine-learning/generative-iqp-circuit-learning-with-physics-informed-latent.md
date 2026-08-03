---
title: "Generative IQP Circuit Learning with Physics-Informed Latent Initialization"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.28866"
summary: "arXiv:2607.28866v1 Announce Type: new Abstract: Quantum generative learning based on instantaneous quantum polynomial-time (IQP) circuits can benefit from efficient classical training strategies. A re"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

arXiv:2607.28866v1 Announce Type: new Abstract: Quantum generative learning based on instantaneous quantum polynomial-time (IQP) circuits can benefit from efficient classical training strategies. A recent latent adaptation framework for IQP-based generative modeling transfers shared circuit parameters across instances of the same task with different hyperparameters while adapting only a low-dimensional latent variable for each new instance. However, existing approaches initialize this latent variable randomly, which can limit optimization efficiency and performance. In this work, we introduce a physics-informed latent initialization scheme for IQP generative learning to improve upon existing random initialization schemes. Motivated by the platonic representation hypothesis, we use latent representations extracted from a classical physics-informed neural network (PINN) surrogate to initialize the latent variables of the quantum model for the solution of the Burgers' equation. The initialized IQP model is then adapted on a higher-resolution solution domain. We find that this structured initialization consistently outperforms random latent initialization, yielding improved adaptation behavior and stronger generative accuracy across multiple viscosity settings. These results show that classical surrogate representations can provide useful inductive bias for quantum generative models and offer a practical route to improved initialization in IQP-based learning.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.28866) | 2026-08-03
