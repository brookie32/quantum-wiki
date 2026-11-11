---
title: "TUTTI: Parallel CKKS Bootstrapping in under 3 ms on CPU"
date: "2026-11-09"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2848"
summary: "This paper introduces TUTTI, a new CKKS bootstrapping procedure that outperforms previous low-latency solutions in multi-threaded latency for any number of messages and, most notably, has a lower late"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

This paper introduces TUTTI, a new CKKS bootstrapping procedure that outperforms previous low-latency solutions in multi-threaded latency for any number of messages and, most notably, has a lower latency than TFHE when bootstrapping a single one. Our bootstrapping builds upon SPRU (CK, TCHES 2027), improving it with new methods for exploiting parallelism and increasing the number of messages, as well as with a refined security analysis, of independent interest, of the block-binary secret keys of LMSS (AsiaCCS 2023). utti bootstraps 4096 real-number messages in 46 to 83.4 ms on 192 threads to restore 1 to 9 multiplicative levels, outperforming SHIP (CHKS, Eurocrypt 2025) by a factor of up to 3 on the same machine. Unlike SHIP, TUTTI gains immediately from bootstrapping fewer messages, with a 256-message bootstrapping taking just 15 to 34 ms on 32 threads. For a single message, TUTTI takes 4.6 ms on 32 threads, whereas TFHE-rs needs 7.3 ms for a 4-bit bootstrapping on the same machine and thread count. We show that this advantage persists across different architectures: on an Apple M5 Pro laptop (ARM), TUTTI takes 2.4 ms on 14 threads, against 4.5 ms for TFHE-rs. Differences between CKKS and lightweight schemes such as TFHE remain on several fronts, from functionality to key sizes and security assumptions, but our work shows that multi-threaded latency is no longer one of them, closing a long-standing gap in the practical FHE literature.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2848) | 2026-11-09
