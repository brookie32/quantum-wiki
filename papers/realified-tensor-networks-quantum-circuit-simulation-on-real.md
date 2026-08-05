---
title: "Realified tensor networks: quantum circuit simulation on real-valued matrix accelerators"
date: "2026-08-05"
updated: "2026-08-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.03987"
summary: "arXiv:2608.03987v1 Announce Type: new Abstract: Tensor-network contraction simulates quantum circuits, but modern matrix accelerators (NPUs, TPUs) expose only real GEMM pipelines, so the complex netwo"
last_verified: "2026-08-05"
review_by: "2026-11-03"
stale: false
---

arXiv:2608.03987v1 Announce Type: new Abstract: Tensor-network contraction simulates quantum circuits, but modern matrix accelerators (NPUs, TPUs) expose only real GEMM pipelines, so the complex networks of quantum simulation must be reconstructed in software. We resolve the mismatch by a realification rewrite that maps any complex tensor network to a real one. At each merge of two complex tensors, a rank-3 structure tensor realizes Gauss's three-multiplication (3M) formula; contractions with one or no complex operand need only two or one real products. We prove a tight cost law: overhead 1 + 2m + r in real multiplications, where m and r are the volume fractions of two- and one-complex-operand contractions, never exceeding 3imes relative to real contraction, with every intermediate at most doubled in size. On 67 circuits (random, Clifford+T, QAOA, VQE), the law holds across the real-to-complex range and complex-gate placement, not count, governs cost. Contraction orders transfer from the complex network with a relative arithmetic-cost gap below 5imes 10^{-4} on 66 of 67 circuits; the exception closes under a few steps of low-temperature simulated annealing. On an Ascend 910 NPU the rewrite beat both the four-real-GEMM baseline and a per-GEMM Gauss lowering on all twelve random circuits and on 52 of 55 structured cells (three cells slower by at most 12%); the four-GEMM baseline was slower by a median 1.7imes (random) and 1.4imes (structured). Realification makes complex tensor-network contraction native to real-only matrix engines.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.03987) | 2026-08-05
