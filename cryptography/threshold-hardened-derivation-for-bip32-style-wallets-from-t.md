---
title: "Threshold Hardened Derivation for BIP32-Style Wallets from the Hydra PRF"
date: "2026-11-22"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2986"
summary: "BIP32 hardened key derivation computes HMAC-SHA512 on the parent private key and chain code. In a threshold wallet these are secret-shared, so the hash must be evaluated inside a multi-party computati"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

BIP32 hardened key derivation computes HMAC-SHA512 on the parent private key and chain code. In a threshold wallet these are secret-shared, so the hash must be evaluated inside a multi-party computation. We present a hardened derivation that replaces HMAC-SHA512 by the arithmetization-oriented PRF Hydra. Once the PRF output is serialized, every remaining step is BIP32's; the derived keys still differ from BIP32's, so the scheme is a sibling of BIP32 and not wire-compatible with it. Both parent secrets form the PRF key, only public data enters its input, and every hardened child stays secret-shared and can derive further. We prove parent--child hiding, sibling independence, and hardened-child unlinkability by one path hybrid. Because the parent key is both part of the PRF key and BIP32's additive offset, the proofs need an offset-PRF assumption, which the published PRF claim of Hydra does not imply. The threshold protocol is proved UC-secure in the arithmetic-black-box model against static semi-honest adversaries, and with abort against static malicious ones, with no assumption on the PRF. With five parties under MP-SPDZ's malicious Shamir protocol, which our proofs do not cover, one derivation needs 243 rounds and 0.33s, against 15226 rounds and 3.3s for HMAC-SHA512; at 10ms round-trip time, this becomes 1.9s against 91s.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2986) | 2026-11-22
