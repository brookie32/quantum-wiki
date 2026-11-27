---
title: "Exact Post-Quantum Security Analysis of Ascon Authenticated Encryption under Nonce Misuse"
date: "2026-11-27"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3076"
summary: "Ascon AEAD is a lightweight authenticated encryption algorithm recently standardized by NIST as SP 800-232, and is expected to be deployed in a wide range of resource-constrained applications. In this"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Ascon AEAD is a lightweight authenticated encryption algorithm recently standardized by NIST as SP 800-232, and is expected to be deployed in a wide range of resource-constrained applications. In this paper, we study its post-quantum security under nonce reuse in the quantum random permutation model. We assume that the adversary makes classical queries to the keyed construction and quantum queries to the public permutation and its inverse. We prove the security up to min{2^{kappa/2},2^{c/3}} quantum and classical query complexities for nonce-misuse resilience confidentiality and authenticity under release of unverified plaintext, where kappa is the key length and c is the capacity size. This improves the dependence on the key length in the previous security bound proved by Hosoyamada (ASIACRYPT 2025) from 2^{kappa/3} to 2^{kappa/2}. To obtain this bound, we introduce a new representation that decomposes Ascon AEAD into an initialization function and a tweakable block cipher, and establish the joint post-quantum security of these components. The representation allows the analysis to exploit c bits of randomness, whereas Hosoyamada's alternative representation of Ascon AEAD used in the previous proof allows kappa (le c) bits of randomness. Combining the joint post-quantum security with the classical security of Ascon AEAD, we prove the post-quantum security of Ascon AEAD. We also construct quantum attacks based on the classical nonce-misuse attacks of Lefevre and Mennink (ToSC 2025(1)), using quantum search with quantum random access memory (qRAM) following the approach of Brassard, Høyer, and Tapp. We first recover an internal state and then use it to construct forgery and key-recovery attacks that break the two security notions considered. Under the stated parameter conditions, these attacks use O(2^{c/3}) primitive queries and processed message blocks. Together with Grover's exhaustive key search, our attacks show that our security bounds are tight in the exponent.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3076) | 2026-11-27
