---
title: "CUDA-Q Logical: Retargetable Compilation for Fault-Tolerant Quantum Computing"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.13388"
summary: "arXiv:2609.13388v1 Announce Type: new Abstract: Realizing fault-tolerant quantum computing requires mapping logical programs to heterogeneous quantum error correction (QEC) codes and diverse fault-tol"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.13388v1 Announce Type: new Abstract: Realizing fault-tolerant quantum computing requires mapping logical programs to heterogeneous quantum error correction (QEC) codes and diverse fault-tolerant execution models, scheduling physical resources, and coupling to real-time classical control and feedback. Specialized tools exist for each step but rely on manual composition and translation that discard assumptions and provenance, separating resource estimates from the compiler artifacts they describe, and making it difficult to validate correctness, compare architectures, or attribute costs to specific design choices. We present CUDA-Q Logical, an extensible compiler infrastructure for retargetable fault-tolerant compilation, analysis, and execution. Interoperable with CUDA-Q and other mainstream front-ends, CUDA-Q Logical progressively lowers target-independent logical programs through a constrained logical virtual machine, QEC microcode, physical gate schedules, and real-time control plans, with each layer preserving semantics and provenance, while verifying composition and resource constraints. By deriving every resource estimate directly from compiler artifacts, the framework unifies compilation and resource analysis, enabling successively refined estimates and principled cross-architecture comparison while permitting QEC codes, execution models, decoders, and hardware architectures to be introduced as modular extensions. Across workloads ranging from application-architecture studies to qLDPC surgery and detector-error-model composition, we show that schedule-derived estimates reconcile with established independent models. Crucially, this compiler-visible structure exposes cost drivers hidden by aggregate analytical formulas, carries QEC artifacts intact into simulation, and demonstrates a complete compilation pipeline for fault-tolerant quantum computing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.13388) | 2026-09-15
