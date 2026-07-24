---
title: "Trotter error compensation with polylogarithmic precision and nested-commutator scaling without ancillas"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.11856"
summary: "arXiv:2607.11856v2 Announce Type: replace Abstract: Product formulas are among the most practical approaches to Hamiltonian simulation, requiring no ancillary qubits and exhibiting error bounds govern"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.11856v2 Announce Type: replace Abstract: Product formulas are among the most practical approaches to Hamiltonian simulation, requiring no ancillary qubits and exhibiting error bounds governed by nested commutators rather than only by Hamiltonian norms. Their circuit size, however, scales polynomially with the inverse precision. We develop a high-order nested-commutator compensation (HNCC) algorithm that preserves the main advantages of product formulas while achieving polylogarithmic precision dependence in the circuit size and the standard O(arepsilon^{-2}) sampling cost. HNCC uses a truncated Baker--Campbell--Hausdorff expansion to represent high-order Trotter errors by products of nested commutators and compensates these errors at the channel level through randomly sampled Pauli-rotation channels, avoiding Hadamard tests and ancillary qubits. For a fixed K-th order product formula applied to a k-local Hamiltonian on N qubits with Gamma Pauli terms and local interaction strength g_0, HNCC estimates operatorname{tr}[Oe^{-i tH}rho e^{i tH}] to additive precision arepsilon|O| using O(arepsilon^{-2}) repetitions. Its maximum gate count per circuit is Oigl( kN^{frac{1}{2K+1}} Gamma^{1-frac{1}{2K+1}} max{Gamma,Nlog(1/arepsilon)}^{frac{1}{2K+1}} (kg_0tlog(1/arepsilon))^{1+frac{1}{2K+1}} igr). Finite-size resource estimates for the periodic Heisenberg chain indicate that HNCC has the lowest estimated T-gate count per circuit among the product-formula-based methods considered.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.11856) | 2026-07-24
