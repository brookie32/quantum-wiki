---
title: "Rachel: A general-purpose language model directs and revises retrosynthetic routes"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.25118"
summary: "arXiv:2609.25118v1 Announce Type: new Abstract: Retrosynthetic planning advances through decisions that reshape the remaining chemical problem: a locally plausible disconnection can leave precursors w"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.25118v1 Announce Type: new Abstract: Retrosynthetic planning advances through decisions that reshape the remaining chemical problem: a locally plausible disconnection can leave precursors whose chemoselectivity constraints complicate the rest of the route. Existing planners often channel model proposals through search or template procedures, leaving open whether a general-purpose large language model (LLM) can itself sustain and revise route strategy. We developed Rachel, a stateful environment that executes and checks LLM-directed chemistry but prescribes neither a search policy nor a stopping rule. Without supplied reference routes or route-level solutions, GPT-5.5 achieved strict closure for 111 of 120 PaRoutes120 targets and 24 of 25 targets in the separate RF25 difficult-target cohort. RF25 was drawn largely from studies published after GPT-5.5's reported knowledge cutoff. Closure required complete routes and independent source resolution of every terminal precursor after planning. On a shared PaRoutes subset, forward-model support exceeded that of most comparator methods, and Rachel received the highest mean overall route score from both method-blinded LLM evaluators. Recorded trajectories showed continued model-proposed chemistry, with revised strategies carried into subsequent steps. Replacing LLM route decisions with fixed policies reduced strict closure to 6-15/120 despite continued local chemical execution; restricting planning support also reduced closure in RF25. Within Rachel, a general-purpose LLM coordinated successive chemical choices and revised its strategy as earlier decisions reshaped the remaining problems.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.25118) | 2026-09-23
