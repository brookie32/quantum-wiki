---
title: "Hybrid Krotov gradient descent Optimization for Quantum Machine Learning"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.18082"
summary: "arXiv:2611.18082v1 Announce Type: new Abstract: We introduce and study a Krotov-inspired discrete adjoint optimization scheme for quantum machine learning and focus on a hybrid online-to-batch schedul"
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2611.18082v1 Announce Type: new Abstract: We introduce and study a Krotov-inspired discrete adjoint optimization scheme for quantum machine learning and focus on a hybrid online-to-batch schedule. The method transfers the forward/costate/local-update logic of continuous-time optimal control to parameterized quantum circuits by replacing time locality with gate-index locality. For a broad class of fixed-generator variational gates and terminal-state losses, we show that the batch Krotov direction coincides with the exact gradient of the empirical loss. Under standard smoothness assumptions, this yields monotonic descent and convergence of the batch method, and convergence of the tail of the hybrid method after a finite switch to the batch phase. Empirically, we benchmark hybrid Krotov against the tuned PennyLane optimizer suite and L-BFGS-B on a four-bit parity classifier and on the Perez-Salinas data re-uploading classifier for the crown problem. Across matched hyperparameter sweeps with three seeds per configuration, hybrid Krotov dominates every tuned first-order baseline and matches the strongest structured PennyLane methods on parity, while approaching the accuracy of L-BFGS-B on Perez-Salinas at first-order per-iteration cost.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.18082) | 2026-11-16
