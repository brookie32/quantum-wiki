---
title: "QTN-RQNN: Quantum Tensor Network-Based Recurrent Quantum Neural Network"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.13694"
summary: "arXiv:2610.13694v1 Announce Type: new Abstract: Resource constraints and imperfect quantum operations remain major challenges for quantum machine learning (QML) on noisy intermediate-scale quantum (NI"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2610.13694v1 Announce Type: new Abstract: Resource constraints and imperfect quantum operations remain major challenges for quantum machine learning (QML) on noisy intermediate-scale quantum (NISQ) devices, particularly for fault-diagnosis tasks involving imbalanced and heterogeneous data. This work proposes QTN-RQNN, a Quantum Tensor Network-Based Recurrent Quantum Neural Network that integrates tensor-network-inspired nearest-neighbor interactions with recurrent quantum processing. The model sequentially encodes input features while propagating quantum memory across recurrent steps and incorporates QSMOTE for class balancing. QTN-RQNN is evaluated on four heterogeneous fault-diagnosis datasets SPID, CWRUBD, EFDD, and SFDD and compared with QNN, QTN-QNN, and RQNN baselines through classification, ablation, multi-seed, convergence, and quantum-resource analyses. Results show dataset-dependent predictive behavior, indicating that increased quantum architectural complexity does not universally improve classification. On SPID, QTN-RQNN improves the RQNN F1-score from 0.3077 to 0.4516 and ROC-AUC from 0.4485 to 0.6970, while the remaining datasets exhibit different performance-resource trade-offs and sensitivity to recurrent timesteps and circuit depth. Across all datasets, QTN-RQNN reduces the two-qubit-gate count from 32 to 24 per sample relative to RQNN, corresponding to a 25% reduction without increasing the four-qubit requirement; the same relative reduction is obtained for QTN-QNN over QNN. These findings establish QTN-RQNN as a resource-conscious recurrent quantum architecture and highlight the need to jointly consider predictive performance and circuit-resource requirements for near-term quantum fault diagnosis.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.13694) | 2026-10-12
