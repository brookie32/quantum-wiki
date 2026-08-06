---
title: "Graph-Aware Exact Branch-and-Bound with Device Profiles for Static Qubit Allocation"
date: "2026-08-06"
updated: "2026-08-06"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.04058"
summary: "arXiv:2608.04058v1 Announce Type: new Abstract: Static qubit allocation maps a circuit's logical qubits to a sparse physical device while minimising an interaction-weighted physical-distance cost func"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

arXiv:2608.04058v1 Announce Type: new Abstract: Static qubit allocation maps a circuit's logical qubits to a sparse physical device while minimising an interaction-weighted physical-distance cost function, yielding a rectangular quadratic assignment problem. Existing work combines strong lower bounds with distributed branch-and-bound. We integrate graph-aware exact reductions with an engineering bundle for a lightweight assignment-bound path: unavoidable assigned-cost filtering, incrementally maintained root-orbit and prefix-stabilizer symmetry pruning, conditioned parent-LAP screening, and circuit-independent physical device profiles. On 21 relatively easy Melbourne instances and six Boeblingen instances completed by the GLB baseline, the final single-thread configuration provides geometric-mean speedups of 2.98x and 13.27x, respectively. With 60 threads on one shared-memory server, all instances in the final Boeblingen--Cairo experiment are certified optimal within half an hour, excluding one-time device-artifact construction. These results show that graph-aware node processing and engineering the search process substantially reduce the resources required for exact allocation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.04058) | 2026-08-06
