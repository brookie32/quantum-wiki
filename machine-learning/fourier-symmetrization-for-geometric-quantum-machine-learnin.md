---
title: "Fourier Symmetrization for Geometric Quantum Machine Learning"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.01874"
summary: "arXiv:2610.01874v1 Announce Type: new Abstract: Geometric quantum machine learning incorporates symmetry into quantum models, but how symmetry shapes their expressivity and guides effective model desi"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01874v1 Announce Type: new Abstract: Geometric quantum machine learning incorporates symmetry into quantum models, but how symmetry shapes their expressivity and guides effective model design remains insufficiently understood. We address this question through the Fourier representation of quantum Fourier models (QFMs). Symmetry organizes the frequency spectrum into orbits and sums the Fourier coefficients within each orbit into a symmetrized coefficient. When QFM trainable layers form independent exact 2-designs, the variance of each symmetrized coefficient equals the sum of the coefficient variances in its orbit. For single-layer QFMs with arepsilon-approximate 2-design trainable layers, we bound the deviation from this identity. The resulting bound for individual Fourier coefficients can be exponentially tighter than an existing bound. The hyperoctahedral group provides an example of orbit growth that can mitigate vanishing expressivity of the symmetrized coefficients. Symmetrization of QFMs over an elementary abelian 2-group also yields pure multivariate Chebyshev polynomial basis functions. We introduce randomized encoding, which implements invariant models without ancilla qubits or the additional circuit depth for quantum twirling. We evaluate the models as quantum physics-informed neural networks (QPINNs) on two-dimensional screened Poisson and stationary viscous Hamilton-Jacobi equations. Under hard boundary constraints, QPINNs using exact symmetrization and randomized encoding achieve the lowest mean errors in the two benchmarks, respectively.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.01874) | 2026-10-02
