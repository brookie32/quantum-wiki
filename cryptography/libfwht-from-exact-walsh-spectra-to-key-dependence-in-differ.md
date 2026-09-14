---
title: "LibFWHT: From Exact Walsh Spectra to Key Dependence in Differential-Linear Correlations"
date: "2026-09-12"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1997"
summary: "The Walsh-Hadamard transform (WHT) computes the correlation of a Boolean function with every input parity function at once. Cryptanalytic workflows transform large arrays repeatedly, in batches. Howev"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

The Walsh-Hadamard transform (WHT) computes the correlation of a Boolean function with every input parity function at once. Cryptanalytic workflows transform large arrays repeatedly, in batches. However, available tools specialize in particular datatypes, platforms, or ecosystems, and none combines what a portable search needs. We present LibFWHT, an open-source C library for dense Walsh-Hadamard transforms, with Python bindings and a command-line interface. It includes vectorized, multicore, and graphics-processor backends, batch operations, and Boolean and substitution-box helpers. With one central processing unit (CPU) core, LibFWHT is 2.5 to 3.3 times faster than FFTW and up to 3.7 times faster than sboxU on batched Boolean spectra. On an NVIDIA H200 its device-resident graphics-processor backend reaches 1.8 trillion operations per second and runs the same Boolean workload about 600 times faster than the CPU-only sboxU. We demonstrate LibFWHT in linear and differential-linear cryptanalysis of SIMON-32, KATAN-32, BEANIE, KeeLoq, and RC5-16, all with 32-bit blocks. We report the first exact differential-linear distinguishers for KATAN-32, BEANIE, KeeLoq, and RC5-16, whose correlations are measured over the complete codebook rather than estimated from round-by-round trails. We then analyze how these correlations depend on the key, using the geometric approach to cryptanalysis. Writing a fixed-key correlation as a signed sum over key masks turns key dependence into a question of which masks survive. We address this question by combining a mixed-basis trail search with exact measurement on sampled keys. The search proposes responsible round-key bits, and only the measurement determines whether those bits explain the dependence. The procedure separates three outcomes: dependence concentrated on a few key bits, cancellation at the enumerated leading orders, and dependence only weakly explained by the tested short list. Distinguishers are normally reported as a single correlation, and key-recovery complexities are computed from that number. We show that relying on this summary is unsafe. For one of our distinguishers, a quarter of the keys belong to a weak class. Its root-mean-square correlation implies a data requirement about 40 times that estimated from the overall root-mean-square correlation. Key dependence therefore belongs in the analysis, and we report distributions over keys rather than single numbers.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1997) | 2026-09-12
