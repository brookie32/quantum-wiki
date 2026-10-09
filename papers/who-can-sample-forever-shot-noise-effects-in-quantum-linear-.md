---
title: "Who can sample forever? Shot noise effects in quantum linear regression"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.12015"
summary: "arXiv:2610.12015v1 Announce Type: new Abstract: Quantum fidelity kernels and quantum extreme learning machines share the same basic architecture: a fixed quantum device generates features that are com"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.12015v1 Announce Type: new Abstract: Quantum fidelity kernels and quantum extreme learning machines share the same basic architecture: a fixed quantum device generates features that are combined through a classically trained linear model. We refer to this broad non-variational setting as quantum linear regression. A defining aspect of these models is that the quantum features are not directly available, but must be estimated from a finite number of shots. We show that finite statistics makes quantum linear regression unavoidably ill-conditioned. Ideal feature vectors are confined to a subspace determined by the dimension of the Hilbert space, whereas finite-shot estimates generically acquire components outside this subspace. Training then attempts to fit directions that disappear in the infinite-statistics limit, making the learned model increasingly sensitive to sampling noise. We analyze this mechanism for quantum extreme learning machines trained on n_{rm tr} states with N shots per state. Despite the ill-conditioning, predictions remain controlled when the training targets are exact. Finite sampling produces a systematic prediction error that decreases quadratically with N, while fluctuations induced by the random training measurements decrease inversely with the total training budget. Thus, unlike in standard linear regression with exactly known features, increasing the dataset size alone cannot remove the error caused by sampling noise. If the training targets are also noisy, due for instance to state-preparation errors, the otherwise hidden directions become active. The test error can then increase with N, a behavior that we ascribe to a form of quantum overfitting. Our results expose a fundamental tradeoff between dataset size and per-state statistics in non-variational quantum learning and provide a baseline for resource-aware training and regularization strategies.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.12015) | 2026-10-09
