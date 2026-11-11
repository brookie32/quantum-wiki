---
title: "Secure Information Flow in Quantum Programs"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.14147"
summary: "arXiv:2611.14147v1 Announce Type: new Abstract: Information-flow security aims to prevent the leakage of confidential information through program execution. This problem becomes fundamentally subtler "
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.14147v1 Announce Type: new Abstract: Information-flow security aims to prevent the leakage of confidential information through program execution. This problem becomes fundamentally subtler for quantum programs, because their states may involve superposition and entanglement, and their executions may involve intricate interactions between classical and quantum variables. This paper develops semantic foundations and verification methods for secure information flow in quantum programs. We formulate two notions of information-flow security. The first is a noninterference-based definition that naturally generalizes its classical counterpart. The second is a simulation-based definition that explicitly models an attacker, providing a clear operational interpretation of security. We prove that these two notions are equivalent. To verify the information-flow security of quantum programs, we develop a proof framework based on quantum Hoare logic. A key challenge is that the standard self-composition technique, which expresses information-flow security in Hoare logic by composing a program with a renamed copy of itself, fails in the quantum setting due to an obstruction analogous to the no-cloning theorem. To overcome this challenge, we introduce self-conjugation, a novel technique that leverages the deferred measurement principle and properties of unitary operations. We demonstrate our framework on examples drawn from the quantum one-time pad, quantum error correction, and anonymous entanglement generation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.14147) | 2026-11-11
