---
title: "DASH: Distributed Asynchronous Schnorr with High Throughput"
date: "2026-09-21"
updated: "2026-09-22"
source: "agent"
category: "error-correction"
tags: [error-correction, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2138"
summary: "Robust asynchronous threshold Schnorr signatures enable honest parties to complete signing despite malicious behavior and network delays. To reduce online latency, these schemes typically follow an of"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Robust asynchronous threshold Schnorr signatures enable honest parties to complete signing despite malicious behavior and network delays. To reduce online latency, these schemes typically follow an offline–online paradigm. The parties prepare batches of shared nonces in the offline phase and consume them to generate signatures online. In high-throughput constructions such as SPRINT (Benhamouda et al.~Eurocrypt 2024), super-invertible matrices are used to extract multiple nonces and their corresponding commitments from a single execution of the nonce-generation protocol. However, the associated group operations incur substantial computational overhead. We identify several computational bottlenecks in SPRINT and present mathsf{DASH}, a suite of robust asynchronous threshold Schnorr signature protocols that substantially improve computational efficiency while retaining SPRINT’s amortized linear communication cost. Our contributions are threefold. First, we propose distributing the group computations involved in nonce extraction among the parties. This reduces the amortized computational cost from O(log n) to O(1) group operations per signature per party. To enable this distributed computation, we employ a batching technique that allows each dealer to distribute L nonce polynomials simultaneously. Second, we introduce an efficient batched share-verification procedure that jointly checks shares of all L polynomials. For concrete parameters, this can accelerate share verification by a factor of 40-60. We also introduce a simple agreement protocol via player elimination, which could be of independent interest. Finally, under a stronger honest-majority assumption, we develop a packed two-stage online reconstruction protocol that enables parties to reconstruct signatures through error correction. This eliminates the need for signature-share verification, and consequently, avoids the expensive group operations performed by the aggregator in SPRINT. Surprisingly, even in the worst case, our mathsf{DASH} protocols preserve the same asymptotic amortized computation and communication costs, provided that L gg nlog n. %We prove the security of all mathsf{DASH} variants in the random oracle model under the standard discrete logarithm assumption.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2138) | 2026-09-21
