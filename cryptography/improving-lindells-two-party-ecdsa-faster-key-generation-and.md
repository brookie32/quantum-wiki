---
title: "Improving Lindell's Two-Party ECDSA: Faster Key Generation and UC Security Without Global Abort"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3028"
summary: "The two-party ECDSA signing protocol constructed by Lindell (CRYPTO '17) has a substantial implementation footprint across the blockchain industry. Despite its advantage of completely static state man"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

The two-party ECDSA signing protocol constructed by Lindell (CRYPTO '17) has a substantial implementation footprint across the blockchain industry. Despite its advantage of completely static state management, the protocol admits two main limitations: (1) its key generation phase is computationally intensive due to the usage of somewhat inefficient zero-knowledge proofs, and (2) its security relies on a "global abort" mechanism (requiring that if a certain error is detected then all current and future executions must halt), which poses significant operational challenges in high-throughput environments. In this work we demonstrate that these limitations are not inherent, presenting "drop-in" improvements that preserve the protocol's structure while delivering substantial gains in both efficiency and security: -- Faster key generation. We overcome the main bottleneck in the protocol's key generation by constructing a drastically improved zero-knowledge proof for the Paillier-EC discrete logarithm (PDL) relation. Utilizing aggregated inner-product arguments (Bulletproofs), we address the algebraic mismatch between Paillier encryption and elliptic curves by constructing a "commitment bridge" that links a Paillier ciphertext to a set of Pedersen commitments over an elliptic curve. This allows us to minimize Paillier operations by shifting the computational cost to significantly faster elliptic-curve operations. -- UC security without global abort. We augment the protocol with a highly efficient non-interactive zero-knowledge proof (integrated into the protocol's second message). We prove that this addition eliminates the need for a global abort mechanism, upgrading the protocol's security from its original game-based definition to UC security against malicious adversaries (under the Paillier and Strong RSA assumptions in the random oracle model). We provide rigorous security proofs and report on the performance of a production-grade implementation, demonstrating that our approach reduces the estimated key-generation time by a factor of approximately four and achieves UC security without global abort with minimal signing overhead: less than 22ms of additional computation per party and only 3.5KB of additional communication.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3028) | 2026-11-24
