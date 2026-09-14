---
title: "SoK: Private Transformer Inference Across Systems, Models, and Cryptography"
date: "2026-09-13"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2005"
summary: "Private inference can protect user queries and model weights without trusted hardware or statistical privacy relaxations, but transformers combine large secret matrix multiplications, costly nonlinear"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Private inference can protect user queries and model weights without trusted hardware or statistical privacy relaxations, but transformers combine large secret matrix multiplications, costly nonlinearities, and sequential autoregressive execution. Prior surveys organize the literature mainly by cryptographic backend, deployment setting, or supported operation, obscuring when techniques remain applicable or composable across execution phases, model adaptations, or security boundaries. We systematize 58 cryptographic private transformer frameworks (2022--2026) across three interacting levels: systems (execution and optimization), models (cryptography--machine learning co-design and adaptation), and cryptography (secure realization of transformer operations). This analysis reveals two recurring cross-backend applicability constraints: optimizations do not transfer unchanged across execution phases when they require values not yet available, while data-dependent pruning, cache management, routing, and sparsity require private execution structure to be hidden, constrained, predicted, or disclosed. Against an output-only reference baseline, we identify four classes of security concerns affecting 5 frameworks and synthesize composition boundaries in maliciously secure designs. We find that 16 frameworks rely on empirically calibrated or distribution-specific mechanisms and 21 require additional training, limiting generalization and cross-framework comparability. We distill these findings into 12 open problems and 16 outlooks spanning protocol efficiency, cross-level co-design, dynamic execution, security, evaluation, and scalability.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2005) | 2026-09-13
