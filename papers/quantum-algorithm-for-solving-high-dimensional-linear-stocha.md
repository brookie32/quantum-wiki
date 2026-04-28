---
title: "Quantum algorithm for solving high-dimensional linear stochastic differential equations via amplitude encoding of the noise term"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24133"
summary: "arXiv:2604.24133v1 Announce Type: new Abstract: This work studies quantum algorithms to solve high-dimensional stochastic differential equations (SDEs) d mathbf{X}_t = A(t) mathbf{X}_t d t + B(t) d ma"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.24133v1 Announce Type: new Abstract: This work studies quantum algorithms to solve high-dimensional stochastic differential equations (SDEs) d mathbf{X}_t = A(t) mathbf{X}_t d t + B(t) d mathbf{W}_t. Aiming for a speed-up in the dimension N of mathbf{X}_t, we generate quantum states that encode mathbf{X}_t in the amplitudes, while most of the existing quantum methods for SDEs employ binary encoding. A key challenge is the amplitude encoding of the noise term, and we address this by utilizing the quantum circuit implementation of a pseudorandom number generator (PRNG). We propose two methods: the Dyson series-based method and the Euler-Maruyama (EM)-based method. In the former, we express the noise term via the Dyson series approximation of the time evolution operator, while in the latter, it is approximated using the EM time discretization. Both methods use the quantum linear systems solver to generate the amplitude-encoding state of mathbf{X}_t, making only {rm polylog}(N) queries to the PRNG circuit and the block-encodings of A and B. Additionally, going beyond state preparation, we present methods to estimate expectations of functions of mathbf{X}_t using the state.



## Related
- [[symplectic-perspective-to-quantum-computing-for-hamiltonian-|Symplectic perspective to quantum computing for Hamiltonian systems]]
- [[constant-factor-analysis-of-optimal-quantum-linear-solvers-i|Constant Factor Analysis of Optimal Quantum Linear Solvers in Practice]]
- [[on-the-complexity-of-quantum-numerical-integration-an-angle-|On the complexity of quantum numerical integration: an angle-structure characterization]]
- [[hermitian-matrix-function-synthesis-without-block-encoding|Hermitian Matrix Function Synthesis without Block-Encoding]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24133) | 2026-04-28
