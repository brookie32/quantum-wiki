---
title: "Lower Bounds on Random-Oracle-Model Signature Length"
date: "2026-09-27"
updated: "2026-09-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2237"
summary: "Hash-based signatures offer a conservative foundation for post-quantum authentication, but their large signatures impose substantial communication and storage costs. For security parameter lambda, dis"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

Hash-based signatures offer a conservative foundation for post-quantum authentication, but their large signatures impose substantial communication and storage costs. For security parameter lambda, discrete-logarithm-based signatures have length O(lambda), while known hash-based constructions have quadratic signature length, up to logarithmic factors, even for one-time signing. Is this gap inherent? We prove what are, to the best of our knowledge, the first lower bounds on the length of signature schemes in the (pure) random oracle model. Our bounds apply to schemes with non-adaptive verifiers and a natural security property called salted soundness: a scheme with such security is unforgeable even against an adversary that is granted a limited ability to resample and restore oracle answers. This class essentially captures all known hash-based constructions (possibly after low-cost modifications). We show that the combined public-key and signature length of a one-time signature scheme must be Omega(lambda^2/loglambda). For many-time signatures, we prove the stronger conclusion that the signature length alone must satisfy the same lower bound, irrespective of the public-key length. More precisely, if the relevant length is o(lambda^2/loglambda), then an adversary making 2^{o(lambda)} random-oracle queries breaks salted soundness with inverse-polynomial probability. Our proof uses the high-entropy hitting lemma of Haitner, Nukrai, and Yogev (Crypto 22) to transform a short signature scheme into a scheme whose verifier makes only a few queries. We then apply the Barak and Mahmoody-Ghidary (FOCS 07) attack on one-time signatures with a low-query verifier. Balancing these two steps yields the near-quadratic lower bounds.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2237) | 2026-09-27
