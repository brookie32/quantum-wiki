---
title: "Verifiable SelfMix"
date: "2026-08-05"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1617"
summary: "Anonymous communication systems aim to hide which user sent which message. Existing designs span efficient mixnets that rely on at least one honest mix server and decentralized protocols such as Dinin"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Anonymous communication systems aim to hide which user sent which message. Existing designs span efficient mixnets that rely on at least one honest mix server and decentralized protocols such as Dining Cryptographers networks (DC-nets) or secure multi-party computation (MPC)-based shuffles, which typically require greater communication or interaction. We introduce verifiable self-mix (VSM), an anonymity architecture for privately placing messages in a public bulletin-board table. VSM separates oblivious slot allocation from anonymous message placement: Unique Number Selection (UNS) assigns each user a distinct hidden location, and Secure Mapping of Private Permutation (SMPP) places each encrypted message at its assigned location without revealing the user-to-location mapping. Because each user learns their own final location, VSM provides unconditional individual verifiability after the table is decrypted. We define VSM and prove anonymity, integrity, and self-verifiability in a static malicious model. We instantiate UNS using either trusted hardware or multi-server plaintext-equivalence tests, and SMPP using ElGamal, Boneh--Goh--Nissim (BGN), and a theoretical fully homomorphic encryption (FHE) construction. For n users and m slots, the vector based SMPP constructions require O(m) ciphertext upload per user and O(nm) public aggregation. We also present an FHE based variant that reduces the client upload to ilde O(log m) for fixed size messages. These constructions offer different tradeoffs between trust, communication, and computation, while preserving the modular structure of VSM and its unconditional individual verifiability.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1617) | 2026-08-05
