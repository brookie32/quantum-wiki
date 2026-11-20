---
title: "Formal Verification of Continuous-Variable Quantum Programs"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.17714"
summary: "arXiv:2607.17714v2 Announce Type: replace Abstract: Continuous-variable quantum computing (CQC) is a promising paradigm already accessible through public cloud services. Yet, unlike discrete-variable "
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2607.17714v2 Announce Type: replace Abstract: Continuous-variable quantum computing (CQC) is a promising paradigm already accessible through public cloud services. Yet, unlike discrete-variable quantum computing (DQC), CQC lacks a formal program logic. Extending existing quantum Hoare logics to CQC poses fundamental challenges: continuous-variable quantum programs act on {em infinite-dimensional} Hilbert spaces; their measurement outcomes are often {em unbounded}, so expectation values may {em diverge}. We overcome these challenges to give a formal semantics to a universal programming language for CQC and, to our knowledge, provide the first Hoare logic for CQC. We introduce an assertion language based on polynomials over canonical observables and establish soundness and relative completeness of the resulting logic. We also implement a symbolic weakest-precondition calculator for CQC. Our tool has successfully verified CQC algorithms from textbooks and calculated their approximation errors for physically realizable implementations, proved the correctness (i.e., equivalence) of gate decompositions for CQC hardware, and computed the resource requirements (i.e., number of photon-number states) for achieving a desired accuracy in the classical simulation of continuous-variable quantum programs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.17714) | 2026-11-20
