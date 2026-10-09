---
title: "Autonomous Code Migration for Quantum Programming Languages: A Case Study with QED-C Benchmarks"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.12187"
summary: "arXiv:2610.12187v1 Announce Type: new Abstract: Quantum programming requires concepts and intuition that differ substantially from those used in traditional programming languages. Multiple quantum pro"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.12187v1 Announce Type: new Abstract: Quantum programming requires concepts and intuition that differ substantially from those used in traditional programming languages. Multiple quantum programming frameworks address these requirements through different abstractions and execution models, creating tradeoffs in programmability, portability, and performance. Because quantum software is less prevalent in the training data available to large language models, autonomous coding agents might be expected to face additional challenges when working with these frameworks. We present a case study in autonomous migration of the QED-C Application-Oriented Benchmarks from Qiskit to CUDA-Q. Opus, GPT, and Gemini models were each tasked with porting thirteen benchmark methods spanning foundational algorithms, amplitude estimation, Monte Carlo methods, variational optimization, linear-system solving, and factoring. In all cases, the models were able to generate satisfactory ports with little direct coding help and there was a drastic reduction in the time required compared to a human engineer. However, in all cases, the agents resorted to shortcuts when implementation challenges surfaced and multiple prompts were required to force appropriate coding directions. Assessment of the generated implementations showed that no single model consistently produced the best port across all benchmarks, indicating that multi-agent ensemble strategies could mitigate challenges associated with quantum software. The effort resulted in publicly available, near-complete CUDA-Q support in the QED-C benchmarks along with model-generated skills designed to improve agent performance when implementing CUDA-Q applications. When tested on an unseen benchmark, these skills reduced the required model turns by up to 85% and token usage by up to 96%. We conclude by distilling lessons from the case study.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.12187) | 2026-10-09
