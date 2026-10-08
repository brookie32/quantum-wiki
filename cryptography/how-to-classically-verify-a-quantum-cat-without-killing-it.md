---
title: "How to Classically Verify a Quantum Cat without Killing It"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.09282"
summary: "arXiv:2602.09282v2 Announce Type: replace Abstract: A quantum verifier decides membership in QMA using a (single) quantum witness state. This witness may be arbitrary, and no requirement is placed on "
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2602.09282v2 Announce Type: replace Abstract: A quantum verifier decides membership in QMA using a (single) quantum witness state. This witness may be arbitrary, and no requirement is placed on it beyond its acceptance probability. A protocol claiming to classically verify QMA should offer the same guarantee: any witness that would convince a quantum verifier should also suffice to convince a classical verifier. Unfortunately, existing classical verification of quantum computation (CVQC) protocols behave quite differently from the original QMA verifier: they require many copies of the witness and destroy every one, effectively demanding that the prover solve the hard problem of witness duplication before verification can begin. We build a protocol to classically verify QMA languages that uses a single copy of the prover's QMA witness. Whenever the original QMA verifier accepts that witness with overwhelming probability, our protocol has negligible completeness and soundness errors and returns the witness negligibly disturbed after interaction with an honest verifier. The soundness of our CVQC is based on the post-quantum Learning With Errors (LWE) assumption. As an intermediate step of independent interest, we introduce witness-preserving classical arguments for NP which enable provers that start out with a superposition over NP witnesses to convince a verifier without disturbing their superposition.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.09282) | 2026-10-08
