---
title: "Accelerating A*-Based Algorithms for Decoding Quantum Low-Density Parity-Check Codes"
date: "2026-09-10"
updated: "2026-09-10"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.10056"
summary: "arXiv:2609.10056v1 Announce Type: new Abstract: Quantum low-density parity-check (QLDPC) codes represent a promising approach for error correction in quantum computing. The recently proposed Tesseract"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

arXiv:2609.10056v1 Announce Type: new Abstract: Quantum low-density parity-check (QLDPC) codes represent a promising approach for error correction in quantum computing. The recently proposed Tesseract decoder uses the A* search algorithm that guarantees finding the most likely error pattern. However, practical implementations of Tesseract often involve an extremely large graph, and the inherently sequential nature of the search results in high computational overhead and long runtime. To improve decoding efficiency, we propose a two-stage decoding framework. First, a belief propagation (BP) decoder efficiently processes the syndrome. This step generates hard decisions (a binary error vector) and soft information (per-qubit confidence levels). In non-convergent BP cases, a gating mechanism examines the BP decoder's output to identify and filter out qubits with oscillating confidence values. In these cases, the refined output serves as input to Tesseract, which then attempts to identify and correct any residual errors. This hybrid approach leverages the high speed of BP decoding and delegates the more challenging decoding instances to Tesseract. Numerical results demonstrate a substantial reduction in overall decoding complexity while maintaining the logical error rate (LER) of the stand-alone Tesseract. Across all tested physical error rates, the proposed method achieves at least 5x reduction in the number of expanded nodes in the Tesseract, with a peak reduction of nearly 15x at a physical error rate of p = 0.05 for the [[126, 12, d < 11]] T1 code, and approximately 8.8x at p = 0.05 for the [[72, 12, 6]] bicycle bivariate (BB) code.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.10056) | 2026-09-10
