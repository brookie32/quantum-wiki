---
title: "Quantum SEDONet: Spectrally-Embedded Quantum Deep Operator Networks for Partial Differential Equations"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.27626"
summary: "arXiv:2608.27626v1 Announce Type: new Abstract: Quantum DeepONet accelerates neural-operator inference by evaluating an orthogonally parameterized network on a quantum computer, reproducing in ideal s"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2608.27626v1 Announce Type: new Abstract: Quantum DeepONet accelerates neural-operator inference by evaluating an orthogonally parameterized network on a quantum computer, reproducing in ideal simulation the accuracy of its classical counterpart at asymptotically lower inference cost. Its trunk network, however, receives query coordinates with limited spectral structure, requiring the network to learn oscillatory features through its nonlinearities. We propose Quantum SEDONet (Spectral-Embedded Deep Operator Network), which assigns each trunk coordinate a spectral basis according to its boundary condition: Fourier features for periodic coordinates and Chebyshev features for bounded, non-periodic coordinates. The basis is selected per coordinate rather than per problem, allowing both representations within a single problem. Under unary amplitude encoding, the embedding incurs no additional qubits or circuit depth when its dimension remains within the network width, while increasing the parameter count by only a few percent. Across four benchmarks, Quantum SEDONet reduces the mean relative L2 error by 54.1% for the antiderivative, 49.6% for advection, 36.0% for Burgers, and 36.2% for a mixed-boundary channel Poisson problem. Quantum and classical evaluation paths agree to within 10^-8 throughout. The channel Poisson problem simultaneously uses Fourier features in the periodic direction and Chebyshev features in the bounded direction, demonstrating coordinate-wise boundary-matched spectral embedding without additional quantum-resource cost.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.27626) | 2026-08-31
