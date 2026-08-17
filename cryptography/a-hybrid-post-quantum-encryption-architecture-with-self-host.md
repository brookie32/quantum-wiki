---
title: "A Hybrid Post-Quantum Encryption Architecture with Self-Hosted Key Management for SME Cloud Data Protection"
date: "2026-08-14"
updated: "2026-08-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1689"
summary: "Harvesting ciphertext from cloud storage needs no quantum computer; decrypting it later does. That gap is the harvest-now-decrypt-later exposure: anything protected by RSA or ECDH today that must stay"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

Harvesting ciphertext from cloud storage needs no quantum computer; decrypting it later does. That gap is the harvest-now-decrypt-later exposure: anything protected by RSA or ECDH today that must stay secret for decades is already compromised. Small and medium-sized enterprises are least able to respond: they neither run the infrastructure on which their data sits on nor employ a cryptographer. Bespoke migration suits firms with security budgets; a managed key service relocates trust rather than removing it. The obstacle is architectural, not cryptographic. We present Quantum Cloud Guard (QCG), a software-only three-layer architecture. No prior SME-oriented system combines its three elements: client-side hybrid post-quantum encryption, self-hosted key custody with client-verifiable ML-DSA-87 signatures on served keys, and an integrated application-layer abuse-prevention gateway. Files never leave the client: each is sealed under AES-256-GCM, its key wrapped to an ML-KEM-1024 public key from the enterprise’s key service. The enterprise alone administers it; it signs every key with ML-DSA-87, so a client that pinned it detects substitution. Separating key custody from data custody is the point: a provider holding both can read the data. On a 24 MHz STM32F407, ML-KEM-1024 key generation takes 40.8 ms and decapsulation 44.0 ms; on the server every post-quantum operation stays sub-millisecond, signing adding 0.24 ms per request. The service runs on a 4.49 EUR/month virtual server. Under sustained flooding, the in-process gateway Sentinel Gate rejected 98.8% of attack traffic while a legitimate client’s median latency moved from 621 to 625 ms. Being single-source, this shows filtering effectiveness, not DDoS resilience.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1689) | 2026-08-14
