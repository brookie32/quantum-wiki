---
title: "Second-Derivative-Corrected FANPT for Robust Continuation of Nonlinear Wavefunction Equations"
date: "2026-08-13"
updated: "2026-08-13"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.11421"
summary: "arXiv:2608.11421v1 Announce Type: new Abstract: We present a second-derivative-corrected extension of the Flexible Ansatz for N-body Perturbation Theory (FANPT) for solving nonlinear Flexible Ansatz f"
last_verified: "2026-08-13"
review_by: "2026-11-11"
stale: false
---

arXiv:2608.11421v1 Announce Type: new Abstract: We present a second-derivative-corrected extension of the Flexible Ansatz for N-body Perturbation Theory (FANPT) for solving nonlinear Flexible Ansatz for N-body Configuration Interaction (FANCI) wavefunction equations. The original quasilinear FANPT approximation neglects second- and higher-order derivatives of the determinant overlap with respect to wavefunction parameters. In this work, we retain the overlap Hessian and neglect only third- and higher-order parameter derivatives, thereby including the leading nonlinear response of the wavefunction ansatz while preserving the same response-matrix structure used in the original FANPT formulation. The resulting additional terms enter only through the constant vector of the response equations and are implemented for coupled-cluster wavefunctions in the FanPy/FANCI framework. The new approximation is tested on the Lithium Hydride molecule and the insertion of Beryllium into H_2 using seniority-restricted coupled-cluster wavefunctions in the STO-6G basis. The main advantage of the second-derivative correction is that it provides a better initial guess for solving the projected FANCI equations at the next point along the adiabatic connection. This improvement is diagnosed by comparing the FANPT-propagated parameters with the independently optimized FANCI parameters at the same value of lambda. For nonlinear coupled-cluster ansatzes, especially when larger lambda-steps are used, the corrected approximation reduces the same-lambda parameter deviations and suppresses large parameter-space excursions. These results show that the leading nonlinear overlap correction improves the reliability of FANPT as a continuation strategy for nonlinear wavefunction equations.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.11421) | 2026-08-13
