---
title: "Well-conditioned iterative methods for large open quantum systems"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.30860"
summary: "arXiv:2608.30860v1 Announce Type: new Abstract: Markovian open quantum systems are well modeled by the Lindblad Master Equation (ME) frac{d}{d t} rho_t = L rho_t, where L is a linear (super-)operator "
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.30860v1 Announce Type: new Abstract: Markovian open quantum systems are well modeled by the Lindblad Master Equation (ME) frac{d}{d t} rho_t = L rho_t, where L is a linear (super-)operator and rho_t is the system state, a positive matrix. When designing or characterizing a quantum system, one is usually interested in the steady state rho_infty (such that L rho_infty = 0), the first few excited states, and trajectories tmapsto rho_t. In finite dimension, rho_t is an nimes n matrix, L thus typically costs n^4 to store explicitly as a dense matrix, and O(n^6) to diagonalize or invert exactly, making standard linear algebraic techniques expensive for large systems. However, L usually costs only O(n^3) to apply. This makes iterative methods appealing, but they do not work without a good preconditioner. In this article, our main observation is that a part of the Lindblad equation, corresponding to the so-called no-jump evolution S, can be inverted efficiently. Using this inverse map, we introduce an auxiliary completely positive trace-preserving (CPTP) map Phi whose fixed point is directly related to rho_infty, all the other eigenvalues having smaller magnitude. The map Phi is thus well suited to iterative methods, and rho_infty can be found in a few Arnoldi iterations. Using the same inverse map S^{-1} as preconditioner, we compute the low-lying spectrum efficiently via shift-invert Arnoldi, and, as a proof of concept, build an implicit time integrator that is competitive on stiff systems in the low-precision regime. For the steady-state and low excited states problems, our methods scale like O(n^3) per iteration and offer state-of-the-art performance on CPU and GPU.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.30860) | 2026-09-01
