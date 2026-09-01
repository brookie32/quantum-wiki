---
title: "C-Phase-Aware Compilation for Efficient Fault-Tolerant Quantum Execution"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.14042"
summary: "arXiv:2605.14042v2 Announce Type: replace Abstract: Achieving practical quantum advantage on fault-tolerant quantum computers (FTQC) is fundamentally constrained by the substantial spatial and tempora"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2605.14042v2 Announce Type: replace Abstract: Achieving practical quantum advantage on fault-tolerant quantum computers (FTQC) is fundamentally constrained by the substantial spatial and temporal overheads required to map logical operations onto physical hardware. Existing compilation approaches typically adopt coarse-grained, slice-based abstractions that overlook fine-grained microarchitectural effects, such as routing contention, leading to inefficient resource utilization and limited alignment between algorithm structure and hardware capabilities. We introduce Qomet, a microarchitecture-aware compiler that tightly couples algorithmic properties with lattice surgery (LS) execution. By exploiting C-Phase gate commutativity, Qomet translates sequential operations into simultaneous multi-target interactions, natively leveraging LS to eliminate false dependencies and expose instruction-level parallelism. To support this, Qomet employs an adaptive, event-driven scheduler that captures precise spatial and routing constraints to overlap instructions temporally. By minimizing grid idling and routing contention, Qomet achieves a geometric-mean execution speedup of 4.29imes and a maximum speedup of 59.7imes across realistic workloads.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.14042) | 2026-09-01
