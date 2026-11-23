---
title: "Evaluating CNF/SMT Encodings for SAT-Based Differential Cryptanalysis of Lightweight Block Ciphers"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2999"
summary: "This study evaluates three encoding methods for automated differential cryptanalysis: (1) SMT formulations (using CVC), (2) standard CNF, and (3) size-optimized CNF (via Logic Friday). We assess these"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

This study evaluates three encoding methods for automated differential cryptanalysis: (1) SMT formulations (using CVC), (2) standard CNF, and (3) size-optimized CNF (via Logic Friday). We assess these using four SAT/SMT solver types: single-core (CryptoMiniSat-v5, CaDiCaL), multi-core (Treengeling), and massively parallel Mallob—novel to cryptanalysis. Encoding-solver combinations are tested on seven lightweight block ciphers representing distinct design philosophies: SPECK-32 and CHAM-64 (ARX structure), SIMON-32 (AND-RX structure), PRESENT, GIFT-128, and MIDORI-64 (4-bit S-box in SPN structure), and LBLOCK (Feistel structure). For each cipher, SAT/SMT instances targeting specific rounds/differential weights were generated, with wall-clock solving time, parallel efficiency, and modeling effort measured. Our results establish criteria for optimal encoding-solver pairings that strike a balance between modeling simplicity and computational performance. Crucially, Mallob emerges as the state-of-the-art framework for large-scale automated differential cryptanalysis.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2999) | 2026-11-23
