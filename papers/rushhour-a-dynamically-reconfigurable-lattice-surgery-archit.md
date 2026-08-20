---
title: "RushHour: A Dynamically Reconfigurable Lattice-Surgery Architecture"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.18985"
summary: "arXiv:2608.18985v1 Announce Type: new Abstract: Practical fault-tolerant quantum computing (FTQC) requires efficient lattice surgery (LS), so that large algorithms fit on resource-constrained quantum "
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2608.18985v1 Announce Type: new Abstract: Practical fault-tolerant quantum computing (FTQC) requires efficient lattice surgery (LS), so that large algorithms fit on resource-constrained quantum chips. Existing approaches, however, are rigid: qubits, routing space, and resource states are allocated ahead of execution, which prevents running on small chips, leaves statically scheduled executions with large time overheads, and fixes each design at a single area of the space-time trade-off. We present dynamic LS, which enables efficient reconfiguration of the ancilla space, just-in-time allocation of resource states, and dynamic rotations of logical qubits, thereby spanning the entire space-time trade-off with a single, unified approach. We realize dynamic LS with RushHour through a hardware-compiler co-design: the RushHour ISA formalizes and programs our dynamic lattice model, the Lattice Management Unit abstracts dynamic lattice management and performs efficient lattice reconfiguration, and the RushHour Compiler compiles logical circuits for physical chips into optimized ISA programs while pipelining instructions. We evaluate RushHour against six state-of-the-art compilers and two resource models. On the smallest chips, 86% of benchmarks run only with RushHour, while existing approaches require 1.2-3.5imes larger chips. On space-constrained early-FTQC chips, RushHour runs a median 2.0-7.2imes faster than the best feasible alternative, while achieving results comparable to the state of the art on very large chips. RushHour's constructive results run 4.8imes from an idealized-machine resource limit.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.18985) | 2026-08-20
