---
title: "SAQC: A SAT-Aware Compilation Framework for QAOA-Based Quantum Optimization"
date: "2026-09-10"
updated: "2026-09-10"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.05737"
summary: "arXiv:2609.05737v2 Announce Type: replace Abstract: The Quantum Approximate Optimization Algorithm (QAOA) is a promising variational approach for solving Boolean satisfiability (SAT) problems. Existin"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

arXiv:2609.05737v2 Announce Type: replace Abstract: The Quantum Approximate Optimization Algorithm (QAOA) is a promising variational approach for solving Boolean satisfiability (SAT) problems. Existing SAT-to-QAOA workflows first translate Boolean formulas into penalty Hamiltonians before applying generic quantum compilation, thereby discarding SAT-specific information such as clause structure, logical operators, and variable dependencies. Consequently, subsequent compiler optimizations cannot exploit the underlying Boolean formulation. This paper presents SAQC, a SAT-aware compilation framework that introduces a SAT Intermediate Representation (SIR) to preserve Boolean structure during compilation. The proposed framework supports both CNF and XOR-extended CNF (eCNF) formulations and performs SAT-aware optimizations including clause rewriting, dependency analysis, and clause scheduling prior to quantum lowering. Building on the optimized SIR, SAQC provides a unified framework for both penalty Hamiltonian generation and direct clause-to-ansatz synthesis, together with ansatz optimizations based on relative-phase decomposition, ancilla-assisted synthesis, and dynamic uncomputation. Experimental results demonstrate significant reductions in circuit depth, two-qubit gate count, and compilation time compared with conventional Hamiltonian-based workflows while remaining compatible with existing quantum compilation frameworks.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.05737) | 2026-09-10
