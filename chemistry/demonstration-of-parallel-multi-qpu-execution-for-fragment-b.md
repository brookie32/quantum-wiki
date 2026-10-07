---
title: "Demonstration of Parallel Multi-QPU Execution for Fragment-Based Quantum Chemistry Using On-Premises Hardware"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.07702"
summary: "arXiv:2610.07702v1 Announce Type: new Abstract: Fragment molecular orbital (FMO) quantum chemistry offers a natural route to parallel quantum computing: large molecular calculations can be decomposed "
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2610.07702v1 Announce Type: new Abstract: Fragment molecular orbital (FMO) quantum chemistry offers a natural route to parallel quantum computing: large molecular calculations can be decomposed into smaller quantum subproblems that can, in principle, run concurrently. Their practical benefit on real quantum hardware, however, has remained unclear. We demonstrate parallel FMO calculations on three room-temperature diamond-based 'Quoll' quantum computers installed on-site at the Oak Ridge Leadership Computing Facility. Helium clusters (He_{n}, n=2,4,8,10,14) served as a testbed for total energy calculations using the Quantum Wave Function Sampler (QWFS), a selected configuration interaction (SCI) approach. We compare two execution modes: synchronous shot-parallel execution, in which quantum processors jointly sample QWFS circuits and combine their SPAM-corrected counts into a single probability distribution; and asynchronous fragment-parallel execution, in which processors independently evaluate FMO fragments using device-specific optimized circuits. Both modes increase quantum sampling throughput without systematic loss of accuracy. The three-QPU shot-parallel workflow reaches a parallel efficiency of 93.60%, while the fragment-parallel workflow achieves a measured efficiency of 75.01%, increasing to 95.17% when excluding the non-useful idle time associated with non-interruptible submitted jobs. In both cases, the assembled FMO-QWFS energies remain chemically accurate compared to the classical ideal. These results provide a proof-of-concept demonstration that parallel quantum execution can improve the practical throughput of quantum chemistry workflows on prototype hardware, motivating the development of future HPC environments with many fault-tolerant quantum processors operating as a distributed resource for molecular and materials simulation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.07702) | 2026-10-07
