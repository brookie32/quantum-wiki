---
title: "Aggregation techniques for the SPoCK scheme"
date: "2026-11-27"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3074"
summary: "In preceding work, we formalized a novel cryptographic primitive called Specialized Proof of Confidential Knowledge (SPoCK). The SPoCK scheme allows any two independent parties to convince a third par"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

In preceding work, we formalized a novel cryptographic primitive called Specialized Proof of Confidential Knowledge (SPoCK). The SPoCK scheme allows any two independent parties to convince a third party that they possess a common secret without revealing it. The proof is non-interactive, bound to the specific party that generated it, and cannot be forged without knowledge of the secret. A SPoCK scheme can be used in systems where members must independently attest to knowledge of a shared secret. One such application is addressing the Verifier’s Dilemma in distributed systems. While the original scheme works with two provers and a single secret, this work introduces new proving and verification schemes with multiple provers and multiple secrets. These schemes improve scalability in distributed systems with numerous participants by reducing proof size and verification time. We define the new Multi-SPoCK scheme, which allows two sets of provers to convince a verifier that they generated proofs from the same secret. Additionally, we propose the Aggregate Multi-SPoCK scheme, which further aggregates proofs from multiple secrets into a single proof. We first formalize the multi-proving schemes and their security model. We then give new pairingbased constructions of both schemes from BLS multisignatures. We provide proofs for the proposed schemes under suitable computational assumptions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3074) | 2026-11-27
