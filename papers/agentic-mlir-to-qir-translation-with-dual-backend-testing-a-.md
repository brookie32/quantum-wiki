---
title: "Agentic MLIR-to-QIR Translation with Dual-Backend Testing: A Hybrid Deterministic and LLM Approach"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.25106"
summary: "arXiv:2611.25106v1 Announce Type: new Abstract: Quantum frameworks each define their own Multi-Level Intermediate Representation (MLIR) dialect, so porting a circuit to a Quantum Intermediate Represen"
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2611.25106v1 Announce Type: new Abstract: Quantum frameworks each define their own Multi-Level Intermediate Representation (MLIR) dialect, so porting a circuit to a Quantum Intermediate Representation (QIR) runtime needs a hand-written pass per dialect. Our translator selects among three paths: a deterministic compiler path for known grammars (Catalyst and Quake), a large language model (LLM) agentic path for unseen dialects, and a repair path invoked when deterministic output fails testing. A dual-backend pipeline executes the source MLIR and generated QIR on independent simulators, comparing output distributions by total variation distance (TVD). For smaller open-weight models we replace retrieval-augmented generation with inline context engineering and add a guardrail-assembler that rebuilds valid QIR from incomplete output. Across 41 circuits spanning three dialects and 1-100 qubits, the deterministic path is gate-exact on all 70 circuit-dialect pairs, averaging above 95% TVD similarity (1-TVD). On an unseen fault-tolerant (FTQC) dialect, four of six models produce valid logical-level QIR on the first iteration.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.25106) | 2026-11-20
