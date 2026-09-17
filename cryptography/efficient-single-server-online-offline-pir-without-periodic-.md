---
title: "Efficient Single-Server Online-Offline PIR without Periodic Preprocessing"
date: "2026-09-14"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2033"
summary: "Private Information Retrieval (PIR) allows a client to retrieve an entry from a public database without revealing the entry of interest. Standard PIR, however, requires the server to perform expensive"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Private Information Retrieval (PIR) allows a client to retrieve an entry from a public database without revealing the entry of interest. Standard PIR, however, requires the server to perform expensive computation that is linear in the database size per client query. To reduce this online cost, Online-Offline PIR (OO-PIR) was proposed, allowing the client to precompute a query-independent hint table that enables sublinear online query complexity. Unfortunately, existing OO-PIR protocols require either a non-colluding two-server setting or a single-server setting with expensive periodic preprocessing, where the entire hint table must be rebuilt after a limited number of online queries. This results in extremely high bandwidth or computation overhead. We present ESCAPE, a novel OO-PIR protocol for the single-server setting that completely eliminates the expensive periodic preprocessing, supporting unlimited online queries in sublinear time with low constant response bandwidth. The core innovation in ESCAPE lies in reconciling a new hint sampling strategy with Linearly Homomorphic Encryption (LHE) to conceal the correlation between any hint and any online query, while allowing the consumed hint to be refreshed on the fly in sublinear time. We design a random sampling structure that aligns with deterministic, precomputable linear functions, enabling the protocol to exploit the streamlined preprocessing of efficient LHE instantiations. We fully implement ESCAPE, evaluate it on large-scale databases, and release our implementation as open source. Experimental results show that ESCAPE radically reduces end-to-end latency to under a second for 1-8 TiB database sizes and 8-16 KiB entries, achieving up to two orders of magnitude lower bandwidth and up to three orders of magnitude lower computation than state-of-the-art PIR.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2033) | 2026-09-14
