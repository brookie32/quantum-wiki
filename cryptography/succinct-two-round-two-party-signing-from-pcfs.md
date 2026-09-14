---
title: "Succinct Two-Round Two-Party Signing from PCFs"
date: "2026-09-11"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1978"
summary: "We introduce new two-party threshold signature schemes with strong efficiency and security. The application of our methodology to the two most popular signatures, Schnorr and ECDSA, yields two-round, "
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

We introduce new two-party threshold signature schemes with strong efficiency and security. The application of our methodology to the two most popular signatures, Schnorr and ECDSA, yields two-round, two-party, stateless and deterministic signing with 4-12 ms of computation on one core of a standard laptop, extremely low communication -- 96 B for Schnorr, and 128 B for ECDSA -- and full concurrent simulatable security. At the heart of our approach is a new pseudorandom correlation function (PCF) for vector-OLE that admits an efficient key generation protocol; we design an end-to-end maliciously-secure and highly parallelizable DKG for this PCF and, using this DKG, we obtain an estimated runtime of 44 s for the (one-time) distributed setup of Schnorr and ECDSA on one core of a standard laptop.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1978) | 2026-09-11
