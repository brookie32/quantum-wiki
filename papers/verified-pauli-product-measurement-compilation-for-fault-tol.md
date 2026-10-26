---
title: "Verified Pauli-Product Measurement Compilation for Fault-Tolerant Quantum Computation"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.31694"
summary: "arXiv:2610.31694v1 Announce Type: new Abstract: Fault-tolerant quantum compilers implement gates through Pauli-product measurements and classical feedback. Verifying such a compiler requires reasoning"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2610.31694v1 Announce Type: new Abstract: Fault-tolerant quantum compilers implement gates through Pauli-product measurements and classical feedback. Verifying such a compiler requires reasoning about the quantum state and the recorded outcomes together: a correction reads an outcome, a gate's internal outcomes must be hidden from its caller, and an application's outcomes must survive optimization. We introduce QPPM, a language for Pauli-product measurement programs, with a weakest-precondition semantics over store-indexed matrix assertions, following quantum Hoare logic with classical variables. Every program terminates, so the Hoare logic is a syntactic presentation of weakest preconditions whose soundness and relative completeness are immediate. Its value is that component specifications compose. All results are mechanized in Lean. We verify lowering of Clifford+T circuits to QPPM with private outcomes and supplied magic states, and an optimizer that eliminates measurements, fuses and reorders rotations, and schedules logical rounds while preserving every outcome that subsequent code can read. A compositional approximation relation bounds the effect of synthesis error on specifications and on output trace distance, and a certificate-checked pipeline selects, among synthesized circuits that meet the user's error limit, the one with the lowest certified depth bound. On QASMBench, verified fusion and scheduling reduce logical measurement depth by a median of 17.9%, and complete source-to-QPPM allowances are certified for all 35 valid selected small-suite inputs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.31694) | 2026-10-26
