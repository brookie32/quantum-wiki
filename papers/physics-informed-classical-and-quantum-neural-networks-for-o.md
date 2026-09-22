---
title: "Physics-Informed Classical and Quantum Neural Networks for One-Dimensional Schrodinger Eigenvalue Problems"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.22189"
summary: "arXiv:2609.22189v1 Announce Type: new Abstract: The Schrodinger equation in one spatial dimension admits a small set of exactly solvable potentials that serve as natural proving grounds for any new ei"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.22189v1 Announce Type: new Abstract: The Schrodinger equation in one spatial dimension admits a small set of exactly solvable potentials that serve as natural proving grounds for any new eigenvalue solver. We formulate Physics-Informed Neural Networks (PINNs) and Physics-Informed Quantum Neural Networks (PIQNNs) for the time-independent Schrodinger equation and apply them to three of these benchmarks: the harmonic oscillator, the infinite square well, and the finite square well. In each case a composite loss encodes the differential-equation residual, the normalization condition, the boundary behavior, and the orthogonality between eigenstates, so that the trial wave function is driven toward a genuine eigenfunction without supervised data. The eigenvalues and wave functions returned by both methods are compared against the exact spectra and against three classical references: the matrix Numerov method, the finite difference method, and the shooting method. For the smooth oscillator the two neural solvers reproduce the lowest four eigenvalues to parts per million, while for the square wells they recover the analytic levels with comparable fidelity even where the potential is discontinuous. The quantum circuit, built as a layered angle-embedding ansatz with strongly entangling blocks, converges more reliably than its classical counterpart on the higher excited states, where the loss landscape of the classical network becomes harder to navigate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.22189) | 2026-09-22
