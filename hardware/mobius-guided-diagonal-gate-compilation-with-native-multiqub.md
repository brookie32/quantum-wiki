---
title: "Mobius-Guided Diagonal-Gate Compilation with Native Multiqubit Controlled-Phase Gates on Neutral-Atom Processors"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.08212"
summary: "arXiv:2607.08212v2 Announce Type: replace Abstract: Diagonal gates are ubiquitous primitives in quantum algorithms, from phase oracles, hypergraph-state preparation, and multi-control logic to Hamilto"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2607.08212v2 Announce Type: replace Abstract: Diagonal gates are ubiquitous primitives in quantum algorithms, from phase oracles, hypergraph-state preparation, and multi-control logic to Hamiltonian simulation of spin models and digitized lattice field theories, where Ising interactions and local potential terms are diagonal in the encoded basis. Standard compilers, however, often lower diagonal structure into one- and two-qubit gates before neutral-atom hardware can exploit native Rydberg-mediated multiqubit controlled-phase operations. We propose a Mobius-guided compiler that maps a diagonal phase function to a phase hypergraph via subset-lattice Mobius inversion. The hypergraph retains the support and angle of each many-body phase term, allowing sparse or local high-order structure to be routed as native multiqubit controlled-phase candidates when feasible and decomposed otherwise. The neutral-atom scheduler accounts for atom motion, interaction-zone constraints, blockade feasibility, and error costs, enabling a direct comparison between native high-order execution and decomposed alternatives. Benchmarks against routed ZAP and ZX-calculus baselines show improved estimated success for algorithmic instances with exploitable three- and four-body phase terms, and comparable performance on predominantly two-body instances. These results provide a feasible compilation strategy for more fully exploiting the native capabilities of neutral-atom hardware, using atom reconfigurability and Rydberg-mediated multiqubit phase operations as practical resources for more efficient quantum computation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.08212) | 2026-07-31
