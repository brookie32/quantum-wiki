---
title: "RxnOptBench: Benchmarking LLMs for Reaction-Condition Optimization in Organic Methodology"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.02242"
summary: "arXiv:2610.02242v1 Announce Type: new Abstract: Chemical reaction-condition optimization -- choosing the catalyst, ligand, solvent, reagent, temperature, time, and atmosphere that jointly maximize yie"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.02242v1 Announce Type: new Abstract: Chemical reaction-condition optimization -- choosing the catalyst, ligand, solvent, reagent, temperature, time, and atmosphere that jointly maximize yield and stereoselectivity -- is a central, judgement-laden subtask of organic methodology research that large language models are increasingly expected to support. Yet existing chemistry benchmarks evaluate reaction-class labelling, retrosynthesis, or SMILES manipulation, and do not ask models to read a real condition-screening table and pick the best set. We introduce RxnOptBench, a benchmark whose every option and precedent is a real wet-lab entry mined from the optimization tables of organic-methodology papers published in 2025, graded by a continuous relative score derived from a declared headline utility that combines reported yield with enantiomeric excess (ee), diastereomeric ratio (dr), and regioisomeric ratio (rr), and equipped with a paired precedents-vs-no-precedents design that isolates in-context use of literature evidence from parametric memorization. Across nine frontier LLMs and three Chemistry LLMs, even the best models leave substantial headroom: chemistry-specialized models fall to the random-baseline floor on multi-axis selection, while open-weight models have closed most of the gap to proprietary frontier models. We release the final human-reviewed benchmark test set and evaluation code.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.02242) | 2026-10-05
