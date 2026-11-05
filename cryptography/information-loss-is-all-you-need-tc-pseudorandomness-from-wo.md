---
title: "Information Loss Is All You Need: TC⁰ Pseudorandomness from Worst-Case Lattices"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2752"
summary: "Pseudorandomness plays a central role in algorithms, complexity theory, and cryptography. We ask whether deterministic information loss alone can yield post-quantum pseudorandomness with TC^0 evaluati"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Pseudorandomness plays a central role in algorithms, complexity theory, and cryptography. We ask whether deterministic information loss alone can yield post-quantum pseudorandomness with TC^0 evaluation. Learning with errors (LWE) hides linear measurements with random noise. Learning with rounding (LWR) replaces noise with deterministic rounding, but a standard polynomial-modulus hardness reduction requires parameters tailored to a predetermined sample bound. Decisional Diffie–Hellman offers a noiseless algebraic route to pseudorandomness, but its standard instantiations are vulnerable to quantum algorithms. We show that deterministic rounding achieves this under quantum worst-case lattice hardness, with fixed polynomial parameters and no predetermined sample bound. We introduce the learning with algebraic rounding (LAR) assumption, which applies an explicit integer rounding map to blocks of secret-dependent linear measurements and encodes the result in a lattice quotient. For one fixed family with polynomially bounded modulus and dimensions, its deterministic labels on exactly uniform, secret-independent public matrices are computationally indistinguishable from independent uniform labels for every polynomial number of classical random examples. Our classical reduction from Gaussian LWE, combined with the quantum worst-case reduction to LWE, bases LAR on GapSVP and SIVP over general lattices at approximation factor widetilde{O}(q), where q is the modulus. To prove this, we develop a source-independent affine transport framework that may be of independent interest. Using public affine maps sampled independently of the hidden errors, it transports the Gaussian error law close to uniform on the rounding map’s zero-label fiber while preserving exactly uniform public matrices. For every fixed inverse-polynomial accuracy, we give a polynomial-time sampler for the same public parameter family. This yields the first post-quantum weak pseudorandom function with joint key-and-input evaluation in TC^0, secure against uniform quantum polynomial-time distinguishers given any polynomial number of classical uniform random examples. We also establish the hardness of learning polynomial-size two-hidden-layer ReLU networks from noiseless uniform random examples, even for quantum polynomial-time improper learners.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2752) | 2026-11-03
