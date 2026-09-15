---
title: "OpenQARP: a modular framework for quantum application research"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.15697"
summary: "arXiv:2609.15697v1 Announce Type: new Abstract: We introduce OpenQARP, the Open Quantum Application Research Package: an open-source Python framework for quantum application research, built on a compi"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.15697v1 Announce Type: new Abstract: We introduce OpenQARP, the Open Quantum Application Research Package: an open-source Python framework for quantum application research, built on a compiled C++ core. In OpenQARP, an application is assembled from an algorithm library that orchestrates three interchangeable layers: blocks describe circuits, primitives describe what to extract from them, and engines describe how they run. The release spans near-term through fault-tolerant methods, targeting problems from electronic structure to combinatorial optimization, with device-aware compilation, circuit cutting, and resource estimation over a single set of numerical conventions that the code must follow. Every numerical feature is checked against an independent oracle, and every published timing carries a correctness check. Against OpenFermion, Qiskit/Aer, PennyLane/Lightning, Qulacs, qsim, and pytket, OpenQARP is one to two orders of magnitude faster on operator algebra and among the fastest on simulation. It matches mature compilers on two-qubit gate count, and expresses a complete algorithm in the lines a framework needs rather than the plumbing a primitive stack demands.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.15697) | 2026-09-15
