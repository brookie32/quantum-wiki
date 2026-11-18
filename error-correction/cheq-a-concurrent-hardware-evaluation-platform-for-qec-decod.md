---
title: "CHEQ: A Concurrent Hardware Evaluation Platform for QEC Decoders via Batch-Invariant Circuit-Level Noise Sampling"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.22247"
summary: "arXiv:2611.22247v1 Announce Type: new Abstract: Hardware quantum error correction (QEC) decoders require validation of logical error suppression and timing compliance before deployment. Rare logical f"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2611.22247v1 Announce Type: new Abstract: Hardware quantum error correction (QEC) decoders require validation of logical error suppression and timing compliance before deployment. Rare logical failures and deadline violations demand extensive sampling, while algorithm-level software evaluation does not directly measure hardware response times. Circuit-level noise models contain many error mechanisms but few firings per shot at low physical error rates, making exhaustive per-shot scanning inefficient. We present CHEQ, an FPGA platform integrating on-chip sampling, concurrent decoder evaluation, scoring, and RISC-V control. Its Sampling Units use geometric skipping to sample firing locations from detector error models and amortize mechanism traversal across shots within each batch. Under independent random draws and exact geometric sampling, the shot distribution is invariant to batch size, enabling a memory-throughput tradeoff. A throughput model guides joint selection of the Sampling Unit count, batch size, and decoder count under FPGA resource constraints. Across evaluated conditions, the pooled one-sided 95% upper bound on the weighted root-mean-square relative firing-rate difference from Stim is 0.16%. At a batch size of 4,096, a Sampling Unit uses only 4.8%-11.2% of a Helios decoder's LUTs for code distances 7, 9, 11, and 13. On an AMD VCU118 FPGA at code distance 7 and physical error rate 10^-3, two Sampling Units supply 20 Helios decoders at 49.2 million shots/s, completing 10^10 shots in 3.4 minutes without host-side shot generation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.22247) | 2026-11-18
