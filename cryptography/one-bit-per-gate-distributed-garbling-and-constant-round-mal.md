---
title: "One-Bit-per-Gate Distributed Garbling and Constant-Round Malicious MPC"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3052"
summary: "Distributed garbling, introduced by Beaver, Micali, and Rogaway (BMR), lets N mutually distrustful parties jointly run the garbling algorithm: as long as one of them is honest, the resulting garbled c"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Distributed garbling, introduced by Beaver, Micali, and Rogaway (BMR), lets N mutually distrustful parties jointly run the garbling algorithm: as long as one of them is honest, the resulting garbled circuit, together with its input, decoding, and authentication keys, satisfies the privacy and authenticity guarantees of the base garbling scheme, as if produced by a single trusted garbler. A long line of work has improved upon BMR, achieving malicious security against all-but-one corruptions and impressive concrete efficiency. However, these protocols all inherit the Ω(𝜆|C|) garbling size of Yao-style schemes, resulting in every garbler incurring Ω(𝜆) bits of communication per circuit gate. We present a distributed garbling protocol in which every garbler communicates an amortized one bit per gate, assuming Ring-LWE and constant-locality PRGs. It enjoys constant round complexity and is secure against a malicious adversary corrupting all but one garbler. Moreover, for sufficiently large circuits C (relative to their depth, input / output length and the security parameter), our garbling scheme and distributed protocols have the following efficiency features: • One bit per gate. The garbled circuit is |C|(1+o (1)) bits, as is each garbler’s total communication for generating and revealing it. • Distributing the garbler is almost free. Each garbler’s communication and computation exceed those of a single trusted garbler by only an additive o(|C|) term. • An efficient base scheme. Our one-bit-per-gate garbling scheme is itself lightweight: garbling is dominated by O(1) operations in the Ring-LWE ring per gate, plus a global computation dependent only on the depth, input, and output lengths of the circuit. Our protocol immediately gives constant-round maliciously secure MPC for any number of parties with per-party communication of one bit per gate, and removes the single point of failure in other applications of garbling, such as enabling distributed generation of ciphertexts in one-key functional encryption or distributed preprocessing in outsourced computation. Previously, for more than two parties, distributed succinct garbling was known only as a feasibility result via running generic MPC on succinct-time RAM garbling schemes, which rely on iO or similarly heavyweight tools and are prohibitively expensive computationally. Since other (more efficient) succinct garbling schemes are only succinct in size rather than time, running said schemes under generic MPC yields communication |C|poly(𝜆) as overhead from the latter.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3052) | 2026-11-26
