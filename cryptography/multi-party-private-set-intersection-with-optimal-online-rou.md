---
title: "Multi-Party Private Set Intersection with Optimal Online Round Complexity and Updatability"
date: "2026-08-22"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1774"
summary: "Multi-party private set intersection (MPSI) enables multiple parties to securely compute the intersection of their private datasets without revealing any information beyond the intersection itself. Ho"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

Multi-party private set intersection (MPSI) enables multiple parties to securely compute the intersection of their private datasets without revealing any information beyond the intersection itself. However, as the number of participants scales, the performance of multi-party PSI protocols is significantly influenced, with the number of interaction rounds emerging as a critical bottleneck. In this paper, we propose a novel MPSI protocol and its updatable extension based on function secret sharing and oblivious key-value stores, achieving optimal one-pass online interaction. Our construction guarantees security in the semi-honest model, resisting collusion among any n-1 parties when the Leader is honest, and among any n-2 parties when the Leader is corrupted—an assumption that aligns well with many practical deployment scenarios. Furthermore, our multi-party updatable PSI (MUPSI) protocol allows parties to efficiently compute the intersection over dynamically updated sets. Our MUPSI protocol achieves collusion resistance against any n-1 participants, assuming an honest Leader. It ensures that both computational and communication complexities scale exclusively with the size of the updates rather than the entire datasets, exhibiting superior performance particularly when handling unbalanced sets and large participant cohorts. All proposed protocols exhibit strong scalability with respect to participant count. We demonstrate the superiority of our protocols through implementation and comparison with state-of-the-art MPSI protocols. Experiments show that when the number of participants ranges from 20 to 140 and the set size ranges from 2^{12} to 2^{20}, our MPSI protocol is competitive. Notably, in the WAN setting with 140 participants and a set size of 2^{20}, the running time is reduced by 49.1imes compared with GLW+24. Our MUPSI protocol avoids PSI operations on entire sets, achieving a reduction in running time by an order of magnitude.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1774) | 2026-08-22
