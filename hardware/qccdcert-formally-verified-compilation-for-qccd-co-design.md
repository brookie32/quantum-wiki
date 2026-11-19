---
title: "QCCDCert: Formally Verified Compilation for QCCD Co-Design"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.23469"
summary: "arXiv:2611.23469v1 Announce Type: new Abstract: Quantum charge-coupled device (QCCD) architectures enable scalable trapped-ion quantum computing by dynamically shuttling ions between specialized proce"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.23469v1 Announce Type: new Abstract: Quantum charge-coupled device (QCCD) architectures enable scalable trapped-ion quantum computing by dynamically shuttling ions between specialized processing and storage zones. A QCCD can be built with many trap sizes and layouts. Comparing them requires compiling every program under each design's transport, capacity and control constraints, and trusting the target code of each compilation. We present a co-design framework built on one Lean-verified compiler. The hardware description and its operating rules are compiler inputs, so a single theorem covers every candidate design: the target code of every compilation preserves its program's behavior and obeys the hardware rules. Across 75 benchmark programs of 11 to 130 qubits, the best design found takes 66% less modeled execution time on average than the worst design of equal capacity. An AI agent that proposes devices based on our compiler's checked results beats the fastest of these designs on 71 of 75 programs. Our verified compiler provably avoids the 11 defects that we report in three previous compilers. It scales to hundreds of qubits, compiling 512-qubit programs for a 38-trap device in 1 to 29 minutes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.23469) | 2026-11-19
