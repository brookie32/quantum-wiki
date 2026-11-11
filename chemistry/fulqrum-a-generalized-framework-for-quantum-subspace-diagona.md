---
title: "Fulqrum: a generalized framework for quantum subspace diagonalization"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.18731"
summary: "arXiv:2603.18731v3 Announce Type: replace Abstract: We present an open-source software framework for computing the solution to Hamiltonian eigenproblems in a subspace defined by bit-strings sampled fr"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2603.18731v3 Announce Type: replace Abstract: We present an open-source software framework for computing the solution to Hamiltonian eigenproblems in a subspace defined by bit-strings sampled from a quantum computer. Hamiltonians are represented using an extended alphabet that includes projection and ladder operators, yielding a unified solution method for qubit and fermionic systems. Operators are grouped and sorted so that only non-zero terms need be evaluated and a minimal number of subspace lookup operations performed. Bit-strings are expressed using bit-sets to reduce memory consumption and allow for evaluating operators with no fundamental limit on the number of qubits. Subspaces defined over bit-sets are stored in a hash map format that allows for efficient indexing and lookup operations. Specializations for problems, such as those from quantum chemistry, can further reduce computational costs. Our method can be used to directly construct sparse matrix Hamiltonian representations or obtain matrix-free solutions, allowing users to utilize their eigensolver of choice. We show the benefits of our framework by computing the ground-state solution to examples from condensed matter physics and quantum chemistry with less memory and runtime compared to existing techniques, in some cases by two orders of magnitude or more. This work provides a flexible interface for performant quantum-classical eigensolutions for candidate quantum advantage applications.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.18731) | 2026-11-11
