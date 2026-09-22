---
title: "Fault-Class-Matched Test Oracles for Output-Invisible Quantum Transpiler Regressions"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.24230"
summary: "arXiv:2609.24230v1 Announce Type: cross Abstract: Test oracles for quantum transpilers typically judge correctness by comparing compiled output against a reference: a statevector, a sampled distributi"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.24230v1 Announce Type: cross Abstract: Test oracles for quantum transpilers typically judge correctness by comparing compiled output against a reference: a statevector, a sampled distribution, or a unitary compared modulo global phase. A companion empirical study measures how often that choice fails. Roughly 28% of merged Qiskit transpiler bug-fixes (95% Wilson CI 19-40%) repair a fault that corrupts layout metadata, global phase, or run-to-run reproducibility while output stays correct: invisible to a black-box output-equivalence oracle by construction. This paper closes that gap with a fault-class-matched, layout-aware, width-tiered oracle family: a layout/permutation contract checker and a contract-level metamorphic relation (MR-1) for the metadata channel, a global-phase tracker for the phase channel, and a determinism runner for reproducibility. Verified from source on nine real, merged Qiskit transpiler regressions (three per channel), the output-equivalence oracle is blind throughout and the matched mechanism fires on every case. A 675-configuration sweep of the contract/metadata invariant finds no false positive. Synthetic mutant families confirm reliability at scale: 1.00 sensitivity and specificity across 36 mutants apiece for the contract/metadata and global-phase channels, and 1.00 sensitivity (95% CI 0.44-1.00) for reproducibility on the three circuits where the mutation is constructible. The contract checker costs two to six orders of magnitude less than a plain output check, the global-phase tracker is comparably cheap within its exact tier, and only the metamorphic relation carries a bounded cost. Ported natively to pytket/tket, the global-phase mechanism transfers cleanly, an identical 1.00/1.00 result with phases recovered to double-precision accuracy, evidence against a Qiskit-specific artifact.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.24230) | 2026-09-22
