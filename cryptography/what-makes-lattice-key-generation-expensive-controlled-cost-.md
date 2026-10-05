---
title: "What Makes Lattice Key Generation Expensive? Controlled Cost Attribution with Structured LWR, ML-KEM, and HAETAE on Cortex-M4"
date: "2026-10-04"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2329"
summary: "End-to-end cycle counts quantify lattice key-generation time on a microcontroller, but not which implementation decisions create that cost. We develop a controlled attribution method for public struct"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

End-to-end cycle counts quantify lattice key-generation time on a microcontroller, but not which implementation decisions create that cost. We develop a controlled attribution method for public structure, candidate admission, and transform lifetime: how public data are organised, when candidate acceptance is checked, and whether transformed secret state is retained or reconstructed. On a fixed STM32L476RG Cortex-M4 target, paired runs within one executable keep the relevant secret, accepted candidate, or output key unchanged; separate measurements record resource effects. In our Bos-based structured-LWR implementation, reorganising public data exposes expansion and multiplication cost, and same-key, first-attempt comparisons show nearly additive admission and lifetime effects. We then test whether these explanations transfer across algorithms and rejection structures. In ML-KEM-512, whose KeyGen has no candidate rejection, retaining the secret's NTT-domain representation reduces cycles; a pre-specified ML-KEM-768 test preserves this direction but shows that the saving does not scale with module rank alone. HAETAE-5 tests both decisions inside a retrying KeyGen. Early checking stops rejected candidates before matrix computation, whereas deferred checking repeats matrix work across attempts and, under recomputation, rebuilds transformed secret state. The interaction grows with the retry count, while retention saves cycles at the cost of a larger KeyGen frame. Together, these experiments establish a compositional account of KeyGen cost: public structure defines the downstream computation for each candidate, while candidate admission and transform lifetime determine how many candidates execute it and how often reusable transformed representations are rebuilt. These relations yield directional predictions across the tested KeyGen structures, with paired measurements quantifying their cycle and storage consequences.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2329) | 2026-10-04
