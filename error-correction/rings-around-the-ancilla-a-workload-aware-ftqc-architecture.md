---
title: "Rings Around the Ancilla: A Workload-Aware FTQC Architecture"
date: "2026-09-17"
updated: "2026-09-17"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.19855"
summary: "arXiv:2604.19855v3 Announce Type: replace Abstract: Obtaining a quantum advantage in practical applications over classical machines requires a fault-tolerant model of computation. However, the resourc"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

arXiv:2604.19855v3 Announce Type: replace Abstract: Obtaining a quantum advantage in practical applications over classical machines requires a fault-tolerant model of computation. However, the resource overhead of developing a fault-tolerant quantum computer (FTQC) architecture is quite high. Current state-of-the-art architecture designs promise constant-time access to logical qubits at the expense of a high qubit overhead, or qubit-dense layouts at the expense of increased latency in the execution of a quantum workload. In this paper, we propose (a) an architecture design that balances the tradeoff of execution time of workloads with the density of logical qubits by placing the surface code patches around the ancilla region, giving almost equal access of the ancilla region to all the data qubits, (b) design a novel algorithm to leverage the T-gate characteristics of the user workload to suggest the optimal placement strategy in the floorplan of our architecture, (c) a workload-selective fast-Y optimization knob that accelerates Y-basis measurements only for qubits whose Y-gate demand justifies the additional tile cost, and (d) explore the scope of executing multiple programs concurrently, which enhances the reconfigurability of our proposed design. Through numerical evaluation, we observe that the proposed architecture design maintains the cycles per instruction time close to optimal while using up to sim21% fewer data tiles, and up to sim90% efficiency under a 10-way concurrency.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.19855) | 2026-09-17
