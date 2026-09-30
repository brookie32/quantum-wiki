---
title: "Generic Bounds for Multi-Instance Problems: The Strange Case of Inverse Diffie-Hellman"
date: "2026-09-28"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2253"
summary: "In a multi-instance problem, the adversary is given n independent problem instances and succeeds if it solves at least k of them. We study the generic hardness of a broad class of multi-instance probl"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

In a multi-instance problem, the adversary is given n independent problem instances and succeeds if it solves at least k of them. We study the generic hardness of a broad class of multi-instance problems over prime-order groups, including multi-instance Computational Diffie-Hellman (CDH), Square Diffie-Hellman (SDH), Inverse Diffie-Hellman (IDH), and Linear Kernel Diffie-Hellman (LKDH). As expected, we show that, in generic groups, solving multi-instance CDH and SDH is as hard as solving k independent discrete logarithm instances. In contrast, although the single-instance versions of CDH and IDH are known to be equivalent, we establish generic upper and lower bounds showing that multi-instance IDH (and LKDH) can be significantly easier to solve than multi-instance CDH in certain parameter regimes. All problems, however, offer 1/2(log(p)+log(k)) bits of security. Our lower-bound techniques extend Yun's information-theoretic hyperplane query model (EUROCRYPT 2015). At the core of our approach lies an inductive argument showing that, in order to establish a generic-group lower bound, it suffices to bound the adversary's "zero-hyperplane-query" advantage in the hyperplane query model. For the multi-instance problems considered in this work, we derive such bounds using techniques from algebraic geometry. More precisely, we analyze the Krull dimension of suitable algebraic varieties, either by explicitly computing Gröbner bases or by upper bounding the number of algebraically independent elements in the associated coordinate rings.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2253) | 2026-09-28
