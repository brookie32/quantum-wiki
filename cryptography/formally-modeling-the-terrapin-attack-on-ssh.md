---
title: "Formally Modeling the Terrapin Attack on SSH"
date: "2026-09-22"
updated: "2026-09-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2158"
summary: "The Terrapin attack against SSH channel integrity (USENIX Security 2024) used a novel attack vector: attacks on the channel state. Surprisingly, not all AEAD modes of SSH were equally affected by this"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

The Terrapin attack against SSH channel integrity (USENIX Security 2024) used a novel attack vector: attacks on the channel state. Surprisingly, not all AEAD modes of SSH were equally affected by this attack, and it remained an open question if "unaffected" meant "secure". Existing formal models for secure channels are based on stateful encryption. However, these models do not define what the channel state is and how it is used as input to the different AEAD modes. In this paper, we propose a formal model for channel integrity under partially chosen state. Applied to the Terrapin attack, the chosen state is the SSH sequence number. It uses an abstract stateful encryption interface, for which we provide pseudocode descriptions for the eight most prominent AEAD modes used in SSH. By varying the SND oracle, we can model ciphertext-only (CO; the Terrapin attack), known-plaintext (KPA), and chosen-plaintext (CPA) attacks. This allows us to establish concrete bounds on the security of the AEAD modes. We find that all three Encrypt-then-MAC (EtM) modes and ChaCha20-Poly1305 in SSH are insecure in the CO model. AES-GCM is the only cipher secure in all three model variants. Going beyond Terrapin, we show that Encrypt-and-MAC (EaM) with a CBC cipher is secure, even in the KPA model. In particular, we describe a novel BEAST-like chosen-plaintext attack on the channel integrity of EaM-CBC, which separates the KPA and CPA models for this scheme.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2158) | 2026-09-22
