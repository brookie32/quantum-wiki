---
title: "ChemGraph-XANES: An Agentic Framework for XANES Simulation and Curation"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2604.16205"
summary: "arXiv:2604.16205v3 Announce Type: replace-cross Abstract: Computational X-ray absorption near-edge structure (XANES) is widely used to interpret local coordination environments, oxidation states, and "
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

arXiv:2604.16205v3 Announce Type: replace-cross Abstract: Computational X-ray absorption near-edge structure (XANES) is widely used to interpret local coordination environments, oxidation states, and electronic structure, but large computational campaigns are often limited by workflow complexity. We present ChemGraph-XANES, a large language model (LLM)-based agentic framework that combines documentation-grounded parameter retrieval via retrieval-augmented generation (RAG), schema-constrained tool execution, deterministic FDMNES input generation, Parsl-backed execution, and provenance-aware data curation. Scripted and natural-language interfaces share a common scientific backend for structure handling, parameterization, execution, spectral extraction, and optional post-processing. We evaluate three workflow modes: documentation-grounded parameter propagation, structure-file-based execution, and composition-based execution from a chemistry-level request. Repeated trials yielded end-to-end completion in 10/10 composition-based runs, 10/10 structure-file-based runs, and 9/10 documentation-grounded RAG runs. In every RAG run, the energy-grid specification retrieved from the FDMNES manual was correctly propagated, with the single end-to-end failure occurring downstream during multi-structure handling. In a separate task-parallel demonstration, the framework retrieved 21 TiO_2 structures from the Materials Project and submitted one FDMNES calculation per structure. All calculations completed successfully, with Parsl distributing the independent tasks across the user-configured worker pool. Together, these results show that ChemGraph-XANES provides a constrained and reproducible orchestration layer for computational spectroscopy, supporting consistent execution of representative tasks, documentation-linked parameter selection, and task-parallel generation of structure-linked XANES collections.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2604.16205) | 2026-08-24
