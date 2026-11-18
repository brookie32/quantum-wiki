---
title: "Efficient targeting of arbitrary excited states with quantum inverse power iteration through filtering polynomials"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.28255"
summary: "arXiv:2606.28255v2 Announce Type: replace Abstract: In this work, we introduce a quantum inverse power iteration (QIPI) algorithm based on the quantum singular value transformation (QSVT) to target ar"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2606.28255v2 Announce Type: replace Abstract: In this work, we introduce a quantum inverse power iteration (QIPI) algorithm based on the quantum singular value transformation (QSVT) to target arbitrary excited states. Given an energy shift omega, QIPI prepares the target excited state by iteratively applying an approximation of the shifted inverse Hamiltonian (H-omega I)^{-1} to a trial state. Prior quantum inverse power approaches typically relied on Fourier decompositions of the inverse Hamiltonian, with numerical quadrature used to reconstruct the transformation, but such methods are highly sensitive to hyperparameter choices and have been observed to be numerically unstable, effectively restricting their use to ground-state preparation. To enable robust excited-state targeting, we investigate two alternative transformation techniques: a Chebyshev decomposition of the inverse (Cheb-inv) and an eigenstate filtering (EF) approach based on QSVT. We find that EF-based QIPI is substantially more robust than Cheb-inv and other decomposition-based approaches due to the symmetry of the applied filtering polynomial, avoiding divergence with respect to the choice of omega and efficiently suppressing off-target eigenstates even in closely spaced spectra. Numerical simulations for molecular Hamiltonians of H_2, LiH, and BeH_2 show improved convergence and enhanced access to higher excited states relative to other quantum power methods. Assuming standard oracle access to the Hamiltonian, we further provide logical resource estimates in fault-tolerant settings in terms of T gate counts, and conclude that QIPI can achieve high target state amplification with modest polynomial degrees, thereby making it a promising candidate for scalable excited-state preparation in fault-tolerant quantum chemistry applications.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.28255) | 2026-11-18
