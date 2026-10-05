---
title: "Query-Limited RAM Programs and their Applications"
date: "2026-10-04"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2336"
summary: "Quantum one-time programs (Broadbent, Gutoski and Stebila, CRYPTO 2013) or OTPs for short, enable a functionality to be encoded into a quantum token that can be evaluated on a single chosen input and "
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Quantum one-time programs (Broadbent, Gutoski and Stebila, CRYPTO 2013) or OTPs for short, enable a functionality to be encoded into a quantum token that can be evaluated on a single chosen input and then becomes unusable. While powerful, this primitive is inherently stateless and tied to a setting in which a quantum token needs to be issued and distributed for every single evaluation of a circuit. This raises a natural question: can the one-time computation paradigm be extended to richer, stateful forms of controlled access, and would such an extension offer inherent advantages beyond standard OTPs? We introduce query-limited RAM programs (QLPs), a RAM-generalization of QOTPs that supports structured, stateful computation under bounded or policy-driven access. QLPs allow controlled sequences of evaluations while preventing adversarial forking or rollback of computational state. This enables new applications beyond stateless one-time programs, including quantum tokens for Turing Machines whose size depends only on code length (and not runtime), transferable k-time or budget-limited programs, and low-communication mechanisms for delegating computation in settings such as Software-as-a-Service. To construct QLPs, we introduce one-shot programs, unifying one-shot signatures (Amos, Georgiou, Kiayias and Zhandry, STOC 2020) with the single effective query paradigm (Gupte, Liu, Raizes, Roberts and Vaikuntanathan, STOC 2025). We prove that one-shot programs generically imply query-limited programs, demonstrating that the strengthened unclonability guarantees of one-shot signatures translate into enhanced functionality. Along the way, we clarify the relationship between signature-token primitives and quantum one-time programs via generic constructions, essentially showing that one-time signing programs imply one-time general computation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2336) | 2026-10-04
