---
title: "Time–Memory Tradeoffs for Message Modification in Step-Reduced SHA-512"
date: "2026-11-23"
updated: "2026-11-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3005"
summary: "SHA-512 is a core standard in the NIST SHA-2 hash family (FIPS PUB 180-4), and evaluating its step-reduced collision resistance is central to tracking its security margin. Recent collision attacks on "
last_verified: "2026-11-25"
review_by: "2027-02-23"
stale: false
---

SHA-512 is a core standard in the NIST SHA-2 hash family (FIPS PUB 180-4), and evaluating its step-reduced collision resistance is central to tracking its security margin. Recent collision attacks on 35–39-step SHA-2 rely on fixed-core two-block frameworks, where online message modification repeatedly connects random first-block chaining values to a fixed core and searches for compatible rear assignments. To eliminate the extensive chaining-value-independent recomputation on both sides of the core, we propose a coordinated front–rear time–memory tradeoff (TMTO) framework: on the front side, a shared counting directed acyclic graph (DAG) with online dynamic programming rapidly synthesizes batches of legal fronts; on the rear side, compact rear coordinates and bit-window bitmaps implicitly filter the step-16 compatibility relation without materializing huge tables. Under the uniform chaining-value model, our full front–rear TMTO lowers the expected online collision complexity of 36-step SHA-512 from 2^{66.2} to 2^{49.8} (7.05 GiB static storage), validated by a concrete standard-IV colliding message pair. At 37 steps, exact internal-branch unions further reduce the complexity from 2^{87} to 2^{75.2} on the public core (32.5 MiB) and 2^{75.0} on a new core (24.5 MiB). At 38 and 39 steps, although the rear space shrinks sharply, our front-side offline selection still applies directly to Gong et al.'s single-word-pinning attack, reducing complexity from 2^{100.7} to 2^{99.0} (38.1 KiB) and from 2^{131.3} to 2^{128.6} (3.11 MiB), respectively. All one-time preprocessing costs (2^{23}–2^{29} compressions) are accounted for separately and are completely negligible relative to the online complexities.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3005) | 2026-11-23
