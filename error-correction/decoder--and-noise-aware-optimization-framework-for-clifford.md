---
title: "Decoder- and Noise-Aware Optimization Framework for Clifford-Deformed Quantum Error-Correcting Codes"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.13589"
summary: "arXiv:2610.13589v1 Announce Type: new Abstract: Practical fault-tolerant quantum computing requires qubit-efficient quantum error correction (QEC). Clifford deformations (CDs) modify the stabilizers o"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2610.13589v1 Announce Type: new Abstract: Practical fault-tolerant quantum computing requires qubit-efficient quantum error correction (QEC). Clifford deformations (CDs) modify the stabilizers of a QEC code to lower its logical error rate at no additional resource cost. However, the number of possible CDs grows exponentially with the number of qubits, making exhaustive search infeasible beyond small codes. In this work, we further show that under circuit level noise the optimal CD depends strongly on both the noise model and decoder. To make systematic CD optimization possible, we introduce Evolution-Based Best-arm Identification (EBBI), a shot-efficient search algorithm that treats the circuit, noise model and decoder as a black box. We benchmark EBBI's performance on the rotated surface code, under two strongly Z-biased circuit-level noise models with the PyMatching decoder. At distance 3, EBBI finds the optimal CD using up to sim 1100imes fewer shots than random search. At distance 5, when run at the target error rate, the median EBBI run converges to the CDs we believe to be optimal, while random search never converges. Under a Z-biased SI1000-like noise model, EBBI discovers a new CD, the B-XZZX code, which we generalized to larger distances. It differs from XZZX on only a fraction O(d^{-1}) of the qubits at code distance d, yet its relative advantage grows from approx 5% at d = 3 to approx 12% at d = 11. We thus show that the B-XZZX pattern found by EBBI can be systematically scaled to larger code distances. Our work represents a first step towards scalable CD optimization for general QEC codes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.13589) | 2026-10-12
