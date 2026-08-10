---
title: "Density-Functional Excited-State Gradients and Nonadiabatic Couplings on a Consumer GPU from a Contraction-DAG"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.06536"
summary: "arXiv:2608.06536v1 Announce Type: new Abstract: Nonadiabatic dynamics needs an excited-state gradient and an interstate nonadiabatic coupling matrix element (NACME) at every nuclear geometry, and a do"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2608.06536v1 Announce Type: new Abstract: Nonadiabatic dynamics needs an excited-state gradient and an interstate nonadiabatic coupling matrix element (NACME) at every nuclear geometry, and a double-hybrid functional's accuracy has been unavailable for the coupling. We report the first analytic derivative NACME for a double-hybrid excited state---deferred in the original hh-TDA method and supplied for hybrids only by Yu et al.---derived, with the hole-hole and particle-particle Tamm--Dancoff (hhTDA/ppTDA) gradients and NACMEs, as a single reverse-mode transpose of one contraction graph closed under a non-symmetric atomic-orbital-direct J/K kernel. Its double-hybrid excitation energy lowers the vertical-excitation mean absolute deviation from bare-hhTDA 0.86 to 0.47~eV and removes the +0.53!rightarrow!+0.05~eV over-excitation bias, improving seven of ten states while over-correcting the ionic pipi^* states---the expected perturbative-doubles failure, reported not trimmed. Every coupling is validated to sim!10^{-4} against an independent literal many-electron wavefunction-overlap oracle that shares no code path with the method, and is physically meaningful at the ammonia n!rightarrow!sigma^* covalent conical intersection, where the hhTDA/ppTDA manifolds recover the F!-!2 seam and adiabatic linear-response TDDFT gives au!equiv!0 by construction. Gradients, NACMEs, and the double-hybrid coupling all run device-resident and AO-direct through one shared Cholesky-decomposed J/K engine within the 8,GB of a consumer RTX~4060 (a profile-guided sim!10^2imes launch collapse preserving double-precision bit-identity)---placing on a commodity desktop card a correlated excited-state derivative capability that has until now required datacenter hardware.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.06536) | 2026-08-10
