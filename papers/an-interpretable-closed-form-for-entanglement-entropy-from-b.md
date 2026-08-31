---
title: "An interpretable closed form for entanglement entropy from bitstrings, guided by a graph neural network"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.22713"
summary: "arXiv:2606.22713v2 Announce Type: replace Abstract: The empirical bitstring distribution is the most accessible observable on Rydberg-atom arrays, but the bipartite von~Neumann entropy it constrains i"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2606.22713v2 Announce Type: replace Abstract: The empirical bitstring distribution is the most accessible observable on Rydberg-atom arrays, but the bipartite von~Neumann entropy it constrains is far costlier to obtain. We present a six-term linear closed form for the entropy, built on bitstring-derivable physics scalars, and characterize its accuracy, portability, scaling behaviour, and calibration cost. The feature set is selected with guidance from a trained graph neural network: probing the network localizes its entropy prediction to the two-point correlators on the bipartition boundary, and an exhaustive ground-truth search restricted to those boundary correlators isolates the form. It reaches 0.024~nats mean absolute error in distribution: 6.4 times the network's error, but in a form a human can read and apply without retraining. Fit once and applied unchanged, it has lower error than the base network on five of six out-of-distribution pools and ties the sixth. An independent density-matrix renormalization-group study to one hundred atoms -- five times the reach of exact diagonalization -- settles the size-extrapolation question: coefficients frozen at small size fail at scale, but the failure is structured. Refit per size the form holds to 25--50~mnat (cross-validated); two of its six slopes follow clean inverse-size laws, one a downward curving growth, and the others are trendless; the fitted laws deploy the form label-free at roughly 40--80~mnat. The result fixes a label-budget rule: at large sizes, a few dozen labels recalibrate the closed form to match a fine-tuned in-distribution ensemble on the same features, while nonlinear ML models pull ahead only given large labelled datasets.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.22713) | 2026-08-31
