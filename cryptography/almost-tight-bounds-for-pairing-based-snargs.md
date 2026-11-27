---
title: "(Almost) Tight Bounds for Pairing-Based SNARGs"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3031"
summary: "We construct a publicly verifiable succinct non-interactive argument (SNARG) for NP in the asymmetric bilinear generic group and random oracle models. At lambda bits of security, a proof consists of o"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

We construct a publicly verifiable succinct non-interactive argument (SNARG) for NP in the asymmetric bilinear generic group and random oracle models. At lambda bits of security, a proof consists of one G_1 element and lambda+o(lambda) additional bits. Assuming exponentially secure pseudorandom generators, we show that the additional bit string cannot have length o(lambda) under natural restrictions on setup and verification. The lower bound applies to schemes with exponentially small completeness and soundness errors, where soundness holds against subexponential adversaries. Our construction uses a variant of the KZG polynomial commitment scheme that may be of independent interest. The commitment is the hash of a target group element, and an opening proof still consists of one G_1 element. Given the opening proof and the claimed evaluation, the verifier reconstructs the target group element with one pairing and checks its hash against the commitment, saving one pairing over standard KZG verification.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3031) | 2026-11-24
