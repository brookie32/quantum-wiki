---
title: "Landscape-Similarity-Guided Optimization in Divide-and-Conquer QAOA"
date: "2026-09-17"
updated: "2026-09-17"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.21689"
summary: "arXiv:2602.21689v4 Announce Type: replace Abstract: Divide-and-conquer strategies mitigate hardware constraints for the Quantum Approximate Optimization Algorithm (QAOA) on Noisy Intermediate-Scale Qu"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

arXiv:2602.21689v4 Announce Type: replace Abstract: Divide-and-conquer strategies mitigate hardware constraints for the Quantum Approximate Optimization Algorithm (QAOA) on Noisy Intermediate-Scale Quantum (NISQ) devices by partitioning large interaction graphs into smaller, hardware-compatible sub-problems. However, this approach introduces a severe classical training bottleneck: a decomposition across m boundary nodes generates 2^m distinct sub-problems that typically require independent optimization. In this work, we demonstrate that across diverse synthetic and real-world interaction graphs, the variational landscapes of these reduced QAOA instances actually exhibit a robust universality. Adapting the replica-overlap framework of spin-glass physics, we define a landscape-overlap order parameter q to quantify geometric correlations between energy landscapes, revealing a sharp landscape-similarity transition as graph connectivity is tuned. Exploiting this, we introduce Doubly Optimized QAOA (DO-QAOA), an adaptive pipeline that collapses the sub-problems from 2^m distinct sub-problems into K=O(1) effective landscape classes. By performing optimization on a single representative sub-problem and dynamically transferring parameters to remaining sub-problems, DO-QAOA lowers runtime and quantum measurement overhead by orders of magnitude while maintaining a competitive Approximation Ratio Gap (ARG).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.21689) | 2026-09-17
