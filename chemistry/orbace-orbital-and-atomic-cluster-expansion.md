---
title: "OrbACE: Orbital and Atomic Cluster Expansion"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.33743"
summary: "arXiv:2611.33743v1 Announce Type: new Abstract: Accurate electronic-structure reference data are expensive, motivating interatomic potentials that learn effectively from limited training sets. We intr"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2611.33743v1 Announce Type: new Abstract: Accurate electronic-structure reference data are expensive, motivating interatomic potentials that learn effectively from limited training sets. We introduce OrbACE (Orbital and Atomic Cluster Expansion), a framework that supplements an E(3)-equivariant cluster-expansion backbone with inexpensive electronic-structure descriptors. On ANI-1x at the omegaB97X/6-31G* level, its atom-centered variant, OrbACE-A, trained on 10,000 configurations and evaluated on 442,000 held-out configurations, achieves energy and force mean absolute errors of 3.16 meV/atom and 76 meV/angstrom in direct learning, compared with 9.61 meV/atom and 146 meV/angstrom for MACE with matched backbone settings. This reduces the energy error by a factor of three and approximately halves the force error. Its energy error is also below that of the best delta-corrected MACE baseline, 5.00 meV/atom, although its force error is slightly higher. Combining OrbACE-A with a Hartree-Fock delta baseline further reduces the errors to 1.48 meV/atom and 35 meV/angstrom. OrbACE-A builds atom- and pair-resolved invariants from a non-self-consistent extended-Hueckel model evaluated within the differentiable forward pass, yielding forces consistent with the predicted energy. The orbital variant, OrbACE-O, instead uses localized Hartree-Fock orbitals as graph nodes, with scalar and equivariant electronic descriptors. Its forces are evaluated at fixed descriptors, omitting their response to nuclear motion. In direct learning on ANI-1x, its energy error is approximately three times that of OrbACE-A. The three benchmarks considered (ANI-1x, revised MD17, and 3BPA) cover neutral, closed-shell, non-periodic molecules containing H, C, N, and O. Performance outside this domain remains to be established.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.33743) | 2026-11-26
