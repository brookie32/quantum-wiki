---
title: "AVXPoS: Reducing Consensus Verification Cost in the Ethereum Proof-of-Stake Client"
date: "2026-08-28"
updated: "2026-08-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1827"
summary: "Ethereum Proof-of-Stake (PoS) clients must verify large volumes of Boneh--Lynn--Shacham (BLS) signatures for attestations, sync-committee messages, and other consensus-critical objects within fixed sl"
last_verified: "2026-08-30"
review_by: "2026-11-28"
stale: false
---

Ethereum Proof-of-Stake (PoS) clients must verify large volumes of Boneh--Lynn--Shacham (BLS) signatures for attestations, sync-committee messages, and other consensus-critical objects within fixed slot deadlines. This recurring cost competes with state transition, fork choice, and message propagation for client CPU time, so reducing it increases the verification headroom available under bursty load. Prior cryptographic-engineering work has shown that SIMD can substantially accelerate BLS verification kernels, but these gains do not automatically survive client software boundaries, runtime scheduling, and irregular verification ranges. We present AVXPoS, a client-aware batching framework for BLS verification in the Prysm Ethereum PoS client. AVXPoS treats batched verification as a client-level systems problem: it preserves Prysm's verification semantics while reorganizing protocol-shaped requests into native batched states that expose SIMD parallelism across API, worker, and native-backend boundaries. We instantiate AVXPoS with an AVX-512 backend for BLS12-381, combining Go-side range formation with C-side width-adaptive dispatch. On a resource-constrained two-core Intel host, AVXPoS gains 1.44--2.10imes over Prysm's production exttt{blst} backend at selected small batch sizes that bracket the post-aggregation p50/p95/p99 batch-size quantiles of an all-subnets steady-state mainnet stress trace, and reaches up to 3.18imes in controlled capacity sweeps. On a 16-core AMD host, a production checkpoint-backfill verifier at Ethereum's 128-block request cap improves by 1.81imes. Cross-platform results indicate that the relative speedup depends in part on Prysm's worker budget, because worker partitioning determines how much SIMD parallelism remains within each native range.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1827) | 2026-08-28
