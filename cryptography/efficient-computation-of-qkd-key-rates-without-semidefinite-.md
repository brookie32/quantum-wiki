---
title: "Efficient Computation of QKD Key Rates without Semidefinite Programming"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.23285"
summary: "arXiv:2608.23285v1 Announce Type: new Abstract: Translating observed data into a reliable estimate of the secure key rate is a crucial step for operating a quantum key distribution device. We provide "
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2608.23285v1 Announce Type: new Abstract: Translating observed data into a reliable estimate of the secure key rate is a crucial step for operating a quantum key distribution device. We provide a computational method for this task that only requires eigenvalue computations and is therefore both fast and resource efficient. In contrast, existing approaches rely on semidefinite programming or programming on the entropy cone, whose memory requirements can scale as d^4 in the underlying Hilbert-space dimension. Our method reduces this requirement to d^2. A minimal implementation of our algorithm takes fewer than 100 lines of Common Lisp. We demonstrate real-time key-rate estimation on a Raspberry Pi with a 1 GB memory and a Cortex-A53 processor. Despite these modest resources, our implementation outperforms existing workstation-based benchmarks by several orders of magnitude. Non-numerical verification can be incorporated with little overhead using rational approximations. These results open the way toward embedding complete numerical security analysis directly into qkd hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.23285) | 2026-08-25
