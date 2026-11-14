---
title: "Optimized Solving Strategy and Two-Step Estimator for LWE with Hints"
date: "2026-11-12"
updated: "2026-11-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2873"
summary: "Side-channel hints can reduce the cost of solving the Learning with Errors (LWE) problem. We optimize a two-step strategy for LWE with hints that uses BKZ reduction followed by final lattice sieving. "
last_verified: "2026-11-14"
review_by: "2027-02-12"
stale: false
---

Side-channel hints can reduce the cost of solving the Learning with Errors (LWE) problem. We optimize a two-step strategy for LWE with hints that uses BKZ reduction followed by final lattice sieving. Given a lattice constructed from the hints and a specified pair of reduction and sieving algorithms, the strategy jointly selects BKZ block sizes, tour counts, and a final sieving configuration. We also introduce a two-step estimator that predicts the reduced-basis profile and estimates the probability of secret recovery. We combine these estimates with cost models to select a strategy that meets the success-probability and resource constraints. Experiments show that our strategy significantly outperforms the methods of Cao et al. (CRYPTO 2025) and May and Nowakowski (ASIACRYPT 2023). For example, using BLASterBKZ for lattice reduction and the BGJ sieve for final sieving, our strategy recovers the secret for a CRYSTALS-KYBER 512 instance with 190 perfect hints in 7 minutes, compared with 1.6 hours reported by Cao et al. and 7.4 hours reported by May and Nowakowski. With 64 threads, our strategy recovers the secret with 170 perfect hints in 82 minutes. These results highlight the importance of accounting for side-channel leakage when assessing lattice-based cryptographic schemes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2873) | 2026-11-12
