---
title: "Implications of the PXP ground-state sign structure for neural-network variational Monte Carlo"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.00603"
summary: "arXiv:2611.00603v2 Announce Type: replace Abstract: Positive-definite neural-network quantum states cannot directly represent the ground state of the PXP Hamiltonian, since the ground-state wavefuncti"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.00603v2 Announce Type: replace Abstract: Positive-definite neural-network quantum states cannot directly represent the ground state of the PXP Hamiltonian, since the ground-state wavefunction carries a nontrivial relative-sign structure. Building on the chiral symmetry of the PXP Hamiltonian, we show that this sign structure is fixed exactly by the parity of the total up-spin number: a diagonal unitary transformation that assigns a sign to each spin configuration according to this parity maps the PXP Hamiltonian to its negative, rendering the transformed Hamiltonian stoquastic on the Rydberg-blockaded Hilbert space. Since the configuration graph of allowed configurations is connected, the Perron-Frobenius theorem guarantees a unique, strictly positive ground state of the transformed Hamiltonian, yielding an exact sign rule for the ground state of the original Hamiltonian in terms of the parity of the up-spin number. Variational Monte Carlo performed directly on the transformed Hamiltonian with a positive-definite ansatz therefore requires no architecture-specific modification to represent the true ground state. We evaluate the performance of this formulation using five representative neural-network quantum state architectures, SineKAN, reflection-symmetrized SineKAN, RBM, MLP, and LSTM, for different chain lengths.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.00603) | 2026-11-05
