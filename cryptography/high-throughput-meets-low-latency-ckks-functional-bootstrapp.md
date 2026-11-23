---
title: "High Throughput Meets Low Latency: CKKS Functional Bootstrapping on GPUs"
date: "2026-11-22"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2989"
summary: "Functional (programmable) bootstrapping extends the bootstrapping operation of Fully Homomorphic Encryption (FHE) to evaluate an arbitrary function while refreshing a ciphertext. This capability was a"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Functional (programmable) bootstrapping extends the bootstrapping operation of Fully Homomorphic Encryption (FHE) to evaluate an arbitrary function while refreshing a ciphertext. This capability was a unique feature of scalar CGGI/DM cryptosystems for many years until it was recently added to the toolset of vectorized FHE schemes, with CKKS being the most promising option both in terms of throughput (amortized time) and functionality. Previous work showed that CKKS functional bootstrapping outperforms CGGI/DM functional bootstrapping in terms of throughput by two to three orders of magnitude, but still loses in latency on CPU by two to three orders of magnitude. We present an optimized GPU implementation of CKKS functional bootstrapping that closes the latency gap. Our implementation supports evaluating functions over both small integers (as in CGGI/DM) and real numbers (unique to CKKS), which we call discrete-CKKS and continuous-CKKS functional bootstrapping, respectively. Our GPU implementation evaluates discrete-CKKS functional bootstrapping over a ciphertext with 64 encrypted Boolean values in 2.30 ms and with 16,384 encrypted Boolean values in 5.24 ms on RTX 4090, a consumer-grade GPU, whereas the CGGI programmable bootstrapping of one encrypted bit on the same GPU takes 2.16 ms. For 6-bit lookup tables, our discrete-CKKS functional bootstrapping takes 31.4 ms for 32,768 integers vs. 15.7 ms for one integer using CGGI. On RTX PRO 6000, our continuous-CKKS functional bootstrapping is 3.5x to 7.4x faster than the best prior GPU implementation on the same GPU, while bootstrapping four to eight times as many values. Our continuous-CKKS functional bootstrapping of the identity function, which corresponds to regular CKKS bootstrapping, takes 4.82 ms for 16,384 slots on RTX PRO 6000, the first reported bootstrapping latency below 5 ms for a CKKS ciphertext with this many slots. We were able to achieve such low latencies via a combination of algorithmic, architectural, and implementation optimizations, many of which were applied to both FIDESlib and OpenFHE. Our continuous-CKKS functional bootstrapping also scales to larger ring dimensions, reaching 28.5 bits of precision with 23 levels remaining at a ring dimension of 2^{17}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2989) | 2026-11-22
