---
title: "Scalable Quantum Machine Learning: Trainability, Expressivity and Efficiency"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.24014"
summary: "arXiv:2607.24014v2 Announce Type: replace Abstract: Designing scalable parameterized quantum circuits for machine learning faces three obstacles: barren plateaus, the absence of guarantees that the le"
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2607.24014v2 Announce Type: replace Abstract: Designing scalable parameterized quantum circuits for machine learning faces three obstacles: barren plateaus, the absence of guarantees that the learned function class is classically hard, and prohibitive circuit evaluations per gradient step. We propose the unitary brick-wall: a k-particle fermionic architecture for nearest-neighbor hardware, combining Reconfigurable Beam Splitter gates with interleaved single-qubit phase gates and a non-Gaussian magic-state encoding, where k is a tunable dial trading classical simulation hardness against training cost. Trainable. The brick-wall has dynamical Lie algebra mathfrak{u}(n) and is surjective onto U(n) via Givens rotations, enabling Haar initialization. Two-body correlator readouts achieve gradient variance Theta(k^3/n^5), polynomial in n throughout n-2k=Omega(n). Expressive. Classical hardness is controlled by k: best-known classical sampling algorithms run in time 2^{Theta(k)}poly(n), worst-case #P-hardness holds from k=n^{epsilon}, and the average-case machinery of Fermion Sampling applies at k=Theta(n). At our operating point k=60, best-known classical simulation exceeds 10^{24} operations at every n. Efficient. A multi-layer parallel parameter-shift rule computes all O(n^2) gradients from 4kn circuit evaluations per gradient step, a factor n/k reduction over the 4n^2 evaluations of the standard rule, growing linearly with n at fixed k. The unitary butterfly variant targets all-to-all hardware, with depth 2log n and (3/2)nlog n parameters, similar hardness guarantees, and 4klog n evaluations per gradient step -- the same factor-n/k reduction. Its trainability holds at two levels: absence of exponential barren plateaus is unconditional, while the sharp Theta(k^3/n^5) rate holds under a two-particle approximate-2-design conjecture.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.24014) | 2026-08-21
