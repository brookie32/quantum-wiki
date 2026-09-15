---
title: "A Modular, Topology-Aware Software Stack for Entanglement-Based Distributed Quantum Computing"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.15728"
summary: "arXiv:2609.15728v1 Announce Type: new Abstract: Distributed quantum computing (DQC) seeks to scale beyond the limits of monolithic processors by interconnecting multiple quantum processing units (QPUs"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.15728v1 Announce Type: new Abstract: Distributed quantum computing (DQC) seeks to scale beyond the limits of monolithic processors by interconnecting multiple quantum processing units (QPUs) through entanglement-based links. Realizing this vision requires the co-design of hardware and software across the domains of quantum networking, compilation, and scheduling, yet existing tools remain fragmented between monolithic circuit compilers and long-distance quantum network simulators. We present an open-source, topology-informed framework for the compilation and scheduling of distributed quantum programs. Given an input circuit and a description of the target network, the framework partitions and reconstructs the circuit into a distributed program that respects the specified inter- and intra-QPU topology, covers cross-QPU operations through gate and state teleportation, and schedules the result under either deterministic or stochastic entanglement-generation models. By accepting and emitting standard OpenQASM, the framework interoperates with existing monolithic toolchains, and its standardized module interfaces allow partitioning and scheduling strategies to be interchanged and benchmarked. Using this framework, we show that the best-performing compilation strategy varies across the tested circuits and network configurations, and that both network topology and intra-QPU connectivity substantially affect the entanglement cost of execution. These findings underscore the need for a co-design approach to distributed quantum computing, which our framework is designed to support.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.15728) | 2026-09-15
