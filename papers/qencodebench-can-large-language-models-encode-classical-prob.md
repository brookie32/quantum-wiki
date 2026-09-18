---
title: "QEncodeBench: Can Large Language Models Encode Classical Problems into Verified Quantum Oracles?"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.20319"
summary: "arXiv:2609.20319v1 Announce Type: new Abstract: Grover search, amplitude amplification, and quantum counting all rely on the same reusable subroutine, a phase oracle, whose construction the algorithms"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2609.20319v1 Announce Type: new Abstract: Grover search, amplitude amplification, and quantum counting all rely on the same reusable subroutine, a phase oracle, whose construction the algorithms literature takes as given: the classical predicate is assumed to be already encoded as a correct, resource-bounded circuit. We turn this assumption into a measured capability. QEncodeBench tasks large language models (LLMs) with encoding classical constraint problems as phase oracles and scores the generated circuits with an adversarially self-validated verifier that decides full solution-set equivalence up to a global phase, with ancillas restored and resource budgets enforced. Sampled basis-state tests, we show, systematically overestimate this ability. Measured this way, models separate sharply: code models without a reasoning mode solve essentially nothing, and enabling native reasoning on identical weights improves accuracy by an order of magnitude. The failures are overwhelmingly semantic rather than syntactic. Two architectures, a unit-verified constraint agent and a neuro-symbolic compilation pipeline, close most of the remaining gap by delegating correctness-critical composition to deterministic procedures. Ablations quantify the contribution of each component, and resource gating exposes an architecture-dependent trade-off between circuit width and depth. Finally, controlled difficulty escalation reveals architecture-specific responses to difficulty structure: different difficulty axes degrade different methods, while the neuro-symbolic pipeline passes every evaluated instance. Code and data are available at https://github.com/chexujun/QEncodeBench.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.20319) | 2026-09-18
