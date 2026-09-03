---
title: "Delegatable Anonymous Credentials from Legacy Credentials using Recursive zk-SNARKs"
date: "2026-09-01"
updated: "2026-09-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1855"
summary: "Digital identity systems are becoming increasingly prevalent, driven by regulatory efforts such as the European Digital Identity (EUDI) Wallet. Yet these systems usually do not achieve strong privacy "
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

Digital identity systems are becoming increasingly prevalent, driven by regulatory efforts such as the European Digital Identity (EUDI) Wallet. Yet these systems usually do not achieve strong privacy guarantees as offered by anonymous credentials, since they rely on standardized curves and widespread signature schemes like ECDSA that are incompatible with pairing-based primitives underpinning most anonymous credential constructions. Recent work bridges this gap by retrofitting such legacy credentials with anonymous-credential properties via zero-knowledge proofs, requiring no issuer-side modifications. However, none of these constructions supports delegation: the ability for users to pass on a restricted credential derived from their own to another party, while all parties along the delegation chain maintain full anonymity. Delegatable anonymous credentials (DACs) provide exactly these guarantees, but are likewise incompatible with existing deployments. We present the first DAC scheme built directly on top of legacy credentials. Our construction requires no issuance infrastructure changes, and yields constant-size credentials independent of delegation depth, with full unlinkability along the chain and selective attribute disclosure at every level. We instantiate it for credentials based on JSON Web Tokens (JWTs) signed with ECDSA using Plonky2 as the recursive proving backend, contributing a secure in-circuit JWT parser that closes vulnerabilities in prior work and a Plonky2 extension for cyclic recursion with per-step zero-knowledge. At 64 attributes, delegation takes 1.2 s and verification only 3.3 ms, with a constant proof size across all delegation levels

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1855) | 2026-09-01
