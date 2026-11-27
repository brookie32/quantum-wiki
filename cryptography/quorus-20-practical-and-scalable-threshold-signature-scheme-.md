---
title: "Quorus 2.0: Practical and Scalable Threshold Signature Scheme for NIST-Standardized ML-DSA"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3044"
summary: "ML-DSA is a widely adopted post-quantum signature algorithm, standardized by NIST as FIPS 204. A threshold signature scheme for ML-DSA lets a group of signers, none of whom holds the key, produce sign"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

ML-DSA is a widely adopted post-quantum signature algorithm, standardized by NIST as FIPS 204. A threshold signature scheme for ML-DSA lets a group of signers, none of whom holds the key, produce signatures that verify under the unmodified, standardized verification. Existing approaches are limited in different ways: they are bound to at most 6 parties, require threshold fully homomorphic encryption, or scale to many parties but spend tens of online rounds and a heavy preprocessing phase involving mixed arithmetic--Boolean computation. Moreover, to avoid evaluating a cryptographic hash function inside multi-party computation (MPC), they reveal the transcripts of rejected signing attempts. To make these transcripts simulatable, they either modify the underlying ML-DSA signing algorithm by adding noise, or rely on a computational assumption beyond those underlying ML-DSA. We first prove that rejected ML-DSA transcripts can be simulated statistically, with no added noise and no additional assumption, so that output signatures follow exactly the standardized distribution. Building on this result, we construct an efficient threshold protocol using only arithmetic modulo ML-DSA's native modulus q that, for the first time, simultaneously (i) scales to any number of parties n with t<n/2 malicious corruptions, (ii) has only 4 online signing rounds and 3.3imes less online communication than the round-optimized instantiation of the closest previous protocol, Quorus (USENIX Security~'26), which takes 16 rounds, (iii) has a far lighter preprocessing phase, with fewer than 20 rounds against 81 to 108 for Quorus, and over an order of magnitude less communication as the number of parties grows, and (iv) avoids any extra primitive or assumption beyond those underlying ML-DSA. In a wide-area deployment with tens of parties spread over different continents worldwide, the online phase of our protocol completes in under a second.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3044) | 2026-11-25
