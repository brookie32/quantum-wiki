---
title: "Variational preparation of thermofield double states for SYK models via multi-angle QAOA: sequential angle pruning for circuit reduction"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.02793"
summary: "arXiv:2609.02793v1 Announce Type: new Abstract: Variational preparation of thermofield double (TFD) states can require deep quantum circuits, particularly for interacting many-body systems. Reducing t"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.02793v1 Announce Type: new Abstract: Variational preparation of thermofield double (TFD) states can require deep quantum circuits, particularly for interacting many-body systems. Reducing these circuits while retaining high fidelity is therefore crucial for TFD-state preparation on noisy quantum processors. We study this problem by applying the multi-angle quantum approximate optimization algorithm (ma-QAOA) to TFD-state preparation and introducing two top-down sequential angle-pruning algorithms. Starting from the optimized initial ma-QAOA circuit, both algorithms sequentially remove Pauli-string evolutions with small optimized angles and reoptimize the remaining parameters after each removal. We apply these algorithms to Gaussian and binary Sachdev--Ye--Kitaev (SYK) models in both dense and sparse cases. We find that ma-QAOA prepares the target TFD states with high fidelity and that sequential small-angle pruning retains high fidelity while reducing the circuit depth, particularly at low temperature. Moreover, using the post-reoptimization cost in sequential small-angle pruning further improves the fidelity. For the binary sparse N=10 SYK model at eta=10, 88.8%--92.1% of the nonlocal Pauli-string evolutions are removed while retaining an average fidelity of approximately 95%. Finally, we propose extensions of the sequential pruning algorithms toward quantum--classical hybrid implementation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.02793) | 2026-09-03
