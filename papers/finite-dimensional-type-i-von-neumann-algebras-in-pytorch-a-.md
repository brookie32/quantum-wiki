---
title: "Finite-Dimensional Type I von Neumann Algebras in PyTorch: A GPU-Accelerated Framework for Random Block-Diagonal Operators"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.15882"
summary: "arXiv:2606.15882v2 Announce Type: replace-cross Abstract: torch_vn_algebra is a PyTorch library for numerical work with finite-dimensional von Neumann algebras, i.e. direct sums of matrix algebras. Th"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2606.15882v2 Announce Type: replace-cross Abstract: torch_vn_algebra is a PyTorch library for numerical work with finite-dimensional von Neumann algebras, i.e. direct sums of matrix algebras. These algebras are central to operator algebra theory and, via commutants of symmetries, describe quantum systems with conserved charges or superselection rules. To our knowledge, no numerical software treats them as a data type with their centre, family of traces, conditional expectations, inclusions and functional calculus. The library fills the gap between computer algebra (exact but small-scale) and quantum simulators (large-scale but limited to Hilbert-space matrices): it handles batches of operators on CPUs and GPUs with automatic differentiation, and converts operators, states and channels. Key features: Compact tensor representation: 4D tensor (B, C, kmax, kmax), where B is batch size (e.g. Monte Carlo samples), C is the number of summands, and kmax is the max block size, enabling batched GPU processing. Lazy evaluation: matrix data materialized only on access, avoiding memory waste. Random operator generation: custom eigenvalue distributions; Haar, SU(n), COE, CSE unitary ensembles. Functional calculus and spectral methods: matrix absolute value, square root, inverse, entropy via SVD; automatic switch between exact diagonalization (block size up to 256) and power iteration for extreme eigenvalues. Three trace functionals: Tr_blunt (sum of block traces), Tr_norm (dimension-normalized), tau_vN (faithful normal tracial state). Performance: on a Tesla P100 GPU, processing 20,000 samples of 100x100 operators yields up to 30x speedup over traditional CPU workflows. Availability: open-source at https://gitlab.com/a.hobukob/von_neumann_type_i/

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.15882) | 2026-10-21
