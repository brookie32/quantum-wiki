---
title: "Distributed SNARGs Resilient to Corrupt Verifiers"
date: "2026-09-17"
updated: "2026-09-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2068"
summary: "Distributed certification is a method for monitoring the correctness of a distributed system. The model consists of a centralized prover in addition to multiple verifiers lying on the nodes of a commu"
last_verified: "2026-09-19"
review_by: "2026-12-18"
stale: false
---

Distributed certification is a method for monitoring the correctness of a distributed system. The model consists of a centralized prover in addition to multiple verifiers lying on the nodes of a communication network, where the goal is to assert that the network satisfies a desired property. In doing so, the prover generates certificates for each verifier; the verifiers can then communicate in a small number of rounds, and accordingly accept or reject. The prover’s assertion is accepted if all verifiers accept. A significant body of work has gone toward developing and understanding limitations of distributed certification schemes, predominantly in the setting of information-theoretic soundness, and recently with computational soundness, achieving a form of distributed (locally verifiable) Succinct Non-interactive Arguments (SNARGs) (Aldema Tshuva et al, TCC 2023). As is standard in the model, soundness holds in existing constructions assuming that all verifiers in the network are honest. In this work, we introduce and explore the notion of robust distributed SNARGs (rdSNARGs) which retain (computational) soundness guarantees even when the cheating prover can collude with some nodes in the network. Addressing cheating verifiers presents several challenges. We construct rdSNARGs for any distributed language in P with succinct certificate size and communication from extended versions of RAM SNARGs (Kalai et al, STOC 2023), where the level of succinctness scales with the threshold of corrupt nodes. Complementarily, we demonstrate a lower bound showing that an rdSNARG with significantly smaller certificates and communication implies a SNARG for NP.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2068) | 2026-09-17
