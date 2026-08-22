---
title: "Adapting AES-Oriented Optimizations to Rijndael-256: Cortex-M4, ARMv8-A, and CUDA"
date: "2026-08-19"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1735"
summary: "Rijndael-256 (R256), the 256-bit block variant of the Rijndael family, is practically relevant in ongoing NIST draft discussions on wider-block standardization and in several NIST post-quantum signatu"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

Rijndael-256 (R256), the 256-bit block variant of the Rijndael family, is practically relevant in ongoing NIST draft discussions on wider-block standardization and in several NIST post-quantum signature candidates. Relative to AES, R256 combines a wider 4imes8 state with non-standard ShiftRows offsets (0,1,3,4), invalidating key assumptions behind many AES-oriented optimizations. We study how these mismatches manifest on three targets and develop three corresponding adaptation strategies: wider classical bitslicing on Cortex-M4, Reuse with Reshuffling on AArch64, and Amortize the Mismatch on CUDA. This yields a bitsliced Cortex-M4 implementation with secret-independent control flow and memory access patterns (4,962 cycles/block), an AArch64 pre-shuffle design that reuses the AESE instruction with AddRoundKey folded in (up to 6,520 MB/s), and a CUDA shared-memory T-table implementation reaching 81.16 GiB/s; we report throughput on AArch64 and CUDA because per-block cycle measurement is not directly available on those platforms. Replacing the R256 cryptographic core in four NIST PQC reference codebases on Apple M2, with minimal integration changes where needed, yields signing speedups of 1.18imes--114.3imes and verification speedups up to 155.6imes, with the end-to-end gain governed by each scheme's R256 fraction.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1735) | 2026-08-19
