---
title: "Q-SPARSE: Quantum Subspace Projection for Near-Field Angle-Range Spectrum Estimation"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.38500"
summary: "arXiv:2609.38500v1 Announce Type: new Abstract: Near-field wavefront curvature enables joint angle-range localization, but exploiting it entails repeated covariance-eigenspace tests over a two-dimensi"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.38500v1 Announce Type: new Abstract: Near-field wavefront curvature enables joint angle-range localization, but exploiting it entails repeated covariance-eigenspace tests over a two-dimensional spherical manifold. We propose a quantum subspace-projection algorithm (Q-SPARSE) for super-resolution estimation of parameters in the near field, employing spectral signature similar to MUSIC. Q-SPARSE prepares each spherical steering hypothesis as a quantum state, applies quantum phase estimation (QPE) to covariance-generated evolution, and converts the resolved spectral mass into a localization spectrum. The proposed method does not need the full classical preparation of the eigenstates, which is a major bottleneck of the QPE algorithm, the main subroutine in quantum variants of MUSIC algorithms. Under an ideal signal-noise partition, its score equals the classical signal-subspace overlap exactly and thus preserves the maximizer of normalized near-field MUSIC. For a finite q number of qubit phase registers, we derive the score from the complete QPE kernel, and propose a nearest-bin selection scheme with soft-thresholding based on Marchenko-Pastur-calibrated logistic weighting decision criteria. Numerical results on IBM's QISKIT software platform are demonstrated for near-field array processing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.38500) | 2026-10-01
