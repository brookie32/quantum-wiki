---
title: "DA-CASE: reusable measurements for adaptive quantum subspaces"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.08739"
summary: "arXiv:2608.08739v1 Announce Type: new Abstract: Quantum subspace methods are often compared by basis dimension or energyerror, although their dominant experimental costs arise from different stateprep"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.08739v1 Announce Type: new Abstract: Quantum subspace methods are often compared by basis dimension or energyerror, although their dominant experimental costs arise from different statepreparations, measurement settings, and shot allocations. We present theDyadic Adaptive Clifford-Algebra Subspace Eigensolver (DA-CASE), whose basisstates are virtual directions A_i|psirangle generated from one reference.Overlap, Hamiltonian, and observable matrices are reconstructed from onecached set of Pauli expectations on that reference. The method thereforetrades multiple prepared basis states for a potentially wide measurement bank.We make that trade explicit on a frozen eight-qubit H_4 Hamiltonian. Twogenerator resolutions reach the same nine-dimensional subspace and the sameenergy to machine precision, while the retained bank changes from 7371 to 2240Pauli words. A reference-conditioned symmetry test certifies the narrower spanwithout asserting that its individual Pauli words conserve the sector asabstract operators. Independently, a dyadic commuting hierarchy reduces thedeterminant bank from 913 qubit-wise-commuting settings to 64 fully commutingsettings, while exposing the added logical-CX cost. In a separate four-qubitfinite-shot diagnostic, covariance-aware allocation reduces theprojected-matrix variance target by 68.9%. Mode-wise overlap regularizationremoves the observed catastrophic energy estimates and lowers RMSE, butdoubles the median error relative to a fixed cutoff. These are small-instanceexact and Monte Carlo results, not a hardware demonstration, scaling result,or quantum advantage claim. The contribution is a single-referencemeasurement architecture and a resource ledger that keeps contexts, settings,shots, circuit depth, and post-selection retries in their proper units.



## Related
- [[algebraic-paradoxes-in-adaptive-quantum-computation|Algebraic paradoxes in adaptive quantum computation]]
- [[quantum-advantage-with-adaptive-shallow-circuits|Quantum Advantage with Adaptive Shallow Circuits]]
- [[hamilton-zero-a-neural-tensor-network-foundation-model-for-g|Hamilton-Zero: A Neural Tensor-Network Foundation Model for Ground States of Arbitrary Quadratic Qubit Hamiltonians]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.08739) | 2026-08-11
