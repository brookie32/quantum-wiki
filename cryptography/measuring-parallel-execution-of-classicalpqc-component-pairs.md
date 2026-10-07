---
title: "Measuring Parallel Execution of Classical–PQC Component Pairs in Hybrid TLS 1.3"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2341"
summary: "Hybrid key exchange and Composite ML-DSA signatures in TLS 1.3 split one operation into a classical component and a post-quantum cryptography (PQC) component that do not depend on each other. Using a "
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Hybrid key exchange and Composite ML-DSA signatures in TLS 1.3 split one operation into a classical component and a post-quantum cryptography (PQC) component that do not depend on each other. Using a cryptographic workload of the TLS handshake rather than a full TLS connection, this paper measures whether running the two components at the same time on two pthread worker threads reduces latency compared with sequential execution. We evaluate the three ECDHE–ML-KEM groups of RFC 10024 with the matching Composite ML-DSA schemes, each with server authentication and mutual authentication (mTLS). Parallel execution keeps the order of operations, overlaps only the component pair of one operation, and is timed with all synchronization cost included. In an ARM and an x86 environment, parallel execution was faster in all six conditions, with speedups of 1.157×–1.281× and 1.041×–1.235×. The gain was large in the signature stages, where the two components take similar time, and small or negative in the key exchange stages, where one component dominates. In a low-power x86 environment, however, the same source code was slower in all six conditions (0.800×–0.917×). There, the overhead of waking and waiting for the worker threads exceeded the time saved, and it grew with the stage length, so a fixed cost per pair does not explain it. Independence of the components therefore does not guarantee a gain, and parallelization should be applied only after measuring in the target environment.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2341) | 2026-10-05
