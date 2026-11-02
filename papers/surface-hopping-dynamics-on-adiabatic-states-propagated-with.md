---
title: "Surface Hopping Dynamics on Adiabatic States Propagated with Real-Time TDDFT"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.41686"
summary: "arXiv:2610.41686v1 Announce Type: new Abstract: Real-time time-dependent density functional theory (RT-TDDFT) is widely used to simulate ultrafast electron dynamics, but it is usually coupled to the n"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41686v1 Announce Type: new Abstract: Real-time time-dependent density functional theory (RT-TDDFT) is widely used to simulate ultrafast electron dynamics, but it is usually coupled to the nuclei through the mean-field Ehrenfest approximation, which cannot describe wavepacket branching and violates detailed balance. Surface hopping avoids these problems, but has not previously been combined with RT-TDDFT because real-time propagation does not directly provide the necessary adiabatic states. In this work we introduce an energy-scaled time-dependent Kohn--Sham (TDKS) propagation scheme, motivated by the quantum adiabatic theorem. Scaling widens the separation between electronic and nuclear timescales, so that each propagated state follows the adiabatic surface selected by its initial condition: either the ground state or a non-Aufbau self-consistent-field (DeltaSCF) solution. The propagation thereby avoids the convergence failures of static SCF solvers in regions of strong nonadiabatic coupling. Because the independently propagated states are complex-valued and not mutually orthogonal, we reformulate the mapping approach to surface hopping (MASH) in a complex adiabatic basis and introduce a dynamical transition orbital (DTO) gauge that restores a well-defined particle--hole representation for evaluating time-derivative couplings and nonadiabatic coupling vectors. Applied to the photoisomerization of extit{trans}-diimide, the scheme converges systematically as the scaling factor is increased and yields an excited-state lifetime in good agreement with previous nonadiabatic simulations based on static SCF.@ These results establish real-time propagation as an efficient and numerically stable route to the adiabatic states and couplings required for first-principles surface hopping.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.41686) | 2026-11-02
