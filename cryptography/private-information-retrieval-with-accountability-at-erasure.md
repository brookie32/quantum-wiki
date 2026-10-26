---
title: "Private Information Retrieval with Accountability at Erasure-Optimal Server Redundancy"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2639"
summary: "Private information retrieval (PIR) hides which database item a client requests. We study PIR that also identifies servers that respond incorrectly. Against a coalition of at most t corrupted servers,"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

Private information retrieval (PIR) hides which database item a client requests. We study PIR that also identifies servers that respond incorrectly. Against a coalition of at most t corrupted servers, the client must retrieve the item and identify every deviating server when at most d deviate. Above that threshold, it must abort and return an empty identification set, with a specified statistical error. We present SynTrace, a single-round compiler for linear PIR supporting audit queries whose honest answers belong to a public code. The client combines the retrieval query with m audit queries using secret linear mixing and independent blinding. Audit syndromes identify deviations before reconstruction. We prove perfect query privacy, zero false-identification probability within the deviation threshold, and statistical realization of an accountable PIR functionality. For Shamir-based PIR, SynTrace uses k=t+d+1 servers. Under the stated privacy and download assumptions, tolerating d missing responses already requires this many servers, so identification adds no server overhead. With this number of servers, m=d audit queries suffice with a suitable field, and are necessary within the specified syndrome-span decoder class. Additional audit queries can reduce communication by allowing a smaller field. For one 32 KiB record from a 1 GiB database, with five servers, privacy and robustness against two corrupted servers, and error at most 2^{-40}, SynTrace uses 2.25 MiB of communication, compared with 8.96 MiB for the homomorphic-MAC construction of Eriguchi, Kurosawa and Nuida (TCC 2022) under the same workload and thresholds. Batched retrievals can share the audit queries.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2639) | 2026-10-26
