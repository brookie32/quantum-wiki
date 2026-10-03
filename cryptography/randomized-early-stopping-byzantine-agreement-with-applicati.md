---
title: "Randomized Early-Stopping Byzantine Agreement with Applications to Round-Efficient MPC"
date: "2026-09-30"
updated: "2026-10-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2284"
summary: "We consider two main classes of synchronous round-efficient Byzantine Agreement (BA) protocols: expected constant rounds and early-stopping. Randomized protocols can terminate in expected constant rou"
last_verified: "2026-10-03"
review_by: "2027-01-01"
stale: false
---

We consider two main classes of synchronous round-efficient Byzantine Agreement (BA) protocols: expected constant rounds and early-stopping. Randomized protocols can terminate in expected constant rounds, and early-stopping protocols' worst-case round complexity depends on the actual number of corrupted parties fle t, with min(t+1, f+2) being optimal. In this work, we combine the benefits of both classes, proposing a protocol that has constant round-complexity in expectation and O(f) in the worst case. We present our protocol in the form of a compiler that can lift a broad class of expected-constant-round BA protocols, including Feldman--Micali and Katz--Koo, to {em also} achieve near-optimal O(f) worst-case complexity. This yields the {em first} treatment of perfectly secure BA protocols for t<n/3 that is both expected constant-round and near-optimal (O(f)) early stopping. Assuming a PKI, we show a variant of the compiler with a better round complexity, tolerating t<n/2 corruptions. We also extend our results to parallel broadcast, also known as interactive consistency (IC). We give a compiler that runs N Byzantine agreement instances in parallel while preserving both guarantees, expected constant rounds and O(f) rounds in the worst case. Parallel broadcast then follows with one extra round for t<n/2. To the best of our knowledge, this is the first compiler of its kind, and the first IC protocol with such expected and worse round-complexity. Finally, by combining our protocol with standard (fast) sequential composition techniques, we obtain a valid candidate to execute multi-party computation protocols that require broadcast as their hybrid. By running existing MPC constructions using our broadcast protocol, we obtain the first MPC protocol that requires constant rounds of P2P communication in expectation and O(f) rounds in the worst case.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2284) | 2026-09-30
