---
title: "Stateful LLM Guardrails without Surveillance via Anonymous Risk Token"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3046"
summary: "Safety guardrails for large language models (LLMs) judge each message on its own, yet multi-turn jailbreaks spread a harmful request over messages that each look benign. To catch them, a guardrail mus"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Safety guardrails for large language models (LLMs) judge each message on its own, yet multi-turn jailbreaks spread a harmful request over messages that each look benign. To catch them, a guardrail must remember the user's earlier messages. If the provider, who hosts and runs the model, keeps this memory, it holds a permanent record of every user, almost all of whom are innocent, along with how suspicious the guardrail judged each of their private queries. One data breach, court order, or change of policy could expose this record. If the user keeps the memory instead, a malicious user can roll it back or reset it. We therefore ask whether a guardrail can remember what it needs for safety without profiling its users. We first show that a guardrail needs far less memory than a full transcript: two numbers per user suffice. Using the classifier Llama Guard 3 on about 10,000 public conversations from automated multi-turn attacks, human red-teaming, and real users, we keep a fast and a slow running average of each user's scores; when the fast one rises above the slow one, the user's messages are becoming more harmful. At a 5% false-alarm rate, the two averages detect 34% of escalating attacks, against 25% for judging each message on its own. Kept across conversations, they cannot be evaded by splitting an attack over several conversations, unlike memory that restarts with each one. Against red-team attacks, which are often harmful from the first message, memory adds little. To keep these averages without a profile, we introduce and design a new cryptographic primitive, anonymous risk tokens (ART), in which the user holds its own averages. For each message, the provider learns only a coarse risk level (e.g., low or high) and cannot link it to the user's earlier conversations; the user cannot lower, roll back, or copy its averages, or reset them without forfeiting a prepaid balance. We formalize the security of ART and give a provably secure construction from Pointcheval-Sanders (PS) blind signatures and zero-knowledge arguments. The price is some loss of detection within a single conversation, because the averages must start from a public value. We implement a prototype of ART in Rust and evaluate it: each message takes each party about 0.4s on one laptop core, and the user uploads 90KB, regardless of the history length.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3046) | 2026-11-25
