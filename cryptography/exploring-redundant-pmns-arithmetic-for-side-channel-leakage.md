---
title: "Exploring Redundant PMNS Arithmetic for Side-Channel Leakage Reduction in ML-DSA"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3060"
summary: "Polynomial Modular Number Systems (PMNS) have been proposed as an efficient alternative to classical modular arithmetic, with applications to elliptic curve cryptography. While existing work has focus"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Polynomial Modular Number Systems (PMNS) have been proposed as an efficient alternative to classical modular arithmetic, with applications to elliptic curve cryptography. While existing work has focused on large-prime arithmetic, lattice-based cryptography operates over small moduli, a regime in which PMNS has not yet been studied. In this work, we explore this setting and propose a tailored PMNS instantiation for the modulus of ML-DSA, whose structure enables particularly efficient modular reductions. We further leverage the intrinsic redundancy of PMNS to construct a randomized arithmetic layer that decorrelates intermediate values from secret data, thereby reducing side-channel leakage without resorting to classical masking schemes. We evaluate the effectiveness of the proposed countermeasure through a comprehensive side-channel analysis, combining leakage detection with machine-learning-based profiling attacks targeting the Number Theoretic Transform. Our results demonstrate that PMNS-based randomization significantly reduces first-order leakage and provides strong resistance to practical side-channel attacks. We further assess the performance overhead of the proposed approach through cycle-accurate profiling on a RISC-V CVA6 core using Verilator. The observed slowdown is comparable to standard side-channel countermeasures reported in the literature. We identify the main computational bottlenecks and discuss how existing hardware acceleration strategies could substantially reduce this overhead, making PMNS a practical candidate for side-channel-resistant embedded implementations of lattice-based cryptography.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3060) | 2026-11-26
