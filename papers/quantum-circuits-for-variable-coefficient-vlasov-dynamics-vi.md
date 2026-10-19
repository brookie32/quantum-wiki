---
title: "Quantum Circuits for Variable-Coefficient Vlasov Dynamics via Schrodingerisation"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.23405"
summary: "arXiv:2610.23405v1 Announce Type: new Abstract: High-dimensional Vlasov equations present promising use cases for quantum simulation, but their transport coefficients must be implemented coherently in"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2610.23405v1 Announce Type: new Abstract: High-dimensional Vlasov equations present promising use cases for quantum simulation, but their transport coefficients must be implemented coherently in order to preserve a compact quantum representation. We develop explicit Schrodingerised circuits for prescribed external field Vlasov dynamics without classical field updates. In 1D1V, velocity-dependent streaming is compiled directly from the encoded velocity register, while a non-linear cubic field is evaluated using reversible fixed-point arithmetic. For fixed polynomial degree, the field workspace scales linearly with the coordinate register width, while the field evaluation subroutine has polynomial depth. As a proof of concept, we simulate a minimal coupled 3D3V anharmonic Penning system and realise mixed electric-field terms and transverse magnetic coupling on a six-dimensional phase space in agreement with classical calculations. Resource analysis shows approximately linear growth with the number of time steps, while identifying the auxiliary register as the dominant depth bottleneck. Structured preparation and register recovery of the auxiliary state reveal an interplay between loading cost and readout. Together, our algorithm demonstrates a fully coherent quantum simulation of high-dimensional Vlasov dynamics with variable coefficients and identifies the practical resource costs that must be controlled for large-scale quantum implementation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.23405) | 2026-10-19
