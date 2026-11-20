---
title: "RELIQ: Optimizing Parallel Execution of Commuting Pauli Product Rotations"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.23738"
summary: "arXiv:2605.23738v2 Announce Type: replace Abstract: Fault-Tolerant Quantum Computation (FTQC) permits parallel execution of mutually commuting Pauli Product Rotations (PPRs), but per-qubit access poin"
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2605.23738v2 Announce Type: replace Abstract: Fault-Tolerant Quantum Computation (FTQC) permits parallel execution of mutually commuting Pauli Product Rotations (PPRs), but per-qubit access point/port limits (e.g. two X and two Z edges on the surface code) force commuting groups that exceed the budget to execute sequentially, inflating circuit depth. We show that minimizing this hardware-limited depth is NP-hard and propose two heuristics for reducing it: 1. port-aware list scheduling, which reorders commuting PPRs by placing each PPR in the earliest group that can still accommodate it, and 2. generator restructuring, which rewrites each group as an equivalent generating set with reduced per-qubit port pressure. On QASMBench circuits compiled to PPRs, we combine the two heuristics in RELIQ (Restructure + List schedule Quantum circuits) and observe an average hardware-limited depth reduction of 76.3% and 79.1% for Clifford + T and Clifford + Rz circuits, respectively, over a non-reordering baseline. These gains persist as the per-qubit port budget grows, with RELIQ still reducing the depth by 71.7% and 51.2% at 16 ports, suggesting these heuristics remain relevant even as hardware exposes more access points.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.23738) | 2026-11-20
