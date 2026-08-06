---
title: "Design and Analysis of Quantum Designated Verifier Signature Scheme"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1603"
summary: "Designated Verifier Signatures (DVS) are an important variant of digital signatures that ensure only a specified verifier can validate a signature, while preserving non-transferability. With the adven"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Designated Verifier Signatures (DVS) are an important variant of digital signatures that ensure only a specified verifier can validate a signature, while preserving non-transferability. With the advent of quantum computing, several quantum DVS schemes have been proposed to achieve quantum security. In this paper, we revisit the quantum DVS protocol of Xin et al. [Quantum Information Processing, 2022] and provide a structural cryptanalysis of its design. We show that the scheme admits an existential forgery under a chosen-message attack: given a valid quantum signature on one message, an adversary can efficiently transform it into a valid signature on another message without knowledge of the signer’s private key. To address this weakness, we propose a minimal countermeasure based on QKD-derived keys and quantum one-time pad encryption.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1603) | 2026-08-04
