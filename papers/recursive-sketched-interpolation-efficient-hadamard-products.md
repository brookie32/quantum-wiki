---
title: "Recursive Sketched Interpolation: Efficient Hadamard Products of Tensor Trains"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.17974"
summary: "arXiv:2602.17974v2 Announce Type: replace Abstract: The Hadamard product of two tensors in the tensor-train (TT) format is a fundamental operation across various applications, such as TT-based functio"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2602.17974v2 Announce Type: replace Abstract: The Hadamard product of two tensors in the tensor-train (TT) format is a fundamental operation across various applications, such as TT-based function multiplication for nonlinear differential equations or convolutions. However, conventional methods for computing this product typically scale as at least O(hi^4) with respect to the TT bond dimension (TT-rank) hi, creating a severe computational bottleneck in practice. By combining randomized tensor-train sketching with slice selection via interpolative decomposition, we introduce Recursive Sketched Interpolation (RSI), a ``scale product'' algorithm that computes the Hadamard product of TTs at a computational cost of O(hi^3). Benchmarks across various TT scenarios demonstrate that RSI offers superior scalability compared to traditional methods while maintaining comparable accuracy. We generalize RSI to compute more complex operations, including Hadamard products of multiple TTs and other element-wise nonlinear mappings, without increasing the complexity beyond O(hi^3).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.17974) | 2026-10-07
