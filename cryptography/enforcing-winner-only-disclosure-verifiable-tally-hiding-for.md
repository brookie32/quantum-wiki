---
title: "Enforcing Winner-Only Disclosure: Verifiable Tally Hiding for Weighted DAO Governance"
date: "2026-08-22"
updated: "2026-08-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1773"
summary: "Token-weighted voting is widely used in DAO governance, but public voting weights together with weighted tallies can reveal identifiable voters' choices. Publishing only the final outcome reduces this"
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

Token-weighted voting is widely used in DAO governance, but public voting weights together with weighted tallies can reveal identifiable voters' choices. Publishing only the final outcome reduces this disclosure, yet an output policy alone does not prevent a privileged participant from reconstructing the exact weighted tally during computation. We present a verifiable winner-only tally-hiding construction for weighted binary voting. Registered weights are bound to credentials in zero-knowledge ballots, while weighted contributions remain encrypted through aggregation and comparison against a public threshold. The blockchain adjudicates ballots, an off-chain backend performs the encrypted computation, and exact ciphertext and transcript bindings allow any public verifier to check that the published outcome corresponds to the accepted ballots. The only tally-derived plaintext output is the outcome bit. The construction is parameterized by electorate size and contribution width; our prototype and formal transcript-privacy result deliberately study a bounded eight-voter, eight-bit instance with 134 encrypted gates and an actual three-of-five final release. For honest execution by all five trustees, we prove passive-public-observer backend transcript privacy from the accepted ciphertexts and outcome alone. Privacy against malicious sub-threshold trustees remains open.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1773) | 2026-08-22
