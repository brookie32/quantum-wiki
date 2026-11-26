---
title: "Merkle Trees Minimize Verifier Complexity in the ROM"
date: "2026-11-24"
updated: "2026-11-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3015"
summary: "Nearly five decades after their introduction, Merkle trees remain the most efficient hash-based vector commitments. They compress a vector x in {0,1}^n into a commitment whose size is independent of n"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

Nearly five decades after their introduction, Merkle trees remain the most efficient hash-based vector commitments. They compress a vector x in {0,1}^n into a commitment whose size is independent of n, such that a verifier can open any bit x_i using log n hash evaluations. The security of the scheme (intractability of finding two distinct openings for a given bit using the same commitment) follows from the collision resistance of the hash function. The verifier's runtime complexity is a bottleneck in many key applications of vector commitments, including SNARKs, credentials, and authenticated dictionaries. As such, a longstanding open question has been whether it is possible to construct hash-based vector commitments where the verifier makes a sublogarithmic number of hash evaluations. We prove that sublogarithmic verifier complexity is impossible to achieve through black-box use of a hash function; we not only rule out constructions from collision resistant hash functions, but in fact show that commitment schemes with sublogarithmic verifier complexity are unachievable in the random oracle model. In particular, any vector commitment with deterministic verifiers has verifier query complexity Omega_{heta}(log n), where heta is the input length of the random oracle. This bound is matched up to constant factors by high-arity Merkle trees. The key technical lemma in our proof is a disjoint product lemma, which can be viewed as a computational analog of the van den Berg-Kesten-Reimer (BKR) inequality. We believe this lemma is of independent interest, and in particular may be useful for showing other lower bounds and separations in the random oracle model.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3015) | 2026-11-24
