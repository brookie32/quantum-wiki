---
title: "Phantom Timing Leaks on Cortex-M4: A Pre-registered Evaluation of ML-KEM Decapsulation"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2744"
summary: "Fixed-versus-random timing tests in the style of dudect are a cheap first check of constant-time behaviour, and on microcontrollers the cycle counter makes them exact to the cycle. We report a pre-reg"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Fixed-versus-random timing tests in the style of dudect are a cheap first check of constant-time behaviour, and on microcontrollers the cycle counter makes them exact to the cycle. We report a pre-registered evaluation of ML-KEM decapsulation on an STM32F411 (Cortex-M4) covering nine implementations of PQM4 (clean, m4fspeed, m4fstack for ML-KEM-512/768/1024) and a positive control in which we restored the pre-KyberSlash division formulas. Each of the 44 campaigns used in the analysis has 100,000 trials and checks every result. With invalid ciphertexts (random bytes, or one modified byte), no difference is detected in 18 of 18 campaigns, and both classes always have exactly the same cycle count, while the control is detected every time (|t| up to 1,877). With fresh valid ciphertexts, however, all nine implementations are flagged, with differences of 4 to 15 cycles and |t| >= 19,000 (or infinite, when both classes have zero variance). A matched control, in which both classes run the same code before the measured call, removes the difference for seven of the nine. An A/A test, in which both classes decapsulate the same bytes, still yields |t| = 12,864 for one implementation. Deterministic few-cycle differences can therefore come from the measurement harness alone: on a part with flash wait states, an instruction cache and prefetching, they can appear when the code around the measured call changes. We also show that per-trial correctness checks matter: they exposed a functional bug in PQM4's ML-KEM-1024 m4fstack (220 wrong shared secrets out of 49,830), which upstream had fixed shortly before. We report every deviation from the pre-registration, including a build error of our own, and publish data, binaries and code (https://doi.org/10.5281/zenodo.23921418).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2744) | 2026-11-03
