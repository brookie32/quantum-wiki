---
title: "Practical lower bounds for hybrid quantum interior point methods in linear programming"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24362"
summary: "arXiv:2604.24362v1 Announce Type: new Abstract: Quantum interior point methods (QIPMs) promise polynomial speed-ups over classical solvers for linear programming by outsourcing the solution of Newton "
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.24362v1 Announce Type: new Abstract: Quantum interior point methods (QIPMs) promise polynomial speed-ups over classical solvers for linear programming by outsourcing the solution of Newton linear systems to quantum linear solvers (QLSAs). However, asymptotic speed-ups do not necessarily translate to practical advantages on realistic problem instances. In this work, I evaluate whether practical advantage of a standard hybrid QIPM pipeline can already be excluded relative to the classical open-source solver HiGHS on a broad and diverse collection of LP instances spanning eight problem families, including public benchmark libraries, such as MIPlib, and relaxations of combinatorial optimisation problems. Following the hybrid benchmarking paradigm initiated by Cade et al., I derive rigorous lower bounds on the quantum runtime under a series of highly benevolent assumptions and compare them against classical runtimes. I equip the QIPMs with the best-performing functional QLSA, the Chebyshev-based method, as identified by Lefterovici et al., and evaluate two Newton system formulations proposed by Mohammadisiahroudi et al.: the modified normal equation system and the orthogonal subspace system. The exclusion analysis yields a consistent negative picture: across all instances and for any realistic quantum cycle duration, the quantum runtime lower bounds already exceed the classical runtimes, establishing that these hybrid QIPMs will offer no practical advantage over good classical solvers for realistic linear programming instances.



## Related
- [[autoqresearch-llm-guided-closed-loop-policy-search-for-adapt|AutoQResearch: LLM-Guided Closed-Loop Policy Search for Adaptive Variational Quantum Optimization]]
- [[a-spectral-gap-informed-parameter-schedule-for-qaoa|A Spectral Gap Informed Parameter Schedule for QAOA]]
- [[exhaustive-and-feasible-parametrisation-with-applications-to|Exhaustive and feasible parametrisation with applications to the travelling salesperson problem]]
- [[gsc-qemit-a-telemetry-driven-hierarchical-forecast-and-bandi|GSC-QEMit: A Telemetry-Driven Hierarchical Forecast-and-Bandit Framework for Adaptive Quantum Error Mitigation]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24362) | 2026-04-28
