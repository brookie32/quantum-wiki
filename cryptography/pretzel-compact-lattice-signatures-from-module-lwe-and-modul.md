---
title: "Pretzel: Compact Lattice Signatures from Module-LWE and Module-SIS"
date: "2026-11-21"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2970"
summary: "We present Pretzel, a lattice-based signature scheme in the style of ML-DSA. Across parameter sets targeting NIST security categories 2, 3, and 5, its signatures are 52-59% smaller than ML-DSA's, it s"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

We present Pretzel, a lattice-based signature scheme in the style of ML-DSA. Across parameter sets targeting NIST security categories 2, 3, and 5, its signatures are 52-59% smaller than ML-DSA's, it signs and verifies faster in all three categories, and its quantum security proof needs fewer assumptions. Across all three parameter sets, Pretzel produces smaller signatures than SHUTTLE (Ming et al., ASIACRYPT 2026), the recent state of the art for iterative rejection sampling from Module-LWE. At category 3, for example, Pretzel's 1361-byte signatures are 14% smaller than SHUTTLE's 1589 bytes. Unlike the quantum analyses of ML-DSA and SHUTTLE, Pretzel's security proof in the quantum random oracle model needs no self-target assumption: it relies only on Module-LWE and Module-SIS. Like SHUTTLE, Pretzel builds on Gartner's iterative rejection sampling (CRYPTO 2025). Its sampler keeps the response exactly on its target distribution after every update, which allows a substantially narrower mask than SHUTTLE's. Its verifier also enforces an additional bound on the response coefficients. This bound lets the security proof adapt Poremba's LWE-phase technique (ITCS 2023) to Module-LWE and rely on Module-LWE and Module-SIS alone.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2970) | 2026-11-21
