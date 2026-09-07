---
title: "A Compilation Framework for Quantum Simulation of Non-unitary Dynamics"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.23358"
summary: "arXiv:2605.23358v2 Announce Type: replace Abstract: Most quantum compilers assume programs are reversible unitary circuits. This fits closed-system algorithms, but not open-system simulation, where th"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2605.23358v2 Announce Type: replace Abstract: Most quantum compilers assume programs are reversible unitary circuits. This fits closed-system algorithms, but not open-system simulation, where the natural program objects are quantum channels describing non-unitary dynamics. We present a channel-first compilation framework that treats channels as first-class compilation objects. Our core IR, ChannelIR, represents channels explicitly in Kraus form, a standard channel representation, with Pauli-sum structure, enabling algebraic rewrites before circuit synthesis. We instantiate the framework with LindFront, a frontend that lowers continuous-time Lindbladian generators to short-time channels, and a backend that compiles these channels to executable circuits with structure-aware optimizations. On Lindbladian and channel-simulation benchmarks, the optimized pipeline reduces gate count by up to 99% over an unoptimized channel-first baseline and scales better than circuit-first Stinespring compilation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.23358) | 2026-09-07
