---
title: "Architecture-aware Unitary Synthesis"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.23777"
summary: "arXiv:2604.23777v1 Announce Type: new Abstract: We present a novel architecture-aware transpilation method for exact general unitary gate synthesis on superconducting quantum hardware. Our approach is"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.23777v1 Announce Type: new Abstract: We present a novel architecture-aware transpilation method for exact general unitary gate synthesis on superconducting quantum hardware. Our approach is tightly integrated with the optimized block-ZXZ decomposition, exploiting its recursive structure to make hardware-aware decisions at each level of the recursion rather than treating transpilation as an independent post-processing step. The method introduces three key techniques: a greedy qubit mapping strategy that minimizes pairwise distances between physical qubits, an adaptive Gray code selection combined with qubit swapping that optimizes the construction of uniformly controlled Rz gates for the target topology, and a heuristic for reducing CNOT gates by exploiting the structure of long-range CNOT ladders. We benchmark our method against TKet, Qiskit, and Pennylane on the 20-qubit IQM Garnet (square lattice) and the 156-qubit IBM Marrakesh (heavy-hex) architectures with qubit counts ranging from 3 to 11. Our method achieves CNOT count reductions of up to 36 percent on the IQM Garnet and up to 34 percent on the IBM Marrakesh compared to the best competing transpiler, while simultaneously achieving transpilation speedups of up to 553x. Furthermore, our method is the only one capable of transpiling circuits beyond 10 qubits within a 30-minute time limit across both architectures.



## Related
- [[experimental-high-dimensional-multi-qubit-bell-non-locality-|Experimental high-dimensional multi-qubit Bell non-locality on a superconducting quantum processor]]
- [[a-spectral-gap-informed-parameter-schedule-for-qaoa|A Spectral Gap Informed Parameter Schedule for QAOA]]
- [[adaptive-tensor-network-sampling-for-quantum-optimal-control|Adaptive Tensor Network Sampling for Quantum Optimal Control]]
- [[autoqresearch-llm-guided-closed-loop-policy-search-for-adapt|AutoQResearch: LLM-Guided Closed-Loop Policy Search for Adaptive Variational Quantum Optimization]]
- [[cablecar-efficiently-scheduling-qldpc-codes-on-a-tileable-sp|CAbLECAR: efficiently scheduling QLDPC codes on a tileable spin qubit chip with shuttling]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.23777) | 2026-04-28
