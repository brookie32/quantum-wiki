---
title: "cuGUGA: Operator-Direct Graphical Unitary Group Approach Accelerated with CUDA"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2601.17729"
summary: "arXiv:2601.17729v2 Announce Type: replace Abstract: We present cuGUGA, an operator-direct graphical unitary group approach (GUGA) configuration interaction (CI) solver in a spin-adapted configuration "
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2601.17729v2 Announce Type: replace Abstract: We present cuGUGA, an operator-direct graphical unitary group approach (GUGA) configuration interaction (CI) solver in a spin-adapted configuration state function (CSF) basis. Dynamic-programming walk counts provide constant-time CSF ranking/unranking, and pretabulated segment factors enable constant-time evaluation of coupling coefficients. Two-electron contributions are organized through an intermediate-weight formulation that separates sparse generator enumeration from integral contraction and supports both dense and density-fitted/Cholesky backends. We further map the same primitives to GPUs by implementing the irregular DRT traversal and accumulation in custom CUDA kernels while delegating contractions to CUDA libraries. The implementation reproduces reference energies at the 10^{-11} Eh level and matches CPU/GPU sigma-vectors to 10^{-14}. On an RTX 4090, the GPU backend provides up to ~10x speedup over the CPU backend for smaller active spaces and multifold speedups on representative CASCI kernels. Speedup decreases as the active space grows because the workload becomes increasingly dominated by FP64 GEMM, which is not strongly accelerated on consumer GPUs. In addition, the cuGUGA CPU backend generally delivers >2x speedup over PySCF's determinant backend and >4x speedup over PySCF CSF backend.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2601.17729) | 2026-07-24
