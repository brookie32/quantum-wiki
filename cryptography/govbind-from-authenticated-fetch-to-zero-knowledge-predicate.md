---
title: "GovBind: From Authenticated Fetch to Zero-Knowledge Predicate over Government Documents"
date: "2026-09-24"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2206"
summary: "Government portals often issue PDF certificates whose provenance can be verified only through a live HTTPS verification service. Proving a limited fact from such a document therefore commonly requires"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Government portals often issue PDF certificates whose provenance can be verified only through a live HTTPS verification service. Proving a limited fact from such a document therefore commonly requires disclosing the complete document or giving the verifier access to the portal. We present GovBind, a protocol that combines zkTLS provenance with a zero-knowledge content proof, without requiring the issuer to modify its service or embed an independently verifiable signature. A baseline construction binds both stages through a commitment to the complete response body. To make client-side proving feasible for compressed PDFs, an optimized construction instead commits separately to private ranges, discloses the remaining bytes, requires their exact partition, and opens the claim-bearing compressed stream in a document profile-specific proof that constrains DEFLATE decompression. We formalize GovBind with game-based definitions of correctness, soundness, and privacy, where soundness jointly captures authenticity, content validity, and binding, and we prove both constructions secure relative to the explicit leakage and trust assumptions of Proxy-mode TLSNotary. Our prototype supports proofs of no overdue tax debt, bounded traffic penalties, and residence city over documents returned by the Turkish government verification service, e-Devlet. Across 72 generated proofs in 24 sessions, end-to-end generation took 54-119 seconds, verification took 44-127 milliseconds, and proofs were 11-12 KiB.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2206) | 2026-09-24
