---
title: "Continuum: Concretely Efficient Asynchronous Dynamic MPC with Guaranteed Output Delivery"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2122"
summary: "Traditional secure multiparty computation (MPC) protocols assume a fixed set of participants throughout the computation. Dynamic MPC (DMPC) relaxes this assumption by permitting parties to join or lea"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Traditional secure multiparty computation (MPC) protocols assume a fixed set of participants throughout the computation. Dynamic MPC (DMPC) relaxes this assumption by permitting parties to join or leave during the process. However, practical deployment of DMPC in Internet settings favors tolerating asynchrony and achieving guaranteed output delivery (GOD). Recently, AD-MPC [CCS 2025] introduced an asynchronous DMPC (ADMPC) achieving this goal, but its reliance on per-epoch preprocessing and masking randomness incurs substantial concrete overhead. In this paper, we present Continuum, a concretely efficient ADMPC protocol with GOD. We introduce an aggregated hand-off protocol that ensures transfer consistency across epochs while eliminating per-epoch masking randomness, and a batch multiplication protocol based on the BGW paradigm that defers degree reduction to the hand-off phase and aggregates verification for all multiplications into succinct proofs. Together, these protocols enable a non-interactive computation phase with interaction concentrated in an efficient hand-off phase, overcoming the primary concrete inefficiencies of prior ADMPC designs. We implement Continuum and evaluate its performance on up to 128 geographically distributed servers. In experiments on 22 servers with circuits of depth 6 and width 100, Continuum reduces linear-gate transfer latency from 76.60s to 15.13s (80% reduction) and multiplication-gate evaluation time from 476.62s to 35.67s (93% reduction), compared with AD-MPC, while preserving strong security guarantees.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2122) | 2026-09-20
