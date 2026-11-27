---
title: "When Verification Leaks: Breaking and Repairing Verifiable PIR with Small Client Storage"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3039"
summary: "Verifiable private information retrieval (vPIR) lets a client retrieve a database entry privately and check the server's answer. Efficient designs such as VeriSimplePIR require clients to retain a lar"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Verifiable private information retrieval (vPIR) lets a client retrieve a database entry privately and check the server's answer. Efficient designs such as VeriSimplePIR require clients to retain a large hint: preprocessed database information needed to recover answers. Rathee, Lee, and Popa (IEEE S&P 2026) reduce this storage by using homomorphic encryption to delegate the computations involving the hint to the server. They argue that the client's acceptance or rejection of a respon se reveals no query information. We refute this claim with two selective-failure attacks. A malicious server can modify an encrypted result so that, after decryption, the client's correctness check tests a guess about the query. Our attacks make acceptance more likely when the query matches a chosen position or falls within a chosen set. For a single-position test under the original parameters, the client accepts with probability about 6% when the guess is correct and negligible probability otherwise. Our repair requires the server to prove that the returned ciphertext is the output of the prescribed computation. The client verifies this proof before decryption, so it rejects manipulated ciphertexts without testing their decrypted contents. We exploit the linear structure of the delegated computation to construct a compact proof checked against a short commitment to the hint. The resulting vPIR scheme provides query privacy and answer correctness against a malicious server without requiring the client to retain the large hint.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3039) | 2026-11-25
