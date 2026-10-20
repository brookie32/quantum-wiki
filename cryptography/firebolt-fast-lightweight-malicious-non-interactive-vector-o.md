---
title: "Firebolt: Fast, Lightweight, Malicious Non-Interactive Vector-OLE"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2549"
summary: "We introduce a new maliciously-secure vector oblivious linear evaluation (VOLE), building upon a recent construction of (semi-honest) Paillier-based non-interactive VOLE. Our protocol is non-interacti"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

We introduce a new maliciously-secure vector oblivious linear evaluation (VOLE), building upon a recent construction of (semi-honest) Paillier-based non-interactive VOLE. Our protocol is non-interactive (the sender can adaptively reveal entries of the VOLE using a single message to the receiver) and enjoys low communication (535 bytes for each VOLE entry) and low computation (around 5ms per party, single-threaded). Our protocol can be used as a drop-in replacement for less efficient VOLEs used in a variety of threshold schemes. We exemplify it by devising a new concurrently-secure two-round two-party ECDSA protocol that significantly improves over the state of the art. Along the way, we introduce several new strategies for proving shortness of plaintexts in Paillier ciphertexts or integer commitments, and we devise a modular framework for building threshold-ECDSA in a VOLE-hybrid model with concurrent security without requiring the use of (typically less efficient) UC-secure VOLE. All of these contributions are of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2549) | 2026-10-19
