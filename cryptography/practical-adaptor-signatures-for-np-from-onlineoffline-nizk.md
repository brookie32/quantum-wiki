---
title: "Practical Adaptor Signatures for NP from Online/Offline NIZK"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2155"
summary: "Adaptor signatures enable conditional payments on blockchain networks: a pre-signature is bound to a public instance Y and can be completed into a valid signature by any party knowing a witness y with"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Adaptor signatures enable conditional payments on blockchain networks: a pre-signature is bound to a public instance Y and can be completed into a valid signature by any party knowing a witness y with R(Y,y)=1, while the pre-signature and full signature together allow the signer to extract y. Existing constructions only support specific algebraically-structured relations, lose witness privacy, or have significant overhead both in signature size and computation. We present a practical adaptor signature framework for arbitrary NP relations, built from a new primitive we call Online/Offline NIZK whose proof is separated into online and offline parts. The key property is that the witness can be extracted from the online part knowing the randomness used in the offline part. We give two generic constructions: a basic scheme achieving witness hiding, and an instance-hiding scheme achieving a new, stronger forward-secure privacy notion we introduce. We instantiate our framework for the AES-128 relation using the VOLE-in-the-Head paradigm and the FAEST post-quantum signature scheme. The resulting complete signature is 11.6 kB, roughly 60% smaller than the state-of-the-art adaptor signature for NP (Ciampi et al., CT-RSA '25), and our implementation is an order of magnitude faster in overall signature generation, verification, and extraction.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2155) | 2026-09-22
