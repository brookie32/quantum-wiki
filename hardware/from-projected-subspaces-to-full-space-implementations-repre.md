---
title: "From Projected Subspaces to Full-Space Implementations: Representation-Equivalence Audits for Open-Shell ADAPT-VQE"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.36060"
summary: "arXiv:2609.36060v1 Announce Type: new Abstract: A variational state optimized in a symmetry-projected space need not be the state prepared by exponentiating the corresponding unprojected parent genera"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.36060v1 Announce Type: new Abstract: A variational state optimized in a symmetry-projected space need not be the state prepared by exponentiating the corresponding unprojected parent generators. For an orthogonal target-space projector P, Q=I-P, and an anti-Hermitian generator A, exact equivalence for all amplitudes requires target-space invariance, QAP=0. We formulate this condition as a representation-equivalence audit for open-shell ADAPT-VQE. For a canonical CAS(15e,9o) type-1 Cu(II) Hamiltonian, 274 of 323 bare Hartree--Fock-origin single, double, and triple excitations violate this condition. Projected-doublet ADAPT reaches 1.5719 mE_h with 121 operators, whereas the same amplitudes in the corresponding full-space sequence give 464.730 mE_h error, 0.07343 fidelity with the projected state, and 54.45% quartet weight. Reoptimizing the same 121 parent generators in the same order under the hard constraint p_Dge0.999 reduces the best converged error to 8.482 mE_h, showing that the catastrophic same-angle failure is primarily a representation/parameter-transfer failure but is not completely repaired by full-space reoptimization of the fixed sequence. An independent 12-qubit NO benchmark exhibits the same mechanism more mildly. A spin-preserving generalized full-space construction removes the representation ambiguity and reaches 1.493 and 1.181 mE_h at 18 and 24 qubits. For the 18-qubit positive control, selectively refining only four Suzuki-2 factors and re-transpiling with a fixed compiler seed passes the predeclared circuit-equivalence gate at 19,660 controlled-X (CX) gates and depth 23,016. Circuit synthesis and final-energy measurement therefore constitute separate validation layers. The contribution is a validation framework, not a new spin-adapted ADAPT algorithm.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.36060) | 2026-09-30
