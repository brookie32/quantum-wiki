---
title: "Resource-efficient formulations of the Knapsack problem for quantum computing"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.06797"
summary: "arXiv:2611.06797v1 Announce Type: new Abstract: Quantum computing has emerged as a new tool for solving combinatorial optimization problems. Quantum optimization approaches usually operate on the subc"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.06797v1 Announce Type: new Abstract: Quantum computing has emerged as a new tool for solving combinatorial optimization problems. Quantum optimization approaches usually operate on the subclass of Quadratic Unconstrained Binary Optimization (QUBO) problems. Many optimization problems can be reformulated in this form, though there are often multiple ways to do so. The choice of formulation can considerably affect the performance of QUBO solvers in practice. In this work, we study QUBO formulations of the Knapsack problem, a canonical example of a problem with inequality constraints. In the standard formulation these constraints are converted into penalty terms, which requires additional slack variables. Here, we investigate three more resource-efficient approaches for formulating the Knapsack as a QUBO. The first two modify the standard formulation, either by deriving a smaller penalty constant or by reducing the number of slack variables. The third approach is a wholly different method, which avoids the use of slack variables entirely. All three approaches increase the probability of finding the optimal solution, both in simulations of the linear ramp Quantum Approximate Optimization Algorithm (LR-QAOA) and on a D-Wave quantum annealer. The slackless method performs best, increasing success probabilities by several orders of magnitude even for relatively small problem sizes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.06797) | 2026-11-05
