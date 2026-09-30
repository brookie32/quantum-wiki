---
title: "NOMOS: Secure Non-Interactive kNN under CKKS"
date: "2026-09-29"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2262"
summary: "The k-nearest neighbor (kNN) algorithm is a core primitive for similarity search over sensitive data, but evaluating kNN under fully homomorphic encryption remains expensive because it requires distan"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

The k-nearest neighbor (kNN) algorithm is a core primitive for similarity search over sensitive data, but evaluating kNN under fully homomorphic encryption remains expensive because it requires distance computation, encrypted ranking, and top-k extraction. CKKS is attractive for this setting because it natively supports packed approximate arithmetic, yet existing CKKS-based systems such as Engorgio (USENIX Security 2025) incur high overhead when used for reranking candidate sets. We present NOMOS, an encrypted kNN protocol for candidate sets that targets the ranking and top-k extraction bottleneck. NOMOS builds on Mazzone et al.'s matrix-based ranking method (USENIX Security 2025), but introduces a gap-amplified sign approximation that focuses precision on near-zero distance gaps, where kNN rank decisions are most sensitive. NOMOS integrates this primitive into a complete encrypted kNN pipeline, using slot-index alignment and ReLU-based top-k extraction to avoid full sorting. For large databases, offline k-means preprocessing forms fixed-capacity candidate sets, allowing NOMOS to avoid global top-k extraction and reduce sign-approximation calls from quadratic global growth to near-linear clustered scaling. With these techniques, NOMOS outperforms state-of-the-art encrypted ranking and top-k baselines. Across the Mazzone-style ranking benchmark and candidate-set workloads compared with Engorgio, NOMOS reduces latency by nearly 8imes and up to 828imes, respectively. On the real-world SIFT dataset, NOMOS achieves 100% top-1 and top-8 retrieval accuracy on evaluated candidate sets, showing consistent retrieval quality on real data.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2262) | 2026-09-29
