---
title: "Scalable Determination of Penalization Weights for Constrained Optimizations on Approximate Solvers"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.02416"
summary: "arXiv:2604.02416v2 Announce Type: replace Abstract: Quadratic unconstrained binary optimization (QUBO) provides problem formulations for various computational problems that can be solved with dedicate"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2604.02416v2 Announce Type: replace Abstract: Quadratic unconstrained binary optimization (QUBO) provides problem formulations for various computational problems that can be solved with dedicated QUBO solvers, based on classical or quantum computation. A common approach to constrained combinatorial optimization problems is to enforce the constraints in the QUBO formulation by adding penalization terms. Penalization introduces an additional hyperparameter that significantly affects the solver's efficacy: the relative weight between the objective terms and the penalization terms. Here we study the problem of a priori determining suitable penalization weights from a foundational and practical perspective. We formally establish that finding its optimal value for Gibbs solvers is mathsf{NP}-hard even approximately and #mathsf{P}-hard exactly. This serves us as a motivation to develop a widely applicable heuristic strategy for determining suitable penalization weights, with provable guarantees for Gibbs solvers, and polynomial complexity for broad problem classes. Experiments across diverse problems and solver architectures, including large-scale instances on Fujitsu's Digital Annealer, show robust performance and order-of-magnitude speedups over existing heuristics. We further extend the strategy to quantum approximate optimization and demonstrate its performance on Quantinuum's H2-2 trapped-ion processor.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.02416) | 2026-10-21
