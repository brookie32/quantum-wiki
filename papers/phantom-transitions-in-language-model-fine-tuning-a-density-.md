---
title: "Phantom Transitions in Language Model Fine-Tuning: A Density-Matrix Analysis"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.07559"
summary: "arXiv:2606.07559v3 Announce Type: replace-cross Abstract: Language models fine-tuned where the correct completion must outrank a near-synonym competitor often fail silently. The cross-entropy loss fal"
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2606.07559v3 Announce Type: replace-cross Abstract: Language models fine-tuned where the correct completion must outrank a near-synonym competitor often fail silently. The cross-entropy loss falls monotonically while the correct token never overtakes the competitor in the model's ranking. We study this across five transformer architectures from two families spanning a sixfold parameter range, on ten contexts whose correct and competing completions share substantial embedding overlap. We build an order parameter combining the predicted distribution with embedding overlap, as a density matrix because that distribution lives over a non-orthogonal basis. It decomposes additively into a signal term tracking commitment to the correct token and a drag term set by how the embedding bulk leaks probability into the score. This isolates two failure modes. In kinematic failure the signal stays too small and the model never commits. In structural failure the drag worsens during fine-tuning, so the model degrades geometrically as its loss falls. The order parameter also shows sharp jumps resembling phase transitions. We test the spontaneous-symmetry-breaking reading by tracking it after every gradient step, and rule it out. The jumps persist under LoRA even though the token embedding matrix never changes. No geometric phase transition is possible when that geometry cannot move, so the discontinuity lies entirely in the softmax readout. A few dimensionless quantities organize the trajectory across architectures. One is consistent across all five models under full fine-tuning. A second sorts architectures into two classes by their bulk embedding distribution and predicts whether LoRA alone can make a sentence commit. As a blind test, the framework predicts a held-out architecture's critical learning rate to within 2.1% of a later sweep. These results characterize this near-synonym mechanism and need recalibration before extrapolation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.07559) | 2026-08-20
