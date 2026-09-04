---
title: "A Quantum Encoding of Traveling Salesperson Tours via Route Generation, Cost Phases, and a Reversible Valid-Permutation Oracle"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.21283"
summary: "arXiv:2603.21283v4 Announce Type: replace Abstract: For a traveling salesperson problem (TSP) of n cities, we present a compact quantum encoding based on a time-register representation of tours. A can"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2603.21283v4 Announce Type: replace Abstract: For a traveling salesperson problem (TSP) of n cities, we present a compact quantum encoding based on a time-register representation of tours. A candidate route is represented as a sequence of n-1 city labels over discrete time steps, with one fixed start city and the remaining cities encoded in binary registers. We describe three ingredients of the construction: uniform route generation over the route register, a reversible validity oracle, and a phase oracle that encodes the total tour cost. The validity oracle checks both that the non-start city labels form a permutation and, for incomplete graphs, that every directed edge used by the route exists. The cost oracle then accumulates the start-edge, intermediate-transition, and return-edge costs into a tour-dependent phase for valid routes. This yields a coherent superposition of candidate routes with feasibility and tour-length information embedded directly in the quantum state. The complete construction uses O(nlog n) qubits, while a naive implementation requires O(n^3log_2 n) CX gates and O!left(n^3[log_2 n+log_2(1/epsilon)]right) T gates, where epsilon denotes the target approximation precision. The encoding is compatible with amplitude amplification or spectral filtering techniques such as the quantum singular value transform (QSVT) or Grover's algorithm. However, due to the exponentially small fraction of valid tours, the overall complexity remains exponential even when combined with amplitude amplification.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.21283) | 2026-09-04
