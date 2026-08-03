---
title: "Qubit Loss Inference with Stabilizer Codes without Leakage Detection Units"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.29603"
summary: "arXiv:2607.29603v1 Announce Type: new Abstract: Qubit loss occurs when the physical carrier of a qubit leaves the computational system without directly revealing the event's location. Such errors are "
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

arXiv:2607.29603v1 Announce Type: new Abstract: Qubit loss occurs when the physical carrier of a qubit leaves the computational system without directly revealing the event's location. Such errors are a major obstacle to fault-tolerant quantum computation on platforms including photonic, neutral-atom, and trapped-ion systems. Loss locations are commonly identified using additional hardware operations such as leakage-detection units (LDUs), which introduce space-time overhead and may themselves become a source of error. We investigate whether qubit loss on stabilizer codes can instead be inferred from syndrome data obtained through standard repeated stabilizer measurements. Under a non-entangling model for gates involving a lost qubit, we derive a sufficient condition for loss detectability in general stabilizer codes. The condition is based on the emergence of anticommutation between stabilizer checks after their support on the lost qubits is removed. By using that condition, we formulate the exact loss-inference problem using the observed set of non-deterministic checks together with its maximum-likelihood formulation. We then relax the problem to the minimum set cover problem with a greedy heuristic algorithm. We evaluate the resulting inference and loss-correction protocols on the rotated surface code via circuit-level noise simulations for trapped-ion and neutral-atom platforms. On both platforms, inference-based and adaptive protocols reduce the logical error rate relative to a noisy-LDU baseline in the low-to-moderate loss-rate regime relevant to near-term hardware, while requiring fewer space-time overheads.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.29603) | 2026-08-03
