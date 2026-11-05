---
title: "Leakage-Resilient Computation via Matrix Refreshing"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2741"
summary: "Leakage-resilient cryptography protects secrets against side-channel attacks, in which a physical implementation reveals partial information about its internal state. A fundamental primitive in this a"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Leakage-resilient cryptography protects secrets against side-channel attacks, in which a physical implementation reveals partial information about its internal state. A fundamental primitive in this area is a leakage-resilient storage, which allows a secret to be stored in a way that remains secure even if an adversary learns some information about the storage's internal state. A popular approach represents a secret as the inner product of two n-bit vectors, called shares. The shares are stored and processed separately by two parts of the implementation, called the left and right parties. Because leakage accumulates over time, the shares must be refreshed repeatedly. We prove that a simple refresh, in which the left party multiplies its share by a uniform invertible matrix M and the right party multiplies its share by M^{-1}, is secure under continual local leakage. After T refreshes, each allowing at most lambda bits of leakage per party, the transcripts for two stored secrets are at statistical distance at most Cdot Tdot 2^{6lambda-n/9} for an absolute constant C. We also obtain a Boolean-circuit compiler with statistical privacy error at most Cdot Sdot 2^{18lambda-n/27} for S operations and at most lambda bits of local leakage per party per operation. The guarantee covers repeated stateful evaluations with adaptively chosen public inputs, with S counting all operations across invocations. Thus, for polynomial-size circuits, a constant leakage fraction is tolerated with share length depending only on the security parameter. We formalize the refreshing bound, the composition and compiler guarantees, and the expected-work bounds in Lean 4. Our results also provide efficient simulation: the leakage can be reproduced from the public inputs and the circuit outputs alone, with expected polynomial overhead.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2741) | 2026-11-03
