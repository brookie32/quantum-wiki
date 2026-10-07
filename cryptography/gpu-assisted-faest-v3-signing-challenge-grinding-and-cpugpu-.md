---
title: "GPU-Assisted FAEST v3 Signing: Challenge Grinding and CPU–GPU Pipelining"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2355"
summary: "Applying a GPU to FAEST v3 signing requires more than exploiting parallel computation: challenge grinding must preserve the minimum accepting counter selected by the original signing procedure, and si"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Applying a GPU to FAEST v3 signing requires more than exploiting parallel computation: challenge grinding must preserve the minimum accepting counter selected by the original signing procedure, and single-sign latency and multi-sign throughput must be evaluated under distinct execution conditions. We implement GPU-assisted challenge grinding in which the GPU filters candidates over contiguous counter ranges in parallel, while the CPU performs the final acceptance checks in increasing counter order. For multiple independent signatures, we construct a CPU–GPU hybrid pipeline with two alternating signing-state slots, allowing CPU work for one slot to proceed while the GPU batch for the other slot is executing. Across the six non-EM FAEST v3 parameter sets evaluated on the same CPU–GPU system, the CPU–GPU path has lower representative single-sign latency for four parameter sets, whereas the optimized CPU path is lower for two. The largest representative same-session CPU/CPU–GPU latency ratio is 1.602799 for FAEST-192s. For multi-sign throughput with (B in {2,4,8}), the CPU–GPU path has higher representative throughput in 9 of the 18 parameter–batch-size combinations, while the CPU path is higher in the remaining 9 under the predefined primary aggregation rule. Correctness validation confirms that GPU-assisted challenge grinding produces the same minimum accepting counter and final signature as the reference path for the evaluated configurations. These results show that the performance effect of GPU assistance is not uniform across the evaluated FAEST v3 signing configurations and depends on both the parameter set and whether the execution targets single-sign latency or the throughput of multiple independent signatures.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2355) | 2026-10-05
