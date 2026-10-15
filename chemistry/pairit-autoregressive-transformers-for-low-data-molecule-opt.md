---
title: "PairIT: Autoregressive Transformers for Low-Data Molecule Optimization"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.19123"
summary: "arXiv:2610.19123v1 Announce Type: cross Abstract: Generating novel molecules with desired properties is a central challenge in drug discovery. Although foundational work focused on de novo generation,"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2610.19123v1 Announce Type: cross Abstract: Generating novel molecules with desired properties is a central challenge in drug discovery. Although foundational work focused on de novo generation, practical use cases require a more complex setting: conditioning on an initial seed molecule, optimizing multiple properties, and operating in data-sparse regimes. We introduce PairIT, a flexible training framework for autoregressive transformers over SMILES sequences that enables seeded generation by learning from pairs of structurally similar molecules. By leveraging matched pairs, the model learns to generate local, chemically meaningful edits that improve a property of the seed molecule. Prompt tokens extend this framework by specifying the target property, desired direction, and approximate magnitude of change. Multiple prompt tokens can be concatenated to enable multi-property optimization at inference time. For properties where pair supervision alone is insufficient, reinforcement learning post-training can further improve optimization, providing a tunable trade-off between proximity to the seed and the optimization objective. PairIT naturally supports pretraining on a large dataset and fine-tuning on a smaller dataset, which is critical for performance in data-sparse regimes. Surprisingly, we observe diminishing returns to the scale of the pretraining dataset. We demonstrate empirically on MoleculeNet and Therapeutics Data Commons datasets that, with appropriate paired-data curation, a standard transformer model of modest size (68M parameters) can achieve robust seeded molecular optimization in low-data regimes.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.19123) | 2026-10-15
