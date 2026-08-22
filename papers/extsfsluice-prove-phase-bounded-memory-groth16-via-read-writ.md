---
title: "extsf{Sluice}: Prove-Phase Bounded-Memory Groth16 via Read-Write Streaming"
date: "2026-08-21"
updated: "2026-08-22"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1758"
summary: "We present extsf{Sluice}, a read-write streaming Groth16 prover that reduces extit{prove-phase} random-access working memory from O(N) to O(log N) once the CRS, QAP, and witness are materialized as pr"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

We present extsf{Sluice}, a read-write streaming Groth16 prover that reduces extit{prove-phase} random-access working memory from O(N) to O(log N) once the CRS, QAP, and witness are materialized as private streams. It preserves the standard Groth16 interface: a proof of 3 group elements, 3-pairing verification, and unchanged verifier contracts. Our key technical contribution is extit{Split-Butterfly-Merge} (mathsf{SBM}), an NTT algorithm in the read-write streaming model with O(log N) memory, O(N log N) total I/O, and O(log N) sequential passes over external storage. Combining SBM with streaming sparse R1CS evaluation and chunked Pippenger MSM yields a verifier-compatible Groth16 proving path that exchanges RAM for sequential storage I/O and wall-clock time. Our prototype uses a fixed-window MSM engineering point; the measurements validate memory reduction and proof compatibility, while the theorem states the asymptotically tuned MSM schedule. We implement extsf{Sluice} over BN-254. Direct prove-only runs produce valid 128-byte proofs through N=2^{25}. The same-size bounded-memory comparison is at N=2^{23}: extsf{Sluice} succeeds under an 8GB Linux cgroup cap, whereas the standard prover is killed under 8GB and 12GB caps and succeeds only at 16GB. These results position extsf{Sluice} as a storage-rich, RAM-limited proving option rather than a replacement for optimized in-memory provers.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1758) | 2026-08-21
