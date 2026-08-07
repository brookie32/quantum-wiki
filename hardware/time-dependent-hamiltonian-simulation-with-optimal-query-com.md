---
title: "Time-Dependent Hamiltonian Simulation with Optimal Query Complexity"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.06094"
summary: "arXiv:2608.06094v1 Announce Type: new Abstract: We give a query-optimal algorithm for simulating a general n-qubit time-dependent Hamiltonian H(t) on [0,T], assuming that H is Lipschitz continuous and"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.06094v1 Announce Type: new Abstract: We give a query-optimal algorithm for simulating a general n-qubit time-dependent Hamiltonian H(t) on [0,T], assuming that H is Lipschitz continuous and |H(t)|leqalpha. In the standard HAMmbox{-T} access model, the algorithm approximates the time-ordered propagator U_H(T) to error arepsilon using $ Oleft( alpha T+frac{log(1/arepsilon)} {log(e+log(1/arepsilon)/(alpha T))} right) HAMmbox{-T} queries. This matches the known query lower bound for time-independent Hamiltonians, showing that time dependence incurs no asymptotic query overhead. Our method first constructs a one-query transducer that, given an auxiliary state, implements an approximation to U_H(T)$ and returns the state unchanged. A weighted combination of circuits that apply the transducer different numbers of times makes the error caused by omitting this state decay factorially, yielding the stated optimal precision dependence. For time-independent Hamiltonians, the same method also gives a query-optimal alternative to qubitization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.06094) | 2026-08-07
