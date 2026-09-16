---
title: "Shuttling Compiler for Trapped-Ion Quantum Computers Based on Fine-Tuned Large Language Models"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.18021"
summary: "arXiv:2512.18021v4 Announce Type: replace Abstract: In trapped-ion quantum computers, qubits must be shuttled between segments to interact. The routing logic that schedules these movements is written "
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2512.18021v4 Announce Type: replace Abstract: In trapped-ion quantum computers, qubits must be shuttled between segments to interact. The routing logic that schedules these movements is written by hand for every new trap architecture. We present shuttling compilers based on five large language models (LLMs). Each LLM is fine-tuned on shuttling schedules produced by hand-coded heuristics for linear and branched one-dimensional trap architectures. We investigate how the shuttling operation counts of their schedules compare with those of the heuristics and how far they generalize to unseen architectures. For circuits of up to 16 qubits, the fine-tuned LLMs generate valid schedules on both training architectures, more often the fewer qubits a circuit has. In 12% of the compilations yielding a schedule, the best of ten runs needs up to 21% fewer operations than the heuristic baselines, after a rule-based post-processing step. A single run of one fine-tuned LLM produces a valid shuttling schedule for a previously unseen four-way branched architecture. This is preliminary evidence of cross-architecture generalization. On two other unseen architectures no LLM produces a valid schedule. Thus, LLM-learned shuttling compilation is feasible, and we show how far it currently reaches.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.18021) | 2026-09-16
