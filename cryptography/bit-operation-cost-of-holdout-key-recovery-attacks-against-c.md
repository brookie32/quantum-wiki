---
title: "Bit Operation Cost of ``Holdout'' Key-Recovery Attacks Against Classic McEliece"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1786"
summary: "We present a self-contained conditional arithmetic model and algorithmic specification for a prospective key-recovery attack on binary Goppa codes, combining the Holdout construction with heterogeneou"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

We present a self-contained conditional arithmetic model and algorithmic specification for a prospective key-recovery attack on binary Goppa codes, combining the Holdout construction with heterogeneous Hasse multiplicities, Lucas-minimal derivative levels, an augmented binary block-Wiedemann supplier, and reconstruction from local flags. The first two reductions give exact, dimension-guaranteed attack-parameter configurations for every Classic McEliece parameter set. We derive the sparse operator, safe-rank-bound sequence state, a supplier tally charging one attempt per relation batch, higher-flag arithmetic, and the downstream solve performed for every guess. At the selected configurations, modeled affine / dense totals range from 2^{172.13} to 2^{235.09} gates, while projective/nested variants range from 2^{146.29} to 2^{207.83}. For mceliece348864, a configuration with c=7 gives 2^{142.15} modeled gates but needs 2^{61.7} bits of retained state before recursive solver scratch. An exhaustive scan of 19,338 admitted singleton (one-position holdout) configurations finds a 2^{114.35} supplier-complexity floor within the fixed one-attempt-per-batch model; no downstream-only improvement can cross it. A synthetic experiment heuristically supports the Frobenius-phase balance test, but no public pure cross-pairing is known. None of the tallies is an established break: reliable small-field Krylov yield, higher-flag recovery from the priced truncated block, binary reconstruction, cross-anchor independence, and memory-aware implementation remain open. This manuscript is currently a living tracking document.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1786) | 2026-08-24
