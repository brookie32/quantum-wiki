---
title: "1d-qt-ideal-solver: 1D Idealized Quantum Tunneling Solver with Absorbing Boundaries"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.22634"
summary: "arXiv:2512.22634v2 Announce Type: replace Abstract: We present 1d-qt-ideal-solver, an open-source Python library for simulating one-dimensional quantum tunneling dynamics under idealized coherent cond"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2512.22634v2 Announce Type: replace Abstract: We present 1d-qt-ideal-solver, an open-source Python library for simulating one-dimensional quantum tunneling dynamics under idealized coherent conditions. The solver implements the split-operator method with second-order Trotter-Suzuki factorization, utilizing FFT-based spectral differentiation for the kinetic operator and complex absorbing potentials to eliminate boundary reflections. Numba just-in-time compilation achieves performance comparable to compiled languages while maintaining code accessibility. We validate the implementation through two canonical test cases: rectangular barriers modeling field emission through oxide layers and Gaussian barriers approximating scanning tunneling microscopy interactions. Both simulations achieve exceptional numerical fidelity with machine-precision energy conservation over femtosecond-scale propagation. Comparative analysis employing information-theoretic measures and nonparametric hypothesis tests reveals that rectangular barriers exhibit moderately higher transmission coefficients than Gaussian barriers in the over-barrier regime, though Jensen-Shannon divergence analysis indicates modest practical differences between geometries. Phase space analysis confirms complete decoherence when averaged over spatial-temporal domains. The library name reflects its scope: idealized signifies deliberate exclusion of dissipation, environmental coupling, and many-body interactions, limiting applicability to qualitative insights and pedagogical purposes rather than quantitative experimental predictions. Distributed under the MIT License, the library provides a deployable tool for teaching quantum mechanics and preliminary exploration of tunneling dynamics.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.22634) | 2026-08-19
