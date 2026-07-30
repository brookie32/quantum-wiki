---
title: "Calibrated Pressure-Observable Born and Hessian Actions for Quantum-Assisted Waveform Inversion"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.26880"
summary: "arXiv:2607.26880v1 Announce Type: new Abstract: We construct a pressure-consistent operator-and-readout interface for Born, adjoint, and Gauss--Newton actions in constant-density acoustic full-wavefor"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2607.26880v1 Announce Type: new Abstract: We construct a pressure-consistent operator-and-readout interface for Born, adjoint, and Gauss--Newton actions in constant-density acoustic full-waveform inversion (FWI) using Schrodingerised propagation. The energy variables pi=c^{-1}partial_t u and q=nabla u yield an auxiliary-space Hamiltonian, while physical pressure p=cpi depends explicitly on wavespeed. Its derivative D(cpi)[c_0](elta c)=c_0eltapi+elta c,pi_0 combines propagated wavefield sensitivity with a direct receiver-calibration term. Duhamel and receiver-row differentiation retain both contributions in the Born map, its adjoint, and the Gauss--Newton normal action. We prove a conditional consistency estimate with a periodic second-order finite-difference specialization and give a resource model for state preparation, normalization, quadrature, and selected-output measurement. A compiled nine-qubit instance realizes structured preparation, product-formula propagation, a derivative-LCU block, and calibrated pressure-overlap measurements. Bernoulli samples from ideal-circuit probabilities drive a four-parameter hybrid inversion. A two-qubit VQLS circuit represents the normalized update direction, while normal-system assembly, line search, and model refresh remain classical. Finite differences, tangent and reverse-adjoint recurrences, autodiff JVP/VJP evaluations, and explicit Jacobians verify the discrete Born, adjoint, and normal actions. Smooth periodic refinement confirms second-order convergence, whereas omitting receiver calibration leaves an order-one Born error and substantially changes the regularized Gauss--Newton direction. All ten predeclared finite-shot runs reduce the initial model error. These results specify the physical-pressure derivative and selected-output measurements needed to connect Schrodingerised propagation to a local FWI update.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.26880) | 2026-07-30
