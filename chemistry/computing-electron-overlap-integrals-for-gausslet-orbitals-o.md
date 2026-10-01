---
title: "Computing electron overlap integrals for Gausslet orbitals on cubic lattices"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.39176"
summary: "arXiv:2609.39176v1 Announce Type: cross Abstract: Gausslet orbitals on a cubic lattice, introduced in [Steven R. White, J. Chem. Phys. 147, 244102 (2017)], represent a localized, smooth, and systemati"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.39176v1 Announce Type: cross Abstract: Gausslet orbitals on a cubic lattice, introduced in [Steven R. White, J. Chem. Phys. 147, 244102 (2017)], represent a localized, smooth, and systematically refineable basis set featuring a "diagonal" approximability of the electron repulsion integral tensor. The present work develops efficient algorithms for evaluating overlap integrals required for electronic-structure simulations using these Gausslets, specifically the kinetic, nuclear, and electron repulsion integrals (both with and without the diagonal approximation). Computational efficiency improvements rest on the exploitation of translation, permutation, and octahedral symmetries, a reordering and precomputation of nested sums, as well as an early truncation of small coefficients. Our algorithms reduce the number of electron repulsion integrals on a 5 imes 5 imes 5 grid from 125^4 = 244140625 to 324275 due to symmetries, and achieve a wall-clock runtime for evaluating the remaining integrals with a truncation tolerance of 10^{-5} in under 2 seconds on a laptop computer. We apply the developed methodology to compute the ground state of the hydrogen atom and molecule as a demonstration.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.39176) | 2026-10-01
