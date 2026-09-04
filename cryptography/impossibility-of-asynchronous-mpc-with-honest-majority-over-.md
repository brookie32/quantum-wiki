---
title: "(Im)possibility of Asynchronous MPC with Honest Majority over Blockchains"
date: "2026-09-02"
updated: "2026-09-04"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1860"
summary: "This work studies asynchronous verifiable secret sharing (AVSS) and asynchronous multi-party computation (AMPC) in the blockchain-hybrid model, where parties have black-box access to an ideal (asynchr"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

This work studies asynchronous verifiable secret sharing (AVSS) and asynchronous multi-party computation (AMPC) in the blockchain-hybrid model, where parties have black-box access to an ideal (asynchronous) blockchain functionality providing only persistence and eventual liveness. Motivated by the practical deployment of MPC in blockchain applications such as privacy-preserving payments and threshold wallets, we investigate whether blockchain access can improve the classical resilience bound of n > 3t, where n is the total number of parties, and t is the number of parties that can be compromised by an adversary. In particular, in the blockchain-hybrid model, we provide a comprehensive set of lower and upper bounds across three cryptographic settings: (i) no trusted setup, (ii) trusted setup with Minicrypt assumptions, (iii) trusted setup with public-key assumptions. 1. We show that without a trusted setup, or under Minicrypt assumptions, even with a setup, the classical resilience bound for AMPC is inherent: AMPC is impossible for n leq 3t, even against weaker fail-stop or omission adversaries. 2. We establish separations between AVSS and AMPC in the intermediate regime 2t 2t without any setup. Moreover, against a Byzantine adversary, again unlike AMPC, AVSS is possible for n>2t under Minicrypt assumptions with a setup. 3. In contrast, under public-key assumptions with trusted setup, we construct an AMPC protocol tolerating Byzantine adversaries whenever n>2t. Our protocol leverages threshold homomorphic encryption, threshold signatures, commitments, and zero-knowledge proofs to minimize on-chain communication, achieving blockchain communication complexity independent of the circuit size. In the process, we define an efficient agreement on a common subset primitive for large messages in the blockchain-hybrid model, which can be of independent interest for secure distributed computing systems.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1860) | 2026-09-02
