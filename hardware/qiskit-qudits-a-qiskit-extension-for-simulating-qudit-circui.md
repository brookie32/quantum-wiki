---
title: "qiskit-qudits: A Qiskit Extension for Simulating Qudit Circuits"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.22032"
summary: "arXiv:2608.22032v1 Announce Type: new Abstract: qiskit-qudits is a Qiskit extension that simulates d-level qudits by encoding each one into m = ceil(log_2 d) qubits. Qudit gates are exposed as ordinar"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2608.22032v1 Announce Type: new Abstract: qiskit-qudits is a Qiskit extension that simulates d-level qudits by encoding each one into m = ceil(log_2 d) qubits. Qudit gates are exposed as ordinary Qiskit Gate and ControlledGate subclasses, and operations that are not unitary gates (measurement, reset, barrier, state preparation) as dedicated Instruction subclasses dispatched through a dedicated apply() hook; every gate carries both a dense encoded unitary (via NumPy's array protocol) and a qubit-level definition. Because d need not be a power of two, the encoded Hilbert space is generally larger than the logical one; the library resolves this by the identity-padding convention, in which every gate acts as the identity on the unphysical part of the encoded space. When every operand dimension is a power of two, gates decompose into a fixed, transpiler-recognisable cascade of standard qubit gates; otherwise the library falls back to exact dense unitary synthesis, so that dimensions 2 <= d <= 16 are supported exactly, not only powers of two. This paper describes the software's circuit model, gate hierarchy, decomposition strategy, and measurement/decoding machinery, states its limitations, and verifies the implementation numerically: the qudit QFT against the discrete Fourier transform for both power-of-two and non-power-of-two d, extending the check of the underlying theory paper, which could only be run for d = 2^m, and every gate's emitted decomposition against its dense unitary across the whole gate set.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.22032) | 2026-08-25
