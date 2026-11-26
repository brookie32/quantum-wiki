---
title: "CHARTS: Compute-efficient Homomorphic Anonymous Routing with Tag Sums"
date: "2026-11-23"
updated: "2026-11-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3012"
summary: "Anonymous routing is a fundamental tool to protect communication privacy by hiding who communicates with whom. Existing constructions based on a single untrusted router, including NIAR (EUROCRYPT'21) "
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

Anonymous routing is a fundamental tool to protect communication privacy by hiding who communicates with whom. Existing constructions based on a single untrusted router, including NIAR (EUROCRYPT'21) and the recent sPAR (CCS'26), typically rely on oblivious permutation or placement of encrypted messages, which incurs substantial computational overhead at the router. In this paper, we present CHARTS, a compute-efficient anonymous routing protocol that eliminates the need for oblivious placement or permutation. Instead, CHARTS uses random tags and homomorphic aggregation to recover encrypted messages as an unordered multiset. Each sender encrypts its message under the intended receiver's public key and associates the resulting ciphertext with a fresh random tag. Using multiparty homomorphic encryption, the router computes power sums of the tags and tag-weighted ciphertext aggregates, from which it recovers a multiset of the encrypted messages. We prove simulation-based security against static semi-honest adversaries under decisional RLWE and an IND-CPA-secure, key-private, weakly robust public-key encryption scheme. We implement CHARTS in Go using Lattigo. Our direct construction requires only homomorphic additions and evaluates a batch of 128 messages in approximately 260 ms of router computation, achieving a speedup of over 35,000 times compared with sPAR using its published parameters, on the same hardware and with the same thread count. We also introduce a factorized variant that reduces sender communication at the cost of additional router computation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3012) | 2026-11-23
