---
title: "A Width-Matched Comparison of Hybrid Quantum-Classical Self-Supervised Learning for Fingerprint Recognition"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.39172"
summary: "arXiv:2609.39172v1 Announce Type: new Abstract: Fingerprint recognition is a widely deployed biometric, but supervised training requires large labeled enrollment sets. Self-supervised learning (SSL) r"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.39172v1 Announce Type: new Abstract: Fingerprint recognition is a widely deployed biometric, but supervised training requires large labeled enrollment sets. Self-supervised learning (SSL) removes this requirement, and hybrid quantum-classical models have been proposed to enrich the learned representations. Prior quantum SSL studies consider a single contrastive objective, so it is unclear whether reported benefits depend on the objective or can be attributed to the quantum circuit. We insert the QuFeX quantum feature-extraction module into three SSL frameworks, the contrastive SimCLR and MoCo v2 and the non-contrastive BYOL, and compare each hybrid with its classical counterpart at matched representation width (8 features, equal to 8 qubits) on the SOCOFing fingerprint dataset, with a CIFAR-10 control, using k-nearest-neighbor identification on encoder features. In single-run experiments the hybrid scores clearly higher for both contrastive objectives, whereas for BYOL a multi-seed analysis shows no reliable difference, suggesting that any benefit depends on the SSL objective. A hardware-efficient circuit (QNet) does not show the same gain. We examine whether the gains can be attributed to the quantum circuit, considering circuit architecture, trainable parameter count, nonlinearity, and the classical simulability of 8-qubit circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.39172) | 2026-10-01
