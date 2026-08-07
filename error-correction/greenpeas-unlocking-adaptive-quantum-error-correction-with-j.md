---
title: "GreenPeas: Unlocking adaptive quantum error correction with just-in-time decoding hypergraphs"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.16613"
summary: "arXiv:2604.16613v2 Announce Type: replace Abstract: Circuit-level decoders are essential for the realisation of low-overhead fault-tolerant quantum computing. However, they rely on complex hypergraphs"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2604.16613v2 Announce Type: replace Abstract: Circuit-level decoders are essential for the realisation of low-overhead fault-tolerant quantum computing. However, they rely on complex hypergraphs that are traditionally compiled ahead-of-time. This static approach introduces a significant bottleneck for an emerging class of adaptive circuits, where the structure is modified during execution based on mid-circuit measurement outcomes. Pre-compiling hypergraphs for all possible circuit branches would incur an exponential memory cost, rendering current tools impractical for these workloads. Hence, we introduce GreenPeas, a just-in-time compiler for decoding hypergraphs. By lowering the realised circuit to a space-time error propagation graph, GreenPeas decomposes Stim's backtracking algorithm for error analysis into two sequentially dependent, internally parallelisable stages: (1) mapping physical errors to their corresponding equivalence classes, and (2) aggregating error probabilities within each class. Evaluated on surface and bivariate bicycle code memory circuits without user-annotated repeat blocks, GreenPeas achieves a geometric mean speedup of 13.2x over Stim using a high-end GPU. This speedup carries over to the adaptive regime, unlocking circuit-level decoding of [[4,2,2]]-concatenated surface code memories with adaptive syndrome measurements -- a capability previously restricted to less accurate phenomenological decoders -- yielding 6.7x lower logical error rate and 4.5x lower decoding latency at a representative outer code distance of 10.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.16613) | 2026-08-07
