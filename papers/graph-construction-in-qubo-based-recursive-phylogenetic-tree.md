---
title: "Graph construction in QUBO-based recursive phylogenetic tree reconstruction"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.16640"
summary: "arXiv:2609.16640v1 Announce Type: cross Abstract: Molecular sequence data are used to reconstruct evolutionary relationships among taxa, but reconstruction accuracy depends not only on the tree-buildi"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2609.16640v1 Announce Type: cross Abstract: Molecular sequence data are used to reconstruct evolutionary relationships among taxa, but reconstruction accuracy depends not only on the tree-building method but also on how pairwise sequence relationships are represented. We evaluated sequence-to-affinity representations in a recursive normalized-cut (Ncut) framework whose graph-partitioning subproblems were formulated as quadratic unconstrained binary optimization (QUBO) models and solved using Simulated Bifurcation. Using simulated amino-acid and nucleotide datasets spanning multiple tree-generation settings and evolutionary divergence, we compared normalized bit-score affinities with representations derived from transformed sequence similarities and evolutionary distances, examined post-swap refinement, and used neighbor joining (NJ) as a distance-based comparator. Affinity representation substantially affected internal split recovery, particularly for nucleotide data. JC69-based local affinities maintained comparatively high accuracy as divergence increased, whereas normalized bit-score and BLAST-derived kernel representations declined more markedly. Post-swap refinement generally improved recovery, but not consistently across individual reconstructions. NJ achieved higher mean split recovery than corresponding recursive Ncut reconstructions for WAG and JC69 distances across all evaluated conditions, whereas recursive Ncut outperformed NJ for BLAST-derived logarithmic distances under some conditions. These results show that graph construction is an important determinant of recursive Ncut-based phylogenetic reconstruction. A representation that performs well within Ncut does not necessarily provide the most accurate use of the underlying pairwise distances. Pairwise representation, affinity transformation, optimization, and recursive tree construction should therefore be evaluated jointly.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.16640) | 2026-09-16
