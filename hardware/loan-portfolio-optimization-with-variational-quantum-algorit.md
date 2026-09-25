---
title: "Loan Portfolio Optimization with Variational Quantum Algorithms"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.30195"
summary: "arXiv:2609.30195v1 Announce Type: new Abstract: Loan portfolio optimization (LPO) seeks portfolios that minimize credit risk while satisfying practical selection constraints. Accounting for portfolio-"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.30195v1 Announce Type: new Abstract: Loan portfolio optimization (LPO) seeks portfolios that minimize credit risk while satisfying practical selection constraints. Accounting for portfolio-level risk requires modeling not only expected losses but also loss variability and borrower-default correlations, leading to a large-scale combinatorial optimization problem whose complexity grows rapidly with portfolio size. In this work, we formulate LPO as a Quadratic Constrained Binary Optimization (QCBO) problem that jointly captures expected and unexpected losses and transform the resulting formulation into a Quadratic Unconstrained Binary Optimization (QUBO) model suitable for variational quantum optimization. To address the limited qubit resources of current quantum hardware, we employ Pauli Correlation Encoding (PCE), which enables a large number of portfolio-selection variables to be represented using comparatively few qubits. The proposed framework is evaluated on a real-world microfinance dataset comprising 2012 borrowers. For problem instances with up to 1000 portfolio-selection variables, we benchmark classical simulations of a variational quantum algorithm (VQA) against Google OR-Tools under matched time budgets, obtaining feasible portfolios with an objective-value gap of about 40% across all sizes. We further implement the framework on superconducting quantum hardware for instances containing up to 1500 variables. Across these instances, the experimentally obtained objective values are within 10% of the corresponding simulation results. These findings demonstrate the feasibility of applying PCE-based variational quantum optimization to large-scale loan portfolio optimization under current quantum hardware limitations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.30195) | 2026-09-25
