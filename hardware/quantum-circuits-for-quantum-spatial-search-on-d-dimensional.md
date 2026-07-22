---
title: "Quantum Circuits for Quantum Spatial Search on d-Dimensional Lattices"
date: "2026-07-22"
updated: "2026-07-22"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.19151"
summary: "arXiv:2607.19151v1 Announce Type: new Abstract: We propose an explicit quantum circuit for quantum spatial search based on discrete-time quantum walks on d-dimensional lattices. In this algorithm, the"
last_verified: "2026-07-22"
review_by: "2026-10-20"
stale: false
---

arXiv:2607.19151v1 Announce Type: new Abstract: We propose an explicit quantum circuit for quantum spatial search based on discrete-time quantum walks on d-dimensional lattices. In this algorithm, the flip-flop shift operator moves the walker to a neighboring site along the selected spatial direction and reverses the corresponding direction label after the move. By encoding each pair of opposite directions so that they differ only in the least significant qubit of the coin register, we implement the shift using coin-controlled modular increment and decrement operations on the position registers, together with a single X gate that reverses the direction label. We verify that the proposed circuits reproduce the theoretical dynamics on two- and three-dimensional periodic lattices. We further extend the circuit construction to systems with position-dependent shift rules, such as non-periodic boundaries, and validate this extension on a two-dimensional lattice. The resource analysis shows logarithmic growth of the circuit width. For the two-dimensional lattice, the synthesized depth is consistent with O(sqrt{N}(log N)^{3/2}), while the three-dimensional depth empirically follows an O(sqrt{N}) dependence over the investigated range. Under a CX-gate depolarizing noise model, CX-optimized circuits exhibit improved noise robustness. These results provide a practical framework for implementing quantum spatial search on regular lattices and extending it to defective and other irregular lattice structures.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.19151) | 2026-07-22
