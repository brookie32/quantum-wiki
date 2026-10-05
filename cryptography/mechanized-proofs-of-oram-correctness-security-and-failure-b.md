---
title: "Mechanized Proofs of ORAM Correctness, Security, and Failure Bounds"
date: "2026-10-03"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2321"
summary: "ORAM is a fundamental cryptographic technique that permits outsourcing memory storage while probabilistically hiding memory access patterns of client programs. We use the EasyCrypt proof assistant to "
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

ORAM is a fundamental cryptographic technique that permits outsourcing memory storage while probabilistically hiding memory access patterns of client programs. We use the EasyCrypt proof assistant to obtain fully mechanized proofs of correctness and security of Simple ORAM [Chung and Pass, 2013] and Path ORAM [Stefanov et al., CCS 2013]. To the best of our knowledge, these are the first machine-checked proofs that cover the correctness bound, i.e., the failure probability, of an ORAM construction. Our proofs refine, simplify, clarify and slightly improve the paper proofs, and many parts of our development can be reused to obtain similar results for other ORAM constructions. As a final contribution, we provide a general library that handles the recursive composition of ORAM constructions to reduce storage demands on the client, and apply this to Path ORAM to capture a practically-relevant instantiation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2321) | 2026-10-03
