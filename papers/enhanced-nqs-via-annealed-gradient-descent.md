---
title: "Enhanced NQS via Annealed Gradient Descent"
date: "2026-07-22"
updated: "2026-07-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.18865"
summary: "arXiv:2607.18865v1 Announce Type: new Abstract: Neural quantum states offer expressive representations of quantum many-body wave functions, yet their practical accuracy can be limited by stochastic op"
last_verified: "2026-07-22"
review_by: "2026-10-20"
stale: false
---

arXiv:2607.18865v1 Announce Type: new Abstract: Neural quantum states offer expressive representations of quantum many-body wave functions, yet their practical accuracy can be limited by stochastic optimization rather than representational capacity. Here we identify a finite-sample instability, termed subspace trapping, in which physically important configurations become strongly underestimated, remain absent from successive sampling batches and receive insufficient gradient feedback. This self-reinforcing loss of sampled support can confine optimization to an effective subspace and produce apparently stationary states above the true ground state energy. To address this problem, we introduce annealed gradient descent (AGD), a sampling-aware update with annealing factor that temporarily increases the relative contribution of sampled low-probability configurations while limiting the dominance of high-probability ones. We establish the connection between finite-sample support loss and effective subspace optimization, and then evaluate the method across molecular systems, one and two-dimensional J_1-J_2 models. Annealed gradient descent suppresses metastable trapping, preserves physically relevant configurations and enables compact neural quantum states to attain chemical accuracy and competitive state-of-the-art performance. These results establish AGD as a lightweight complement to expressive neural architectures, improved sampling strategies for scalable quantum many-body optimization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.18865) | 2026-07-22
