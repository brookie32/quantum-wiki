---
title: "Evaluating Quantum Kernel Methods for Track-Based Classification in High-Energy Physics"
date: "2026-08-28"
updated: "2026-08-28"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.27333"
summary: "arXiv:2608.27333v1 Announce Type: new Abstract: We present a systematic design for large-scale quantum kernel classification, demonstrated through a quantum support vector classifier (QSVC) for partic"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

arXiv:2608.27333v1 Announce Type: new Abstract: We present a systematic design for large-scale quantum kernel classification, demonstrated through a quantum support vector classifier (QSVC) for particle-track classification using centroid-based CLAS12 drift-chamber features. Each event is encoded into a six-qubit state via a fully entangled ZZFeatureMap, whose fidelities define a quantum kernel within a standard SVM framework. By decoupling state preparation from kernel construction and distributing evaluation across a multi-node MPI-based HPC allocation, the approach scales to 1.0x10^5 training and 4.0x10^5 test events with an exactly constructed kernel matrix, to our knowledge more than an order of magnitude larger than prior high-energy-physics quantum-kernel studies. Benchmarked against linear, polynomial, RBF, and sigmoid SVM kernels and extremely randomized trees (ERT), the ideal QSVC achieves the highest recall (99.99%) among all models. Under a calibrated hardware noise model (FakeMumbaiV2, 500 training / 2,000 test events), AUC falls from 0.9985 to 0.9671 and peak significance improvement falls from 17.5 to ~3.5, yet recall remains at 99.51% -- indicating this signal-retention advantage is attenuated but not eliminated by circuit-level decoherence. Geometric analysis of the quantum embedding shows near-orthogonal inter-class states with coherent intra-class neighborhoods under ideal simulation; under noise this structure compresses toward the maximally mixed state while preserving its relative ordering. These results demonstrate a scalable, reproducible workflow for quantum kernel experimentation at HEP-relevant scale, quantifying the practical cost of realistic hardware noise on quantum-enhanced classification.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.27333) | 2026-08-28
