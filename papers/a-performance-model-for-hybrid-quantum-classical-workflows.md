---
title: "A Performance Model for Hybrid Quantum-Classical Workflows"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.15426"
summary: "arXiv:2607.15426v2 Announce Type: replace Abstract: Hybrid quantum-classical workflows are expected to underpin practical quantum computing, yet the community lacks a shared framework for reasoning ab"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2607.15426v2 Announce Type: replace Abstract: Hybrid quantum-classical workflows are expected to underpin practical quantum computing, yet the community lacks a shared framework for reasoning about integration requirements. We introduce a runtime model that decomposes workflow execution into quantum compute, classical compute, and communication costs at two levels of analysis. At the application level, where communication overhead only affects performance, we use a communication-to-computation ratio to quantify its impact on runtime. At the real-time level, when communication overhead determines feasibility, we examine how decoding and feedback latency affect logical operation times and resource requirements. The model evaluates execution with allocated resources, excluding scheduling and resource management. Applied to representative workflows, it shows that the compute-intensive applications, including those requiring HPC resources, are largely insensitive to communication overhead. However, the model identifies when hardware evolution, such as faster quantum processing and greater parallelism, can shift this balance toward communication bottlenecks.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.15426) | 2026-11-19
