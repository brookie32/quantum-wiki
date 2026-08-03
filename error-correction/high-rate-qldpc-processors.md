---
title: "High-rate qLDPC processors"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.28795"
summary: "arXiv:2607.28795v1 Announce Type: new Abstract: Despite significant progress on quantum low-density parity-check (qLDPC) codes, building qLDPC processors that are high-rate, high-throughput, hardware-"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

arXiv:2607.28795v1 Announce Type: new Abstract: Despite significant progress on quantum low-density parity-check (qLDPC) codes, building qLDPC processors that are high-rate, high-throughput, hardware-friendly, and fast-to-decode remains a challenge. We introduce mitten codes, a family of qLDPC processor codes of encoding rate 20% and check weight 9, based on non-abelian groups. Their non-abelian structure evades distance bounds constraining abelian counterparts, allowing mitten codes to reach distance 18 and beyond with just a few hundred data qubits. The logical operators of a mitten code are related by the group action, yielding a modular, low-overhead logical toolkit: full Clifford operations follow from bridging two reusable seed surgery gadgets or from a single fixed extractor. Furthermore, qLDPC processors based on mitten codes support high-rate surgery that executes many logical measurements in parallel, and parallel magic-state injection into all logical qubits at once. Under circuit-level noise, with our fast decoder, the [![300,60,14]!] mitten code achieves, without extrapolation, a block logical error rate of {sim}10^{-11} per round at 0.1% physical error rate (PER), while the [![ 975,195,leq 24 ]!] code reaches {sim}10^{-8} at 0.4% PER. Decoding 15 billion surgery experiments on the [![540,108,18]!] code at 0.1% PER, we observe only two logical failures, demonstrating a qLDPC processor capable of running {sim}10^{10} logical operations. Our decoder is compatible with sub-millisecond average latency per logical cycle, sufficient for real-time decoding on neutral atom hardware. Discovered by an end-to-end design pipeline built on sQetch, a distance estimator orders of magnitude faster than existing tools, and mapping efficiently onto near-term neutral atom and superconducting hardware, mitten codes open a practical path toward fault-tolerant quantum computation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.28795) | 2026-08-03
