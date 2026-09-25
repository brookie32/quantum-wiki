---
title: "Representation-Dependent Recoverability in Quantum Compilation"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.29210"
summary: "arXiv:2609.29210v1 Announce Type: new Abstract: Fault-tolerant compilation can disperse high-level structure: schedules split an accumulated phase across rounds, gate synthesis replaces an angle by a "
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.29210v1 Announce Type: new Abstract: Fault-tolerant compilation can disperse high-level structure: schedules split an accumulated phase across rounds, gate synthesis replaces an angle by a Clifford+T word, and randomized compiling spreads rotations over sign-randomized fragments. They preserve the computation but change how cheaply a downstream compiler can recover the aggregate phase data. We formalize this representation-dependent recoverability by charging two channels: output committed before the suffix arrives, and a serialized restart state crossing the cut. For an r-round accumulation of a commuting layer with m generators at accuracy epsilon (K_epsilon=Theta(1/epsilon)), any p-pass compiler correct on every valid stream with failure probability at most elta obeys overline{A}_p+(2p-1)Sgeq(1-elta)mlog_2 K_epsilon-h_2(elta), where overline{A}_p is committed output and S is the crossing-state cap. The bound covers compile-time randomized compiling; a memory-capped block compiler attains it within a constant factor, and direct semantic aggregation reaches compact output with logarithmic state. The two channels are not always interchangeable. A compiler whose committed prefix is executed at the cut pays a toll the state channel never pays: the entropy log_2inom{m}{k} of the mask naming which k coordinates it commits early. Compilers that defer or buffer pay none of it. We prove both directions and, with instrumented compilers under a preregistered protocol, measure a per-generator toll matching log_2inom{m}{k}/k that vanishes for a public mask and a buffered control. Under a disclosed fixed-total-error Clifford+T and surface-code model, a materialize-first pipeline costs orders of magnitude more logical T states and spacetime volume than a semantic-first one. Phase semantics should therefore be preserved until aggregation whenever the interface permits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.29210) | 2026-09-25
