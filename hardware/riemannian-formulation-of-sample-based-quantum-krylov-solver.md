---
title: "Riemannian Formulation of Sample-Based Quantum Krylov Solvers for Elliptic Problems: Energy-Norm Guarantees and Duct-Flow Applications"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.15586"
summary: "arXiv:2610.15586v2 Announce Type: replace Abstract: Sample-based quantum linear solvers measure quantum Krylov states e^{-iAT}|brangle and reconstruct the solution of Ax=b classically on the observed "
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2610.15586v2 Announce Type: replace Abstract: Sample-based quantum linear solvers measure quantum Krylov states e^{-iAT}|brangle and reconstruct the solution of Ax=b classically on the observed basis states. We develop this approach for positive-definite systems that arise from elliptic partial differential equations. We show that the sampling guarantees hold in any fixed basis with an efficient transform. We then replace the variational reconstruction by a Galerkin solve on the sampled set. For this reconstruction we derive expected and high-probability energy-norm error bounds, a sample complexity in terms of the smallest sampling probability on an essential set, a computable residual certificate, and a support-completeness theorem for the dephased outcome law. We formulate the method for elliptic problems on Riemannian cross sections. In two dimensions the stiffness matrix is metric-independent in conformal coordinates, and curved vessels lead to the same matrix class. Killing symmetries of the cross section give selection rules for the measurement outcomes, and the Lie derivative of the metric gives first-order bounds for geometric perturbations. We separate operator approximations, whose effect we bound, from sampler approximations, which affect coverage but not the target. As examples we treat the implicit step of pulsatile flow in elliptic, lens-shaped, and curved ducts. In simulations of up to 12 qubits, the number of Fourier modes required for 1% error grows from 14 to 60 while the number of unknowns grows from 64 to 4096. A classical residual-greedy selection is nevertheless more efficient than quantum sampling in all cases studied, consistent with the low measured sampling efficiency. On a six-qubit trapped-ion processor, the measured outcome laws follow a replacement-noise model whose strength grows by about 0.6% per two-qubit gate, and a parity selection rule rejects shots at the predicted rate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.15586) | 2026-10-15
