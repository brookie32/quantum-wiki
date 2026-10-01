---
title: "From Wavefunction Regularity to Eigenvector Conditioning: Accuracy--Cost Trade-offs of Quantum Algorithms for Non-Hermitian Transcorrelated Hamiltonians"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.39452"
summary: "arXiv:2609.39452v1 Announce Type: new Abstract: The electron--electron Coulomb singularity forces cusp structure in electronic wavefunctions. This cusp structure limits wavefunction regularity and slo"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.39452v1 Announce Type: new Abstract: The electron--electron Coulomb singularity forces cusp structure in electronic wavefunctions. This cusp structure limits wavefunction regularity and slows the convergence of expansions in smooth bases, requiring large basis sets to reach a target accuracy. The transcorrelated (TC) method incorporates this short-range behavior into the Hamiltonian, thereby improving the regularity of the transformed wavefunction and accelerating convergence toward the complete-basis-set limit. The resulting Hamiltonian is non-Hermitian and non-normal, which limits the direct applicability of standard quantum algorithms. For such non-normal operators, the complexity of several recent quantum algorithms depends explicitly on quantities related to eigenvector conditioning and eigenvalue sensitivity. Understanding these quantities is essential for assessing both algorithmic complexity and quantum resource requirements. In this work, we address these issues in two stages. We first study a solvable model, which provides a controlled setting for isolating how transcorrelation affects basis convergence and eigenvector conditioning. Within this setting, we investigate two distinct one-parameter Jastrow correlators. We derive the asymptotic energy-error scaling: N^{-1/2} for the bare projection and N^{-3/2} for both TC correlators at generic fixed parameters, with Ndenoting the basis size. Furthermore, we show that this faster convergence can yield a polynomial improvement in the asymptotic query-complexity upper bound. We then extend the analysis to second-quantized electronic-structure Hamiltonians and use particle-number-sector diagnostics to distinguish target-sector from auxiliary-sector conditioning. Our work provides a framework for understanding the central accuracy--cost trade-off in TC Hamiltonians.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.39452) | 2026-10-01
