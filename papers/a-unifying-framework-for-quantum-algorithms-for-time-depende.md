---
title: "A unifying framework for quantum algorithms for time-dependent non-unitary dynamics"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.07133"
summary: "arXiv:2608.07133v1 Announce Type: new Abstract: Quantum algorithms for simulating linear differential equations have attracted growing interest, driven by applications ranging from Hamiltonian dynamic"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2608.07133v1 Announce Type: new Abstract: Quantum algorithms for simulating linear differential equations have attracted growing interest, driven by applications ranging from Hamiltonian dynamics to general non-unitary dynamics. While time-independent cases are well studied, time-dependent non-unitary dynamics remains considerably less explored, and it is unclear how to systematically adapt existing solvers for time-independent systems to such problems. In this work, we address this gap by introducing an autonomization framework based on the clock-variable formulation, a technique originally developed for time-dependent Hamiltonian systems in~ite{CJL23TimeSchr}. By lifting the original non-autonomous system to an autonomous transport-type equation on an extended space and applying the Fourier spectral discretization in the clock variable, we obtain an explicit time-independent linear system, together with a suitable initial state and a recovery map for the target solution. Crucially, this formulation decouples the treatment of time dependence from the choice of the quantum ODE solver, thereby enabling the direct application of existing solvers designed for time-independent systems to the resulting autonomous problem. We combine this framework with Schrodingerization and a Taylor-expansion-based quantum ODE solver. In the Schrodingerization-based combination, our complexity analysis shows that the precision dependence can scale as log^{5/4}(1/arepsilon), improving upon the log^2(1/arepsilon) scaling found in existing approaches. Numerical experiments validate the autonomization formulation and confirm the successful recovery of the target solution.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.07133) | 2026-08-10
