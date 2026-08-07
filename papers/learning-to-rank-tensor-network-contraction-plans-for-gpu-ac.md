---
title: "Learning to Rank Tensor Network Contraction Plans for GPU-Accelerated Quantum Circuit Simulation"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.05819"
summary: "arXiv:2608.05819v1 Announce Type: cross Abstract: Classical simulation remains essential for developing and validating quantum algorithms, but its cost grows rapidly with circuit size. Tensor-network "
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.05819v1 Announce Type: cross Abstract: Classical simulation remains essential for developing and validating quantum algorithms, but its cost grows rapidly with circuit size. Tensor-network contraction can reduce this cost by exploiting circuit structure, although its efficiency depends strongly on the chosen contraction plan. On GPUs, plans with similar theoretical complexity may perform very differently because execution also depends on parallelism, reduction structure, memory traffic, and contraction geometry. We present a learning-to-rank framework for selecting efficient contraction plans before executing them. Each plan is represented by structural features derived directly from its sequence of pairwise contractions, and gradient-boosted rankers are trained from GPU measurements using listwise and pairwise objectives. We evaluate the resulting models on diverse circuit families, using separate in-distribution and circuit-family-shift test sets, and compare them with random and MinFill-based baselines. The learned rankers generally identify better plans, with the listwise model providing the strongest overall decision quality. We also study backend shift by comparing empirical plan orderings on two GPU architectures and evaluating the source-trained models on the second device without retraining. The rankings remain substantially, though not perfectly, stable across GPUs, and the models retain useful decision quality. These results support Learning to Rank as a practical way to reduce contraction-plan search, while showing that performance remains partly backend dependent.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.05819) | 2026-08-07
