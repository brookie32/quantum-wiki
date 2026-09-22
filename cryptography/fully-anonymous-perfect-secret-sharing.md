---
title: "Fully Anonymous Perfect Secret-Sharing"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2145"
summary: "Fully anonymous secret-sharing schemes ensure two properties at once: for any fixed secret, the combined shares of every unauthorized set of participants are uniformly random, and every authorized set"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Fully anonymous secret-sharing schemes ensure two properties at once: for any fixed secret, the combined shares of every unauthorized set of participants are uniformly random, and every authorized set can reconstruct the secret exactly using only the share values, without needing to know which participant holds which share or in what order the shares appear. It was previously open whether such schemes exist for nontrivial exact-threshold parameters 2 < t < n. For the smallest previously open threshold, t= 3, we give, for every n≥4, an explicit fully anonymous scheme for one-bit secrets, with 2⌈log n⌉-bit shares and a perfect reconstruction algorithm running in poly(log n) time. The next result, found by ChatGPT, shows that for every 1 ≤t ≤n there exists a fully anonymous perfect (t,n) threshold secret-sharing scheme for one-bit secrets, in which each share has length O(tlog n) bits. The proof is purely existential and does not provide an efficient construction. Moreover, ChatGPT identified a simple construction of a fully anonymous perfect scheme for every access structure A; if A contains ℓ authorized sets, then each share consists of ℓ2 bits. The authors subsequently verified and streamlined the proofs on their own and take full responsibility for their correctness.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2145) | 2026-09-22
