---
title: "Tensor-network simulation of strongly coupled multi-fluxonium circuits"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.05627"
summary: "arXiv:2611.05627v1 Announce Type: new Abstract: Designing a superconducting quantum processor rests on predicting the low-lying spectrum of its coupled circuit. The Hilbert-space dimension of the circ"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.05627v1 Announce Type: new Abstract: Designing a superconducting quantum processor rests on predicting the low-lying spectrum of its coupled circuit. The Hilbert-space dimension of the circuit's lumped-element model grows exponentially with the number of circuit nodes. The usual methods split the circuit into subsystems, but that split is hard to choose when the elements are strongly coupled. We present a tensor-network method that chooses no subsystems and whose memory and run time per solve are set by the number of modes and two truncations, the Fock cutoff of each normal mode and the bond dimension of a matrix product state (MPS), not by the Hilbert-space dimension. From the capacitance matrix, the inverse-inductance matrix and the junction list alone, the linear circuit is diagonalized into normal modes. Each junction cosine is then a sum of two products of single-mode operators, so the complete lumped-element Hamiltonian is a matrix product operator (MPO) of small bond dimension with one site per mode, solved by the density matrix renormalization group (DMRG). The normal modes make the method generic, and the tensor network makes it affordable. For two fluxonia joined by a tunable coupler, the method agrees with exact diagonalization of the same truncated space to within 1 MHz. Our circuit of three fluxonia joined by two couplers has 11 normal modes and a truncated space of 10^9 states, out of reach of exact diagonalization in dense or sparse storage. At a bond dimension of 32, its lowest eight levels are converged to within 1 MHz in both truncations, and each state is stored in a small fraction of the numbers a dense vector needs. One solve at that bond dimension takes 81 min and 1.3 GB of memory on one CPU node.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.05627) | 2026-11-05
