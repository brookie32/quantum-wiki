---
title: "Exact Asymptotic Rates and an Exponential Strong Converse for quantum SMP and One-Way Communication"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.14658"
summary: "arXiv:2609.14658v1 Announce Type: new Abstract: Computing many instances jointly can reduce communication per instance. We ask whether such savings occur in the simultaneous-message-passing (SMP) mode"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.14658v1 Announce Type: new Abstract: Computing many instances jointly can reduce communication per instance. We ask whether such savings occur in the simultaneous-message-passing (SMP) model and how they depend on quantum messages and shared resources. For every finite total function f and fixed error 0learepsilon<1, we prove that the optimal worst-case communication per instance for f^n converges to [ D^parallel(f)=log|Row(f)|+log|Col(f)|, ] where Row(f) and Col(f) are the sets of distinct rows and columns of the table (f(x,y))_{x,y}. This holds for classical and quantum SMP without shared entanglement, with or without shared randomness. Thus, transmitting row and column indices is asymptotically optimal, even with bounded error, joint computation, and quantum messages. In particular, the exponential advantage of quantum fingerprinting for a single instance of equality without shared randomness disappears in the asymptotic rate. We also prove that the same threshold governs an exponential strong converse: every fixed worst-case communication rate below it forces the probability of computing all n outputs correctly to decay as 2^{-Omega(n)}, even on average under a fixed product input distribution. With shared randomness, the optimal expected communication rate is (1-arepsilon)D^parallel(f). Entanglement shared between each sender and the referee halves both rates; arbitrary tripartite entanglement gives no further reduction. The results extend to a class of total relations and yield one-way characterizations with D^parallel(f) replaced by log|Row(f)|. Our proof reduces SMP to one-way communication and relates successful computation to sampling based on quantum min-entropy; we also give a simpler proof of the key lemma using the pretty-good measurement.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.14658) | 2026-09-15
