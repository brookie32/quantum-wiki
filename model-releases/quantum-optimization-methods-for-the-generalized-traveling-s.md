---
title: "Quantum Optimization Methods for the Generalized Traveling Salesman Problem"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25531"
summary: "arXiv:2604.25531v1 Announce Type: new Abstract: This paper studies quantum optimization baselines for the Generalized Traveling Salesman Problem (GTSP), a clustered routing problem that naturally mode"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25531v1 Announce Type: new Abstract: This paper studies quantum optimization baselines for the Generalized Traveling Salesman Problem (GTSP), a clustered routing problem that naturally models variant selection and sequencing problems under discrete alternatives. We propose a novel GTSP QUBO formulation focused on maintaining feasible solutions for quantum annealing, as well as a hardware-executable gate-based pipeline utilizing the Quantum Approximate Optimization Algorithm (QAOA). We implement a constrained QAOA variant using an XY-mixer, which preserves the stepwise Hamming weight in the ideal circuit model, while feasibility with respect to the full GTSP constraints is tracked explicitly during post-processing. We compare the two quantum optimization paradigms on problem instances from GTSPLIB, an established benchmark dataset, and validate against classical state-of-the-art solvers. To mitigate current quantum hardware size limitations, we further extend a preprocessing method to reduce the node count in instance clusters, constructing new NISQ-friendly instances from reduced subsets. Across all tested instances, quantum solvers often produce competitive solution quality when tested on smaller graphs, but exhibit higher runtimes and a sharp degradation in feasibility and scalability as instance size grows. Our evaluation highlights where quantum optimizers can already succeed and which algorithmic bottlenecks, like sampling rates, runtime issues, and other practical failure modes, remain as open problems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25531) | 2026-04-29
