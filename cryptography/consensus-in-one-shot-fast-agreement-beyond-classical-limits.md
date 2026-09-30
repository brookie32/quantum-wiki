---
title: "Consensus in One Shot: Fast Agreement Beyond Classical Limits"
date: "2026-09-29"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2269"
summary: "Good-case latency, studied in early fast-consensus protocols (Martin and Alvisi, DSN 2005) and formalized by Abraham, Nayak, Ren, and Xiang (DISC 2020), captures a natural efficiency goal: when the se"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

Good-case latency, studied in early fast-consensus protocols (Martin and Alvisi, DSN 2005) and formalized by Abraham, Nayak, Ren, and Xiang (DISC 2020), captures a natural efficiency goal: when the sender is honest, agreement should be reached quickly for the honest parties. In the standard classical model, however, there exists a barrier for any fgeq n/3 corrupted parties. Specifically, synchronous broadcast requires good-case latency at least Delta+elta for fgeq n/3, where elta is the actual, unknown message-delay bound and Delta gg elta is its known, conservative upper bound. Under partial synchrony, consistency and liveness cannot even both hold for f geq n/3 (Dwork, Lynch, and Stockmeyer, JACM 1988). In this work we study the use of quantum information to get past these classical barriers, and specifically using one-shot signatures (OSS) (Amos et al., STOC 2020, Shmueli and Zhandry, CRYPTO 2025). OSS prevents even a corrupt signer from issuing signatures on different messages under the same verification key, which provides cryptographic non-equivocation without trusted hardware assumptions. Assuming OSS and a public-key infrastructure, we obtain two main results against quantum polynomial-time static corruptions. First, under synchrony, we construct a state-machine replication (SMR) protocol without clients, with optimal elta good-case latency, tolerating any ff. Specifically, a corrupt majority may cause progress to stop, but cannot create conflicting histories. Such an always consistent protocol is impossible classically (without assumptions like trusted hardware) even if liveness is only required to hold against a single corrupt party. In both our SMR protocols, communication is entirely classical, with only local quantum computation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2269) | 2026-09-29
