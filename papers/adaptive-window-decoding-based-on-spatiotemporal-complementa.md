---
title: "Adaptive Window Decoding based on Spatiotemporal Complementary Gap"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.14637"
summary: "arXiv:2605.14637v2 Announce Type: replace Abstract: Real-time decoding plays a crucial role in practical fault-tolerant quantum computing. Window decoding, in which the decoding problem is divided int"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2605.14637v2 Announce Type: replace Abstract: Real-time decoding plays a crucial role in practical fault-tolerant quantum computing. Window decoding, in which the decoding problem is divided into windows, is a promising approach. While reducing the window size is desirable for faster decoding, each window contains a buffer region whose size must typically be at least the code distance to avoid degrading the logical error rate, which limits how much the window can shrink. In this paper, we propose an adaptive decoding scheme in which window decoding is first performed with a small buffer size and a decoding confidence (soft information) is computed; if the confidence is low, the buffer size is enlarged and decoding is redone. This approach reduces the average decoding time, since most shots are decoded with a small buffer. A central challenge in realizing this scheme is that existing forms of soft information are not directly applicable to window decoding, especially with a small buffer. We address this challenge by introducing a new form of soft information, the spatiotemporal complementary gap, specifically designed for this setting. Numerical simulations demonstrate that the proposed scheme reduces the average buffer size by approximately 40% while maintaining the logical error rate. Beyond the reduction of average decoding time, the proposed method is also expected to contribute to reducing the reaction time for non-Clifford operations and relaxing the hardware requirements for real-time decoding.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.14637) | 2026-10-12
