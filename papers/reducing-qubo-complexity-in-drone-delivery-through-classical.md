---
title: "Reducing QUBO Complexity in Drone Delivery Through Classical Feasibility Preprocessing"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.21003"
summary: "arXiv:2610.21003v1 Announce Type: new Abstract: Drone-delivery planning combines routing decisions with operational constraints such as payload capacity and limited onboard energy, resulting in combin"
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

arXiv:2610.21003v1 Announce Type: new Abstract: Drone-delivery planning combines routing decisions with operational constraints such as payload capacity and limited onboard energy, resulting in combinatorial optimization problems that can become costly to encode directly in binary form. This work investigates a hybrid quantum--classical approach in which candidate drone missions are generated and evaluated classically before constructing a quadratic unconstrained binary optimization (QUBO) model for mission selection. Payload- and energy-infeasible missions are removed during preprocessing, while the reduced QUBO is solved using exact enumeration, simulated annealing (SA), and the Quantum Approximate Optimization Algorithm (QAOA), with mixed-integer linear programming (MILP) used as a classical reference. Experiments on controlled synthetic delivery instances evaluate solution quality, the effect of preprocessing, and computational scaling. Exact QUBO optimization reproduces the MILP optimum on the evaluated small instances, while SA achieves 100% feasibility with a median optimality gap of 0%. Combined payload-and-energy preprocessing reduces the mean number of QUBO variables by 29.60% and quadratic interactions by 49.20%, while reducing mean SA runtime by 31.26%. In contrast, the evaluated shallow statevector-based QAOA configuration achieves lower feasibility and is restricted to small QUBO instances. These results indicate that, in the considered setting, the main practical benefit of the hybrid architecture comes from classical feasibility preprocessing that reduces the binary search space before QUBO-based optimization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.21003) | 2026-10-16
