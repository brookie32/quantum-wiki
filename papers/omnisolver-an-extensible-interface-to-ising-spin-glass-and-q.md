---
title: "Omnisolver: An extensible interface to Ising spin-glass and QUBO solvers: adding a distributed GPU brute-force plugin"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.10542"
summary: "arXiv:2610.10542v1 Announce Type: cross Abstract: This software update extends Omnisolver with exttt{omnisolver-bruteforce}, a first-class plugin for exact exhaustive search of QUBO and Ising instance"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.10542v1 Announce Type: cross Abstract: This software update extends Omnisolver with exttt{omnisolver-bruteforce}, a first-class plugin for exact exhaustive search of QUBO and Ising instances on CUDA-enabled GPUs. The update contributes three components: packaging of the single-GPU brute-force kernel of [Computer Physics Communications 260, 107728, 2021] as a first-class Omnisolver plugin with a uniform Python and CLI interface, a Ray-based distributed framework that splits the search into 2^{k} fixed-variable subproblems and dispatches them across multiple GPUs and hosts, with a controller that gathers and merges partial results, and numerical stabilization of the fast exttt{float32} ground-state path through compensated incremental updates, periodic exact energy re-anchoring, and best-buffer refresh. Stabilization activates automatically for N geq 40 leaving the public sampler API is unchanged. On dense random Ising instances we measure exhaustive solve times up to N=60 on 8imes NVIDIA H100 (96 GB) GPUs, reaching approx!3.15 days at N=60 in close agreement with the empirical t_{N+1}=2,t_N doubling rule, with the distributed sampler reaching the full approx!8imes speedup over a single H100 from N!gtrsim!44 onwards. The plugin thereby serves as a practical ground-truth oracle for state-of-the-art classical heuristics such as the Simulated Bifurcation Machine.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.10542) | 2026-10-09
