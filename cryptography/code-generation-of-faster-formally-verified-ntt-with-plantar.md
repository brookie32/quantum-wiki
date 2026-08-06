---
title: "Code Generation of Faster Formally Verified NTT with Plantard Reduction"
date: "2026-08-06"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1624"
summary: "We present a formally verified implementation of the ML-KEM Number-Theoretic Transform (NTT) based on Plantard arithmetic, produced via a code generator that targets ML-KEM, ML-DSA, and FN-DSA from a "
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

We present a formally verified implementation of the ML-KEM Number-Theoretic Transform (NTT) based on Plantard arithmetic, produced via a code generator that targets ML-KEM, ML-DSA, and FN-DSA from a single parameter triple. The generator embeds a static bound analyzer that places modular reductions at code-generation time without runtime branching, eliminating per-scheme manual tuning while preserving constant-time guarantees. Each generation produces structurally identical implementations in two backends: portable C, and Jasmin for formal verification. To establish end-to-end correctness, we contribute a parametric formalization of Plantard arithmetic in extsc{EasyCrypt} and a layer-by-layer program-equivalence proof connecting the extracted Jasmin ML-KEM NTT to the abstract specification of formosa-mlkem; the existing algebraic chain is reused unchanged to extend correctness down to the mathematical NTT definition. Benchmarks across three schemes show that the generated code outperforms reference C by 1.5imes--1.8imes on the forward NTT and 1.7imes--2.5imes on the inverse, and outperforms the formally verified formosa-mlkem Jasmin baseline by 1.26imes and 2.19imes on ML-KEM. We believe our techniques generalize to other lattice-arithmetic primitives requiring both performance and formal verification.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1624) | 2026-08-06
