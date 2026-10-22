---
title: "Differentiated Determinant Graphs Enable Large-Scale Multideterminant Auxiliary-Field Quantum Monte Carlo"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.29851"
summary: "arXiv:2610.29851v1 Announce Type: new Abstract: Multideterminant trial wave functions can reduce phaseless bias in auxiliary-field quantum Monte Carlo (AFQMC), but the repeated evaluation of their ove"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

arXiv:2610.29851v1 Announce Type: new Abstract: Multideterminant trial wave functions can reduce phaseless bias in auxiliary-field quantum Monte Carlo (AFQMC), but the repeated evaluation of their overlap, force bias, and local energy restricts systematic trial improvement. In this work, we organize particle--hole excitation determinants as a shared arithmetic directed acyclic graph of canonical minors. A coefficient-weighted reverse pass and batched directional passes evaluate the complete estimator without determinant-resolved cofactor tensors while preserving the sparse alpha--eta coefficient coupling exactly. Controlled complex-valued tests verify the complete kernel to machine precision and show orders-of-magnitude acceleration over direct determinant summation. In molecular calculations, the observed cost remains sublinear through million-configuration selected-CI trials and the same estimator remains usable at one hundred million configurations, where the eventual exact coefficient-contraction boundary becomes visible. For Cr_2, an orbital-optimized CAS(12e,42o) trial in a double-zeta basis yields a potential-energy curve (PEC) and spectroscopic constants in close agreement with experiment. Differentiated determinant graphs therefore convert very large correlated trials from a formal accuracy hierarchy into a practical route for systematic AFQMC studies of strongly correlated molecules.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.29851) | 2026-10-22
