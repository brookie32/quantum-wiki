---
title: "Partial-Moment PINNs for Caldeira--Leggett Parameter Learning in Quantum Brownian Motion"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.23093"
summary: "arXiv:2608.23093v1 Announce Type: new Abstract: We study parameter recovery in the Caldeira--Leggett (quantum Brownian) oscillator from partial moment traces. Our model is a moment-level PINN that pre"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2608.23093v1 Announce Type: new Abstract: We study parameter recovery in the Caldeira--Leggett (quantum Brownian) oscillator from partial moment traces. Our model is a moment-level PINN that predicts the five first/second moments and enforces the linear CL/HPZ ODEs by automatic differentiation. Physical structure is imposed through a PSD (Cholesky) covariance head, high-temperature CL assumptions with D_{xp}approx0, and fluctuation--dissipation ties between D_{pp} and gamma. On synthetic CL data with channels {mu_x,sigma_{xx},sigma_{xp}}, the constrained variant recovers (omega,gamma) accurately, stabilizes D_{pp}, and achieves low rollout error compared to finite differences and Kalman--EM (expectation--maximization) with exact Van Loan discretization. Fisher-style checks confirm that diffusion needs at least one variance observable, and sparse sigma_{pp} ``anchors'' restore conditioning. We also show that the same PINN can learn time-varying HPZ coefficients.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.23093) | 2026-08-25
