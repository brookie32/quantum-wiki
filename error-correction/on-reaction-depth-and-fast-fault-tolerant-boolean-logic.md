---
title: "On Reaction Depth and Fast Fault-Tolerant Boolean Logic"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.24687"
summary: "arXiv:2611.24687v1 Announce Type: new Abstract: Reducing runtimes of quantum applications is critical for practical viability. On quantum computers, the runtime can depend both on the speed of quantum"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.24687v1 Announce Type: new Abstract: Reducing runtimes of quantum applications is critical for practical viability. On quantum computers, the runtime can depend both on the speed of quantum operations and on how often the program must wait for the classical coprocessor to determine adaptive operations. Some recent approaches to reducing this overhead have focused on minimizing the "reaction depth" of a computation, informally defined as the number of times the classical coprocessor must be consulted while running a quantum program. In this work, we formalize the notion of reaction depth. We find several subtleties in this theory. For example, we distinguish the reaction depth of a circuit from that of a circuit run, and show that the magic depth of a unitary can be higher than the reaction depth once compiled into Clifford computation and magic state injection. We then focus on the specific case of coherent Boolean logic, a common and expensive component in quantum algorithms. We use a natural gateset for fast operations with Low-Density Parity Check (LDPC) codes, which consists of homogeneous Z- and X-type Pauli Product Measurements (PPMs), alongside a supply of Toffoli states. We prove that, using this gateset, any Boolean arithmetic circuit can be implemented on a quantum computer with constant quantum depth and constant reaction depth, at the cost of exponential space and leaving some qubits "dirty". Using the same gateset we find two efficient AutoAND circuits that require only a Toffoli state and homogeneous PPMs. We then give efficient implementations of the quantum ripple-carry adder and quantum schoolbook multiplier, which require a low number of heterogeneous PPMs for uncomputation. We find implementations competitive with the state-of-the-art despite the restricted gateset.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.24687) | 2026-11-19
