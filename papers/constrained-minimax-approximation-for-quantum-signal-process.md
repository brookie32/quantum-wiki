---
title: "Constrained minimax approximation for quantum signal processing"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.30937"
summary: "arXiv:2608.30937v1 Announce Type: new Abstract: Quantum signal processing (QSP) provides a simple and efficient framework for implementing polynomial transformations using quantum circuits. Its classi"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.30937v1 Announce Type: new Abstract: Quantum signal processing (QSP) provides a simple and efficient framework for implementing polynomial transformations using quantum circuits. Its classical design stage leads to a constrained minimax approximation problem: find a polynomial of prescribed parity that approximates a target function uniformly on a fitting set while remaining bounded in magnitude by one on the domain [0,1], which can be viewed as a semi-infinite constraint. Discretization converts the problem into a linear program, but feasibility at a set of finitely many sampled points does not ensure feasibility on the whole domain, especially when an optimal approximant reaches the boundary of the feasible set. We investigate two approaches to address this difficulty. A Remez exchange method combined with active-set constraint enforcement is efficient on many tested instances, but its stability depends on the target and problem geometry. We then introduce nonlinear Fourier retraction, which uses QSP completion and phase synthesis to turn a nearly feasible polynomial into phase factors for a feasible QSP polynomial without increasing the degree. Across representative problems, retraction largely preserves approximation accuracy and remains effective on instances where the Remez heuristic is unstable. The resulting workflow connects classical minimax approximation and semi-infinite optimization with nonlinear Fourier analysis, and is implemented in the qsppack software package.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.30937) | 2026-09-01
