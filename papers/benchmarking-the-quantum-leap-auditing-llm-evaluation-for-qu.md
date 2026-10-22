---
title: "Benchmarking the Quantum Leap: Auditing LLM Evaluation for Quantum Code Generation"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.28678"
summary: "arXiv:2610.28678v1 Announce Type: cross Abstract: Large language models (LLMs) can generate quantum programs, but reliable evaluation remains difficult because benchmarks differ in task composition, s"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

arXiv:2610.28678v1 Announce Type: cross Abstract: Large language models (LLMs) can generate quantum programs, but reliable evaluation remains difficult because benchmarks differ in task composition, scoring, and failure handling. We evaluate 15 hosted frontier, open-weight, quantum-specialized, and retrieval-augmented models on five quantum code-generation suites (530 tasks), plus 10 models on our new QuantumBenchEval (QBE) benchmark (96 tasks across six topics). We report bootstrap confidence intervals, multiplicity-adjusted paired comparisons, and audits of output validity and evaluator behavior. QiskitHumanEval-Standard approaches saturation (98.7% pass@1), while its Hard variant retains headroom (63.8%). None of the five top-two comparisons across primary suites remains significant after multiple-comparison correction. Evaluator design substantially changes scores: removing checks for unspecified quantities raises GPT-6 Astra's QBE pass@1 from 0% to 94.1% (T1) and from 1.2% to 92.9% (T6), without changing model outputs. We identify 17 QuanBench-117 tasks with shared failures linked to benchmark-owned imports. Controlled probes also reveal unexecuted unit tests, leakage of canonical functions into candidate execution, and reference imports that block otherwise valid candidates. These defects can produce both false failures and false passes, so historical QuanBench results require revalidation under an isolated evaluator. Overall, leaderboard scores alone do not adequately characterize progress in quantum code generation. We release our harness, per-sample results, and audit artifacts and recommend validating evaluators, isolating candidate code, and reporting uncertainty and output validity.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.28678) | 2026-10-22
