---
title: "SSP-QST: Spectral Subspace Purification for Photonic Quantum State Tomography"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "sensing"
tags: [sensing, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.21836"
summary: "arXiv:2607.21836v1 Announce Type: new Abstract: Photonic quantum sensing often uses low-rank entangled probes such as Greenberger-Horne-Zeilinger (GHZ), Bell, and NOON states. Although these probes ar"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2607.21836v1 Announce Type: new Abstract: Photonic quantum sensing often uses low-rank entangled probes such as Greenberger-Horne-Zeilinger (GHZ), Bell, and NOON states. Although these probes are ideally rank-1, practical quantum state tomography (QST) can produce density-matrix estimates with many small finite-shot and noise-induced eigenmodes. This eigenvalue contamination can increase the estimated entropy of the reconstruction and reduce the quantum Fisher information (QFI) available for downstream sensing, while fixed rank-1 purification can discard valid signal modes when real probes acquire additional signal modes. We introduce Spectral Subspace Purification for Quantum State Tomography (SSP-QST), a rank-adaptive post-processing layer for least-squares quantum state tomography (LS-QST). SSP-QST eigendecomposes the least-squares estimate, computes a Weyl-motivated noise floor from the measured spectrum and shot count, removes eigenmodes below this floor, and renormalises the retained subspace. It requires no rank prior, no iterative optimisation, and only one eigendecomposition. In Qiskit Aer simulations, SSP-QST achieves the highest fidelity among the tested non-iterative baselines across the evaluated probe ranks, with a maximum fidelity gain of +0.584. It also improves shot efficiency by at least 8imes within the tested range. These results show that SSP-QST can make photonic QST more reliable under finite-shot noise while providing a lightweight reconstruction primitive for feedback-oriented quantum sensing pipelines.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.21836) | 2026-07-27
