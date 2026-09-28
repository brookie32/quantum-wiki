---
title: "QASM-Eval: A Dataset to Train and Evaluate LLMs on OpenQASM-3 Beyond Quantum Circuits"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.30358"
summary: "arXiv:2605.30358v2 Announce Type: replace-cross Abstract: Quantum computing remains in the Noisy Intermediate-Scale Quantum (NISQ) era, with performance constrained by noise. Addressing this limitatio"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2605.30358v2 Announce Type: replace-cross Abstract: Quantum computing remains in the Noisy Intermediate-Scale Quantum (NISQ) era, with performance constrained by noise. Addressing this limitation requires hardware-facing capabilities beyond gate sequences: mid-circuit measurement and classical feedback for quantum error correction (QEC), precise timing for dynamical decoupling (DD), and pulse-level waveform access for calibration. OpenQASM 3 exposes these capabilities through a hardware-level programming interface. Despite rapid progress in large language models (LLMs) for code generation, datasets targeting these advanced features remain lacking. We introduce QASM-Eval, the first comprehensive dataset to train and evaluate LLMs on OpenQASM 3, targeting completion of hardware-facing constructs within a supplied program context. QASM-Eval comprises an expert-curated test set of 1,200 tasks and a training set of over 4,000 tasks, covering classical logic, timing scheduling, pulse control, and complex tasks inspired by quantum-control workflows. An extended verifier automatically checks syntax, quantum measurement distributions, and program timelines. Our evaluation identifies substantial headroom for OpenQASM 3 code generation and significant gains from targeted fine-tuning. Fine-tuned Llama-3-8B outperforms zero-shot GPT-5.6-Terra, while fine-tuned Llama-3-70B achieves 61.17% overall pass@1 and approaches few-shot-augmented GPT-5.6-Terra. QASM-Eval provides a benchmark and training resource for specification-guided code generation over the hardware-facing constructs of OpenQASM 3, supporting the development of LLM assistants for quantum programming. Data and code: https://github.com/fuzhenxiao/QASM-Eval

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.30358) | 2026-09-28
