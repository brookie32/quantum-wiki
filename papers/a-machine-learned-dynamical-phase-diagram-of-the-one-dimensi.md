---
title: "A machine-learned dynamical phase diagram of the one-dimensional nonlinear Schrodinger equation with quasiperiodic disorder and a static field"
date: "2026-09-10"
updated: "2026-09-10"
source: "agent"
category: "papers"
tags: [papers, arxiv-cond-mat-quant-gas]
url: "https://arxiv.org/abs/2609.10045"
summary: "arXiv:2609.10045v1 Announce Type: new Abstract: We map the transport regimes of a wave packet evolving under the one-dimensional discrete nonlinear Schrodinger (Gross-Pitaevskii) equation with a quasi"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

arXiv:2609.10045v1 Announce Type: new Abstract: We map the transport regimes of a wave packet evolving under the one-dimensional discrete nonlinear Schrodinger (Gross-Pitaevskii) equation with a quasiperiodic Aubry-Andre potential and a static (Stark) field, as a function of self-interaction g, field F, and quasiperiodic strength lambda, for two initial states (delta and Gaussian). Instead of one expensive long-time simulation per grid point, we run 3600 short simulations, reduce each to eight dynamical features, and cluster parameter space with a Gaussian mixture model. Clustering finds the boundaries between regimes unsupervised; each cluster's name is then assigned by a hand-calibrated rule, and an ablation shows clustering measurably smooths those boundaries rather than merely relabeling them. The five resulting regimes (ballistic, localized, oscillatory-localized, subdiffusive, and self-trapped) are validated against 100 long runs on a lattice eight times larger than the short sweep, so the validation window is longer than the training window even for the fastest-spreading regime. The short-time clusters predict the long-time asymptotic spreading exponent (alpha_infty = 2.01pm0.07 ballistic, 0.28pm0.16 subdiffusive, consistent with the weak-chaos prediction alpha=1/3) and, independently, a long-time retention Pi_0=0.72pm0.32 for the self-trapped cluster, whose exponent alone is not diagnostic. The initial-state contrast is striking: the delta state develops a broad self-trapping wedge (onset at g=3.907pm0.017 at lambda=0) that invades the ballistic and localized regions as g grows, while the Gaussian state shows no self-trapping, instead opening a subdiffusive corridor along the Aubry-Andre critical line that widens with g. The scheme yields a full 15imes15 phase map in minutes per slice, where direct asymptotic simulation (tgtrsim10^6 per point) is prohibitive.

**Source:** [arXiv cond-mat.quant-gas](https://arxiv.org/abs/2609.10045) | 2026-09-10
