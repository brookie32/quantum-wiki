---
title: "Linear combination of Schrodingerization for quantum linear systems with optimal matrix-query complexity"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.19676"
summary: "arXiv:2609.19676v1 Announce Type: new Abstract: Quantum linear systems algorithms (QLSAs) aim to solve linear systems Ab{x}=b{b} exponentially faster than classical methods under certain conditions. I"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2609.19676v1 Announce Type: new Abstract: Quantum linear systems algorithms (QLSAs) aim to solve linear systems Ab{x}=b{b} exponentially faster than classical methods under certain conditions. In this work, we develop quantum algorithms for solving linear algebraic equations from an ODE-based perspective. Inspired by the linear combination of Hamiltonian simulation (LCHS) representation in the Fourier approach ite{Childs2017QLSA}, we express the solution b{x} as a linear combination of solutions to a system of linear convection equations, which become Schrodinger-type equations with unitary evolutions in the Fourier domain. We refer to this representation as LC-Schrodingerization. Based on this result, we construct an LCHS-based quantum algorithm with two LCHS instances: one for time-marching and one for numerical integration. The key construction uses the derivative of a Gaussian-smoothed hat function and recovers the solution over a fixed auxiliary interval. This permits a truncation time independent of the target accuracy and avoids the loss in success probability from selecting a single grid point. Periodization and explicit Fourier coefficients provide the corresponding projection error bounds. Under the stated oracle assumptions and given a constant-factor estimate of the solution norm, direct simulation of the select operators and block preconditioning achieve the optimal matrix-query complexity O(kappa_Alogfrac1arepsilon) without using variable-time amplitude amplification (VTAA). The same upper bound holds for queries to the right-hand-side preparation oracle.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.19676) | 2026-09-18
