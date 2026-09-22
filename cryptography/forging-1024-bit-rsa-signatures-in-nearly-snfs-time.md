---
title: "Forging 1024-bit RSA signatures in nearly SNFS time"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2131"
summary: "The security of RSA is generally understood to be based on the complexity of factoring, and key size parameters are extrapolated from the general number field sieve (GNFS). However, this may not accur"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

The security of RSA is generally understood to be based on the complexity of factoring, and key size parameters are extrapolated from the general number field sieve (GNFS). However, this may not accurately represent RSA security in practical scenarios. An under-appreciated 2007 algorithm of Joux, Naccache, and Thomé allows an attacker to forge RSA signatures after temporary access to a raw RSA signing/decryption oracle in time close to the *special* number field sieve (SNFS) without factoring the key. We implement and run this algorithm for 1024-bit RSA. In total, the attack took 1380 CPU core-years over five calendar months, and made 2^{32} oracle queries. Most of this time is precomputation; after the precomputation the attacker can forge any signature of choice, offline, in 180 core-years. We carried out our attack using a hardware security module (HSM) as the signing oracle, thus demonstrating the ability to impersonate the HSM through black-box API interactions, without exfiltrating the key. Blind RSA schemes also provide such a signing oracle. Extrapolating our empirical running times to larger key sizes, we conclude that the concrete security of RSA with a signing oracle should be 15 to 30 bits lower than the factoring-based security estimates for the 1024-bit to 4096-bit RSA parameters that are common in practice. Even 4096-bit RSA does not appear to meet a 128-bit security level in this attack model. This highlights a gap in current RSA-type security assumptions, and gives classical cryptanalytic evidence in favor of moving away from RSA entirely during the current post-quantum transition.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2131) | 2026-09-20
