---
title: "Interpretable Activation-Selection Neural Networks for Symbolic Regression of Parameter-Dependent Hamiltonian Eigenvalues"
date: "2026-08-27"
updated: "2026-08-27"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.25475"
summary: "arXiv:2608.25475v1 Announce Type: new Abstract: Analytical approximations to eigenvalues of parameter-dependent Hamiltonians can provide physical insight that is not readily apparent from numerical di"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

arXiv:2608.25475v1 Announce Type: new Abstract: Analytical approximations to eigenvalues of parameter-dependent Hamiltonians can provide physical insight that is not readily apparent from numerical diagonalization alone. Here, we introduce an activation-selection network (ASN), a differentiable symbolic-regression architecture in which each input node learns a sparse combination of predefined analytical functions, and the trained network can be converted directly into an explicit expression. Before regression, the Hamiltonian parameters and eigenvalues are expressed as dimensionless ratios. This normalization enforces dimensional homogeneity, reduces the number of independent variables, and ensures that the extracted expressions do not depend on the choice of energy units. Using the library {0, x, x^2}, compositions across successive hidden layers generate polynomial expansions of progressively higher degree; polynomial expansions of arbitrary finite degree can therefore be obtained in principle by increasing the network depth. We apply the ASN to effective three- and four-site spin-chain Hamiltonians relevant to zero-quantum nuclear magnetic resonance. Comparisons with degenerate perturbation theory show that the extracted expressions capture the expected constant, linear, and quadratic structure. Fixed-basis least-squares models match or slightly outperform the ASN when an appropriate quadratic basis is specified in advance, while inclusion of a radial feature improves the local approximation near the degeneracy. These results establish the ASN as a differentiable framework for selecting compact symbolic representations when several functional forms are plausible, while showing that adaptive activation selection does not provide an intrinsic accuracy advantage over a suitable predefined basis.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.25475) | 2026-08-27
