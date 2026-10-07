---
title: "HyBind: Structural Analysis of PQ/T Hybrid Cryptographic Usage"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2347"
summary: "The quantum threat to traditional public-key cryptography makes migration to post-quantum cryptography necessary. During migration, the presence of both post-quantum and traditional (PQ/T) algorithms "
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

The quantum threat to traditional public-key cryptography makes migration to post-quantum cryptography necessary. During migration, the presence of both post-quantum and traditional (PQ/T) algorithms does not establish that their outputs jointly determine a key or verification decision. We propose HyBind, an intraprocedural Python source-analysis framework using registered API contracts. HyBind traces component secrets to returned keys and checks whether signature acceptance requires both verifiers to succeed. Function-return and execution-effect checks account for alternative outcomes and changes to local bindings. Two internal presence-based heuristics give identical decisions for joint versus omitted secret contribution and AND versus OR verification, while HyBind distinguishes these structures. All 50 controlled fixtures match their specified outputs with the annotation assumption enabled. A separate suite of 33 programs, including 15 using native cryptographic APIs, matches its specified positive-finding counts in both settings. Native runtime checks exercise ML-KEM/X25519 key derivation and ML-DSA/Ed25519 acceptance. Relaxing return or effect requirements admits traditional-only key results as hybrid findings in the evaluated cases. HyBind provides the contributing calls and outcome evidence needed to review whether an individual traditional invocation participates in a PQ/T hybrid.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2347) | 2026-10-05
