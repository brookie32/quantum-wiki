---
title: "Indistinguishability Lifting for Keyed Oracles, Compressed Ideal Cipher, and More Applications"
date: "2026-10-03"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2324"
summary: "Cryptographic security proofs often involve an adversary interacting with a larger, keyed oracle that consists of (potentially exponentially) many independent instances of a smaller, base oracle. Exam"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Cryptographic security proofs often involve an adversary interacting with a larger, keyed oracle that consists of (potentially exponentially) many independent instances of a smaller, base oracle. Examples include ideal ciphers, which provide access to an independent random permutation for each key, and random oracles, which provide an independent random bit string for each input. However, showing quantum indistinguishability between two such keyed oracles can be tricky, since a single query made by an adversary may involve a superposition that covers all instances of the base oracles simultaneously. In this paper, we establish a generic indistinguishability lifting theorem of the following form: if the two base oracles are indistinguishable under quantum queries, then their corresponding keyed oracles are too, up to an O(q^2) multiplicative loss in distinguishing advantage, where q is the number of queries made by the adversary. Our lifting theorem applies to both statistical and computational settings, and to oracles that are stateful as well. It is also optimal in that it matches the obvious Grover search attack for a certain (contrived) choice of oracles. As an immediate application, we extend Carolan's compressed permutation oracle to an efficiently implementable compressed ideal cipher, and use it to prove preimage resistance of the Davies-Meyer compression function in the quantum ideal cipher model. Thanks to our lifting theorem, the soundness of our compressed ideal cipher reduces to that of Carolan's oracle, and any further improvement on the latter would automatically carry over to the former. As our second application, we give a modular construction that doubles the message length of any quantum-secure strong pseudorandom permutation. Along the way, we show that an existing two-round tweakable Feistel construction is indistinguishable from a random permutation under quantum bidirectional queries. This is done via a dedicated polynomial-method argument, which may be of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2324) | 2026-10-03
