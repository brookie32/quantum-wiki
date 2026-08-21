---
title: "Variational Quantum Linear Solver via Block Encoding for the Poisson Equation"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.19655"
summary: "arXiv:2608.19655v1 Announce Type: new Abstract: We present a variational quantum linear solver (VQLS) for the Poisson equation built on an exact block encoding of the discrete Laplacian, and demonstra"
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2608.19655v1 Announce Type: new Abstract: We present a variational quantum linear solver (VQLS) for the Poisson equation built on an exact block encoding of the discrete Laplacian, and demonstrate its performance on physically motivated benchmarks. Unlike LCU-based VQLS where the number of distinct circuits required per cost-function evaluation is O(L^2), where L is the number of terms in the LCU decomposition of the discrete Laplacian operator, this approach requires only a single circuit for cost evaluation. We further empirically demonstrate that the choice of classical optimizer materially affects where the variational optimization ceases to make progress. The solver is benchmarked on three problems: a Poisson equation with sinusoidal forcing and a steady-state heat conduction problem with a localized Gaussian source, both with Dirichlet boundaries, and the pressure-Poisson equation of a two-dimensional lid-driven cavity flow, in which the solver is invoked once per time step under Neumann boundary conditions.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.19655) | 2026-08-21
