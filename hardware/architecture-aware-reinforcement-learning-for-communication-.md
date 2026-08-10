---
title: "Architecture-Aware Reinforcement Learning for Communication-Efficient Distributed Quantum Circuit Compilation"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.06892"
summary: "arXiv:2608.06892v1 Announce Type: new Abstract: Distributed quantum computing provides a scalable route for executing quantum circuits beyond the capacity limits of a single quantum processing unit (Q"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2608.06892v1 Announce Type: new Abstract: Distributed quantum computing provides a scalable route for executing quantum circuits beyond the capacity limits of a single quantum processing unit (QPU), but it introduces a communication-aware compilation problem involving strict hardware constraints and circuit dependencies. This paper presents an architecture-aware reinforcement-learning framework that formulates distributed quantum compilation as a constrained Markov Decision Process (MDP). The compiler-level communication actions dynamically update logical-qubit placement and enable subsequent gate execution. A heterogeneous graph model represents interactions among hardware, logical qubits, and circuit operations, while a policy trained via Proximal Policy Optimization optimizes EPR-pair consumption and communication makespan. Evaluation across benchmark circuits shows that our policy matches state-of-the-art heuristics on structured workloads, with lookahead reward shaping yielding modest improvements on unstructured circuits. These results demonstrate that reinforcement learning is a flexible alternative to manual heuristics, though scalability remains a key bottleneck for practical use.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.06892) | 2026-08-10
