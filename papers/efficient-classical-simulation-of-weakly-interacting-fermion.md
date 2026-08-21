---
title: "Efficient Classical Simulation of Weakly Interacting Fermion Dynamics"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.19448"
summary: "arXiv:2608.19448v1 Announce Type: new Abstract: We consider the task of simulating the real-time dynamics of weakly interacting fermionic systems. In particular, we focus on computing the expectation "
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2608.19448v1 Announce Type: new Abstract: We consider the task of simulating the real-time dynamics of weakly interacting fermionic systems. In particular, we focus on computing the expectation value of a local observable A at time t. By analyzing the convergence of the perturbative expansion in the interaction strength lambda for the Heisenberg-picture observable, we propose a polynomial-time algorithm for estimating this expectation value in the weakly interacting regime lambda |t|^{2D+1}=O(1), when the Hamiltonian is geometrically local on a D-dimensional lattice. Importantly, this condition is independent of the system size. If the goal is instead to approximate the time-evolved observable in normalized Frobenius norm, we extend the convergence regime to lambda |t|=O(1) with quasi-polynomial runtime. When the non-interacting part exhibits Anderson localization, our polynomial-time algorithm can be extended up to lambda |t|=O(1), modulo polylogarithmic factors. Our algorithm brings together ideas from continuous-time QMC, diagrammatic QMC, and Majorana Propagation, but with a new Heisenberg-picture operator-growth analysis that makes the sampling complexity rigorously controllable. This leads to provably efficient classical algorithms in regimes where the interaction is weak enough that the sampling variance remains bounded independently of system size. Together, these results identify broad regimes in which weak interactions, locality, and localization can be leveraged to make real-time fermionic dynamics classically tractable.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.19448) | 2026-08-21
