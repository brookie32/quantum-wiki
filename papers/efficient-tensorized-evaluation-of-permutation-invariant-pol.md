---
title: "Efficient tensorized evaluation of permutation invariant polynomials for representing potential energy surfaces"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.19584"
summary: "arXiv:2609.19584v1 Announce Type: new Abstract: Permutation invariant polynomials (PIPs), together with related polynomial-based invariant descriptors such as fundamental invariants (FIs), are widely "
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2609.19584v1 Announce Type: new Abstract: Permutation invariant polynomials (PIPs), together with related polynomial-based invariant descriptors such as fundamental invariants (FIs), are widely used in constructing high-fidelity global potential energy surfaces (PESs) of molecules that contain identical atoms. Although the monomial symmetrization approach (MSA) enables fast evaluation of PIPs through recursive factorization, it leads to deeply nested computational graphs that may require large memory and are inefficient in modern automatic differentiation frameworks. In this work, we introduce JaxPIP, a JAX-based implementation that reformulates PIP/FI evaluation into tensorized linear algebra operations. By replacing recursive factorization with dense matrix operations combined with log-exp transformation and segmented summation, the evaluation becomes regular and GPU-friendly. This allows efficient execution with just-in-time compilation and enables large-scale batch evaluation of energies and forces (as well as higher-order derivatives). The resulting architecture supports ensemble simulations such as quasi-classical trajectory (QCT), path-integral molecular dynamics (PIMD), and diffusion Monte Carlo (DMC) in a fully vectorized manner. As demonstrated in examples, JaxPIP provides a practical route for efficient simulations of molecular systems with scalable GPU execution.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.19584) | 2026-09-18
