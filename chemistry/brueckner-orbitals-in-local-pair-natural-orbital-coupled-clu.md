---
title: "Brueckner Orbitals in Local Pair Natural Orbital Coupled-Cluster Theory: DLPNO-BCCD(T) and DLPNO-BCCD(T)_Lambda2"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.06600"
summary: "arXiv:2611.06600v1 Announce Type: new Abstract: In this work, we implement closed-shell Brueckner orbitals for the efficient domain-based local pair natural orbital DLPNO-CCSD(T) and DLPNO-CCSD(T)_{La"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.06600v1 Announce Type: new Abstract: In this work, we implement closed-shell Brueckner orbitals for the efficient domain-based local pair natural orbital DLPNO-CCSD(T) and DLPNO-CCSD(T)_{Lambda} methods of the free and open-source extsc{Psi4} package. We introduce a new algorithm that allows Brueckner orbitals to be computed within the DLPNO framework, resulting in the novel DLPNO-BCCD(T) and DLPNO-BCCD(T)_{Lambda_2} methods. We show that DLPNO-BCCD(T) approximates its canonical BCCD(T) counterpart with significantly lower errors relative to the errors incurred by DLPNO-CCSD(T) over CCSD(T). Through a test on the S22 set of noncovalent dimers, the peak error across the set is reduced from 0.36 kcal mol^{-1} to 0.25 kcal mol^{-1} using normal cutoffs, and 0.28 kcal mol^{-1} to 0.13 kcal mol^{-1} at tight cutoffs. In addition, we show that BCCD(T)_{Lambda_2}, a {Lambda_2}-only implementation of Brueckner orbitals for the asymmetric triples method, generally produces the best agreement with CCSDT, compared to the (T), (T)_{Lambda}, and B(T) perturbative triples corrections. This is established through benchmarks on thermochemistry tests on the barrier heights of semibullvalene and bullvalene Cope rearrangement, while the robustness of DLPNO-BCCD(T)_{Lambda_2} is demonstrated along bond-breaking potential energy curves, where it matches the orbital-optimized quasi-variational asymmetric renormalized-triples OQVCCDAR(T) method closely for single-bond breaking, and approximates DLPNO-CCSDT respectably even when triple bonds are stretched, at a fraction of the computational cost.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.06600) | 2026-11-05
