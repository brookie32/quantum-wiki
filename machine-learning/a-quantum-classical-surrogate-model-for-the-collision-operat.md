---
title: "A Quantum-Classical Surrogate Model for the Collision Operator of the Lattice Boltzmann Method"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.31351"
summary: "arXiv:2606.31351v2 Announce Type: replace Abstract: We introduce a hybrid approach utilising a quantum machine learning surrogate model to approximate the non-linear collision dynamics of the LBM. It "
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2606.31351v2 Announce Type: replace Abstract: We introduce a hybrid approach utilising a quantum machine learning surrogate model to approximate the non-linear collision dynamics of the LBM. It offloads the non-unitary operations that challenge pure quantum solvers. The surrogate's expressivity relies on variational quantum circuits that implement partial Fourier series, while data re-uploading extends the representable frequency spectrum. Unlike previous approaches that use a fixed relaxation parameter, the relaxation step is embedded analytically in the circuit, allowing the learned equilibrium to be used for any relaxation parameter without retraining. We reassess standard VQC metrics, including expressibility, entanglement, and effective dimension, by relating them directly to task-specific surrogate performance and identifying the architectural parameters that determine approximation accuracy. The proposed surrogate is validated against the classical BGK collision operator using benchmark problems, including the Taylor-Green vortex for energy dissipation and the double shear layer for shear-driven instabilities and nonlinear flow evolution. Our results show that the surrogate closely reproduces the BGK reference on both benchmarks, using a single set of trained circuits across all relaxation parameters. These findings suggest that hybrid quantum-classical strategies offer a practical path toward realising the potential of quantum computing in fluid engineering.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.31351) | 2026-11-16
