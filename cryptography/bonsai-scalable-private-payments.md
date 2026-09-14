---
title: "Bonsai: Scalable Private Payments"
date: "2026-09-12"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1987"
summary: "Virtually all deployed private payment systems publish a nullifier for every transaction to prevent double spending. At a million transactions per second, the nullifier set grows by a petabyte each ye"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Virtually all deployed private payment systems publish a nullifier for every transaction to prevent double spending. At a million transactions per second, the nullifier set grows by a petabyte each year. In this work, we tackle the question of sustaining massive throughput in private payments while ensuring the system can be run on commodity hardware. We construct Bonsai, an account-based private payment scheme where validators store a single commitment per account and never store any nullifiers. Instead, each user privately maintains the nullifiers of the payments it has received, and can prune older nullifiers to cold storage so that its active state remains small. An external observer only learns that an account performed some action (send/receive) but never learns the amount or counterparty of a payment. To verify proofs at this rate, we add zero-knowledge to Pari [USENIX '26] with no increase in proof size and negligible prover overhead, and use it with a batch verification strategy. Our prototype verifies over a million operations per second on an M5 MacBook Pro.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1987) | 2026-09-12
