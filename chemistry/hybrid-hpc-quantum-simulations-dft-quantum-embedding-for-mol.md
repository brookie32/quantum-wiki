---
title: "Hybrid HPC-Quantum Simulations: DFT-Quantum Embedding for Molecular Systems"
date: "2026-08-14"
updated: "2026-08-14"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.12884"
summary: "arXiv:2608.12884v1 Announce Type: new Abstract: Scientific simulations demand methods combining scalability with predictive accuracy. Density Functional Theory (DFT) on High-Performance Computing (HPC"
last_verified: "2026-08-14"
review_by: "2026-11-12"
stale: false
---

arXiv:2608.12884v1 Announce Type: new Abstract: Scientific simulations demand methods combining scalability with predictive accuracy. Density Functional Theory (DFT) on High-Performance Computing (HPC) enables large-scale electronic-structure simulations but is limited by approximations affecting strongly correlated systems and band-gap predictions. Quantum computing offers a pathway to address this, though current Noisy Intermediate-Scale Quantum (NISQ) hardware remains constrained by qubit resources, noise, and execution cost. This work presents a hybrid DFT-Quantum Embedding (QDFT) framework integrating classical HPC-based DFT with a quantum electronic-structure solver. Large systems are partitioned to isolate a chemically relevant active space, treated via the Variational Quantum Eigensolver (VQE), while the remaining degrees of freedom are described by DFT. The framework incorporates active-space selection, embedded Hamiltonian construction, symmetry preservation, operator mapping, self-consistent density updating, and modular classical-quantum coupling. We focus on noiseless quantum simulation to systematically evaluate accuracy, convergence, active-space dependence, computational cost, and HPC scalability without hardware noise. Detailed profiling identifies computational bottlenecks and highlights limitations of CPU-based quantum simulation. A QPU runtime-estimation methodology is additionally developed to assess execution requirements on actual quantum hardware. Results demonstrate quantum embedding's potential to improve selected electronic-structure properties while retaining classical HPC's scalability. Noisy quantum simulation and QPU execution remain key future directions, providing a pathway toward practical, scalable HPC-quantum hybrid simulations as hardware matures.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.12884) | 2026-08-14
