---
title: "Efficient Two-Dimensional Representation Evaluation via Dual Isogenies with Applications to Isogeny-Based Cryptography"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2506"
summary: "The evaluation of two-dimensional isogeny representations is a fundamental operation in many isogeny-based cryptographic schemes, notably the public-key encryption schemes POKE (Eurocrypt 2025) and PI"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

The evaluation of two-dimensional isogeny representations is a fundamental operation in many isogeny-based cryptographic schemes, notably the public-key encryption schemes POKE (Eurocrypt 2025) and PIKE (PKC 2026), as well as the digital signature schemes SQIsign2D-West (Asiacrypt 2024) and SQIsign2DPush (Eurocrypt 2026). However, existing two-dimensional evaluation algorithms rely on time-consuming discrete logarithm computations and torsion-basis generation, creating a severe performance bottleneck for the entire protocol. In this paper, we propose a novel algorithm for evaluating two-dimensional representations by leveraging the properties of dual isogenies, thereby eliminating the need for costly discrete logarithms. We apply this methodology to significantly accelerate some isogeny-based protocols, including POKE, SQIsign2D, and their variants. We provide optimized C implementations for the speed-optimized variants of POKE and SQIsign2D using our proposed method. Experimental benchmarks demonstrate that the fast variants of POKE combined with our new techniques achieve computational speedups of up to 3.47imes in terms of CPU clock cycles compared to POKE at the NIST-I security level. Additionally, our explicit analysis and implementation results confirm that the signing phase of SQIsign2DPush (resp. the NIST post-quantum cryptography standardization candidate SQIsign-v3.0), when using our method, achieves a performance improvement of up to 11.24% (resp. 5.02%) across the three NIST security levels.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2506) | 2026-10-16
