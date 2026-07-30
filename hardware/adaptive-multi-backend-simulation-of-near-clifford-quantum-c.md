---
title: "Adaptive Multi-Backend Simulation of Near-Clifford Quantum Circuits via Spatial Stabilizer-Frame Partitioning"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.27075"
summary: "arXiv:2607.27075v1 Announce Type: new Abstract: We present an exact amplitude simulator for Clifford+T quantum circuits that combines a Feynman path sum across a balanced qubit bipartition with stabil"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2607.27075v1 Announce Type: new Abstract: We present an exact amplitude simulator for Clifford+T quantum circuits that combines a Feynman path sum across a balanced qubit bipartition with stabilizer-frame simulation on each half. The construction extends prior stabilizer-based Schrodinger-Feynman methods in three directions: recursive multilevel bipartition into a binary tree, automatic fallback to dense state-vector simulation when a leaf's stabilizer frame would exceed its memory ceiling, and a cost-model-driven partition selector that replaces the standard cut-count minimization heuristic. We show cut-count minimization is an unreliable proxy in practice: a globally cleaner partition can reduce cross-cut count yet increase wall-clock time, because it imbalances T-gate density across halves and inflates per-half stabilizer-frame size. Our cost model substitutes the stabilizer-frame bound 2w for the dense 2n ceiling per side and explicitly models per-amplitude readout cost; isolating that term uncovered a quadratic-asymptotic inefficiency in the leaf simulator's end-of-path amplitude extraction, fixed by replacing it with an existing O(F * s * n) single-amplitude inner product. On a structured hierarchical n=16 benchmark the recursive simulator beats monolithic stabilizer-frame simulation by 92x to 17,645x, wins by 79x per path against a dense half-state-vector baseline under an identical cut, and beats a production state-vector simulator end to end by up to 47.9x (median ~5x). On adversarial random Clifford+T circuits the dense state vector wins past a crossover near n/2 cross-cut gates -- the regime the cost model identifies. The dominant cost, the cross-cut Feynman sum, is embarrassingly parallel with constant inter-worker communication, unlike recent matrix-product-state stabilizer-tensor methods whose inner contraction loop is sequential.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.27075) | 2026-07-30
