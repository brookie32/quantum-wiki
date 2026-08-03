---
title: "More on the OpenAI Agent’s Attack on Hugging Face"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "cryptography"
tags: [cryptography, schneier-on-security]
url: "https://www.schneier.com/blog/archives/2026/08/more-on-the-openai-agents-attack-on-hugging-face.html"
summary: "Hugging Face has published a detailed timeline of the attack. From the summary: The agent was running an internal OpenAI cyber-capability evaluation based on the ExploitGym benchmark, which tasks an A"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

Hugging Face has published a detailed timeline of the attack. From the summary: The agent was running an internal OpenAI cyber-capability evaluation based on the ExploitGym benchmark, which tasks an AI agent with finding and exploiting software vulnerabilities. OpenAI ran this on its own infrastructure, and the ExploitGym maintainers and their infrastructure had no involvement in the deployment or operation of that evaluation environment. As far as we were able to infer, across the course of being evaluated on this benchmark, the agent inferred that Hugging Face may host that benchmark’s models, datasets, and reference solutions. We believe the entire intrusion was, from the agent’s point of view, an attempt to cheat the evaluation: reach our production systems and steal the test solutions rather than solve the challenge on its own...

**Source:** [Schneier on Security](https://www.schneier.com/blog/archives/2026/08/more-on-the-openai-agents-attack-on-hugging-face.html) | 2026-08-03
