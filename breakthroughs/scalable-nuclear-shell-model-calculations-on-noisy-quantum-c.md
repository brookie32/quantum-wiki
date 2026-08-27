---
title: "Scalable nuclear shell model calculations on noisy quantum computers"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.16371"
summary: "arXiv:2608.16371v1 Announce Type: cross Abstract: The exact diagonalization of the nuclear shell model scales exponentially, leading to severe memory bottlenecks in classical high-performance computin"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.16371v1 Announce Type: cross Abstract: The exact diagonalization of the nuclear shell model scales exponentially, leading to severe memory bottlenecks in classical high-performance computing (HPC). While hybrid quantum algorithms like the Variational Quantum Eigensolver (VQE) aim to overcome these limits, their deep quantum circuits and iterative feedback loops are susceptible to substantial noise inherent in the current Noisy Intermediate-Scale Quantum (NISQ) hardware. This noise renders several algorithms, such as the VQE, impractical for large-scale calculations despite sophisticated noise-mitigation techniques. As a pragmatic approach tolerant to these issues, we apply the Sample-based Quantum Diagonalization (SQD) framework to nuclear shell models for the first time. Using ^{38}ext{Ar} as a benchmark to confirm the numerical accuracy, we extend SQD to ^{32}ext{Mg}, solving a nuclear shell-model Hamiltonian whose underlying Hilbert space cannot be directly diagonalized using conventional classical methods in a given HPC system. We present a systematic comparison of SQD with standard variational quantum schemes and exact classical solvers. By leveraging NISQ hardware connected via the cloud to classical HPC clusters, the SQD-based scheme could outperform conventional supercomputers in memory scaling and total execution time, enabling more rigorous large-scale shell model calculations.



## Related
- [[hamilton-zero-a-neural-tensor-network-foundation-model-for-g|Hamilton-Zero: A Neural Tensor-Network Foundation Model for Ground States of Arbitrary Quadratic Qubit Hamiltonians]]
- [[quantum-uncomputation-of-clean-and-dirty-ancilla-qubits|Quantum Uncomputation of Clean and Dirty Ancilla Qubits]]
- [[bounded-error-quantum-simulation-via-hamiltonian-and-lindbla|Bounded-Error Quantum Simulation via Hamiltonian and Lindbladian Learning]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.16371) | 2026-08-18
