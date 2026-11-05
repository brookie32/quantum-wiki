---
title: "Noise-regularized training of quantum circuit Born machines under a finite shot budget"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.06630"
summary: "arXiv:2611.06630v1 Announce Type: new Abstract: Quantum circuit Born machines (QCBMs) can learn distributions that are hard to sample from classically, but their value depends on generalizing from fin"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.06630v1 Announce Type: new Abstract: Quantum circuit Born machines (QCBMs) can learn distributions that are hard to sample from classically, but their value depends on generalizing from finite training data. Here, we study how hardware noise affects this generalization. We show that, for any noise process, the generalization gap of a QCBM trained with the maximum mean discrepancy is bounded by the complexity of the distributions the noisy model can reach. Scrambled local Pauli noise contracts this complexity but biases the model towards the uniform distribution, so residual noise acts as a regularizer whose optimal strength can be intermediate. We propose GENIE, a framework that realizes a chosen noise level with capped error mitigation and selects it during training from held-out data within a fixed execution budget, with provably bounded regret. In simulations on synthetic and census data, GENIE stays close to the best of four noise-control strategies, whereas every fixed noise level falls short in many settings.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.06630) | 2026-11-05
