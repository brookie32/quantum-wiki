---
title: "CAROUSEL: GPU-Accelerated Private Vector Search via Homomorphic Sketching"
date: "2026-10-01"
updated: "2026-10-04"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2302"
summary: "Vector search on untrusted infrastructure exposes the query embedding, a faithful summary of the user's intent. Fully homomorphic encryption can hide the query, but existing approaches still require a"
last_verified: "2026-10-04"
review_by: "2027-01-02"
stale: false
---

Vector search on untrusted infrastructure exposes the query embedding, a faithful summary of the user's intent. Fully homomorphic encryption can hide the query, but existing approaches still require a full scan followed by ranking of encrypted scores. Scalable private systems avoid encrypted ranking by either sending scores from a single cluster to the client or moving the search to the client, which must first stream the entire vector index for preprocessing. We present Carousel, which instead scores the full corpus under encryption and compresses the results for client-side ranking. The server scores every vector under encryption, raises the scores to a power that preserves their order by magnitude while suppressing all but a handful, and compresses the resulting sparse vector into a logarithmic number of ciphertexts using homomorphic additions alone. Because every vector is scored, Carousel incurs no recall loss from discarding candidates. Since clients hold no database-dependent state, insertions and deletions take effect immediately at the cost of a single vector write. Carousel searches 1 billion vectors of BIGANN SIFT1B across multiple GPUs and achieves recall@100 of 0.9715. At 100 million SIFT vectors, it achieves recall@100 of 0.9845 with a query latency of 3.735 seconds on a single GPU.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2302) | 2026-10-01
