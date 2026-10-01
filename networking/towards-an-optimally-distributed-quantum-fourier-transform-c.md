---
title: "Towards an Optimally Distributed Quantum Fourier Transform Circuit"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.18494"
summary: "arXiv:2606.18494v2 Announce Type: replace Abstract: A promising avenue for scaling quantum computing is to connect quantum processing units (QPUs) by generating entanglement between them. This require"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2606.18494v2 Announce Type: replace Abstract: A promising avenue for scaling quantum computing is to connect quantum processing units (QPUs) by generating entanglement between them. This requires circuit partitioning: partially rewriting quantum circuits to run on a distributed quantum system using quantum teleportation protocols, while preserving the unitary operation implemented by the circuit. The key metric to minimize when partitioning is the e-bit count, defined as the number of maximally entangled qubit pairs that must be generated between QPUs. We focus on partitioning the quantum Fourier transform (QFT) circuit, which is widely used as a subroutine in quantum algorithms such as quantum phase estimation and arithmetic circuits. Specifically, we present an optimal gate-packing-based partitioning scheme under bounded communication ancilla constraints, as well as a novel detached-gate-based partitioning scheme that achieves optimal e-bit consumption when ancilla availability is unrestricted. We compare these schemes against prior analytical partitioning approaches for the QFT and evaluate them against partitions produced by general-purpose circuit partitioning algorithms. We further validate our approach by implementing the bounded-ancilla circuits on quantum hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.18494) | 2026-10-01
