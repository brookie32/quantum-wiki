---
title: "Efficient simulation of variational quantum circuits: representation, accuracy and CPU/GPU allocation"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.24444"
summary: "arXiv:2611.24444v1 Announce Type: new Abstract: Classical circuit simulation supports quantum software development and verification and provides a baseline for assessing quantum advantage. We compare "
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.24444v1 Announce Type: new Abstract: Classical circuit simulation supports quantum software development and verification and provides a baseline for assessing quantum advantage. We compare gate-based statevector simulation, direct Pauli evolution and matrix product states for molecular and spin Variational Hamiltonian Ansatze and hardware-efficient ansatze on CPU/GPU systems, varying width, depth, precision and resource allocation. In the tested implementations, direct Pauli evolution benefits complex molecular VHA, whereas GPUs accelerate wider spin and hardware efficient circuits. Matrix product state is useful when limited entanglement permits accurate compression; corrected CPU FP32 can meet the tested tolerance while costing more than FP64. Workload size, startup, worker memory and task-specific profiling can change the preferred allocation. Matched NumPy Pauli updates accelerate two-layer full LiH by 3.45-fold; the GPU gives approximately 30-fold acceleration over 18-thread Aer for 28-qubit, four-layer TFIM, both in FP64. We provide a procedure for choosing representation, precision and worker allocation jointly, comparing the cost of complete energy evaluations under accuracy, memory and core constraints.



## Related
- [[parallel-classical-simulation-of-noisy-shallow-circuits-no-q|Parallel classical simulation of noisy shallow circuits: no quantum advantage in 1D]]
- [[a-polynomial-time-classical-sampler-for-noisy-quantum-circui|A polynomial-time classical sampler for noisy quantum circuits from statistical mechanics]]
- [[locally-optimized-variational-evolution-for-quantum-many-bod|Locally optimized variational evolution for quantum many-body systems]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.24444) | 2026-11-19
