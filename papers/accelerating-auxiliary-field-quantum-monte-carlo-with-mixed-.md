---
title: "Accelerating auxiliary-field quantum Monte Carlo with mixed-precision random propagators"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.21992"
summary: "arXiv:2611.21992v1 Announce Type: cross Abstract: We develop an algorithm to propagate auxiliary-field quantum Monte Carlo (AFQMC) wavefunctions in mixed precision. We target NVIDIA Tensor Cores using"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2611.21992v1 Announce Type: cross Abstract: We develop an algorithm to propagate auxiliary-field quantum Monte Carlo (AFQMC) wavefunctions in mixed precision. We target NVIDIA Tensor Cores using the TensorFloat-32 (TF32) format. We approximate each full-precision array by a TF32 leading term and a TF32 residual, and each full-precision matrix product by three TF32 products accumulated in full precision. Benchmarks on hydrogen chains show that mixed-precision propagation is consistently faster than double-precision GPU propagation, with an increasing advantage as the system size grows. The resulting local-energy deviations remain small over the propagation windows considered here. These results identify the stochastic two-body propagator as a particularly effective target for reduced precision, while our method allows higher precision to be retained for accuracy-sensitive operations. Hence, our algorithm provides a practical way to speed up AFQMC calculations and demonstrates where reduced precision can be applied without adverse effects on the method's accuracy.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.21992) | 2026-11-18
