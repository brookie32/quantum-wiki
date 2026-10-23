---
title: "ConQEC: Concolic Testing for Quantum Error-Correcting Code Implementations"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.31443"
summary: "arXiv:2610.31443v1 Announce Type: new Abstract: Quantum error-correcting code (QECC) implementations are hybrid software-control systems: measured syndromes drive decoder dispatch, recovery actions, a"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2610.31443v1 Announce Type: new Abstract: Quantum error-correcting code (QECC) implementations are hybrid software-control systems: measured syndromes drive decoder dispatch, recovery actions, and logical checks. Existing QECC verification techniques can prove formal obligations, and general quantum testing can expose final failures, but developers still lack a scalable testing workflow that generates concrete faults and explains where a QECC repair path first diverges. This paper presents ConQEC, to our knowledge the first concolic testing framework for QECC implementations. By combining concrete (Pauli) fault replay with symbolic repair-path constraints, ConQEC generates tests that expose not only final logical failures but also fault--syndrome--decoder--recovery (FSDR) diagnostics: the injected fault, observed syndrome, decoder decision, recovery action, oracle result, and earliest divergent stage. Its symbolic encoding of Pauli faults, syndrome predicates, decoder and recovery relations, and oracle checks enables this diagnostic workflow to scale beyond exponentially increasing amplitude-level quantum-state reasoning. We implemented ConQEC and evaluated it on generated source-level QECC families and public QECC artifacts with up to thousands of qubits. ConQEC detects the seeded bug in every experimental case and reports a replay-valid, fault-localizing FSDR witness for each.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.31443) | 2026-10-23
