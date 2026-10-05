---
title: "Three-Move Blind Signatures from DL"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2309"
summary: "This paper considers the problem of building blind signatures in pairing-free groups. We provide the first three-move blind signature which is provably one-more unforgeable, in the random-oracle model"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

This paper considers the problem of building blind signatures in pairing-free groups. We provide the first three-move blind signature which is provably one-more unforgeable, in the random-oracle model, under the minimal assumption that the discrete logarithm (DL) problem is hard. Our construction in fact achieves one-more strong unforgeability, and also supports partial blindness. Blindness is statistical, also in the ROM. Our construction makes black-box use of the underlying group and does not rely on non-black-box techniques. For most such constructions, three moves are necessary by a recent result of Dietz, Kastner, and Tessaro (CRYPTO '26). We build on recent work by Chairattana-Apirom, Reichle, and Tessaro (CRYPTO '26), which achieved the same combination of round complexity and security guarantees, but under the stronger decisional Diffie--Hellman (DDH) assumption. In particular, we follow the same paradigm of boosting the security of a weakly secure scheme (namely, the Okamoto--Schnorr blind signature) to a fully secure one by authenticating the initial nonce. We provide, however, a substantially different instantiation of this paradigm that dispenses with the use of DDH and establishes security from DL alone.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2309) | 2026-10-02
