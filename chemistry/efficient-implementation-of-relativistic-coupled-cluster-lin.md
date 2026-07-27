---
title: "Efficient Implementation of Relativistic Coupled Cluster Linear Response Theory in Combination with Perturbation Sensitive Natural Spinors and Cholesky Decomposition Treatment of Two-electron Integrals"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2604.12914"
summary: "arXiv:2604.12914v2 Announce Type: replace Abstract: We present an efficient implementation of the low-cost linear-response coupled-cluster singles and doubles (LR-CCSD) method for computing static and"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2604.12914v2 Announce Type: replace Abstract: We present an efficient implementation of the low-cost linear-response coupled-cluster singles and doubles (LR-CCSD) method for computing static and frequency-dependent polarizabilities in systems with significant relativistic and electron-correlation effects. The implementation combines X2C-based Hamiltonians (X2CAMF and X2CMP), perturbation-sensitive natural spinors (FNS++), and Cholesky decomposition (CD)- based treatment of two-electron integrals to reduce both the computational and memory demands of relativistic LR-CCSD calculations. Benchmark calculations reveal that X2CMP exhibits more robust behavior than X2CAMF in the presence of highly augmented basis sets. The proposed FNS++CD-X2CMP-LR-CCSD approach reproduces four-component reference values with excellent accuracy across a diverse set of atomic and molecular systems. Additionally, different strategies for constructing the FNS++ basis were assessed, and the averaged-density approach was found to offer a favorable balance between accuracy and computational cost. Across the benchmark systems considered in this work, approximately 70% of the virtual spinor space can be removed with the FNS++ approach. The present implementation enables accurate and scalable relativistic response calculations for large molecular systems, as demonstrated by the computation of the static and dynamic polarizabilities of uranium hexafluoride using a triple-zeta basis comprising more than 1,400 basis functions.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2604.12914) | 2026-07-27
