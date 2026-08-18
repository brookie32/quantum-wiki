---
title: "Post-Quantum TLS Migration: A Systematization of Hybrid Handshakes, PSKs, KeyUpdate, and Certificate Strategies"
date: "2026-08-16"
updated: "2026-08-18"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1703"
summary: "Post-quantum migration of Transport Layer Security (TLS) is often described as replacing a classical key-exchange algorithm with a post-quantum alternative. This framing is incomplete: TLS distributes"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

Post-quantum migration of Transport Layer Security (TLS) is often described as replacing a classical key-exchange algorithm with a post-quantum alternative. This framing is incomplete: TLS distributes security across key establishment, authentication, resumption and pre-shared keys (PSKs), traffic-secret evolution, and the X.509/PKIX ecosystem. These functions have different security objectives, failure modes, lifecycle dependencies, and deployment constraints. This Systematization of Knowledge (SoK) develops a functional framework for analyzing post-quantum TLS migration as an architectural problem rather than a single algorithm transition. We systematize classical, pure post-quantum, and hybrid key establishment; TLS 1.3 PSK modes and resumption; KeyUpdate; ML-KEM; ML-DSA and SLH-DSA; hybrid and composite authentication; X.509/PKIX and trust-anchor migration; HSM dependencies; interoperability; performance; deployment environments; cryptographic inventory; and crypto-agility. We classify evidence by mechanism, security objective, source of keying material, forward-secrecy behavior, quantum threat, post-compromise behavior, communication and computational cost, interoperability dependency, standardization status, deployment evidence, and migration complexity. We explicitly separate finalized standards from evolving Internet-Drafts and implementation-specific evidence. The systematization produces four analytical conclusions. First, confidentiality migration and authentication migration are coupled operationally but distinct security programs. Second, hybrid ECDHE-ML-KEM is a strong transitional architecture for confidentiality migration when the relevant TLS integration and implementation support are available, because its security objective can tolerate failure of one component; the exact security claim nevertheless depends on the standardized construction and its assumptions. Third, PSKs, resumption, and KeyUpdate are not interchangeable forms of rekeying: their security depends on the provenance and role of the secret, while KeyUpdate remains within an existing traffic-secret lineage and does not create an independent post-quantum secret. Fourth, deployment readiness is constrained as much by certificates, trust stores, HSMs, middleboxes, inventory, and interoperability as by primitive availability. We therefore derive a migration decision framework that prioritizes HNDL-sensitive data, controlled hybrid deployment, interoperability testing, staged authentication and PKI migration, and observable retirement of classical-only mechanisms.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1703) | 2026-08-16
