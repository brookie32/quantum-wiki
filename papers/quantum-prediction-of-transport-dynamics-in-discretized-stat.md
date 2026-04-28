---
title: "Quantum Prediction of Transport Dynamics in Discretized State Spaces"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24161"
summary: "arXiv:2604.24161v1 Announce Type: new Abstract: We propose a gate-based quantum algorithm for the prediction step of Bayesian state estimation based on the Fokker-Planck equation on a discretized posi"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.24161v1 Announce Type: new Abstract: We propose a gate-based quantum algorithm for the prediction step of Bayesian state estimation based on the Fokker-Planck equation on a discretized position-velocity state space. The probability density is encoded in the amplitudes of a quantum state, enabling a compact representation of high-dimensional distributions. Exploiting the circulant structure of finite-difference operators, the evolution is realized in the spectral domain using quantum Fourier transforms and phase rotations. A key result is that the drift component can be implemented exactly in amplitude space, leading to an accurate reproduction of the classical transport dynamics. In contrast, the diffusion term does not admit a linear representation in amplitude space due to the nonlinear relation between probability density and wave function. To enable a quantum implementation, we introduce a unitary surrogate based on a Wick rotation, transforming diffusion into a dispersive phase evolution. This yields a fully unitary propagation that can be implemented efficiently on a gate-based quantum computer. The proposed method is evaluated numerically for different scenarios and shows strong agreement with the exact solution of the Fokker-Planck equation. The approach demonstrates the potential of quantum computing for Bayesian state estimation, as the representable state space grows exponentially with the number of qubits. This allows the efficient representation and propagation of probability densities that would otherwise require complex tensor decompositions on classical hardware, making the method a promising candidate for high-dimensional filtering problems.



## Related
- [[a-unified-quantum-computing-quantum-monte-carlo-framework-th|A unified quantum computing quantum Monte Carlo framework through structured state preparation]]
- [[constant-factor-analysis-of-optimal-quantum-linear-solvers-i|Constant Factor Analysis of Optimal Quantum Linear Solvers in Practice]]
- [[quantum-algorithm-for-solving-high-dimensional-linear-stocha|Quantum algorithm for solving high-dimensional linear stochastic differential equations via amplitude encoding of the noise term]]
- [[on-the-complexity-of-quantum-numerical-integration-an-angle-|On the complexity of quantum numerical integration: an angle-structure characterization]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24161) | 2026-04-28
