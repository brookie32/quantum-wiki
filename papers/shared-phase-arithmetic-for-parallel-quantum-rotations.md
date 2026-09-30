---
title: "Shared Phase Arithmetic for Parallel Quantum Rotations"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.36574"
summary: "arXiv:2609.36574v1 Announce Type: new Abstract: A layer of diagonal quantum gates can be specified by an integer-valued function on computational basis states. This description suggests implementing t"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.36574v1 Announce Type: new Abstract: A layer of diagonal quantum gates can be specified by an integer-valued function on computational basis states. This description suggests implementing the layer by evaluating that function reversibly and translating its value into a phase using a shared quantum register. We develop this viewpoint for parallel phase kickback (PPK): the weighted sum of several rotation parameters is computed coherently, added once to a phase-gradient state, and then uncomputed. The construction separates the cost of representing a phase function from the cost of applying it. We prove correctness, give explicit error bounds, and analyze logical gate counts for general weights, pairs of rotations, and weights with disjoint binary support. With Clifford-only encoding, a batch uses at most 4(b-1) T gates at b-bit phase resolution, excluding initialization. The first phase reference is prepared with independent rotations synthesized by Gridsynth; additional phase-gradient states then follow from the disjoint-support construction with O(b) T gates each. The resulting bounds identify when shared phase arithmetic reduces amortized rotation cost and when encoding overhead limits that advantage.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.36574) | 2026-09-30
