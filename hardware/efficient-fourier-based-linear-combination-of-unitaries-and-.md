---
title: "Efficient Fourier-Based Linear Combination of Unitaries and Applications in Quantum Optimization"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.18985"
summary: "arXiv:2605.18985v2 Announce Type: replace Abstract: We investigate ancilla-free linear combination of unitaries (LCU) as a framework for approximating complex quantum circuits. This is particularly ef"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2605.18985v2 Announce Type: replace Abstract: We investigate ancilla-free linear combination of unitaries (LCU) as a framework for approximating complex quantum circuits. This is particularly effective for quantum optimization algorithms, where candidate solutions can be evaluated classically and the task is to sample high-quality bitstrings rather than reproduce the full output distribution. We show that Fourier-based LCU constructions efficiently decompose broad classes of diagonal and non-diagonal unitaries, replacing highly connected qubit interactions with single-qubit gate layers or significantly simpler structures at the cost of a polynomial sampling overhead. Applied to algorithms such as QAOA, this yields efficient, hardware-friendly decompositions of, for instance, cardinality-constraint penalties and the fully connected XY-mixer, while maintaining rigorous performance guarantees compared to fully coherent implementations. Furthermore, we establish a formal connection between Fourier-based quantum penalties and Lagrangian relaxation, offering a unified perspective on constraint handling. We validate our approach using exact statevector simulations of 12-qubit circuits and large-scale experiments on 106 superconducting qubits. Our results illustrate how approximate sampling via an LCU systematically trades circuit complexity for sampling overhead, extending the practical reach of near-term quantum optimization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.18985) | 2026-09-04
