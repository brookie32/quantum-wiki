---
title: "Statevector-to-Hardware Reconstruction of a Four-Qubit ZZ Quantum Kernel: A Single-Backend Case Study of Three Execution Jobs"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.20377"
summary: "arXiv:2607.20377v2 Announce Type: replace Abstract: Hardware noise and finite sampling perturb the fidelity estimates forming a quantum-kernel Gram matrix. We measured how far three hardware-reconstru"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2607.20377v2 Announce Type: replace Abstract: Hardware noise and finite sampling perturb the fidelity estimates forming a quantum-kernel Gram matrix. We measured how far three hardware-reconstructed Gram matrices depart from an exact statevector reference for one frozen four-qubit ZZ feature map on N=24 indoor air-quality windows, executed on ibm_fez at 1024 shots per circuit in three single, non-interleaved jobs: baseline, dynamical decoupling alone, and gate twirling alone. All were complete, finite, and positive-semidefinite. Off-diagonal root-mean-squared error (RMSE) against the reference was 0.0878, 0.0864, and 0.0427; full-matrix centered kernel alignment (CKA) ranged 0.933-0.989 and the post hoc diagonal-excluded (U-centered) CKA 0.816-0.986. The gate-twirled job deviated least on every reported geometry axis; its baseline contrasts are deletion-stable for the Spearman, mean-absolute-error, RMSE, and full-matrix CKA diagnostics, while the Pearson and diagonal-excluded contrasts fall just below that convention. Dynamical decoupling was not separated from the baseline. The observed error exceeded both finite-shot reference scales, so, under those sampling-only models, sampling does not explain it. Centered kernel-target alignment did not track reconstruction fidelity and stayed at or below each label-permutation reference: implementation fidelity and task relevance are distinct diagnostic axes. All configuration-level statements describe three realized jobs on one backend; no mitigation-efficacy, classifier-superiority, forecasting, or quantum-advantage claim is made.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.20377) | 2026-09-07
