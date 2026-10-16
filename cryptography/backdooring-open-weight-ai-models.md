---
title: "Backdooring Open-Weight AI Models"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "cryptography"
tags: [cryptography, schneier-on-security]
url: "https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html"
summary: "This is a problem: Any open model whose weights have been edited can carry a backdoor, whether it’s a task-specific fine-tune, a merged adapter or an abliterated build. We have abliterated models in t"
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

This is a problem: Any open model whose weights have been edited can carry a backdoor, whether it’s a task-specific fine-tune, a merged adapter or an abliterated build. We have abliterated models in the title because it’s the most popular reason people download modified weights without verifying what’s inside. Abliteration is a cheap fine-tune that takes away a model’s ability to refuse. You find the direction in the weights that carries “no” and subtract it. The model then answers things a safety-tuned version would turn down. It began as a research trick and it’s now routine before people upload a model to Hugging Face, where you’ll find abliterated builds of most of the popular open weights: Qwen, Llama, even OpenAI’s gpt-oss...

**Source:** [Schneier on Security](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html) | 2026-10-16
