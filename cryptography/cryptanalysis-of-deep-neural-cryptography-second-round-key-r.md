---
title: "Cryptanalysis of Deep Neural Cryptography: Second Round Key Recovery on the Unprotected Implementation and a Floating-Point Attack on the Protected Implementation of AES"
date: "2026-09-08"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1919"
summary: "At EUROCRYPT 2026, Gérault et al. introduced natural DNN implementations of block ciphers: ReLU networks that agree exactly with the underlying cipher on binary inputs but extend it continuously to re"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

At EUROCRYPT 2026, Gérault et al. introduced natural DNN implementations of block ciphers: ReLU networks that agree exactly with the underlying cipher on binary inputs but extend it continuously to real-valued inputs. They showed that this extension exposes the first round key to recovery, and proposed a generic Secure Blackbox Transformation that turns an arbitrary DNN-based implementation into a provably secure implementation. We revisit both sides of their result. On the attack side, the known attacks on the unprotected implementation reach only the first round key. Under the same threat model, we refine the absorption property of the natural S-box and combine it with a chosen-plaintext collision test, validated empirically, to recover the second round key of AES-256 in about 2^{39} queries. On the defense side, their transformation is provably secure over the reals, but that guarantee does not carry over to finite precision, where any neural-network implementation must ultimately run. We give a floating-point attack that recovers the first round key of the protected AES-128 implementation in 128 chosen queries, driven by an input value that the defense fails to round to a bit. Such a value exists in bfloat16, float16, float32, and float64, so moving to higher precision does not remove the weakness. We confirm the recovery in all four formats. Finally, we block the attack with a clamp placed before that rounding step, which keeps every finite input in [0,1] in the working precision and changes neither the cipher nor the exact-real security guarantee. Whether a finite-precision security guarantee can be established for the construction as a whole remains open.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1919) | 2026-09-08
