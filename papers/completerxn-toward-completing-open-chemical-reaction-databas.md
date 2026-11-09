---
title: "CompleteRXN: Toward Completing Open Chemical Reaction Databases"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2605.00222"
summary: "arXiv:2605.00222v3 Announce Type: replace-cross Abstract: Chemical reaction datasets such as USPTO suffer from substantial incompleteness, frequently missing byproducts, co-reactants, and stoichiometr"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2605.00222v3 Announce Type: replace-cross Abstract: Chemical reaction datasets such as USPTO suffer from substantial incompleteness, frequently missing byproducts, co-reactants, and stoichiometric coefficients. This limits their applicability and reliability in downstream applications. Here, we introduce CompleteRXN, a large-scale supervised benchmark for reaction completion under realistic missing-data conditions. We construct a dataset of aligned incomplete and atom-balanced reactions by mapping USPTO records to curated mechanistic reactions. We evaluate representative baselines, including a novel encoder-decoder reaction completion model with constrained decoding, the Constrained Reaction Balancer (CRB), and a recent algorithmic method, SynRBL. On our CompleteRXN benchmark, the CRB achieves high performance across splits of increasing difficulty, reaching 99.28% equivalence accuracy on the random split and 91.71% on the extreme out-of-distribution split. SynRBL produces many balanced and chemically plausible completions, but with lower accuracy on the benchmark test splits. Across all methods, performance degrades with increasing incompleteness. We observe a substantial drop when evaluating on reactions outside the benchmark (full uncurated USPTO), highlighting the gap between benchmark performance and practical robustness and motivating future work. Data, code and models can be found at: https://github.com/Intelligent-molecular-systems/CompleteRxn-Benchmarking.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2605.00222) | 2026-11-09
