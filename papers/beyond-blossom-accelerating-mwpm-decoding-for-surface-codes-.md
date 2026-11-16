---
title: "Beyond Blossom: Accelerating MWPM Decoding for Surface Codes With Local Predecoding and Architecture-Aware Optimizations"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.18476"
summary: "arXiv:2611.18476v1 Announce Type: cross Abstract: Minimum-weight perfect matching (MWPM) is widely used to decode surface codes, but its computational cost increases with code distance. We present Bey"
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2611.18476v1 Announce Type: cross Abstract: Minimum-weight perfect matching (MWPM) is widely used to decode surface codes, but its computational cost increases with code distance. We present Beyond Blossom, a state-of-the-art CPU-based MWPM decoder for surface codes. It combines algorithmic optimization through local predecoding, architecture-aware optimization, and pipeline-wide parallelism to reduce matching workload and execution overhead while preserving MWPM optimality. Across rotated surface codes with distances 9-33 and circuit-level physical error rates of 0.05%-0.3%, on a single CPU core, Beyond Blossom achieves a 4.23imes geometric-mean speedup and up to 5.58imes speedup over Sparse Blossom in PyMatching. At distance 33 and a physical error rate of 0.1%, with 8 CPU cores, decoding a block of 33 measurement rounds takes 21.40 mus on average, equivalent to 0.65 mus per round.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.18476) | 2026-11-16
