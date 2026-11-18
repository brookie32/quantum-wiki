---
title: "Symmetry-reduced k-point sampling and Wannier analysis with localized Gaussian orbitals"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.21801"
summary: "arXiv:2611.21801v1 Announce Type: new Abstract: Brillouin-zone sampling with localized orbitals requires consistent transformations between sparse real-space matrices and complex Bloch states. Symmetr"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2611.21801v1 Announce Type: new Abstract: Brillouin-zone sampling with localized orbitals requires consistent transformations between sparse real-space matrices and complex Bloch states. Symmetry reduces the number of reciprocal-space problems, but scalar integration weights alone cannot reconstruct the matrices and wavefunctions needed for densities and orbital analysis. We develop a unified formulation of these transformations for nonorthogonal Gaussian bases and describe its implementation in CP2K. Atom permutations, local orbital rotations, and lattice phases connect irreducible-point solutions to full symmetry orbits while preserving the overlap metric. Direct and fast lattice transforms couple this construction to self-consistent calculations, including complex orbital optimization and finite-temperature occupations. Gauge-consistent full-mesh orbitals and directed inter-point overlaps support Wannier90 export, Wannier construction, and Hamiltonian interpolation. In silicon and aluminium tests, symmetry reduces a 64-point mesh to four representatives while retaining cell energies or electronic free energies within 1.5imes10^{-12} hartree of the unreduced calculation. Hybrid exchange and many-body applications illustrate the additional role of auxiliary bases and transfer momenta. The resulting framework connects symmetry-reduced integration to gauge-consistent analysis of periodic electronic states within a localized-orbital representation.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.21801) | 2026-11-18
