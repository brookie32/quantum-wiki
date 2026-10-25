---
title: "Tritone: Pairwise Garbled Disputes for Multi-Party Proof Verification on Bitcoin"
date: "2026-10-23"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2612"
summary: "Bitcoin Script lacks native pairing operations for efficient direct verification of Groth16 proofs. Conventional federated bridges instead authorize withdrawals through a signing quorum, whose collusi"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Bitcoin Script lacks native pairing operations for efficient direct verification of Groth16 proofs. Conventional federated bridges instead authorize withdrawals through a signing quorum, whose collusion can release funds without valid evidence. We present the Tritone protocol, which lets Bitcoin enforce the outcome of verifying a Groth16 proof for an NP relation fixed in a one-time trusted setup, with the locked funds secure as long as one of a fixed set of N operators is honest. Verification is optimistic and off-chain, and every transaction is standard under current relay policy, so Tritone runs on Bitcoin today without consensus changes. Tritone generalizes the two-party BABE protocol to a fixed committee of N operators, with one dispute instance per ordered pair. Cut-and-choose protects against malicious garblers, while Feldman verifiable secret sharing correlates input keys across candidates. Our new Lamport-adaptor gadget forces a challenging verifier to disclose the shares selected by the prover's committed proof element, providing the transaction-level binding left unspecified by BABE. A single set of disclosed shares then unlocks all retained candidates. We formalize the multi-party primitive, prove the protocol secure against up to N-1 statically corrupted operators, and specify its complete pre-signed transaction graph. We implement Tritone in Rust. On Bitcoin mainnet, when one verifier disputes a claim at every stage, the prover-candidate posts 9,607 vB and the verifier 18,160 vB of protocol transactions. In local benchmarks at 40-bit statistical security, the prover-candidate of each dispute instance retains as little as 112.83 MiB. Tritone thus replaces trust in a signing quorum with a single-honest-operator assumption wherever locked bitcoin is released to an operator against a Groth16 proof, with Bitcoin bridges as our showcase.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2612) | 2026-10-23
