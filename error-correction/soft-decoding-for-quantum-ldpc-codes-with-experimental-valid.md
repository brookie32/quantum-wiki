---
title: "Soft decoding for quantum LDPC codes with experimental validation"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.26958"
summary: "arXiv:2609.26958v1 Announce Type: new Abstract: The decoder is a critical component of a fault-tolerant quantum computer, computing corrections based on parity-check measurements performed throughout "
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

arXiv:2609.26958v1 Announce Type: new Abstract: The decoder is a critical component of a fault-tolerant quantum computer, computing corrections based on parity-check measurements performed throughout the computation. A soft decoder supplements its output with a confidence score which, when used alongside post-selection, can substantially improve logical performance. We introduce a soft beam search decoder for quantum low-density parity-check codes that uses internal decoder data as a confidence metric, removing the need for extra computation. We perform circuit-level simulations of five quantum LDPC codes relevant for superconducting and trapped ion architectures equipped with our global soft decoder and we obtain up to 580imes logical-error suppression at a physical error rate of 10^{-3} while rejecting only 0.1% of shots. Then, we simulate an error detected measurement, which is a core logical operation of the walking cat architecture, using a streaming version of soft beam decoder and we achieve up to 210imes error suppression while increasing the rejection probability by only 0.5 percentage points. Finally, we revisit recent quantum LDPC code memory experiments on trapped ions, demonstrating that our soft decoder doubles the logical qubit lifetimes at the price of a mean rejection rate of 2.6%--5.6% per syndrome round, bringing all five codes into the beyond-breakeven regime.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.26958) | 2026-09-24
