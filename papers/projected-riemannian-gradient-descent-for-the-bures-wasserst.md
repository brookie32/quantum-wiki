---
title: "Projected Riemannian Gradient Descent for the Bures-Wasserstein Barycenter: Dimension-Independent Linear Convergence at Unit Step Size"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.03762"
summary: "arXiv:2609.03762v1 Announce Type: cross Abstract: The computation of the Bures-Wasserstein (BW) barycenter of an ensemble of positive definite matrices arises throughout machine learning, optimal tran"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2609.03762v1 Announce Type: cross Abstract: The computation of the Bures-Wasserstein (BW) barycenter of an ensemble of positive definite matrices arises throughout machine learning, optimal transport, and quantum information. Riemannian gradient descent (RGD) at unit step size -- the fixed-point iteration used in practice -- converges rapidly, yet existing analyses present a dichotomy: unit-step guarantees carry worst-case exponential dependence on the dimension, while dimension-independent guarantees require small step sizes that forfeit the empirical speed. We resolve this dichotomy, not by improving the guarantees for unit-step RGD, but by proposing a Projected RGD algorithm that achieves dimension-independent linear convergence at unit step size. The achieved rate, (1 - kappa^{-3/2}), where kappa is the condition number of the ensemble, also polynomially improves on the best small-step guarantee (kappa^{3/2} versus kappa^{5/2} iteration complexity). The crux is a novel Projection Lemma: clipping the eigenvalues of a positive matrix to an interval [alpha, eta] is the closed-form, non-expansive (1-Lipschitz) BW-metric projection onto the set {S : alpha I leq S leq eta I} -- a statement which, unlike its known one-sided counterpart, does not follow from convexity. The projection is moreover free: it reuses an eigendecomposition the next iteration must perform in any case, so the projected and unprojected iterations cost the same per step. The same analysis covers the invariant matrix projection problem of Brahmachari et al. (2025), whose fixed-point algorithm we identify as unit-step RGD on a totally geodesic submanifold, thereby extending the dimension-independent guarantee to that setting verbatim.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.03762) | 2026-09-04
