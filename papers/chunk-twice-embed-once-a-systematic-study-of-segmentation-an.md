---
title: "Chunk Twice, Embed Once: A Systematic Study of Segmentation and Representation Trade-offs in Chemistry-Aware Retrieval-Augmented Generation"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2506.17277"
summary: "arXiv:2506.17277v2 Announce Type: replace-cross Abstract: The retrieval stage of retrieval-augmented generation (RAG) for scientific question answering depends on how documents are segmented and how c"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2506.17277v2 Announce Type: replace-cross Abstract: The retrieval stage of retrieval-augmented generation (RAG) for scientific question answering depends on how documents are segmented and how chunks are represented in embedding space. This dependence is especially relevant to chemistry texts, which contain dense terminology, symbolic notation, quantitative evidence, and context associated with document structure. However, benchmark-based evidence on the interaction between chunking strategy and embedding model remains limited for chemistry-specific retrieval. Using ChemQuests, a corpus of 952 question-answer pairs from 151 ChemRxiv papers across 17 chemistry subfields, we construct chunk-level, Massive Text Embedding Benchmark (MTEB)-compatible retrieval benchmarks for controlled evaluation. We first screen 41 embedding models on the external chemistry retrieval benchmarks ChemNQRetrieval and ChemHotpotQARetrieval using a geometric-mean metric at rank 10 (Geom@10), which we validate against the full retrieval-metric profile. We then evaluate shortlisted models on ChemQuests-derived tasks across five chunking strategies, seven chunk sizes, and multiple overlap settings. Embedding choice is associated with the largest observed differences in evidence retrieval, with retrieval-tuned E5, Beijing Academy of Artificial Intelligence General Embedding (BGE), and Nomic models among the strongest overall. Within the evaluated grid, medium-to-large chunks combined with fixed-token, recursive-token, or hierarchical-section chunking provide a practical starting point for the retrieval stage of chemistry-aware RAG. Low overlap was generally favored where overlap variation was evaluated.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2506.17277) | 2026-09-18
