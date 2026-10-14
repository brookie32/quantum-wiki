---
title: "A Black-Box Compiler from Static to Dynamic SNARKs"
date: "2026-10-11"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2445"
summary: "Succinct Non-Interactive Arguments of Knowledge (SNARKs) for NP allow a prover to prove knowledge of a witness of an NP relation to a verifier with a short proof. The primary goal of a (static) SNARK "
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Succinct Non-Interactive Arguments of Knowledge (SNARKs) for NP allow a prover to prove knowledge of a witness of an NP relation to a verifier with a short proof. The primary goal of a (static) SNARK is to make verification cheap: the proof should be short, and the verifier's work should be minimal. However, recent work has also focused on making SNARKs more prover-efficient: cheap verification should ideally not come at the cost of large prover overhead. One avenue for achieving prover efficiency is via Dynamic SNARKs, which allow a prover to efficiently update the proof when the witness is updated. For example, one may use a SNARK to issue a proof of a query being performed correctly on a database, and then issue a new proof of the query once the database is updated. If these updates are small compared to the size of the witness (only a single entry of a large database is updated), then the prover should ideally be able to use the old proof to generate a new proof in time proportional to the distance between the old and the new witness. While some constructions of dynamic SNARKs for NP have been recently proposed by Wang et al. [Eurocrypt 2026] and Zhang et al. [Eurocrypt 2026], they have many limitations, such as lack of post-quantum security, dependence on a setup by a trusted third-party, and poor asymptotic and concrete efficiency. In this work, we present a compiler for constructing a dynamic SNARK for Plonkish constraints (which capture arbitrary NP computations) by using a static SNARK for NP and a vector commitment scheme as black boxes. When instantiated with a state-of-the-art hash-based SNARK and Merkle trees, the compiler yields a dynamic SNARK that is post-quantum secure in the QROM, has a transparent setup, and achieves O(n) initial prover time and O(k log^2 n) update prover time, with succinct proofs and verification, where k is the Hamming distance between the old and new instance-witness pairs. Our Ligerito-based implementation achieves cumulative prover speedups of 147imes and 11.7imes over a static HyperPlonk baseline for 10,000 successive one-gate updates and 1,000 successive 128-gate updates, respectively, on a 2^{23}-gate circuit, including the full dynamic initialization cost.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2445) | 2026-10-11
