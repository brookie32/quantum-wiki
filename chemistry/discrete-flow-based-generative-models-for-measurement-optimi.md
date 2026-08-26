---
title: "Discrete Flow-Based Generative Models for Measurement Optimization in Quantum Computing"
date: "2026-08-26"
updated: "2026-08-26"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.15486"
summary: "arXiv:2509.15486v3 Announce Type: replace Abstract: Estimating molecular Hamiltonians to chemical accuracy requires a large number of measurements. Hamiltonian overlapping grouping methods focus on re"
last_verified: "2026-08-26"
review_by: "2026-11-24"
stale: false
---

arXiv:2509.15486v3 Announce Type: replace Abstract: Estimating molecular Hamiltonians to chemical accuracy requires a large number of measurements. Hamiltonian overlapping grouping methods focus on reducing measurement counts, employing greedy initializations, such as sorted insertion (SI), leaving useful measurement/circuit trade-offs unexplored. Here, we formulate Hamiltonian grouping as a reward-driven generative search problem and introduce a Generative Flow Networks (GFlowNets)-based model that colors graph representations of molecular qubit Hamiltonians to sample non-overlapping commuting groupings. The reward function can combine measurement cost, circuit count, and compiled two-qubit-gate count, enabling multi-objective optimization without differentiable cost functions or model pretraining. Across molecular Hamiltonian benchmarks, the GFlowNets sampler finds fully commuting non-overlapping groupings with average measurement requirements 18% lower than SI, and produces Pareto sets that expose trade-offs among shots, circuits, and two-qubit resources. When used to initialize iterative coefficient splitting (ICS), GFlowNet-generated groupings reduce post-ICS measurement estimates by up to 40% for Jordan-Wigner-mapped fully commuting Hamiltonians relative to SI initialization. Composite rewards further identify lower two-qubit gate groupings, including cases with more than 100 fewer compiled two-qubit gates, while retaining comparable post-ICS measurement benefits. GFlowNets provide a flexible workflow for resource-aware measurement and quantum-resource optimization in quantum chemistry, replacing single-heuristic outputs with diverse candidate groupings that can be selected according to hardware-specific priorities. Our results show that our GFlowNets' generative policy framework not only reduces measurement and two-qubit gate costs but also provides flexibility for hardware-aware adaptations via its reward function.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.15486) | 2026-08-26
