---
title: "Molecular Implementation of the Machine-Learned Skala Exchange-Correlation Functional in CP2K through GauXC"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.19033"
summary: "arXiv:2608.19033v1 Announce Type: cross Abstract: Machine-learned exchange--correlation (XC) functionals offer a route to improve Kohn--Sham density-functional theory without incurring the cost of exp"
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2608.19033v1 Announce Type: cross Abstract: Machine-learned exchange--correlation (XC) functionals offer a route to improve Kohn--Sham density-functional theory without incurring the cost of explicitly correlated electronic-structure methods. Their use in production simulation codes, however, requires a well-defined mapping between the learned model and the host-code density representation. We formulate and implement a Skala-1.1 interface in CP2K through the external GauXC library. CP2K supplies the geometry, Gaussian basis, spin-resolved atomic-orbital density matrix, and communicator, while GauXC evaluates the XC energy, atomic-orbital potential matrix, and available nuclear derivatives. The interface accepts both all-electron and valence-only density matrices. The latter may arise from separable dual-space pseudopotentials or molecular effective-core potentials. Implementation errors are isolated from functional differences by comparing the Perdew--Burke--Ernzerhof (PBE) functional evaluated through GauXC with native CP2K PBE. The resulting interface gives consistent energies, forces validated against finite-difference total-energy checks, and force-based molecular-virial diagnostics for representative molecular cases. The dietGMTKN55 benchmark suite is evaluated with an all-electron Gaussian augmented plane-wave treatment for elements up to bromine and def2 effective-core potentials for the heavier elements. The resulting aggregate mean absolute deviation of 1.255 kcal/mol is within 0.020 kcal/mol of the corresponding Skala reference value of 1.235 kcal/mol. This work establishes a validated molecular implementation of Skala in CP2K through GauXC.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.19033) | 2026-08-20
