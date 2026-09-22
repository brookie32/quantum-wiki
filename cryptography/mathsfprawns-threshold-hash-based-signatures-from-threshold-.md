---
title: "mathsf{PRAWNS}: Threshold Hash-Based Signatures from Threshold PRFs"
date: "2026-09-21"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2142"
summary: "We propose an efficient threshold mechanism that is well suited for certain hash-based signatures. Our proposal has a number of compelling features: • The final signature assembled from a quorum of si"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

We propose an efficient threshold mechanism that is well suited for certain hash-based signatures. Our proposal has a number of compelling features: • The final signature assembled from a quorum of signature shares has the same format as a non-threshold hash-based signature. In particular, the verifier is unaware that the signer is thresholdized. Moreover, we can add and remove parties and change the threshold without changing the public key. • Our framework can be used to thresholdize one-time signature schemes, such as Winternitz, and a few-time schemes, such as XMSS, HORS, FORS, and PORS+FP. • The public key and the signatures reveal nothing about the number of parties n or the threshold t. • An instantiation of our framework scales well to a large number of parties n and a large threshold t. One limitation of the framework is that it does not support an efficient distributed key generation protocol (DKG). Another limitation is that the framework does not directly apply to SLH-DSA. It is primarily designed for the Winternitz, XMSS, and FORS schemes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2142) | 2026-09-21
