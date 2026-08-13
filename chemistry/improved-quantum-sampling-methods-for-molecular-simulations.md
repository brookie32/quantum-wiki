---
title: "Improved quantum sampling methods for molecular simulations"
date: "2026-08-13"
updated: "2026-08-13"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.11569"
summary: "arXiv:2608.11569v1 Announce Type: new Abstract: Quantum-selected configuration interaction (QSCI) methods use a quantum computer to identify dominant electronic configurations in the molecular ground "
last_verified: "2026-08-13"
review_by: "2026-11-11"
stale: false
---

arXiv:2608.11569v1 Announce Type: new Abstract: Quantum-selected configuration interaction (QSCI) methods use a quantum computer to identify dominant electronic configurations in the molecular ground state, while a classical computer diagonalizes the Hamiltonian within the reduced subspace spanned by those configurations. Sample-based quantum diagonalization (SQD), a leading QSCI approach, uses iterative classical post-processing to correct noisy quantum measurement to ensure that the corresponding configurations remain physically sensible. In this work, we show that SQD performance can be strongly influenced by uncontrolled growth of the classical diagonalization subspace. When classical resources are not explicitly constrained, classical uniform random sampling can reproduce SQD benchmarks as noise increases the diversity of sampled configurations. We show any fair benchmarking protocol of SQD must explicitly control diagonalization size over unique samples. We then address the problem of efficiently discovering physically relevant, energy-lowering configurations by introducing a measurement protocol based on non-orthogonal configuration interaction (NOCI). By distributing measurements across orbital bases optimized with respect to the molecular Hamiltonian, we obtain improved sample efficiency relative to measurements performed solely in the Hartree--Fock basis. Importantly, these improvements persist even under fixed classical resource budgets, demonstrating that the resulting configurations are of higher quality rather than being more numerous. Under our proposed benchmarking procedure, we establish measurement-basis engineering as a promising route to improving quantum sampling methods for electronic structure.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.11569) | 2026-08-13
