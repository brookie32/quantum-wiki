---
title: "QAdapt: A Noise-Adaptive Neural Pre-Decoding Framework for Quantum Error Correction"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.28422"
summary: "arXiv:2607.28422v1 Announce Type: cross Abstract: Fault-tolerant quantum computing (FTQC) relies on quantum error correction to suppress physical errors and preserve logical information at scale. In p"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

arXiv:2607.28422v1 Announce Type: cross Abstract: Fault-tolerant quantum computing (FTQC) relies on quantum error correction to suppress physical errors and preserve logical information at scale. In practice, however, performance is constrained not only by physical noise but also by the latency of classical decoders processing rapidly generated syndrome data. This challenge is exacerbated by hardware noise that is strong, heterogeneous, and nonstationary, as well as by the simulation-to-hardware distribution shift that can substantially degrade fixed neural decoders. We present QAdapt, a noise-adaptive neural pre-decoding framework for surface-code quantum error correction. QAdapt captures local spatiotemporal correlations in syndrome data, sequentially adapts to evolving noise conditions while mitigating catastrophic forgetting, and forwards the residual syndrome to a conventional global decoder. Across 110 synthetic out-of-distribution noise configurations for rotated surface-code memory circuits, QAdapt consistently reduces the logical error rate relative to the neural pre-decoding baseline. On Google's Willow benchmark data, without target-domain fine-tuning, it achieves reductions of up to 5.79 percent in logical error rate and 9.32 percent in backend decoding latency on the residual syndrome. These results demonstrate that QAdapt provides a practical and decoder-compatible approach to improving the robustness and backend decoding efficiency of quantum error correction under evolving hardware noise.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.28422) | 2026-08-03
