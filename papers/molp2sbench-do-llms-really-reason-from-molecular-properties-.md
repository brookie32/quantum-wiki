---
title: "MolP2SBench: Do LLMs Really Reason from Molecular Properties to Structure?"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.12522"
summary: "arXiv:2610.12522v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used in molecular discovery and structure elucidation, where decisions depend on physical observations. Ex"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2610.12522v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used in molecular discovery and structure elucidation, where decisions depend on physical observations. Existing evaluations primarily focus on end-to-end molecular reconstruction, where correct predictions do not necessarily indicate reliance on the supplied properties. We introduce MolP2SBench, a benchmark for molecular property-to-structure (P2S) reasoning in LLMs. Each task presents a masked molecular scaffold with given properties and asks the model to select the missing structure from plausible candidates. We shuffle or replace properties to test reliance on correct property-structure pairing and responsiveness to counterfactual property changes. A channel-wise leaderboard uses Property-Grounded Recovery (PGR), giving equal weight to source and counterfactual recovery. Evaluating seven models, we find that LLMs can use physical properties for structure prediction, but performance varies substantially across property types. Higher accuracy with a property does not necessarily imply greater responsiveness to it: a model may benefit more from ^1H NMR than from ^{13}C NMR, yet be less likely to change its prediction when the ^1H data is replaced. LLM performance also need not reflect the relative difficulty of these properties for human chemists. Although UV-Vis spectra provide less direct structural information than NMR spectra, Astra achieves higher accuracy with UV-Vis data than with NMR peaks. MolP2SBench supports studying how LLMs extract and use physical-property information, revealing patterns that may differ from conventional chemical intuition and providing a foundation for more reliably property-grounded models for molecular and quantum-chemical inference. Code and dataset: https://github.com/DUAL-Xiao/MolP2SBench.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.12522) | 2026-10-12
