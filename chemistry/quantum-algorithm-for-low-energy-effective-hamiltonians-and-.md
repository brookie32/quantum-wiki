---
title: "Quantum Algorithm for Low-Energy Effective Hamiltonians and Subspace Eigenvalue Problem"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2510.08088"
summary: "arXiv:2510.08088v3 Announce Type: replace Abstract: Subspace eigenvalue problems arise ubiquitously in quantum chemistry and condensed-matter physics, where the relevant object is often a low-energy m"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2510.08088v3 Announce Type: replace Abstract: Subspace eigenvalue problems arise ubiquitously in quantum chemistry and condensed-matter physics, where the relevant object is often a low-energy manifold rather than a single ground-state wavefunction. In this work, we propose a fault-tolerant quantum algorithm for this subspace-level task based on the Feshbach effective-Hamiltonian formalism. Given block-encoding access to the full Hamiltonian and a chosen d-dimensional reference subspace, the algorithm estimates eigenvalues of states with nonzero overlap with the reference subspace through a local secant fixed-point search. It then implements the associated wave operator and prepares an orthonormal basis whose span approximates the target invariant subspace. The construction combines projected block encodings with quantum singular value transformation (QSVT), which approximates the complementary-space resolvent and thereby provides both the self-energy used for eigenvalue estimation and the wave operator used for eigenstate reconstruction. For target accuracy arepsilon, a single evaluation of the effective Hamiltonian has query complexity widetilde{O}(d^3/(g^2arepsilon)), up to block-encoding normalization factors, where g is the distance between the target eigenvalue and the nearest pole of the effective Hamiltonian. Under the stated local regularity conditions, the secant search requires only O(loglog(1/arepsilon)) effective-Hamiltonian evaluations to reach the working precision. Classical numerical emulations for an open 4imes2 Fermi--Hubbard cluster, all-electron LiH bond stretching, and [Ru(bpy)_{3}]^{2+} demonstrate the resolution and reconstruction of low-energy states and manifolds across spin-sector crossings, near-degeneracies, and dense excited-state spectra.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2510.08088) | 2026-09-01
