---
title: "Low-gate-count block encodings for second-quantized fermionic Hamiltonians"
date: "2026-09-17"
updated: "2026-09-17"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2510.08644"
summary: "arXiv:2510.08644v2 Announce Type: replace Abstract: Efficient block encoding of many-body Hamiltonians is a central requirement for quantum algorithms in scientific computing, particularly in the earl"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

arXiv:2510.08644v2 Announce Type: replace Abstract: Efficient block encoding of many-body Hamiltonians is a central requirement for quantum algorithms in scientific computing, particularly in the early fault-tolerant era. In this work, we introduce new explicit constructions for block encoding second-quantized Hamiltonians that substantially reduce Clifford+T gate complexity and ancilla overhead. By utilizing a data lookup strategy based on the SWAP architecture for the sparsity oracle O_C, and a direct sampling method for the amplitude oracle O_A with SELECT-SWAP architecture, we achieve a T count that scales as ilde{O}(sqrt{L}) with respect to the number of interaction terms L in general second-quantized Hamiltonians. We also achieve an improved constant factor in the Clifford gate count of our oracle. Furthermore, we design a block encoding that directly targets the eta-particle subspace, thereby reducing the subnormalization factor from O(L) to O(sqrt{L}), and improving fault-tolerant efficiency when simulating systems with fixed particle numbers. Building on the block encoding framework developed for general many-body Hamiltonians, we extend our approach to electronic Hamiltonians whose coefficient tensors exhibit translation invariance or possess decaying structures. Our results provide a practical path toward early fault-tolerant quantum simulation of many-body systems, substantially lowering resource overheads compared to previous methods.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2510.08644) | 2026-09-17
