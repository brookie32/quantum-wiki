---
title: "Zippel: A Language, Compiler, Runtime, and Analyzer for ZK Proof Systems"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2517"
summary: "This paper introduces Zippel, a language, compiler, runtime, and analyzer for cryptographic proof systems. Zippel lets developers write proof systems with ease using syntax that mimics pseudocode in c"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

This paper introduces Zippel, a language, compiler, runtime, and analyzer for cryptographic proof systems. Zippel lets developers write proof systems with ease using syntax that mimics pseudocode in cryptography papers. It also eliminates entire classes of vulnerabilities by construction owing to its type system and runtime. For example, Zippel automatically synchronizes protocol transcripts and correctly applies the Fiat--Shamir transform. Zippel also has fully automated static analyses that confirm whether a protocol is complete and sound given only the protocol's description. We have implemented 35 proof systems in Zippel including Sumcheck, Schnorr, KZG, Groth16, Bulletproofs, Hyrax, Spartan, Dory, HyperPlonk, DeKART, and Pari. Our evaluation shows that Zippel programs are competitive with hand-written implementations on multi-core hardware, so Zippel's security and implementation benefits do not come at high cost.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2517) | 2026-10-16
