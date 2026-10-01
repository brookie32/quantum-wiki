---
title: "Query-Limited RAM Programs and their Applications"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40194"
summary: "arXiv:2609.40194v1 Announce Type: new Abstract: Quantum one-time programs (Broadbent, Gutoski and Stebila, CRYPTO 2013) or OTPs for short, enable a functionality to be encoded into a quantum token tha"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40194v1 Announce Type: new Abstract: Quantum one-time programs (Broadbent, Gutoski and Stebila, CRYPTO 2013) or OTPs for short, enable a functionality to be encoded into a quantum token that can be evaluated on a single chosen input and then becomes unusable. While powerful, this primitive is inherently stateless and tied to a setting in which a quantum token needs to be issued and distributed for every single evaluation of a circuit. This raises a natural question: can the one-time computation paradigm be extended to richer, stateful forms of controlled access, and would such an extension offer inherent advantages beyond standard OTPs? We introduce extit{query-limited RAM programs} (QLPs), a RAM-generalization of QOTPs that supports structured, stateful computation under bounded or policy-driven access. QLPs allow controlled sequences of evaluations while preventing adversarial forking or rollback of computational state. This enables new applications beyond stateless one-time programs, including quantum tokens for Turing Machines whose size depends only on extit{code length} (and not runtime), transferable k-time or budget-limited programs, and low-communication mechanisms for delegating computation in settings such as Software-as-a-Service. To construct QLPs, we introduce extit{one-shot programs}, unifying one-shot signatures (Amos, Georgiou, Kiayias and Zhandry, STOC 2020) with the single effective query paradigm (Gupte, Liu, Raizes, Roberts and Vaikuntanathan, STOC 2025). We prove that one-shot programs generically imply query-limited programs, demonstrating that the strengthened unclonability guarantees of one-shot signatures translate into enhanced functionality. Along the way, we clarify the relationship between signature-token primitives and quantum one-time programs via generic constructions, essentially showing that one-time signing programs imply one-time general computation.



## Related
- [[a-noise-operator-approach-to-quantum-query-complexity-and-ti|A Noise Operator Approach to Quantum Query Complexity and Time-Space Tradeoff Lower Bounds]]
- [[quantum-query-advantage-requires-space|Quantum Query Advantage Requires Space]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40194) | 2026-10-01
