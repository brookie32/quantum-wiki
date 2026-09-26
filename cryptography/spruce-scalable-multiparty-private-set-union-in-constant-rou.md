---
title: "SPRUCE: Scalable Multiparty Private Set Union in Constant Rounds"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2188"
summary: "Multiparty private set union (MPSU) enables a group of mutually distrusting parties, each holding a private set, to learn the union of their sets without revealing additional information. MPSU is a fu"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

Multiparty private set union (MPSU) enables a group of mutually distrusting parties, each holding a private set, to learn the union of their sets without revealing additional information. MPSU is a fundamental primitive with applications to privacy-preserving tasks such as cyber-risk assessment and private record matching. State-of-the-art MPSU protocols require parties to sequentially shuffle encrypted values in order to hide which party contributed which inputs to the final result. We introduce a new paradigm for semi-honest MPSU that eliminates the need for such shuffling. This allows the protocol to run in constant rounds regardless of how many parties are involved. The resulting protocol also benefits from improved parallelism, an information-theoretic online phase, and native support for unbalanced input sizes, a situation most prior works must handle by padding inputs to hide individual input sizes. We implement and evaluate our protocol across a range of party counts, input sizes, and network conditions. In the unbalanced setting, where parties hold unequal-sized inputs, our protocol significantly outperforms the state-of-the-art schemes PULSE (CCS ’25) and DZBC25 (USENIX Security ’25). In the balanced setting, it achieves an order-of-magnitude improvement over PULSE in most settings and outperforms DZBC25 in WAN deployments with 100ms latency.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2188) | 2026-09-23
