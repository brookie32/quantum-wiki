---
title: "How wide must an eavesdropper be? Leakage of a toric-code logical bit to a strip and the Nishimori point"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.13174"
summary: "arXiv:2611.13174v1 Announce Type: new Abstract: Fault-tolerant quantum computers hand pieces of each logical qubit to separate decoder modules and shared readout lines. How much does a piece reveal? W"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.13174v1 Announce Type: new Abstract: Fault-tolerant quantum computers hand pieces of each logical qubit to separate decoder modules and shared readout lines. How much does a piece reveal? We prove that for any region and any Pauli noise, including correlated noise, an observer's optimal advantage in learning a logical bit is exactly 1 - 2 P_fail, where P_fail is the failure probability of maximum-likelihood decoding confined to that region. Two lessons follow. Geometry, not noise, provides the protection: a region that misses a single column of the code learns exactly nothing at any noise level, while a region that spans the code is protected by noise only at impractical distances (d > 350 for one row at a 10^-3 flip rate). And width is a poor guide to risk: under i.i.d. noise a two-row strip learns exactly as little as one row, yet below threshold an eavesdropper needs a width growing only as ln d. Through the identity, the strip's operational threshold is the Nishimori point of the random-bond Ising model, and a Walsh-Hadamard transfer matrix up to width 16 locates it to within a few thousandths. On two IBM Heron processors (d = 3, 5), an emulated strip adversary shows the predicted jump at width three, and non-uniform qubit errors let a trained attacker profit from the second row that uniform noise makes useless. We turn these results into design rules for partitioned decoding and multiplexed readout. Code and data are included.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.13174) | 2026-11-11
