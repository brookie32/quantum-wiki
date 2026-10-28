---
title: "From Leaves to Clusters: Depth-Efficient SAT-Oracle Synthesis Based on the FORM Model"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.11401"
summary: "arXiv:2607.11401v2 Announce Type: replace Abstract: Quantum oracles play a fundamental role in many quantum algorithms, such as Grover's search and quantum counting. In oracle synthesis, reducing the "
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2607.11401v2 Announce Type: replace Abstract: Quantum oracles play a fundamental role in many quantum algorithms, such as Grover's search and quantum counting. In oracle synthesis, reducing the circuit depth under a limited number of ancilla qubits is essential, given the constraints of current quantum devices. However, for satisfiability oracles (SAT-oracles) under a limited ancilla budget, existing synthesis methods fail to fully exploit clause-level parallelism, leading to deep circuits. In practice, evaluating clauses in parallel can quickly exhaust the ancilla budget. To address this issue, we introduce the Clustered Synthesis Tree (CST), a depth-oriented SAT-oracle synthesis framework that exploits clause-level parallelism while respecting the ancilla budget. CST leverages a recursive synthesis tree as the backbone for scheduling clause evaluations and groups its clause leaves into clusters, whose clauses are evaluated in parallel by a reversible oracle called ClausePack. To form the clusters, CST introduces a polynomial-time heuristic called SeedGrow for the NP-hard clause-grouping problem, and the resulting tree is compiled into an executable circuit by CST-Map. Compared with the depth-oriented pAND baseline, CST can reduce the circuit depth by an average of 10.2x and 8.8x-11.0x on SATLIB and random 4-CNF benchmarks, respectively, under the same ancilla budgets, while also outperforming the width-oriented pAND, clause-storing, and qSAT baselines.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.11401) | 2026-10-28
