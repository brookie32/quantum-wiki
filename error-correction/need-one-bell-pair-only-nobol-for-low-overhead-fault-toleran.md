---
title: "Need One Bell-pair Only (NOBOL) for Low-Overhead Fault-Tolerant Quantum Computing"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.01901"
summary: "arXiv:2609.01901v1 Announce Type: new Abstract: Fault-tolerant quantum computation fundamentally relies on encoding a logical qubit into a structured block of physical qubits, typically in the tens to"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.01901v1 Announce Type: new Abstract: Fault-tolerant quantum computation fundamentally relies on encoding a logical qubit into a structured block of physical qubits, typically in the tens to hundreds. As a trade-off for improved fault-tolerance, logical gate operations will incur a linear overhead in terms of both the amount of time and quantum resources than before. For example, in monolithic quantum computing, performing a gate operation on two distant logical qubits will first require using a linear number of SWAP operations in order to move the logical qubits next to each other; while in distributed quantum computing, doing so will first require a linear number of ancilla qubits in order to form entanglement connections (or a logical Bell pair). In this paper, we focus on significantly reducing the overhead involved in logical CNOT operations, a fundamental primitive. We propose NOBOL, a novel approach that requires only one Bell pair to perform a logical CNOT operation on two distant qubits encoded in arbitrary CSS codes. More importantly, NOBOL only requires performing gate operations on the logical X or Z operator subsets of the logical qubits. For many CSS codes, such as the surface code, these subsets are significantly smaller than the size of the code itself. In this paper, we describe various circuit realizations of NOBOL, including a depth-optimal circuit with logarithmic depth in terms of the size of the logical operators. Finally, we propose effective methods to contain error propagation without incurring much additional overhead. Since NOBOL can be effectively applied to a wide range of quantum error-correcting (QEC) codes and, in addition, is agnostic to qubit modalities and effective for various architectures, including those based on either a monolithic QPU or distributed QPUs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.01901) | 2026-09-03
