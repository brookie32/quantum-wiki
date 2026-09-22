---
title: "QuantumSavory: symbolic modeling and multi-backend simulation of quantum computing and networking systems"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.16752"
summary: "arXiv:2512.16752v2 Announce Type: replace Abstract: Progress in quantum computing and networking depends on codesign across abstraction layers: device-level noise and heterogeneous hardware, algorithm"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2512.16752v2 Announce Type: replace Abstract: Progress in quantum computing and networking depends on codesign across abstraction layers: device-level noise and heterogeneous hardware, algorithmic structure, and distributed classical control. We present QuantumSavory, an open-source toolkit built to make such end-to-end studies practical by cleanly separating a symbolic computer-algebra frontend from interchangeable numerical simulation backends. States, operations, measurements, and protocol logic are expressed in a backend-agnostic symbolic language; the same model can be executed across multiple backends (e.g., stabilizer, wavefunction, phase-space), enabling rapid exploration of accuracy-performance tradeoffs without rewriting the model. Furthermore, new custom backends can be added via a small, well-defined interface that immediately reuses existing models and protocols. QuantumSavory also addresses the classical-quantum interaction inherent to LOCC protocols via discrete-event execution and a tag/query system for coordination. Tags attach structured classical metadata to quantum registers and message buffers, and queries retrieve, filter, or wait on matching metadata by wildcards or arbitrary predicates. This yields a data-driven control plane where protocol components coordinate by publishing and consuming semantic facts (e.g., resource availability, pairing relationships, protocol outcomes) rather than by maintaining rigid object graphs or bespoke message plumbing, improving composability and reuse as models grow. Our toolkit is also not limited to qubits and Bell pairs; rather, any networking dynamics of any quantum system under any type of multipartite entanglement can be tackled. Lastly, QuantumSavory ships reusable libraries of standard states, circuits, and protocol building blocks with consistent interfaces, enabling full-stack examples to be assembled, modified, and compared with minimal glue code.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.16752) | 2026-09-22
