---
title: "Sparse-Blossom Decoding in o(1) Time"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.12262"
summary: "arXiv:2609.12262v1 Announce Type: new Abstract: Matching-based decoding is widely used in quantum error correction, and accelerating it is key to enabling fast and scalable fault-tolerant quantum comp"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

arXiv:2609.12262v1 Announce Type: new Abstract: Matching-based decoding is widely used in quantum error correction, and accelerating it is key to enabling fast and scalable fault-tolerant quantum computation. Minimum-weight perfect matching (MWPM) decoding provides rigorous guarantees for error suppression, while sparse blossom enables its practical implementation at modest problem sizes. However, the runtime of existing sparse-blossom implementations unavoidably increases with problem size, motivating a rigorous parallelization framework that guarantees correctness and a runtime shorter than the syndrome-extraction timescale. Here, we present such a framework and prove that the resulting parallel sparse-blossom algorithm produces the same correction as the original, non-parallel sparse blossom. For the rotated surface code with code distance d and physical error rates below a finite threshold, we prove that the average parallel runtime of decoding for O(d) rounds of syndrome extraction is upper bounded by a quasi-polylogarithmic function of d. For a d-round decoding window, this implies that the average parallel runtime per round is o(1). We also perform numerical simulation to identify conditions under which the parallel runtime per round decreases with increasing code distance. These results suggest that increasing code distance need not lead to longer parallel decoding times, providing a foundation for scalable parallel matching-based decoding.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.12262) | 2026-09-14
