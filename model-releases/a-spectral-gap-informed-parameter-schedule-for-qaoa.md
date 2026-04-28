---
title: "A Spectral Gap Informed Parameter Schedule for QAOA"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24580"
summary: "arXiv:2604.24580v1 Announce Type: new Abstract: A challenge with the Quantum Approximate Optimisation Algorithm (QAOA), and variational algorithms in general, is finding good variational parameters, a"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.24580v1 Announce Type: new Abstract: A challenge with the Quantum Approximate Optimisation Algorithm (QAOA), and variational algorithms in general, is finding good variational parameters, a task which in itself can be NP-hard. Recent work has sought to de-variationalise QAOA by picking well-informed guesses for the variational parameters. The Linear Ramp QAOA (LR-QAOA) achieves this by using parameter schedules inspired by the quantum adiabatic algorithm. We go a step further and use spectral gap information from an adiabatic Hamiltonian, with the QAOA mixer Hamiltonian as our initial Hamiltonian, to make smooth ramps which we call Spectral Gap Informed Ramps (SGIR-QAOA). SGIR-QAOA schedules perform slow evolution where the spectral gap of the adiabatic Hamiltonian is small. We show that SGIR-QAOA has performance improvements over LR-QAOA on Grover's problem at constant depth and that SGIR-QAOA requires shorter depths to achieve the same optimal solution probability. We then show that these performance benefits extend to a problem with potential practical applications -- the Maximum Independent Set (MIS) problem. Finally, we demonstrate the scalability of the SGIR-QAOA method using extrapolated spectral gap information for scales that the spectral gap cannot be exactly evaluated, and show that the advantage appears to persist under mild depolarising noise.



## Related
- [[autoqresearch-llm-guided-closed-loop-policy-search-for-adapt|AutoQResearch: LLM-Guided Closed-Loop Policy Search for Adaptive Variational Quantum Optimization]]
- [[exhaustive-and-feasible-parametrisation-with-applications-to|Exhaustive and feasible parametrisation with applications to the travelling salesperson problem]]
- [[do-quantum-transformers-help-a-systematic-vqc-architecture-c|Do Quantum Transformers Help? A Systematic VQC Architecture Comparison on Tabular Benchmarks]]
- [[gsc-qemit-a-telemetry-driven-hierarchical-forecast-and-bandi|GSC-QEMit: A Telemetry-Driven Hierarchical Forecast-and-Bandit Framework for Adaptive Quantum Error Mitigation]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24580) | 2026-04-28
