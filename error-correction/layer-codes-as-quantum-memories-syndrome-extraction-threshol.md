---
title: "Layer codes as quantum memories: syndrome extraction, thresholds and idle robustness"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.39522"
summary: "arXiv:2609.39522v1 Announce Type: new Abstract: Layer codes are three-dimensional local CSS codes of check weight at most six, obtained by quasi-concatenating a CSS input code with unrotated surface c"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.39522v1 Announce Type: new Abstract: Layer codes are three-dimensional local CSS codes of check weight at most six, obtained by quasi-concatenating a CSS input code with unrotated surface code patches. What is established about them describes the code, not the circuit that measures it. In this work, we evaluate them as active memories under circuit-level noise. Doing so first requires a syndrome extraction circuit, and the junction stabilizers that couple the patches rule out borrowing a surface code patch's CNOT schedule. We present a decoder-free scheduler that constrains hook propagation first and compresses depth afterwards, generate circuits for eighteen layer codes across four input codes, and compare them with surface codes of the same distance, simulated and decoded in the same way. The circuits lose no distance to hook errors on [[4,2,2]]-input codes wherever a circuit-distance proof is affordable, and reach a lower logical error rate than those of a general-purpose scheduler for CSS codes at roughly half its CNOT depth per round. Our primary family built from a [[4,2,2]] input code reaches a circuit-level threshold of 5.06(7)imes 10^{-3}. The layer code outperforms the surface code in terms of idle robustness: at the same distance it tolerates an interval between syndrome extraction rounds 1.7-3.0 times longer than the rotated surface code. This comes at the cost of 1.7-5.0 times more operations per unit time and approximately five times more physical qubits, both per logical qubit. Finally, we model the cost of the beyond-2D cross-plane CNOTs that the construction demands, and find that their speed matters far more than their fidelity.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.39522) | 2026-10-01
