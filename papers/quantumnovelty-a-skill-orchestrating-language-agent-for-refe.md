---
title: "QuantumNovelty: A Skill-Orchestrating Language Agent for Referee-Style Review and Patentability Screening of Quantum Papers and Patents"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.16900"
summary: "arXiv:2608.16900v1 Announce Type: cross Abstract: Language-model agents increasingly produce quantum-science results; we ask whether the same agentic paradigm can also scrutinize them in an auditable,"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.16900v1 Announce Type: cross Abstract: Language-model agents increasingly produce quantum-science results; we ask whether the same agentic paradigm can also scrutinize them in an auditable, reproducible, and cost-transparent form. We present QuantumNovelty, an open-source skill-orchestrating language agent that both generates quantum-computing artifacts (papers, Pareto-front ansatz candidates, and patent drafts) and reviews them through simulated referee and patent-examiner panels. Its design contribution is an audit-and-falsify layer of deterministic gates -- strict Pareto domination, numerical recomputation from on-disk artifacts, Wilson small-sample intervals, and a cross-vendor consensus guard -- that constrains, rather than generates, the claims allowed to survive; every model call is logged with backend, token count, and cost. We make no accuracy claim against human experts, and validate only what is checkable without human labels: on a planted adversarial corpus the deterministic gates catch every planted overclaim with no false positives, and on a first deployment (six manuscripts and one granted patent, at a measured cost of about twenty-four US dollars) the panels are directionally more conservative than the public acceptance record, on a one-sided sample. The framework is decision support, not a replacement for peer review or patent examination, and we report in full where its mechanisms remain unexercised on real inputs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.16900) | 2026-08-19
