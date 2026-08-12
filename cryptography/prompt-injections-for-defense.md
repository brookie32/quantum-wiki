---
title: "Prompt Injections for Defense"
date: "2026-08-12"
updated: "2026-08-12"
source: "agent"
category: "cryptography"
tags: [cryptography, schneier-on-security]
url: "https://www.schneier.com/blog/archives/2026/08/prompt-injections-for-defense.html"
summary: "This seems to work: Researchers from Tracebit on Monday said they found that placing prompt injections alongside passwords, cryptographic keys, and other secrets stored on Amazon Web Services was ofte"
last_verified: "2026-08-12"
review_by: "2026-11-10"
stale: false
---

This seems to work: Researchers from Tracebit on Monday said they found that placing prompt injections alongside passwords, cryptographic keys, and other secrets stored on Amazon Web Services was often all that was needed to shut down attacks from AI hacking agents. The prompts direct the attacking LLM to perform an action forbidden by its guardrails, the safety barriers AI developers erect to prevent it from taking harmful actions. The LLM responds by shutting down. Examples are a prompt that orders the LLM to provide steps for developing inhalable Anthrax spores, or, in the case of LLMs from Chinese developers, make references to the iconic Tank Man from the 1989 Tiananmen Square massacre. Once the LLM encounters these forbidden commands, it no longer follows its existing commands. The researchers have named the technique context bombing...

**Source:** [Schneier on Security](https://www.schneier.com/blog/archives/2026/08/prompt-injections-for-defense.html) | 2026-08-12
