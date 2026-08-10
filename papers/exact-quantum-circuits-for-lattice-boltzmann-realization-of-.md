---
title: "Exact quantum circuits for lattice Boltzmann realization of the Dirac equation"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.06570"
summary: "arXiv:2608.06570v1 Announce Type: new Abstract: The quantum lattice Boltzmann (QLB) scheme of Succi and Dellar advances a four-component Dirac spinor on a lattice by a fixed sequence of local, exactly"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2608.06570v1 Announce Type: new Abstract: The quantum lattice Boltzmann (QLB) scheme of Succi and Dellar advances a four-component Dirac spinor on a lattice by a fixed sequence of local, exactly norm-preserving operations: a basis rotation, a collision, a streaming shift, and the inverse rotation. This unitarity is a structural property of the scheme, not an approximation, which suggests that a QLB time step should map onto a sequence of quantum gates. Here we make that mapping explicit. We give a gate-level construction of every operation of the three-dimensional Dirac QLB scheme: the fixed rotation gates, the collision gate, the streaming shift as a controlled increment on a position register, the position-dependent potential as a phase oracle, and periodic and reflecting (bounce-back) boundary conditions as unitary circuits. We then compose them into single-axis, two- and three-dimensional time steps. On a state-vector emulator the resulting circuits reproduce the classical QLB solver to machine precision (maximum density deviation between 3.7imes10^{-12} and 1.0imes10^{-17} across the one-, two-, and three-dimensional tests), so the circuits are the scheme rather than an approximation of it. The scope is narrow: we establish that the Succi-Dellar theory can be implemented on a (gate-model) quantum computer, and report the associated gate counts. We make no claim of computational advantage; state preparation, measurement, and asymptotic cost are discussed as open questions. All operators, circuits, tests, and figures are reproducible from the open-source quantumKineticMethods library.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.06570) | 2026-08-10
