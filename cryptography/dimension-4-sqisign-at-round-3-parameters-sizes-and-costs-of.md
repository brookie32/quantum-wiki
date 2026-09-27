---
title: "Dimension-4 SQIsign at Round-3 Parameters: Sizes and Costs of the Compact Format"
date: "2026-09-26"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2221"
summary: "SQIsign holds the smallest known combination among post-quantum signatures, and its dimension-2 signature carries an auxiliary curve whose only role is to make the response computable in dimension 2. "
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

SQIsign holds the smallest known combination among post-quantum signatures, and its dimension-2 signature carries an auxiliary curve whose only role is to make the response computable in dimension 2. SQIsignHD's dimension-4 response has no such curve. We take that construction to the round-3 SQIsign primes, which replaced the round-2 primes in September 2026 after the attacks of Wesolowski and others, on our Rust port of the SQIsign reference code, and measure it in one session next to the reference's own assembly build. At NIST level I the dimension-4 signature is 142 bytes against 200 for the specification's format, with an 84-byte public key: 226 bytes for key and signature together, the smallest level-I combination we are aware of, among isogeny schemes and post-quantum signatures alike, at parameters that stand after those attacks. The price is verification: the dimension-4 verifier costs 9.9 times the dimension-2 verifier of the same code (120.3 against 12.2 megacycles). The dimension-4 parameters published with SQIsignHD are for its authors' own primes; we derive them for the round-3 primes, state which choices are SQIsignHD's and which are ours, and report what was built and measured.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2221) | 2026-09-26
