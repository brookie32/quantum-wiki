---
title: "Efficient Complex-Valued State Preparation on Bucket Brigade QRAM"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "applications"
tags: [applications, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25644"
summary: "arXiv:2604.25644v1 Announce Type: new Abstract: Efficient quantum state preparation is a critical component in quantum algorithms that process large classical data, and it is fundamental to realizing "
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25644v1 Announce Type: new Abstract: Efficient quantum state preparation is a critical component in quantum algorithms that process large classical data, and it is fundamental to realizing quantum advantage in domains such as machine learning, quantum linear algebra, and quantum finance. Building on the framework of~ite{berti2025efficient}, which integrates Bucket Brigade QRAM (BBQRAM) with a segment tree to achieve amplitude encoding in polylogarithmic query time, we present two improvements within the same architecture-aware framework. First, we remove the U_{2CR} subroutine by classically precomputing the rotation angles determined by the segment tree and storing these angles directly in the BBQRAM cells. The tradeoff is that the classically loaded QRAM stores precomputed fixed-point angles rather than raw subtree weights. Second, we extend the construction to complex-valued matrices A in C^{M imes N} by storing a leaf phase alongside each precomputed rotation angle and using a two-step magnitude-then-phase procedure; the real signed case is naturally subsumed as a one-bit phase specialization. At unchanged O(log_2^2(MN)) BBQRAM query complexity, the QPU procedure reduces to BBQRAM retrievals and controlled-rotation cascades, with O(MN) memory cells per matrix and no reversible arithmetic on the QPU.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25644) | 2026-04-29
