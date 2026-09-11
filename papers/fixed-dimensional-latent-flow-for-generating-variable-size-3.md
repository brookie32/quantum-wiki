---
title: "Fixed-Dimensional Latent Flow for Generating Variable-Size 3D Molecules"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.08333"
summary: "arXiv:2609.08333v2 Announce Type: replace Abstract: In molecular discovery, molecule size is coupled to composition, structure, and other target properties. Yet most 3D generators require molecule siz"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2609.08333v2 Announce Type: replace Abstract: In molecular discovery, molecule size is coupled to composition, structure, and other target properties. Yet most 3D generators require molecule size to be specified before generation. Here, we introduce Equivariant-Free Transformer-Autoencoded Latent Flow Matching, a two-stage generative framework that relies entirely on a single fixed-dimensional molecule-level latent representation to generate variable-size molecules. The second-stage flow matching model samples this latent vector, and an autoregressive Transformer decoder then determines molecule size while generating atom types, coordinates, and chemically informative states. Canonical atom ordering and rigid-pose alignment enable standard Transformers without equivariant layers, while joint decoding of molecular geometry and an enriched chemical state enables reliable, deterministic, chemistry-guided graph recovery without requiring a learned dense pairwise bond decoder. The same fixed-dimensional latent supports unconditional and property-conditioned flow matching, while optional property supervision adds an internal ranking readout, with no separate predictor or reference calculations. On PCQM4Mv2, EF-TALFM achieves the highest fraction of molecules that are unique, training-set novel, pass sanitization and PoseBusters sanity checks, 89.4%, compared with 75.6% for UAE-3D and 69.8% for FlowMol. EF-TALFM also achieves higher measured computational throughput for training and sampling. Across ten target HOMO--LUMO gaps, internal ranking doubles the density functional theory (DFT)-verified hit rate within 0.1,eV, while preserving 97% novelty among unique verified hits. These results demonstrate that fixed-dimensional molecule-level generation followed by symmetry-resolved autoregressive realization provides a practical architecture for open-ended and property-directed 3D molecular design.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.08333) | 2026-09-11
