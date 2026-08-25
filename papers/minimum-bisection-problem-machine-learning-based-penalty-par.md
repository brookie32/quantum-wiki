---
title: "Minimum Bisection Problem: Machine Learning-Based Penalty Parameter Tuning for Optimization on Quantum Annealers"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.19005"
summary: "arXiv:2509.19005v2 Announce Type: replace Abstract: The Minimum Bisection Problem is a fundamental, computationally hard graph partitioning problem with applications in parallel computing, network des"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2509.19005v2 Announce Type: replace Abstract: The Minimum Bisection Problem is a fundamental, computationally hard graph partitioning problem with applications in parallel computing, network design, and large-scale data processing. When formulated as a Quadratic Unconstrained Binary Optimization problem for quantum annealing, solution quality depends critically on the penalty parameter that enforces balanced partitions. Selecting this parameter is problem-dependent and typically relies on manual tuning or heuristics. This paper proposes a machine learning-based approach for automatic penalty-parameter tuning developed specifically for the Minimum Bisection Problem. We first derive a graph-dependent initial penalty estimate and then use two Gradient Boosting Regressor models to predict the endpoints of an effective penalty-multiplier interval from the number of nodes, graph density, and the initial estimate. The final penalty is obtained from the predicted interval and used to construct the model solved by D-Wave's quantum annealing solvers. The models were calibrated on 607 Erdos-Renyi graphs, with Metis and Kernighan-Lin as classical references, and evaluated on 126 independently generated instances with up to 4000 nodes. Under the adopted experimental setup, the predicted penalties enabled the hybrid solver to return balanced partitions for all evaluation instances and lower cut values than Metis in every case.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.19005) | 2026-08-25
