---
title: "Secure Compilation of Probabilistic Side-Channel Countermeasures"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2510"
summary: "Probabilistic countermeasures are a common means of protecting programs against side-channels. These countermeasures are hard to implement and are routinely broken by compilers. Proving that a compile"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

Probabilistic countermeasures are a common means of protecting programs against side-channels. These countermeasures are hard to implement and are routinely broken by compilers. Proving that a compiler preserves probabilistic side-channel security directly would require reasoning about perfect simulatability of distributions, a challenging technique normally reserved for high-assurance cryptography in frameworks like EasyCrypt and out of scope for compiler correctness. In this paper, we present a language- and leakage-model-agnostic framework for provably secure compilation of probabilistic side-channel security notions. Our main contribution is formalizing a deterministic leakage-preservation relation that implies preservation of probabilistic security notions, including d-NI and d-SNI for masking and cryptographic constant-time. Our framework establishes the same guarantees without probabilistic proof obligations, reducing preservation to a per-pass simulation argument on deterministic traces. We use the Rocq proof assistant to prove that a model of the core pipeline and several optimizing passes of the Jasmin compiler preserve security in the value-probing model with glitches. We also show how to harden against transition leakage with lightweight annotations at the source level. On top of this, we build libmasking, an open-source library of arbitrary-order masked gadgets in Jasmin that securely compiles to ARM and RISC-V assembly, provides C language bindings, and is benchmarked on real hardware. Together, these contributions are a step towards programming environments in which masked code is written or generated, verified at the source level, optimized, and compiled without breaking security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2510) | 2026-10-16
