---
title: "Hybrid quantum-classical attention for histopathology-based molecular profiling in data-limited cancers"
date: "2026-09-21"
updated: "2026-09-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.21115"
summary: "arXiv:2609.21115v1 Announce Type: new Abstract: Molecular profiling from routine histopathology could expand access to precision oncology when sequencing is unavailable, tissue is limited, or training"
last_verified: "2026-09-21"
review_by: "2026-12-20"
stale: false
---

arXiv:2609.21115v1 Announce Type: new Abstract: Molecular profiling from routine histopathology could expand access to precision oncology when sequencing is unavailable, tissue is limited, or training cohorts are small. We developed a hybrid quantum-classical strategy that replaces softmax attention in a transformer for histopathology-based gene expression prediction with a quantum-derived doubly stochastic matrix (QDSM). Across 29 cancer cohorts from The Cancer Genome Atlas and an independent pancreatic cancer cohort from the Clinical Proteomic Tumor Analysis Consortium, QDSM attention produced selective gains, with the largest relative improvements in smaller, data-limited cohorts, including adrenocortical carcinoma and uveal melanoma. Rather than improving transcriptome-wide performance uniformly, QDSM redistributed predictive accuracy across genes and pathways, improving biologically relevant targets in some tumor contexts while worsening others. In adrenocortical carcinoma, preferentially improved genes were enriched for adverse overall-survival associations, linking enhanced molecular inference to prognostically relevant biology. In pancreatic cancer transfer experiments, QDSM improved selected metabolic and lineage-associated genes but did not consistently improve performance under cross-cohort shift. Leave-one-cancer-out mixed-effects analysis showed that baseline molecular features predicted part of the gene-level benefit, while residuals identified cancer-specific programs that improved more or less than expected. Separate experiments on IBM quantum processors recovered the doubly stochastic matrix primitive underlying the attention mechanism. These findings position QDSM attention as a context- and target-dependent strategy for image-based molecular profiling and molecular triage when direct testing is unavailable, incomplete, or impractical.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.21115) | 2026-09-21
