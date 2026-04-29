---
title: "A SWAP-free Framework for QAOA"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25058"
summary: "arXiv:2604.25058v1 Announce Type: new Abstract: The performance of the Quantum Approximate Optimization Algorithm (QAOA) on noisy intermediate-scale quantum (NISQ) devices is strongly limited by spars"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25058v1 Announce Type: new Abstract: The performance of the Quantum Approximate Optimization Algorithm (QAOA) on noisy intermediate-scale quantum (NISQ) devices is strongly limited by sparse qubit connectivity. When interactions required by QAOA Hamiltonians are not aligned to the hardware topology, transpilation introduces SWAP gates, increasing circuit depth and noise. We propose a SWAP-free QAOA framework based on modifying the cost Hamiltonian so that it can be implemented natively on the hardware. We formulate this as a mixed-integer semidefinite program (MISDP) that selects a hardware-compatible approximation of the original cost matrix and optimizes the allocation of logical variables to physical qubits. We prove that the associated decision problem is NP-complete and derive theoretical guarantees relating the MISDP objective to the loss in the original optimization problem through the Lovasz number of the hardware graph. Since solving MISDPs is practical only for small instances, we introduce heuristics based on spectral properties of the problem matrix and hardware graph. Our experiments on a cardinality-constrained quadratic optimization model for index tracking show competitive performance against a baseline representing ideal QAOA under SWAP-induced noise. These results indicate that, on sparse NISQ architectures, a hardware-aware approximation of the objective may be more effective than an exact but heavily transpiled Hamiltonian implementation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25058) | 2026-04-29
