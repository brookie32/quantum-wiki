---
title: "Sample-Based Quantum Diagonalization with Amplitude Amplification"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.02565"
summary: "arXiv:2605.02565v2 Announce Type: replace Abstract: Recently, sample-based quantum diagonalization (SQD) has emerged as a promising approach to compute ground and excited states of problem Hamiltonian"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2605.02565v2 Announce Type: replace Abstract: Recently, sample-based quantum diagonalization (SQD) has emerged as a promising approach to compute ground and excited states of problem Hamiltonians. This method classically diagonalizes a Hamiltonian in a subspace that is spanned by samples obtained from a quantum computer. However, by its nature, SQD suffers from a fundamental sampling problem, as some basis states that are required for a targeted accuracy may only be sampled extremely rarely. To alleviate this limitation, we introduce the SQD-AA algorithm that combines SQD with amplitude amplification (AA). SQD-AA uses AA to sequentially reduce probabilities of already measured bitstrings, thus making the observation of new ones more likely. We observe a reduction in the total query complexity of more than a factor 100 for algebraically and exponentially decaying model distributions, and analytically show a quadratic advantage for the latter. Moreover, we evaluate real molecules in an early fault-tolerant scenario and compare SQD-AA to SQD and iterative quantum phase estimation (iQPE). For almost all considered examples, we observe the lowest total number of T-gates for SQD-AA while only requiring circuits that are 2-4 orders of magnitude shallower than those needed for iQPE. Given this substantial reduction in circuit depth compared to iQPE while saving 2 orders of magnitude in total runtime compared to SQD, we expect a significant regime in early fault-tolerance where SQD-AA runs feasibly, but iQPE circuits are too deep to execute confidently.



## Related
- [[machine-learned-compact-subspace-generation-for-quantum-sele|Machine-Learned Compact Subspace Generation for Quantum Selected Configuration Interaction within Density Matrix Embedding Framework]]
- [[spin-adapted-sample-based-quantum-diagonalization-with-rando|Spin-adapted sample-based quantum diagonalization with randomized time evolution]]
- [[quantum-centric-geometry-optimization-with-wave-function-bas|Quantum-Centric Geometry Optimization with Wave-Function-Based Embedding]]
- [[a-basis-aware-approach-to-quantum-sampling-of-the-fermi-hubb|A Basis-Aware Approach to Quantum Sampling of the Fermi-Hubbard Ladder]]
- [[a-scalable-sample-based-quantum-diagonalization-solver-for-g|A scalable sample-based quantum diagonalization solver for general Pauli-sum Hamiltonians]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.02565) | 2026-11-18
