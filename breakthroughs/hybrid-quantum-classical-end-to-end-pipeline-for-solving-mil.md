---
title: "Hybrid quantum-classical end-to-end pipeline for solving MILPs: a vehicle routing case study"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.26771"
summary: "arXiv:2607.26771v1 Announce Type: new Abstract: We demonstrate an end-to-end hybrid quantum-classical optimisation framework based on Benders decomposition, capable of solving mixed-integer linear pro"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2607.26771v1 Announce Type: new Abstract: We demonstrate an end-to-end hybrid quantum-classical optimisation framework based on Benders decomposition, capable of solving mixed-integer linear programming (MILP) problems. The framework builds on a previously presented hybrid quantum-classical end-to-end pipeline based on Multiple Cuts via Multiple Solutions (MCMS) Benders decomposition where the cut selection step was performed on quantum annealing hardware. We extend this with gate-based QAOA implementations for both tensor network emulators and superconducting quantum hardware. The Vehicle Routing Problem (VRP) is used as a representative case study and we run the pipeline end-to-end on 10 permutations of a standardised benchmarking instance (20 customers and 4 vehicles from QOptLib) with a classical solver performing the cut selection step. We find that for our instances, only a small fraction of the compute in classical MCMS Benders decomposition is spent on the cut selection step. For a full hybrid end-to-end assessment, we run the pipeline for a toy problem with MPS-JuliQAOA, a powerful tensor network emulator, to execute QAOA. Here, the majority of the time is spent on the cut selection step, deeming quantum advantage of this framework unlikely at problems of this size. This highlights the need for more large-scale benchmarking research when more powerful (QPU) QUBO solvers are available.



## Related
- [[experimental-workflows-for-combinatorial-optimization-toward|Experimental Workflows for Combinatorial Optimization: Towards Quantum Advantage]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.26771) | 2026-07-30
