---
title: "Functional Tensor Trains for High-Order Greeks and Exposure Tails of Multi-Asset Structured Products"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.42119"
summary: "arXiv:2610.42119v1 Announce Type: cross Abstract: Risk management of worst-of autocallables needs price sensitivities (Greeks) up to third order and the potential future exposure, a tail quantile of t"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.42119v1 Announce Type: cross Abstract: Risk management of worst-of autocallables needs price sensitivities (Greeks) up to third order and the potential future exposure, a tail quantile of the note's future value. In Monte Carlo, each order of differentiation multiplies the sampling noise by a factor that grows with the observation frequency, and nested simulation turns the noise of its inner paths into a bias of the quantile. We instead solve the backward pricing recursion, storing the continuation value as an hp functional tensor train (hp-FTT) whose piecewise-polynomial cores are split at the barriers, so that worst-of barrier events act exactly, with rank one. For Gaussian transitions we show that the polynomial degree sufficient for an error arepsilon grows only as sqrt{log(1/arepsilon)}. One solve then gives every Greek at any spot without sampling noise, by integrating the likelihood-ratio weight against the stored value, and the values it stores at future dates replace inner simulation. Against the strongest Monte Carlo estimators we could build or find published, on worst-of autocallables observed monthly on three to five assets, the order of the Greek and the accuracy decide which method is cheaper. At 1% accuracy Monte Carlo is more than an order of magnitude cheaper for deltas, second-order Greeks go either way, and hp-FTT is cheaper for every third-order Greek, by up to two orders of magnitude. At 0.1% hp-FTT is cheaper for every Greek we could check, under geometric Brownian motion and local volatility alike. For the exposure alone Monte Carlo is cheaper at 1% and hp-FTT at 0.1%, and a solve run for the Greeks yields it for little more than scenario sampling. Sampling pays in variance for each derivative and hp-FTT in rank for each asset, so Monte Carlo keeps low-order Greeks at percent accuracy, rarely observed contracts and many assets.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.42119) | 2026-11-02
