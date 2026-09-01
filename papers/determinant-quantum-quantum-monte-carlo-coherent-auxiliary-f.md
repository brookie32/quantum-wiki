---
title: "Determinant Quantum-Quantum Monte Carlo: Coherent Auxiliary-Field Sampling"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.28742"
summary: "arXiv:2608.28742v1 Announce Type: cross Abstract: We introduce determinant quantum-quantum Monte Carlo (DQ^2MC), a quantum algorithm that lifts the auxiliary-field sampling and averaging at the operat"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.28742v1 Announce Type: cross Abstract: We introduce determinant quantum-quantum Monte Carlo (DQ^2MC), a quantum algorithm that lifts the auxiliary-field sampling and averaging at the operational core of determinant quantum Monte Carlo onto a quantum computer. A determinant oracle synthesizes the DQMC amplitudes directly from a block encoding of the single-particle action matrix via quantum singular value transformations, so that the exponentially many Hubbard-Stratonovich weights are never enumerated, precomputed, or stored. Since the fermions are free for fixed auxiliary fields, the construction operates entirely at the single-particle level, requiring O(log N_{st}) system qubits and no Jordan-Wigner or Bravyi-Kitaev encoding, where N_{st} is the space-time volume. A full-quantum protocol makes observables interference amplitudes, eliminating the Markov chain and its autocorrelation time altogether; a hybrid quantum-classical protocol retains a constant-size active block of qubits and replaces the Metropolis-Hastings acceptance step with an exact heat-bath draw, so that cluster updates of any size are rejection-free, and passes only classical information between updates, admitting parallel tempering and distributed execution across quantum processors. The circuit-depth scales more favorably with spatial volume than classical DQMC, at the price of a post-selection overhead determined exactly by the largest target probability --- polynomial for smooth distributions, exponential for sharply peaked ones. Finally, the reweighting estimator underlying the fermion sign problem maps exactly onto a quantum weak value, placing the exponential cost of sign-problematic DQMC in precise correspondence with the post-selection overhead of weak-value extraction.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.28742) | 2026-09-01
