---
title: "Interface Energy and Phase Transformations: A Comparative Analysis of Cahn-Hilliard and CALPHAD-based Models in Ternary Substitutional Alloys"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2411.16430"
summary: "arXiv:2411.16430v3 Announce Type: replace-cross Abstract: Diffusional phase transformations in alloys are modeled either by phase-field methods of Cahn-Hilliard type, in which a double-well free energ"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2411.16430v3 Announce Type: replace-cross Abstract: Diffusional phase transformations in alloys are modeled either by phase-field methods of Cahn-Hilliard type, in which a double-well free energy and a gradient term impose an interface energy, or by reactive diffusion models, in which the driving forces follow from the CALPHAD methodology, the convex hull of the molar free energy, and the interface carries no energy. Their numerical schemes are tied to their free energies: phase-field schemes break down when the interface energy is set to zero, and reactive diffusion codes rely on finite differences. We derive, from the thermodynamic extremal principle, a single finite element scheme that covers both limits: the stationarity of the Rayleighian functional (free energy rate plus one half of the dissipation, with mass conservation imposed by multipliers) with respect to the rates, fluxes and multipliers at a frozen state. Fluxes and chemical affinities are primary unknowns, so no derivative of the affinity is required. The time-discrete scheme is the corresponding incremental minimization; it conserves mass exactly and satisfies a discrete energy-dissipation inequality for every convex molar free energy, including the convex hull without regularization. We make explicit that this last case is a degenerate parabolic problem of Stefan type, whose degeneracy can be removed, without altering the free energy, only by a moving mesh; since our aim is the coupling to continuum mechanics and damage on a fixed mesh, we operate at the boundary of degeneracy and show that mass conservation, the energy balance and the second law remain intact there. Thermodynamic consistency is proved for multi-component systems, a scheme relating Onsager and diffusion coefficients is proposed, and the role of interface energy is studied in binary and ternary examples, the latter with vacancies as a non-conserved component.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2411.16430) | 2026-10-08
