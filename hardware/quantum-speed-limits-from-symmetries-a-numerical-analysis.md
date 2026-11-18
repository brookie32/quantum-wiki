---
title: "Quantum speed limits from symmetries: A numerical analysis"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.22630"
summary: "arXiv:2611.22630v1 Announce Type: new Abstract: Target-specific quantum speed limits (QSLs) bound the minimal time required to realize a given operation. Recent theoretical work derives these limits d"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2611.22630v1 Announce Type: new Abstract: Target-specific quantum speed limits (QSLs) bound the minimal time required to realize a given operation. Recent theoretical work derives these limits directly from the symmetries of the dynamical Lie algebra of the control system and a symmetry-restoring perturbation, bypassing the need to solve the equations of motion. In practice, however, identifying a suitable symmetry and a perturbation that restores it demands strong physical intuition and offers no guarantee of tightness. We show that, for any given symmetry, the minimal restoring perturbation is the solution of a convex semidefinite program, which can be solved to global optimality and thus yields the tightest achievable speed limit for that symmetry. This semidefinite program is one building block of our numerical method, alongside an explicit computation of the space of admissible symmetries and a search over this space. Since this search is non-convex, it is addressed with gradient-based optimization, black-box heuristics, or the injection of physically motivated candidate symmetries. We apply the method to three examples: a two-qubit CNOT gate, a SWAP on a spinless-particle chain, and a Dicke state preparation on a qubit ring. Our results improve on previously known symmetry-based bounds, most notably for the SWAP, where solving the semidefinite program for the known analytical symmetry tightens the bound by a factor of approximately 2.5. For the Dicke state preparation, however, the bounds decrease with system size, which we trace back to a symmetry-independent perturbation ceiling. This work provides a reproducible numerical procedure for constructing target-specific quantum speed limits directly from the system Hamiltonians and the target operation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.22630) | 2026-11-18
