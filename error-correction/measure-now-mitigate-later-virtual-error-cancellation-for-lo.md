---
title: "Measure Now, Mitigate Later: Virtual Error Cancellation for Logical Quantum Circuits"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.12400"
summary: "arXiv:2610.12400v1 Announce Type: new Abstract: Early fault-tolerant quantum algorithms are a key step in scalable quantum computing, but are ultimately constrained by residual, uncorrectable logical "
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.12400v1 Announce Type: new Abstract: Early fault-tolerant quantum algorithms are a key step in scalable quantum computing, but are ultimately constrained by residual, uncorrectable logical errors. Logical quantum error mitigation can eliminate this bias, however its standard requirements include prior noise characterization, more complex experiments, and substantial sampling overhead. Although no mitigation technique can simultaneously overcome all three constraints, we demonstrate that the first two---noise learning and need for modified circuits---can be completely bypassed for logical circuits by leveraging only syndrome records. Specifically, we introduce virtual error cancellation: a method that, unlike previous bias-free approaches, operates entirely in classical post-processing on universal quantum circuits. We develop and numerically test end-to-end protocols that reduce the sampling overhead beyond fundamental limitations of existing syndrome-aware mitigation techniques, including syndrome-based postselection. In particular, we propose a scheme that pairs the low-latency decoder used in the experiment with a high-complexity decoder run in post-processing. In numerical simulations of a distance-7 rotated surface code, we show that our full-stack dual-decoder algorithm exhibits an error that diminishes as the number of samples increases, capable of reaching more than three orders of magnitude of suppression compared to the decoded logical error rate in an experimentally achievable setting. These results establish syndrome records as a resource for correcting universal computational estimates after quantum execution.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.12400) | 2026-10-09
