---
title: "Quadratic unconstrained binary optimization benchmark problems from mixed Hamming packings"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.27637"
summary: "arXiv:2611.27637v1 Announce Type: new Abstract: Benchmarking exact solvers and noisy intermediate-scale quantum devices for quadratic unconstrained binary optimization (QUBO) requires small yet challe"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2611.27637v1 Announce Type: new Abstract: Benchmarking exact solvers and noisy intermediate-scale quantum devices for quadratic unconstrained binary optimization (QUBO) requires small yet challenging instances, preferably coming from actual applications. We propose such a benchmark set derived from mixed Hamming packing, a hard problem in coding theory. Starting from its mixed-integer linear programming formulation, we provide a generator for the equivalent QUBO models and study 133 instances whose optima are certified by that formulation. In the feature space of the MQLib library, we position a broad range of existing quantum-oriented benchmarks relative to the classical ones: they lie along a narrow, sparse border of the region covered by MQLib, whereas our instances form a coherent family in a region that both collections leave almost empty. Classical heuristics and a simulated bifurcation machine find the optimum of most instances quickly, in several cases sooner than an exact mixed-integer solver first encounters it, suggesting heuristic warm starts for exact solvers; for an exact QUBO solver, in turn, it appears challenging to prove optimality. In Ising form, the instances are densely connected antiferromagnets whose large local fields are almost exactly balanced by the couplings, so that the decision on each variable rests on a small remainder. This makes them hard to embed and to represent accurately on current quantum annealers, in line with our D-Wave experiments.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.27637) | 2026-11-23
