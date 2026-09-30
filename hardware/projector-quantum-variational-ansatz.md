---
title: "Projector Quantum Variational Ansatz"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.07084"
summary: "arXiv:2606.07084v2 Announce Type: replace Abstract: Quantum computing offers several algorithms for computing the ground state of a problem Hamiltonian. Algorithms in the Fault-Tolerant Quantum Comput"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2606.07084v2 Announce Type: replace Abstract: Quantum computing offers several algorithms for computing the ground state of a problem Hamiltonian. Algorithms in the Fault-Tolerant Quantum Computing (FTQC) regime, such as Quantum Phase Estimation (QPE) and Quantum Signal Processing (QSP), are the most desirable because they offer optimal asymptotic scaling. In the Noisy Intermediate Scale Quantum (NISQ) regime, the most realistic approaches involve Variational Quantum Eigensolver (VQE) algorithms and their variants. A central difference between the two regimes is that FTQC algorithms do not prepare the ground state via direct state transition. Instead, they build a project that identifies the ground state using ancillary qubits that flag the target subspace. The desired state is then recovered via amplitude amplification or post-selection. In this work, we propose a VQE ansatz whose structure is more similar to that of an FTQC algorithm. We introduce the Projector Variational Ansatz (PVA), which incorporates the projector structure into the adaptive variational setting. Depending on its parametrization, this ansatz can be equivalent to either an Adaptive Derivative-Assembled Pseudo-Trotter (ADAPT)-VQE when all ancilla mixing angles vanish, or to an Intermediate Scale Quantum (ISQ)-QSP quantum circuit structure. We benchmarked PVA against an ADAPT-VQE baseline using both qubit-excitation and fermionic-operator pools. We propose an implementation in which an L-layer PVA circuit is designed using 3L + 1 parameters and requires only one ancilla and two additional CNOT gates per Pauli generator used in ADAPT. Our experimental results show that this first proposal for PVA converges using fewer CNOT gates than the standard ADAPT-VQE on the tested system.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.07084) | 2026-09-30
