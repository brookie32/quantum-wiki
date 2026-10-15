---
title: "Reaction Attack on CKKS Deployments with Asymptotically Optimal Query Complexity"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2490"
summary: "We study a protocol-level reaction leakage in CKKS deployments where public coefficient-to-slot (C2S) evaluation keys are combined with a client's 1-bit validity response. Under this deployment surfac"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

We study a protocol-level reaction leakage in CKKS deployments where public coefficient-to-slot (C2S) evaluation keys are combined with a client's 1-bit validity response. Under this deployment surface, a malicious evaluator can recover a ternary secret key using asymptotically optimal O(H) reaction queries, where H is the entropy of the secret key. The attack does not break RLWE or CKKS IND-CPA security. Instead, it exploits the interaction between client-side validity reactions and public homomorphic linear transformations. A shift of a public encryption key yields a ciphertext whose plaintext is a function of the secret key; the public {sf C2S} layer then repacks this information to construct a ciphertext whose validity depends strictly on whether a targeted secret coefficient matches a guessed value. Furthermore, each submitted query is independently randomized with a fresh encryption of zero, so that each resulting malicious ciphertext appears entirely distinct, thereby allowing the attack to simply evade trivial detection mechanisms on the client side. We implemented the full end-to-end attack in Lattigo v6.2.0 and recovered the full secret key across four parameter sets drawn from standard CKKS presets. For uniform ternary secrets, the attack uses O(N) queries and is within a factor 2/log_2 3 < 2 of the oracle-only entropy lower bound. For sparse ternary secrets, a tailored variant further reduces the number of queries in practice. Our results show that observable validity reactions form a practical key-recovery channel in CKKS deployments exposing this surface, even when the underlying cryptographic assumptions remain intact.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2490) | 2026-10-15
