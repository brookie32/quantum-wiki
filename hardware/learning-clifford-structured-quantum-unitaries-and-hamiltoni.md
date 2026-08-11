---
title: "Learning Clifford-structured quantum unitaries and Hamiltonians"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.09912"
summary: "arXiv:2608.09912v1 Announce Type: new Abstract: Learning algorithms for structured quantum unitaries and Hamiltonians have primarily considered classes of processes that are local or sparse in the Pau"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.09912v1 Announce Type: new Abstract: Learning algorithms for structured quantum unitaries and Hamiltonians have primarily considered classes of processes that are local or sparse in the Pauli basis. We turn our attention to learning n-qubit quantum unitaries U and Hamiltonians H, given query access to U or the unitary evolution of H, that may be dense in the Pauli basis but still admit concise Clifford decompositions. Specifically, we consider unitaries (or Hamiltonians) of the form U = sum_i alpha_i C_i over Cliffords C_i with bounded Clifford extent sum_i |alpha_i|. To extract this Clifford structure, we introduce an agnostic tomography protocol for Clifford unitaries that given query access to an unknown unitary U with optimal Clifford fidelity extsf{opt}, outputs a Clifford unitary witnessing fidelity geq extsf{opt} - arepsilon for some error arepsilon > 0, in time extsf{poly}(n,(1/arepsilon)^{log(1/arepsilon)}). We then apply this protocol to obtain tomography protocols for unitaries and Hamiltonians that have bounded Clifford extent. This extends learnability of Hamiltonians from those with sparse Pauli decompositions to those that are dense (i.e., has sparsity Omega(2^n)) in the Pauli basis but are Clifford structured.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.09912) | 2026-08-11
