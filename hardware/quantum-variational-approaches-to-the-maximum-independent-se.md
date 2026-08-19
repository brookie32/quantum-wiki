---
title: "Quantum Variational Approaches to the Maximum Independent Set Problem at Utility Scale"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.28866"
summary: "arXiv:2606.28866v4 Announce Type: replace Abstract: We study variational quantum algorithms for the Maximum Independent Set (MIS) problem on benchmark graphs of 64, 99, and 180 vertices. The Variation"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2606.28866v4 Announce Type: replace Abstract: We study variational quantum algorithms for the Maximum Independent Set (MIS) problem on benchmark graphs of 64, 99, and 180 vertices. The Variational Quantum Eigensolver (VQE) and Quantum Approximate Optimization Algorithm (QAOA) are compared across SPSA and COBYLA optimizers at multiple circuit depths. A preprocessing pipeline comprising spectral graph reordering (via the Fiedler vector) and distance-based sparsification reduces circuit depth while preserving energy fidelity. Classical post-processing via history-guided bitstring correction and stepwise maximality extension recovers the exact MIS across all instances. With CVaR optimization, VQE with SPSArecovers up to 6 distinct MIS per run for the 64-node instance and up to 10 distinct MIS per run for the 99-node instance, sampling broadly from the optimal solution population. Repeated runs with different SPSA trajectories collectively enumerate a larger fraction of all MIS for each instance. For the 180-node instance, where standard approaches stall at size 14 (MIS is 15), we introduce ancilla-assisted superposition initialization: ancilla qubits prepare a uniform superposition over classically-found near-optimal solutions, and an excitation-preserving ansatz evolves this state while conserving Hamming weight. This novel construction enables quantum-parallel variational search over multiple seeds simultaneously, discovering the exact MIS where single-seed methods fail. The 180-qubit simulation represents, to our knowledge, the largest scale at which gate-based variational algorithms have solved MIS to optimality. Hardware validation on IBM Quantum hardware ibm_marrakesh confirms that converged simulator parameters transfer effectively to noisy quantum execution.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.28866) | 2026-08-19
