---
title: "Quantum Compiler Design for Fault-Tolerant Quantum Computing"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.17465"
summary: "arXiv:2609.17465v1 Announce Type: new Abstract: Scalable quantum computation is expected to rely on fault-tolerant quantum computation (FTQC), in which quantum error correction (QEC) suppresses physic"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2609.17465v1 Announce Type: new Abstract: Scalable quantum computation is expected to rely on fault-tolerant quantum computation (FTQC), in which quantum error correction (QEC) suppresses physical errors sufficiently to support reliable logical operations. This requires quantum compilation to move beyond general-purpose circuit optimization toward encoding-aware and protocol-structured compilation across the full stack of fault-tolerant quantum computers. Beyond circuit synthesis and hardware mapping, an FTQC compiler must lower algorithm-level operations into the logical gate set supported by the chosen code, coordinate encoded data and ancilla resources, realize logical operations together with repeated syndrome extraction under hardware constraints, and provide the resulting measurement stream to real-time decoding. This survey presents a full-stack view of compiler design for QEC-protected quantum computation. We organize existing work into three interacting layers: logical-level QEC compilation, physical-level QEC realization, and decoder runtime integration. At the logical level, we review surface-code lattice-surgery compilers, beyond-surface-code code-surgery frameworks including emerging qLDPC approaches, and compilation support for non-Clifford operations such as magic-state distillation and code switching. At the physical level, we survey hardware-aware QEC realization on superconducting, trapped-ion, and neutral-atom platforms. We further examine decoder models, real-time decoding systems, and frame-management mechanisms that close the feedback loop during fault-tolerant execution. Finally, we identify open challenges in cross-layer optimization, qLDPC compilation, compiler-decoder co-design, runtime adaptivity, and the development of integrated and benchmarkable FTQC compilation stacks. An actively maintained paper list is available at: github.com/chenghongz/QEC-compiler-design.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.17465) | 2026-09-16
