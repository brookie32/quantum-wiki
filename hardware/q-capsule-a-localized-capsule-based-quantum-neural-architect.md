---
title: "Q-Capsule: A Localized Capsule-Based Quantum Neural Architecture for Barren Plateau Mitigation"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.11261"
summary: "arXiv:2610.11261v1 Announce Type: new Abstract: Variational quantum algorithms are often limited by barren plateaus: gradients vanish as circuit size and depth increase, making quantum neural networks"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.11261v1 Announce Type: new Abstract: Variational quantum algorithms are often limited by barren plateaus: gradients vanish as circuit size and depth increase, making quantum neural networks difficult to train. We propose Q-Capsule, a localized capsule-based quantum neural architecture that mitigates this problem through register partitioning, local readout, sparse inter-capsule coupling, trainable data re-uploading, and Quantum Fisher Information Matrix (QFIM)-guided adaptive depth growth. By restricting the dominant support of each observable to a small capsule and controlling inter-capsule entanglement, Q-Capsule preserves useful gradient signals while retaining communication between local quantum representations. As the register width increases, Q-Capsule consistently maintains stable gradient variance, whereas globally entangling baselines exhibit exponential suppression with a log-gradient-variance slope near -ln 2 per qubit. Q-Capsule also produces more structured optimization landscapes, higher parameter efficiency, improved robustness to depolarizing noise, and lower measurement requirements. Its adaptive policy achieves 98.1% accuracy on binary classification and 97.7% on four-class classification, while using approximately 73% fewer two-qubit gates than the fixed-deep model on the multiclass task.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.11261) | 2026-10-09
