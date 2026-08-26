---
title: "StabQ: Quantum Program Analysis via Weighted Stabilizer Representations"
date: "2026-08-26"
updated: "2026-08-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.24144"
summary: "arXiv:2608.24144v1 Announce Type: cross Abstract: Quantum program analysis remains challenging due to the exponentially large state space of quantum programs and the difficulty of precisely characteri"
last_verified: "2026-08-26"
review_by: "2026-11-24"
stale: false
---

arXiv:2608.24144v1 Announce Type: cross Abstract: Quantum program analysis remains challenging due to the exponentially large state space of quantum programs and the difficulty of precisely characterizing their execution behavior. In particular, non-Clifford operations introduce additional complexity that limits the applicability of stabilizer-based techniques. Although stabilizer representations provide compact descriptions for Clifford circuits, their limited expressiveness prevents them from directly supporting general quantum program analysis. In this work, we propose StabQ, a symbolic execution framework for quantum program analysis based on stabilizer representations. StabQ extends stabilizer-based symbolic execution beyond Clifford-only programs by introducing a symbolic state representation that captures and propagates quantum state evolution while preserving execution semantics. Based on this representation, StabQ constructs a Tableau Chain that represents the evolution of intermediate symbolic states throughout program execution and enables reusable analysis of quantum program executions. Furthermore, StabQ incorporates tableau consolidation and global-phase recovery mechanisms to mitigate symbolic state growth during execution. Building upon the Tableau Chain, StabQ supports multiple quantum program analysis tasks, including quantum state reconstruction, entanglement analysis, and Clifford-property detection. We evaluate StabQ on three benchmark suites---Algorithms, MQT Bench, and QASMBench. The results demonstrate that StabQ constructs semantically consistent symbolic models, accurately preserves quantum state evolution, and effectively supports downstream analysis tasks across diverse quantum programs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.24144) | 2026-08-26
