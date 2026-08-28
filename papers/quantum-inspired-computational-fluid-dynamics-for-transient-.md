---
title: "Quantum-Inspired Computational Fluid Dynamics for Transient Turbulent Compressible Flows"
date: "2026-08-28"
updated: "2026-08-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.26995"
summary: "arXiv:2608.26995v1 Announce Type: cross Abstract: Quantum-inspired algorithms are an emerging class of algorithms for computational fluid dynamics (CFD) with potentially favourable scaling for large p"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

arXiv:2608.26995v1 Announce Type: cross Abstract: Quantum-inspired algorithms are an emerging class of algorithms for computational fluid dynamics (CFD) with potentially favourable scaling for large problems compared to classical methods. However, their applications have been limited to incompressible flows due to arithmetic limitations, which are addressed in this work. This work introduces the first complete quantum-inspired computational fluid dynamics (QICFD) solver for direct numerical simulation of the compressible Navier--Stokes equations, that is, all arithmetic operations are undertaken in the tensor train (TT) format. Importantly, new division and square-root algorithms using TTs enable the use of Sutherland's law for viscosity. The new QICFD solver is validated by comparison with the classical CFD solver HiPSTAR and by way of a challenging fluid-flow test case, the low resolution Taylor--Green Vortex (TGV) at Mach numbers of 0.8 and 0.1. The TGV test case is a transient turbulent case that is very sensitive to accumulating errors, yet our QICFD solver achieves excellent agreement with the classical CFD reference. This work demonstrates the correctness of the new TT division and square-root algorithms, and that QICFD is capable of compressible flow simulations. The new QICFD solver is also able to perform simultaneous simulations, running multiple TGV-like cases initialised differently in parallel with marginal (10-20%) extra cost. Finally, the demonstrated TGV test case reveals additional challenges of QICFD as well as highlight the need for future advances to make TT methods viable for industrially-relevant conditions.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.26995) | 2026-08-28
