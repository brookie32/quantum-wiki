---
title: "Gate-Efficient Implementation of the Query-Optimal Time-Dependent Hamiltonian Simulation"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.30629"
summary: "arXiv:2608.30629v1 Announce Type: new Abstract: The query-optimal algorithm of [CGWZ26] for general time-dependent Hamiltonian simulation uses $ q = Oleft( alpha T + frac{log(1/arepsilon)}{logleft(e +"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.30629v1 Announce Type: new Abstract: The query-optimal algorithm of [CGWZ26] for general time-dependent Hamiltonian simulation uses $ q = Oleft( alpha T + frac{log(1/arepsilon)}{logleft(e + log(1/arepsilon)/(alpha T) right)} right) queries to HAMmbox{-T} within arepsilon error for a Lipschitz-continuous time-dependent Hamiltonian H(t) on [0,T] satisfying leftlVert H(t)rightrVertleqalpha. However, its direct circuit implementation incurs a substantially larger gate overhead. In this note, we give an implementation of the same algorithm that retains its optimal query complexity and uses Oleft[ q left( a + logleft(1 + frac{T(alpha + eta T)}{arepsilon} right) right) right] one- and two-qubit gates, where a is the number of block-encoding ancilla qubits and eta is the Lipschitz constant of H$. The main ingredient is an exact dyadic factorization of the ordered update product in the underlying one-query transducer.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.30629) | 2026-09-01
