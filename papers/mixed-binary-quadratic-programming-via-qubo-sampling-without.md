---
title: "Mixed-Binary Quadratic Programming via QUBO Sampling without Continuous-Variable Binarization"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.21286"
summary: "arXiv:2607.21286v1 Announce Type: new Abstract: Quantum annealing and related combinatorial optimization methods typically accept quadratic unconstrained binary optimization (QUBO) problems as input, "
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.21286v1 Announce Type: new Abstract: Quantum annealing and related combinatorial optimization methods typically accept quadratic unconstrained binary optimization (QUBO) problems as input, whereas many practical models include constraints and continuous variables. Standard QUBO conversions discretize continuous variables, increasing the binary dimension and often making feasible low-energy states harder to sample. We develop a finite-temperature formulation for a separable class of mixed-binary quadratic programs (MBQPs) that avoids this discretization. At fixed Lagrange multipliers, the continuous sector is integrated out analytically and enters only the multiplier update, leaving a QUBO over the original binary variables. We evaluate the method on the continuous relaxation of the quadratic p-median problem. Compared with a penalty-based QUBO formulation, it generates feasible solutions more reliably. At an appropriate inverse temperature, its conditional relative error is comparable to that of local search for small instances and often lower for the larger tested instances. In the time-to-target experiment, it also reaches the target faster than a commercial mixed-integer optimization solver toward the upper end of the tested range.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.21286) | 2026-07-24
