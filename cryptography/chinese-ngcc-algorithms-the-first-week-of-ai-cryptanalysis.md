---
title: "Chinese NGCC Algorithms: The First Week of AI Cryptanalysis"
date: "2026-09-29"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2266"
summary: "On September 20, 2026, the Chinese Institute of Commercial Cryptography Standards published the 119 first-round candidates of its Next-generation Commercial Cryptographic Algorithms (NGCC) program: 34"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

On September 20, 2026, the Chinese Institute of Commercial Cryptography Standards published the 119 first-round candidates of its Next-generation Commercial Cryptographic Algorithms (NGCC) program: 34 signature schemes, 41 key encapsulation mechanisms, 9 key exchange protocols, and 35 hash functions. The program follows the template of the open NIST competitions for AES, SHA-3, and post-quantum cryptography. It opened just after cryptographers' ``Lee Sedol moment'' in the summer of 2026, when AI analysis overtook humans in analyzing the HAWK signature scheme. During the first 7 days of the NGCC competition, according to our harvested sources, 191 active findings were published for 89 candidates, 78 of them rated Critical: universal forgeries, signing-key recovery, trivial hash collisions, broken implicit rejection, and seeds too short for the claimed security level. Our independent evaluation effort discovered, verified, and disclosed 110 of those issues (47 Critical) using the agentic workflow described in this work; outside researchers, some AI-assisted, found the rest. Early AI-assisted findings mostly concerned implementations; by the end of the week, reproduced AI-assisted attacks also included new design-level key recovery. We describe the workflow, review loop, classification ruleset, and observed failure modes. As part of the evaluation, we also benchmarked all algorithm candidates and found that NGCC hash selection may significantly affect final public-key performance, as candidate implementations spend a large share of their cycles on ``placeholder'' hashes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2266) | 2026-09-29
