---
title: "A Heterogeneous Distributed Architecture for Quantum Simulation"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.09215"
summary: "arXiv:2608.09215v1 Announce Type: new Abstract: Architectural specialization and distribution can help scale fault-tolerant quantum computers, but may also introduce substantial overheads from communi"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.09215v1 Announce Type: new Abstract: Architectural specialization and distribution can help scale fault-tolerant quantum computers, but may also introduce substantial overheads from communication, routing, and resource duplication. We introduce a heterogeneous distributed architecture in which a magic core is connected to an extensible storage system composed of one-dimensional lanes of specialized cold-storage nodes. The storage system supports parallel random access to Pauli string parities. This organization is particularly well suited to fermionic quantum simulation, enabling parallel execution of the highly non-local Pauli strings arising from these systems. We evaluate the architecture on fault-tolerant simulations of the dynamics of the Fermi-Hubbard and sparse Sachdev-Ye-Kitaev (SYK) models on systems of up to 450 logical qubits. These workloads exhibit complementary communication structures: Fermi-Hubbard produces a spectrum of interactions from local to non-local shaped by lattice geometry, whereas sparse SYK produces highly non-local and overlapping Pauli operators. For a Trotter step of a 450-logical-qubit Fermi-Hubbard workload, a six-lane system with 30 T-state factories is within approximately 1.4imes the wall-clock time of a homogeneous distributed architecture with 4 times as many T-state factories and substantially greater connectivity and sites for injecting magic. For matched T-factory counts, our architecture is sim 2imes faster.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.09215) | 2026-08-11
