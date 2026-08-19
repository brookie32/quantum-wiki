---
title: "M-QAM MIMO Maximum-Likelihood Detection with QAOA: ML-Rate Offline Angle Design and Correlated Infinite-Size Spin-Glass Models"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.17721"
summary: "arXiv:2608.17721v1 Announce Type: cross Abstract: The quantum approximate optimization algorithm (QAOA) targets NP-hard maximum-likelihood (ML) detection in multiple-input multiple-output (MIMO) syste"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.17721v1 Announce Type: cross Abstract: The quantum approximate optimization algorithm (QAOA) targets NP-hard maximum-likelihood (ML) detection in multiple-input multiple-output (MIMO) systems. Existing M-ary quadrature amplitude modulation (M-QAM) detectors design angles by expected Ising energy: online per instance, warm-started, or ramped, while train-once designs remain B/QPSK-only or block-local, leaving M-QAM without a size-scalable benchmark. Their infinite-size spin-glass theory assumes independent disorder, matching the retained covariances at B/QPSK but not M-QAM's correlated couplings and fields. We develop a correlated infinite-size multi-species spin-glass framework whose covariance-matched evaluators make that energy an offline objective with a size-scalable benchmark. In addition, the ML rate, the exponential rate of sampling the ML string, is for the first time exploited for QAOA angle design in MIMO detection. The energy evaluator is q-free at O(p,4^p) cost while the ML rate transfers angles from a fixed q_{rm ref}-qubit reference. Tests reach 4096-QAM, 128 antennas, p=30 and per-symbol SNR 0-45 dB. In simulations, ML rates fall as a power law r_0,p^{-alpha}, with larger exponents for the sampling design, which tracks exact ML at 5imes5 16-QAM (0-20 dB) and 3imes3 64-QAM (8-28 dB) while its bit-error rate (BER) advantage widens with SNR to two orders of magnitude. The approach points toward near-optimum decoding on deeper noiseless fault-tolerant quantum (FTQ) circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.17721) | 2026-08-19
