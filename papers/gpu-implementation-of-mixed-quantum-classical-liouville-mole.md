---
title: "GPU implementation of mixed quantum-classical Liouville molecular dynamics without momentum jump"
date: "2026-08-17"
updated: "2026-08-17"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.14544"
summary: "arXiv:2608.14544v1 Announce Type: cross Abstract: We implemented on GPU a mixed quantum-classical Liouville molecular dynamics simulation based on a momentum-jump-free theory. The trajectory spawning "
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

arXiv:2608.14544v1 Announce Type: cross Abstract: We implemented on GPU a mixed quantum-classical Liouville molecular dynamics simulation based on a momentum-jump-free theory. The trajectory spawning that was previously implemented on CPU for sampling enhancement was eliminated to avoid the overhead of thread divergence and dynamic memory allocation on the GPU. This achieved a speedup of an order of magnitude compared to the CPU computation with spawning, as well as a linear scaling with respect to the number of sampling trajectories.



## Related
- [[learning-to-rank-tensor-network-contraction-plans-for-gpu-ac|Learning to Rank Tensor Network Contraction Plans for GPU-Accelerated Quantum Circuit Simulation]]
- [[numerical-methods-for-the-simulation-of-quantum-walks-and-qu|Numerical methods for the simulation of quantum walks and quantum annealing]]
- [[criteria-for-feasible-monte-carlo-stochastic-simulations-of-|Criteria for Feasible Monte Carlo Stochastic Simulations of Bosonic Markovian Open Quantum Dynamics]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.14544) | 2026-08-17
