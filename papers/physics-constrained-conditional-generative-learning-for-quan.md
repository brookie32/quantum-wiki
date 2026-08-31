---
title: "Physics-Constrained Conditional Generative Learning for Quantum State and Process Tomography"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.28035"
summary: "arXiv:2608.28035v1 Announce Type: new Abstract: Quantum state and process tomography constitute essential diagnostic tools in quantum information science, yet their standard formulations suffer from p"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2608.28035v1 Announce Type: new Abstract: Quantum state and process tomography constitute essential diagnostic tools in quantum information science, yet their standard formulations suffer from prohibitive computational scaling as the number of qubits grows. In this work, we introduce a physics-constrained conditional generative adversarial network that bypasses iterative constrained inversion by directly learning a forward generative mapping conditioned on Pauli expectation values. The generator embeds a differentiable Cholesky layer at its output, which enforces Hermiticity, positive semidefiniteness, and unit trace by construction. Our experiments reveal that the strength of the L^1 penalty critically governs the emergence of GHZ coherence during training: an excessively large penalty postpones the coherence onset and yields a prolonged low-fidelity plateau, whereas an intermediate value enables the fastest stable convergence. Moreover, for high-temperature thermal states, an over-complete measurement basis proves necessary to prevent sustained late-stage fluctuations. By extending the same Cholesky constraint to the Choi-matrix representation, the framework naturally accommodates quantum process tomography. For systems with n ge 6 qubits, the exponential growth of the underlying 2^n imes 2^n density matrix remains the fundamental bottleneck; we discuss how integrating tensor-network structures can contain the per-iteration cost while preserving reconstruction fidelity. Altogether, these results suggest that physically constrained generative learning offers a scalable and amortizable pathway toward data-driven tomography for noisy intermediate-scale quantum devices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.28035) | 2026-08-31
