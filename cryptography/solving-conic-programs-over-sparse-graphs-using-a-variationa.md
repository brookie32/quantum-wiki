---
title: "Solving Conic Programs over Sparse Graphs using a Variational Quantum Approach: The Case of the AC Optimal Power Flow"
date: "2026-09-17"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.00341"
summary: "arXiv:2509.00341v3 Announce Type: replace-cross Abstract: Conic programs arising in physics, quantum information, machine learning, and engineering are often defined over sparse graphs. Although such "
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

arXiv:2509.00341v3 Announce Type: replace-cross Abstract: Conic programs arising in physics, quantum information, machine learning, and engineering are often defined over sparse graphs. Although such problems can be solved in polynomial time using classical interior-point solvers, the computational complexity scales unfavorably with graph size. We propose a variational quantum paradigm for solving conic programs, including quadratically constrained quadratic programs and semidefinite programs. We encode primal variables via the state of a parameterized quantum circuit (PQC) and dual variables via the probability mass function associated with a second PQC. The Lagrangian function can thus be expressed as scaled expectations of quantum observables. We pursue approximately stationary points of the Lagrangian by minimizing/maximizing the Lagrangian over the parameters of the first/second PQC. This is accomplished in a hybrid fashion: gradients are estimated using the two PQCs, while their parameters are updated classically using a primal-dual method. We propose permuting primal variables so that related observables have a banded form, enabling efficient measurement. We provide a complexity analysis that is useful to determine which problem types may enjoy quantum advantage. The framework is applied to the AC OPF problem, a large-scale optimization problem central to electric power system operation. Numerical tests on the IEEE 57-node system using PennyLane's simulator show that the proposed doubly variational quantum framework can find high-quality OPF solutions. While this demonstration does not yield a quantum speedup, the results serve as a proof-of-concept and highlight challenges toward practical quantum advantage. Although showcased for OPF, the framework has broader scope, including conic programs with many variables and constraints, problems defined over sparse graphs, and training quantum machine learning models to satisfy constraints.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.00341) | 2026-09-17
