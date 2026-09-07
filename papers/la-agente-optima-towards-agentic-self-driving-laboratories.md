---
title: "La Agente Optima: Towards Agentic Self-Driving Laboratories"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.04564"
summary: "arXiv:2609.04564v1 Announce Type: cross Abstract: Self-driving laboratories (SDLs) combine automated experimentation with adaptive decision-making to accelerate scientific discovery. Their operation n"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2609.04564v1 Announce Type: cross Abstract: Self-driving laboratories (SDLs) combine automated experimentation with adaptive decision-making to accelerate scientific discovery. Their operation nevertheless often depends on human specialists who translate scientific objectives into executable closed-loop campaigns. Specialists adjust them as data and operating conditions change. Here, we present La Agente Optima, an agentic framework that constructs and supervises Bayesian optimization campaigns across computational and experimental systems while maintaining a persistent optimization state. By separating large language model (LLM) reasoning from executed campaigns, Optima runs repetitive optimization loops consistently, returns control to the agent only when progress requires interpretation or campaign revision, and keeps every decision auditable. We evaluate Optima across ablation studies, five digital discovery tasks, and two physical platforms. Throughout, Optima maintained executable campaigns as both the scientific problem and execution environment evolved. In a closed-loop contact angle optimization campaign, Optima identified and corrected a mid-run measurement failure, bringing the contact angle from 71.4 to 67.8 degrees, just above the 64-66 degree range. From this result, Optima correctly inferred that the target was likely unattainable with the available reagents and recommended changing the formulation. In a five-day multi-objective flow-chemistry campaign, Optima increased the yield from 30% to 59% over 23 experiments. Despite substantial inference costs, it cost less and used substantially less starting material than a human-directed campaign, while selecting a more mass-efficient operating point. These results show that LLM-based agents can make rigorous, long-running optimization campaigns accessible to domain scientists without specialist setup, expanding the scope of SDLs.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.04564) | 2026-09-07
