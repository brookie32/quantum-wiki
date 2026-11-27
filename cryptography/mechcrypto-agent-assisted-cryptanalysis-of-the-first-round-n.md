---
title: "MechCrypto: Agent-Assisted Cryptanalysis of the First-Round NGCC Candidates"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3050"
summary: "Evaluating large batches of cryptographic submissions demands sustained scrutiny across mathematical design, security proofs, concrete parameters, and implementation code. Although large language mode"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Evaluating large batches of cryptographic submissions demands sustained scrutiny across mathematical design, security proofs, concrete parameters, and implementation code. Although large language model (LLM) agents have begun uncovering genuine flaws in public competitions, general-purpose coding agents remain brittle in cryptanalysis: they routinely miss implicit security notions and community conventions, drift outside the intended parameter or threat-model scope, and lose consistency across coupled proofs, complexity estimates, code, and prior literature. We present MechCrypto, a cryptanalytic research agent built on a persistent graph-structured framework. MechCrypto combines explicit task contracts, typed cross-artifact provenance, adaptively loaded cryptographic knowledge packs, and an independent verification gate that checks both evidential soundness and contract coverage before releasing reproducible artifacts. We evaluate MechCrypto blind on all 119 first-round candidates of the Next-generation Commercial Cryptographic Algorithms (NGCC) program (34 digital signatures, 41 key encapsulation mechanisms, 9 key exchange protocols, and 35 hash functions) without access to existing NGCC attack reports. The campaign with DeepSeek V4.1 Flash-1017 produces 115 comparable principal results, including 23 Critical findings. Against the 24 November 2026 public-results snapshot, MechCrypto achieves higher candidate-level severity on five submissions and identifies 57 principal findings whose underlying mechanisms have no matching public entry. Notably, for MEGASCON, MechCrypto derives an explicit, zero-search collision in the AVX-512 S-box compiled from Listing~3 of the specification, raising the candidate from the public tracker's High rating to Critical. Reports, proofs, code, and campaign data are available at https://github.com/MechMath/NGCC-results.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3050) | 2026-11-25
