---
title: "Write-Public Oblivious RAM and Its Applications"
date: "2026-09-22"
updated: "2026-09-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2163"
summary: "Oblivious RAM (ORAM) protocols enable a resource-constrained client to outsource data to an untrusted server, and access this data without revealing what is being accessed. While ORAM protocols are al"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

Oblivious RAM (ORAM) protocols enable a resource-constrained client to outsource data to an untrusted server, and access this data without revealing what is being accessed. While ORAM protocols are almost optimal, concretely efficient ORAM protocols incur sub-optimal bandwidth overhead and require multiple roundtrips of communication between the client and the server. In this work, we introduce write-public ORAM: a relaxed variant of ORAM that hides what data is being read, but not what data is being updated on the server. We present wpORAM, a write-public ORAM that modifies Path ORAM to achieve a log N-factor improvement in bandwidth and roundtrips over Path ORAM during writes. The asymptotic cost of reads in wpORAM remains the same as Path ORAM, with a slight slowdown in practice. wpORAM, when used with a Trusted Execution Environment (TEE), can implement a dynamic Private Information Retrieval scheme that efficiently updates data stored in a public database. We use wpORAM to implement a private blockchain RPC server that enables blockchain clients to query RPC nodes without revealing their queries to the server operator. Our evaluation shows that, while syncing with the latest blockchain state, our RPC node achieves a 3-4x speedup over Path ORAM. Our RPC node can serve reads with a slowdown of approximately 23% compared to Path ORAM.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2163) | 2026-09-22
