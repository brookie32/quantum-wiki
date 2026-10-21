---
title: "Quantum algorithm for high-dimensional nonlinear stochastic differential equations based on Carleman linearization"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.27416"
summary: "arXiv:2610.27416v1 Announce Type: new Abstract: Addressing nonlinear numerical problems in quantum computing remains challenging, but several approaches, including Carleman linearization (CL), have be"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2610.27416v1 Announce Type: new Abstract: Addressing nonlinear numerical problems in quantum computing remains challenging, but several approaches, including Carleman linearization (CL), have been proposed to construct quantum algorithms for such problems. In this work, we develop a CL-based method for a high-dimensional nonlinear stochastic differential equation (SDE) d mathbf{X}_t = left(A(t) mathbf{X}_t + F(t) mathbf{X}_t^{otimes s}right) d t + B(t) d mathbf{W}_t for an R^N-valued random process mathbf{X}_t, aiming at quantum speed-up with respect to the dimension N. We introduce auxiliary processes mathbf{Y}^j_t that approximate mathbf{X}_t^{otimes j}, derive a linearized system of SDEs for them, and obtain the linear ordinary differential equation (ODE) governing their expectations. We then apply a quantum ODE solver to it and, from the resulting quantum state, extract an estimate for the expectation of a linear function of mathbf{X}_t by overlap estimation. We show that, provided the nonlinear and noise terms in the SDE are sufficiently small relative to the linear term, the CL error decreases exponentially with the truncation order J in CL, and we can estimate the target expectation with a {rm polylog}(N) number of queries to unitaries encoding coefficient matrices A, F, and B. Finally, we also run a numerical demonstration for an SDE related to Langevin dynamics, observing the exponential decay of the CL error as J increases.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.27416) | 2026-10-21
