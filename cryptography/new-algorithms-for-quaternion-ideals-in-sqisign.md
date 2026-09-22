---
title: "New algorithms for quaternion ideals in SQIsign"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2153"
summary: "Many isogeny-based schemes rely on the Deuring correspondance and thus require computations with quaternion ideals. In this paper, we generalize the recent results of Leroux on the inert representatio"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Many isogeny-based schemes rely on the Deuring correspondance and thus require computations with quaternion ideals. In this paper, we generalize the recent results of Leroux on the inert representation of quaternion ideals, yielding a normalized representation together with a set of simple and efficient algorithms for quaternion ideals in the context of the Deuring correspondence when the prime characteristic p is equal to 3 mod 4. One of the main benefit of our new algorithms is that the size of the integers involved in the computations is both easy to bound, and smaller than previous work. In particular, when applied to the latest version of SQIsign, our algorithms yield a concrete integer bound of O(p^4) in the worst case, proven under an experimentally verified assumption on the size of the integers required to perform the lattice reduction part of the response sampling. This bound improves upon all known previous bound by a factor at least O(p^2). Our new algorithms are used in the latest update of SQIsign's implementation submitted to the third round of the NIST call for additional post-quantum signatures. In particular, their low integer bounds facilitated the removal of a dependency on the GMP library in favor of a custom library of fixed-size integers without performance overhead. We stress that our algorithms are not limited to SQIsign, but apply to any isogeny-based cryptographic protocol that relies on the Deuring correspondence such as the PRISM signature scheme for instance.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2153) | 2026-09-22
