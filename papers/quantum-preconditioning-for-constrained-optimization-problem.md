---
title: "Quantum Preconditioning For Constrained Optimization Problems"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.28842"
summary: "arXiv:2608.28842v1 Announce Type: new Abstract: We study the effect of quantum preconditioning on constrained combinatorial optimization problems, focusing on balanced graph bi-partitioning. The propo"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.28842v1 Announce Type: new Abstract: We study the effect of quantum preconditioning on constrained combinatorial optimization problems, focusing on balanced graph bi-partitioning. The proposed approach uses two-point correlations between decision variables derived from the Quantum Approximate Optimization Algorithm (QAOA) to construct a modified objective function that is subsequently provided to mixed-integer programming (MIP) solvers. The preconditioned MIP formulation retains the original hard constraint, and all incumbent solutions are evaluated under the original objective. Computational experiments on dense, weighted complete-graph instances show that the preconditioned problem instances reach near-optimal solutions faster, with most of the benefit already realized at the shallowest QAOA depth tested. Solver callback trajectories show this arises from earlier discovery of high-quality incumbents during the solution search. These results support a hybrid optimization framework in which quantum algorithms provide problem-specific information to guide classical exact MIP solvers.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.28842) | 2026-09-01
