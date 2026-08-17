---
title: "Concurrently Secure Compact Blind Signatures from Module-SIS"
date: "2026-08-14"
updated: "2026-08-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1690"
summary: "A blind signature scheme allows a user to interact with a signer to obtain a valid signature on a message, while ensuring that the signer cannot learn any information on the message being signed, nor "
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

A blind signature scheme allows a user to interact with a signer to obtain a valid signature on a message, while ensuring that the signer cannot learn any information on the message being signed, nor link a given couple message-signature to the specific interaction that produced it (blindness). In round-optimal (i.e., two-move) blind signature schemes, a user sends a request (typically a commitment) for a message, and the signer responds with a signature. To achieve blindness, the resulting blind signature usually consists of a zero-knowledge proof of knowledge of a valid signature from the signer on a request. This reliance on zero-knowledge proofs has become the main bottleneck in reducing the blind signature size. In particular, state-of-the-art lattice-based blind signature schemes are instantiated based on the zero-knowledge proof system from [Lyubashevsky et al., EUROCRYPT, 2022], which results in blind signatures of at least 22 KB. In this work, we carefully design a blind signature protocol following the classical lattice-based Σ-protocol as in [Ducas et al., CRYPTO, 2013], so that the last component naturally forms a short preimage of the hash of the message, as a classical GPV signature. As a result, this removes the need for zero-knowledge proofs in the blind signature. Eventually, this design allows us to obtain a significantly more compact blind signature of size 4.7 KB, with concurrent security under the Module-SIS assumption. As a trade-off, our protocol may require more than one round with small probability, due to the rejection sampling in lattice-based Σ-protocols. Under our proposed parameters, however, the expected number of rounds for honest users can be as small as 1.1, which is very close to optimal. To minimize the number of rounds, we require users to prove that they failed to derive a blind signature in the previous round, before starting a new one. This technique yields a moderately looser bound on the expected number of rounds for malicious users, who will be forced to terminate in at most 2.6 rounds.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1690) | 2026-08-14
