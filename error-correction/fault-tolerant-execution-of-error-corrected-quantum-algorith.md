---
title: "Fault-tolerant execution of error-corrected quantum algorithms"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.04584"
summary: "arXiv:2603.04584v2 Announce Type: replace Abstract: Scaling up quantum algorithms to tackle high-impact problems in science and industry requires quantum error correction and fault tolerance. While pr"
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2603.04584v2 Announce Type: replace Abstract: Scaling up quantum algorithms to tackle high-impact problems in science and industry requires quantum error correction and fault tolerance. While progress has been made in experimentally realizing error-corrected primitives, the end-to-end execution of logical quantum algorithms using only fault-tolerant (FT) components has remained out of reach. We demonstrate the FT and error-corrected execution of two quantum algorithms, the Quantum Approximate Optimization Algorithm (QAOA) and the Harrow-Hassidim-Lloyd (HHL) algorithm applied to the Poisson equation, on Quantinuum H2 and Helios trapped-ion quantum processors using the [[7,1,3]] Steane code. For QAOA circuits on 5 and 6 logical qubits, we show performance improvements from increasing the number of QAOA layers and the number of T gates used to approximate logical rotations, despite increased physical circuit complexity. We further show that QAOA circuits with up to 8 logical qubits and 9 logical T gates perform similarly to unencoded circuits. For the largest QAOA circuits we run, with 12 logical (97 physical) qubits and 2132 physical two-qubit gates, we still observe better-than-random performance. Finally, we show that adding active QEC cycles and increasing the repeat-until-success limit of state preparation subroutines can improve the performance of a quantum algorithm, thereby demonstrating critical capabilities of scalable FT quantum computation. Our results are enabled by a FT logical T gate implementation with an infidelity of 2.7(4)imes10^{-3} and dynamic circuits with measurement-dependent feedback. Our work demonstrates near-break-even performance of complex, error-corrected algorithmic quantum circuits using only FT components.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.04584) | 2026-11-20
