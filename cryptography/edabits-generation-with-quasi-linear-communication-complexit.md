---
title: "Edabits Generation with Quasi-Linear Communication Complexity"
date: "2026-10-14"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2482"
summary: "The work of (Escudero et al., CRYPTO 2020) introduces the so-called edabits, which are defined as a secret sharing of an integer over an arithmetic domain, together with its bit decomposition secret s"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

The work of (Escudero et al., CRYPTO 2020) introduces the so-called edabits, which are defined as a secret sharing of an integer over an arithmetic domain, together with its bit decomposition secret shared over a binary domain. In the same work, it is shown how edabits can be used to securely evaluate advanced primitives such as comparison, bit decomposition, and truncation, which are essential building blocks in more complex applications such as privacy-preserving machine learning and beyond. Edabits are general and can be defined over any secret-sharing scheme or corruption model. Such flexibility, coupled with their wide range of applications, makes edabits a powerful target correlation. Escudero et al.~introduced a protocol to generate edabits that works in the arithmetic black-box (ABB) model, that is, it is agnostic to the concrete secret-sharing scheme and even works both for fields F_p and rings Z_{2^ell}, as well as both for honest majority t0. This includes the honest majority case t<n/2, but also dishonest majority with an (arbitrarily small) constant fraction of honest parties. Our result is achieved via novel applications of randomness extraction methods, as well as better edabit aggregation for the binary components. Along the way and of independent interest, we improve the communication complexity of dabit generation (dabits are bits shared in both binary and arithmetic domains) from Omega(n^2ell) bits achieved in (Rotaru and Wood, INDOCRYPT 2019), to linear O(nell) bits.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2482) | 2026-10-14
