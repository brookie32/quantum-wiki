---
title: "Efficient quantum ultraspherical transform and a well-conditioned quantum spectral method"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.06651"
summary: "arXiv:2611.06651v1 Announce Type: new Abstract: Solving differential equations is a promising application of quantum computing. Spectral methods, where the solution is represented by coefficients in a"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.06651v1 Announce Type: new Abstract: Solving differential equations is a promising application of quantum computing. Spectral methods, where the solution is represented by coefficients in a basis, are particularly well suited to quantum solvers because their structured discretizations can enable efficient linear-algebra operations while providing rapid convergence. Their quantum implementation, however, requires an efficient transform between amplitudes encoding function values and amplitudes encoding expansion coefficients. This work develops two key components of a quantum spectral method. First, we construct the quantum ultraspherical transform (QUT) for orthonormal ultraspherical polynomials, a basis that supports sparse and well-conditioned discretizations of differential equations. For the basis parameters m=0 and 1, this transform reduces to the discrete cosine and sine transforms with known efficient circuits. Our contribution covers every fixed integer mgeq2: for dimensions N with N+m=2^n, where n is the number of qubits, the QUT achieves error at most arepsilon using a gate count polynomial in n and log(1/arepsilon). The construction builds on the quantum Fourier transform, augmented by approximations whose accuracy guarantees are independent of N. Second, we develop a quantum spectral solver for regular linear ordinary differential equations based on the QUT. Under suitable boundary conditions and data-access assumptions, preconditioning keeps condition numbers bounded independently of the basis size, allowing the solution state to be prepared at polylogarithmic cost in system size and inverse error. Together, these contributions provide a framework for quantum spectral methods with the potential to solve linear differential equations efficiently.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.06651) | 2026-11-05
