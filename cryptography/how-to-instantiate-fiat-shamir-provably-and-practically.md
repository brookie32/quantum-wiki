---
title: "How to instantiate Fiat-Shamir Provably and Practically?"
date: "2026-09-19"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2114"
summary: "We propose a new variant of the Fiat–Shamir transformation where the Fiat-Shamir hash is instantiated by an external verifiable random function (VRF) service. We prove that soundness holds as long as "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

We propose a new variant of the Fiat–Shamir transformation where the Fiat-Shamir hash is instantiated by an external verifiable random function (VRF) service. We prove that soundness holds as long as the VRF secret key remains hidden from the prover, i.e., assuming no collusion between the prover and the VRF evaluator. Crucially, due to the public verifiability of VRF outputs, the VRF computation itself need not be trusted beyond the key-generation phase. This yields the first NIZK compiler in a non-idealized model that is both practical and provably sound. Our transformation can be instantiated using extensively deployed blockchain-based VRF services. Moreover, it naturally supports distributed VRF services, allowing the no-collusion assumption to be relaxed: soundness holds even if the prover colludes with up to a threshold number of evaluators. In this setting, distributed key generation for the VRF further eliminates trust in the setup. A distinctive feature of our approach is that the verification step is local and does not require accessing the VRF. This is particularly advantageous for recursive proof systems such as incrementally verifiable computation, where the verification circuit must be embedded within the circuit for which a proof needs to be generated. This enables construction of the first provable and practical recursive proof -- bypassing well-known impossibilities in the random oracle model. We demonstrate the real-world utility of our framework with an implementation for the GKR protocol.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2114) | 2026-09-19
