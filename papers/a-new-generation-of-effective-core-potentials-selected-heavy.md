---
title: "A new generation of effective core potentials: Selected heavy 5d and 6p elements"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.10853"
summary: "arXiv:2609.10853v1 Announce Type: cross Abstract: We expand the correlation-consistent effective core potentials (ccECPs) library by developing semi-local pseudopotentials and matching basis sets by h"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2609.10853v1 Announce Type: cross Abstract: We expand the correlation-consistent effective core potentials (ccECPs) library by developing semi-local pseudopotentials and matching basis sets by heavy-elements from 5d (Hf, Os, Hg) and 6p (Tl, Po, At, Rn) blocks. In order to accurately capture scalar relativistic effects, spin-orbit coupling, and electron-electron correlation, we implement a tiered core-valence partitioning strategy across three distinct resolutions. This includes a small 60-core (Hf, Os, Hg) that explicitly correlates subvalence shells, a large 78-core definition for the main-group elements that rigorously accounts for core polarization and relaxation effects in sparse valence environments, and an intermediate 68-core partition for Hg and Tl. This 68-core architecture represents a unique development in the ccECP library, optimizing the balance between accuracy and computational efficiency in a manner unexplored for ligther elements. Optimized against relativistic all-electron CCSD(T) references, the ccECPs deliver outstanding atomic precision, achieving a global average atomic low-lying states deviation of just 0.045 eV. This accuracy translates directly to robust molecular transferability, systematically restricting dissociation energy discrepancies to under 0.03 eV, equilibrium bond lengths to within 0.005 {AA}. By enforcing a regularized, finite potential at the origin for enhanced numerical stability in stochastic quantum Monte Carlo methods, this library removes a critical methodological bottleneck for predictive many-body simulations of heavy-element systems and materials.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.10853) | 2026-09-11
