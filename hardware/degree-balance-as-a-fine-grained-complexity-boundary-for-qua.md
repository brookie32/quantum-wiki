---
title: "Degree Balance as a Fine-Grained Complexity Boundary for Quantum SAT"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.36464"
summary: "arXiv:2609.36464v1 Announce Type: new Abstract: The local Hamiltonian problem is the canonical mathsf{QMA}-complete problem, and O(2^n) time classical algorithms and O(2^{n/2}) time quantum algorithms"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.36464v1 Announce Type: new Abstract: The local Hamiltonian problem is the canonical mathsf{QMA}-complete problem, and O(2^n) time classical algorithms and O(2^{n/2}) time quantum algorithms are known to solve the problem in the worst case. It is not clear how to improve these brute force strategies for a broad class of the problem because ground states are highly entangled in general, and we cannot directly apply known strategies for classical CSPs. In this work, we present exponentially faster classical and quantum algorithms under two mild assumptions: (1) the Hamiltonian is frustration-free on YES instances, and (2) it is approximately regular, meaning that every qubit is acted upon by approximately the same number of constraints. We complement these upper bounds by showing that, assuming (Q)SETH, quantum 5-SAT admits no non-trivial worst-case speedup. Our lower bound further demonstrates that the dependence of our algorithms on regularity is in some sense nearly optimal. Specifically, quantum 5-SAT remains (Q)SETH-hard even for Hamiltonians in which all but O(sqrt{n}) qubits participate in only constantly many constraints, while the remaining O(sqrt{n}) qubits each participate in O(sqrt{n}) constraints. By contrast, if either the size of this high-degree subset or the degrees of its qubits is reduced by a factor of n^elta, for any elta>0, our algorithm solves the problem in time O(2^{(1- arepsilon)n}) for some arepsilon>0. Together, our upper and lower bounds establish a fine-grained complexity dichotomy for quantum satisfiability.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.36464) | 2026-09-30
