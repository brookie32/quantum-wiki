---
title: "QMClaw: A Scalable General-purpose Framework for Quantum Measurement and Control"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.04674"
summary: "arXiv:2609.04674v1 Announce Type: new Abstract: As quantum computing continues to scale, quantum measurement and control (QMC) are increasingly constrained by calibration workflow complexity and by re"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2609.04674v1 Announce Type: new Abstract: As quantum computing continues to scale, quantum measurement and control (QMC) are increasingly constrained by calibration workflow complexity and by requirements for low-latency execution, robust exception handling, and traceable workflow governance. Existing frameworks for QMC are specialized and task-specific, while language-model-based agents for QMC suffer from excessive latency and cannot satisfy the strict timing and control-density demands of large-scale quantum systems. Here we propose QMClaw, a general, workflow-oriented framework for QMC built, featuring a local-first, tool-governed, robust architecture. At its core is a RuleEngine-centered control layer that processes structured context, performs rule-based state transitions, and generates execution plans for typical calibration workflows. Language models are used only for natural-language interaction, high-level task understanding, and exception support, keeping the critical fast path efficient. We implement a single qubit tune-up workflow as a demonstration and validation using real quantum device dataset. We also prove that the framework achieves quantitatively acceptable levels in terms of resource cost, LLM calling times and decision latency, enabling its practical deployment in large-scale quantum qubit measurement and control scenarios. This work presents a general workflow-oriented framework for QMC and provides evidence that rule-centered architectures are a promising design choice for scalable quantum-system calibration.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.04674) | 2026-09-07
