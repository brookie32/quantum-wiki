---
title: "Qubit-Efficient Variational Quantum Optimization via Pauli Correlation Encoding: Application to Large-Scale Power Demand Portfolio Optimization"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.24722"
summary: "arXiv:2607.24722v2 Announce Type: replace Abstract: Variational quantum algorithms offer a promising route to combinatorial optimization, but their applicability is limited by the challenge of encodin"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2607.24722v2 Announce Type: replace Abstract: Variational quantum algorithms offer a promising route to combinatorial optimization, but their applicability is limited by the challenge of encoding large-scale problems within restricted qubit resources. In this work, we introduce a qubit-efficient variational framework based on Pauli correlation encoding (PCE) and apply it to electric power demand portfolio optimization. Binary variables are represented through expectation values of Pauli correlation operators, which encode multi-body correlations of the quantum state and provide a continuous relaxation enabling compact representations with few qubits. We further propose a two-stage hybrid formulation, in which a time-averaged problem provides initialization for a time-resolved optimization. Numerical simulations demonstrate near-optimal performance across problem sizes ranging from m=18 to 10{,}296, with normalized cost gaps on the order of 10^{-4} relative to solutions with certified optimality. We show that the performance is governed by the interplay between continuous relaxation and discretization: the effective resolution of the correlator representation determines how reliably improvements in the continuous loss translate into better discrete solutions, with larger systems exhibiting more consistent behavior. Finally, we demonstrate robustness on a trapped-ion quantum processor, where high-quality solutions are obtained despite noise and finite sampling. These results establish PCE as a physically motivated and qubit-efficient framework for large-scale combinatorial optimization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.24722) | 2026-09-15
