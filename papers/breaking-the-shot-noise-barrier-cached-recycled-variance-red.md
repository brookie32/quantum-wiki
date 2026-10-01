---
title: "Breaking the Shot-Noise Barrier: Cached Recycled Variance-Reduced Gradients for Quantum Optimization"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.38800"
summary: "arXiv:2609.38800v1 Announce Type: new Abstract: Variational Quantum Algorithms (VQAs) rely heavily on classical optimization routines to navigate high-dimensional, noisy parameter landscapes. However,"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.38800v1 Announce Type: new Abstract: Variational Quantum Algorithms (VQAs) rely heavily on classical optimization routines to navigate high-dimensional, noisy parameter landscapes. However, the evaluation of analytical gradients via the parameter-shift rule requires O(p) circuit executions, rendering this approach computationally prohibitive for deep circuits. While simultaneous perturbation methods provide an O(1) alternative, their gradient estimates suffer from severe O(p) spatial variance, which impedes convergence. To resolve this tension, we introduce the Cached Recycled Variance-Reduced Gradient (CRVG) by leveraging variance reduction techniques. We formulate two variants: a 3-Circuit (1-Sided) Non-Recursive CRVG and a Recursive CRVG. By introducing a center-point caching mechanism, the 3-Circuit CRVG mathematically recycles quantum measurements to reduce the inner-loop circuit complexity by 25% across both variants. We establish a theoretical separation between the two routing paths to achieve an epsilon^2-stationary point: the non-recursive variant reaches a sample complexity of O(max{p/epsilon^2, p^{2/3}/epsilon^{10/3}}), while the recursive variant achieves an improved complexity of O(max{p/epsilon^2, sqrt{p}/epsilon^3}). Empirically, extensive evaluations on MaxCut and Maximum Independent Set (MIS) benchmarks validate these findings. While standard simultaneous perturbation remains a robust baseline across varying depths, CRVG demonstrates targeted advantages in specific amortizable regimes, such as the non-recursive variant on EfficientSU2 circuits and both variants on depth-three QAOA, yielding superior energy minimums and tighter output variances. Ultimately, CRVG establishes a principled bias-throughput trade-off for scaling near-term quantum optimization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.38800) | 2026-10-01
