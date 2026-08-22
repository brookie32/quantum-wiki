---
title: "Notes on Short-Limb Modular Multiplication Techniques: Barrett, Montgomery, Plantard, and the Explicit CRT"
date: "2026-08-19"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1743"
summary: "This note collects, in compressed form, some techniques for modular multiplication with word-size (“short-limb”), or at most a-handful-of-words sized moduli as they are used in implementations of latt"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

This note collects, in compressed form, some techniques for modular multiplication with word-size (“short-limb”), or at most a-handful-of-words sized moduli as they are used in implementations of lattice-based cryptography: Barrett reduction and multiplication (in signed and unsigned flavors, with exact error, range, and canonicality analyses), Montgomery reduction and multiplication (including the folded-constant form, the precise equivalence with Barrett multiplication, even moduli, the multi-limb case, and the k-reduction), Plantard multiplication (the original unsigned algorithm, the signed variant, and a variant taking signed inputs to the canonical unsigned representative in [0,q)), and modular multiplication via the explicit Chinese remainder theorem. These are compressed out of my lecture slides in the class Post-Quantum Cryptography at National Taiwan University 2020--2025 (EE 5176/921 U2540). All numerical examples, ranges, and windows stated here have been verified by exhaustive or randomized machine search; several constants and ranges correct typos and miscalculations that circulated after lectures.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1743) | 2026-08-19
