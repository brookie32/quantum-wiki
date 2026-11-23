---
title: "Mosaic: A Modular Framework for Private Fuzzy Heavy Hitters"
date: "2026-11-20"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2968"
summary: "We present Mosaic, a modular cryptographic framework for Private Fuzzy Heavy Hitters Detection, a new problem introduced and formalized in this work. In this problem, a service provider aims to identi"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

We present Mosaic, a modular cryptographic framework for Private Fuzzy Heavy Hitters Detection, a new problem introduced and formalized in this work. In this problem, a service provider aims to identify the most frequent items (i.e., heavy hitters) in private client data without learning any individual client's data. Motivated by real-world applications where inputs are inherently noisy, we consider fuzzy heavy hitters that are close to a sufficiently large number of client data points under a chosen distance metric. Mosaic operates in the setting with two non-colluding servers and supports both the known-dictionary setting (where candidate fuzzy heavy hitters are fixed in advance) and the unknown-dictionary setting (where popular items must be discovered). The framework proceeds in two phases: during the upload phase, each client shares an encoding of their input with each server; in the fuzzy matching phase, the servers jointly identify fuzzy heavy hitters without learning any additional information about individual client's data. In the upload phase, Mosaic introduces a new cryptographic primitive called Property-Based Function Secret Sharing (PB-FSS), which relaxes the standard notion of FSS (Boyle et al., Eurocrypt 2015) in that the outputs of the FSS evaluations satisfy a certain property, rather than forming exact additive secret shares of the function output. We present a suite of new PB-FSS constructions for the L_infty and L_p distance metrics from lightweight cryptographic techniques. Furthermore, we introduce new methods to prevent malicious client behavior by detecting malformed PB-FSS shares. In the fuzzy matching phase, Mosaic presents two approaches, one involving only the two servers, and one involving an additional trusted dealer to improve efficiency. All parties are assumed to be semi-honest during the fuzzy matching phase. Finally, we implement Mosaic and evaluate it using real-world trace data from a ride-sharing service. In one scenario, Mosaic servers discovered over a thousand of the most popular ride start locations among 21 thousand users within 30-90 seconds. On the user side, the protocol requires only lightweight computation (as low as 0.14 millisecond) and communication (as low as 9 KB).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2968) | 2026-11-20
