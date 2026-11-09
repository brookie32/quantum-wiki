---
title: "A Complete Calculus for Hamiltonian Quantum Programming"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.08675"
summary: "arXiv:2611.08675v1 Announce Type: cross Abstract: Given the forces acting on a quantum particle, a Hamiltonian models its continuous evolution. Quantum computers evolve Hamiltonians to simulate physic"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2611.08675v1 Announce Type: cross Abstract: Given the forces acting on a quantum particle, a Hamiltonian models its continuous evolution. Quantum computers evolve Hamiltonians to simulate physical systems, to solve optimisation problems, and to estimate eigenvalues, and even the popular circuit abstraction is compiled to Hamiltonians on the hardware. We introduce Hamilton, a process calculus whose parallel operator is the sum of interactions acting simultaneously. Its operational semantics is the Lie-Trotter product formula, which recovers a sum as the limit of ever finer sequential interleavings; compiling a program means halving it to a chosen precision and unrolling the interleaving into a circuit. The semantics is fully abstract, the expressible Hamiltonians are exactly those whose Pauli coefficients have the form m/2^k, the precision that successive halving reaches, and the equational theory is complete and decidable. A full implementation compiles Hamilton programs to circuits and decides their equivalence, and Agda proofs sanity-check the core metatheory.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.08675) | 2026-11-09
