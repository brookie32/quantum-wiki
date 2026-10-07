---
title: "Exponential Reduction of Mesh Dependence in Quantum Estimation of Parabolic PDE Observables"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.18113"
summary: "arXiv:2607.18113v2 Announce Type: replace Abstract: Can a quantum PDE algorithm avoid the polynomial cost of resolving a fine spatial mesh? For standard fixed-order discretizations, direct classical m"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2607.18113v2 Announce Type: replace Abstract: Can a quantum PDE algorithm avoid the polynomial cost of resolving a fine spatial mesh? For standard fixed-order discretizations, direct classical methods require work polynomial in h^{-1}, or equivalently in the number of spatial degrees of freedom N_h=Theta(h^{-d}). Direct quantum implementations of a parabolic semigroup still have coherent complexity widetilde{mathcal O}(sqrt{T}/h), and gradient-dependent observables such as heat flux and dissipation introduce additional mesh dependence. Decay of the solution norm will further suppress the postselection probability for preparing a normalized final state. We develop a multilevel quantum algorithm that estimates linear and quadratic observables directly and places the fine--coarse cancellation inside the circuit before measurement. A contour-based LCU reconstructs each target-time correction from a coherent family of shifted resolvent differences. Rather than block encoding the fine and coarse inverses separately, we encode their difference through a shifted Ritz--Schur factorization, exposing its mathcal O(h_ell^2) two-grid normalization. For Fourier hierarchies, the corresponding SELECT oracle consists of a quantum Fourier or sine transform, a spectral-band selector, and reversible diagonal arithmetic. We also give a non-Fourier realization based on energy-orthogonal dyadic midpoint details in one dimension, together with structured tensor-product extensions under fixed-rank coefficient and access assumptions. For readouts with derivative order 0lehile2, optimized amplitude estimation removes all polynomial dependence on the finest mesh size. Under the stated access assumptions, both linear and quadratic observables can be estimated with complexity widetilde{mathcal O}(1+(Tepsilon)^{-1}), with only polylogarithmic dependence on h^{-1}.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.18113) | 2026-10-07
