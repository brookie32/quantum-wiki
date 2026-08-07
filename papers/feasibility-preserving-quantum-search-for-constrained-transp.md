---
title: "Feasibility-Preserving Quantum Search for Constrained Transportation Routing"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.05394"
summary: "arXiv:2608.05394v1 Announce Type: new Abstract: Transportation routing problems such as the Traveling Salesperson Problem (TSP) and the Vehicle Routing Problem (VRP) are characterized by strict feasib"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.05394v1 Announce Type: new Abstract: Transportation routing problems such as the Traveling Salesperson Problem (TSP) and the Vehicle Routing Problem (VRP) are characterized by strict feasibility requirements involving customer assignment and visit rules, route sequencing, and depot-return logic alongside cost minimization. Most quantum routing formulations adopt Quadratic Unconstrained Binary Optimization (QUBO) encodings, where feasibility is incorporated indirectly via penalty terms in the cost Hamiltonian. While convenient for standard implementations of the Quantum Approximate Optimization Algorithm (QAOA), QUBO encodings allow the quantum search dynamics to allocate substantial probability to infeasible route configurations. This study develops a transportation-grounded constraint-aware Quantum Alternating Operator Ansatz (QAOA+) framework that embeds feasibility-preserving logic directly into the search operator. We introduce a custom mixer that functions as a quantum analogue of feasibility-preserving routing neighborhoods, using column-wise swap moves, it restricts evolution to feasible configurations while enabling structured exploration of valid routes. We compare three constraint-handling architectures: penalty-based QUBO QAOA, penalty free QAOA+ with the feasibility-preserving mixer, and a Hybrid QAOA+ combining mixer based feasibility with and penalty guidance. Results on small TSP and VRP instances show that constraint-handling architecture strongly influences feasible-route sampling, convergence behavior, and probability concentration over low-cost feasible routes. These findings position constraint-aware quantum search as a methodological extension of transportation routing search approaches, where feasibility is enforced through admissible quantum transitions rather than post-hoc penalties.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.05394) | 2026-08-07
