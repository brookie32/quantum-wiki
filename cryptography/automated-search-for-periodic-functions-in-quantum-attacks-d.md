---
title: "Automated Search for Periodic Functions in Quantum Attacks: Distinguishers and Key-Recovery Attacks"
date: "2026-10-03"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2319"
summary: "Quantum attacks based on Simon's algorithm rely on Boolean functions with hidden XOR periods. At ASIACRYPT 2025, Liu et al. introduced a symbolic automated search model for periodic functions used in "
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Quantum attacks based on Simon's algorithm rely on Boolean functions with hidden XOR periods. At ASIACRYPT 2025, Liu et al. introduced a symbolic automated search model for periodic functions used in distinguishers. However, for distinguishers on target ciphers, the search mainly works with truncated differences and does not jointly constrain exact differential propagation. A separate modeling gap arises in the key-recovery setting: the model does not cover the key-dependent periodic functions used in the polynomial-time key-recovery attacks presented by Canale et al. at CRYPTO 2022. In this work, we study automated search for two classes of periodic functions: periodic functions for distinguishers and key-dependent periodic functions for polynomial-time key-recovery attacks. For the former, we refine the symbolic search model of Liu et al. by adding fixed input differences, differential propagation, and probability constraints. Based on this model, we extend the periodic distinguishers of TWINE and LBlock from 10 rounds to 12 rounds, obtain a 12-round periodic distinguisher for LBlock-S, and find a full-round periodic distinguisher for ALLPC with verified probability (2^{-9.06}). For key recovery, we adapt the symbolic-state tracking used for distinguishers to key-dependent values. The model tracks key-dependent shifts and checks that the periodic core is exposed through an output-computable expression. With this model, we extend the attack on MISTY L-FK from 5 to 6 rounds and obtain new polynomial-time key-recovery attacks on Type-1/2 GFS and Skipjack-B variants with FK or KF round functions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2319) | 2026-10-03
