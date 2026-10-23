---
title: "Multi-FPGA Synchronization and Data Communication for Quantum Control and Measurement"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2506.09856"
summary: "arXiv:2506.09856v2 Announce Type: replace Abstract: Quantum computing has grown from novel physics experiments with a few qubits controlled by a single controller to systems with qubit counts that req"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2506.09856v2 Announce Type: replace Abstract: Quantum computing has grown from novel physics experiments with a few qubits controlled by a single controller to systems with qubit counts that require multiple controllers working in concert. While a few expensive multi-board commercial solutions exist, most open-source solutions are limited to single-board radio frequency system-on-chip (RFSoC). The essential requirements for a multi-board solution are clock synchronization among multiple boards and the ability to transfer data with low latency for performing real-time feedback. In this work, we design a clock synchronization framework to distribute deterministic clock and synchronize the clock counters across multiple RFSoC boards to generate time-aligned radio frequency (RF) pulses used to control qubits. We also develop a data communication system over a fiber link to transfer quantum measurement data among multiple field-programmable gate arrays (FPGAs). This clock synchronization and data communication module has been integrated into the open-source quantum control system, QubiC, to enable the execution of quantum algorithms across multiple boards. We validate the design through bench tests and qubit experiments on a superconducting quantum processor. Qubit coherence experiments driven by two clock-synchronized boards show no measurable degradation compared to single-board operation. The data communication link, built directly on raw gigabit transceivers with a minimal custom protocol, achieves a one-way board-to-board latency of 71.2 pm 2.6 ns and enables a real-time cross-board conditional bit-flip experiment, demonstrating mid-circuit measurement and feed-forward across multiple boards well within the qubit coherence time.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2506.09856) | 2026-10-23
