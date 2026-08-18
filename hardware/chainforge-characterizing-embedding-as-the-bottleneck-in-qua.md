---
title: "ChainForge: Characterizing Embedding as the Bottleneck in Quantum Annealer Workloads"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.15961"
summary: "arXiv:2608.15961v1 Announce Type: new Abstract: Quantum Annealers (QAs) are among the first commercially scaled quantum computing systems designed for large-scale optimization. Unlike digital systems "
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.15961v1 Announce Type: new Abstract: Quantum Annealers (QAs) are among the first commercially scaled quantum computing systems designed for large-scale optimization. Unlike digital systems that execute sequences of compiled instructions, QAs operate as analog single-instruction machines that directly evolve an Ising Hamiltonian toward low-energy solutions. To execute an application, the logical problem graph must first be mapped onto the hardware's sparse connectivity via embedding, where logical variables are represented by chains of connected physical qubits. As a result, embedding becomes the dominant system challenge in QAs, shaping whether and how workloads can execute on the machine. Despite its central role, embedding has largely been treated as a preprocessing step rather than a system bottleneck. In this work, we present ChainForge, the first systems and architecture characterization of embedding in QA workloads. Using diverse workload families and graph topologies on modern QA hardware, we characterize how embedding impacts effective hardware capacity, routing overheads, runtime variability, and solution quality. Our results show that embedding inflates physical resource usage, long chains degrade annealing fidelity and scalability, and heuristic embedders may fail even when valid embeddings exist. We further show that embedding latency can become a runtime bottleneck for dynamic workloads requiring frequent remapping, while nominal qubit counts significantly overestimate the usable capacity of QAs for realistic applications. Overall, our findings establish embedding as the defining workload bottleneck and systems abstraction of QAs, providing architectural insights for future hardware topologies, runtime systems, and workload-aware annealing platforms.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.15961) | 2026-08-18
