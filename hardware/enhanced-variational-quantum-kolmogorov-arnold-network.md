---
title: "Enhanced Variational Quantum Kolmogorov-Arnold Network"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2503.22604"
summary: "arXiv:2503.22604v4 Announce Type: replace Abstract: The Kolmogorov-Arnold Network (KAN) places the trainable functions on the synapses rather than on the neurons. Existing quantum implementations eith"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2503.22604v4 Announce Type: replace Abstract: The Kolmogorov-Arnold Network (KAN) places the trainable functions on the synapses rather than on the neurons. Existing quantum implementations either lack accuracy (Variational Quantum KAN, VQKAN) or rely on block encoding and Quantum Signal Processing, which demand many control gates and ancillae. We propose the Enhanced Variational Quantum Kolmogorov-Arnold Network (EVQKAN), a variational ansatz that emulates a 2^{N_q}-dimensional KAN layer matrix by tiling controlled rotations through a sum-operator construction, using only 2^{N_q-1} trainable spline functions per layer. On the fitting of an elementary function, EVQKAN attains a significantly lower test error than Quantum Neural Networks (QNN), VQKAN and Adaptive VQKAN (Mann-Whitney p<0.002, Cliff's eltaleq-0.86 over ten attempts; EVQKAN beats VQKAN on every attempt), though classical KAN is more accurate still. On a two-dimensional classification task the ordering reverses: under a leak-free protocol introduced here, EVQKAN classifies above chance (accuracy 0.620, p=0.0005) but is significantly less accurate than a QNN carrying one fifth as many parameters (Deltaaccuracy -0.134, p=0.0014; DeltaAUC -0.252, p=0.0002). We withdraw the classification results of an earlier version of this work: their encoding placed the target label into the circuit as a feature for EVQKAN but not for the methods it was compared against. The dominant error source is overfitting from an under-determined training set; enlarging that set closes the train-test gap by 58% (Spearman p<10^{-3}). We also report the circuit cost in full --- three layers emit 1017 operations, or 4110 two-qubit gates once the multi-controlled gates are decomposed --- so the construction is simulator-scale and fault-tolerant-era rather than NISQ-ready, with block encoding and qubitization the route to reducing it.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2503.22604) | 2026-07-30
