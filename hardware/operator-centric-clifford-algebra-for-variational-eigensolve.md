---
title: "Operator-centric Clifford algebra for variational eigensolvers and finite-shot adaptive selection"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.17443"
summary: "arXiv:2607.17443v2 Announce Type: replace Abstract: We develop a sparse operator-centric realization of n-qubit variational quantum algorithms in the complex Clifford algebra Cl(2n,C) ong M(2^n,C). De"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

arXiv:2607.17443v2 Announce Type: replace Abstract: We develop a sparse operator-centric realization of n-qubit variational quantum algorithms in the complex Clifford algebra Cl(2n,C) ong M(2^n,C). Density operators, gates, observables, channels, fermionic modes, and adaptive-selection observables are represented in one Pauli-word algebra, with the Jordan--Wigner map providing the exact bridge to anticommuting Clifford generators. We distinguish general Pauli-word rotations from Spin-group rotors and formulate the familiar odd-Y restriction for real-state adaptive ansatzes as an exact transpose-parity statement: for real Hamiltonians and real states, every candidate Pauli word containing an even number of Y factors has zero ADAPT gradient, while odd-Y rotations preserve the real sector. For the critical open transverse-field Ising chain, a depth-three Hamiltonian variational ansatz gives relative energy errors 4.84imes10^{-5}, 2.19imes10^{-3}, and 3.67imes10^{-3} for n=4,5,6. A compact local ADAPT pool is exact at n=4 but leaves residual errors at larger sizes; a systematic contiguous three-local odd-Y pool reaches relative errors below 1.3imes10^{-12} for nleq6. In 100-seed finite-shot tests at n=4, fixed-shot selection succeeds in 0/100 runs, whereas uniform escalation and confidence-bound racing each succeed in 84/100 runs; racing lowers median shots by 34%. We claim no asymptotic speedup over matrix methods. The contribution is a corrected algebraic formulation, a density-operator derivation and implementation of the real-sector pool filter, and a reproducible study of measurement-limited adaptive selection.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.17443) | 2026-08-03
