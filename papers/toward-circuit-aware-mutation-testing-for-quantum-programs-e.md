---
title: "Toward Circuit-Aware Mutation Testing for Quantum Programs: Exact Visibility and Execution Planning"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.36976"
summary: "arXiv:2610.36976v1 Announce Type: cross Abstract: Mutation testing assesses test suites by introducing program changes and checking whether tests detect them. In quantum programs, a surviving mutant m"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2610.36976v1 Announce Type: cross Abstract: Mutation testing assesses test suites by introducing program changes and checking whether tests detect them. In quantum programs, a surviving mutant may leave program behavior unchanged, produce a change hidden by the chosen input or measurement, or remain undetected because statistical evidence is insufficient. We develop a circuit-aware framework to distinguish these causes and guide execution planning and test changes. The framework covers ideal, noiseless programs and mutations that replace one gate or subcircuit. The method traces how a mutation can affect measured outputs and combines established mathematical checks with statistical estimates. For supported cases, we establish conditions under which a test cannot reveal a mutation and exact formulas for its effect when the required state information is available. Under stated assumptions, we bound the mutation score while retaining surviving and unresolved mutants, and identify a restricted circuit family whose mutation effects admit efficient classical classification. The deliverables include a decision procedure, mathematical guarantees, worked examples of test changes and their implementation requirements, and a small-circuit reference implementation for differential expectation tests. These results help testers decide what to execute, what to change, and what remains unknown. The evidence is limited to proofs and executable examples under the ideal model.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.36976) | 2026-10-28
