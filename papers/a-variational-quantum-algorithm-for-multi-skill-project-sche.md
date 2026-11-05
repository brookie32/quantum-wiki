---
title: "A Variational Quantum Algorithm for Multi-Skill Project Scheduling"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.06502"
summary: "arXiv:2611.06502v1 Announce Type: new Abstract: Job scheduling is an NP-hard optimization problem with clear industrial relevance. In practice, distributing work across a team is not only about meetin"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.06502v1 Announce Type: new Abstract: Job scheduling is an NP-hard optimization problem with clear industrial relevance. In practice, distributing work across a team is not only about meeting deadlines or improving productivity; it also affects fatigue, stress, and employee well-being. Variational Quantum Algorithms (VQAs) provide a promising way to address these problems through QUBO formulations, although their scalability on near-term NISQ hardware is still limited by Hilbert-space growth and barren plateaus. In this work, we simulate a VQA for a realistic Multi-Skill Resource-Constrained Project Scheduling Problem (MS-RCPSP), including worker capacities, skill matrices, task priorities, deadlines, and calendar stability during rescheduling. To keep the problem within a near-term circuit size, we use a temporal batch decomposition that solves one day at a time, propagates the remaining workload, and combines it with a logarithmic binary encoding that keeps every batch at or below 30 qubits. Because the ground state of a QUBO Hamiltonian is a computational basis state, entanglement is not required to represent the solution, raising the question of whether it helps or hinders ansatz training. We address this question by comparing the linear and brick-wall entangling topologies of a hardware-efficient ansatz with an entanglement-free reference that has the same number of parameters and by training every configuration with COBYLA and with Adam using SPSA gradient estimation. For the instance and initialization studied, the entanglement-free reference produced feasible schedules under both optimizers. With COBYLA, it produced the feasible schedule closest to the required workload at a fraction of the simulation cost of the entangled topologies, indicating that entanglement did not improve the solutions found by the VQA.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.06502) | 2026-11-05
