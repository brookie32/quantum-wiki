---
title: "QuWARP: A Workload-Aware Reuse Planner for simulating Quantum Circuits"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.23664"
summary: "arXiv:2609.23664v1 Announce Type: new Abstract: Quantum circuit simulation often appears as repeated-run workloads rather than isolated circuits: variational quantum eigensolver (VQE) sweeps, noisy mu"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.23664v1 Announce Type: new Abstract: Quantum circuit simulation often appears as repeated-run workloads rather than isolated circuits: variational quantum eigensolver (VQE) sweeps, noisy multishot studies, and quantum error correction (QEC) cycles revisit closely related structure across many runs. Existing simulators optimise individual executions well, but they largely ignore cross-task shared state and therefore repeat work that could be reused safely. We propose QuWARP, a planner-based workload optimiser for a bounded state of the art simulator execution surface: it performs workload-level planning over related tasks, identifies shared prefixes, and chooses when to materialize exact typed boundary artifacts for later reuse across the evaluated statevector mode, and stabilizer-hybrid mode. Its planner treats continuation legality as a narrow correctness guardrail, abstains when reuse is unprofitable, and keeps each reuse, abstention, or refusal decision auditable through EXPLAIN-style traces, meaning inspectable planner reports with provenance and realized-cost summaries. Across real world quantum application workloads QuWARP delivers 2.95x-32.84x speedups over this work's main direct per-task Qrack denominator on reuse-positive workloads. These results show workload-level reuse planning improves repeated-run simulation while keeping unsupported handoffs auditable and out of the execution path.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.23664) | 2026-09-22
