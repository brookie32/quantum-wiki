---
title: "Quantum algorithm for differential equations via permutation matrix representation with application to the Burgers equation"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.19508"
summary: "arXiv:2608.19508v1 Announce Type: new Abstract: We develop a quantum algorithm for solving the dynamics of the nonlinear viscous Burgers equation. We apply the Carleman linearization procedure on the "
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2608.19508v1 Announce Type: new Abstract: We develop a quantum algorithm for solving the dynamics of the nonlinear viscous Burgers equation. We apply the Carleman linearization procedure on the spatially discretized equation, followed by a padding scheme that allows implementation on qubit registers. Existing Carleman-based quantum algorithms commonly formulate the lifted linear differential equation in an oracle model. Here we decompose the padded generator into diagonal masks and reversible arithmetic permutations using the Permutation Matrix Representation (PMR), which we show to be naturally compatible with the Linear Combination of Hamiltonian Simulations (LCHS) algorithm. Under the assumptions required by LCHS - most importantly positive semidefiniteness of the Hermitian part of the linear generator, possibly after a stabilizing shift - the algorithm prepares a normalized quantum state proportional to the solution of the truncated lifted system; the stabilizing shift introduces an exponential postselection overhead, which we quantify and mitigate through a rescaling scheme. We show that our algorithm scales with the off-diagonal norm of the Carleman generator instead of the matrix norm, which can be advantageous for other generators that are diagonally dominant. We also extend the PMR scheme to general fluid equations that may contain higher-order derivatives or nonlinear terms, or may involve multiple fluid variables or spatial dimensions. The construction illustrates how PMR can serve as a convenient Hamiltonian-simulation primitive for a broader class of LCU-based algorithms.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.19508) | 2026-08-21
