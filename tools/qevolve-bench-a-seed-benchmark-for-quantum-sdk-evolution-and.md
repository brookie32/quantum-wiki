---
title: "QEVOLVE-Bench: A Seed Benchmark for Quantum SDK Evolution and Repair Planning"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.29492"
summary: "arXiv:2609.29492v1 Announce Type: new Abstract: Quantum software is increasingly built on fast-moving Python SDKs such as Qiskit, PennyLane, and Cirq. When these SDKs evolve, user programs can fail be"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.29492v1 Announce Type: new Abstract: Quantum software is increasingly built on fast-moving Python SDKs such as Qiskit, PennyLane, and Cirq. When these SDKs evolve, user programs can fail because execution helpers are removed, import paths change, simulator abstractions shift, device names are deprecated, or circuit export interfaces are revised. Although some failures surface as simple missing-symbol errors, repairing them is not only a syntactic problem: developers must identify the replacement workflow, preserve the quantum-facing intent, and validate behavior under pinned framework versions. This paper presents QEVOLVE-Bench, a small executable seed benchmark for quantum SDK evolution. The current public release contains 14 controlled migration tasks across Qiskit, PennyLane, and Cirq. Each task is a self-contained Python project with pinned dependencies, failing and passing outputs, pytest acceptance checks, metadata, and benchmark notes. The artifact also includes a manifest, sanity checker, representative smoke-test logs, Zenodo archive, screencast, and a lightweight QEVOLVE-Agent prototype that converts task evidence into structured repair proposals. QEVOLVE-Bench is intentionally not a statistically powered benchmark; instead, it is an extensible seed artifact that lowers the setup cost for studying automated repair, LLM-based software engineering, and maintenance of quantum SDK-based projects.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.29492) | 2026-09-25
