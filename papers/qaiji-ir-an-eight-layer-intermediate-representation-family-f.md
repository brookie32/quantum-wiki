---
title: "QaiJi IR: An Eight-Layer Intermediate Representation Family for Hybrid Quantum-Classical Compilation"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.29305"
summary: "arXiv:2609.29305v1 Announce Type: new Abstract: Hybrid quantum-classical compilers exchange programs among circuit, control-flow, pulse, device, and physical representations. Existing formats make dif"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.29305v1 Announce Type: new Abstract: Hybrid quantum-classical compilers exchange programs among circuit, control-flow, pulse, device, and physical representations. Existing formats make different abstraction choices, so the properties that must survive a lowering step are often enforced by tool-specific code rather than stated in a common intermediate representation (IR). We present QaiJi IR, an eight-layer family organized by a five-axis semantic contract for data, semantics, lowering, runtime, and verification. Its L4 SemanticIR records the operation class, declared equivalence level, optimization role, and classical-feedback model as attributes, and maps operation classes to ISA-neutral hardware actions. The prototype provides typed quantum and classical circuit nodes, OpenQASM~2 compatibility input, canonical OpenQASM~3 output, explicit rejection of unsupported constructs, and executable gate-convention checks. A representative measurement-conditioned program reaches a canonical QASM fixed point, acquires a measurement-to-condition edge, passes an exact aggregate consistency check, and produces a symbolic pulse template. For a one-bit active-reset case, device lowering materializes ALU/FPROC records and a conditional branch. Running the resulting virtual pulse processing unit (VPPU) program with externally supplied outcomes 0 and 1 respectively skips and executes the conditional drive. These tests validate the represented compiler path and binary branch behavior. They do not establish a physical feedback loop, because the simulator cannot yet apply mid-circuit measurement collapse and continue the same dynamical trajectory.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.29305) | 2026-09-25
