---
title: "Multivariate quantum signal processing with optimal query complexity"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03393"
summary: "arXiv:2610.03393v1 Announce Type: new Abstract: Polynomial transformations of data encoded in quantum operations are a building block of quantum algorithms, and their query complexity measures how oft"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03393v1 Announce Type: new Abstract: Polynomial transformations of data encoded in quantum operations are a building block of quantum algorithms, and their query complexity measures how often those operations are used. For multiple variables, existing methods either realize restricted polynomial families or implement monomials separately at a query cost exponential in the number of variables. We present a quantum circuit that implements every multivariate trigonometric polynomial up to an explicit normalization. The circuit processes one variable coherently over the frequency components of the remaining variables, allowing all components to share the same signal queries. Each variable is queried exactly as many times as its degree in the polynomial, and we prove that this query complexity is optimal. We further extend the construction to commuting unitaries. The resulting circuit applies the multivariate polynomial simultaneously across their shared eigenbasis, using the minimum numbers of forward and inverse queries to each unitary. We also study trainable rotations with fixed preparation and a local readout of the last input. At query depth at least two, independent uniform initialization gives every active readout gradient a variance lower bound set by its squared branch weight and the inverse square root of the depth, uniformly over data states and dimensions. For supervised squared loss, retaining sample correlations gives an initialization gradient-variance bound in terms of targets and input spectra. This also bounds the expected loss decrease after the first exact gradient step with a specified step size. These results provide a scalable and practical solution for developing multivariate quantum algorithms and quantum learning models.



## Related
- [[multivariate-quantum-signal-processing|Multivariate Quantum Signal Processing]]
- [[simulation-of-non-hermitian-hamiltonians-with-bivariate-quan|Simulation of Non-Hermitian Hamiltonians with Bivariate Quantum Signal Processing]]
- [[from-block-encoding-to-generalized-quantum-signal-processing|From Block-encoding to Generalized Quantum Signal Processing: Principles, Algorithms and Applications]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03393) | 2026-10-05
