---
title: "Analytic Gradients and Nonadiabatic Couplings for Device-Resident DMRG-QD-NEVPT2 Through Conical Intersections on a Consumer GPU"
date: "2026-09-10"
updated: "2026-09-10"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.09990"
summary: "arXiv:2609.09990v1 Announce Type: new Abstract: Nonadiabatic dynamics through a conical intersection needs both static and dynamic correlation and, at every geometry, an excited-state gradient and int"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

arXiv:2609.09990v1 Announce Type: new Abstract: Nonadiabatic dynamics through a conical intersection needs both static and dynamic correlation and, at every geometry, an excited-state gradient and interstate nonadiabatic coupling (NACME); analytic multireference derivatives at this level have been cluster-scale. We report device-resident mbox{DMRG-QD-NEVPT2} with analytic derivatives, on B2PLYP double-hybrid Kohn--Sham orbitals: a density-matrix-renormalization-group reference supplies the static correlation, and quasi-degenerate NEVPT2 adds the dynamic correlation through a multi-state effective Hamiltonian that stays valid through the intersection, where single-state perturbation theory fails. Each gradient and NACME is one reverse-mode transpose of a contraction graph that carries the DMRG sweep as a gauge-free, tape-free node and reduces to active-space RDM contractions with Cholesky factors. The whole construction runs on a consumer 8,GB GPU. The DMRG reference is FCI-in-active-space to 10^{-15} and the single-precision leg is spectroscopically inert (<10^{-6},eV); the correction yields smooth adiabats and a non-vanishing, 1/Delta E-divergent NACME through the twisted-ethene intersection---where adiabatic linear-response TDDFT returns zero---and restores the dynamic correlation the ionic pipi^* states require. DMRG-NEVPT2 and quasi-degenerate NEVPT2 are each established; the contribution is the entire stack---multi-state through a conical intersection, with analytic gradients and couplings---made device-resident on commodity hardware. Multireference companion to our density-functional realization of the same engine.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.09990) | 2026-09-10
