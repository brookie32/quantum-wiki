---
title: "Packing Stern into L2: GPU-Accelerated Primal-Shortened ISD for High-Codimension Binary Goppa Key Recovery"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2993"
summary: "Primal-Shortened Information-Set Decoding (ISD) with quadratic polar lifting recently pushed TII McEliece Track-2 key recovery to (TII-228, 2,463 CPU core-hours), with over 99% of runtime spent harves"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Primal-Shortened Information-Set Decoding (ISD) with quadratic polar lifting recently pushed TII McEliece Track-2 key recovery to (TII-228, 2,463 CPU core-hours), with over 99% of runtime spent harvesting weight- codewords. Porting MiniMax's Mode-6 Stern sampler directly to one block per SM leaves 1.0–1.5 GB of hash tables active and stalls on global memory. For , we pack all remaining syndrome bits into one 16-byte ulonglong2 without left-triple indices, share cooperative tables inside GPU L2 cache, batch random systematic reductions per launch, and widen the shortening prefix to cut modeled GPU-hours by 34%–47%. Across four Track-2 challenges (), every recovered private key passes both the official SageMath checker and a standalone pure-Python verifier. Eight Modal L40S GPUs solve TII-228 () in 18.9 min (2.15 GPU-hours, faster in wall-clock than MiniMax's EPYC cluster). We further recover keys for the previously undocumented challenges TII-237 (, 22.1 L4 GPU-hours) and TII-235 (, 4.30 h across ten L40S GPUs, 39.62 GPU-hours, 17.97 s lift), using 127 of 128 packed bits. These results do not demonstrate practical recovery against Classic McEliece parameters ().

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2993) | 2026-11-23
