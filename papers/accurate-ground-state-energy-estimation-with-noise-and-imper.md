---
title: "Accurate ground state energy estimation with noise and imperfect state preparation"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.21873"
summary: "arXiv:2603.21873v2 Announce Type: replace Abstract: We introduce a classical estimator for the post-processing of quantum phase estimation (QPE) data when a single target phase is isolated within a kn"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2603.21873v2 Announce Type: replace Abstract: We introduce a classical estimator for the post-processing of quantum phase estimation (QPE) data when a single target phase is isolated within a known interval, as is typical of ground state energy estimation of gapped systems. Our estimator filters the QPE signal within this promise region and recovers the phase through a moment-projection routine, which is robust to both external spurious phases and experimental noise. In the noiseless case this achieves an exponential suppression of bias with respect to a naive mean estimator. In the presence of global depolarizing noise the bias is exponentially small in the circuit depth t, and the variance is O(t^{-2}F^{-2}) for circuit fidelity F. This improves by a factor of t^2 over a naive shifted-and-rescaled-mean approach. To mitigate realistic circuit-level noise, we combine our method with the explicit unbiasing scheme described in [Dutkiewicz et al., 2025]. This yields an overhead interpolating between the F^{-4} scaling typical of explicitly unbiased error mitigation and a reduced F^{-2} scaling when the noise samples fall outside the promise interval. We validate our estimators on a small-scale simulation of the Ising model, observing better-than-expected performance for a global depolarizing noise approximation. This robustness to both multiple eigenvalues and realistic noise makes limited-depth phase estimation practical for early fault tolerant quantum experiments.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.21873) | 2026-08-04
