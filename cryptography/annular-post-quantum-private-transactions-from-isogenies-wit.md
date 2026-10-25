---
title: "ANNULAR: Post-Quantum Private Transactions from Isogenies with Recursive Batch Verification"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2596"
summary: "ANNULAR is a shielded pool built on isogeny-based primitives. Notes are committed in a Merkle tree and spent by nullifier with hidden amounts, following the structure of Zcash's Sapling, but every pri"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

ANNULAR is a shielded pool built on isogeny-based primitives. Notes are committed in a Merkle tree and spent by nullifier with hidden amounts, following the structure of Zcash's Sapling, but every primitive is post-quantum: spends are authorised by the prime-degree PRISM signature of Basso et al., note ciphertexts are keyed by the MIKE non-interactive key exchange, and each transaction carries a STARK proved natively over the isogeny field. The transaction proofs of a block are then folded into a single recursive proof. A ledger need record and verify only this one proof, 426 KB in 15 ms, whatever the batch holds, and check each transaction's two signatures alongside it. A transaction's body is the size of Sapling's at the same memo length (2,685 bytes against 2,756 with a 512-byte memo); its share of the batch proof adds under 500 bytes. A move to post-quantum primitives is generally expected to raise a pool's operating cost. We argue that the post-quantum change and the scaling change are complementary: with a STARK as the proof system, proofs fold, and with isogeny keys, the per-transaction data remains small. The cost moves to the sender, whose proof takes 1.4 s on sixteen cores, and to one aggregator per batch, which we measure: 1,248 transactions in 99 s on one GPU. Each proof in the tree carries 100 bits of round-by-round soundness and the batch about 90 under a union bound; under Fiat–Shamir that is the work an adversary needs. The constraints of the leaf circuit are proven in Lean 4 to encode the spend statement, while the soundness of the STARK itself rests on a paper argument. The scheme's claims rest on the signature's existential unforgeability; its strong unforgeability, argued by the construction's authors and not yet proved, is not relied on.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2596) | 2026-10-22
