---
title: "Lexicure: Efficient, Encrypted Lexical Search"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2182"
summary: "Lexical search retrieves documents containing query keywords that require exact matches, such as rare terms, entity names or codewords. Search is increasingly hosted in the cloud, which places both th"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

Lexical search retrieves documents containing query keywords that require exact matches, such as rare terms, entity names or codewords. Search is increasingly hosted in the cloud, which places both the corpus and every query on infrastructure the data owner does not control. Encrypted lexical search addresses this concern by ensuring no third party, including the cloud provider, learns which queries are issued or which documents are retrieved. The key binding constraints are all on the client — accuracy, memory, computation, and communication — since cloud capacity is elastic. Existing approaches that guarantee full privacy without caveats require prohibitively high client-side persistent storage or communication. We present Lexicure, a protocol for encrypted lexical search that reduces the search to arithmetic operations favorable to cryptographic primitives, such as encrypted matrix–vector products (EMVP). Across sixteen diverse datasets, Lexicure retains over 95% of plaintext BM25 accuracy on average. Lexicure sets a new baseline for leakage-free lexical search, requiring 2.6-9.9imes less communication than alternative approaches and less than 1KB of client-side storage. A major challenge is that secure lexical search is inherently bandwidth-bound. We additionally describe an approach for compressing the communication further in exchange for a larger server. To do so, we introduce a new cryptographic primitive that modifies EMVP to securely compute quadratic and higher-degree functions, more efficiently than a direct reduction. Lexicure demonstrates that leakage-free encrypted search with practical performance is achievable and opens new avenues for secure information retrieval systems.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2182) | 2026-09-23
