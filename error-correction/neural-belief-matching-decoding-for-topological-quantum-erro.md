---
title: "Neural Belief-Matching Decoding for Topological Quantum Error Correction Codes"
date: "2026-07-22"
updated: "2026-07-22"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.21730"
summary: "arXiv:2603.21730v2 Announce Type: replace Abstract: Quantum error correction (QEC) is critical for scalable fault-tolerant quantum computing. Topological codes, such as the toric code, offer hardware-"
last_verified: "2026-07-22"
review_by: "2026-10-20"
stale: false
---

arXiv:2603.21730v2 Announce Type: replace Abstract: Quantum error correction (QEC) is critical for scalable fault-tolerant quantum computing. Topological codes, such as the toric code, offer hardware-efficient architectures but their Tanner graphs contain many girth-4 cycles that degrade the performance of belief-propagation (BP) decoding. For this reason, BP decoding is typically followed by a more complex second stage decoder such as minimum-weight perfect matching. These combined decoders achieve a remarkable performance, albeit at the cost of increased complexity. In this paper we propose two key improvements for the decoding of toric code. The first one is replacing the BP decoder by a neural BP decoder, giving rise to the neural belief-matching decoder which substantially decreases the average decoding complexity. The main drawback of this approach is the high cost associated with the training of the neural BP decoder. To address this issue, we impose a convolutional architecture on the neural BP decoder, enabling weight sharing across the spatially homogeneous structure of the code's factor graph. This design allows a model trained on a modest-size topological code to be directly transferred to much larger instances, preserving decoding quality while dramatically lowering the training burden. Our numerical experiments on toric-code lattices of various sizes demonstrate that this technique does not result in a noticeable loss in performance.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.21730) | 2026-07-22
