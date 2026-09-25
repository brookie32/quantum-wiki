---
title: "MagiCFirm: A Runtime for Magic-State Cultivation with Algorithm-Hardware Co-Design"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.29267"
summary: "arXiv:2609.29267v1 Announce Type: new Abstract: Magic-state cultivation offers a promising alternative for lowering the cost of non-Clifford operations in fault-tolerant quantum computing (FTQC). Howe"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.29267v1 Announce Type: new Abstract: Magic-state cultivation offers a promising alternative for lowering the cost of non-Clifford operations in fault-tolerant quantum computing (FTQC). However, realizing cultivation in practice exposes two challenges: (i) the lack of an open-source classical runtime layer between logical software and physical control, and (ii) the latency constraints on protocol-specific decisions that determine magic-state readiness. To address these challenges, we adopt an algorithm--hardware co-design approach. At the algorithm level, we develop a two-stage early-escape scheme that identifies an informative subset of detectors offline, constructs a compact decoding problem, and performs partial decoding in parallel with complete decoding at runtime, allowing high-confidence attempts to advance before full decoding completes. At the hardware level, we present MagiCFirm, a configurable runtime that combines offline-compiled microprograms with dedicated datapaths for detector construction, event processing, and protocol control, enabling end-to-end execution of magic-state cultivation. Across evaluated configurations, MagiCFirm reduces wall-clock magic-state preparation time by up to 39.3% at matched logical error rate. For a representative magic-state-bound workload, this translates to an estimated 11% reduction in overall application runtime.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.29267) | 2026-09-25
