---
title: "Parallel Circuit Execution for Scalable Quantum Computation"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.12172"
summary: "arXiv:2609.12172v1 Announce Type: new Abstract: Today's quantum processors have tens to hundreds of physical qubits, but reliable execution of arbitrary circuits remains limited to fewer than 30 entan"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

arXiv:2609.12172v1 Announce Type: new Abstract: Today's quantum processors have tens to hundreds of physical qubits, but reliable execution of arbitrary circuits remains limited to fewer than 30 entangled qubits across hardware modalities. Building upon prior work, we introduce an error- and topology-aware method for mapping multiple independent circuits onto disjoint regions of a single large-scale QPU for parallel circuit execution. For applications with many similarly sized circuits, such as observable estimation for Hamiltonian simulation, this approach can reduce billed QPU execution time, with ideal speedup proportional to the number of usable partitions. We demonstrate the approach on IBM's 156-qubit ibm_boston processor using standard QED-C benchmark and Hamiltonian-based observable-estimation workloads. Compared with standard sequential execution, parallel execution reduces billed execution time by 3.5-5.5x while retaining 83-92% of the sequential fidelity. We further evaluate the scaling of parallel circuit execution using GPU-accelerated classical simulation, distributing measurement circuits across GPUs via MPI. Using CUDA-Q on the NERSC Perlmutter system, we achieve up to 13.8x speedup on 16 GPUs (86% parallel efficiency) for an H2 electronic-structure simulation, with scaling evaluated across multiple Hamiltonians and circuit counts. These results provide an indication of the performance ceiling that parallel execution on future quantum hardware may eventually approach. Both execution modes are implemented as a runtime option within the QED-C Application-Oriented Benchmark suite. Together, the results show that circuit-level parallelism can reduce execution cost on current quantum hardware and simulation time on GPU clusters, with the potential for greater benefits as device quality and qubit counts increase.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.12172) | 2026-09-14
