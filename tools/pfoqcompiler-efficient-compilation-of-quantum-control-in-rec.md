---
title: "pfoqcompiler: Efficient Compilation of Quantum Control in Recursive First-Order Quantum Programs"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.08503"
summary: "arXiv:2611.08503v1 Announce Type: cross Abstract: Recursive quantum control allows for simple and concise descriptions of algorithms. However, a naive circuit compilation sequentializes the different "
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2611.08503v1 Announce Type: cross Abstract: Recursive quantum control allows for simple and concise descriptions of algorithms. However, a naive circuit compilation sequentializes the different branches of the quantum if-statement and results in an exponential increase in circuit depth. Existing techniques can parallelize these branches, but do so at the cost of an exponential number of ancillary qubits. We present pfoqcompiler, a compiler targeting Qiskit for the first-order quantum programming language FOQ that exploits program structure to merge compatible recursive procedure calls across quantum branches. We introduce weaker syntactically-checkable conditions for well-foundedness, recursive halving, and uniformity, while preserving previously demonstrated complexity characterizations. For weakly well-founded bounded-width programs, the compiler produces polynomial-size circuits; weakly recursively halving programs additionally yield polylogarithmic depth, while weak uniformity removes the asymptotic overhead of branch sequentialization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.08503) | 2026-11-09
