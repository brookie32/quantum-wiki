---
title: "Committing Security of Forkcipher-based AEAD"
date: "2026-10-14"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2479"
summary: "Authenticated Encryption with Associated Data (AEAD) provides confidentiality and integrity, but traditional security notions do not prevent ciphertexts from decrypting correctly under multiple keys. "
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

Authenticated Encryption with Associated Data (AEAD) provides confidentiality and integrity, but traditional security notions do not prevent ciphertexts from decrypting correctly under multiple keys. This motivates committing security, which requires ciphertexts to bind to their encryption inputs uniquely. Recent analyses revealed commitment failures in several forkcipher-based AEAD schemes, leaving open the question of whether these failures are inherent to forkciphers or design specific. We provide a comprehensive committing security analysis of existing forkcipher-based AEAD constructions, filling this gap by establishing both negative and positive results. Our analysis shows that while some designs inherently fail to achieve strong commitment, others achieve meaningful commitment guarantees, demonstrating that forkciphers can serve as a foundation for committing-secure AEAD schemes. We derive tight bounds for commitment notions for existing constructions. As a key technical contribution, we formalize a forkcipher-based hash construction and prove its collision resistance, which serves as a foundation for our security analysis.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2479) | 2026-10-14
