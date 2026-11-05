---
title: "Blockchain-Anchored Proactive Refresh for Dynamic Threshold Services"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2755"
summary: "A long-lived threshold service must issue shares to participants that join after deployment, refresh them against a mobile adversary, and allow participants offline during a refresh to recover missed "
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

A long-lived threshold service must issue shares to participants that join after deployment, refresh them against a mobile adversary, and allow participants offline during a refresh to recover missed updates. We show that charging exposure solely to committed epochs is fundamentally insufficient: an aborted refresh attempt that publishes candidate update tokens can reveal the secret even if no committed epoch exceeds its corruption budget. To eliminate this exposure leakage, we index security by fine-grained states covering both committed epochs and aborted attempts. Each state's budget bounds all participants whose local material or public update records originate from that state, enforced via an append-only, durable release ledger that is never rolled back upon abort. A fixed dealer committee anchors encrypted update records in blockchain blob storage, enabling non-interactive recovery for offline participants without contacting dealers, while an interactive bisection dispute protocol deterministically attributes faulty records on chain. Our core cryptographic result is an explicit distribution-preserving shift of the actual generation transcript, establishing proactive secrecy and past-share unforgeability after dealer-state disclosure without idealizing the underlying subprotocols. An end-to-end Rust implementation benchmarks complete lifecycles across up to 1,280 participants on an EVM chain, demonstrating sub-second group recovery and practical gas costs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2755) | 2026-11-04
