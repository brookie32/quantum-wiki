---
title: "A hardware-efficient variational ansatz with an exact diagonal metric for real- and imaginary-time evolution and Haar sampling"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.07942"
summary: "arXiv:2607.07942v2 Announce Type: replace Abstract: Variational quantum algorithms depend on the geometry of their parametrised circuits: metric-aware optimisation and time evolution require the Fubin"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2607.07942v2 Announce Type: replace Abstract: Variational quantum algorithms depend on the geometry of their parametrised circuits: metric-aware optimisation and time evolution require the Fubini--Study metric, which has hitherto demanded costly auxiliary measurements and ill-conditioned inversions. This work introduces a hardware-efficient n-qubit ansatz, which parametrises states by a binary tree and whose Hilbert-space pullback metric is diagonal in closed form. Quantum natural gradient on the tree parameters, variational imaginary- and real-time evolution, and exact unitary-invariant (Haar) sampling on a symmetry sector run with no auxiliary metric circuits or matrix inversion. When the target state is supported on a subspace of k computational-basis states, the redundant tree parameters carry a gauge freedom a pruning compiler converts into circuits whose two-qubit count provably grows linearly in k; a variant reaches near-optimal O(nk/log n) scaling with the closed-form metric intact. On electronic-structure calculations for small molecules and half-filled Hubbard quench dynamics, the method reaches reference-level accuracy with one to three orders of magnitude fewer two-qubit gates than leading alternatives. Interchangeable constructions (a Schur-transform dressing or internal reparameterisations) make the ansatz exactly spin-adapted, with fixed total spin at every parameter and no penalty terms. The bare ansatz is an exactly controllable, well-conditioned and barren-plateau-free primitive for preparing and sampling sector states: on its own, it is classically simulable in k (a boundary proved for a general class of sector-sparse ansatze); composed with a classically hard dressing, it yields molecular ground states, sector-Haar benchmarking, thermal correlators, and exact effective Hamiltonians trained from energy measurements alone, with the composed circuit carrying the potential for quantum advantage.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.07942) | 2026-11-06
