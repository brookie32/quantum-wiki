---
title: "Quantum Hamiltonian Evolution for Coherent Quantum Learning"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.03640"
summary: "arXiv:2609.03640v1 Announce Type: new Abstract: We introduce Coherent Quantum Learning (CQL), a training framework for quantum learning models in which the model parameters are quantum degrees of free"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2609.03640v1 Announce Type: new Abstract: We introduce Coherent Quantum Learning (CQL), a training framework for quantum learning models in which the model parameters are quantum degrees of freedom evolved under a Hamiltonian that encodes the loss function. Current quantum machine learning retains classical optimization: parameters are updated by a classical outer loop using gradient estimates from measurements, and quantum coherence has no role in the training dynamics, just as in any classical treatment of the same problem. In the quantum case, a parameter register initialized in superposition evolves unitarily, and probability amplitude concentrates near low-loss configurations through interference, without gradient computation or classical feedback. We give an explicit construction using block encodings and Hamiltonian simulation, applicable to arbitrary parameterized circuits. Numerical experiments on binary classification and interferometric phase estimation confirm that the evolved distribution peaks at the optimal parameters, matching gradient-based performance. The construction is compatible in principle with fault-tolerant implementations and extends to batched training via sequential Hamiltonian evolution.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.03640) | 2026-09-04
