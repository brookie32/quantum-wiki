---
title: "Restricting Trainable Lie-Algebra Growth in Equivariant Quantum Networks via Hierarchical Ancilla-Controlled Subspace Projections"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.30283"
summary: "arXiv:2609.30283v1 Announce Type: new Abstract: Equivariant quantum networks encode symmetry as an inductive bias, which can improve generalization and may also favor optimization convergence. Equivar"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2609.30283v1 Announce Type: new Abstract: Equivariant quantum networks encode symmetry as an inductive bias, which can improve generalization and may also favor optimization convergence. Equivariance alone, however, does not constrain the noncommuting closure of trainable generators, and this closure can still grow rapidly in symmetry-preserving variational circuits. We introduce a hierarchical ancilla-controlled architecture that addresses this Lie-algebra-growth mechanism. Commuting invariant-sector projectors on the data register select parameterized operations on a shared ancilla register, where the noncommuting trainable dynamics is confined. The trainable circuit decomposes into compatible joint sectors, giving a sector-probability-weighted ancilla response and an explicit view of parameter sharing across hierarchical paths. For an ancilla dimension d_A=2^m and K_ell retained layer-wise control modes, we prove the group-independent bound im(mathfrak g)le (d_A^2-1)prod_{ell=1}^{L}(K_ell+1). The bound is polynomial in the number of data qubits when m and K_ell remain constant along a logarithmic-depth hierarchy. Particle-number and parity projectors illustrate the general construction, while a fixed Clebsch--Gordan coupling tree supplies a concrete SU(2) realization with rotation-invariant scalar outputs. Finite-size state-vector simulations exhibit slower gradient-variance decay and larger initialization gradients than generic and conventional rotationally equivariant circuits over the studied system sizes. The same realization fits sparse rotation-invariant classification tasks and geometry-dependent Heisenberg ground-state energies. These results support restricted trainable Lie-algebra growth as a structural strategy for initialization trainability in the regimes considered here.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.30283) | 2026-09-28
