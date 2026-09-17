---
title: "Optimistic History-Independent Sleepy Atomic Broadcast"
date: "2026-09-14"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2024"
summary: "The latency of sleepy consensus protocols has been improved significantly, with recent designs achieving constant-round confirmation. However, existing protocols either rely on unrealistic additional "
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

The latency of sleepy consensus protocols has been improved significantly, with recent designs achieving constant-round confirmation. However, existing protocols either rely on unrealistic additional assumptions about access to historical messages, where messages sent in round t may depend on messages received in rounds [t-k,t-1] for some k>1, or do not consider optimizing performance under optimistic conditions. In this work, we study history-independent sleepy atomic broadcast protocols while simultaneously considering optimistic conditions, where messages sent in round t depend only on messages received in round t-1. We first design a sleepy atomic broadcast protocol that achieves a confirmation latency of 2Delta (Delta is the upper bound on network delay) and an optimal latency of Delta under up to 1/5 corruption. Second, we present a super-optimistic atomic broadcast protocol, achieving a best-case latency of 2Delta under fault-free executions. Building on this insight, we propose an optimistic sleepy atomic broadcast protocol that relaxes the super-optimistic condition to tolerate sub-optimal faults. As a building block, we introduce an optimistic graded agreement protocol, OptimisticGA, which enables a dynamic optimistic quorum with four decision grades. Built on OptimisticGA, our optimistic atomic broadcast protocol achieves a good-case latency of 2Delta when the leader is honest, while tolerating up to 1/6 corruptions rather than requiring a fault-free setting. When corruption is more than 1/6, it seamlessly adapts to 1/3 resilience with a good-case latency of 3Delta. All protocols require no historical messages and tolerate an adversary that grows proportionally with honest nodes, with a minimal delay of Delta.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2024) | 2026-09-14
